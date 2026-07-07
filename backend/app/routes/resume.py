from fastapi import APIRouter
from fastapi import UploadFile,BackgroundTasks
from fastapi import File,Form
from pypdf import PdfReader
from rag.embeddings import embed
from services.redis import prog
import redis



router=APIRouter()

redis_Client=redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


@router.post("/upload_resume")
async def upload_resume(
    background_tasks:BackgroundTasks,
    file: UploadFile=File(...),
    task_id:str=Form(...)
    ):
    
    redis_Client.hset(
        f"task:{task_id}",
        mapping={
            "status":"running",
            "progress":0
        }
    )
    
    content=await file.read()
    
    with open("../data/resume.pdf","wb") as f:
        f.write(content)

    background_tasks.add_task(prog,task_id,"../data/resume.pdf")


   # reader=PdfReader("../data/resume.pdf","../data/resume.pdf")
    #text=""
    #for pages in reader.pages:
        #new_text=pages.extract_text()
        #if new_text:
            #text+=new_text+"\n"
    
   # with open("../data/resume.txt","w",encoding="utf-8") as f:
   #     f.write(text)
    
   # embed()
       