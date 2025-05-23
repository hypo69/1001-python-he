### `question_308_interview.md`

**שאלה 308.** מהם אותות (signals) ב-Django, ולפתרון אילו משימות *עיקריות* הם משמשים?

A. אותות ב-Django משמשים להגדרת קשרים בין מודלים של מסד נתונים (לדוגמה, "אחד לרבים" או "רבים לרבים").
B. אותות ב-Django הם מנגנון לביצוע אסינכרוני של משימות, המאפשר הקלה על תהליך הביצוע הראשי של האפליקציה.
C. אותות ב-Django מאפשרים לרכיבים באפליקציה ליידע זה את זה על אירועים שהתרחשו, מה שמועיל ליישום לוגיקה המתבצעת בתגובה לפעולות מסוימות (לדוגמה, שמירת אובייקט).
D. אותות ב-Django משמשים להגדרת הרשאות גישה לחלקים שונים באפליקציה (לדוגמה, מי יכול לערוך אובייקטים מסוימים).

**תשובה נכונה: C**

**הסבר:**

אותות (signals) ב-Django הם מנגנון עוצמתי המאפשר לרכיבים שונים באפליקציה לתקשר זה עם זה, ללא תלות ישירה זה בזה.

*   **כיצד פועלים אותות:**
    *   רכיב אחד באפליקציה *שולח* אות כאשר מתרחש אירוע מסוים (לדוגמה, שמירת מודל, מחיקת מודל, כניסת משתמש מוצלחת למערכת).
    *   רכיבים אחרים באפליקציה יכולים *להירשם* לאותות אלו ולבצע פעולות מסוימות כאשר האות נשלח.

*   **תחומי שימוש עיקריים:**
    *   **תגובה לאירועים:** ביצוע פעולות מסוימות בתגובה לאירועים המתרחשים במודלים (לדוגמה, שליחת התראה לאחר יצירת אובייקט חדש).
    *   **פירוק האפליקציה:** חלוקת הלוגיקה של האפליקציה לחלקים בלתי תלויים. רכיבים יכולים לתקשר דרך אותות, מבלי לדעת זה על זה באופן ישיר.
    *   **הרחבה:** הוספת פונקציונליות חדשה לאפליקציה ללא שינוי הקוד הקיים.

*   **אפשרות A אינה נכונה:** קשרים בין מודלים מתוארים במודלים עצמם.
*   **אפשרות B אינה נכונה:** לביצוע אסינכרוני של משימות ניתן להשתמש ב-Celery, אך לא באותות עצמם.
*   **אפשרות C נכונה:** זוהי בדיוק המשימה העיקרית של האותות.
*   **אפשרות D אינה נכונה:** על הרשאות הגישה אחראים permissions.

**דוגמה:**

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"New user {instance.username} created!")
```

**לסיכום:**

אותות ב-Django מאפשרים לרכיבים באפליקציה ליידע זה את זה על אירועים שהתרחשו, מה שמועיל ליישום לוגיקה המתבצעת בתגובה לפעולות מסוימות, ולהבטחת פירוק והרחבה של האפליקציה.

לפיכך, אפשרות C היא הנכונה.