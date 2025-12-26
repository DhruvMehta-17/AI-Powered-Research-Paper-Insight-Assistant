from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),
               model_name = "mixtral-8x7b-32768",
               temperature=0)