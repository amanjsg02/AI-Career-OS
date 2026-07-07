from fastapi import APIRouter
from services.llm import (stream_llm_response)
from services.websocket_manager import manager
from services.prompt_builder import build_prompt
from rag.embeddings import (embed_text,embed_memory)
from memory.memory_extractor import get_memory
from agents.intent import classify_intent
from agents.orchestrator import run
from fastapi.responses import StreamingResponse
from fastapi import BackgroundTasks



router=APIRouter()
conversational_history=[]
@router.post("/stream")
async def stream_chat(data:dict,
                      background_tasks:BackgroundTasks):
    user_message=data["message"]
    task_id=data["task_id"]
    background_tasks.add_task(get_memory,user_message)
    intent=await classify_intent(user_message)
    await manager.send_progress(task_id,{
        "status":"running",
        "progress":20
    })
    if "roadmap_generation" in intent:
        answer=await run(user_message,task_id)
        return StreamingResponse(stream_llm_response(answer),
                                 media_type="text/plain")
    elif "general_chat" in intent:
        await manager.send_progress(id,{
        "status":"completed",
        "progress":100
    })
        return StreamingResponse(stream_llm_response(user_message),
                                 media_type="text/plain")
    else:
      text=embed_text(user_message)
      await manager.send_progress(id,{
        "status":"running",
        "progress":50
    })
      text_memory=embed_memory(user_message)
      await manager.send_progress(id,{
        "status":"running",
        "progress":80
    })  
      prompt_data=build_prompt(user_message,text,text_memory)
      await manager.send_progress(id,{
        "status":"completed",
        "progress":100
    })
      return StreamingResponse(stream_llm_response(prompt_data),
                               media_type="text/plain")
    