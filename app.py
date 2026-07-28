from fastapi import FastAPI
from pydantic import BaseModel

from document_loader import load_pdf
from embeddings import get_embedding
from vector_store import create_vector_db, load_db
from chatbot import ask_question

app = FastAPI()

documents = load_pdf("data/annual_report.pdf")

embedding = get_embedding()

create_vector_db(documents, embedding)

db = load_db(embedding)

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):

    answer = ask_question(
        db,
        query.question
    )

    return {
        "answer": answer
    }
