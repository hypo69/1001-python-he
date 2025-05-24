### `question_016.md`

**שאלה 16.** מה תהיה הפלט של קטע קוד Python הבא בעת הרצתו?

```python
x = "Python"
y = 15
print("Welcome to " + x + " programming where the value of y is " + str(y))
```

- A. `Welcome to Python programming where the value of y is 15`
- B. שגיאה עקב טיפוסי נתונים לא תואמים
- C. `Welcome to Python programming where the value of y is y`
- D. אף אחת מהתשובות לעיל

**תשובה נכונה: A**

**הסבר:**

ב-Python, האופרטור `+` משמש לשרשור (חיבור) מחרוזות. אולם, הוא אינו יכול לשמש לחיבור ישיר של מחרוזות עם טיפוסי נתונים אחרים (לדוגמה, עם מספרים שלמים). בקוד זה, המשתנה `y` הוא מספר שלם, ולכן יש להמיר אותו למחרוזת כדי שניתן יהיה לשרשר אותו עם ליטרלים מחרוזתיים והמשתנה `x`. לשם כך משתמשים בפונקציה `str()`.

ננתח את הקוד שלב אחר שלב:

1.  `x = "Python"`: למשתנה `x` מושם הערך המחרוזתי `"Python"`.
2.  `y = 15`: למשתנה `y` מושם הערך המספרי השלם `15`.
3. `print("Welcome to " + x + " programming where the value of y is " + str(y))`:
    *   נוצרת המחרוזת `"Welcome to "`.
    *   למחרוזת זו מצורפת (באמצעות האופרטור `+`) המחרוזת מהמשתנה `x` (`"Python"`).
    *   למחרוזת שהתקבלה מצורפת המחרוזת `" programming where the value of y is "`.
    *   המשתנה `y` (שהוא מספר שלם) מומר למחרוזת באמצעות `str(y)`, ולאחר מכן משרשור למחרוזת הקודמת.
    *   המחרוזת הסופית מודפסת על המסך.

*   **אפשרות A**: `Welcome to Python programming where the value of y is 15` - זוהי הפלט הנכונה, מכיוון שהמשתנה `y` הומר כהלכה למחרוזת.
*   **אפשרות B**: שגיאה עקב טיפוסי נתונים לא תואמים. אפשרות זו הייתה נכונה אילו לא הייתה בשימוש הפונקציה `str(y)` להמרת המספר השלם למחרוזת.
*   **אפשרות C**: `Welcome to Python programming where the value of y is y` - אפשרות שגויה, כיוון שהמשתנה `y` אמור להיות מומר למחרוזת, וערכו יודפס, לא שמו.
*   **אפשרות D**: אף אחת מהתשובות לעיל - אפשרות שגויה, מכיוון שאפשרות A נכונה.

**דוגמה:**

```python
x: str = "Python"
y: int = 15
result_string: str = "Welcome to " + x + " programming where the value of y is " + str(y)
print(result_string) # פלט: Welcome to Python programming where the value of y is 15
```

**לסיכום:**

הקוד יבוצע ללא שגיאות, מכיוון שהמספר השלם `y` מומר למחרוזת לפני השרשור, והוא ידפיס על המסך את המחרוזת `Welcome to Python programming where the value of y is 15`.

לפיכך, **אפשרות A** היא התשובה הנכונה.