import speech_recognition as sr
import pyttsx3
from datetime import datetime


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate', 150) 
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("????? Speak now")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"You said:✅ {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("????? Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"❌ API error:{e}")

        return ""

def reply_to_command(command):
    if "hello" in command:
        speak("Hi! How can I help you today?")

    elif "your name" in command:
        speak("I am your Python voice assistant.")

    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"⌚The time is {now}.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Im not sure how to help with that")
    return False

def main():
    speak("Voice assistant activated. Say something!")

    while True:
        command = get_audio()
        if command and not reply_to_command(command):
            break

if __name__ == "__main__":
    main()


    

    