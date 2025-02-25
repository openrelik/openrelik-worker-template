## NOTE: Bootstrap the new worker with `bash bootstrap.sh`!

# Openrelik worker TEMPLATEWORKERNAME
## Description
Enter a good description of your worker here.

## Deploy
Add the below configuration to the OpenRelik docker-compose.yml file.

```
openrelik-worker-TEMPLATEWORKERNAME:
    container_name: openrelik-worker-TEMPLATEWORKERNAME
    image: ghcr.io/openrelik/openrelik-worker-TEMPLATEWORKERNAME:latest
    restart: always
    environment:
      - REDIS_URL=redis://openrelik-redis:6379
      - OPENRELIK_PYDEBUG=0
    volumes:
      - ./data:/usr/share/openrelik/data
    command: "celery --app=src.app worker --task-events --concurrency=4 --loglevel=INFO -Q openrelik-worker-TEMPLATEWORKERNAME"
    # ports:
      # - 5678:5678 # For debugging purposes.
```

## Test
```
pip install poetry
poetry install --with test --no-root
poetry run pytest --cov=. -v
```