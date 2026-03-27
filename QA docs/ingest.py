import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


DATA_PATH = "data/"
VECTORSTORE_PATH = "vectorstore/"


def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(file_path)
            documents.extend(loader.load())

    return documents


def split_documents(documents):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings()

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTORSTORE_PATH)


def main():
    print("📥 Loading documents...")
    docs = load_documents()

    print("✂️ Splitting documents...")
    chunks = split_documents(docs)

    print("🧠 Creating embeddings & vector store...")
    create_vectorstore(chunks)

    print("✅ Done! Vectorstore saved.")


if __name__ == "__main__":
    main()