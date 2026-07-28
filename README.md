# AI-Financial-Assistant

Step 1
pip install -r requirements.txt


Step 2
uvicorn app:app --reload


Step 3
open. - http://127.0.0.1:8000/docs

Step 4
{
  "question":"What was the company's total revenue?"
}


project tree structure - 


AI-Financial-Assistant/
│
├── app.py                 # FastAPI application
├── chatbot.py             # AI logic
├── document_loader.py     # Reads PDF files
├── embeddings.py          # Creates embeddings
├── vector_store.py        # ChromaDB operations
├── requirements.txt
├── data/
│   └── annual_report.pdf
└── README.md
