from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.utils import GrammarChecker


app = FastAPI()
# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GrammarRequest(BaseModel):
    text: str

@app.post("/api/grammar")
async def grammar_api(request: GrammarRequest):
    grammar_checker = GrammarChecker(request.text)
    result = grammar_checker.check_grammar()
    return {"result": result}
