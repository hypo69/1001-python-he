### `question_172.md`

**שאלה 172.** איזו מהאפשרויות הבאות מתארת נכונה את השימוש בבלוקים `try`, `except` ו-`finally` בפייתון?

א. בלוק `try` מכיל קוד שבו עלולה להתרחש שגיאה, בלוק `except` מבוצע אם שגיאה לא התרחשה, ובלוק `finally` מבוצע תמיד.
ב. בלוק `try` מכיל קוד שחייב להתבצע רק במקרה של שגיאה, ובלוקים `except` ו-`finally` – כשאף שגיאה לא התרחשה.
ג. בלוק `try` מכיל קוד שבו עלולה להתרחש שגיאה, בלוק `except` מבוצע אם שגיאה התרחשה, ובלוק `finally` מבוצע תמיד.
ד. בלוק `try` מיועד לביצוע קוד מספר פעמים, ובלוקים `except` ו-`finally` משמשים לטיפול בתוצאות הסופיות.

**התשובה הנכונה: C**

**הסבר:**

המבנה `try-except-finally` נועד לטיפול בחריגות (שגיאות) בפייתון ומאפשר שליטה אמינה יותר על ביצוע הקוד.

*   **אפשרות א אינה נכונה:** בלוק `except` מבוצע בעת התרחשות שגיאה, ולא בהיעדרה.
*   **אפשרות ב אינה נכונה:** בלוק `try` מיועד לקוד שעלול *לגרום* לשגיאה, ולא רק לקוד שיש לבצע כשאין שגיאה.
*   **אפשרות ג נכונה:** אפשרות זו מתארת נכונה את התפקידים של כל בלוק.
*   **אפשרות ד אינה נכונה:** `try-except-finally` אינם מיועדים לביצוע קוד מספר פעמים.

**כיצד פועלים הבלוקים `try-except-finally`:**

1.  **בלוק `try`:** מכיל קוד שבו עלולה להתרחש חריגה.
2.  **בלוק `except`:** מבוצע במקרה של התרחשות חריגה בבלוק `try`. יכול לטפל בחריגות מסוגים ספציפיים או בכל החריגות.
3.  **בלוק `finally`:** מבוצע תמיד, ללא קשר לשאלה האם הייתה חריגה והאם היא נתפסה בבלוק `except`. משמש בדרך כלל לפעולות שחייבות להתבצע בכל מקרה (לדוגמה, שחרור משאבים).

**דוגמה:**

```python
try:
    result: float = 10 / 0
except ZeroDivisionError:
    print("שגיאה: חלוקה באפס!")
finally:
    print("בלוק finally מבוצע תמיד!")

# פלט:
# שגיאה: חלוקה באפס!
# בלוק finally מבוצע תמיד!


try:
    result: int = 10 + 10
except ZeroDivisionError:
    print("שגיאה: חלוקה באפס!") # לא יבוצע
finally:
    print("בלוק finally מבוצע תמיד!") # פלט: בלוק finally מבוצע תמיד!
```

**לסיכום:**
*   `try` מבצע קוד שעלול לגרום לחריגה.
*   אם תתרחש שגיאה בבלוק `try`, יבוצע הבלוק `except`, אחרת הוא יידלג.
*   בלוק `finally` יבוצע בכל מקרה, ללא קשר לשאלה אם הייתה חריגה או לא.

לפיכך, **אפשרות ג** היא התשובה הנכונה.