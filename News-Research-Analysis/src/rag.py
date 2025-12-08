from src.utils import Knowledgebase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.prompt import system_prompt
from dotenv import load_dotenv
import os
from operator import itemgetter

load_dotenv()


def load_rag_chain(urls: str):
    url_list = [u.strip() for u in urls.split(",") if u.strip()]
    if not url_list:
        raise ValueError("No URLs provided.")
    kb = Knowledgebase(URL=url_list)
    docs = kb.load()
    if not docs:
        raise ValueError("No documents loaded from the provided URLs.")
    embd = kb.model()
    vectorstore = kb.vectorstore(docs, embd)
    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 2}
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}\n\nContext:\n{context}"),
        ]
    )

    gemini_api = os.getenv("GEMINI_API_KEY")
    gemini = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.2,
        max_output_tokens=1024,
        top_p=0.95,
        top_k=40,
        google_api_key=gemini_api,
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            "context": itemgetter("input") | retriever | format_docs,
            "input": itemgetter("input"),
        }
        | prompt
        | gemini
        | StrOutputParser()
    )
    
    return rag_chain
