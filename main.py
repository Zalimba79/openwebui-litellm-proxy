# main.py
from fastapi import FastAPI, Request
import litellm
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "LiteLLM Proxy läuft ✅"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "Sag etwas.")

    # Beispielhafte LiteLLM-Nutzung (OpenAI)
    response = litellm.completion(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        api_key=os.getenv("OPENAI_API_KEY")
    )

    return {"response": response['choices'][0]['message']['content']}
