from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.embeddings import HuggingFaceEmbeddings

# Sample dictionary with file data
# embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
embedding_model = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl")

# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def split_documents_dict(file_data_dict):
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Convert dictionary into a list of Document objects
    documents = [Document(page_content=data, metadata={"source": file_name}) for file_name, data in file_data_dict.items()]

    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    # Split documents
    split_docs = text_splitter.split_documents(documents)

    # Check results
    # for doc in split_docs:
        # print(f"Source: {doc.metadata['source']}, Content: {doc.page_content}\n")
    # vectorstore = Chroma.from_documents(split_docs, embedding_model)

    valid_texts = [doc.page_content for doc in split_docs if doc.page_content.strip() != ""]
    valid_metadatas = [doc.metadata for doc in split_docs if doc.page_content.strip() != ""]

    if not valid_texts:
        print("Error: No valid texts available for embedding!")
    # embeddings = [model.encode(doc.page_content) for doc in split_docs if doc.page_content.strip() != ""]

    vectorstore = Chroma(embedding_function=embedding_model)
    vectorstore.add_texts(valid_texts, metadatas=valid_metadatas)

    return vectorstore

def extract_query_results(vectorstore, query):
    # Setup retrieval system
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=vectorstore.as_retriever())

    # Ask a question
    query = "What is the main concept discussed in these documents?"
    response = qa.run(query)

    print(response)

