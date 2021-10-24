import speech_recognition as sr


class SpeechRecognition:
    def __init__(self):
        print("SpeechRecognizer initialized")

    def recognize(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Konuşun...")
            data = r.record(source, duration=5)
            print("Sesinizi Metne Dönüştürülüyor...")
            text = r.recognize_google(data, language='tr')
            return text