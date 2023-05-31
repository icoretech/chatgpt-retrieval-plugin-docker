import toml
import sys

TOML_FILE_PATH = "chatgpt-retrieval-plugin/pyproject.toml"
DEPENDENCIES_KEY = "tool.poetry.dependencies"


class DependencyManager:
    def __init__(self, toml_file_path):
        self.toml_file_path = toml_file_path
        self.content = self.read_toml_file()
        self.dependencies = {
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
            "analyticdb": ["pinecone-client", "weaviate-client", "pymilvus", "qdrant-client", "redis", "llama-index", "azure-identity", "azure-search-documents", "supabase", "psycopg2", "pgvector"]
        }

    def read_toml_file(self):
        with open(self.toml_file_path, "r") as file:
            return toml.load(file)

    def write_toml_file(self):
        with open(self.toml_file_path, "w") as file:
            toml.dump(self.content, file)

    def remove_unused_dependencies(self, provider):
        for dependency in self.dependencies[provider]:
            if dependency in self.content[DEPENDENCIES_KEY]:
                del self.content[DEPENDENCIES_KEY][dependency]

    def add_dependency_if_not_present(self, package, version):
        if package not in self.content[DEPENDENCIES_KEY]:
            self.content[DEPENDENCIES_KEY][package] = version


def main():
    if len(sys.argv) != 2:
        print("Usage: python manage_deps.py <provider>")
        sys.exit(1)

    provider = sys.argv[1]
    manager = DependencyManager(TOML_FILE_PATH)
    manager.remove_unused_dependencies(provider)

    # for https://github.com/openai/chatgpt-retrieval-plugin/issues/292#issuecomment-1568588920
    manager.add_dependency_if_not_present("loguru", ">=0.5.0")

    manager.write_toml_file()


if __name__ == "__main__":
    main()
