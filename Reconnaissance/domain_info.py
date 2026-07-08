import requests


url = input("entrer domain name : ")

response = requests.get(f"https://api.whois.vu/?q={url}")

print(response.text)