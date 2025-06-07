import chromadb

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="chroma_db")

# Create collection
collection = chroma_client.get_or_create_collection(name="document_store")

# Function to store documents

def store_document(file_name, page, paragraph, content):
    collection.add(
        documents=[content],
        metadatas=[{"file_name": file_name, "page": page, "paragraph": paragraph}],
        ids=[f"{file_name}_{page}_{paragraph}"]
    )

# Function to query documents
def search_documents(query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    return results["documents"]