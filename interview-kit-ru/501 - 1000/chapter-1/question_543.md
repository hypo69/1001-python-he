### `question_543.md`

**שאלה 543.** מהם דקורטורים ב-Python ולשם מה הם משמשים? ספק דוגמת קוד המדגימה את השימוש בהם.

-   א. דקורטורים הם משתנים מיוחדים המשמשים לאחסון נתונים נוספים אודות פונקציות, מבלי לשנות את התנהגותן.
-   ב. דקורטורים הם פונקציות המשנות שמות של פונקציות אחרות והופכות את קריאותיהן לקצרות יותר.
-   ג. דקורטורים הם פונקציות המקבלות פונקציה אחרת כארגומנט, מרחיבות את פונקציונליותה ומחזירות פונקציה חדשה. הם מאפשרים להוסיף התנהגות לפונקציות מבלי לשנות את קוד המקור שלהן.
-   ד. דקורטורים הם דרכים להסתרת קוד כדי למנוע קריאתו ושינויו.

**תשובה נכונה: ג**

**הסבר:**

דקורטורים ב-Python הם כלי רב עוצמה ואלגנטי המאפשר לשנות התנהגות של פונקציות או מתודות מבלי לשנות את קוד המקור שלהן. הם מנצלים את קונספט הפונקציות מסדר גבוה (high-order functions), כלומר פונקציות שיכולות לקבל פונקציות אחרות כארגומנטים ולהחזיר אותן.

*   **רעיונות מרכזיים של דקורטורים:**
    *   דקורטור הוא פונקציה המקבלת פונקציה אחרת כארגומנט.
    *   הדקורטור מוסיף פונקציונליות חדשה לפונקציה המקבלת.
    *   הדקורטור מחזיר פונקציה חדשה (בדרך כלל "עטיפה" – wrapper) הכוללת את הפונקציונליות המורחבת.
    *   דקורטורים משתמשים בתחביר `@decorator_name` ליישום הדקורטור על פונקציה.

*   **יתרונות הדקורטורים:**
    *   **שימוש חוזר בקוד:** מאפשרים שימוש חוזר בלוגיקה (למשל, לוגינג, בדיקת הרשאות) עבור פונקציות שונות.
    *   **שינוי התנהגות:** מרחיבים פונקציונליות של פונקציות מבלי לשנות את קוד המקור שלהן (עקרון הפתיחות/סגירות).
    *   **פישוט קוד:** מסייעים להפוך את הקוד לקריא ומאורגן יותר באמצעות הפרדת אחריות.

**דוגמת קוד:**

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f'הפונקציה {func.__name__} נקראה') # The function ... was called
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def multiply(a,b):
  return a * b

add(2, 3) # ידפיס 'הפונקציה add נקראה' # Will print 'The function add was called'
multiply(4,5) # ידפיס 'הפונקציה multiply נקראה' # Will print 'The function multiply was called'
```
**תיאור הדוגמה:**

*   **`logger(func)`:** דקורטור המקבל פונקציה `func`.
    *   `wrapper(*args, **kwargs)`: פונקציה מקוננת שתשמש כ"עטיפה" לפונקציה המקורית.
    *   `print(f'הפונקציה {func.__name__} נקראה')`: מבצע רישום יומן (לוגינג) של קריאת הפונקציה.
    *   `return func(*args, **kwargs)`: קוראת לפונקציה המקורית ומחזירה את התוצאה שלה.

*   **`@logger`:** מיישם את הדקורטור `logger` על הפונקציות `add` ו-`multiply`.
*   כעת בעת קריאה ל-`add(2, 3)` או `multiply(4,5)` תחילה יקרא הדקורטור `logger`, שידפיס הודעה לקונסולה על איזו פונקציה נקראה, ולאחר מכן תיקרא הפונקציה עצמה שהועברה לדקורטור.

**ניתוח האפשרויות:**
*  **א. דקורטורים הם משתנים מיוחדים המשמשים לאחסון נתונים נוספים אודות פונקציות, מבלי לשנות את התנהגותן:** שגוי. דקורטורים הם פונקציות, לא משתנים.
*   **ב. דקורטורים הם פונקציות המשנות שמות של פונקציות אחרות והופכות את קריאותיהן לקצרות יותר:** שגוי. דקורטורים אינם משנים שמות של פונקציות.
*   **ג. דקורטורים הם פונקציות המקבלות פונקציה אחרת כארגומנט, מרחיבות את פונקציונליותה ומחזירות פונקציה חדשה. הם מאפשרים להוסיף התנהגות לפונקציות מבלי לשנות את קוד המקור שלהן:** נכון.
*   **ד. דקורטורים הם דרכים להסתרת קוד כדי למנוע קריאתו ושינויו:** שגוי. דקורטורים אינם מסתירים קוד, אלא הופכים אותו למאורגן יותר.

**לסיכום:**
*   דקורטורים מאפשרים להוסיף פונקציונליות חדשה לפונקציות "על עטיפה", מבלי לשנות את הקוד שלהן ישירות.
*   הם מהווים כלי חשוב לכתיבת קוד נקי, מודולרי וניתן לשימוש חוזר יותר ב-Python.

לפיכך, התשובה הנכונה היא **ג. דקורטורים הם פונקציות המקבלות פונקציה אחרת כארגומנט, מרחיבות את פונקציונליותה ומחזירות פונקציה חדשה. הם מאפשרים להוסיף התנהגות לפונקציות מבלי לשנות את קוד המקור שלהן.**