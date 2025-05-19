FIPFOP:
=================
**מורכבות:** 5
-----------------
המשחק FIPFOP הוא משחק חידה שבו השחקן נדרש להזין מספרים בזה אחר זה.
מטרת המשחק היא להגיע למצב שבו כל המספרים שהוזנו על ידי המשתמש מסתכמים ב-100.
המשחק מסתיים כאשר סכום כל המספרים שהוזנו מגיע ל-100.

**כללי המשחק:**
1. השחקן מזין מספרים שלמים, אחד בכל פעם.
2. כל מספר שהוזן מתווסף לסכום הכולל.
3. המשחק מסתיים כאשר הסכום הכולל מגיע ל-100.
4. לאחר סיום המשחק, מוצג המספר הכולל של המספרים שהוזנו (מהלכים).
-----------------
**אלגוריתם:**
1. אתחל את הסכום ל-0.
2. אתחל את מונה המהלכים ל-0.
3. התחל לולאה "כל עוד הסכום קטן מ-100":
    3.1 בקש מהשחקן להזין מספר.
    3.2 הגדל את מונה המהלכים ב-1.
    3.3 הוסף את המספר שהוזן לסכום הכולל.
4. הצג את ההודעה "השתמשת ב-{מספר המהלכים} מהלכים".
5. סוף המשחק.
-----------------
**בלוק-סכמה:**
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    totalSum = 0
    numberOfTurns = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד totalSum < 100"}
    LoopStart -- כן --> InputNumber["קלט מספר מהמשתמש: <code><b>userNumber</b></code>"]
    InputNumber --> IncreaseTurns["<code><b>numberOfTurns = numberOfTurns + 1</b></code>"]
     IncreaseTurns --> AddNumber["<code><b>totalSum = totalSum + userNumber</b></code>"]
    AddNumber --> CheckSum{"בדיקה: <code><b>totalSum >= 100?</b></code>"}
    CheckSum -- כן --> OutputTurns["פלט הודעה: <b>YOU USED <code>{numberOfTurns}</code> TURNS</b>"]
    OutputTurns --> End["סיום"]
     CheckSum -- לא --> LoopStart
    LoopStart -- לא --> End
```

**מקרא:**
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: totalSum (סכום המספרים שהוזנו) מאותחל ל-0, ו-numberOfTurns (מספר המהלכים) מאותחל ל-0.
    LoopStart - תחילת הלולאה, הנמשכת כל עוד totalSum קטן מ-100.
    InputNumber - בקשה מהמשתמש להזין מספר ושמירתו במשתנה userNumber.
    IncreaseTurns - הגדלת מונה מספר המהלכים ב-1.
    AddNumber - הוספת המספר המוזן userNumber לסכום הכולל totalSum.
    CheckSum - בדיקה האם הסכום הכולל totalSum גדול או שווה ל-100.
    OutputTurns - פלט הודעה אודות מספר המהלכים ששימשו את המשתמש.
    End - סיום התוכנית.
"""


```python
# אתחול סכום ומונה מהלכים
totalSum = 0 # סכום המספרים שהוזנו
numberOfTurns = 0 # מספר המהלכים

# לולאת המשחק הראשית
while totalSum < 100:
    # מבקשים קלט מספר מהמשתמש
    try:
        userNumber = int(input("הזן מספר: "))
    except ValueError:
         print("אנא הזן מספר שלם.")
         continue
    
    # מגדילים את מונה המהלכים
    numberOfTurns += 1
    # מוסיפים את המספר שהוזן לסכום הכולל
    totalSum += userNumber

# מדפיסים הודעה על מספר המהלכים
print(f"השתמשת ב-{numberOfTurns} מהלכים")


"""
הסבר על הקוד:
1. **אתחול משתנים:**
   - `totalSum = 0`: מאתחל את המשתנה totalSum לאחסון סכום המספרים שהוזנו; מתחילים מ-0.
   - `numberOfTurns = 0`: מאתחל את המשתנה numberOfTurns לספירת מספר המהלכים; גם כן מתחילים מ-0.
2. **הלולאה הראשית `while totalSum < 100`:**
   -  הלולאה נמשכת כל עוד סכום המספרים שהוזנו (totalSum) קטן מ-100.
3. **קלט מהמשתמש:**
    - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך שאינו מספר שלם, תוצג הודעת שגיאה.
   - `userNumber = int(input("הזן מספר: "))`: מבקש מהמשתמש להזין מספר וממיר אותו למספר שלם, שומר את התוצאה במשתנה userNumber.
4. **הגדלת מונה המהלכים:**
   - `numberOfTurns += 1`: מגדיל את מונה המהלכים ב-1 בכל איטרציה של הלולאה.
5.  **הוספת המספר לסכום:**
   -  `totalSum += userNumber`: מוסיף את המספר שהוזן (userNumber) לסכום הכולל (totalSum).
6.  **פלט התוצאה:**
    - `print(f"השתמשת ב-{numberOfTurns} מהלכים")`: מדפיס למסך הודעה על מספר המהלכים שבוצעו כאשר סכום המספרים הגיע ל-100 או יותר.
"""
```