### `question_187.md`

**שאלה 187.** מהו "מתודה" (method) בהקשר של תכנות מונחה-עצמים ב-Python?

A. משתנה המאחסן נתונים.
B. פונקציה הקשורה לאובייקט של מחלקה ויש לה גישה לנתונים שלו.
C. דרך ליצירת מחלקות חדשות.
D. דרך לשינוי טיפוס הנתונים של אובייקט.

**תשובה נכונה: B**

**הסבר:**

בתכנות מונחה-עצמים (OOP) ב-Python, מתודה היא פונקציה הקשורה לאובייקט של מחלקה ויש לה גישה לנתונים של אובייקט זה.

*   **אפשרות A** אינה נכונה: תכונות (attributes) (משתנים) מאחסנות נתונים, לא מתודות.
*   **אפשרות B** נכונה: מתודה היא פונקציה הקשורה לאובייקט ויש לה גישה לנתוניו דרך `self`.
*   **אפשרות C** אינה נכונה: מחלקות נוצרות באמצעות מילת המפתח `class`.
*   **אפשרות D** אינה נכונה: לשינוי טיפוס משתמשים בפונקציות המרת טיפוס (לדוגמה, `int()`, `str()`, `float()`).

**כיצד פועלות מתודות:**

1.  מתודה מוגדרת בתוך מחלקה.
2.  הארגומנט הראשון של מתודה הוא תמיד `self`, המייצג את מופע המחלקה שדרכו נקראת המתודה.
3.  מתודה יכולה לעבוד עם התכונות (נתונים) של האובייקט.
4.  מתודה יכולה לבצע כל פעולה עם נתוני האובייקט.

**דוגמה:**

```python
class Car:
    def __init__(self, model: str, color: str):
        self.model = model  # תכונת מופע
        self.color = color  # תכונת מופע

    def display_info(self):  # מתודת מופע
        print(f"Модель: {self.model}, Цвет: {self.color}") # הדפסה: דגם: טסלה, צבע: אדום

car1: Car = Car("Tesla", "red")
car1.display_info()  # הדפסה: דגם: טסלה, צבע: אדום
```

**כתוצאה מכך:**

*   המתודה `display_info()` קשורה לאובייקטים של המחלקה `Car` ויש לה גישה לתכונותיה `model` ו-`color`.
*   המתודה מדפיסה את הנתונים עבור אובייקט ספציפי.

לפיכך, **אפשרות B** היא התשובה הנכונה.