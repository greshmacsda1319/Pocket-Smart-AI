from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Pocket Smart AI")

@app.get("/")
def home():
    return {"message": "Pocket Smart AI is Running! 🤖"}

@app.post("/chat")
def chat(message: str):
    # ... code
