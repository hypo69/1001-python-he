### `question_144.md`

**שאלה 44.** מה תהיה הפלט של הקוד הבא?

```python
x: int = 5

def modify_x():
  x = 10
  print(f"הערך של x בתוך הפונקציה: {x}")


modify_x()
print(f"הערך של x מחוץ לפונקציה: {x}")
```

A.  `הערך של x בתוך הפונקציה: 10`, `הערך של x מחוץ לפונקציה: 10`
B.  `הערך של x בתוך הפונקציה: 5`, `הערך של x מחוץ לפונקציה: 5`
C.  `הערך של x בתוך הפונקציה: 10`, `הערך של x מחוץ לפונקציה: 5`
D.  `הערך של x בתוך הפונקציה: 5`, `הערך של x מחוץ לפונקציה: 10`

**תשובה נכונה: C**

**הסבר:**

דוגמה זו מדגימה את ההבדל בין משתנים מקומיים לגלובליים בפייתון.

1.  **משתנה גלובלי:** בתחילת הקוד, נוצר משתנה גלובלי `x` ומקבל את הערך 5.
2.  **הפונקציה `modify_x`:**
    *   בתוך הפונקציה `modify_x`, נוצר משתנה *מקומי* חדש `x` ומקבל את הערך 10.
    *   שינוי המשתנה `x` בתוך הפונקציה אינו משפיע על המשתנה הגלובלי `x`.
    *   בתוך הפונקציה, מודפס הערך של המשתנה המקומי `x`.
3.  **קריאה לפונקציה:** הפונקציה `modify_x()` נקראת, והיא מדפיסה את הערך של המשתנה ה*מקומי* `x`.
4.  **הדפסה מחוץ לפונקציה:** לאחר הקריאה לפונקציה, מודפס הערך של המשתנה ה*גלובלי* `x`.

עתה נבחן את אפשרויות התשובה:

*   **אפשרות A** אינה נכונה: המשתנה הגלובלי לא ישתנה.
*   **אפשרות B** אינה נכונה: המשתנה המקומי ישתנה.
*   **אפשרות C** נכונה: הערכים מודפסים בהתאם לתחום ההיקף (scope).
*   **אפשרות D** אינה נכונה: הערכים מודפסים בסדר שגוי.

**כתוצאה מכך:**

*   הפונקציה `modify_x` תדפיס `"הערך של x בתוך הפונקציה: 10"`.
*   לאחר קריאת הפונקציה, התוכנית תדפיס `"הערך של x מחוץ לפונקציה: 5"`, מכיוון ששינוי המשתנה `x` בתוך הפונקציה אינו משפיע על המשתנה הגלובלי `x`.

לפיכך, **אפשרות C** היא הנכונה.