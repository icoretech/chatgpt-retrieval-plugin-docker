import toml
import sys


def remove_unused_dependencies(provider):
    # Define the dependencies for each provider
    dependencies = {
        "pinecone": ["weaviate-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "weaviate": ["pinecone-client", "pymilvus", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "zilliz": ["pinecone-client", "weaviate-client", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "milvus": ["pinecone-client", "weaviate-client", "qdrant-client", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "qdrant": ["pinecone-client", "weaviate-client", "pymilvus", "redis", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "redis": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "chromadb", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "llamaindex": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "chromadb", "redis", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "chroma": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "llama-index", "redis", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "azure": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "llama-index", "redis", "chromadb", "supabase", "psycopg2", "psycopg2cffi", "pgvector"],
        "supabase": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "llama-index", "azure-identity", "azure-search-documents", "psycopg2", "psycopg2cffi", "pgvector"],
        "postgres": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "llama-index", "azure-identity", "azure-search-documents", "supabase"],
        "analyticdb": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "llama-index", "azure-identity", "azure-search-documents", "supabase"]
    }

    # Read the pyproject.toml file
    with open("chatgpt-retrieval-plugin/pyproject.toml", "r") as file:
        content = toml.load(file)

    # Remove the unused dependencies
    for dependency in dependencies[provider]:
        if dependency in content["tool"]["poetry"]["dependencies"]:
            del content["tool"]["poetry"]["dependencies"][dependency]

    # Write the modified content back to the file
    with open("chatgpt-retrieval-plugin/pyproject.toml", "w") as file:
        toml.dump(content, file)


def add_dependency_if_not_present(package, version):
    # Read the pyproject.toml file
    with open("chatgpt-retrieval-plugin/pyproject.toml", "r") as file:
        content = toml.load(file)

    # Check if the package is already present in the dependencies
    if "dependencies" not in content["tool"]["poetry"]:
        content["tool"]["poetry"]["dependencies"] = {}

    dependencies = content["tool"]["poetry"]["dependencies"]
    if package not in dependencies:
        dependencies[package] = version

    # Write the modified content back to the file
    with open("chatgpt-retrieval-plugin/pyproject.toml", "w") as file:
        toml.dump(content, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python manage_deps.py <provider>")
        sys.exit(1)

    provider = sys.argv[1]
    remove_unused_dependencies(provider)
    # for https://github.com/openai/chatgpt-retrieval-plugin/issues/292#issuecomment-1568588920
    add_dependency_if_not_present("loguru", ">=0.5.0")
