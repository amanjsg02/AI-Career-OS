from gtts import gTTS
from fastapi import APIRouter
from fastapi.responses import FileResponse

router=APIRouter()

@router.post("/gtts")
async def ans(data:dict):
    text=data["message"]
    tts=gTTS(text=text,lang="en")
    filename="response.mp3"
    tts.save(filename)
    return FileResponse(
        filename,
        media_type="audio/mpeg"
    )