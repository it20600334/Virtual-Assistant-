import speech_recognition as sr
import pyttsx3 as tts

listener = sr.Recognizer()
engine = tts.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id) 
engine.say('Hi I am ELWIN')
engine.say('What can I do for you')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('Listening.....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'Elwin' in command:
            print (command)
except:
    pass


