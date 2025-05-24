### `question_840.md`

**שאלה 840.** באילו מצבים בפייתון עולה החריגה (`exception`) מסוג `NotImplementedError`?

א. כאשר נעשה ניסיון לחבר שני טיפוסי נתונים לא תואמים, כגון מחרוזת ומספר.
ב. כאשר נעשה ניסיון לקרוא למתודה או לפונקציה שלא מומשה במחלקת בת, למרות שהוצהרה במחלקת אב.
ג. כאשר מתבצעת חלוקה באפס.
ד. כאשר נעשה ניסיון לגשת לאינדקס לא קיים ברשימה או בטאפל.

**התשובה הנכונה: ב'**

**הסבר:**

החריגה `NotImplementedError` בפייתון מאותתת על כך שמתודה או פעולה מסוימת *לא מומשה*, למרות שצפוי שהיא תמומש במחלקת בת.

*   **אפשרות א' אינה נכונה:** חיבור טיפוסי נתונים לא תואמים לרוב גורם לחריגה `TypeError`.
*   **אפשרות ב' נכונה:** בדיוק במקרה זה נועדה להיזרק החריגה `NotImplementedError`.
*   **אפשרות ג' אינה נכונה:** חלוקה באפס גורמת לחריגה `ZeroDivisionError`.
*   **אפשרות ד' אינה נכונה:** גישה לאינדקס לא קיים גורמת לחריגה `IndexError`.

**מתי נעשה שימוש ב־`NotImplementedError`:**

1.  **מתודות מופשטות במחלקות אב:**
    *   במחלקת אב מוצהרת מתודה, אך לא מסופקת לה מימוש.
    *   מחלקות בת חייבות לדרוס מתודה זו ולספק לה מימוש משלהן.
    *   אם מחלקת בת לא תדרוס מתודה זו, אזי בעת קריאה אליה תיווצר החריגה `NotImplementedError`.

2.  **ציון פונקציונליות שאינה גמורה:**
    *  באופן זמני, כדי להראות שהפונקציונליות טרם מומשה.

**דוגמה:**

```python
class BaseClass:
    def my_method(self):
        raise NotImplementedError("This method must be implemented in subclass")

class SubClass(BaseClass):
    def my_method(self):
        return "Implementation in SubClass"

obj = SubClass()
print(obj.my_method())

obj2 = BaseClass()
try:
  obj2.my_method()
except NotImplementedError as e:
  print(e) # פלט: This method must be implemented in subclass
```

**לסיכום:**

החריגה `NotImplementedError` מתרחשת כאשר מתודה או פונקציה אמורות להיות ממומשות במחלקת בת, אך הדבר לא נעשה.

לפיכך, אפשרות ב' היא הנכונה.