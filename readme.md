# Open source LLM server

* ~~simple dolly server. ~~
* More models exists, so this is a generic hugging face lllm server. 
* servers LLM. 

```bash
docker build -t llmserver:latest .

# share a folder with the docker container, I have hugging face .cache folder 
# on my bare metal server in /mnt/data/huggingface
mkdir -p /mnt/data/huggingface
docker run   -v /mnt/data/huggingface:/mnt/data/huggingface -p 8005:8005 llmserver:latest
docker run --gpus 1  -v /mnt/data/huggingface:/mnt/data/huggingface -p 8005:8005 llmserver:latest
```

## using it with this frontend. 
* https://github.com/garland3/mysimplechatbot

## interesting models

The non-commercial use models are only moderately interesting.
The commercial use models are very interesting since you could leverage the for a business. 

There are bigger models than these 3B ones, but I'm jsut putting the 3B ones here.

* Dolly databricks/dolly-v2-3b
* Sabilitylm-base stabilityai/stablelm-base-alpha-3b