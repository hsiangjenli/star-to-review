# 🚀 petercat-ai/petercat

- https://www.youtube.com/@petercat-ai
- Support one click to deploy to AWS

<!--  -->
The most interesting feature of this project is you can input any github repo into and create an AI agent specifically tailored to that repo. The AI agent also can open an issue on the repo. Some people may ask questions on the repo, and the AI agent can answer the questions automatically based on the repo's content. 

## Run Locally

Ensure that can successfully generate standalone folder.

```shell
# client/next.config.js
module.exports = {
  output: "standalone",
```

```shell
docker build -t petercat-server -f docker/Dockerfile.vercel .
```

```bash
docker run --rm -it -p 3000:3000 -e NEXT_PUBLIC_API_DOMAIN=http://localhost:3000 petercat-server:latest
```

## Result
A lot of errors when running entering the website. (I don't know how to fix it...)