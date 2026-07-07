from pypdf import PdfReader
import redis
from rag.parser import parse
from sentence_transformers import SentenceTransformer
import chromadb
from services.websocket_manager import manager

model_name="sentence-transformers/all-MiniLM-L6-v2"
model=SentenceTransformer(model_name)
chroma_Client=chromadb.PersistentClient("../data")
collection=chroma_Client.get_or_create_collection(name="my_embeddings")

redis_Client=redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

async def prog(id,file_path):
    reader=PdfReader(file_path)
    text=""
    embed_toAdd=[]
    for pages in reader.pages:
        new_text=pages.extract_text()
        if new_text:
            text+=new_text+"\n"
    with open("../data/resume.txt","w",encoding="utf-8") as f:
        f.write(text)
    redis_Client.hset(
        f"task:{id}",
        mapping={
            "status":"running",
            "progress":20
        }
    )
    await manager.send_progress(id,{
        "status":"running",
        "progress":20

    })
    sections=parse()
    redis_Client.hset(
        f"task:{id}",
        mapping={
            "status":"running",
            "progress":40
        }
    )
    await manager.send_progress(id,{
        "status":"running",
        "progress":40

    })
    for i,chunk in enumerate(sections):
        embed_data=model.encode(chunk).tolist()
        embed_toAdd.append({
            "id":i,
            "embed":embed_data,
            "document":chunk,
            "metadata":{
                "source":"resume.txt",
                "chunk_id":i
            }
        })
    redis_Client.hset(
        f"task:{id}",
        mapping={
            "status":"running",
            "progress":70
        }
    )
    await manager.send_progress(id,{
        "status":"running",
        "progress":70

    })
    for k in embed_toAdd:
        chunk_id=k["id"]
        document=k["document"]
        embeddings=k["embed"]
        metadatas=k["metadata"]
        collection.add(
            documents=[document],
            ids=[str(chunk_id)],
            embeddings=[embeddings],
            metadatas=[metadatas]
        )
    redis_Client.hset(
      f"task:{id}",
      mapping={
        "status":"completed",
        "progress":100
        }
    )
    await manager.send_progress(id,{
        "status":"running",
        "progress":100

    })
   
        
    







