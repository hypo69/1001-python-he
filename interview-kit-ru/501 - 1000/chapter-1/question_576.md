### `question_70.md`

**פרק 1. שאלה 70.** מה קורה כאשר הפונקציה (method) `append()` נקראת על מילון ב-Python?

- A. היא מוסיפה זוג מפתח-ערך חדש למילון.
- B. היא גורמת לשגיאת `AttributeError`, מכיוון שמילונים אינם תומכים בפונקציה `append()`.
- C. היא משרשרת מילון אחר למילון הקיים.
- D. היא מעדכנת את הערך של מפתח קיים.

**התשובה הנכונה: B**

**הסבר:**

ב-Python, מילונים (`dict`) אינם תומכים בפונקציה `append()`, המיועדת לרשימות. ניסיון לקרוא לפונקציה `append()` על מילון יוביל לשגיאת `AttributeError`.

*   **אפשרות A** שגויה: מילונים משתמשים בפונקציות אחרות להוספת זוגות מפתח-ערך.
*   **אפשרות B** נכונה: קריאה ל-`append()` על מילון תוביל לשגיאת `AttributeError`.
*   **אפשרות C** שגויה: עבור שרשור (קונקטנציה) משתמשים בפונקציה `update()`.
*   **אפשרות D** שגויה: `append()` אינה מיועדת לעדכון ערכים קיימים.

**מדוע מילונים אינם משתמשים ב-`append()`:**

*   רשימות (lists) מיועדות לאחסון אוספים מסודרים של אלמנטים ויכולות להתרחב בסופן.
*   מילונים (dictionaries) מיועדים לאחסון זוגות "מפתח-ערך", כאשר המפתחות חייבים להיות ייחודיים.
*   הפונקציה `append()` מיועדת במהותה להוספת אלמנט חדש לסופו של אובייקט בר חזרה (iterable), ולא לשינוי קשרי מפתח-ערך.

**דוגמה:**

```python
my_dict: dict[str, int] = {"a": 1, "b": 2}

try:
    my_dict.append({"c": 3})
except AttributeError as e:
    print(f"Ошибка: {e}") # פלט: שגיאה: 'dict' object has no attribute 'append'

print(my_dict) # פלט: {'a': 1, 'b': 2}
```

**תוצאה:**
הקוד ניסה לקרוא לפונקציה `append()` שאינה קיימת עבור מילון, מה שהוביל לשגיאת `AttributeError`. המילון המקורי אינו משתנה כתוצאה מכך.

לפיכך, **אפשרות B** נכונה.