import requests

file_url = 'http://testphp.vulnweb.com/admin/create.sql'

response = requests.get(file_url)

if response.status_code == 200:
    with open("data.sql","wb" ) as f:
        f.write(response.content)
    print("ok")
else:
    print("error")