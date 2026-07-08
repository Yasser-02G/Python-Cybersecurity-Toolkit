import requests
from rich import print

url = "https://jsonplaceholder.typicode.com/"

response = requests.get(url)

if response.status_code == 200:
    print(f"[bold red on white] Technology Enumeration [/]")
    for x,y in response.headers.items():
        print(f"[bold yellow ]{x}[/] : [bold green]{y}[/]")