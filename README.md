# ChatGPT Retrieval Plugin Docker Image

This repository hosts an automated build system for creating Docker images of the [ChatGPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin), a ChatGPT plugin by OpenAI.

## Overview

The build system is set up to automatically pull the latest code from the `main` branch of the ChatGPT Retrieval Plugin project, package it into a Docker image, and publish the AMD64 image. The build system also creates optimized images for each supported vector database provider, removing unused dependencies to reduce the size of the image and improve performance.

## Usage

To pull a Docker image, use the following command:

```bash
docker pull ghcr.io/icoretech/chatgpt-retrieval-plugin-docker:<tag>
```

Replace `<tag>` with the specific version you wish to pull.
If you want to pull an image optimized for a specific vector database provider, use the provider's name as the tag. For example, to pull the image optimized for Pinecone, use `pinecone-<commit_sha>-<timestamp>` as the tag.

## Supported Vector Database Providers

The build system creates optimized images for the following vector database providers:

- Pinecone
- Weaviate
- Zilliz
- Milvus
- Qdrant
- Redis
- LlamaIndex
- Chroma
- Azure
- Supabase
- Postgres

## License

The Docker images and the code in this repository are released under [MIT License](LICENSE).

Please note that the ChatGPT Retrieval Plugin project has its own license, which you should review if you plan to use, distribute, or modify the code.
