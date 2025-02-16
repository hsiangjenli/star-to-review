# 🚀 frdel/agent-zero

- https://github.com/frdel/agent-zero/tree/main
- It can execute commands and code, cooperate with other agent instances.
- Persistent memory.
- It can write its own code and use the terminal to create and utilize its own tools as needed.
- Default tools include: online search, memory features, communication (with the user and other agents), and code/terminal execution.
- Even with small models, it remains compatible and reliable.
- The terminal interface is real-time streaming and interactive. You can stop and intervene at any point.

## Run Locally

```shell
docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run
```
- http://localhost:50001

## Result

- I gave it a command
    ```
    Write a technical blog post about microservices and save as markdown file into home dir and file name is test.md
    ```

1. The agent will take the input as a query and try to retrieve relevant information to better respond to it.
For example, the agent retrieves a blog post about microservices.

    ![20250216142647](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20250216142647.png)

1. It also finds the necessary tools and solutions to write a blog post.

    ![20250216142658](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20250216142658.png)

1. Generating ...

    ![20250216142709](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20250216142709.png)

1. Even though the agent had a small issue saving the file, it was still able to solve the problem by itself.

    ![20250216142721](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20250216142721.png)

    ![20250216142731](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20250216142731.png)

    ![20250216142743](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20250216142743.png)