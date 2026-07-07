from google import genai
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



async def get_llm_response(message):
    response=await asyncio.to_thread(
        client.models.generate_content,
        model="gemini-2.5-flash",
        contents=message
    )

    return response.text

async def stream_llm_response(prompt):
    response=await asyncio.to_thread(
        client.models.generate_content,
        model="gemini-2.5-flash",
        contents=prompt
    )
    for chunk in response:
        if chunk.text:
            yield chunk.text


