import speech_recognition as sr
import sys

rec = sr.Recognizer()

with sr.Microphone() as src:
    while True:
        print("Please speak something:")
        audio = rec.listen(src)
        text = rec.recognize_google(audio)

        if text in "hello":
            print("Hello! How can I assist you?")
        elif text in ["how are you", "how are you doing", "how are you today"]:
            print("I'm just a program, but thanks for asking!")
        elif text in "stop":
            sys.exit(0)
        else:
            print("I didn't understand that command.")
