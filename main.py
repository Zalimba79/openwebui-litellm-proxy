from fastapi import FastAPI, Request
import litellm
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "LiteLLM Proxy läuft ✅"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "Sag etwas.")
    model = data.get("model", "openai")  # z.B. "openai" oder "gemini"

    if model == "openai":
        # OpenAI API Key aus der env
        response = litellm.completion(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            api_key=os.getenv("OPENAI_API_KEY")
        )
    elif model == "gemini":
        # Gemini via Vertex AI (keine API-Key-Übergabe nötig, wenn korrekt authentifiziert)
        response = litellm.completion(
            model="gemini/gemini-1.5-pro",
            messages=[{"role": "user", "content": prompt}]
        )
    else:
        return {"error": "Unbekanntes Modell. Bitte 'openai' oder 'gemini' angeben."}

    return {"response": response['choices'][0]['message']['content']}
