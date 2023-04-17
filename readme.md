# dolly server

* simple dolly server. 
* servers LLM. 

```bash
docker build -t dollyserver:latest .

# share a folder with the docker container, I have hugging face .cache folder 
# on my bare metal server in /mnt/data/huggingface
mkdir -p /mnt/data/huggingface
docker run   -v /mnt/data/huggingface:/mnt/data/huggingface -p 8005:8005 dollyserver:latest
docker run --gpus 1  -v /mnt/data/huggingface:/mnt/data/huggingface -p 8005:8005 dollyserver:latest
```

## using it with this frontend. 
* https://github.com/garland3/mysimplechatbot

