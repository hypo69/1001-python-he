### `question_132.md`

**שאלה 32.** האופרטור `break` משמש בתוך לולאה בפייתון לביצוע משימה מסוימת. מה יקרה אם האופרטור `break` יבוצע בתוך לולאה?

א. תתבצע רק האיטרציה הנוכחית של הלולאה, ולאחר מכן הלולאה תמשיך עם האיטרציה הבאה.
ב. ביצוע התוכנית יופסק, והתוכנית תסתיים בהודעת שגיאה.
ג. הלולאה תסתיים מיד, וביצוע התוכנית ימשיך מהשורה הבאה של הקוד לאחר הלולאה.
ד. הלולאה תופעל מחדש מהאיטרציה הראשונה, תוך דילוג על כל האיטרציות הנותרות.

**תשובה נכונה: C**

**הסבר:**

האופרטור `break` בפייתון משמש לשליטה על זרימת הביצוע בתוך לולאות (`for` ו-`while`).

*   **אפשרות א** אינה נכונה: האופרטור `break` אינו מבצע רק את האיטרציה הנוכחית.
*   **אפשרות ב** אינה נכונה: `break` אינו מסיים את התוכנית כולה.
*   **אפשרות ג** נכונה: האופרטור `break` מסיים מיד את הלולאה שבה הוא מופיע.
*   **אפשרות ד** אינה נכונה: האופרטור `break` אינו מפעיל מחדש את הלולאה.

**כיצד פועל האופרטור `break`:**

1.  כאשר מפרש פייתון נתקל באופרטור `break` בתוך לולאה, ביצוע הלולאה נפסק מיד.
2.  השליטה מועברת לשורה הראשונה של הקוד לאחר הלולאה.

**דוגמה:**

```python
for i in range(10):
    if i == 3:
        print("מפסיקים את הלולאה כאשר i שווה ל-3")
        break
    print(i)
print("הלולאה הסתיימה")
```

# פלט:
```
0
1
2
מפסיקים את הלולאה כאשר i שווה ל-3
הלולאה הסתיימה
```

**כתוצאה מכך:**

*   לולאת `for` הייתה אמורה לעבור 10 איטרציות (מ-0 עד 9).
*   אולם, כאשר `i` מגיע לערך 3, מבוצע האופרטור `break`.
*   הלולאה מסתיימת, והאיטרציות הנותרות (מ-3 עד 9) אינן מבוצעות.
*   התוכנית ממשיכה להתבצע משורת `print("הלולאה הסתיימה")`.

לפיכך, **אפשרות ג** היא התשובה הנכונה.