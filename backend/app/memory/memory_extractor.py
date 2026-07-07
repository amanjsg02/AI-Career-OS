from services.llm import get_llm_response
from memory.get_memoryPrompt import prompt
from memory.memory_store import update_memory
from memory.memory_embedding import message_embed
import json
async def get_memory(message):
 memory_prompt=prompt(message)
 memory=await get_llm_response(memory_prompt)
 memory = memory.replace("```json", "")
 memory = memory.replace("```", "")
 memory = memory.strip()
 memory=json.loads(memory)
 message_embed(memory)
 update_memory(memory)


