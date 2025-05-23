### `question_730.md`

**שאלה 730.** פתח פונקציה בפייתון המקבלת כשתי מטריצות ריבועיות (רשימות של רשימות) ומחזירה את סכומן. כל אלמנטי המטריצות הם מספרים שלמים. יש ליישם את האלגוריתם ללא שימוש בספריית `numpy` ובשיטה `matrix.sum()`.

**דוגמאות:**
```
קלט: 
matrixAddition([ [1, 2, 3], [3, 2, 1], [1, 1, 1] ], [[2, 2, 1], [3, 2, 3], [1, 1, 3]])
פלט: [[3, 4, 4], [6, 4, 4], [2, 2, 4]]

```

- א. כדי לפתור את הבעיה, יש פשוט לעבור על כל אלמנטי המטריצות ולסכום אותם בזה אחר זה.
- ב. כדי לפתור את הבעיה, יש להשתמש באלגוריתם רקורסיבי ולסכום את האלמנטים באלכסון.
- ג. כדי לפתור את הבעיה, יש להשתמש באלגוריתם עם שתי לולאות, שבו ערכי האלמנטים עם אינדקסים זהים במטריצות מסוכמים, ונכתבים למטריצה חדשה.
- ד. כדי לפתור את הבעיה, יש למיין תחילה את שתי המטריצות, ולאחר מכן לסכום אותן.

**תשובה נכונה: C**

**הסבר:**

כדי לפתור את בעיית חיבור שתי מטריצות, יש להשתמש באלגוריתם איטרטיבי עם שתי לולאות מקוננות, שיעבור על כל תא במטריצות ויסכום את האלמנטים המתאימים, תוך יצירת רשימה חדשה.

*   **אלגוריתם (איטרטיבי עם לולאות מקוננות):**
    1.  **ממדי המטריצות:** יש לוודא שלמטריצות ממדים זהים.
    2.  **יצירת מטריצת התוצאה:** יש ליצור מטריצה חדשה, `result`, באותם ממדים כמו המטריצות המקוריות, אותה נמלא תוך כדי חישוב סכום האלמנטים.
    3.  **לולאות מקוננות:** יש לעבור על כל שורה ועל כל עמודה במטריצות באמצעות שתי לולאות `for`:
        *   יש לסכום את האלמנטים באינדקסים הנוכחיים `[row][col]` משתי המטריצות ולכתוב את סכומם למטריצת התוצאה `result[row][col]`.
    4.  **החזרת התוצאה:** לאחר שעברנו על כל האלמנטים, יש להחזיר את מטריצת התוצאה `result`.

*   **יתרונות האלגוריתם:**
    *   **פשטות:** הקוד קל ליישום ולהבנה.
    *   **יעילות:** יש לו סיבוכיות זמן לינארית `O(n^2)` (כאשר n הוא גודל צלע המטריצה הריבועית), והוא אינו משתמש בזיכרון נוסף.

**דוגמאות (פסאודו-קוד):**
```
function matrix_addition(matrix1, matrix2):
  result = create a matrix with the same dimensions as matrix1 and zeroed out

  for i from 0 to the number of rows in matrix1:
    for j from 0 to number of cols in matrix1:
       result[i][j] = matrix1[i][j] + matrix2[i][j]
  return result;
```
**דוגמאות ליישום בפייתון:**

```python
def matrix_addition(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

matrix1 = [ [1, 2, 3],
            [3, 2, 1],
            [1, 1, 1] ]

matrix2 = [[2, 2, 1],
           [3, 2, 3],
           [1, 1, 3] ]

print(f"קלט: matrix1 = {matrix1}, matrix2 = {matrix2}")
print(f"פלט: {matrix_addition(matrix1,matrix2)}")

```
**ניתוח האפשרויות:**
*   **א. כדי לפתור את הבעיה, יש פשוט לעבור על כל אלמנטי המטריצות ולסכום אותם בזה אחר זה.:** שגוי.
*   **ב. כדי לפתור את הבעיה, יש להשתמש באלגוריתם רקורסיבי ולסכום את האלמנטים באלכסון.:** שגוי. אלגוריתם רקורסיבי אינו אופטימלי לבעיה זו.
*   **ג. כדי לפתור את הבעיה, יש להשתמש באלגוריתם עם שתי לולאות, שבו ערכי האלמנטים עם אינדקסים זהים במטריצות מסוכמים, ונכתבים למטריצה חדשה.:** נכון.
*   **ד. כדי לפתור את הבעיה, יש למיין תחילה את שתי המטריצות, ולאחר מכן לסכום אותן.:** שגוי. מיון אינו נחוץ.

**לסיכום:**
*   שתי לולאות מקוננות מאפשרות לעבור על כל האלמנטים במערך דו-ממדי.
*   האלגוריתם מחשב את הסכום עבור כל זוג אלמנטים ויוצר מערך תוצאה חדש.
*   סיבוכיות האלגוריתם היא O(n*n) או O(n^2).

לפיכך, התשובה הנכונה היא **ג. כדי לפתור את הבעיה, יש להשתמש באלגוריתם עם שתי לולאות, שבו ערכי האלמנטים עם אינדקסים זהים במטריצות מסוכמים, ונכתבים למטריצה חדשה.**