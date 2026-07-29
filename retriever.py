from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def load_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 12,          # Number of documents returned
        "fetch_k": 20,   # Number of candidates to consider
        "lambda_mult": 0.7
    }
)

    return retriever


def retrieve_documents(question):
    retriever = load_retriever()
    return retriever.invoke(question)


if __name__ == "__main__":

    query = "Explain De Morgan's Law."

    results = retrieve_documents(query)

    print(f"Retrieved {len(results)} documents.\n")

    for i, doc in enumerate(results, start=1):

        print("=" * 60)
        print(f"Result {i}")
        print("=" * 60)

        print(doc.page_content)

        print("\nSource:", doc.metadata["source"])
        print("Page:", doc.metadata["page"] + 1)