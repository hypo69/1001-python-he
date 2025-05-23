### `question_305.md`

**שאלה 305.** כיצד מגדירים פונקציית Python שיכולה לקבל מספר שרירותי של ארגומנטים בעלי שם (מילות מפתח) ולהחזיר את סכום כל הערכים שהועברו כארגומנטים בעלי שם?

A. `def sum_args(**kwargs): return sum(kwargs)`
B. `def sum_args(*kwargs): return sum(kwargs)`
C. `def sum_args(*args): return sum(args)`
D. `def sum_args(**args): return sum(args)`

**תשובה נכונה: A**

**הסבר:**

ב-Python, על מנת להגדיר פונקציה שיכולה לקבל מספר שרירותי של ארגומנטים *בעלי שם* (מילות מפתח), משתמשים בתחביר `**kwargs` בהגדרת הפונקציה. כל הארגומנטים בעלי השם שהועברו בעת קריאה לפונקציה נאספים לתוך *מילון* (dictionary), הזמין בתוך הפונקציה באמצעות המשתנה `kwargs`.

*   **אפשרות A נכונה:** `**kwargs` אוסף ארגומנטים בעלי שם לתוך מילון, ו-`sum(kwargs.values())` יחזיר את סכומם.
*   **אפשרות B אינה נכונה:** `*kwargs` אינו תחביר נכון. `*args` אוסף ארגומנטים פוזיציונליים.
*   **אפשרות C אינה נכונה:** `*args` אוסף ארגומנטים פוזיציונליים, ולא ארגומנטים בעלי שם.
*   **אפשרות D אינה נכונה:** `**args` אינו תחביר נכון. `**kwargs` אוסף ארגומנטים בעלי שם לתוך מילון.

**כיצד פועל `**kwargs`:**

1.  בהגדרת פונקציה, `**kwargs` מציין שהפונקציה יכולה לקבל כל מספר של ארגומנטים *בעלי שם* (מילות מפתח).
2.  ארגומנטים אלו נאספים לתוך *מילון* (dictionary), כאשר המפתחות הם שמות הארגומנטים, והערכים הם ערכי הארגומנטים.
3.  בתוך הפונקציה ניתן לעבוד עם המילון `kwargs`, למשל, לעבור על מפתחותיו וערכיו.

**דוגמה:**

```python
def sum_args(**kwargs):
    print(f"Type of kwargs: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    return sum(kwargs.values())

result = sum_args(a=1, b=2, c=3) # Output: Type of kwargs: <class 'dict'>
print(f"Sum: {result}") #Output: Sum: 6
result = sum_args(x=10, y=20, z=30, w=40)
print(f"Sum: {result}") # Output: Sum: 100
```
**לסיכום:**

על מנת להגדיר פונקציה המקבלת מספר שרירותי של ארגומנטים בעלי שם ומחזירה את סכומם, יש להשתמש ב-`def sum_args(**kwargs): return sum(kwargs.values())`, כאשר `kwargs` יהיה מילון המכיל את כל הארגומנטים בעלי השם שהועברו.

לפיכך, אפשרות A היא הנכונה.

---

מוכן לשאלה הבאה!