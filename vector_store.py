from langchain_community.vectorstores import Chroma

def create_vector_db(documents, embeddings):
    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory="db"
    )
    db.persist()
    return db

def load_db(embeddings):
    return Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )
