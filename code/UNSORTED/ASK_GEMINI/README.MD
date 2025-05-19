### הצגת שאלה למודל Gemini

להפעלת המערכת נדרש מפתח API.

ניתן לקבל מפתח API עבור המודל כאן: [https://aistudio.google.com/](https://aistudio.google.com/)




```python
import google.generativeai as genai

class GoogleGenerativeAI:
    """
    מחלקה לאינטראקציה עם מודלי Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """
        איניציאליזציה של מודל GoogleGenerativeAI.

        ארגומנטים:
            api_key (str): מפתח API לגישה למודל הגנרטיבי.
            model_name (str, optional): שם המודל לשימוש. ברירת המחדל היא "gemini-2.0-flash-exp".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        שולח שאילתת טקסט למודל ומחזיר את התשובה.

        ארגומנטים:
            q (str): השאלה שתישלח למודל.

        מחזיר:
            str: התשובה מהמודל.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"
```

### כיצד קוד זה פועל

1.  **ייבוא הספרייה**: אנו מייבאים את ספריית `google.generativeai`, המספקת ממשק לאינטראקציה עם מודלי Google AI.

2.  **מחלקה `GoogleGenerativeAI`**: מחלקה זו מאגדת את כל לוגיקת האינטראקציה עם מודל Gemini. היא מקבלת מפתח API ושם מודל כפרמטרים. כברירת מחדל נעשה שימוש במודל `gemini-2.0-flash-exp`.

3.  **מתודת `__init__`**: במתודה זו מתבצעת תצורת המודל. אנו מעבירים את מפתח ה-API ואת שם המודל, ולאחר מכן מאתחלים את אובייקט המודל.

4.  **מתודת `ask`**: מתודה זו שולחת שאילתת טקסט למודל ומחזירה את התשובה. אם משהו משתבש, המתודה תחזיר הודעת שגיאה.

### כיצד להשתמש?

```python
################################################################################
#                                                                              #
#             INSERT YOUR GEMINI API KEY                                       #
#                                                                              #
################################################################################

API_KEY: str = input("API key from `gemini`: ")
model = GoogleGenerativeAI(api_key=API_KEY)

q = input("Question: ")
response = model.ask(q)
print(response)
```

1.  **הכנסת מפתח API**: תחילה התוכנית מבקשת מהמשתמש את מפתח ה-API לגישה למודל Gemini. ניתן לקבל מפתח זה באתר [Google AI Studio](https://aistudio.google.com/).

2.  **יצירת אובייקט מודל**: אנו יוצרים אובייקט מהמחלקה `GoogleGenerativeAI`, ומעבירים לו את מפתח ה-API.

3.  **הכנסת שאלה**: המשתמש מכניס את שאלתו אותה הוא רוצה להציג למודל.

4.  **קבלת התשובה**: התוכנית שולחת את השאלה למודל ומדפיסה את התשובה על המסך.

### דוגמת שימוש

יש לכם מפתח API, ואתם רוצים לשאול את המודל: "כיצד לשפר את הקוד שלי?". כך זה ייראה:

```
API key from `gemini`: your_api_key
Question: איך לשפר את הקוד שלי?
Answer: לשיפור הקוד שלך, מומלץ לפעול על פי עקרונות קוד נקי, כגון שמות משתנים ופונקציות ברורים והגיוניים, שימוש בהערות להסבר לוגיקה מורכבת, ויישום עקרונות SOLID לתכנון מחלקות ומודולים.
```


ניתן להריץ את הקוד [כאן](https://colab.research.google.com/github/hypo69/101_python_computer_games_ru/blob/master/GAMES/AI/ASK_GEMINI/ask_gemini_ru.ipynb)