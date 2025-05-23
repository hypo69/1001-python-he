### `question_588.md`

**שאלה 588.** כיצד מבוצעת אינטרפולציית מחרוזות ב-Python? ציין/י לפחות שלוש דרכים לאינטרפולציית מחרוזות, מבלי להשתמש בקלאס `Template`.

-   א. אינטרפולציית מחרוזות ב-Python יכולה להתבצע רק באמצעות הקלאס `Template`.
-   ב. אינטרפולציית מחרוזות ב-Python יכולה להתבצע באמצעות שרשור (האופרטור +) והמתודה `join()`.
-   ג. אינטרפולציית מחרוזות ב-Python יכולה להתבצע באמצעות f-strings, האופרטור `%` והמתודה `format()`.
-   ד. אינטרפולציית מחרוזות אינה נתמכת ב-Python.

**תשובה נכונה: ג**

**הסבר:**

אינטרפולציית מחרוזות (או עיצוב מחרוזות) היא תהליך של הטמעת ערכי משתנים בתוך מחרוזת. Python מספקת מספר דרכים לאינטרפולציית מחרוזות, מלבד השימוש בקלאס `Template`.

*   **דרכים עיקריות לאינטרפולציית מחרוזות ב-Python:**
    1.  **f-strings (ליטרלים של מחרוזות מעוצבות):**
        *   משתמשים בקידומת `f` לפני המחרוזת.
        *   משתנים או ביטויים מוכנסים בתוך סוגריים מסולסלים `{}` בתוך המחרוזת.
        *   פועלים מהר יותר משיטות אחרות.
        *   דוגמה: `f'Hello {name}'`.
    2.  **האופרטור `%` (אופרטור המודולו):**
        *   משתמש במצייני פורמט `%s` (למחרוזות), `%d` (למספרים שלמים), `%f` (למספרים עשרוניים).
        *   הערכים להחלפה מועברים בטופל לאחר האופרטור `%`.
        *   דוגמה: `'Hey %s' % name`.
    3.  **המתודה `format()`:**
        *   משתמשת בסוגריים מסולסלים `{}` כפלייסהולדרים במחרוזת.
        *   הערכים המוחלפים מועברים כארגומנטים לפונקציה `format()`.
        *   יכולה להשתמש בפלייסהולדרים פוזיציונליים ובעלי שם.
        *   דוגמה: `"My name is {}".format(name)`.
        *   שיטה גמישה יותר בהשוואה לאופרטור `%`.

**דוגמאות:**

```python
name = 'Chris'
age = 30
city = "New York"

# 1. f-strings
print(f'Hello {name}, your age is {age}') # פלט: Hello Chris, your age is 30
print(f'Hello {name.upper()}, you live in {city.lower()}') # פלט: Hello CHRIS, you live in new york
# 2. % operator
print('Hey %s %s' % (name, name)) # פלט: Hey Chris Chris
print('My age is %d, and my name is %s' % (age, name)) # פלט: My age is 30, and my name is Chris
print("My city is %s and I am %d old" % (city, age)) # פלט: My city is New York and I am 30 old
# 3. format
print("My name is {}".format(name))  # פלט: My name is Chris
print("I am {} years old and live in {}".format(age, city)) # פלט: I am 30 years old and live in New York

# דוגמאות עם פלייסהולדרים בעלי שם ב-format
print("Hello, my name is {name} and I live in {city}".format(name=name,city=city))
```

**ניתוח האפשרויות:**
*   **א. אינטרפולציית מחרוזות ב-Python יכולה להתבצע רק באמצעות הקלאס `Template`. :** שגוי.
*   **ב. אינטרפולציית מחרוזות ב-Python יכולה להתבצע באמצעות שרשור (האופרטור +) והמתודה `join()`. :** שגוי, למרות שגם אלו יכולים לשמש לצירוף מחרוזות, זה אינו נחשב לאינטרפולציית מחרוזות.
*   **ג. אינטרפולציית מחרוזות ב-Python יכולה להתבצע באמצעות f-strings, האופרטור `%` והמתודה `format()`. :** נכון.
*   **ד. אינטרפולציית מחרוזות אינה נתמכת ב-Python. :** שגוי.

**לסיכום:**
*   Python מספקת מספר דרכים להטמעת משתנים במחרוזות.
*   f-strings תמציתיות וקלות יותר לשימוש.
*   המתודה `format()` גמישה יותר מהאופרטור `%`.

לפיכך, התשובה הנכונה היא **ג. אינטרפולציית מחרוזות ב-Python יכולה להתבצע באמצעות f-strings, האופרטור `%` והמתודה `format()`**.