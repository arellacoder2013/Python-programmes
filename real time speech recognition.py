import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')

    if language == "en":
        engine.setProperty('voice', voices[0].id)  
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("??? Please speak now in english...")
        audio = recognizer.listen(source)

    try:
        print("??? Recognizing speech ...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅You said {text}")
        return text
    
    except sr.UnknownValueError:
        print("❌Could not understand audio")

    except sr.RequestError as e:
        print(f" ❌API error: {e}")

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
    
def display_languages():
    print("🌍 Select a Language")
    print("Arabic (ar)") 
    print("Tamil (ta)")
    print("Kiswahili (sw)")
    print("Bengali (bn)")
    print("Zulu (zu)")
    print("Marathi (mr)")
    print("French (fr)")
    print("Portuguese (pt)")
    print("Chinese (zh)")

    choice = input("Please select the target language number (1-9):")
    language_dict = {
        "1": "ar",
        "2": "ta",
        "3": "sw",
        "4": "bn",
        "5": "zu",
        "6": "mr",
        "7": "fr",
        "8": "pt",
        "9": "zh"
    }
    return language_dict.get(choice, "es")

def main():
    target_language = display_languages()
    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(original_text, target_language=target_language)
        speak(translated_text, language="en")
        print("✅ Translation spoken out! ")

if __name__ == "__main__":
    main()
        
    


