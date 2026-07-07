import chromadb

client = chromadb.PersistentClient(path="./data")

collection = client.get_collection(name="memory")

data = collection.get()

print(data)