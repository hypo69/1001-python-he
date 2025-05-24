### `question_772.md`

**שאלה 772.** איזו פונקציה בפייתון משמשת ליצירת מספרים אקראיים, ואילו וריאציות שימוש עיקריות שלה אתה מכיר?

- א. בפייתון, ליצירת מספרים אקראיים משתמשים רק בפונקציה `random()`.
- ב. בפייתון, ליצירת מספרים אקראיים משתמשים בפונקציה `random.random()`, שמחזירה מספר בין 0.0 ל-1.0, וכן ישנן הפונקציות `randint()` ו-`randrange()`.
- ג. בפייתון, הפונקציה `random()` מיועדת ליצירת מחרוזות אקראיות, לא מספרים.
- ד. בפייתון קיימת רק פונקציה אחת `random(a,b)` ליצירת מספרים אקראיים.

**תשובה נכונה: ב**

**הסבר:**

בפייתון, ליצירת מספרים אקראיים משתמשים במודול `random`, המספק מספר פונקציות למטרות שונות. העיקריות שבהן הן `random()`, `randint()`, ו-`randrange()`.

*   **המודול `random`:**
    *   משמש ליצירת מספרים פסאודו-אקראיים.
*   **הפונקציות העיקריות של `random`:**
    *   **`random.random()`:**
        *   מחזירה מספר אקראי מסוג נקודה צפה (float) בטווח שבין 0.0 (כולל) ל-1.0 (לא כולל 1.0).
    *   **`random.randint(a, b)`:**
        *   מחזירה מספר שלם אקראי (int) בטווח שבין `a` (כולל) ל-`b` (כולל).
        *   שני הפרמטרים חייבים להיות מספרים שלמים.
    *   **`random.randrange(start, stop, step)`:**
        *   מחזירה מספר שלם אקראי (int) מתוך סדרה המוגדרת על ידי הארגומנטים `start`, `stop` ו-`step`.
        *   `start` - תחילת הסדרה (ברירת מחדל 0).
        *   `stop` - סוף הסדרה (לא כולל `stop`).
        *   `step` - גודל הצעד בסדרה (ברירת מחדל 1).
        *   הפרמטרים `start` ו-`step` אינם חובה.

**דוגמאות:**

```python
import random

# Example 1: random() - generate a random number in the range [0,1)
print(f"random.random(): {random.random()}")  # Will print a random number from 0.0 to 1.0

print(f"random.random(): {random.random()}") # Will print another random number from 0.0 to 1.0

# Example 2: randint(a, b) - integer from the range [a,b]
print(f"random.randint(1, 7): {random.randint(1, 7)}")   # Will print a random integer from 1 to 7 (inclusive)
print(f"random.randint(1, 7): {random.randint(1, 7)}")    # Will print a random integer from 1 to 7 (inclusive)


# Example 3: randrange(stop)  - integer from the range [0, stop)
print(f"random.randrange(4): {random.randrange(4)}")     # Will print a random integer from 0 to 4 (not including 4)
print(f"random.randrange(4): {random.randrange(4)}")     # Will print a random integer from 0 to 4 (not including 4)
# Example 4: randrange(start, stop)
print(f"random.randrange(4, 10): {random.randrange(4, 10)}") # Will print a random integer from 4 to 10 (not including 10)
print(f"random.randrange(4, 10): {random.randrange(4, 10)}") # Will print a random integer from 4 to 10 (not including 10)

# Example 5: randrange(start, stop, step)
print(f"random.randrange(4, 10, 2): {random.randrange(4, 10, 2)}")   # Will print a number from [4,6,8]
print(f"random.randrange(4, 10, 2): {random.randrange(4, 10, 2)}")  # Will print a number from [4,6,8]
```

**ניתוח האפשרויות:**
*   **א. בפייתון, ליצירת מספרים אקראיים משתמשים רק בפונקציה `random()`. :** שגוי.
*   **ב. בפייתון, ליצירת מספרים אקראיים משתמשים בפונקציה `random.random()`, שמחזירה מספר בין 0.0 ל-1.0, וכן ישנן הפונקציות `randint()` ו-`randrange()`. :** נכון.
*   **ג. בפייתון, הפונקציה `random()` מיועדת ליצירת מחרוזות אקראיות, לא מספרים. :** שגוי.
*   **ד. בפייתון קיימת רק פונקציה אחת `random(a,b)` ליצירת מספרים אקראיים. :** שגוי.

**לסיכום:**
*   המודול `random` מספק מגוון רחב של פונקציות ליצירת מספרים פסאודו-אקראיים.
*   `random()` מחזירה float, בעוד ש-`randint()` ו-`randrange()` מחזירות int.
*   `randrange` מאפשרת ליצור מספרים אקראיים עם צעד.
*   בחירת הפונקציה תלויה במשימה.

לפיכך, התשובה הנכונה היא **ב. בפייתון, ליצירת מספרים אקראיים משתמשים בפונקציה `random.random()`, שמחזירה מספר בין 0.0 ל-1.0, וכן ישנן הפונקציות `randint()` ו-`randrange()`.**