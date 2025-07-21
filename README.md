<!--
README for the OpenRelik Worker Template

This file provides instructions on how to use this template to create a new OpenRelik worker.
The placeholder `TEMPLATEWORKERNAME` needs to be replaced with the actual name of your worker.
The `bootstrap.sh` script is designed to help with this process.
-->

1.  **Bootstrap your new worker:**
    Run the `bash bootstrap.sh` script located in the root of this template. This script will guide you through renaming `TEMPLATEWORKERNAME` to your chosen worker name throughout the project files (e.g., directory names, Python files, etc.).
2.  **Update this README:**
    After bootstrapping, manually replace all remaining instances of `TEMPLATEWORKERNAME` in this `README.md` file with your actual worker name. Also, fill in the description section below.
3.  **Write Tests:**
    Before or alongside developing your worker's core logic, start creating tests.
    *   **Unit Tests:** Create unit tests for individual functions and classes within your worker's `src` directory. Place these in the `tests/` directory.
    *   Refer to the "Test" section below for instructions on how to run your tests.
4.  **Implement Worker Logic:**
    Fill in the `src/tasks.py` file (and any other necessary modules) with the core functionality of your worker.
5.  **Add LICENSE file:**
    Add a License file to the repository.

# Openrelik worker TEMPLATEWORKERNAME
## Description
**TODO:** Enter a comprehensive description of your worker here. Explain its purpose, what kind of tasks it handles, and any specific functionalities or integrations it provides.

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
uv sync --group test
uv run pytest -s --cov=.
```
