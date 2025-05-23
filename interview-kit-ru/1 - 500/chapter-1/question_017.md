### `question_017.md`

**שאלה 17.** מה יהיה התנהגות פונקציית Python הבאה?

```python
def check_number(n):
    if n % 2 == 0:
        return "Even"
    elif n % 3 == 0:
        return "Divisible by 3"
    else:
        return "Other"
```

- A. הפונקציה מחזירה `"Even"` רק אם `n` מתחלק ב-2 וב-3.
- B. הפונקציה מחזירה `"Divisible by 3"` עבור כל המספרים המתחלקים ב-3, ללא קשר אם הם זוגיים.
- C. הפונקציה מחזירה `"Even"` עבור כל המספרים הזוגיים, ו-"Divisible by 3"` עבור מספרים שאינם זוגיים אך מתחלקים ב-3.
- D. הפונקציה אינה יכולה להחזיר `"Other"`.

**תשובה נכונה: C**

**הסבר:**

הפונקציה `check_number(n)` בודקת את המספר `n` להתאמה לתנאים מסוימים ומחזירה מחרוזת בהתאם לתוצאת הבדיקה.

*   **`if n % 2 == 0:`**: בודקת האם המספר `n` הוא זוגי (כלומר, האם הוא מתחלק ב-2 ללא שארית). אם התנאי מתקיים, הפונקציה מחזירה מיד את המחרוזת `"Even"` ומפסיקה את פעולתה.

*   **`elif n % 3 == 0:`**: אם התנאי הקודם שקרי (כלומר, המספר `n` אינו זוגי), נבדק האם `n` מתחלק ב-3 ללא שארית. אם תנאי זה מתקיים, הפונקציה מחזירה את המחרוזת `"Divisible by 3"` ומפסיקה את פעולתה.

*   **`else:`**: אם אף אחד מהתנאים הקודמים לא התקיים (כלומר, המספר `n` אינו זוגי ואינו כפולה של 3), הפונקציה מחזירה את המחרוזת `"Other"`.

הבה ננתח את אפשרויות התשובה:

*   **אפשרות A** אינה נכונה: הפונקציה מחזירה `"Even"` אם המספר מתחלק ב-2 בלבד, ולא ב-2 וגם ב-3.
*   **אפשרות B** אינה נכונה: אם המספר זוגי (מתחלק ב-2), אזי הענף `if n % 2 == 0:` מבוצע ראשון והפונקציה מחזירה `"Even"`, מבלי לבדוק התחלקות ב-3.
*   **אפשרות C** נכונה: כך בדיוק פועלת הפונקציה, בודקת תחילה זוגיות ולאחר מכן התחלקות ב-3.
*   **אפשרות D** אינה נכונה: הפונקציה יכולה להחזיר `"Other"`, אם המספר אינו עומד באף אחד משני התנאים הראשונים.

**דוגמאות:**

```python
def check_number(n: int) -> str:
    if n % 2 == 0:
        return "Even"
    elif n % 3 == 0:
        return "Divisible by 3"
    else:
        return "Other"

print(check_number(4))   # פלט: Even
print(check_number(9))  # פלט: Divisible by 3
print(check_number(7))  # פלט: Other
print(check_number(6)) # פלט: Even (המספר מתחלק ב-2, הענף הראשון מבוצע)
```

**כתוצאה מכך:**

*   `check_number(4)` מחזירה `"Even"`, מכיוון ש-4 מתחלק ב-2.
*   `check_number(9)` מחזירה `"Divisible by 3"`, מכיוון ש-9 אינו זוגי אך מתחלק ב-3.
*   `check_number(7)` מחזירה `"Other"`, מכיוון ש-7 אינו מתחלק לא ב-2 ולא ב-3.
*   `check_number(6)` מחזירה `"Even"`, מכיוון ש-6 מתחלק ב-2, והתנאים הבאים אינם נבדקים.

לפיכך, **אפשרות C** היא היחידה הנכונה.