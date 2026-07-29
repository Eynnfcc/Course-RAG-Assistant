import os
import re

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from retriever import load_retriever

# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found. Make sure it exists in your .env file."
    )

# ==========================================================
# LOAD RETRIEVER
# ==========================================================

retriever = load_retriever()

# ==========================================================
# LOAD GEMINI MODEL
# ==========================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=api_key,
    temperature=0
)

print("=" * 60)
print("Running:", __file__)
print("Model:", llm.model)
print("=" * 60)


# ==========================================================
# QUESTION PREPROCESSING
# ==========================================================

def preprocess_question(question):

    question = question.lower().strip()
    question = re.sub(r"\s+", " ", question)

    return question


# ==========================================================
# ASK QUESTION
# ==========================================================

def ask_question(question):

    question = preprocess_question(question)

    docs = retriever.invoke(question)
    print("=" * 60)
    print("QUESTION:", question)
    print("DOCUMENTS FOUND:", len(docs))

    for i, doc in enumerate(docs):
            print("\n" + "-" * 30)
            print(f"Document {i+1}")
            print("-" * 30)
            print(doc.page_content[:1200])

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an expert university teaching assistant.

Your ONLY source of knowledge is the provided course material.

Rules:

1. Answer ONLY from the retrieved course material.

2. The student's wording does not have to exactly match the slides.

3. Understand:
- abbreviations
- spelling mistakes
- singular/plural
- synonyms
- paraphrases

4. If the answer is spread across multiple retrieved passages,
combine them into one coherent answer.

5. If the slides describe a concept without explicitly defining it,
infer the definition only if it is directly supported by the retrieved text.

6. Never invent facts.

7. Never use outside knowledge.

8. If multiple retrieved passages discuss the same topic,
combine them.

9. Ignore irrelevant retrieved passages.

10. If the answer truly does not exist in the retrieved context, reply exactly:

"I couldn't find the answer in the course material."

Answer in a clear educational style.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.text


# ==========================================================
# TERMINAL APP
# ==========================================================

if __name__ == "__main__":

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        try:
            answer = ask_question(question)

            print("\nAnswer:\n")
            print(answer)

        except Exception as e:
            print("\nERROR:")
            print(e)