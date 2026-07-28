from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

def ask_question(db, question):

    docs = db.similarity_search(question, k=3)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Context:

{context}

Question:

{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content
