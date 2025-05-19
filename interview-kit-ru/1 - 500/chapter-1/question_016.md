### `question_016.md`

**שאלה 16.** מה יהיה הפלט של קטע הקוד הבא בפייתון בעת הרצתו?

```python
x = "Python"
y = 15
print("Welcome to " + x + " programming where the value of y is " + str(y))
```

- A.  `Welcome to Python programming where the value of y is 15`
- B.  `שגיאה עקב סוגי נתונים לא תואמים`
- C.  `Welcome to Python programming where the value of y is y`
- D.  `אף אחד מהאפשרויות הנ"ל`

**תשובה נכונה: A**

**הסבר:**

בפייתון, האופרטור `+` משמש לשרשור (איחוד) מחרוזות. עם זאת, לא ניתן להשתמש בו לאיחוד ישיר של מחרוזות עם סוגי נתונים אחרים (למשל, עם מספרים שלמים). בקוד זה, המשתנה `y` הוא מספר שלם, ולכן יש להמיר אותו למחרוזת על מנת שניתן יהיה לשרשר אותו עם ליטרלים מחרוזתיים והמשתנה `x`. לשם כך משתמשים בפונקציה `str()`.

ננתח את הקוד צעד אחר צעד:

1.  `x = "Python"`: למשתנה `x` מושם הערך המחרוזתי `"Python"`.
2.  `y = 15`: למשתנה `y` מושם הערך השלם `15`.
3. `print("Welcome to " + x + " programming where the value of y is " + str(y))`:
    *   נוצרת המחרוזת `"Welcome to "`.
    *  למחרוזת זו מתווספת המחרוזת מתוך המשתנה `x` (`"Python"`), באמצעות האופרטור `+`.
    *  למחרוזת שהתקבלה מתווספת המחרוזת `" programming where the value of y is "`.
    *  המשתנה `y` (שהוא מספר שלם) מומר למחרוזת באמצעות `str(y)`, ומשרשור לאחר מכן למחרוזת הקודמת.
    *   המחרוזת הסופית מודפסת למסך.

*   **אפשרות A**: `Welcome to Python programming where the value of y is 15` - זהו הפלט הנכון, מכיוון שהמשתנה y הומר כהלכה למחרוזת.
*   **אפשרות B**: שגיאה עקב סוגי נתונים לא תואמים. אפשרות זו הייתה נכונה אילו לא הייתה בשימוש הפונקציה `str(y)` להמרת מספר שלם למחרוזת.
*   **אפשרות C**: `Welcome to Python programming where the value of y is y` - אפשרות שגויה, מכיוון שהמשתנה `y` חייב לעבור המרה למחרוזת, ויוצג ערכו, ולא שמו.
*  **אפשרות D**: אף אחד מהאפשרויות הנ"ל - אפשרות שגויה, מכיוון שאפשרות A נכונה.

**דוגמה:**

```python
x: str = "Python"
y: int = 15
result_string: str = "Welcome to " + x + " programming where the value of y is " + str(y)
print(result_string) # פלט: Welcome to Python programming where the value of y is 15
```

**לסיכום:**

הקוד ירוץ ללא שגיאות, מכיוון שהמספר השלם `y` מומר למחרוזת לפני השרשור, וידפיס למסך את המחרוזת `Welcome to Python programming where the value of y is 15`.

לפיכך, **אפשרות A** היא התשובה הנכונה.