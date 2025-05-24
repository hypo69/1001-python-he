# משחק 'דיבור לטקסט - טקסט לדיבור'

## תיאור

משחק זה משלב את הפונקציונליות של המרת דיבור לטקסט (Speech-to-Text או STT) וטקסט לדיבור (Text-to-Speech או TTS). באפשרותכם לדבר למיקרופון ולשמוע כיצד הדיבור שלכם מומר לטקסט, או להזין טקסט ולהאזין לאופן שבו הוא מושמע.

## תנאי המשחק

המשחק מציע שני מצבים עיקריים:

1.  **דיבור לטקסט (STT)**:
    *   אתם מדברים למיקרופון.
    *   המערכת מקליטה את האודיו שלכם.
    *   האודיו מומר לטקסט ומוצג על המסך.
    *   מצב זה מאפשר לכם לבדוק את יכולות זיהוי הדיבור של המערכת.

2.  **טקסט לדיבור (TTS)**:
    *   אתם מזינים טקסט באמצעות המקלדת.
    *   המערכת ממירה את הטקסט שהוזן לאודיו.
    *   אתם שומעים את הטקסט מושמע.
    *   מצב זה מאפשר לכם להאזין כיצד טקסט ישמע כשהוא מושמע.

המשחק מאפשר לכם לעבור בין שני המצבים הללו. באפשרותכם גם לצאת מהמשחק.

## כיצד להריץ

1.  **התקינו Python**: אם Python אינו מותקן אצלכם, הורידו והתקינו אותו מ-[האתר הרשמי](https://www.python.org/).
2.  **התקינו את הספריות הנדרשות**: השתמשו ב-`pip` כדי להתקין את הספריות:
    ```bash
    pip install SpeechRecognition gTTS mpg123
    ```

3.  **העתיקו את הקוד לקובץ**: העתיקו את קוד ה-Python, המוצג להלן, לקובץ, לדוגמה, `speech_game.py`.
4.  **הריצו את המשחק**: בטרמינל או בשורת הפקודה, הפעילו:
    ```bash
    python speech_game.py
    ```

## קוד מקור (Python)

```python
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

# Function for recording audio from the microphone
def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now:")
        try:
             # Adjust for ambient noise and record audio
             audio = recognizer.listen(source, phrase_time_limit=5)
        except Exception as e:
            # Handle cases where audio could not be understood
            print ("Could not understand audio, try again")
            return None

    return audio

# Function for transcribing audio to text
def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        # Use Google's speech recognition service
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        # API was unable to understand the speech
        return "Could not understand the audio."
    except sr.RequestError as e:
        # API was unreachable or unresponsive
        return f"API Error: {e}"

# Function for converting text to speech
def text_to_speech(text, language = "en"):

    # Create a gTTS object
    tts = gTTS(text=text, lang=language)
    # Use a temporary file to save and play the audio
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete = True) as temp:
      tts.save(temp.name)
      # Play the audio file using mpg123
      os.system(f'mpg123 {temp.name}')

# Main function to run the game loop
def main():
    while True:
        # Prompt user for choice
        choice = input("Choose action: (1: STT, 2: TTS, 3: Exit) ")
        if choice == "1":
            # Record and transcribe audio
            audio = record_audio()
            if audio:
                text = transcribe_audio(audio)
                print("Transcribed Text:", text)
        elif choice == "2":
          # Get text input from user and convert to speech
          text = input("Enter the text to synthesize: ")
          text_to_speech(text)
        elif choice == "3":
          # Exit the loop
          break
        else:
            # Handle invalid input
            print("Invalid Choice")
        print() # Print a newline for better readability
    print ("Good Bye")

if __name__ == "__main__":
   main()
```

### ניתוח הקוד

*   **הצהרות `import`**: מייבאות את הספריות הנדרשות:
    *   `speech_recognition` לזיהוי דיבור.
    *   `gtts` להמרת טקסט לדיבור.
    *   `os` ו-`tempfile` לניהול קבצי אודיו זמניים.

*   **`record_audio()`**:
    *   פונקציה להקלטת אודיו מהמיקרופון.
    *   משתמשת ב-`speech_recognition` ללכידת האודיו.

*   **`transcribe_audio(audio)`**:
    *   מקבלת אודיו שהוקלט קודם לכן.
    *   משתמשת ב-Google Speech Recognition API להמרת אודיו לטקסט.
    *   מחזירה את הטקסט שזוהה או הודעת שגיאה.

*   **`text_to_speech(text, language="en")`**:
    *   מקבלת טקסט ושפה (ברירת מחדל אנגלית) כארגומנטים.
    *   משתמשת ב-`gtts` להמרת טקסט לאודיו.
    *   שומרת את האודיו בקובץ זמני.
    *   משמיעה את האודיו באמצעות `mpg123`.

*   **`main()`**:
    *   הפונקציה הראשית המנהלת את מהלך המשחק.
    *   מציעה למשתמש לבחור פעולה (STT, TTS או יציאה).
    *   קוראת לפונקציות המתאימות לביצוע הפעולה שנבחרה.
    *   מעבדת את קלט המשתמש ומדפיסה את התוצאות למסוף.

## הערות נוספות

*   **תלויות**: קוד זה דורש את הספריות `SpeechRecognition`, `gtts`, ו-`mpg123` מותקנות. ודאו שהן מותקנות לפני ההרצה.
*   **אודיו**: אם `mpg123` אינו עובד, באפשרותכם להשתמש בנגן אחר להשמעת האודיו, על ידי שינוי הפונקציה `text_to_speech`.