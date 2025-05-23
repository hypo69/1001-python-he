### `question_307.md`

**שאלה 307.** איזו מבין האפשרויות הבאות היא הדרך הנכונה להגדיר פונקציית Python שתחזיר מספר ערכים, ומה יהיה סוג הנתונים של התוצאה המוחזרת?

A. `def multiply(a, b): return a * b, a + b`
B. `def multiply(a, b): return [a * b, a + b]`
C. `def multiply(a, b): return (a * b, a + b)`
D. `def multiply(a, b): return {a * b, a + b}`

**תשובה נכונה: C**

**הסבר:**

ב-Python, כדי שפונקציה תחזיר מספר ערכים, יש להשתמש בטיפל (tuple). זאת מושגת באמצעות רישום הערכים המוחזרים מופרדים בפסיקים, אשר נארזים באופן אוטומטי לתוך טיפל.

*   **אפשרות A אינה נכונה:** אף על פי שתחביר זה תקין, הוא יוצר טיפל באופן מרומז, בעוד שאפשרות C מציגה את יצירת הטיפל באופן מפורש.
*   **אפשרות B אינה נכונה:** תחביר זה יחזיר *רשימה* (list), ולא טיפל.
*   **אפשרות C נכונה:** זוהי הדרך הנכונה להגדיר פונקציה המחזירה מספר ערכים בצורת טיפל.
*   **אפשרות D אינה נכונה:** תחביר זה יחזיר *מְסֻלֶמֶת* (set), ולא טיפל.

**כיצד פועלת החזרת מספר ערכים:**

1.  רשמו את הערכים המוחזרים מופרדים בפסיקים לאחר האופרטור `return` (למשל, `return value1, value2`).
2.  Python אורזת ערכים אלה באופן אוטומטי לתוך *טיפל*.
3.  הצד הקורא יקבל טיפל זה ויכול לפרוק אותו למשתנים נפרדים.

**דוגמה:**

```python
def multiply(a, b):
    return (a * b, a + b)  # מחזיר טיפל

result = multiply(5, 3)
print(f"Type of result: {type(result)}") # Output: <class 'tuple'>
print(result) # Output: (15, 8)
product, sum_result = multiply(5,3) # פירוק הטיפל המוחזר
print(product) # Output: 15
print(sum_result) # Output: 8

def multiply2(a, b):
  return a*b, a+b # אותו הדבר, אך מרומז

result = multiply2(5,3)
print(result) # Output: (15, 8)

```

**לסיכום:**

כדי להגדיר פונקציית Python המחזירה מספר ערכים, יש להשתמש באופרטור `return` עם מספר ערכים המופרדים בפסיקים, מה שיוצר באופן אוטומטי טיפל. סוג הנתונים של התוצאה המוחזרת יהיה טיפל.

לפיכך, אפשרות C היא הנכונה.