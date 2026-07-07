from services.llm import get_llm_response

async def run(state):
    prompt = f"""
    Review this roadmap.

    Roadmap:
    {state['roadmap']}

    Check:
    - realism
    - missing skills
    - timeline

    Improve if necessary.
    """
    return prompt
