def prompt(message):
 return f"""
   Extract long-term useful user information.

Return answer in JSON format only and not in string format and no extra comments like 
```json 

``` needed, just give clear json format which i can process in my backend

For example:
career_goal
target_company
study_hours
skill_level
completed_skills
It is not mandatory to use all the fields given in the example,use only which is relevant and you can take relevant field
according to you also!

Message:
{message}
"""