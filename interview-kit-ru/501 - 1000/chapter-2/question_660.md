### question_640.md

**שאלה 640.** כיצד ב-Python ניתן לבדוק האם מחרוזת מורכבת אך ורק מתווים מספריים?

-   א. השתמשו במתודה `isdigit()`.
-   ב. השתמשו במתודה `isnumeric()`.
-   ג. השתמשו במתודה `isdecimal()`.
-   ד. השתמשו בפונקציה `is_number()`.

**תשובה נכונה: ב**

**הסבר:**

ב-Python, לבדיקה האם מחרוזת מורכבת אך ורק מתווים מספריים, נעשה שימוש במתודה `isnumeric()`. חשוב לציין כי המתודה `isdigit()` תחזיר `False` עבור מחרוזות המכילות תווים שהינם ספרות במערכות ספירה אחרות.

*   **המתודה `isnumeric()`:**
    *   **בדיקת ייצוג מספרי:** מחזירה `True` אם כל התווים במחרוזת הינם תווים מספריים (כולל תווי ספרות מאלפביתים שונים, לדוגמה, ספרות ערביות ורומיות).
    *   **מחזירה `False`:** מחזירה `False` אם המחרוזת אינה מורכבת אך ורק מתווים מספריים.
    *   **אינה מתחשבת ברווחים:** תווים ריקים (רווחים) מחזירים `False`, לכן אם יש צורך לעבד מחרוזת עם רווחים, יש להסיר אותם קודם.
    *   **מחרוזת:** מיושמת על אובייקטי מחרוזת.

*   **ההבדל בין `isnumeric()` לבין `isdigit()`:**
    *   `isdigit()` - בודקת שהמחרוזת מורכבת אך ורק מתווי הספרות `0`-`9`.
    *   `isnumeric()` - בודקת שהמחרוזת מורכבת אך ורק מתווים מספריים, כולל מאלפביתים אחרים (`½,³, ⅕`).
*   **המתודה `isdecimal()`:**
    *   המתודה `isdecimal()` בודקת שכל תווי המחרוזת הינם ספרות עשרוניות (לדוגמה `0` - `9`).
    *   מחזירה `True` רק עבור מחרוזות המכילות תווים שניתן להשתמש בהם לכתיבת מספרים שלמים במערכת הספירה העשרונית, לדוגמה `"\u0031\u0032\u0033"`.

**דוגמאות:**

```python
# Example 1: String with only digits
string1 = '123456'
print(f"'{string1}'.isnumeric(): {string1.isnumeric()}")  # Output: True
print(f"'{string1}'.isdigit(): {string1.isdigit()}")  # Output: True
print(f"'{string1}'.isdecimal(): {string1.isdecimal()}") # Output True

# Example 2: String with letters
string2 = '123a'
print(f"'{string2}'.isnumeric(): {string2.isnumeric()}")  # Output: False
print(f"'{string2}'.isdigit(): {string2.isdigit()}")   # Output: False
print(f"'{string2}'.isdecimal(): {string2.isdecimal()}") # Output False

# Example 3: String with whitespace characters
string3 = '123 45'
print(f"'{string3}'.isnumeric(): {string3.isnumeric()}")  # Output: False

# Example 4: Character from another script
string4 = "½"
print(f"'{string4}'.isnumeric(): {string4.isnumeric()}")  # Output: True
print(f"'{string4}'.isdigit(): {string4.isdigit()}")  # Output: False
print(f"'{string4}'.isdecimal(): {string4.isdecimal()}")  # Output: False
# Example 5: String with Unicode decimal characters
string5 = "\u0031\u0032\u0033"
print(f"'{string5}'.isnumeric(): {string5.isnumeric()}") # Output: True
print(f"'{string5}'.isdigit(): {string5.isdigit()}") # Output True
print(f"'{string5}'.isdecimal(): {string5.isdecimal()}") # Output True

```

**ניתוח האפשרויות:**
*   **א. השתמשו במתודה `isdigit()`:** שגוי, מכיוון שהמתודה אינה מזהה שמחרוזת מורכבת מתווים מספריים *מאלפביתים שונים.*
*   **ב. השתמשו במתודה `isnumeric()`:** נכון.
*   **ג. השתמשו במתודה `isdecimal()`.:** שגוי, מכיוון שהמתודה בודקת שכל תווי המחרוזת הינם ספרות עשרוניות (0 - 9).
*   **ד. השתמשו בפונקציה `is_number()`.:** שגוי.

**לסיכום:**
*   המתודה `isnumeric()` מחזירה `True` אם כל התווים במחרוזת הינם מספריים, כולל מאלפביתים אחרים.
*   אם יש צורך לבדוק רק את התווים `0`-`9`, יש להשתמש ב-`isdigit`.
*   לבדיקת האם תו הינו תו של מספרים עשרוניים, השתמשו במתודה `isdecimal`.

לפיכך, התשובה הנכונה היא **ב. השתמשו במתודה `isnumeric()`.**