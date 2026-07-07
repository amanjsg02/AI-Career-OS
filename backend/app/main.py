from fastapi import FastAPI
from routes.chat import router as chat_router
from routes.resume import router as resume_router
from fastapi.middleware.cors import CORSMiddleware
from core.system_prompt import router as system_prompt
from routes.stream import router as stream_router
from routes.transribe import router as transribe_router
from routes.tts import router as tts_router
from routes.status import router as status_router
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(chat_router)
app.include_router(resume_router)
app.include_router(system_prompt)
app.include_router(stream_router)
app.include_router(transribe_router)
app.include_router(tts_router)
app.include_router(status_router)

@app.get("/")
def home():
    return {"home":"Running"}
