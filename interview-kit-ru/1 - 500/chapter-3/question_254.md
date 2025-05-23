### `question_254.md`

**שאלה 254.** בפייתון, מה ההבדל בין רשימה (`list`) לטיפל (`tuple`) מבחינת שינוּת (mutability) ושימושיהם האופייניים?

א. רשימה הינה בלתי ניתנת לשינוי (immutable), כלומר, לא ניתן לשנותה לאחר יצירתה, בעוד שטיפל הינו ניתן לשינוי (mutable) וניתן לשנותו בכל עת.
ב. רשימה הינה ניתנת לשינוי (mutable) ומאפשרת שינויים, בעוד שטיפל הינו בלתי ניתן לשינוי (immutable), כלומר, תוכנו אינו יכול להשתנות לאחר הגדרתו.
ג. גם רשימה וגם טיפל הינם בלתי ניתנים לשינוי (immutable) ואינם יכולים להשתנות לאחר יצירתם.
ד. גם רשימה וגם טיפל הינם ניתנים לשינוי (mutable), אך טיפל מספק גישה יעילה יותר לאלמנטים שלו.

**התשובה הנכונה: B**

**הסבר:**

בפייתון, רשימות (`list`) וטיפלים (`tuple`) הם שניהם סוגים של רצפים (sequences), אך הם נבדלים מבחינת שינוּתם (mutability).

*   **רשימה (`list`)**:
    *   הינה סוג נתונים *ניתן לשינוי* (mutable).
    *   לאחר יצירת רשימה, ניתן להוסיף, להסיר או לשנות אלמנטים ברשימה.
    *   מיוצגת בסוגריים מרובעים `[]`.
    *   משמשת בדרך כלל כאשר יש צורך לאחסן אוסף של אלמנטים שעשוי להשתנות במהלך ריצת התוכנית.

*   **טיפל (`tuple`)**:
    *   הינו סוג נתונים *בלתי ניתן לשינוי* (immutable).
    *   לאחר יצירת טיפל, *לא ניתן* לשנות את תוכנו. לא ניתן להוסיף, להסיר או לשנות אלמנטים.
    *   מיוצג בסוגריים עגולים `()`.
    *   משמש בדרך כלל כאשר יש צורך לאחסן אוסף של אלמנטים שאינם אמורים להשתנות לאחר יצירתם (לדוגמה, קואורדינטות, מפתחות במילון).

*   **אפשרות א' אינה נכונה:** להיפך, רשימה הינה ניתנת לשינוי, ואילו טיפל - לא.
*   **אפשרות ב' נכונה:** זהו התיאור הנכון של שינוּת הרשימה והטיפל.
*   **אפשרות ג' אינה נכונה:** רשימה הינה ניתנת לשינוי.
*   **אפשרות ד' אינה נכונה:** טיפלים אינם מספקים גישה יעילה יותר. ההבדל במהירות הגישה הוא בדרך כלל זניח.

**דוגמאות:**

```python
# רשימות (ניתנות לשינוי)
my_list = [1, 2, 3]
my_list.append(4)  # שינוי רשימה
my_list[0] = 0     # שינוי אלמנט
print(my_list) # פלט: [0, 2, 3, 4]

# טיפלים (בלתי ניתנים לשינוי)
my_tuple = (1, 2, 3)
# my_tuple.append(4) # שגיאה: לטיפלים אין מתודה append
# my_tuple[0] = 0 # שגיאה: טיפלים בלתי ניתנים לשינוי
print(my_tuple) # פלט: (1, 2, 3)
```

**לסיכום:**

רשימות הינן ניתנות לשינוי, ותוכנן ניתן למודִיפִיקַצְיָה (שינוי). טיפלים הינם בלתי ניתנים לשינוי, ואת תוכנם לא ניתן לשנות לאחר יצירתם. הבחירה בין רשימה לטיפל תלויה בשאלה האם יש צורך לשנות את הנתונים לאחר יצירתם.

לפיכך, אפשרות ב' הינה נכונה.

---

מוכן לשאלה הבאה!