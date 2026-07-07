from fastapi import APIRouter, WebSocket
from services.websocket_manager import manager
import redis
import uuid
router = APIRouter()
redis_Client=redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

@router.websocket("/ws/{task_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    task_id: str
):
    await manager.connect(task_id, websocket)

    try:
        while True:
            await websocket.receive()
    except:
        manager.disconnect(task_id)

@router.get("/status/{id}")
def givestatus(id:str):
    result=redis_Client.hgetall(f"task:{id}")
    return result

@router.get("/id")
def giveid():
    id=str(uuid.uuid4())
    return {
        "task_id":id
    }

