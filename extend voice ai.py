import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤Speak now in English...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print("🔊You said:", text)
        return text

    except sr.UnknownValueError:
        print("🤔Could not understand audio.")
        return ""

    except sr.RequestError as e:
        print("⛔Speech Recognition Error:", e)
        return ""

def translate_text(text, target_language):
    try:
        translated = GoogleTranslator(
            source='en',
            target=target_language
        ).translate(text)

        print("✅✔Translated text:", translated)
        return translated

    except Exception as e:
        print("❌❗Translation Error:", e)
        return ""

def display_language_options():
    print("\n 🌍Pick a language")
    print("1. French")
    print("2. Spanish")
    print("3. German")
    print("4. Italian")
    print("5. Swahili")
    print("6. Arabic")
    print("7. Chinese")
    print("8. Japanese")

    choice = input("\nSelect language (1-8): ")

    languages = {
        "1": "fr",
        "2": "es",
        "3": "de",
        "4": "it",
        "5": "sw",
        "6": "ar",
        "7": "zh-CN",
        "8": "ja"
    }

    return languages.get(choice, "fr")

def main():
    target_language = display_language_options()

    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(
            original_text,
            target_language
        )

        if translated_text:
            speak(translated_text)
            print("✅ 🎉👏Translation spoken successfully!")

if __name__ == "__main__":
    main()