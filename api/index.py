import os
from fastapi import FastAPI  # type: ignore
from fastapi.responses import PlainTextResponse  # type: ignore
from openai import OpenAI  # type: ignore

app = FastAPI()

@app.get("/api", response_class=PlainTextResponse)
def idea():
    model="openai/gpt-oss-120b"
    GROQ_BASE_URL=os.getenv("GROQ_BASE_URL")
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    client=OpenAI(api_key=GROQ_API_KEY,base_url=GROQ_BASE_URL)
    messages=[{"role":"user","content":"come up with a new business idea for Ai agents"}]
    response=client.chat.completions.create(model=model,messages=messages)
    return response.choices[0].message.content


    

