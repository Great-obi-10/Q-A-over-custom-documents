import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from retriever import get_retriever

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    print("🤖 Q&A over your documents")
    print("Type 'exit' to quit\n")

    retriever = get_retriever()

    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=OPENAI_API_KEY
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    while True:
        query = input("❓ Ask a question: ")

        if query.lower() == "exit":
            break

        response = qa_chain.run(query)
        print(f"\n💡 Answer: {response}\n")


if __name__ == "__main__":
    main()