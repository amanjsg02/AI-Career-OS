from google import genai
import asyncio
from dotenv import load_dotenv
import os
from services.websocket_manager import manager

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

async def stream_llm_response(prompt,id):
   response=client.models.generate_content_stream(
      model="gemini-2.5-flash",
      contents=prompt
   )
   try:
       for chunk in response:
        if getattr(chunk,"text",None):
            yield chunk.text
   finally:
      await manager.send_progress(id,{
         "status":"completed",
         "progress":100
      })
      

    


