import toml
import sys
from typing import Dict, List, Any

# Define the dependencies to be removed for each provider
DEPENDENCIES: Dict[str, List[str]] = {
    "pinecone": ["weaviate-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "weaviate": ["pinecone-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "zilliz": ["pinecone-client", "weaviate-client", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "milvus": ["pinecone-client", "weaviate-client", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "qdrant": ["pinecone-client", "weaviate-client", "pymilvus", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "redis": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "chroma": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "llamaindex": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "chromadb", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "azure": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "supabase", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "supabase": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "psycopg2", "psycopg2cffi", "pgvector", "elasticsearch"],
    "postgres": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "elasticsearch"],
    "analyticdb": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "pgvector", "elasticsearch"],
    "elasticsearch": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"]
}


def read_toml(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r") as file:
        content = toml.load(file)
    print(f"Read content from {file_path}.")
    return content


def write_toml(file_path: str, content: Dict[str, Any]) -> None:
    with open(file_path, "w") as file:
        toml.dump(content, file)
    print(f"Written changes to {file_path}.")


def remove_unused_dependencies(provider: str, content: Dict[str, Any]) -> None:
    if provider not in DEPENDENCIES:
        raise ValueError(f"Provider {provider} not found.")

    removed_deps = []

    # Remove the unused dependencies
    for dependency in DEPENDENCIES[provider]:
        if dependency in content["tool"]["poetry"]["dependencies"]:
            del content["tool"]["poetry"]["dependencies"][dependency]
            removed_deps.append(dependency)

    print(
        f"Removed {len(removed_deps)} dependencies for provider {provider}: {', '.join(removed_deps)}")


def add_dependency_if_not_present(package: str, version: str, content: Dict[str, Any]) -> None:
    # Check if the package is already present in the dependencies
    if "dependencies" not in content["tool"]["poetry"]:
        content["tool"]["poetry"]["dependencies"] = {}

    dependencies = content["tool"]["poetry"]["dependencies"]
    if package not in dependencies:
        dependencies[package] = version
        print(f"Added dependency: {package} with version {version}")
    else:
        print(
            f"Dependency {package} already exists with version {dependencies[package]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python manage_deps.py <provider>")
        sys.exit(1)

    provider = sys.argv[1]
    file_path = "chatgpt-retrieval-plugin/pyproject.toml"
    content = read_toml(file_path)
    remove_unused_dependencies(provider, content)
    # add_dependency_if_not_present("loguru", ">=0.5.0", content)
    write_toml(file_path, content)
