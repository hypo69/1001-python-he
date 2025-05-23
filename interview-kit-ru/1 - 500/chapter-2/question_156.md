### `question_156.md`

**שאלה 56.** איזו מהפונקציות הבאות בשפת Python מאפשרת יצירת פונקציה אנונימית?

A.  `def`
B.  `lambda`
C.  `function`
D.  `anon`

**התשובה הנכונה: B**

**הסבר:**

בשפת Python, פונקציות אנונימיות נוצרות באמצעות מילת המפתח `lambda`. פונקציות למדא (lambda) הן פונקציות המוגדרות בשורה אחת ואין להן שם.

*   **אפשרות A** אינה נכונה: `def` משמשת להגדרת פונקציות רגילות בעלות שם.
*   **אפשרות B** נכונה: `lambda` משמשת ליצירת פונקציות אנונימיות.
*   **אפשרות C** אינה נכונה: `function` אינה מילת מפתח.
*  **אפשרות D** אינה נכונה: `anon` אינה מילת מפתח.

**אופן הפעולה של `lambda`:**

1.  לפונקציות למדא (lambda) יש את התחביר הבא: `lambda arguments: expression`.
2.  `arguments` - זו רשימת הפרמטרים שהפונקציה מקבלת, מופרדים בפסיקים.
3.  `expression` - זהו ביטוי יחיד המחושב ומחזיר תוצאה.
4.  פונקציות למדא אינן יכולות להכיל אופרטורי השמה או ביטויים מרובים.

**דוגמה:**

```python
# Лямбда-функция, которая умножает число на 2
double: Callable = lambda x: x * 2
print(double(5)) # Вывод: 10

# Использование lambda в map
numbers: list[int] = [1, 2, 3, 4]
squared_numbers: list[int] = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Вывод: [1, 4, 9, 16]
```

**לסיכום:**
*   בדוגמה לעיל, `lambda x: x * 2` יוצרת פונקציה אנונימית המחזירה את מכפלת `x` ב-`2`.
*  הפונקציה `lambda` מועברת לפונקציה `map()` ומחשבת את הריבועים עבור כל מספר ברשימה `numbers`.

לפיכך, **אפשרות B** היא התשובה הנכונה.