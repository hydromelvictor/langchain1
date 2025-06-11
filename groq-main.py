import requests
import os

from dotenv import load_dotenv, find_dotenv

api_key = os.environ['GROQ']
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    # "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    # llama3-8b-8192
    # llama3-70b-8192
    # mixtral-8x7b-32768
    # gemma-7b-it
    "model": "llama3-8b-8192",
    "messages": [
        {"role": "system", "content": "Tu es un assistant utile."},
        {"role": "user", "content": "Explique-moi le fonctionnement de Groq."}
    ]
}

response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)

print(response.json()["choices"][0]["message"]["content"])



# const axios = require('axios');

# const apiKey = "TA_CLE_GROQ_ICE";

# axios.post('https://api.groq.com/openai/v1/chat/completions', {
#   model: "llama3-8b-8192",
#   messages: [
#     { role: "system", content: "Tu es un assistant utile." },
#     { role: "user", content: "Explique-moi le fonctionnement de Groq." }
#   ]
# }, {
#   headers: {
#     'Authorization': `Bearer ${apiKey}`,
#     'Content-Type': 'application/json'
#   }
# })
# .then(res => {
#   console.log(res.data.choices[0].message.content);
# })
# .catch(err => {
#   console.error("Erreur : ", err.response?.data || err.message);
# });
