import speech_recognition as sr
import datetime
import subprocess



recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Sorry, could not request results. Please check your internet connection.")

    if "chrome" in text:
        a = "Opening chrome ..."
        


recognize_speech()
