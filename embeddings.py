from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from loaders import load_documents
from preprocessing import preprocess_documents
from chunking import chunk_documents


def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store


if __name__ == "__main__":

    documents = load_documents()

    cleaned_documents = preprocess_documents(documents)

    chunks = chunk_documents(cleaned_documents)

    vector_store = create_vector_store(chunks)

    vector_store.save_local("vector_store")

    print(f"Original Pages : {len(cleaned_documents)}")
    print(f"Total Chunks   : {len(chunks)}")

    print("\nFAISS vector database created successfully!")
    print("Saved in: vector_store/")