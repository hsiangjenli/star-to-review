# 🚀 jina-ai/vectordb

A Pythonic vector database.
- Uses `docarray` as the document schema
- Vectordb can function as both a server and a client, supporting communication protocols such as `gRPC`, `HTTP`, and `WebSocket`
- Retrieval logic is based on the `docarray` schema
- Data is persisted in the ***`workspace`*** folder

## Scaling the Database
- **Shards** - Enables horizontal scaling.
- **Replicas** - Provides fault tolerance.

## Search Algorithms
- **InMemoryExactNNVectorDB** - Performs exhaustive search for each query
- **HNSW** - Utilizes the Hierarchical Navigable Small World (HNSW) algorithm
