import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 250)  
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print("🎵📣The text you said is:", text)
        return text

    except sr.UnknownValueError:
        print("🙅I couldn't understand the audio. Please try again.")
        return ""

    except sr.RequestError as e:
        print("❌Recognition error:", e)
        return ""

def translate_text(text, target_language):
    try:
        translated = GoogleTranslator(
            source='en',
            target=target_language
        ).translate(text)

        print("✅ The translated text is:", translated)
        return translated

    except Exception as e:
        print("👎 Translation error:", e)
        return ""


def display_language_options():
    print("🌍 Select a Language")
    print("Arabic (1)") 
    print("Tamil (2)")
    print("Kiswahili (3)")
    print("Bengali (4)")
    print("Zulu (5)")
    print("Marathi (6)")
    print("French (7)")
    print("Portuguese (8)")
    print("Chinese (9)")

    choice = input("\nSelect language (1-9): ")

    languages_menu = {
        "1": "ar",
        "2": "ta",
        "3": "sw",
        "4": "bn",
        "5": "zu",
        "6": "mr",
        "7": "fr",
        "8": "pt",
        "9": "zh-cn"
    }

    return languages_menu.get(choice, "hi")

# Main Program
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
            print("🎉🤩Successfully translated and spoken in the selected language.")

if __name__ == "__main__":
    main()