### `question_879.md`

**שאלה 879.** כיצד ב-Python מתבצעת החלפה סימולטנית של ערכים בין שני משתנים באמצעות התחביר `a, b = b, a`, ואילו יתרונות יש לשיטה זו בהשוואה לגישה המסורתית המשתמשת במשתנה זמני?

A. ‏Python מבצעת פעולה זו על ידי יצירת משתנה זמני לאחסון אחד הערכים, בדומה לשפות תכנות אחרות.
B. ‏Python מבצעת פעולה זו על ידי השמת ערכים באופן סדרתי מימין לשמאל, ולכן אין צורך במשתנה זמני.
C. ‏Python יוצרת תחילה טאפל מהערכים בצד ימין של הביטוי, ולאחר מכן פורקת טאפל זה למשתנים מצד שמאל, ומבצעת את הכל בצעד אחד ללא יצירה מפורשת של משתנה זמני.
D. תחביר זה הוא קיצור לשתי פעולות השמה נפרדות ואין לו קשר לטאפלים.

**תשובה נכונה: C**

**הסבר:**

ב-Python, החלפה סימולטנית של ערכים באמצעות התחביר `a, b = b, a` היא דרך אלגנטית ויעילה להחליף את הערכים של שני משתנים.

1.  **אריזת טאפל (Tuple Packing):** ראשית, Python מחשבת את הערכים בצד ימין של הביטוי (`b, a`) ואורזת אותם בטאפל.
2.  **פריקת טאפל (Tuple Unpacking):** לאחר מכן, טאפל זה נפרק למשתנים המצוינים בצד שמאל (`a, b`). חשוב לציין ששתי הפעולות (אריזה ופריקה) מתבצעות *במקביל*.

*   **יתרונות:**
    *   **היעדר משתנה זמני:** אין צורך ליצור משתנה זמני לאחסון אחד הערכים, מה שהופך את הקוד לתמציתי וקריא יותר.
    *   **אטומיות:** הפעולה מתבצעת כיחידה שלמה אחת. הדבר מאפשר להימנע מבעיות שעלולות להיווצר במקרה של ביצוע חלקי של הפעולה (לדוגמה, בעת התרחשות חריגה).
    *   **יעילות:** Python ממוטבת לעבודה עם טאפלים, ולכן השמה סימולטנית מתבצעת במהירות מספקת.

*   **אפשרות A אינה נכונה:** ב-Python פעולה זו אינה דורשת משתנה זמני.
*   **אפשרות B אינה נכונה:** ההשמה אינה מתרחשת באופן סדרתי.
*   **אפשרות C נכונה:** זהו תיאור מדויק של אופן הפעולה של תחביר זה.
*   **אפשרות D אינה נכונה:** התחביר קשור ישירות ליצירת טאפל.

**דוגמה:**

```python
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")

a, b = b, a  # החלפה סימולטנית של ערכים

print(f"After swap: a = {a}, b = {b}")
```

**כתוצאה מכך:**

Python יוצרת תחילה טאפל מהערכים בצד ימין של הביטוי `b, a`, ולאחר מכן פורקת טאפל זה למשתנים `a` ו-`b`, מה שמאפשר לבצע החלפה סימולטנית של ערכים ללא שימוש במשתנה זמני.

לפיכך, אפשרות C היא הנכונה.