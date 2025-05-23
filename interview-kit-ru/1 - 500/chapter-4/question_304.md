### `question_304.md`

**שאלה 304.** אם יש לך פונקציית Python עם ארגומנט `*args` ואתה קורא לה כפי שמוצג: `my_function(1, 2, 3)`, איזה סוג אובייקט יהיה `args` בתוך הפונקציה?

A. קורטז' (`tuple`)
B. רשימה (`list`)
C. מילון (`dictionary`)
D. מספר שלם (`integer`)

**תשובה נכונה: A**

**הסבר:**

כאשר משתמשים ב-`*args` בהגדרה של פונקציית Python, כל ה*ארגומנטים המיקומיים* שעוברים בעת קריאת הפונקציה נאספים לתוך *קורטז'* (tuple). בתוך הפונקציה, המשתנה `args` יצביע על קורטז' זה.

*   **אפשרות A נכונה:** `*args` אוסף את הארגומנטים לתוך קורטז'.
*   **אפשרות B אינה נכונה:** `*args` אוסף את הארגומנטים לתוך קורטז', לא לתוך רשימה.
*   **אפשרות C אינה נכונה:** מילונים נאספים באמצעות `**kwargs`.
*   **אפשרות D אינה נכונה:** ארגומנטים בודדים אינם נאספים לתוך מספר שלם.

**כיצד פועל `*args`:**

1.  בהגדרת הפונקציה `def my_function(*args):`, הסימון `*args` מציין שהפונקציה יכולה לקבל מספר שרירותי של ארגומנטים מיקומיים.
2.  כאשר הפונקציה נקראת, למשל, `my_function(1, 2, 3)`, כל הארגומנטים המיקומיים שעברו (1, 2, 3) נארזים לתוך קורטז'.
3.  בתוך הפונקציה, המשתנה `args` יצביע על קורטז' זה.

**דוגמה:**

```python
def my_function(*args):
    print(f"Type of args: {type(args)}")
    print(f"args: {args}")

my_function(1, 2, 3)
# Output:
# Type of args: <class 'tuple'>
# args: (1, 2, 3)
```
**לסיכום:**

אם פונקציית Python מוגדרת עם ארגומנט `*args`, אזי בתוך הפונקציה `args` יהווה קורטז' המכיל את כל הארגומנטים המיקומיים שעברו.

לכן, אפשרות A היא התשובה הנכונה.

---

מוכן לשאלה הבאה!