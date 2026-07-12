from services.llm import get_llm_response

async def classify_intent(question):
    prompt = f"""
    You are an intent classification engine for an AI Career Operating System.

Your task is to classify the user's query into **exactly one** of the following categories.

### Categories

**resume_query**

* Questions about the user's resume, CV, projects, experience, education, skills, ATS score, resume improvements, resume rewriting, resume formatting, interview questions based on the resume, or anything requiring information from the uploaded resume.

**memory_query**

* Questions that require retrieving previously stored user information or conversation memory.
* Examples:

  * "What did I tell you before?"
  * "Do you remember my career goal?"
  * "What technologies am I learning?"
  * "Recall my previous preferences."

**roadmap_generation**

* Requests to generate a learning roadmap, study plan, preparation strategy, learning path, milestone plan, or step-by-step roadmap for any topic.
* Examples:

  * "Create a roadmap for MLOps."
  * "How should I prepare for DRDO?"
  * "Give me a backend development roadmap."

**career_advice**

* Career guidance, job search advice, internship guidance, higher studies, salary discussions, company selection, role comparison, interview strategy, career planning, or professional decision-making.
* Examples:

  * "Should I learn Go or Rust?"
  * "Should I pursue an MS?"
  * "How do I prepare for product-based companies?"

**skill_gap_analysis**

* Requests to evaluate current skills against a target role and identify missing skills.
* Examples:

  * "Am I ready for an AI Engineer role?"
  * "What skills am I missing for Google?"
  * "Compare my skills with a Data Scientist."

**general_chat**

* ANY query that does not clearly belong to one of the five categories above.
* This includes:

  * Greetings
  * Casual conversation
  * General knowledge
  * Programming questions
  * Mathematics
  * Science
  * Entertainment
  * Jokes
  * News
  * Weather
  * Coding help unrelated to resume, memory, roadmap, career advice, or skill-gap analysis
  * Any other unrelated conversation

### Rules

1. Return **exactly one** category.
2. Never explain your answer.
3. Never return multiple categories.
4. Never return any extra text.
5. The output must be one of these exact strings only:

resume_query
memory_query
roadmap_generation
career_advice
skill_gap_analysis
general_chat

User Question:
{question}
    """
    result=await get_llm_response(prompt)
    return result
