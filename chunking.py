from langchain_text_splitters import RecursiveCharacterTextSplitter

from loaders import load_documents
from preprocessing import preprocess_documents


def chunk_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=250,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":

    documents = load_documents()

    cleaned_documents = preprocess_documents(documents)

    chunks = chunk_documents(cleaned_documents)

    print(f"Original Pages : {len(cleaned_documents)}")
    print(f"Total Chunks   : {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)

    print("\n" + "=" * 60 + "\n")

    print("Metadata:")
    print(chunks[0].metadata)

    long_pages = 0

    for doc in cleaned_documents:
      if len(doc.page_content) > 500:
        long_pages += 1

    print(f"Pages longer than 500 characters: {long_pages}")

    for i in range(5):
     print(f"Chunk {i+1}: {len(chunks[i].page_content)} characters")