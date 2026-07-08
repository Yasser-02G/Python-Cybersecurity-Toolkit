import requests

url = 'http://testphp.vulnweb.com'

response = requests.head(url)

print(f"header info is : {response}")



for key, value in response.headers.items():
    print(f"{key}: {value}")