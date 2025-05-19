### question_015.md

**שאלה 15.** בעת ביצוע איטרציה על רשימה בפייתון כדי לחשב את סכום איבריה, איזו מבניית הלולאה הבאות מנוסחת כהלכה כדי למנוע שגיאת `IndexError` ולחשב בהצלחה את הסכום הכולל?

```python
- A. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) + 1): total += list_values[i]; print(total)
- B. list_values = [1, 2, 3, 4, 5]; total = 0; for value in list_values: total += value; print(total)
- C. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(1, len(list_values)): total += list_values[i]; print(total)
- D. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) - 1): total += list_values[i]; print(total)
```

**התשובה הנכונה: B**

**הסבר:**

לביצוע איטרציה על איברי רשימה בפייתון קיימות מספר שיטות. חשוב לבחור את השיטה הנכונה כדי להימנע משגיאות, כגון `IndexError`, המתרחשת בעת ניסיון לגשת לאינדקס שאינו קיים.

*   **אפשרות A**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) + 1): total += list_values[i]; print(total)` - אפשרות שגויה. לולאת ה-`for` באפשרות זו מנסה לעבור על האינדקסים מ-0 ועד `len(list_values)`, כולל, מה שיגרום ל-`IndexError` באיטרציה האחרונה, מכיוון שאינדקסי הרשימה מתחילים מ-0 ומסתיימים ב-`len(list_values) - 1`.

*   **אפשרות B**: `list_values = [1, 2, 3, 4, 5]; total = 0; for value in list_values: total += value; print(total)` - זוהי האפשרות הנכונה. לולאת ה-`for` באפשרות זו מבצעת איטרציה ישירות על איברי הרשימה, ולא על האינדקסים שלהם. זוהי דרך פשוטה, יעילה ופיית'ונית לבצע איטרציה על רשימות בפייתון, שבה עוברים אוטומטית על כל איברי הרשימה ללא צורך להשתמש באינדקסים.
    
*   **אפשרות C**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(1, len(list_values)): total += list_values[i]; print(total)` - אפשרות שגויה. לולאה זו תדלג על האיבר הראשון של הרשימה (בעל אינדקס 0), מכיוון שהיא מבצעת איטרציה על טווח מ-1 ועד `len(list_values) - 1`.

*   **אפשרות D**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) - 1): total += list_values[i]; print(total)` - אפשרות שגויה. לולאה זו תדלג על האיבר האחרון של הרשימה (בעל אינדקס `len(list_values) - 1`), מכיוון שהיא מבצעת איטרציה עד `len(list_values) - 2`.

**דוגמה:**

```python
# דוגמה עם האפשרות הנכונה (B)
list_values: list[int] = [1, 2, 3, 4, 5]
total: int = 0
for value in list_values:
    total += value
print(f"סכום האיברים: {total}")  # פלט: סכום האיברים: 15

# דוגמה עם האפשרות השגויה (A) - תגרום ל-IndexError
list_values: list[int] = [1, 2, 3, 4, 5]
total: int = 0
try:
    for i in range(len(list_values) + 1):
        total += list_values[i]
    print(total)
except IndexError as e:
     print(e) # פלט: list index out of range
```

**לסיכום:**

*   **אפשרות B** מבצעת איטרציה מוצלחת על כל איברי הרשימה, מסכמת אותם ומדפיסה את התוצאה `15`.
*   **אפשרות A** תגרום לשגיאת `IndexError` בעת ניסיון לגשת לאינדקס 5, שאינו קיים ברשימה.

לפיכך, רק **אפשרות B** מחשבת בצורה נכונה ויעילה את סכום איברי הרשימה.