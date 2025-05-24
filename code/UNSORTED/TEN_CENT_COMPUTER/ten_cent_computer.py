import os
from pathlib import Path
import google.generativeai as genai


class GoogleGenerativeAI:
    """
    מחלקה ליצירת אינטראקציה עם מודלי Google Generative AI.
    """

    MODELS = [
        'gemini-1.5-flash-8b',
        'gemini-2-13b',
        'gemini-3-20b'
    ]

    def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2-13b'):
        """
        אתחול מודל GoogleGenerativeAI.

        :param api_key: מפתח ה-API לגישה ל-Gemini.
        :type api_key: str
        :param system_instruction: הנחיה למודל (פרומפט מערכתי).
        :type system_instruction: str
        :param model_name: שם מודל Gemini הנמצא בשימוש. ברירת המחדל היא 'gemini-2-13b'.
        :type model_name: str
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)  # הגדרת הספרייה עם מפתח ה-API
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # אתחול המודל עם ההנחיה

    def ask(self, q: str) -> str:
        """
        שליחת שאילתה למודל וקבלת תגובה.

        :param q: טקסט השאילתה.
        :type q: str
        :return: תגובת המודל או הודעת שגיאה.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q)  # שליחת השאילתה למודל
            return response.text  # קבלת התגובה הטקסטואלית
        except Exception as ex:
            return f'Error: {str(ex)}'  # טיפול וקבלת השגיאה


def set_key(dotenv_path: str, key: str, value: str):
    """שומר צמד מפתח-ערך בקובץ .env"""
    if os.path.exists(dotenv_path):
        with open(dotenv_path, 'r') as f:
            lines = f.readlines()
        with open(dotenv_path, 'w') as f:
            updated = False
            for line in lines:
                if line.strip().startswith(f'{key}='):
                    f.write(f'{key}={value}\n')
                    updated = True
                else:
                    f.write(line)
            if not updated:
                f.write(f'{key}={value}\n')
    else:
        with open(dotenv_path, 'w') as f:
            f.write(f'{key}={value}\n')



if __name__ == '__main__':

    __root__ = Path(__file__).resolve().parent
    relative_path: Path = Path('games', 'ai')  # נתיב יחסי לתיקיית המשחקים
    base_path: Path = __root__ / relative_path  # נתיב מוחלט לתיקייה

    # קריאת מפתח ה-API ממשתני הסביבה או בקשה מהמשתמש
    API_KEY: str = os.getenv('API_KEY')
    if not API_KEY:
        API_KEY = input('מפתח API לא נמצא. אנא הזן את מפתח ה-API עבור `gemini`: ')  # בקשת מפתח ה-API מהמשתמש
        # שמירת המפתח שהוזן בקובץ .env
        set_key('.env', 'API_KEY', API_KEY)

    instructions: dict = {
        '1': 'input_output',
        '2': 'ten_cent_computer',
    }

    # ברכת שלום למשתמש
    print('ברוכים הבאים לעולם המשחקים המתמטיים!')
    print('אנא בחר באיזה משחק תרצה לשחק:')

    while True:
        # בחירת המשחק
        print('1. המשחק "קלט-פלט"')
        print('2. המשחק "מחשב 10 סנט"')
        choice = input('הזן את מספר המשחק (1 או 2, או "q" ליציאה): ')

        if choice == 'q':
             print('להתראות!')
             break

        if choice in ('1', '2'):
            system_instruction: str = Path(base_path, f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # קריאת ההנחיה מקובץ
            # יצירת מופע של המחלקה עם ההנחיה שנבחרה
            model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
            if choice == '1':
                # הפעלת המשחק קלט-פלט
                while True:
                    user_input = input("הזן שאילתה למשחק 'קלט-פלט' ('q' ליציאה): ")
                    if user_input.lower() == 'q':
                        break
                    response = model.ask(user_input)
                    print(response)

            elif choice == '2':
                # הפעלת המשחק מחשב 10 סנט
                while True:
                     user_input = input("הזן שאילתה למשחק 'מחשב 10 סנט' ('q' ליציאה): ")
                     if user_input.lower() == 'q':
                         break
                     response = model.ask(user_input)
                     print(response)

        else:
            print('בחירה לא חוקית. אנא נסה שוב.')