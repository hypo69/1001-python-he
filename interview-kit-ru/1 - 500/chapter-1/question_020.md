### `question_020.md`

**שאלה 20.** מה תהיה תוצאת ההרצה של לולאת Python והאופרטורים התנאיים הבאים?

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

- א. `['2 is even', '4 is divisible by 4', '6 is even', '8 is divisible by 4', '10 is even']`
- ב. `['1 is odd', '2 is even', '3 is odd', '4 is divisible by 4', '5 is odd', '6 is even', '7 is odd', '8 is divisible by 4', '9 is odd', '10 is even']`
- ג. `['2 is even', '4 is even', '6 is even', '8 is even', '10 is even']`
- ד. `['2 is divisible by 4', '4 is divisible by 4', '6 is divisible by 4', '8 is divisible by 4', '10 is divisible by 4']`

**תשובה נכונה: א**

**הסבר:**

הקוד מבצע איטרציה על רשימת מספרים ומוסיף מחרוזות לרשימה `output` בהתאם לבדיקות התנאיות.

1.  **אתחול:** `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` יוצר רשימת מספרים, ו-`output = []` יוצר רשימה ריקה לאחסון מחרוזות.
2.  **לולאת `for`:** `for number in numbers:` עוברת על כל מספר ברשימה `numbers`.
3.  **אופרטורים תנאיים מקוננים:**
    *   `if number % 2 == 0:`: בודק אם המספר זוגי (מתחלק ב-2 ללא שארית).
    *   אם המספר זוגי: `if number % 4 == 0:`: בודק אם המספר מתחלק ב-4.
        *   אם המספר מתחלק ב-4, מתווספת ל-`output` מחרוזת מהצורה `"{number} is divisible by 4"`.
        *   אם המספר זוגי אך אינו מתחלק ב-4, מתווספת ל-`output` מחרוזת מהצורה `"{number} is even"`.
4.  **פלט:** `print(output)` מדפיס את רשימת המחרוזות.

עכשיו נתחקה אחר פעולת הקוד עבור כל מספר:

*   1: אי-זוגי, הבדיקות הפנימיות מדולגות.
*   2: זוגי, אינו מתחלק ב-4, מתווסף `"2 is even"`.
*   3: אי-זוגי, הבדיקות הפנימיות מדולגות.
*   4: זוגי, מתחלק ב-4, מתווסף `"4 is divisible by 4"`.
*   5: אי-זוגי, הבדיקות הפנימיות מדולגות.
*   6: זוגי, אינו מתחלק ב-4, מתווסף `"6 is even"`.
*   7: אי-זוגי, הבדיקות הפנימיות מדולגות.
*   8: זוגי, מתחלק ב-4, מתווסף `"8 is divisible by 4"`.
*   9: אי-זוגי, הבדיקות הפנימיות מדולגות.
*   10: זוגי, אינו מתחלק ב-4, מתווסף `"10 is even"`.

לפיכך, רשימת `output` תכיל את המחרוזות המבוססות על תנאים אלו.

*   **אפשרות א'** היא התשובה הנכונה, המשקפת במדויק את פעולת הקוד.
*   **אפשרות ב'** שגויה: אפשרות זו מוסיפה הודעות עבור כל המספרים, ולא רק הזוגיים.
*   **אפשרות ג'** שגויה: אפשרות זו מוסיפה רק `"is even"` עבור כל הזוגיים, ואינה בודקת חלוקה ב-4.
*   **אפשרות ד'** שגויה: אפשרות זו מוסיפה `"is divisible by 4"` עבור כל הזוגיים, וזה שגוי.

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

**תוצאה:**

הקוד ידפיס רשימת מחרוזות, כמו באפשרות א': `['2 is even', '4 is divisible by 4', '6 is even', '8 is divisible by 4', '10 is even']`.

לפיכך, **אפשרות א'** היא הנכונה.