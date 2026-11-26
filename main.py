from fastapi import FastAPI
from pydantic import BaseModel
from search import search
from agent import run_agent

app = FastAPI(title="Job Matcher")

class Query(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/search")
def search_jobs(q: Query):
    return search(q.text, k=5)

@app.post("/match")
def match(q: Query):
    return {"answer": run_agent(q.text)}