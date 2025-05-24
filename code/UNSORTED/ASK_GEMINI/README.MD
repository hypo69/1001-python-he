### שאל את מודל Gemini

לצורך עבודה נדרש מפתח API.

ניתן להשיג מפתח API למודל כאן: [https://aistudio.google.com/](https://aistudio.google.com/)

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
        אתחול מודל GoogleGenerativeAI.

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
            q (str): השאלה שתשלח למודל.

        מחזירה:
            str: התשובה מהמודל.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"
```

### כיצד קוד זה פועל

1.  **ייבוא ספרייה**: אנו מייבאים את ספריית `google.generativeai`, המספקת ממשק לאינטראקציה עם מודלי Google AI.

2.  **מחלקה `GoogleGenerativeAI`**: מחלקה זו עוטפת את כל הלוגיקה של אינטראקציה עם מודל Gemini. היא מקבלת את מפתח ה-API ואת שם המודל כפרמטרים. כברירת מחדל, נעשה שימוש במודל `gemini-2.0-flash-exp`.

3.  **מתודה `__init__`**: במתודה זו מתבצעת הגדרת המודל. אנו מעבירים את מפתח ה-API ואת שם המודל, ולאחר מכן מאתחלים אובייקט מודל.

4.  **מתודה `ask`**: מתודה זו שולחת שאילתת טקסט למודל ומחזירה את התשובה. אם משהו משתבש, המתודה תחזיר הודעת שגיאה.

### כיצד להשתמש?

```python
################################################################################
#                                                                              #
#             INSERT YOUR GEMINI API KEY                                       #
#                                                                              #
################################################################################

API_KEY: str = input("API ключ от `gemini`: ")
model = GoogleGenerativeAI(api_key=API_KEY)

q = input("Вопрос: ")
response = model.ask(q)
print(response)
```

1.  **הזנת מפתח API**: ראשית, התוכנית מבקשת מהמשתמש את מפתח ה-API לגישה למודל Gemini. ניתן לקבל מפתח זה באתר [Google AI Studio](https://aistudio.google.com/).

2.  **יצירת אובייקט מודל**: אנו יוצרים אובייקט של המחלקה `GoogleGenerativeAI`, ומעבירים אליו את מפתח ה-API.

3.  **הזנת שאלה**: המשתמש מזין את שאלתו אותה הוא רוצה להפנות למודל.

4.  **קבלת תשובה**: התוכנית שולחת את השאלה למודל ומדפיסה את התשובה על המסך.

### דוגמה לשימוש

ברשותכם מפתח API, ואתם רוצים לשאול את המודל: "כיצד לשפר את הקוד שלי?". כך זה ייראה:

```
API ключ от `gemini`: המפתח_api_שלך
Вопрос: Как улучшить мой код?
Ответ: עבור שיפור הקוד שלך מומלץ לעקוב אחר עקרונות קוד נקי, כגון מתן שמות למשתנים ופונקציות בצורה ברורה והגיונית, שימוש בהערות להסברת לוגיקה מורכבת, וכן יישום עקרונות SOLID לעיצוב מחלקות ומודולים.
```

ניתן להפעיל את הקוד [כאן](https://colab.research.google.com/github/hypo69/101_python_computer_games_ru/blob/master/GAMES/AI/ASK_GEMINI/ask_gemini_ru.ipynb)