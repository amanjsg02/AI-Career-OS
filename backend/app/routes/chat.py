from fastapi import APIRouter
from services.llm import get_llm_response
from services.prompt_builder import build_prompt
from rag.embeddings import (embed_text,embed_memory)
import json
from memory.memory_extractor import get_memory
router=APIRouter()
from agents.intent import classify_intent
from agents.orchestrator import run

conversational_history=[]
f=open("../data/data.json","w")

@router.post("/chat")
async def chat(data:dict):
    user_message=data["message"]
    conversational_history.append({
        "role": "user",
        "content": user_message
    })
    
    await get_memory(user_message)
    intent=await classify_intent(user_message)
    if "roadmap_generation" in intent:
        answer=await run(user_message)
    elif "general_chat" in intent:
        answer=await get_llm_response(user_message)
    else:
      text=embed_text(user_message)
      text_memory=embed_memory(user_message)
      prompt_data=build_prompt(user_message,text,text_memory)
      answer=await get_llm_response(prompt_data)
    conversational_history.append({
        "role":"assistance",
        "content":answer
    })
    json.dump(conversational_history,f)

    return {
        "response":answer
    }
@router.get("/history")
def history():
    return {
        "history": conversational_history
    }