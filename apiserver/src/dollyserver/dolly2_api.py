import os
import numpy as np
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from transformers import (AutoModelForCausalLM, AutoTokenizer, PreTrainedModel,
                          PreTrainedTokenizer)

# Use this variable as the default API key or read from the environment.
DEFAULT_API_KEY = "xx1asafs9uaxlkQe32qasdofadsouf@@@adosucaeoru#@!n"
API_KEY = os.environ.get("API_KEY", DEFAULT_API_KEY)  # Override API_KEY if the environment variable is set.


app = FastAPI()

modelname = "databricks/dolly-v2-3b"
tokenizer = AutoTokenizer.from_pretrained(modelname, padding_side="left")
model = AutoModelForCausalLM.from_pretrained(modelname, device_map="auto", trust_remote_code=True)
print("Model loaded.")

PROMPT_FORMAT = """Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
"""

class Instruction(BaseModel):
    instruction: str

def generate_response(instruction: str, *, model: PreTrainedModel, tokenizer: PreTrainedTokenizer, 
                      do_sample: bool = True, max_new_tokens: int = 2000, top_p: float = 0.92, top_k: int = 0, **kwargs) -> str:
    input_ids = tokenizer(PROMPT_FORMAT.format(instruction=instruction), return_tensors="pt").input_ids.to("cuda")

    response_key_token_id = tokenizer.encode("### Response:")[0]
    end_key_token_id = tokenizer.encode("### End")[0]

    gen_tokens = model.generate(input_ids, pad_token_id=tokenizer.pad_token_id, eos_token_id=end_key_token_id,
                                do_sample=do_sample, max_new_tokens=max_new_tokens, top_p=top_p, top_k=top_k, **kwargs)[0].cpu()

    response_positions = np.where(gen_tokens == response_key_token_id)[0]

    if len(response_positions) >= 0:
        response_pos = response_positions[0]
        
        end_pos = None
        end_positions = np.where(gen_tokens == end_key_token_id)[0]
        if len(end_positions) > 0:
            end_pos = end_positions[0]

        return tokenizer.decode(gen_tokens[response_pos + 1 : end_pos]).strip()

    return "No response found."

@app.post("/run")
async def run(instruction: Instruction, api_key: str = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    response = generate_response(instruction.instruction, model=model, tokenizer=tokenizer)
    return {"response": response}

# conda activate dollytest
# uvicorn dolly2_api:app --host 0.0.0.0 --port 8000
