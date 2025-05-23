### `question_78.md`

**שאלה 78.** מהי המטרה העיקרית של הפונקציה `zip()` ב-Python?

- א. לדחיסת קבצים.
- ב. לאיטרציה סימולטנית על שתי רצפים או יותר.
- ג. לחילוץ קבצים.
- ד. לקידוד נתונים.

**תשובה נכונה: ב**

**הסבר:**

הפונקציה `zip()` ב-Python מיועדת לשלב מספר אובייקטים איטרביליים (למשל, רשימות, טאפלים או מחרוזות) ולאפשר איטרציה סימולטנית עליהם.

*   **אפשרות א'** אינה נכונה: הפונקציה `zip()` אינה עוסקת בדחיסת קבצים.
*   **אפשרות ב'** נכונה: `zip()` מאפשרת לבצע איטרציה על מספר רצפים בו-זמנית.
*   **אפשרות ג'** אינה נכונה: `zip()` אינה מיועדת לחילוץ קבצים.
*   **אפשרות ד'** אינה נכונה: `zip()` אינה עוסקת בקידוד נתונים.

**כיצד `zip()` עובדת:**

1.  הפונקציה `zip()` מקבלת כאגרגומנטים שני אובייקטים איטרביליים או יותר.
2.  היא מחזירה איטרטור שמייצר טאפלים.
3.  כל טאפל מכיל אלמנטים מהעמדות המקבילות באובייקטים האיטרביליים הקלט.
4.  האיטרציה נמשכת עד שאחד מאובייקטי הקלט האיטרביליים מסתיים.

**מקרים נפוצים לשימוש ב-`zip()`:**

1.  **איטרציה מקבילה:** כאשר יש צורך לעבור על מספר רצפים בו-זמנית, עם גישה לאלמנטים בעלי אותו אינדקס.
2.  **יצירת מילונים:** ליצירת מילון משתי רשימות, כאשר האחת משמשת כמפתחות והשנייה כערכים.
3.  **טרנספוזיציה של מטריצות:** `zip()` משמשת לביצוע טרנספוזיציה של מטריצות (החלפת שורות בעמודות ולהיפך).
4.  **שילוב נתונים:** חיבור נתונים מרשימות שונות לזוגות או טאפלים לצורך עיבוד נוסף.

**דוגמה:**

```python
names: list[str] = ["Alice", "Bob", "Charlie"]
ages: list[int] = [25, 30, 35]
cities: list[str] = ["New York", "London"] # הרשימה קצרה יותר, לכן zip תפסיק את האיטרציה כשתגיע ל-London

# מבצעים איטרציה סימולטנית על מספר רשימות
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# פלט:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# ניצור מילון מהרשימות
name_age_dict: dict[str, int] = dict(zip(names, ages))
print(f"Словарь: {name_age_dict}")  # פלט: Словарь: {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

**בתוצאה:**

*   בעת איטרציה באמצעות `zip()`, זוגות של אלמנטים מ-`names` ומ-`ages` מונפקים בכל איטרציה.
*   `zip(names, ages)` יחזיר זוגות רק עד שיסתיים האובייקט האיטרבילי הקצר ביותר.
*   במילון, כל מפתח יהיה מרשימת `names`, והערך יהיה מרשימת `ages`.

לפיכך, **אפשרות ב'** היא התשובה הנכונה.