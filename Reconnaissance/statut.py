import requests

url = "http://testphp.vulneb.com/"

response = requests.get(url, timeout=5)

if response.status_code == 200:

    print(url,"it's UP , code = ",response.status_code)
else :

    print(url,"it's DOWN , code = ",response.status_code)



''''import requests
import socket
from rich import print

url = "http://testphp.vulnweb.com/"
domain = "testphp.vulnweb.com"  # Correction de l'orthographe
ip = socket.gethostbyname(domain)

try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f"[bold green]OK: {url} is UP [/] {response.status_code}, IP: {ip}")

    else:
        print(f"{url} is DOWN, code = {response.status_code}")
except requests.RequestException as e:
    print(f"Error accessing {url}")'''