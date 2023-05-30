# 💻 ChatGPT Retrieval Plugin Docker Image

 This repository hosts an automated build system for creating 🐳 Docker images of the [ChatGPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin), a ChatGPT plugin by OpenAI. The built Docker images are also hosted in this repository for easy access and usage.

## 📖 Overview

The build system automates the process of pulling the latest code from the main branch of the ChatGPT Retrieval Plugin project, packaging it into a Docker image, and publishing the image. The images are optimized for different vector database providers, resulting in improved performance and reduced image size.

⚡️ **New**: We now have a Helm chart available for deploying the ChatGPT Retrieval Plugin! Check it out [here](https://github.com/icoretech/helm) for easy deployment and management of the plugin.

## 🚀 Supported Vector Database Providers

The build system creates optimized images for the following vector database providers:

[![Matrix Badge](https://github-actions.40ants.com/icoretech/chatgpt-retrieval-plugin-docker/matrix.svg)](https://github.com/icoretech/chatgpt-retrieval-plugin-docker/actions/workflows/build.yml)

## 💡 Usage

The idea is to use these images as a base to further customize your running instances.

To pull a Docker image, use the following command:

```bash
docker pull ghcr.io/icoretech/chatgpt-retrieval-plugin-docker:<tag>
```

Replace `<tag>` with the specific version you wish to pull.
To choose an image optimized for a particular vector database provider, use the provider's name as the tag.

For example, to pull the Pinecone optimized image, use `pinecone-<commit_sha>-<timestamp>` as the tag.

You can find the available tags on the [GitHub Packages page](https://github.com/icoretech/chatgpt-retrieval-plugin-docker/pkgs/container/chatgpt-retrieval-plugin-docker) for this repository.

While it is possible to run images as-is without customization, it is strongly recommended to do so in environments where you can properly configure and manage the runtime, such as Helm or Docker Compose setups or if you are an implementator.

## 📋 Example

```Dockerfile
# example/Dockerfile.custom
# docker build -t chatgpt-retrieval-plugin-docker:custom -f example/Dockerfile.custom .
FROM ghcr.io/icoretech/chatgpt-retrieval-plugin-docker:redis-9969191-1685433326

# Set the necessary environment variables
ENV DATASTORE redis
ENV BEARER_TOKEN 5841c60f9371441121997f95c1c5f3673c10b3e4
ENV OPENAI_API_KEY sk-xxxxxx
ENV REDIS_HOST myredishost
# ...

COPY config/logo.png /code/.well-known/logo.png
COPY config/openapi.yaml /code/.well-known/openapi.yaml
COPY config/ai-plugin.json /code/.well-known/ai-plugin.json
```

## 📄 License

The Docker images and the code in this repository are released under [MIT License](LICENSE).

Please note that the ChatGPT Retrieval Plugin project has its own license, which you should review if you plan to use, distribute, or modify the code.
