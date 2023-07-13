import speech_recognition as sr
import pyttsx3
import locale

# Set the locale to Russian
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# Create a recognizer
recognizer = sr.Recognizer()

# Create a microphone input
microphone = sr.Microphone()
while True:
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Скажи что-нибудь!")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='ru-RU')
        print("Вы сказали: " + text)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Я не понял это.")
    except sr.RequestError as e:
        print("Ошибка: " + str(e))