import socket

url = input("entrer l'addresse de votre site : ")

ip = socket.gethostbyname(url)

print(f"IP = {ip}")
