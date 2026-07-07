from services.llm import get_llm_response

async def run(state):

    prompt = f"""
    Analyze the resume.

    Question:
    {state['question']}

    Resume:
    {state['resume_context']}

    Give:
    - strengths
    - weaknesses
    - relevant experience
    """
    print("Resume Agent Started")
    result = await get_llm_response(prompt)

    return result

    