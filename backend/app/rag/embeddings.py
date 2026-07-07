from sentence_transformers import SentenceTransformer
from rag.parser import parse
import chromadb
model_name = "sentence-transformers/all-MiniLM-L6-v2"

chroma_client=chromadb.PersistentClient("../data")
model=SentenceTransformer(model_name)
collection=chroma_client.get_or_create_collection(name="my_embeddings")
memory_collection=chroma_client.get_or_create_collection(name="memory")


def embed():
  sections=parse()
  for i,chunk in enumerate(sections):
    embeddings_text=model.encode(chunk).tolist()
    chunk_id=f"chunck_id{i}"
    metadata={
        "source":"resume.txt",
        "chunk_id":i
           }
    collection.add(
        documents=[chunk],
        ids=[str(chunk_id)],
        embeddings=[embeddings_text],
        metadatas=metadata
        )
def embed_text(message):
  embedded_message=model.encode(message).tolist()
  result=collection.query(query_embeddings=[embedded_message],n_results=3)
  result=result['documents'][0]
  print(result)
  return result

def embed_memory(message):
  embed_text=model.encode(message).tolist()
  result=memory_collection.query(query_embeddings=[embed_text],n_results=3)
  print(result["documents"][0])
  return result["documents"][0]
  


