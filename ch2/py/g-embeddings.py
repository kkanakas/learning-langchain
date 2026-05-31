from langchain_huggingface import HuggingFaceEmbeddings

model = HuggingFaceEmbeddings()
embeddings = model.embed_documents([
    "Hi there!",
    "Oh, hello!",
    "What's your name?",
    "My friends call me World",
    "Hello World!"
])

print(embeddings)
