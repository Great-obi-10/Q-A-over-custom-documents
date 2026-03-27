from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

VECTORSTORE_PATH = "vectorstore/"


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings()
    return FAISS.load_local(VECTORSTORE_PATH, embeddings)


def get_retriever():
    vectorstore = load_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": 3})