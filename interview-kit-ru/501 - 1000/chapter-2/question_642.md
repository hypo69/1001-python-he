### `question_642.md`

**שאלה 642.** ב-Python, כיצד ניתן לבדוק האם מחרוזת מורכבת אך ורק מתווים אלפאנומריים (תווי אלפבית וספרות)?

- A. השתמשו במתודה `isnumeric()`
- B. השתמשו במתודה `isalpha()`
- C. השתמשו במתודה `isalnum()`
- D. השתמשו במתודה `isdecimal()`

**תשובה נכונה: C**

**הסבר:**

ב-Python, לבדיקה האם מחרוזת מורכבת אך ורק מתווים אלפאנומריים (תווי אלפבית וספרות), נעשה שימוש במתודה המובנית `isalnum()`.

*   **מאפיינים עיקריים של המתודה `isalnum()`:**
    *   **אותיות וספרות:** מחזירה `True` אם כל התווים במחרוזת הם אותיות (מאלפביתים שונים) או ספרות (`0`–`9`), ו-`False` אחרת.
    *   **שילוב:** המחרוזת יכולה להכיל הן אותיות והן ספרות.
    *   **רווחים ותווים מיוחדים:** רווחים, סימני פיסוק ותווים אחרים אינם נחשבים אלפאנומריים.
    *   **מחרוזת:** מיושמת על אובייקטי מחרוזת.

*   **ההבדל בין `isalnum()`, `isdigit()`, ו-`isalpha()`:**
    *   `isalnum()`: - מחזירה `True` אם כל התווים במחרוזת הם אותיות או ספרות, ו-`False` אחרת
    *   `isdigit()`: - מחזירה `True` רק אם כל התווים הם ספרות (0-9)
    *   `isalpha()`: - מחזירה `True` אם כל התווים הם אותיות.

**דוגמאות:**

```python
# דוגמה 1: מחרוזת רק עם אותיות וספרות
string1 = 'abc123'
print(f"'{string1}'.isalnum(): {string1.isalnum()}") # יציג: True
print(f"'{string1}'.isalpha(): {string1.isalpha()}") # יציג False
print(f"'{string1}'.isnumeric(): {string1.isnumeric()}")  # יציג: False
print(f"'{string1}'.isdecimal(): {string1.isdecimal()}")   # יציג False

# דוגמה 2: מחרוזת עם תווי רווח
string2 = 'abc 123'
print(f"'{string2}'.isalnum(): {string2.isalnum()}")  # יציג: False
print(f"'{string2}'.isalpha(): {string2.isalpha()}")  # יציג: False
print(f"'{string2}'.isnumeric(): {string2.isnumeric()}") # יציג: False
print(f"'{string2}'.isdecimal(): {string2.isdecimal()}") # יציג False
# דוגמה 3: מחרוזת עם תווים מיוחדים
string3 = 'abc-123'
print(f"'{string3}'.isalnum(): {string3.isalnum()}")   # יציג: False

# דוגמה 4: מחרוזת רק עם אותיות
string4 = "hello"
print(f"'{string4}'.isalnum(): {string4.isalnum()}") # יציג: True
print(f"'{string4}'.isalpha(): {string4.isalpha()}") # יציג: True
# דוגמה 5: מחרוזת רק עם ספרות
string5 = '1234'
print(f"'{string5}'.isalnum(): {string5.isalnum()}") # יציג: True
print(f"'{string5}'.isnumeric(): {string5.isnumeric()}") # יציג True
print(f"'{string5}'.isdigit(): {string5.isdigit()}") # יציג True
print(f"'{string5}'.isdecimal(): {string5.isdecimal()}") # יציג True
```

**ניתוח האפשרויות:**
*   **A. השתמשו במתודה `isnumeric()`:** שגוי. מתודה זו בודקת האם המחרוזת מורכבת אך ורק מתווים מספריים (לדוגמה "123"), אך לא מתווים אלפאנומריים.
*   **B. השתמשו במתודה `isalpha()`:** שגוי. מתודה זו בודקת האם המחרוזת מורכבת אך ורק מאותיות, אך לא מספרות.
*   **C. השתמשו במתודה `isalnum()`:** נכון.
*   **D. השתמשו במתודה `isdecimal()`:** שגוי, מכיוון שהמתודה בודקת רק תווים של מספרים עשרוניים.

**לסיכום:**
*   המתודה `isalnum()` מאפשרת לבדוק האם מחרוזת מורכבת אך ורק מאותיות וספרות.
*   רווחים ותווים אחרים אינם נחשבים אלפאנומריים.
*   מתודות שונות כמו `isnumeric()`, `isdigit()`, `isdecimal()` מאפשרות לבדוק מחרוזות לייצוג מספרי.

לפיכך, התשובה הנכונה היא **C. השתמשו במתודה `isalnum()`.**