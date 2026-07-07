from services.llm import get_llm_response

async def run(state):
    prompt = f"""
    Analyze user memory.

    Memory:
    {state['memory_context']}

    Summarize:
    - goals
    - interests
    - study habits
    """
    print("Memory Agent Started")
    result=await get_llm_response(prompt)
    return result
    