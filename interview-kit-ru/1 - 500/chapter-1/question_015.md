### `question_015.md`

**שאלה 15.** בעת ביצוע איטרציה על רשימה ב-Python לשם חישוב סכום איבריה, איזו מהמבנים הבאים של לולאה מנוסחת באופן נכון כדי למנוע שגיאת `IndexError` ולחשב בהצלחה את הסכום הכולל?

```python
- A. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) + 1): total += list_values[i]; print(total)
- B. list_values = [1, 2, 3, 4, 5]; total = 0; for value in list_values: total += value; print(total)
- C. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(1, len(list_values)): total += list_values[i]; print(total)
- D. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) - 1): total += list_values[i]; print(total)
```

**תשובה נכונה: B**

**הסבר:**

לשם ביצוע איטרציה על איברי רשימה ב-Python קיימות מספר דרכים. חשוב לבחור את הדרך הנכונה כדי להימנע משגיאות, כגון `IndexError`, אשר מתרחשת כאשר מנסים לגשת לאינדקס שאינו קיים.

*   **אפשרות A**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) + 1): total += list_values[i]; print(total)` - אפשרות שגויה. לולאת ה-`for` באפשרות זו מנסה לעבור על אינדקסים מ-0 ועד `len(list_values)`, כולל. הדבר יוביל לשגיאת `IndexError` באיטרציה האחרונה, מכיוון שאינדקסים של רשימה מתחילים מ-0 ומסתיימים ב-`len(list_values) - 1`.

*   **אפשרות B**: `list_values = [1, 2, 3, 4, 5]; total = 0; for value in list_values: total += value; print(total)` - זוהי האפשרות הנכונה. לולאת ה-`for` באפשרות זו מבצעת איטרציה ישירות על איברי הרשימה, ולא על האינדקסים שלהם. זוהי דרך פשוטה, יעילה ואידיומטית לבצע איטרציה על רשימות ב-Python, שבה עוברים אוטומטית על כל איברי הרשימה ללא צורך בשימוש באינדקסים.

*   **אפשרות C**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(1, len(list_values)): total += list_values[i]; print(total)` - אפשרות שגויה. לולאה זו תדלג על האיבר הראשון ברשימה (עם אינדקס 0), מכיוון שהיא מבצעת איטרציה על טווח מ-1 ועד `len(list_values) - 1`.

*   **אפשרות D**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) - 1): total += list_values[i]; print(total)` - אפשרות שגויה. לולאה זו תדלג על האיבר האחרון ברשימה (עם אינדקס `len(list_values) - 1`), מכיוון שהיא מבצעת איטרציה עד `len(list_values) - 2`.

**דוגמה:**

```python
# Example with the correct option (B)
list_values: list[int] = [1, 2, 3, 4, 5]
total: int = 0
for value in list_values:
    total += value
print(f"סכום האלמנטים: {total}")  # Output: סכום האלמנטים: 15

# Example with the incorrect option (A) - will raise IndexError
list_values: list[int] = [1, 2, 3, 4, 5]
total: int = 0
try:
    for i in range(len(list_values) + 1):
        total += list_values[i]
    print(total)
except IndexError as e:
     print(e) # Output: list index out of range
```

**תוצאה:**

*   **אפשרות B** מבצעת איטרציה בהצלחה על כל איברי הרשימה, מסכמת אותם ומציגה את התוצאה `15`.
*   **אפשרות A** תגרום לשגיאת `IndexError` בעת ניסיון גישה לאינדקס 5, שאינו קיים ברשימה.

לפיכך, רק **אפשרות B** מחשבת באופן תקין ויעיל את סכום איברי הרשימה.