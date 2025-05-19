### `question_020.md`

**שאלה 20.** מה תהא תוצאת ביצוע הלולאה הבאה בפייתון ופסוקיות התנאי?

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = []
for number in numbers:
    if number % 2 == 0:
        if number % 4 == 0:
            output.append(f"{number} is divisible by 4")
        else:
            output.append(f"{number} is even")
print(output)
```

- A. `['2 is even', '4 is divisible by 4', '6 is even', '8 is divisible by 4', '10 is even']`
- B. `['1 is odd', '2 is even', '3 is odd', '4 is divisible by 4', '5 is odd', '6 is even', '7 is odd', '8 is divisible by 4', '9 is odd', '10 is even']`
- C. `['2 is even', '4 is even', '6 is even', '8 is even', '10 is even']`
- D. `['2 is divisible by 4', '4 is divisible by 4', '6 is divisible by 4', '8 is divisible by 4', '10 is divisible by 4']`

**תשובה נכונה: A**

**הסבר:**

הקוד מבצע איטרציה על רשימת מספרים ומוסיף מחרוזות לרשימה `output` בהתאם לבדיקות התנאי.

1.  **אתחול:** `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` יוצר רשימת מספרים, ו-`output = []` יוצר רשימה ריקה לאחסון מחרוזות.
2.  **לולאת `for`:** `for number in numbers:` עוברת על כל מספר ברשימה `numbers`.
3.  **פסוקיות תנאי מקוננות:**
    *   `if number % 2 == 0:`: בודקת האם המספר זוגי (מתחלק ב-2 ללא שארית).
    *   אם המספר זוגי: `if number % 4 == 0:`: בודקת האם המספר מתחלק ב-4.
        *   אם המספר מתחלק ב-4, לרשימה `output` מתווספת מחרוזת מהצורה `"{number} is divisible by 4"`.
        *   אם המספר זוגי, אך אינו מתחלק ב-4, לרשימה `output` מתווספת מחרוזת מהצורה `"{number} is even"`.
4.  **פלט:** `print(output)` מדפיסה את רשימת המחרוזות.

כעת נתחקה אחר אופן פעולת הקוד עבור כל מספר:

*   1: אי-זוגי, הבדיקות הפנימיות מדלגות.
*   2: זוגי, אינו מתחלק ב-4, מתווספת המחרוזת `"2 is even"`.
*   3: אי-זוגי, הבדיקות הפנימיות מדלגות.
*   4: זוגי, מתחלק ב-4, מתווספת המחרוזת `"4 is divisible by 4"`.
*   5: אי-זוגי, הבדיקות הפנימיות מדלגות.
*   6: זוגי, אינו מתחלק ב-4, מתווספת המחרוזת `"6 is even"`.
*   7: אי-זוגי, הבדיקות הפנימיות מדלגות.
*   8: זוגי, מתחלק ב-4, מתווספת המחרוזת `"8 is divisible by 4"`.
*   9: אי-זוגי, הבדיקות הפנימיות מדלגות.
*   10: זוגי, אינו מתחלק ב-4, מתווספת המחרוזת `"10 is even"`.

לפיכך, הרשימה `output` תכיל את המחרוזות המבוססות על תנאים אלו.

*   **אפשרות A**: `['2 is even', '4 is divisible by 4', '6 is even', '8 is divisible by 4', '10 is even']` - מהווה את התשובה הנכונה, המשקפת במדויק את פעולת הקוד.
*   **אפשרות B** אינה נכונה: אפשרות זו מוסיפה הודעות עבור כל המספרים, ולא רק עבור הזוגיים.
*   **אפשרות C** אינה נכונה: אפשרות זו מוסיפה רק `"is even"` עבור כל הזוגיים, ואינה בודקת חלוקה ב-4.
*   **אפשרות D** אינה נכונה: אפשרות זו מוסיפה `"is divisible by 4"` עבור כל הזוגיים, ואין זה נכון.

**דוגמה:**

```python
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output: list[str] = []
for number in numbers:
    if number % 2 == 0:
        if number % 4 == 0:
            output.append(f"{number} is divisible by 4")
        else:
            output.append(f"{number} is even")
print(output) # פלט: ['2 is even', '4 is divisible by 4', '6 is even', '8 is divisible by 4', '10 is even']
```

**כתוצאה מכך:**

הקוד ידפיס רשימת מחרוזות, כמו באפשרות A: `['2 is even', '4 is divisible by 4', '6 is even', '8 is divisible by 4', '10 is even']`.

לפיכך, **אפשרות A** הינה הנכונה.