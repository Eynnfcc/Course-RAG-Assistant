from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader


def load_documents(data_folder="data"):
    data_folder = Path(data_folder)

    pdf_files = list(data_folder.glob("**/*.pdf"))

    all_documents = []

    for pdf in pdf_files:
        print(f"Loading: {pdf}")

        loader = PyMuPDFLoader(str(pdf))
        documents = loader.load()

        all_documents.extend(documents)

    print(f"\nLoaded {len(all_documents)} pages.")

    return all_documents


if __name__ == "__main__":

    documents = load_documents()

    for i in range(min(5, len(documents))):
        print(f"\n{'=' * 50}")
        print(f"Page {i + 1}")
        print(f"{'=' * 50}\n")
        print(documents[i].page_content[:1000])