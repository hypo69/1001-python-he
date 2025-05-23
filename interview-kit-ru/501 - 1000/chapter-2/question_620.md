### `question_620.md`

**שאלה 620.** מה ההבדל בין מודול לחבילה ב-Python?

-   א. מודול הוא רק קובץ Python ניתן להרצה, וחבילה היא קוד מקומפל.
-   ב. מודול הוא ספרייה עם קבצי `.py`, וחבילה היא קובץ `.py` בודד.
-   ג. מודול הוא קובץ נפרד או אוסף של קבצים המיובאים יחד, וחבילה היא ספרייה המכילה מודולים.
-   ד. מודול מכיל רק הגדרות פונקציות, וחבילה יכולה להכיל גם הגדרות מחלקות.

**תשובה נכונה: ג**

**הסבר:**

ב-Python, מודולים וחבילות הם הדרכים העיקריות לארגן ולבנות קוד. הם מאפשרים לפצל פרויקטים גדולים לחלקים קטנים יותר, ניתנים לניהול ולשימוש חוזר.

*   **מודול:**
    *   **קובץ בודד (או מספר קבצים):** מודול הוא קובץ נפרד עם סיומת `.py` המכיל קוד ב-Python.
    *   **הגדרות:** יכול להכיל הגדרות של משתנים, פונקציות, מחלקות ואלמנטים אחרים של Python.
    *   **ייבוא:** מודול מיובא באמצעות מילת המפתח `import`, וניתן להשתמש בפונקציות ובמחלקות שלו בקוד אחר.
    *   **דוגמה:** `import my_module`.
    *   מודול יכול להכיל גם אוסף של קבצים המיובאים יחד, אך הם נמצאים באותה ספרייה.
*   **חבילה:**
    *   **ספרייה עם מודולים:** חבילה היא ספרייה המכילה מודולים (קבצי `.py`) וחבילות אחרות.
    *   **קובץ `__init__.py`:** חבילה חייבת להכיל קובץ בשם `__init__.py`, שיכול להיות ריק, אך הוא מודיע למפרש Python שהתיקייה הנוכחית היא חבילה.
    *   **מבנה היררכי:** יכולה להיות בעלת מבנה היררכי, המאפשר לארגן קוד ברמה גבוהה יותר.
    *   **ייבוא:** מודולים וחבילות בתוך חבילה ניתנים לייבוא באמצעות האופרטור `from package import module`, לדוגמה, `from sklearn import cross_validation`.

**דוגמאות:**

```python
# דוגמה למודול
# קובץ my_module.py
def greet(name):
    print(f"Hello, {name}!")

# קובץ main.py
import my_module
my_module.greet("John")

# דוגמה לחבילה
# my_package/
#     __init__.py
#     module1.py
#     module2.py

# קובץ my_package/module1.py
def function1():
  print("function1 from module 1")

# קובץ my_package/module2.py
def function2():
  print("function2 from module 2")
# קובץ main.py

from my_package import module1
from my_package import module2

module1.function1()
module2.function2()

```

**ניתוח האפשרויות:**
*   **א. מודול הוא רק קובץ Python ניתן להרצה, וחבילה היא קוד מקומפל.:** שגוי.
*   **ב. מודול הוא ספרייה עם קבצי `.py`, וחבילה היא קובץ `.py` בודד.:** שגוי.
*   **ג. מודול הוא קובץ נפרד או אוסף של קבצים המיובאים יחד, וחבילה היא ספרייה המכילה מודולים.:** נכון.
*   **ד. מודול מכיל רק הגדרות פונקציות, וחבילה יכולה להכיל גם הגדרות מחלקות.:** שגוי.

**לסיכום:**
*   מודולים מייצגים קבצי קוד, בעוד שחבילות הן ספריות המכילות מודולים.
*   חבילות מאפשרות לארגן קוד במבנה היררכי.

לכן, התשובה הנכונה היא **ג. מודול הוא קובץ נפרד או אוסף של קבצים המיובאים יחד, וחבילה היא ספרייה המכילה מודולים.**