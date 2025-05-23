### `question_706.md`

**שאלה 706.** נתונה מטריצה דו-ממדית של מספרים שלמים `matrix`, כאשר המספרים ממוינים בסדר עולה הן מלמעלה למטה והן משמאל לימין בכל שורה. פתח אלגוריתם יעיל לקביעת האם מספר שלם נתון `target` קיים במטריצה, עם סיבוכיות O(log(m\*n)).

**דוגמאות:**
```
קלט: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
פלט: True

קלט: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
פלט: False
```

*   א. כדי לפתור את הבעיה יש לעבור על כל אלמנטי המטריצה באמצעות שתי לולאות מקוננות.
*   ב. כדי לפתור את הבעיה יש למיין את המטריצה ולהשתמש בחיפוש בינארי.
*   ג. כדי לפתור את הבעיה יש לצמצם את המטריצה למערך חד-ממדי ולאחר מכן להשתמש בחיפוש בינארי.
*   ד. כדי לפתור את הבעיה, ניתן להשתמש בחיפוש בינארי, על ידי התייחסות למטריצה כאל רצף ממוין ומעבר עליה באמצעות חישוב קואורדינטות מתוך האינדקס.

**תשובה נכונה: ד**

**הסבר:**

לפתרון בעיית חיפוש אלמנט במטריצה דו-ממדית ממוינת עם סיבוכיות זמן של O(log(m\*n)), האלגוריתם המתאים ביותר הוא התאמה של חיפוש בינארי. אלגוריתם זה מתייחס למטריצה כאל רצף ממוין, כאשר קואורדינטות האלמנט בפועל מחושבות על בסיס האינדקס.

*   **אלגוריתם (חיפוש בינארי):**
    1.  **גבולות החיפוש:** אתחל את המצביע השמאלי `left` כ-`0` ואת המצביע הימני `right` כ-`m * n - 1`, כאשר `m` הוא מספר השורות ו-`n` הוא מספר העמודות במטריצה.
    2.  **חיפוש בינארי:**
        *   חשב את האמצע: `mid = left + (right-left)//2`
        *   **המרת אינדקס לקואורדינטות:** חשב את קואורדינטות השורה והעמודה על פי האינדקס `mid`:
            *   `row = mid // n`
            *   `col = mid % n`.
        *   **השוואה:** השווה את הערך `matrix[row][col]` לערך המטרה `target`.
        *   **תנאי חיפוש בינארי:**
            *   אם `matrix[row][col]` שווה ל-`target` - האלמנט נמצא.
            *   אם `matrix[row][col]` קטן מ-`target`, הזז את הגבול השמאלי ל-`mid + 1`.
            *   אם `matrix[row][col]` גדול מ-`target`, הזז את הגבול הימני ל-`mid - 1`.
    3.  **תוצאה:** לאחר השלמת החיפוש הבינארי, החזר `True` אם האלמנט נמצא, או `False` אם לא נמצא.

*   **יתרונות האלגוריתם:**
    *   **סיבוכיות לוגריתמית:** מאפשר להגיע לסיבוכיות זמן של O(log (m\*n)), שהיא יעילה משמעותית מ-O(n\*m).
    *   **עובד עם כל גדלים:** האלגוריתם עובד עם מטריצות בכל גודל.
    *   **פשטות:** הקוד פשוט למדי למימוש.

**דוגמאות (פסאודו-קוד):**
```
function search_matrix(matrix, target):
    m = number of rows # מספר השורות
    n = number of columns # מספר העמודות
    left = 0
    right = m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        row = mid // n
        col = mid % n
       if matrix[row][col] == target:
           return True
       elif matrix[row][col] < target:
          left = mid + 1
       else:
         right = right - 1
    return False
```
**דוגמאות מימוש ב-Python:**
```python
def search_matrix(matrix, target):
    m = len(matrix)
    if m == 0:
      return False
    n = len(matrix[0])
    left = 0
    right = m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = right - 1
    return False
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
print(f"קלט: matrix = {matrix1}, target = {target1}")
print(f"פלט: {search_matrix(matrix1, target1)}") # פלט: True

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(f"קלט: matrix = {matrix2}, target = {target2}")
print(f"פלט: {search_matrix(matrix2, target2)}") # פלט: False
```
**ניתוח האפשרויות:**

*   **א. כדי לפתור את הבעיה יש לעבור על כל אלמנטי המטריצה באמצעות שתי לולאות מקוננות.:** שגוי. סריקה מלאה בעלת סיבוכיות O(n\*m).
*   **ב. כדי לפתור את הבעיה יש למיין את המטריצה ולהשתמש בחיפוש בינארי.:** שגוי. המטריצה כבר ממוינת.
*   **ג. כדי לפתור את הבעיה יש לצמצם את המטריצה למערך חד-ממדי ולאחר מכן להשתמש בחיפוש בינארי.:** שגוי, מכיוון שזה יגרום לעלויות נוספות של הקצאת זיכרון.
*   **ד. כדי לפתור את הבעיה ניתן להשתמש בחיפוש בינארי, על ידי התייחסות למטריצה כאל רצף ממוין ומעבר עליה באמצעות חישוב קואורדינטות מתוך האינדקס.:** נכון.

**לסיכום:**
*   אלגוריתם החיפוש הבינארי עם חישוב קואורדינטות מאפשר למצוא אלמנטים במטריצה ממוינת בסיבוכיות `O(log(m*n))`.
*   האלגוריתם משתמש במנגנון של חלוקה לשני חלקים ובדיקת האלמנט האמצעי.
*   הקואורדינטות המתקבלות מאפשרות לעבור על המטריצה כאילו הייתה רשימה ארוכה אחת ממוינת.

לפיכך, התשובה הנכונה היא **ד. כדי לפתור את הבעיה ניתן להשתמש בחיפוש בינארי, על ידי התייחסות למטריצה כאל רצף ממוין ומעבר עליה באמצעות חישוב קואורדינטות מתוך האינדקס.**