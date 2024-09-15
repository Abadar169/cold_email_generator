import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")
collection.add(
    documents=[
        "This is a document about New York City.",
        "This is  a document about New Delhi.",
    ],
    ids=["id1", "id2"],
    metadatas=[
        {"url":"https://en.wikipedia.org/wiki/New_York_City"},
        {"url":"https://en.wikipedia.org/wiki/New_Delhi"},
    ]
)

all_docs = collection.get()
print(all_docs)

# result = collection.query(
#     query_texts=['Query is about Taj Mahal'],
#     n_results=2
# )

# print(result)