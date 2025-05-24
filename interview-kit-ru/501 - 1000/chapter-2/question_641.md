### `question_641.md`

**שאלה 641.** כיצד ניתן לבדוק בפייתון האם מחרוזת מורכבת אך ורק מתווים אלפביתיים (אותיות)?

-   א. יש להשתמש במתודה `isnumeric()`.
-   ב. יש להשתמש במתודה `isletter()`.
-   ג. יש להשתמש במתודה `isalpha()`.
-   ד. יש להשתמש בפונקציה `is_alpha()`.

**תשובה נכונה: ג**

**הסבר:**

בפייתון, כדי לבדוק האם מחרוזת מורכבת אך ורק מתווים אלפביתיים (אותיות), יש להשתמש במתודה המובנית `isalpha()`.

*   **המתודה `isalpha()`:**
    *   **בדיקת אותיות:** מחזירה `True` אם כל התווים במחרוזת הם אותיות (אלפביתיות), ו-`False` אחרת.
    *   **אלפביתים שונים:** המתודה מתחשבת באותיות מאלפביתים שונים, כלומר לא רק אלפבית לטיני, אלא גם, למשל, קירילי או יווני.
    *   **אינה מתחשבת ברווחים ובסימני פיסוק:** רווחים, ספרות ותווים מיוחדים אחרים יגרמו למתודה להחזיר `False`.
    *   **מחרוזת:** מיושמת על אובייקטי מחרוזת.

**דוגמאות:**

```python
# Example 1: String with only letters
string1 = 'hello'
print(f"'{string1}'.isalpha(): {string1.isalpha()}")  # Will output: 'hello'.isalpha(): True

# Example 2: String with digits
string2 = 'hello123'
print(f"'{string2}'.isalpha(): {string2.isalpha()}") # Will output: 'hello123'.isalpha(): False

# Example 3: String with spaces
string3 = 'hello world'
print(f"'{string3}'.isalpha(): {string3.isalpha()}") # Will output: 'hello world'.isalpha(): False

# Example 4: String with characters from other alphabets
string4 = "Привіт"
print(f"'{string4}'.isalpha(): {string4.isalpha()}") # Will output: 'Привіт'.isalpha(): True

# Example 5: Empty string
string5 = ""
print(f"'{string5}'.isalpha(): {string5.isalpha()}") # Will output: ''.isalpha(): False
```
**ניתוח האפשרויות:**
*   **א. יש להשתמש במתודה `isnumeric()`.:** שגוי. המתודה בודקת האם המחרוזת מורכבת מתווים מספריים, ולא מאותיות.
*   **ב. יש להשתמש במתודה `isletter()`.:** שגוי, אין מתודה בשם `isletter()` בפייתון.
*   **ג. יש להשתמש במתודה `isalpha()`.:** נכון.
*   **ד. יש להשתמש בפונקציה `is_alpha()`.:** שגוי.

**לסיכום:**
*   המתודה `isalpha()` מאפשרת לקבוע האם מחרוזת מורכבת אך ורק מתווים אלפביתיים.
*   רווחים, סימני פיסוק וספרות אינם עוברים את הבדיקה.

לפיכך, התשובה הנכונה היא **ג. יש להשתמש במתודה `isalpha()`.**