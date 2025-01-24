# 🚀 TransformerOptimus/SuperAGI


## Understanding the Project

### `Entire Project`
```shell
gitingest https://github.com/TransformerOptimus/SuperAGI -e ".github/, gui/, nginx/, /static/, tests/, /workspace, *.md, *.MD"
```

### `Setup Docker`

The project uses Docker for containerization. Which can separate the application into three parts:
1. `Dockerfile` - Backend
2. `DockerfileCelery` - 
3. `DockerfileRedis` - 

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


## Run Locally

```shell
git clone https://github.com/TransformerOptimus/SuperAGI.git 
```

```shell
docker compose -f docker-compose.yaml up --build
```