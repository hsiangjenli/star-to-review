# 🚀 TransformerOptimus/SuperAGI

## Review
- [x] Understand the project structure ***@2025-01-26***
- [x] Set up Docker environment and run the application locally ***@2025-01-26***
- [ ] Analyze and understand the agent's functionality and workflow

## Understanding the Project

### `Entire Project`
```shell
gitingest https://github.com/TransformerOptimus/SuperAGI -e ".github/, gui/, nginx/, /static/, tests/, /workspace, *.md, *.MD"
```

### `Setup Docker`

The project uses Docker for containerization. Which can separate the application into three parts:
1. `Dockerfile` - Backend
2. `DockerfileCelery` - Celery (Task Queue Worker)
3. `DockerfileRedis` - Redis (Message Broker and Cache)

```shell
gitingest https://github.com/TransformerOptimus/SuperAGI -i "Dockerfile*, docker*.yaml"
```

```yaml
Directory structure:
└── TransformerOptimus-SuperAGI/
    ├── docker-compose.yaml
    ├── DockerfileCelery
    ├── DockerfileRedis
    ├── Dockerfile
    ├── docker-compose.image.example.yaml
    ├── docker-compose-dev.yaml
    └── Dockerfile-gpu
```


## Run Locally (Not Working as Expected)

### First, clone the repository

Due to the original repository not being updated (some errors), **sahilk0108** has forked the repository and made some changes to the code. 

```shell
git clone https://github.com/sahilk0108/SuperAGI.git
```

### Copy the `config_template.yaml` to `config.yaml`
```shell
cp config_template.yaml config.yaml
```

### Run the following command to start the project

```shell
docker compose -f docker-compose.yaml up --build
```

### Access the application at `http://localhost:3000`

I already setup the correct API key in the `config.yaml` file. But, the application is not working as expected. 

```python
celery-1           | [2025-01-26 09:23:08,405: WARNING/ForkPoolWorker-9]  
celery-1           | [2025-01-26 09:23:08,405: WARNING/ForkPoolWorker-9] 1184
celery-1           | [2025-01-26 09:23:08,664: INFO/ForkPoolWorker-9] error_code=invalid_api_key error_message='Incorrect API key provided: YOUR_OPE*****_KEY. You can find your API key at https://platform.openai.com/account/api-keys.' error_param=None error_type=invalid_request_error message='OpenAI API error received' stream_error=False
celery-1           | 2025-01-26 09:23:08 UTC - Super AGI - INFO - [/app/superagi/llms/openai.py:108] - OpenAi AuthenticationError:
celery-1           | [2025-01-26 09:23:08,664: INFO/ForkPoolWorker-9] OpenAi AuthenticationError:
celery-1           | 2025-01-26 09:23:08 UTC - Super AGI - INFO - [/app/superagi/llms/openai.py:108] - Incorrect API key provided: YOUR_OPE*****_KEY. You can find your API key at https://platform.openai.com/account/api-keys.
```

![20250216142601](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20250216142601.png)