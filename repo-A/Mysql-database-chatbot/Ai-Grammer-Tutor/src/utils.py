from src.prompts import grammer_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api = os.getenv("GEMINI_API")

class GrammarChecker:
    def __init__(self, para):
        self.para = para
        self.prompt = self.build_prompt()

    def build_prompt(self):  
        prompt = f"""{grammer_prompt}
User input:
\"\"\"
{self.para}
\"\"\"  
Respond as a helpful tutor.
"""
        return prompt

    def check_grammar(self):
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  
            google_api_key=gemini_api, 
            temperature=0.2 
        )
        response = llm.invoke([
            HumanMessage(content=self.prompt)
        ])
        return response.content

