
from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import generate_response

app = FastAPI(title="AI Chatbot API")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/")
def root():
    return {"status": "AI Chatbot Backend Running"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = generate_response(request.message)
    return {"reply": reply}


