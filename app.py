from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

CONTEXT = [
    """BEON.tech mission is to place the brightest tech talent in the most
    disruptive and innovative U.S. companies.
    """,
    """BEON.tech offer IT staff augmentation services for every modern tech need,
    from backend and frontend to AI, machine learning, DevOps and QA.
    """,
    """At BEON.tech, building software means far more than just filling roles — it's
    about creating strong relationships, empowering careers and helping people
    """
]

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    system_prompt = f"""
        You are a Sales manager.
        Use only the provided context to answer.
        If the answer is not in the context, say you do not know.

        Context:
        {chr(10).join(CONTEXT)}
    """

    completion = client.chat.completions.create(
        model="moonshotai/Kimi-K2-Instruct-0905",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": request.message,
            },
        ],
    )

    return {
        "message": completion.choices[0].message.content
    }