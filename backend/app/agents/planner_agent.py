from services.llm import get_llm_response

async def run(state):
    prompt = f"""
    Create a roadmap.

    Resume Analysis:
    {state['resume_analysis']}

    Memory Analysis:
    {state['memory_analysis']}

    Market Analysis:
    {state['']}

    Create a detailed roadmap.
    """
    result=await get_llm_response(prompt)
    state["roadmap"]=result
    return state