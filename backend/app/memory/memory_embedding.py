from sentence_transformers import SentenceTransformer
import chromadb

model_name = "sentence-transformers/all-MiniLM-L6-v2"
model=SentenceTransformer(model_name)
client=chromadb.PersistentClient("../data")
collection=client.get_or_create_collection(name="memory")

def message_embed(message):
    documents=[]
    for key,value in message.items():
        if isinstance(value,list):
            for item in value:
                documents.append(f"{key}:{item}")
        else:
            documents.append(f"{key}:{value}")
    for i,value in enumerate(documents):
        embedding=model.encode(value)
        collection.add(
            ids=[str(i)],
            documents=[value],
            embeddings=[embedding]
        )

