import chromadb

client = chromadb.Client()
collection = client.create_collection(name="test_collection")

collection.add(
    documents=[
        "Python is a programming language.",
        "The Eiffel Tower is in Paris.",
        "Groq provides fast LLM inference.",
    ],
    ids=["1", "2", "3"],
)

results = collection.query(query_texts=["Where is the Eiffel Tower?"], n_results=1)
print(results["documents"])