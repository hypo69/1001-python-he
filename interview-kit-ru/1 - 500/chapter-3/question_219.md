### `question_219.md`

**שאלה 219.** מה עושה המתודה `__init__` במחלקת Python?

א. יוצר מופע חדש של אובייקט המחלקה.
ב. מחזיר ייצוג מחרוזתי של האובייקט.
ג. מאתחל את האובייקט בעת יצירתו.
ד. מוחק את האובייקט מהזיכרון.

**תשובה נכונה: ג**

**הסבר:**

המתודה `__init__` היא מתודה מיוחדת (קונסטרוקטור) ב-Python, הנקראת אוטומטית בעת יצירת מופע (אובייקט) חדש של המחלקה. המטרה העיקרית של מתודה זו היא לאתחל את מאפייני האובייקט עם ערכי התחלה.

*   **אפשרות א** שגויה: המתודה האחראית על יצירת אובייקט חדש היא `__new__`, ואילו `__init__` רק מאתחלת אותו.
*   **אפשרות ב** שגויה: ייצוג מחרוזתי של האובייקט נוצר על ידי המתודות `__str__()` או `__repr__()`.
*   **אפשרות ג** נכונה: המתודה `__init__` משמשת לאתחול האובייקט.
*   **אפשרות ד** שגויה: למחיקת אובייקט מהזיכרון משמשת המתודה `__del__()`.

**כיצד פועלת `__init__`:**

1.  המתודה `__init__` נקראת אוטומטית על ידי מפרש ה-Python בעת יצירת מופע חדש של המחלקה.
2.  הפרמטר הראשון של `__init__` הוא תמיד `self`, המתייחס לאובייקט הנבנה.
3.  בתוך המתודה `__init__` מוגדרים לרוב ערכי התחלה עבור מאפייני האובייקט.
4.  המתודה יכולה לקבל פרמטרים נוספים, שיועברו בעת יצירת מופע האובייקט.

**דוגמה:**

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name  # אתחול המאפיין name
        self.age = age  # אתחול המאפיין age
        print("Объект создан!")

person1: Person = Person("Alice", 30) #  פלט: האובייקט נוצר!
print(f"Имя: {person1.name}, Возраст: {person1.age}")  # פלט: שם: Alice, גיל: 30
```

**תוצאה:**
*   בעת יצירת האובייקט `person1` נקראת המתודה `__init__` על מנת להגדיר את מאפייני השם והגיל.

לפיכך, **אפשרות ג** היא התשובה הנכונה.