import os
import re  # ייבוא ספרייה לעבודה עם ביטויים רגולריים
import json

from pathlib import Path
from dotenv import load_dotenv, set_key  # ייבוא פונקציה לשמירת משתנה ב-env.

import google.generativeai as genai  # ייבוא ספרייה לעבודה עם Gemini
from header import __root__  # ייבוא אובייקט __root__, המכיל את הנתיב המוחלט לשורש הפרויקט


# טעינת משתני סביבה מהקובץ env.
load_dotenv()

class GoogleGenerativeAI:
    """
    מחלקה לאינטראקציה עם מודלי Google Generative AI.
    """

    MODELS = [
        'gemini-1.5-flash-8b',
        'gemini-2-13b',
        'gemini-3-20b'
    ]

    def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
        """
        אתחול מודל GoogleGenerativeAI.

        :param api_key: מפתח API לגישה ל-Gemini.
        :type api_key: str
        :param system_instruction: הוראה למודל (פרומפט מערכת).
        :type system_instruction: str
        :param model_name: שם מודל Gemini הנמצא בשימוש. ברירת המחדל היא 'gemini-2.0-flash-exp'.
        :type model_name: str
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)  # קונפיגורציה של הספרייה עם מפתח ה-API
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # אתחול המודל עם ההוראה

    def ask(self, q: str) -> str:
        """
        שליחת שאילתה למודל וקבלת מענה.

        :param q: טקסט השאילתה.
        :type q: str
        :return: מענה מהמודל או הודעת שגיאה.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q)  # שליחת שאילתה למודל
            return response.text  # קבלת המענה הטקסטואלי
        except Exception as ex:
            return f'Error: {str(ex)}'  # טיפול וקבלת השגיאה


# החלק הראשי של התוכנית
if __name__ == '__main__':
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # נתיב יחסי לספרייה
    base_path: Path = __root__ / relative_path  # נתיב מוחלט לספרייה באמצעות __root__


    # קריאת מפתח ה-API ממשתני הסביבה או בקשתו מהמשתמש
    API_KEY: str = os.getenv('API_KEY')
    if not API_KEY:
        API_KEY = input('מפתח ה-API לא נמצא. אנא הזן את מפתח ה-API עבור `gemini`: ')  # בקשת מפתח ה-API מהמשתמש
        # שמירת המפתח שהוזן בקובץ env.
        set_key('.env', 'API_KEY', API_KEY)

    instructions: dict = {
        '1': 'system_instruction_asterisk',
        '2': 'system_instruction_tilde',
        '3': 'system_instruction_hash',
    }

    # ברכת שלום למשתמש
    print('ברוכים הבאים למשחק Banner!')
    print('הזן טקסט, ואני אייצר עבורך באנר טקסטואלי.')

    while True:
        # בחירת סגנון העיצוב של הבאנר
        print('אנא בחר סגנון עיצוב לבאנר:')
        print('1. סימן \'*\'')
        print('2. סימן \'~\'')
        print('3. סימן \'#\'')
        choice = input('הזן את מספר הסגנון (1, 2 או 3): ')

        if choice in ('1', '2', '3'):
            system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # קריאת ההוראה מקובץ
        else:
            print('בחירה שגויה. נעשה שימוש בסגנון ברירת המחדל \'*\'')
            system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # קריאת הוראת ברירת המחדל

        # יצירת מופע של המחלקה עם ההוראה שנבחרה
        model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)

        # בקשת טקסט מהמשתמש
        user_text: str = input('הזן טקסט עבור הבאנר: ')

        # בדיקה שהטקסט אינו ריק
        if user_text.strip() == '':
            print('לא הזנת טקסט. אנא נסה שוב.')
        else:
            # שליחת הטקסט למודל וקבלת הבאנר המעוצב
            response = model.ask(user_text)
            print('\nהבאנר שלך מוכן:')
            print(response)