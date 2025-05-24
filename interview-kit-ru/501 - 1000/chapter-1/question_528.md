### `question_528.md`

**שאלה 528.** איזו מבין אפשרויות הקוד המוצגות מהווה פתרון תקין בשורה אחת לספירת מספר האותיות הרישיות בקובץ טקסט?

-   A. `sum(1 for line in open(filename) for char in line if char.isupper())`
-   B. `sum(char.isupper() for line in open(filename) for char in line)`
-   C. `len([char for line in open(filename) for char in line if char.isupper()])`
-   D. `count = 0; with open(filename) as f: for line in f: for char in line: if char.isupper(): count +=1`

**תשובה נכונה: A**

**הסבר:**

שאלה זו עוסקת בשימוש בגנרטורים ובפונקציות מסדר גבוה לצורך פתרון תמציתי של בעיות בפייתון.

*   **הבנת הבעיה:** נדרש לקרוא קובץ טקסט, לעבור תו אחר תו על תוכנו ולספור את מספר האותיות הרישיות.
*   **פתרון בשורה אחת:**
    *   `open(filename)` פותח את הקובץ לקריאה.
    *   `for line in open(filename)`: מייצר שורות מהקובץ בזו אחר זו.
    *    `for char in line`: מייצר תווים מכל שורה בזו אחר זו
    *   `if char.isupper()`: תנאי בדיקה, האם התו הנוכחי הוא אות רישית.
    *   `1 for ... if char.isupper()`: ביטוי גנרטור שמחזיר `1` עבור כל אות רישית.
    *   `sum(...)`: פונקציית sum מקבלת גנרטור ומסכמת את כל האחדות, וסופרת בכך את מספר האותיות הרישיות.

**ניתוח האפשרויות:**

*   **A. `sum(1 for line in open(filename) for char in line if char.isupper())`:** נכון. זהו פתרון קומפקטי בשורה אחת, המשתמש בגנרטור ובפונקציה `sum()`.
*   **B. `sum(char.isupper() for line in open(filename) for char in line)`:** לא נכון. כאן מסוכמות התוצאות `True` ו-`False` (ערכים לוגיים), ולא כמות האותיות הרישיות.
*  **C. `len([char for line in open(filename) for char in line if char.isupper()])`**: נכון. אך אפשרות זו משתמשת ב-list comprehension, מה שפחות יעיל מאשר ביטוי גנרטור באפשרות A.
*  **D. `count = 0; with open(filename) as f: for line in f: for char in line: if char.isupper(): count +=1`:** לא נכון. זהו קוד רב-שורתי, ונדרש פתרון בשורה אחת.

**דוגמת שימוש:**
נניח שיש לנו קובץ בשם `test.txt` עם התוכן הבא:

```
Hello World!
Python Is AWESOME.
```
```python
filename = "test.txt"
count = sum(1 for line in open(filename) for char in line if char.isupper())
print(count) # יציג 5
```
**לסיכום:**
*   גנרטורים ו-list comprehension מאפשרים לכתוב קוד קומפקטי ותמציתי.
*   פתרונות בשורה אחת יכולים להיות נוחים למשימות פשוטות, אך יש לשקול את קריאות הקוד.
*   שימוש בגנרטורים יעיל יותר מ-list comprehension במקרה זה.

לפיכך, התשובה הנכונה היא **A. `sum(1 for line in open(filename) for char in line if char.isupper())`**.