### `question_615.md`

**שאלה 615.** כיצד ניתן ב-Python לפרוס (לבצע חיתוך) רשימה לחלקים? תאר/י את תחביר הפריסה של רשימה, והבא/י דוגמאות שימוש עם ערכים שונים של הפרמטרים `start`, `stop` ו-`step`.

*   א. פריסת הרשימה מתבצעת באמצעות הפונקציה `split(list, start, stop, step)`.
*   ב. פריסת הרשימה מתבצעת באמצעות המתודה `slice()`, המקבלת את הפרמטרים `start`, `stop` ו-`step`.
*   ג. פריסת הרשימה מתבצעת באמצעות סוגריים מרובעים `[]` והפרמטרים `start`, `stop`, ו-`step` בפורמט `list[start:stop:step]`.
*   ד. פריסת הרשימה מתבצעת רק באמצעות לולאות ותנאים.

**תשובה נכונה: ג**

**הסבר:**

ב-Python, עבור פריסה (יצירת פרוסה) של רשימה לחלקים משתמשים בתחביר הפריסה (slicing), המאפשר לחלץ תת-רצפים מהרשימה באמצעות ציון `start`, `stop`, ו-`step`.

*   **תחביר פריסה:**
    *   `list[start:stop:step]`
        *   `start`: אינדקס ההתחלה של הפרוסה (ברירת מחדל 0).
        *   `stop`: אינדקס הסוף של הפרוסה (לא כולל אותו), (ברירת מחדל היא אורך הרשימה).
        *   `step`: הצעד בין איברי הפרוסה (ברירת מחדל 1).
    *   אם הפרמטרים אינם מצוינים, נעשה שימוש בערכי ברירת המחדל.
    *   פריסות יוצרות רשימות *חדשות*, מבלי לשנות את הרשימה המקורית.

*   **דרכי שימוש עיקריות בפריסות:**
    *   `list[:]` או `list[::]` - עותק של כל הרשימה.
    *   `list[start:]` - פרוסה מ-`start` ועד סוף הרשימה.
    *   `list[:stop]` - פרוסה מההתחלה ועד `stop` (לא כולל `stop`).
    *   `list[start:stop]` - פרוסה מ-`start` ועד `stop` (לא כולל `stop`).
    *   `list[start:stop:step]` - פרוסה מ-`start` ועד `stop` (לא כולל `stop`), עם צעד נתון `step`.
    *   ניתן להשתמש בערכים שליליים עבור `start`, `stop` ו-`step`.

**דוגמאות:**

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"רשימה מקורית: {my_list}")
# פרוסה מההתחלה ועד אינדקס 2 (לא כולל)
print(f"my_list[:2]: {my_list[:2]}") # יציג: [0, 1]

# פרוסה מאינדקס 8 ועד הסוף
print(f"my_list[8:]: {my_list[8:]}") # יציג: [8, 9]

# פרוסה מאינדקס 2 ועד 8 (לא כולל)
print(f"my_list[2:8]: {my_list[2:8]}") # יציג: [2, 3, 4, 5, 6, 7]

# פרוסה מאינדקס 2 ועד 8 (לא כולל) עם צעד 2
print(f"my_list[2:8:2]: {my_list[2:8:2]}") # יציג: [2, 4, 6]

# פרוסה מההתחלה ועד הסוף (עותק)
copy_list = my_list[:]
print(f"עותק רשימה ([:] ): {copy_list}") # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# אינדקסים שליליים
print(f"my_list[-1:]:{my_list[-1:]}") # יציג: [9] (האיבר האחרון)
print(f"my_list[:-2]:{my_list[:-2]}") # יציג: [0, 1, 2, 3, 4, 5, 6, 7] (הכל למעט שני האחרונים)

# צעד שלילי
print(f"my_list[::-1]:{my_list[::-1]}") # יציג: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (היפוך)
```
**ניתוח האפשרויות:**
*   **א. פריסת הרשימה מתבצעת באמצעות הפונקציה `split(list, start, stop, step)`.:** לא נכון.
*   **ב. פריסת הרשימה מתבצעת באמצעות המתודה `slice()`, המקבלת את הפרמטרים `start`, `stop` ו-`step`.:** לא נכון.
*   **ג. פריסת הרשימה מתבצעת באמצעות סוגריים מרובעים `[]` והפרמטרים `start`, `stop`, ו-`step` בפורמט `list[start:stop:step]`.:** נכון.
*   **ד. פריסת הרשימה מתבצעת רק באמצעות לולאות ותנאים.:** לא נכון.

**לסיכום:**
*   פריסות הן כלי רב עוצמה לקבלת חלקים מרשימה.
*   התחביר `list[start:stop:step]` מאפשר לחלץ תת-רצפים בצורה גמישה עם פרמטרים נתונים.
*   פריסות אינן משנות את הרשימה המקורית, אלא מחזירות עותק חדש.

לפיכך, התשובה הנכונה היא **ג. פריסת הרשימה מתבצעת באמצעות סוגריים מרובעים `[]` והפרמטרים `start`, `stop`, ו-`step` בפורמט `list[start:stop:step]`.**