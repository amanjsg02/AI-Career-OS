from agents.critic_agent import run as critic_agent
from agents.memory_agent import run as memory_agent
from agents.planner_agent import run as planner_agent
from agents.research_agent import run as research_agent
from agents.resume_agent import run as resume_agent
from rag.embeddings import (embed_memory,embed_text)
import asyncio
from services.websocket_manager import manager


async def run(user_message,id):
    resume_text=embed_text(user_message)
    await manager.send_progress(id,{
        "status":"running",
        "progress":30
    })
    memory_text=embed_memory(user_message)
    await manager.send_progress(id,{
        "status":"running",
        "progress":40
    })
    state={
        "question":{user_message},
        "resume_context":[resume_text],
        "memory_context":[memory_text]
    }

    resume_result,memory_result,research_result=await asyncio.gather(resume_agent(state),memory_agent(state),research_agent(state))
    await manager.send_progress(id,{
        "status":"running",
        "progress":50
    })
    state["resume_analysis"]=resume_result
    state["memory_analysis"]=memory_result
    state["market_analysis"]=research_result
    state=await planner_agent(state)
    await manager.send_progress(id,{
        "status":"running",
        "progress":80
    })
    response= await critic_agent(state)
    await manager.send_progress(id,{
        "status":"completed",
        "progress":100
    })
    return response