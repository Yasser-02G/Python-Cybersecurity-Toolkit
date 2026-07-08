from speedtest import Speedtest

data = Speedtest()

print("Votre vitesse de connexion est en cours de calcul...")
download = data.download()
print(f"Votre vitesse de téléchargement est : {download / 10**6:.2f} Mbit/s")
upload = data.upload()
print(f"Votre vitesse d'envoi est : {upload / 10**6:.2f} Mbit/s")