import google.generativeai as genai  # ייבוא ספריית לעבודה עם Gemini
import re  # ייבוא ספריית לעבודה עם ביטויים רגולריים

class GoogleGenerativeAI:
    """
    מחלקה לאינטראקציה עם מודלים של Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, system_instruction: str = "", model_name: str = "gemini-2.0-flash-exp"):
        """
        אתחול מודל GoogleGenerativeAI.

        Args:
            api_key: מפתח API לגישה ל-Gemini.
            system_instruction: הוראה למודל (פרומפט מערכת).
            model_name: שם מודל ה-Gemini הנמצא בשימוש.
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)  # מגדירים את הספרייה עם מפתח ה-API
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction) # מאתחלים את המודל עם ההוראה

    def ask(self, q: str) -> str:
        """
        שולח בקשה למודל ומחזיר תשובה.

        Args:
            q: טקסט הבקשה.

        Returns:
            תשובת המודל או הודעת שגיאה.
        """
        try:
            response = self.model.generate_content(q)  # שולחים בקשה למודל
            return response.text  # מחזירים את התשובה הטקסטואלית
        except Exception as ex:
            return f"Error: {str(ex)}"  # מטפלים בשגיאה ומחזירים אותה

# הוראה ל-Gemini (פרומפט מערכת)
system_instruction = """
את/ה מחולל אנאגרמות. משימתך היא למצוא מילה קיימת בשפה הרוסית, המורכבת מאוסף אותיות נתון (באמצעות כולן או חלקן).

כללים:

1. התעלם/י מכל התווים למעט אותיות רוסיות. ספרות ותווים אחרים אינם נלקחים בחשבון.
2. אם ניתן להרכיב מספר מילים מהאותיות הנתונות, החזר/י אחת מהן.
3. אם לא ניתן להרכיב אף מילה בשפה הרוסית מהאותיות הנתונות, החזר/י את התשובה "Нет анаграмм".
4. אל תייצר/י נאולוגיזמים או מילים מומצאות. השתמש/י רק במילים קיימות בשפה הרוסית.
5. אל תסביר/י את התהליך, פשוט החזר/י את המילה או "Нет анаграмм".
"""

API_KEY: str = input("מפתח API מ-`gemini`: ")  # מבקשים את מפתח ה-API מהמשתמש
model = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction) # יוצרים מופע של המחלקה, מעבירים את מפתח ה-API וההוראה

if __name__ == "__main__":
    while True:  # לולאה אינסופית לקבלת בקשות
        q = input("הכנס/י אותיות שלפיהן Gemini תמצא אנאגרמה (לסיום לחץ/י Ctrl+C): ")
        # ניקוי הקלט מתווים שאינם קיריליים
        q = re.sub(r"[^а-яА-ЯёЁ]", "", q) # מסירים את כל התווים מלבד אותיות רוסיות
        if not q: # בודקים אם המחרוזת נשארה ריקה לאחר הניקוי
            print("הוזנו תווים לא תקינים. הכנס/י אותיות רוסיות.")
            continue # עוברים לאיטרציה הבאה של הלולאה
        response = model.ask(q) # שולחים בקשה למודל
        print(response) # מדפיסים את תשובת המודל