# https://jsonplaceholder.typicode.com/ 
# ❌✅

import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    "body": "xman",
    "title": "test",
    "userId": 1
}

# Il faut envoyer les données en JSON, pas en 'data'
send = requests.post(url, json=data)

print("code stats :", send.status_code)
print("response :", send.json())

