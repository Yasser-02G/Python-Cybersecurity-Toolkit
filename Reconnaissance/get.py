# https://jsonplaceholder.typicode.com/ 
# ❌✅

import requests
import json

url = 'https://jsonplaceholder.typicode.com/photos/1'

data = requests.get(url)

if data.status_code == 200 :
    print("get information ✅" )
    print(data.json())


    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data.json(), f, ensure_ascii=False, indent=4)


else: 
    print("error ❌")
