# BANNER AI
מודל Gemini מחזיר תשובה בצורת באנר ASCII בהתאם להנחיה הניתנת לו.

 התוכנית מקיימת אינטראקציה עם מודל Google Generative AI ליצירת באנרים טקסטואליים.
 המשתמש יכול לבחור את סגנון עיצוב הבאנר ולשלוח למודל טקסט לעיבוד.

## התקנת תלויות
להרצת הקוד על מכונה מקומית, תידרש התקנת ספריות google.

```python
pip install google
pip install google-generativeai
```

מומלץ בחום לבצע את כל הניסויים בסביבה וירטואלית.

## מאפייני הקוד בתוכנית זו
1. הנחיות מאוחסנות בקבצים שונים ונטענות לפי הצורך.
2. החל מדוגמה זו, אני שומר את המפתח של המודל במשתנה סביבה, מה שחוסך לי את הצורך להזין את המפתח שוב ושוב.
3. אני משתמש בנתיבים מוחלטים לקבצים.
    לקביעת ספריית השורש של הפרויקט, אני מחפש רקורסיבית כלפי מעלה קבצי סמן ('pyproject.toml', 'requirements.txt', '.git').
    את הספרייה שנמצאה אני מאחסן במשתנה `__root__`. ממנה אני בונה את הנתיב להנחיות המערכת:
    ```python
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # נתיב יחסי לספרייה
    base_path: Path = __root__ / relative_path  # נתיב מוחלט לספרייה באמצעות __root__
    ```

### 1. **ייבוא ספריות נחוצות**
```python
import google.generativeai as genai  # ייבוא ספרייה לעבודה עם Gemini
import re  # ייבוא ספרייה לעבודה עם ביטויים רגולריים
from pathlib import Path  # ייבוא לעבודה עם נתיבי מערכת קבצים
from header import __root__  # ייבוא אובייקט __root__, המכיל נתיב מוחלט לשורש הפרויקט
from dotenv import load_dotenv, set_key  # ייבוא פונקציות לעבודה עם משתני סביבה
import os  # ייבוא לעבודה עם משתני סביבה
```

- **`google.generativeai`**: משמש ליצירת אינטראקציה עם API של Google Generative AI.
- **`re`**: ספרייה לעבודה עם ביטויים רגולריים (אינה בשימוש בקוד זה, אך עשויה להיות שימושית בעתיד).
- **`Path`**: מאפשרת עבודה עם נתיבי מערכת קבצים.
- **`__root__`**: אובייקט המכיל את הנתיב המוחלט לשורש הפרויקט.
- **`dotenv`**: מאפשר טעינת משתני סביבה מקובץ `.env` ושמירתם.
- **`os`**: משמש לעבודה עם משתני סביבה.

---

### 2. **טעינת משתני סביבה**
```python
load_dotenv()
```
- הפונקציה `load_dotenv()` טוענת משתני סביבה מקובץ `.env`, אם הוא קיים.

---

### 3. **מחלקה `GoogleGenerativeAI`**
המחלקה מיועדת ליצירת אינטראקציה עם מודל Google Generative AI.

#### 3.1. **מאפייני המחלקה**
```python
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b'
]
```
- רשימת המודלים הזמינים של Google Generative AI.

#### 3.2. **מתודת `__init__`**
```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
    """
    אתחול מודל GoogleGenerativeAI.

    :param api_key: מפתח API לגישה ל-Gemini.
    :type api_key: str
    :param system_instruction: הנחיה למודל (פרומפט מערכת).
    :type system_instruction: str
    :param model_name: שם מודל Gemini הנמצא בשימוש. ברירת מחדל 'gemini-2.0-flash-exp'.
    :type model_name: str
    """
    self.api_key = api_key
    self.model_name = model_name
    genai.configure(api_key=self.api_key)  # הגדרת הספרייה עם מפתח ה-API
    self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # אתחול המודל עם ההנחיה
```
- **`api_key`**: מפתח API לגישה ל-Google Generative AI.
- **`system_instruction`**: הנחיה למודל (לדוגמה, סגנון עיצוב טקסט).
- **`model_name`**: שם המודל, ברירת המחדל היא `'gemini-2.0-flash-exp'`.
- **`genai.configure(api_key=self.api_key)`**: הגדרת הספרייה באמצעות מפתח ה-API.
- **`genai.GenerativeModel(...)`**: אתחול המודל עם הפרמטרים שצוינו.

#### 3.3. **מתודת `ask`**
```python
def ask(self, q: str) -> str:
    """
    שליחת שאילתה למודל וקבלת תשובה.

    :param q: טקסט השאילתה.
    :type q: str
    :return: תשובת המודל או הודעת שגיאה.
    :rtype: str
    """
    try:
        response = self.model.generate_content(q)  # שליחת השאילתה למודל
        return response.text  # קבלת התשובה הטקסטואלית
    except Exception as ex:
        return f'Error: {str(ex)}'  # טיפול בשגיאה וקבלת פרטיה
```
- **`q`**: טקסט השאילתה הנשלחת למודל.
- **`self.model.generate_content(q)`**: שליחת השאילתה למודל.
- **`response.text`**: קבלת התשובה הטקסטואלית מהמודל.
- **`except Exception as ex`**: טיפול בשגיאות והחזרת הודעת שגיאה.

---

### 4. **חלק עיקרי של התוכנית**
```python
if __name__ == '__main__':
```
- בדיקה שהתוכנית מורצת כסקריפט עצמאי.

#### 4.1. **הגדרת נתיבים**
```python
relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # נתיב יחסי לספרייה
base_path: Path = __root__ / relative_path  # נתיב מוחלט לספרייה באמצעות __root__
```
- **`relative_path`**: נתיב יחסי לספרייה בתוך הפרויקט.
- **`base_path`**: נתיב מוחלט, המתקבל על ידי איחוד `__root__` ו-`relative_path`.

#### 4.2. **קריאת מפתח API**
```python
API_KEY: str = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')  # Запрос API ключа у пользователя
    set_key('.env', 'API_KEY', API_KEY)  # Сохранение ключа в файл .env
```
- **`os.getenv('API_KEY')`**: ניסיון לקבל את מפתח ה-API ממשתני הסביבה.
- אם המפתח לא נמצא, מבקשים אותו מהמשתמש באמצעות `input`.
- **`set_key('.env', 'API_KEY', API_KEY)`**: שומרים את המפתח שהוזן בקובץ `.env` לשימוש עתידי.

#### 4.3. **הנחיות למודל**
```python
instructions: dict = {
    '1': 'system_instruction_asterisk',
    '2': 'system_instruction_tilde',
    '3': 'system_instruction_hash',
}
```
- מילון המכיל שמות קבצים עם הנחיות למודל.

#### 4.4. **ברכת המשתמש**
```python
print('Добро пожаловать в игру Banner!')
print('Введите текст, и я создам для вас текстовый баннер.')
```
- ברכת המשתמש והסבר על פונקציונליות התוכנית.

#### 4.5. **לולאה לבחירת סגנון הבאנר**
```python
while True:
    print('Выберите стиль оформления баннера:')
    print('1. Символ \'*\'')
    print('2. Символ \'~\'')
    print('3. Символ \'#\'')
    choice = input('Введите номер стиля (1, 2 или 3): ')
```
- המשתמש בוחר את סגנון עיצוב הבאנר.

#### 4.6. **קריאת ההנחיה למודל**
```python
if choice in ('1', '2', '3'):
    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # Чтение инструкции из файла
else:
    print('Неверный выбор. Используется стиль по умолчанию \'*\'')
    system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # Чтение инструкции по умолчанию
```
- אם הבחירה תקינה, קוראים את ההנחיה המתאימה מהקובץ.
- אם הבחירה אינה תקינה, משתמשים בהנחיית ברירת המחדל.

#### 4.7. **יצירת מופע של המחלקה**
```python
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
```
- יוצרים מופע של המחלקה `GoogleGenerativeAI` עם הפרמטרים שצוינו.

#### 4.8. **בקשת טקסט מהמשתמש**
```python
user_text: str = input('Введите текст для баннера: ')
```
- המשתמש מזין טקסט לבאנר.

#### 4.9. **בדיקת הטקסט**
```python
if user_text.strip() == '':
    print('Вы не ввели текст. Попробуйте снова.')
else:
    response = model.ask(user_text)
    print('\nВаш баннер готов:')
    print(response)
```
- אם הטקסט ריק, מציגים הודעת שגיאה.
- אם הוזן טקסט, שולחים אותו למודל ומציגים את התוצאה.