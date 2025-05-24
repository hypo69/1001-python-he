### `question_637.md`

**שאלה 637.** מהו ההבדל בין שיטות הקסם (magic methods) `__getattr__` ו-`__getattribute__` בפייתון, ובאילו מקרים השימוש בהן יכול להיות מועיל?

*   א. השיטה `__getattr__` נקראת בניסיון לקבל כל מאפיין של אובייקט, בעוד שהשיטה `__getattribute__` נקראת רק בעת גישה לשיטות (methods) של אובייקט.
*   ב. השיטה `__getattribute__` נקראת בניסיון לקבל כל מאפיין של אובייקט, בעוד שהשיטה `__getattr__` נקראת רק בעת גישה למאפיינים שאינם קיימים.
*   ג. השיטה `__getattr__` משמשת לשינוי מאפיינים של אובייקט, בעוד ש-`__getattribute__` משמשת לקבלת מידע על אובייקט.
*   ד. השיטות `__getattr__` ו-`__getattribute__` הן חלופיות זו לזו ומבצעות את אותה הפונקציה.

**תשובה נכונה: ב**

**הסבר:**

בפייתון, `__getattr__` ו-`__getattribute__` הן שיטות קסם המאפשרות שליטה על גישה למאפיינים של אובייקט. הן ממלאות תפקיד חשוב במנגנון הגישה למאפיינים ומספקות אפשרות להתאמה אישית של הטיפול בהם.

*   **השיטה `__getattr__(self, name)`:**
    *   **נקראת בעת היעדר מאפיין:** השיטה נקראת רק אם לא נמצא מאפיין בשם `name` באמצעות מנגנון הגישה הסטנדרטי למאפיינים (`__getattribute__`).
    *   **טיפול במאפיינים שאינם קיימים:** מאפשרת להגדיר פעולות ברירת מחדל כאשר ניגשים לאובייקט עם מאפיין שאינו קיים.
    *    **ארגומנט אחד:** מקבלת את שם המאפיין המבוקש (בפורמט מחרוזת) ומחזירה ערך.
*   **השיטה `__getattribute__(self, name)`:**
    *   **שליטה על כל הגישות:** השיטה נקראת *בכל פעם* שמתבצעת גישה למאפיין של אובייקט, בין אם הוא קיים ובין אם אינו קיים.
    *   **מתבצעת תמיד:** נקראת גם במקרים שבהם המאפיין קיים ומהווה חלק מהאובייקט.
    *   **שליטה בלוגיקת הגישה:** מאפשרת לשלוט בלוגיקת הגישה לכל המאפיינים.
     *  **מחזירה ערך:** מקבלת את שם המאפיין המבוקש (בפורמט מחרוזת) ומחזירה ערך.

*   **ההבדל בין `__getattr__` ל-`__getattribute__`:**
    *   `__getattribute__` מתבצעת *תמיד* בעת גישה לכל מאפיין של אובייקט.
    *   `__getattr__` נקראת רק *לאחר* `__getattribute__`, אם `__getattribute__` לא הצליחה למצוא את המאפיין המבוקש.
     *  אם דרסתם (overrode) את `__getattribute__`, עליכם לקרוא במפורש לשיטת האב (parent method) אם ברצונכם שהמנגנון יפעל כרגיל.

**דוגמאות:**

```python
class Missing:
    attr = 42

    def __getattr__(self, name):
        # In __getattr__, asked for {name}
        print(f"In __getattr__, asked for {name}")
        return 73

m = Missing()
print(m.attr)  # Output: 42
print(m.xyz)  # Output: In __getattr__, asked for xyz; 73


class Always:
    attr = 42

    def __getattribute__(self, name):
        # In __getattribute__, asked for {name}
        print(f"In __getattribute__, asked for {name}")
        return 73

a = Always()
print(a.attr) # Output: In __getattribute__, asked for attr; 73
print(a.xyz) # Output: In __getattribute__, asked for xyz; 73

class MyClass:
    def __init__(self, name):
       self._name = name
    def __getattribute__(self, name):
        # if the attribute starts with _ then call the standard mechanism.
        if name.startswith("_"):
            return super().__getattribute__(name)
        # getting {name}
        print(f"getting {name}")
        # call the standard mechanism
        return super().__getattribute__(name)

    def __getattr__(self, name):
        # in __getattr__ getting {name}
        print(f"in __getattr__ getting {name}")
        return None
c = MyClass("John")
# Will output getting name\n None
print(c.name)
# Will output John
print(c._name)
```

**ניתוח האפשרויות:**

*   **א. השיטה `__getattr__` נקראת בניסיון לקבל כל מאפיין של אובייקט, בעוד שהשיטה `__getattribute__` נקראת רק בעת גישה לשיטות של אובייקט.:** לא נכון.
*    **ב. השיטה `__getattribute__` נקראת בניסיון לקבל כל מאפיין של אובייקט, בעוד שהשיטה `__getattr__` נקראת רק בעת גישה למאפיינים שאינם קיימים.:** נכון.
*  **ג. השיטה `__getattr__` משמשת לשינוי מאפיינים של אובייקט, בעוד ש-`__getattribute__` משמשת לקבלת מידע על אובייקט.:** לא נכון.
*   **ד. השיטות `__getattr__` ו-`__getattribute__` הן חלופיות זו לזו ומבצעות את אותה הפונקציה.:** לא נכון.

**לסיכום:**
*   `__getattribute__` היא שיטה כללית יותר לשליטה על גישה לכל המאפיינים.
*   `__getattr__` משמשת לטיפול במאפיינים שאינם קיימים.
*   `__getattribute__` נקראת תמיד (לפני `__getattr__`).

לפיכך, התשובה הנכונה היא **ב. השיטה `__getattribute__` נקראת בניסיון לקבל כל מאפיין של אובייקט, בעוד שהשיטה `__getattr__` נקראת רק בעת גישה למאפיינים שאינם קיימים.**