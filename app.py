import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

if not groq_api_key:
    raise ValueError("GROQ API key is not set in environment variables.")

llm = ChatGroq(
    temperature=0, 
    groq_api_key=groq_api_key, 
    model_name="llama-3.1-70b-versatile"
)

response = llm.invoke("What is the capital of France?")
print(response.content)
