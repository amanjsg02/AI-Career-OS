from services.llm import get_llm_response

async def classify_intent(question):
    prompt = f"""
    Classify the user question into one category:

    1. resume_query
    2. memory_query
    3. roadmap_generation
    4. career_advice
    5. skill_gap_analysis
    6. general_chat

    Question:
    {question}

    Return only category name.
    """
    result=await get_llm_response(prompt)
    return result
