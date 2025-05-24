### `question_769.md`

**שאלה 769.** פתח פונקציה בפייתון, המקבלת שנה `year` ומספר חודש `month` (כאשר 1 הוא ינואר) כקלט, ומחזירה מחרוזת המכילה את התאריך (בפורמט `YYYY-MM-DD`) של יום שלישי הראשון בחודש זה.

**דוגמאות:**
```
קלט: first_tuesday_of_the_month(1997, 1)
פלט: "1997-01-07"

קלט: first_tuesday_of_the_month(2021, 2)
פלט: "2021-02-02"

קלט: first_tuesday_of_the_month(2023, 3)
פלט: "2023-03-07"
```

- א. לפתרון הבעיה יש להשתמש רק במתודה `datetime.today()` ולבדוק את יום השבוע.
- ב. לפתרון הבעיה יש להשתמש רק בפונקציות לוח שנה של פייתון, כדי למצוא את היום הראשון בחודש ולקבוע את יום השבוע שלו, ובמקרה שזה אינו יום שלישי, לבצע איטרציה עד למציאת יום שלישי.
- ג. לפתרון הבעיה יש להשתמש במתודה `datetime.weekday()` ולחשב את יום שלישי הראשון.
- ד. לפתרון הבעיה יש לעבור על כל ימי החודש ולמצוא את ההופעה הראשונה של יום שלישי.

**תשובה נכונה: ג**

**הסבר:**

לפתרון הבעיה של מציאת יום שלישי הראשון בחודש ושנה נתונים, הגישה הטובה ביותר היא שימוש במתודות של ספריית `datetime`, המספקות את הפונקציונליות הנדרשת ומאפשרות חישוב מדויק של התאריך המבוקש.

*   **אלגוריתם (שימוש בספריית datetime):**
    1.  **יצירת תאריך היום הראשון בחודש:** יוצרים אובייקט תאריך עבור היום הראשון בחודש (לדוגמה `2023-03-01`) באמצעות ספריית `datetime`.
    2.  **בדיקת יום השבוע:** מוצאים את מספר יום השבוע עבור היום הראשון בחודש (כאשר 0 הוא יום שני, ו-6 הוא יום ראשון) באמצעות `date.weekday()`.
        *   **חישוב יום שלישי הראשון:** מחשבים את התאריך של יום שלישי הראשון בחודש, על ידי הוספת המספר הנדרש של ימים כך שהיום הראשון יהיה יום שלישי (מוסיפים 1 - אם יום שני, 0 - אם יום שלישי, 6 - אם יום רביעי, וכו').
    3.  **עיצוב התאריך:** ממירים את התאריך שהתקבל לפורמט הנדרש `YYYY-MM-DD`.
    4.  **החזרת התוצאה:** מחזירים את התאריך כמחרוזת.

*   **יתרונות האלגוריתם:**
    *   **דיוק:** מבטיח מציאה נכונה של יום שלישי.
    *   **יעילות:** אינו דורש מעבר על כל הימים, אלא מחשב את התאריך של יום שלישי הראשון בהתבסס על היום הראשון בחודש.
    *   **שימוש ב-`datetime`:** עושה שימוש בפונקציות המסופקות על ידי מודול `datetime`.

**דוגמאות (פסאודו-קוד):**

```
function first_tuesday_of_the_month(year, month):
    first_day_of_month = create date object for given year, month and 1st day
    day_of_week = first_day_of_month.weekday() # 0 is monday and 6 is sunday
     if day_of_week  is 1
       first_tuesday = first_day_of_month
     elif day_of_week == 0:
       first_tuesday = first_day_of_month + 1 day
    elif day_of_week == 2
        first_tuesday = first_day_of_month + 6 day
    elif day_of_week == 3
      first_tuesday = first_day_of_month + 5 day
    elif day_of_week == 4
       first_tuesday = first_day_of_month + 4 day
     elif day_of_week == 5
      first_tuesday = first_day_of_month + 3 day
    elif day_of_week == 6
     first_tuesday = first_day_of_month + 2 day
   return first_tuesday to string (YYYY-MM-DD)
```

**דוגמאות ליישום בפייתון:**
```python
from datetime import date
from datetime import timedelta

def first_tuesday_of_the_month(year, month):
    first_day = date(year, month, 1)
    day_of_week = first_day.weekday() # 0 is Monday and 6 is Sunday
    days_to_tuesday = (1 - day_of_week) % 7
    first_tuesday = first_day + timedelta(days=days_to_tuesday)
    return first_tuesday.strftime("%Y-%m-%d")
year1 = 1997
month1 = 1
print(f"קלט: year = {year1}, month = {month1}")
print(f"פלט: {first_tuesday_of_the_month(year1, month1)}") # Output: 1997-01-07

year2 = 2021
month2 = 2
print(f"קלט: year = {year2}, month = {month2}")
print(f"פלט: {first_tuesday_of_the_month(year2, month2)}") # Output: 2021-02-02

year3 = 2023
month3 = 3
print(f"קלט: year = {year3}, month = {month3}")
print(f"פלט: {first_tuesday_of_the_month(year3, month3)}")  # Output: 2023-03-07
```

**ניתוח האפשרויות:**
*   **א. לפתרון הבעיה יש להשתמש רק במתודה `datetime.today()` ולבדוק את יום השבוע.:** שגוי. המתודה `today()` תחזיר רק את התאריך הנוכחי, ולא תאריך שרירותי.
*   **ב. לפתרון הבעיה יש להשתמש רק בפונקציות לוח שנה של פייתון, כדי למצוא את היום הראשון בחודש ולקבוע את יום השבוע שלו, ובמקרה שזה אינו יום שלישי, לבצע איטרציה עד למציאת יום שלישי.:** שגוי, לולאה אינה נחוצה כאן, מכיוון שניתן לבצע זאת בביטוי אחד.
*   **ג. לפתרון הבעיה יש להשתמש במתודה `datetime.weekday()` ולחשב את יום שלישי הראשון.:** נכון, אך זהו תיאור חלקי יותר.
*   **ד. לפתרון הבעיה יש לעבור על כל ימי החודש ולמצוא את ההופעה הראשונה של יום שלישי.:** שגוי. מעבר על כל הימים אינו פתרון אופטימלי.

**לסיכום:**
*   האלגוריתם מוצא את יום שלישי הראשון במספר מינימלי של פעולות.
*   נעשה שימוש ביכולות של מודול `datetime` לעבודה עם תאריכים.
*   האלגוריתם מחשב את יום שלישי הראשון, ומעצב אותו למחרוזת.

לפיכך, התשובה הנכונה היא **ג. לפתרון הבעיה יש להשתמש במתודה `datetime.weekday()` ולחשב את יום שלישי הראשון.**