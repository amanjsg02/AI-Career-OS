from fastapi import APIRouter
from services.prompt_builder import analyze_resume
from services.llm import get_llm_response
router=APIRouter()

@router.get("/analyze_resume")
async def ans():
    text="Check Resume!"
    resume_text=analyze_resume(text)
    answer=await get_llm_response(resume_text)
    return {
        "response":answer
    }

