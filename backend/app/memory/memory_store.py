import json

MEMORY_FILE="./memory/user_memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE,"r") as f:
            return json.load(f)
    except:
        return {}
def save_memory(memory):
    with open(MEMORY_FILE,"w") as f:
        json.dump(memory,f,indent=4)

def update_memory(new_data):
    memory=load_memory()
    for key,value in new_data.items():
       if isinstance(value,list):
           if key not in memory:
               memory[key]=[]
           for item in value:
               if item not in memory[key]:
                memory[key].append(item)
       else:
           memory[key]=value
    save_memory(memory)
