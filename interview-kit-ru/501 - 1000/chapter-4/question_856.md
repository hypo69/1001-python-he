### `question_865.md`

**שאלה 856.** ב-Python, בעת שימוש במתודת `format()` לעיצוב מחרוזות, מהי מטרת דגלי ההמרה המפורשים `!r` ו-`!s` ובמה הם שונים זה מזה?

A. `!r` ממיר את הערך למחרוזת באמצעות הפונקציה `str()`, ו-`!s` ממיר את הערך למחרוזת באמצעות הפונקציה `repr()`.
B. `!r` ממיר את הערך למחרוזת באמצעות הפונקציה `repr()`, ו-`!s` ממיר את הערך למחרוזת באמצעות הפונקציה `str()`.
C. `!r` ו-`!s` מבצעים את אותה פעולה – ממירים את הערך למחרוזת, אך `!r` מוסיף רווחים נוספים.
D. `!r` ו-`!s` משמשים רק עבור מספרים ואין להם השפעה על מחרוזות.

**תשובה נכונה: B**

**הסבר:**

ב-Python, בעת שימוש במתודת `format()` לעיצוב מחרוזות, דגלי ההמרה המפורשים `!r` ו-`!s` משמשים לציון האופן המדויק שבו יש להמיר את הערך למחרוזת לפני העיצוב.

*   **`!r` (repr())**:
    *   משתמש בפונקציה `repr()` להמרת הערך למחרוזת.
    *   הפונקציה `repr()` מחזירה את הייצוג המחרוזתי *הרשמי* של האובייקט, שאם אפשר, צריך להיות כזה שניתן להשתמש בו ליצירת אובייקט חדש מאותו סוג. לעיתים קרובות, אך לא תמיד, כולל גרשיים ותווים מיוחדים אחרים. מתאים לניפוי שגיאות (debugging).

*   **`!s` (str())**:
    *   משתמש בפונקציה `str()` להמרת הערך למחרוזת.
    *   הפונקציה `str()` מחזירה את הייצוג המחרוזתי *הבלתי רשמי*, או *הנוח למשתמש* של האובייקט. מתאים להצגה למשתמש.

*   **אפשרות A אינה נכונה:** ההפך נכון, `!r` משתמש ב-`repr()`, ו-`!s` משתמש ב-`str()`.
*   **אפשרות B נכונה:** זהו התיאור הנכון של התנהגות דגלי ההמרה המפורשים.
*   **אפשרות C אינה נכונה:** `!r` ו-`!s` מבצעים פעולות שונות, ולא סתם מוסיפים רווחים.
*   **אפשרות D אינה נכונה:** `!r` ו-`!s` ניתנים לשימוש עם כל סוגי הנתונים, לא רק עם מספרים.

**דוגמה:**

```python
name = "Alice"
age = 30

print(f"Name (str): {name!s}, Age (str): {age!s}")  # Name (str): Alice, Age (str): 30
print(f"Name (repr): {name!r}, Age (repr): {age!r}") # Name (repr): 'Alice', Age (repr): 30

print("Value with !s: {0!s}, Value with !r: {0!r}".format("Hello"))
# Value with !s: Hello, Value with !r: 'Hello'
```
**תוצאה:**

הדגל `!r` משתמש ב-`repr()` כדי להמיר את הערך למחרוזת (לעתים קרובות מוסיף גרשיים ופרטים אחרים), בעוד שהדגל `!s` משתמש ב-`str()`, מה שמניב פלט "ידידותי" יותר.

לפיכך, אפשרות B היא התשובה הנכונה.