### `question_855.md`

**שאלה 855.** מה יודפס למסך כתוצאה מהרצת קוד הפייתון הבא?

```python
def multiplication_division(num1, num2):
    return num1 * num2, num1 / num2

product, division = multiplication_division(15, 3)
print("Product =", product, "Quotient =", division) # Product = 45 Quotient = 5.0
```

A.  `Product = 45 Quotient = 5.0`
B.  `Product = (45, 5.0) Quotient = `
C.  `Product = 45 Quotient = `
D.  `Error`

**תשובה נכונה: A**

**הסבר:**

בפייתון, פונקציות יכולות להחזיר מספר ערכים, הנארזים אוטומטית בתוך טאפל (tuple). לאחר מכן, בעת קריאה לפונקציה, ניתן לפרוק (unpack) את הטאפל המוחזר למספר משתנים.

1.  **`def multiplication_division(num1, num2):`**: מוגדרת פונקציה בשם `multiplication_division` המקבלת שני ארגומנטים.
2.  **`return num1 * num2, num1 / num2`**: הפונקציה מחזירה שני ערכים: מכפלת `num1` ו-`num2`, ותוצאת החלוקה של `num1` ב-`num2`. ערכים אלו נארזים אוטומטית לטאפל.
3.  **`product, division = multiplication_division(15, 3)`**: הפונקציה `multiplication_division` נקראת עם הארגומנטים `15` ו-`3`. הטאפל המוחזר `(45, 5.0)` נפרק לשני משתנים: `product` (אשר לו מושם הערך `45`) ו-`division` (אשר לו מושם הערך `5.0`).
4.  **`print("Product =", product, "Quotient =", division)`**: מודפסת המחרוזת "Product =", ערך המשתנה `product`, המחרוזת "Quotient =", וערך המשתנה `division`.

*   **אפשרות A נכונה:** זוהי הפלט הנכון של הקוד. כל הערכים הוצבו כראוי.
*   **אפשרות B אינה נכונה:** הפלט שגוי, שכן המחרוזת `"Quotient"` אמורה להופיע גם כן.
*   **אפשרות C אינה נכונה:** הפלט שגוי, הערכים המודפסים אינם מצוינים.
*   **אפשרות D אינה נכונה:** הקוד תקין תחבירית ולא יגרום לשגיאה.

**כתוצאה מכך:**

על המסך יודפס `Product = 45 Quotient = 5.0`.

לפיכך, אפשרות A היא הנכונה.