import re

def parse():
  text=""
  with open("../data/resume.txt") as f:
    text=f.read()
   
  sections=re.split(r"\n(?=Education|Technical Skills|Technical Projects|Experience|Certifications & Achievements)",text.strip())
  return sections




      
   