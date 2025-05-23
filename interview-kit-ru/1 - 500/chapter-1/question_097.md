### `question_97.md`

**שאלה 97.** מה עושה מילת המפתח `yield` בפייתון?

- א. מסיימת פונקציה.
- ב. מחזירה ערך מפונקציה ומשעה את מצבה.
- ג. מונעת ביצוע לולאה.
- ד. מדלגת על האיטרציה הנוכחית של הלולאה.

**תשובה נכונה: ב**

**הסבר:**

מילת המפתח `yield` בפייתון משמשת להגדרת מחוללים (generators). מחוללים הם סוג מיוחד של פונקציות המאפשרות איטרציה עצלה (lazy iteration), כלומר, הן מחזירות ערכים אחד אחד, תוך השעיית הביצוע שלהן בין קריאות.

*   **אפשרות א'** אינה נכונה: `yield` אינה מסיימת פונקציה, אלא משעה את ביצועה.
*   **אפשרות ב'** נכונה: `yield` מחזירה ערך ומשעה את מצב הפונקציה.
*   **אפשרות ג'** אינה נכונה: `yield` אינה מונעת ביצוע לולאה.
*   **אפשרות ד'** אינה נכונה: `yield` אינה מדלגת על איטרציות בלולאה.

**איך `yield` עובדת:**

1.  פונקציה המכילה `yield` הופכת למחולל.
2.  בעת קריאה למחולל, הוא אינו מבצע את קוד הפונקציה מיידית, אלא מחזיר איטרטור.
3.  כאשר מתודת `__next__` נקראת על האיטרטור, המחולל מבצע את הקוד עד לאופרטור `yield`.
4.  לאחר `yield`, הפונקציה מחזירה ערך ומשעה את מצבה, תוך שמירת כל המשתנים המקומיים.
5.  בעת קריאה חוזרת ל-`__next__`, או כאשר נדרש האלמנט הבא בלולאת `for`, ביצוע הפונקציה ממשיך מהמקום בו הושעה.

**יתרונות `yield`:**

1.  **יצירה עצלה:** ערכים נוצרים לפי הצורך, מה שחוסך בזיכרון.
2.  **תמיכה במאגרי נתונים גדולים:** מחוללים אידיאליים לעבודה עם כמויות גדולות של נתונים שעלולות לא להיכנס לזיכרון.
3.  **עיבוד נתונים בזרם:** מחוללים יכולים לעבד נתונים ביעילות ככל שהם מגיעים.

**דוגמה:**

```python
def my_generator(n: int) -> int:
  for i in range(n):
    yield i * 2

gen = my_generator(5)
for number in gen:
  print(number)
# פלט:
# 0
# 2
# 4
# 6
# 8
```
**כתוצאה מכך:**
הפונקציה `my_generator()` משתמשת ב-`yield` ליצירת ערכים אחד אחד. לולאת ה-`for` מקבלת ערכים מהמחולל ומעבדת אותם.

לפיכך, **אפשרות ב'** היא הנכונה.