# Pyttsx3 is a text to speech python library used to convert text into speech.
# SpeechRecognition: This Python library is used to convert speech into text

import speech_recognition as sp


def command():
    r = sp.Recognizer()
    while True:
        with sp.Microphone() as source:
            print("Alexa: Listening...")
            audio=r.listen(source)
            try:
                query = r.recognize_google(audio)
                print(f"master:{query}")
                return query
            except:
                print("Try Again")


