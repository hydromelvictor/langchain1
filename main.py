import os
import requests

from langchain.chat_models import ChatGroq
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

api_key = os.environ['GROQ']
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def get_completion(prompt, model="llama3-8b-8192"):
    messages = [{"role": "user", "content": prompt}]
    data = {
        "model": model,
        "messages": messages,
        "temperature": 0
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# 



# 
# print(response)
