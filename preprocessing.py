import re
from langchain_core.documents import Document
from loaders import load_documents


def clean_text(text):
    if not text:
        return ""

    text = text.replace("\t", " ")
    text = re.sub(r"[ ]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text.strip()


def preprocess_documents(documents):

    cleaned_documents = []

    for doc in documents:

        cleaned_documents.append(
            Document(
                page_content=clean_text(doc.page_content),
                metadata=doc.metadata
            )
        )

    return cleaned_documents


if __name__ == "__main__":

    documents = load_documents()

    cleaned_documents = preprocess_documents(documents)

    print(cleaned_documents[0].page_content[:1000])