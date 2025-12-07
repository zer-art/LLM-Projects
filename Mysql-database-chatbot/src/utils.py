from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts.prompt import PromptTemplate
from dotenv import load_dotenv
from src.few_shorts_queries import few_shots
from src.mysql_prompt import prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
import os
import re

load_dotenv()


class MYSQLChain:
    def __init__(self):
        self.llm = self._create_llm()
        self.db = self._create_db()
        self.embeddings = self._create_embeddings()
        self.example_selector = self._create_example_selector()
        self.few_shot_prompt = self._create_few_shot_prompt()
        self.agent = self._build_agent()
        self.qa_chain = self._build_qa_chain()

    def _create_llm(self):
        return ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.2,
        )

    def _create_db(self):
        db_user = "root"
        db_password = os.getenv("MYSQL_PASSWORD")
        db_host = "localhost"
        db_name = "atliq_tshirts"
        return SQLDatabase.from_uri(
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
            sample_rows_in_table_info=3,
        )

    def _create_embeddings(self):
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def _create_example_selector(self):
        # Ensure all values are strings before joining
        to_vectorize = [
            " ".join(str(v) for v in example.values()) for example in few_shots
        ]
        vectorstore = Chroma.from_texts(
            to_vectorize, self.embeddings, metadatas=few_shots
        )
        return SemanticSimilarityExampleSelector(
            vectorstore=vectorstore,
            k=2,
        )

    def _create_few_shot_prompt(self):
        example_prompt = PromptTemplate(
            input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
            template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
        )
        return FewShotPromptTemplate(
            example_selector=self.example_selector,
            example_prompt=example_prompt,
            prefix=prompt,
            suffix=PROMPT_SUFFIX,
            input_variables=["input", "table_info", "top_k"],
        )

    def _build_agent(self):

        toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)
        agent_executor = create_sql_agent(llm=self.llm, toolkit=toolkit, verbose=True)
        return agent_executor

    def _build_qa_chain(self):
        # Use invoke instead of run
        return self.few_shot_prompt | self.llm | StrOutputParser()

    def run_agent(self, query: str):
        result = self.agent.invoke({"input": query})
        return result

    def run_qa_chain(self, query: str):
        # Use invoke instead of run
        return self.qa_chain.invoke(
            {"input": query, "table_info": self.db.get_table_info(), "top_k": "3"}
        )
