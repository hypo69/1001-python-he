import google.generativeai as genai  # ייבוא הספרייה לעבודה עם Gemini
import re  # ייבוא הספרייה לעבודה עם ביטויים רגולריים

class GoogleGenerativeAI:
    """
    מחלקה לאינטראקציה עם מודלי Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, system_instruction: str = "", model_name: str = "gemini-2.0-flash-exp"):
        """
        אתחול מודל GoogleGenerativeAI.

        ארגומנטים:
            api_key: מפתח ה-API לגישה ל-Gemini.
            system_instruction: הוראה למודל (פרומפט מערכת).
            model_name: שם מודל Gemini שבו משתמשים.
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)  # מגדיר את הספרייה עם מפתח ה-API
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction) # מאתחל את המודל עם ההוראה

    def ask(self, q: str) -> str:
        """
        שולח שאילתה למודל ומחזיר את התשובה.

        ארגומנטים:
            q: טקסט השאילתה.

        מחזיר:
            תשובת המודל או הודעת שגיאה.
        """
        try:
            response = self.model.generate_content(q)  # שולח את השאילתה למודל
            return response.text  # מחזיר את התשובה כטקסט
        except Exception as ex:
            return f"Error: {str(ex)}"  # מטפל ומחזיר את השגיאה

# הוראה עבור Gemini (פרומפט מערכת)
system_instruction = """
את/ה מחולל אנאגרמות. משימתך היא למצוא מילה קיימת בשפה הרוסית מתוך קבוצת אותיות נתונה (שימוש בכל האותיות או בחלקן).

כללים:

1. התעלם/התעלמי מכל תווים פרט לאותיות רוסיות. ספרות ותווים אחרים אינם נלקחים בחשבון.
2. אם ניתן להרכיב מספר מילים מהאותיות הנתונות, החזר/החזירי אחת מהן.
3. אם לא ניתן להרכיב אף מילה בשפה הרוסית מהאותיות הנתונות, החזר/החזירי את התשובה "Нет анаграмм".
4. אל תייצר/תייצרי מילים חדשות או מילים מומצאות. השתמש/י רק במילים קיימות בשפה הרוסית.
5. אל תסביר/י את התהליך, פשוט החזר/החזירי את המילה או את "Нет анаграмм".
"""

API_KEY: str = input("מפתח API מ-`gemini`: ")  # מבקש את מפתח ה-API מהמשתמש
model = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction) # יוצר מופע של המחלקה, מעביר את מפתח ה-API וההוראה

if __name__ == "__main__":
    while True:  # לולאה אינסופית לקליטת שאילתות
        q = input("הכנס אותיות שעבורן Gemini ימצא אנאגרמה (ליציאה לחץ על Ctrl+C): ")
        # ניקוי הקלט מתווים שאינם קיריליים
        q = re.sub(r"[^а-яА-ЯёЁ]", "", q) # מסיר את כל התווים מלבד אותיות רוסיות
        if not q: # בודק אם המחרוזת נשארה ריקה לאחר הניקוי
            print("הוזנו תווים לא תקינים. אנא הכנס אותיות רוסיות.")
            continue # עובר לאיטרציה הבאה של הלולאה
        response = model.ask(q) # שולח את השאילתה למודל
        print(response) # מדפיס את תשובת המודל