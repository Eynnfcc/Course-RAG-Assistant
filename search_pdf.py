from loaders import load_documents


documents = load_documents()

keywords = [
    "number comparison",
    "comparison",
    "comparator"
]


for i, doc in enumerate(documents):

    text = doc.page_content.lower()

    for word in keywords:

        if word in text:
            print("="*60)
            print("FOUND:", word)
            print("PAGE:", doc.metadata)
            print(text[:500])