### `question_587.md`

**שאלה 587.** מה ההבדל העיקרי בין רשימות (`list`) לטופלים (`tuple`) בפייתון?

*   א. רשימות וטופלים הן מבני נתונים זהים לחלוטין, וניתן להשתמש בהם באופן חליפי.
*   ב. ניתן לשנות רשימות לאחר יצירתן (הן ניתנות לשינוי), בעוד שטופלים אינם ניתנים לשינוי לאחר יצירתם (הם בלתי ניתנים לשינוי). רשימות מיועדות לרצפים מסודרים של איברים מאותו סוג, בעוד שטופלים יכולים להכיל נתונים מסוגים שונים בעלי מבנה קבוע.
*   ג. טופלים תומכים בסוגי נתונים מספריים בלבד, בעוד שרשימות תומכות בכל סוג נתונים.
*   ד. רשימות מאחסנות נתונים בסדר יורד, וטופלים בסדר עולה.

**תשובה נכונה: B**

**הסבר:**

רשימות (`list`) וטופלים (`tuple`) הם שני סוגי רצפים בסיסיים בפייתון, אך יש להם הבדלים מהותיים מבחינת יכולת השינוי והשימוש המיועד.

*   **רשימות (`list`):**
    *   **ניתנות לשינוי (mutable):** לאחר יצירת רשימה, ניתן לשנות אותה (להוסיף, למחוק, לשנות איברים).
    *   **רצפים מסודרים:** מייצגות רצפים מסודרים של אובייקטים, שבדרך כלל הם מאותו סוג נתונים, למשל רשימת שמות משתמשים: `["Seth", "Ema", "Eli"]`
    *   **תחביר:** מוגדרות באמצעות סוגריים מרובעים `[]`.

*   **טופלים (`tuple`):**
    *   **בלתי ניתנים לשינוי (immutable):** לאחר יצירת טופל, לא ניתן לשנות אותו (לא ניתן להוסיף, למחוק או לשנות איברים).
    *   **מבנה:** לטופלים יש בדרך כלל מבנה קבוע והם יכולים להכיל איברים מסוגים שונים. לדוגמה, רשומה על משתמש: `(2, "Ema", "2020-04-16")`
    *   **תחביר:** מוגדרים באמצעות סוגריים עגולים `()`.

**הבדלים:**
*   **יכולת שינוי:** רשימות ניתנות לשינוי, טופלים בלתי ניתנים לשינוי.
*   **מבנה:** רשימות הן רצפים הומוגניים, טופלים הם נתונים מובנים (structured data).
*   **יישום:** רשימות משמשות לאחסון רצפים משתנים, טופלים, כרשומות, שניתן לראותן כנתונים בלתי ניתנים לשינוי.

**דוגמאות:**

```python
# דוגמה לרשימה
my_list = [1, 2, 3]
my_list[0] = 10 # משנים איבר ברשימה
my_list.append(4) # מוסיפים איבר לסוף
print(my_list) # ידפיס [10, 2, 3, 4]

# דוגמה לטופל
my_tuple = (1, "hello", 3.14)
# my_tuple[0] = 10 # יגרום לשגיאת TypeError
try:
   my_tuple = my_tuple + (5,)
   print(my_tuple) # ידפיס: (1, 'hello', 3.14, 5)
except TypeError as e:
    print(f"Error: {e}")

# דוגמה לרשימה
user_list = ["John", "Mary", "Alice"]

# דוגמה לטופל
user_tuple = (1, "John", "2020-04-16")
```

**ניתוח האפשרויות:**
*   **א. רשימות וטופלים הן מבני נתונים זהים לחלוטין, וניתן להשתמש בהם באופן חליפי.:** שגוי.
*   **ב. ניתן לשנות רשימות לאחר יצירתן (הן ניתנות לשינוי), בעוד שטופלים אינם ניתנים לשינוי לאחר יצירתם (הם בלתי ניתנים לשינוי). רשימות מיועדות לרצפים מסודרים של איברים מאותו סוג, בעוד שטופלים יכולים להכיל נתונים מסוגים שונים בעלי מבנה קבוע.:** נכון.
*   **ג. טופלים תומכים בסוגי נתונים מספריים בלבד, בעוד שרשימות תומכות בכל סוג נתונים.:** שגוי.
*   **ד. רשימות מאחסנות נתונים בסדר יורד, וטופלים בסדר עולה.:** שגוי.

**לסיכום:**
*   לרשימות ולטופלים ייעוד שונה בפייתון.
*   רשימות מיועדות לאחסון רצפים הניתנים לשינוי.
*   טופלים מיועדים לאחסון נתונים מובנים ובלתי ניתנים לשינוי.

לפיכך, התשובה הנכונה היא **ב. ניתן לשנות רשימות לאחר יצירתן (הן ניתנות לשינוי), בעוד שטופלים אינם ניתנים לשינוי לאחר יצירתם (הם בלתי ניתנים לשינוי). רשימות מיועדות לרצפים מסודרים של איברים מאותו סוג, בעוד שטופלים יכולים להכיל נתונים מסוגים שונים בעלי מבנה קבוע.**