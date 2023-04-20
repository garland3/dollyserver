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

