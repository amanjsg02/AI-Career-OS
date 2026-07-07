from services.llm import get_llm_response

async def run(state):
    prompt = f"""
    User asked:

    {state['question']}

    What current skills,
    technologies and trends
    are relevant?
    """
    print("Research Agent Started")
    result=await get_llm_response(prompt)
    
    return result