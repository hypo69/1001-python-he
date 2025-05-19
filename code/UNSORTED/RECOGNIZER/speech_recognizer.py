import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("אנא דבר:")
        try:
             audio = recognizer.listen(source, phrase_time_limit=5)
        except Exception as e:
            print ("לא ניתן היה להבין את השמע, אנא נסה שנית")
            return None

    return audio


def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "לא ניתן היה להבין את השמע."
    except sr.RequestError as e:
        return f"שגיאת API: {e}"


def text_to_speech(text, language = "en"):

    tts = gTTS(text=text, lang=language)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete = True) as temp:
      tts.save(temp.name)
      os.system(f'mpg123 {temp.name}')

def main():
    while True:
        choice = input("בחר פעולה: (1: דיבור לטקסט, 2: טקסט לדיבור, 3: יציאה) ")
        if choice == "1":
            audio = record_audio()
            if audio:
                text = transcribe_audio(audio)
                print("טקסט מתומלל:", text)
        elif choice == "2":
          text = input("הזן את הטקסט לסינתזה קולית: ")
          text_to_speech(text)
        elif choice == "3":
          break
        else:
            print("בחירה לא חוקית")
        print()
    print ("להתראות")

if __name__ == "__main__":
   main()