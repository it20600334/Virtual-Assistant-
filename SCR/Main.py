import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        voice = listener.listen(source)
except:
    pass
