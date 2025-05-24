### question_514

**שאלה 514:**
```python
def apply_operation(x, y, operation):
    return operation(x,y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 2, add)
result2 = apply_operation(5, 2, multiply)
print(result1, result2)
```
מה תהיה תוצאת ביצוע קוד זה?

A. 7 10
B. 10 7
C. 7 25
D. תתרחש שגיאה.

**תשובה נכונה: A**

**הסבר:**
קוד זה מדגים את הרעיון של פונקציות מסדר גבוה (higher-order functions) והעברת פונקציות כאַרְגּוּמֶנְטִים בפייתון.

1.  **הפונקציה `apply_operation`:**
    *   מקבלת שלושה אַרְגּוּמֶנְטִים: `x`, `y` (מספרים) ו-`operation` (פונקציה).
    *   מחזירה את התוצאה של קריאה לפונקציה `operation` עם האַרְגּוּמֶנְטִים `x` ו-`y`.

2.  **הפונקציה `add`:**
    *   מקבלת שני אַרְגּוּמֶנְטִים: `a` ו-`b`.
    *   מחזירה את הסכום של `a` ו-`b`.

3.  **הפונקציה `multiply`:**
    *   מקבלת שני אַרְגּוּמֶנְטִים: `a` ו-`b`.
    *   מחזירה את המכפלה של `a` ו-`b`.

4.  **הקריאות ל-`apply_operation`:**
    *   `result1 = apply_operation(5, 2, add)`: הפונקציה `add` מועברת כאַרְגּוּמֶנְט `operation`. `apply_operation` תקרא ל-`add(5, 2)`, אשר תחזיר `5 + 2 = 7`.
    *   `result2 = apply_operation(5, 2, multiply)`: הפונקציה `multiply` מועברת כאַרְגּוּמֶנְט `operation`. `apply_operation` תקרא ל-`multiply(5, 2)`, אשר תחזיר `5 * 2 = 10`.

5. **הפלט** `print(result1, result2)` ידפיס את הערכים של המשתנים `result1` ו-`result2`, מופרדים ברווח.

**ניתוח האפשרויות:**

*   **A. 7 10:** נכון. `result1` שווה ל-7, ו-`result2` שווה ל-10.
*   **B. 10 7:** שגוי. סדר הפעולות הפוך.
*   **C. 7 25:** שגוי. תוצאה שגויה עבור `result2`.
*   **D. תתרחש שגיאה:** שגוי, הקוד יבוצע ללא שגיאות.

**קוד עבור הקובץ `question_514.md`:**
```markdown
### `question_514.md`

**שאלה 514.** מה תהיה תוצאת ביצוע קוד זה?

```python
def apply_operation(x, y, operation):
    return operation(x,y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 2, add)
result2 = apply_operation(5, 2, multiply)
print(result1, result2)
```

- A. 7 10
- B. 10 7
- C. 7 25
- D. תתרחש שגיאה.

**תשובה נכונה: A**

**הסבר:**

קוד זה מדגים את הרעיון של פונקציות מסדר גבוה (higher-order functions) והעברת פונקציות כאַרְגּוּמֶנְטִים בפייתון.

*   **הפונקציה `apply_operation`:** מקבלת שלושה אַרְגּוּמֶנְטִים: שני מספרים (`x`, `y`) ופונקציה (`operation`). היא מחזירה את התוצאה של קריאה לפונקציה המועברת `operation` עם האַרְגּוּמֶנְטִים `x` ו-`y`.
*   **הפונקציות `add` ו-`multiply`:** אלו הן פונקציות פשוטות, אשר מבצעות חיבור וכפל בהתאמה.
*   **הקריאות ל-`apply_operation`:**
    *   ל-`result1` מושמת התוצאה של הקריאה ל-`apply_operation` עם המספרים 5 ו-2 והפונקציה `add`. הפונקציה `add(5, 2)` תחזיר 7.
    *   ל-`result2` מושמת התוצאה של הקריאה ל-`apply_operation` עם המספרים 5 ו-2 והפונקציה `multiply`. הפונקציה `multiply(5, 2)` תחזיר 10.

כתוצאה מכך, `print(result1, result2)` ידפיס `7 10`.

**הערות נוספות:**

- בפייתון, פונקציות הן אובייקטים מהסדר הראשון (first-class objects), מה שאומר שניתן להעביר אותן כאַרְגּוּמֶנְטִים לפונקציות אחרות, להחזיר אותן מפונקציות, ולהקצות למשתנים.
- פונקציות המקבלות פונקציות אחרות כאַרְגּוּמֶנְטִים או מחזירות אותן, נקראות פונקציות מסדר גבוה.
- יכולת זו הופכת את פייתון לשפה גמישה וחזקה מאוד.
```