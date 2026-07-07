from fastapi import APIRouter,UploadFile,File
import whisper

router=APIRouter()
model=whisper.load_model("base")

@router.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    file_name="temp.webm"
    with open(file_name,"wb") as f:
        f.write(await audio.read())
    contents=model.transcribe(file_name)
    print(type(contents["text"]))
    print(contents["text"])
    return {
        "message":contents["text"]
     }
