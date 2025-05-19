# המשחק "דיבור לטקסט - טקסט לדיבור"

## תיאור

משחק זה משלב פונקציונליות של המרת דיבור לטקסט (Speech-to-Text או STT) וטקסט לדיבור (Text-to-Speech או TTS). באפשרותכם לדבר למיקרופון ולשמוע כיצד דיבורכם מומר לטקסט, או להקליד טקסט ולהאזין להקראתו.

## תנאי המשחק

המשחק מספק שני מצבים עיקריים:

1.  **דיבור לטקסט (STT)**:
    *   אתם מדברים למיקרופון.
    *   המערכת מקליטה את האודיו שלכם.
    *   האודיו מומר לטקסט ומוצג על המסך.
    *   מצב זה מאפשר לכם לבחון את יכולות זיהוי הדיבור של המערכת.

2.  **טקסט לדיבור (TTS)**:
    *   אתם מזינים טקסט באמצעות המקלדת.
    *   המערכת ממירה את הטקסט שהוזן לאודיו.
    *   אתם שומעים את הטקסט מושמע.
    *   מצב זה מאפשר לכם להאזין כיצד טקסט מסוים יישמע בעת הקראה.

המשחק מאפשר לכם לעבור בין שני מצבים אלו. ניתן גם לצאת מהמשחק.

## כיצד להפעיל

1.  **התקינו Python**: אם Python אינו מותקן אצלכם, הורידו והתקינו אותו מ[האתר הרשמי](https://www.python.org/).
2.  **התקינו את הספריות הנדרשות**: השתמשו ב-`pip` להתקנת הספריות:
    ```bash
    pip install SpeechRecognition gTTS mpg123
    ```

3.  **העתיקו את הקוד לקובץ**: העתיקו את קוד Python המוצג להלן לקובץ, לדוגמה, `speech_game.py`.
4.  **הריצו את המשחק**: בטרמינל או בשורת הפקודה, בצעו:
    ```bash
    python speech_game.py
    ```

## קוד מקור (Python)

```python
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now:")
        try:
             audio = recognizer.listen(source, phrase_time_limit=5)
        except Exception as e:
            print ("Could not understand audio, try again")
            return None

    return audio


def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"API Error: {e}"


def text_to_speech(text, language = "en"):
   
    tts = gTTS(text=text, lang=language)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete = True) as temp:
      tts.save(temp.name)
      os.system(f'mpg123 {temp.name}')

def main():
    while True:
        choice = input("Choose action: (1: STT, 2: TTS, 3: Exit) ")
        if choice == "1":
            audio = record_audio()
            if audio:
                text = transcribe_audio(audio)
                print("Transcribed Text:", text)
        elif choice == "2":
          text = input("Enter the text to synthesize: ")
          text_to_speech(text)
        elif choice == "3":
          break
        else:
            print("Invalid Choice")
        print()
    print ("Good Bye")

if __name__ == "__main__":
   main()
```

### ניתוח הקוד

*   **הצהרות `import`**: מיובאות הספריות הנדרשות:
    *   `speech_recognition` לזיהוי דיבור.
    *   `gtts` להמרת טקסט לדיבור.
    *   `os` ו-`tempfile` לניהול קבצי אודיו זמניים.

*   **`record_audio()`**:
    *   פונקציה להקלטת אודיו מהמיקרופון.
    *   משתמשת ב-`speech_recognition` ללכידת האודיו.

*   **`transcribe_audio(audio)`**:
    *   מקבלת את האודיו שהוקלט קודם לכן.
    *   משתמשת ב-Google Speech Recognition API להמרת אודיו לטקסט.
    *   מחזירה את הטקסט המזוהה או הודעת שגיאה.

*   **`text_to_speech(text, language="en")`**:
    *   מקבלת טקסט ושפה (ברירת מחדל אנגלית) כארגומנטים.
    *   משתמשת ב-`gtts` להמרת טקסט לאודיו.
    *   שומרת את האודיו בקובץ זמני.
    *   מנגנת את האודיו באמצעות `mpg123`.

*   **`main()`**:
    *   הפונקציה הראשית המנהלת את מהלך המשחק.
    *   מציעה למשתמש בחירה בפעולה (STT, TTS, או יציאה).
    *   קוראת לפונקציות המתאימות לביצוע הפעולה שנבחרה.
    *   מעבדת את קלט המשתמש ומציגה את התוצאות במסוף.

## הערות נוספות

*   **תלויות**: קוד זה דורש התקנה של הספריות `SpeechRecognition`, `gTTS`, ו-`mpg123`. ודאו שהן מותקנות לפני ההרצה.
*   **אודיו**: אם `mpg123` אינו פועל, באפשרותכם להשתמש בנגן אחר להשמעת האודיו על ידי שינוי הפונקציה `text_to_speech`.