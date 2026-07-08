import pyttsx3

# Initialisation du moteur TTS
engine = pyttsx3.init()

# Configuration de la vitesse de lecture (par défaut ~200, 150 = plus lent, 250 = plus rapide)
engine.setProperty('rate', 180)  # Vitesse modérée

# Obtenir la liste des voix disponibles
voices = engine.getProperty('voices')

# Afficher les voix disponibles et choisir une voix
print("Voix disponibles :")
for i, voice in enumerate(voices):
    print(f"{i + 1}. {voice.name} (Lang: {voice.languages})")

# Demander à l'utilisateur de choisir une voix (par défaut: voix 0)
try:
    choice = int(input("Choisissez un numéro de voix (par défaut: 1) : ")) - 1
    if 0 <= choice < len(voices):
        engine.setProperty('voice', voices[choice].id)
    else:
        print("Choix invalide, utilisation de la voix par défaut.")
except ValueError:
    print("Entrée invalide, utilisation de la voix par défaut.")

# Demander le texte à lire
text = input("Entrez le texte à lire : ")

# Option pour enregistrer dans un fichier
save_to_file = input("Voulez-vous enregistrer dans un fichier ? (Oui/Non) : ").strip().lower()
if save_to_file in ('oui', 'o', 'y', 'yes'):
    filename = input("Nom du fichier de sortie (ex: 'sortie.mp3') : ")
    engine.save_to_file(text, filename)
    print(f"Enregistrement dans '{filename}'...")
    engine.runAndWait()  # Nécessaire pour générer le fichier
    print("Fichier audio enregistré avec succès !")
else:
    # Lire le texte immédiatement
    engine.say(text)
    engine.runAndWait()