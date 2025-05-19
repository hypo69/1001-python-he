<BULLEYE>:
=================
רמת מורכבות: 4
-----------------
המשחק "בול עין" (Bullseye) הוא משחק שבו שחקן מנסה לנחש קואורדינטות על לוח מטרה. לוח המטרה הוא מעגל המחולק למספר אזורים, כשכל אזור מקנה לשחקן כמות שונה של נקודות. השחקן מזין קואורדינטות (x, y) ומקבל נקודות בהתאם לאזור בלוח המטרה אליו הגיעה היריה. המשחק מסתיים כאשר השחקן צובר 100 נקודות או יותר.

כללי המשחק:
1.  לוח המטרה הוא מעגל עם רדיוס 10.
2.  מרכז לוח המטרה נמצא בקואורדינטות (0, 0).
3.  לוח המטרה מחולק לאזורים הבאים:
    -   פגיעה במרכז (רדיוס 1): 10 נקודות.
    -   פגיעה במעגל הפנימי (רדיוס 5): 5 נקודות.
    -   פגיעה במעגל החיצוני (רדיוס 10): 2 נקודות.
    -   החטאה (מחוץ לרדיוס 10): 0 נקודות.
4.  השחקן מזין את קואורדינטות היריה (x, y).
5.  המשחק נמשך עד שהשחקן צובר 100 נקודות או יותר.
-----------------
אלגוריתם:
1.  איתחול ניקוד השחקן ל-0.
2.  התחלת לולאה "כל עוד ניקוד השחקן נמוך מ-100":
    2.1 בקשת קלט מהשחקן עבור קואורדינטות x ו-y.
    2.2 חישוב המרחק מהנקודה (x, y) למרכז (0, 0).
    2.3 בהתאם למרחק, הענקת נקודות:
        -   אם המרחק <= 1, הוספת 10 נקודות.
        -   אחרת אם המרחק <= 5, הוספת 5 נקודות.
        -   אחרת אם המרחק <= 10, הוספת 2 נקודות.
        -   אחרת, הוספת 0 נקודות.
    2.4 הצגת הניקוד הנוכחי של השחקן.
3.  הצגת ההודעה "YOU SCORED {ניקוד השחקן} POINTS.".
4.  סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeScore["<code><b>playerScore = 0</b></code>"]
    InitializeScore --> LoopStart{"תחילת לולאה: כל עוד <code><b>playerScore < 100</b></code>"}
    LoopStart -- כן --> InputCoordinates["קלט קואורדינטות <code><b>x, y</b></code>"]
    InputCoordinates --> CalculateDistance["<code><b>distance = sqrt(x^2 + y^2)</b></code>"]
    CalculateDistance --> CheckCenter{"בדיקה: <code><b>distance <= 1?</b></code>"}
    CheckCenter -- כן --> Add10Points["<code><b>playerScore = playerScore + 10</b></code>"]
    Add10Points --> OutputScore["פלט ניקוד נוכחי <code><b>playerScore</b></code>"]
    OutputScore --> LoopStart
    CheckCenter -- לא --> CheckInner{"בדיקה: <code><b>distance <= 5?</b></code>"}
    CheckInner -- כן --> Add5Points["<code><b>playerScore = playerScore + 5</b></code>"]
    Add5Points --> OutputScore
    OutputScore --> LoopStart
    CheckInner -- לא --> CheckOuter{"בדיקה: <code><b>distance <= 10?</b></code>"}
    CheckOuter -- כן --> Add2Points["<code><b>playerScore = playerScore + 2</b></code>"]
    Add2Points --> OutputScore
    OutputScore --> LoopStart
    CheckOuter -- לא --> Add0Points["<code><b>playerScore = playerScore + 0</b></code>"]
    Add0Points --> OutputScore
    OutputScore --> LoopStart
    LoopStart -- לא --> OutputFinalScore["פלט הודעה: <b>YOU SCORED <code>{playerScore}</code> POINTS.</b>"]
    OutputFinalScore --> End["סיום"]
```

מקרא:
    Start - התחלת המשחק.
    InitializeScore - איתחול המשתנה playerScore (ניקוד השחקן) ל-0.
    LoopStart - תחילת הלולאה הנמשכת כל עוד ניקוד השחקן נמוך מ-100.
    InputCoordinates - בקשת קלט מהמשתמש עבור קואורדינטות x ו-y.
    CalculateDistance - חישוב המרחק מהנקודה (x, y) למרכז (0, 0).
    CheckCenter - בדיקה האם המרחק נמצא בטווח אזור המרכז (רדיוס 1).
    Add10Points - הוספת 10 נקודות לניקוד השחקן אם הפגיעה במרכז.
    OutputScore - הצגת הניקוד הנוכחי של השחקן.
    CheckInner - בדיקה האם המרחק נמצא בטווח המעגל הפנימי (רדיוס 5).
    Add5Points - הוספת 5 נקודות לניקוד השחקן אם הפגיעה במעגל הפנימי.
    CheckOuter - בדיקה האם המרחק נמצא בטווח המעגל החיצוני (רדיוס 10).
    Add2Points - הוספת 2 נקודות לניקוד השחקן אם הפגיעה במעגל החיצוני.
    Add0Points - הוספת 0 נקודות לניקוד השחקן אם מדובר בהחטאה.
    OutputFinalScore - הצגת הודעה על ניקוד השחקן הסופי לאחר סיום המשחק.
    End - סיום המשחק.
```
import math

# אתחול ניקוד השחקן
playerScore = 0

# לולאת המשחק הראשית
while playerScore < 100:
    try:
        # בקשת קואורדינטות מהמשתמש
        x = float(input("הזן קואורדינטה x: "))
        y = float(input("הזן קואורדינטה y: "))
    except ValueError:
        print("אנא הזן ערכים מספריים עבור הקואורדינטות.")
        continue

    # חישוב המרחק מהנקודה (x, y) למרכז (0, 0)
    distance = math.sqrt(x**2 + y**2)

    # הענקת נקודות בהתאם לאזור הפגיעה
    if distance <= 1:
        playerScore += 10
    elif distance <= 5:
        playerScore += 5
    elif distance <= 10:
        playerScore += 2
    else:
        playerScore += 0

    # הצגת הניקוד הנוכחי
    print(f"ניקוד נוכחי: {playerScore}")

# הצגת הודעה על סיום המשחק
print(f"YOU SCORED {playerScore} POINTS.")
```
"""
הסבר על הקוד:
1.  **ייבוא מודול `math`**:
    -   `import math`: מייבא את מודול `math`, המשמש לפעולות מתמטיות כגון חישוב שורש ריבועי.
2.  **איתחול ניקוד השחקן**:
    -   `playerScore = 0`: מאתחל את המשתנה `playerScore`, המאחסן את ניקוד השחקן הנוכחי, החל מ-0.
3.  **לולאת המשחק הראשית `while playerScore < 100:`**:
    -   הלולאה מבוצעת כל עוד ניקוד השחקן נמוך מ-100.
    -   **קלט קואורדינטות**:
        -   `try...except ValueError:`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערכים שאינם מספרים, תוצג הודעת שגיאה.
        -   `x = float(input("הזן קואורדינטה x: "))`: מבקש מהמשתמש את קואורדינטה x וממיר אותה למספר נקודה צפה.
        -   `y = float(input("הזן קואורדינטה y: "))`: מבקש מהמשתמש את קואורדינטה y וממיר אותה למספר נקודה צפה.
    -   **חישוב מרחק**:
        -   `distance = math.sqrt(x**2 + y**2)`: מחשב את המרחק מהנקודה (x, y) למרכז (0, 0) באמצעות הנוסחה sqrt(x^2 + y^2).
    -   **הענקת נקודות**:
        -   `if distance <= 1:`: בודק אם הנקודה נפלה במרכז לוח המטרה (רדיוס 1). אם כן, מוספות 10 נקודות לניקוד.
        -   `elif distance <= 5:`: בודק אם הנקודה נפלה באזור הפנימי של לוח המטרה (רדיוס 5). אם כן, מוספות 5 נקודות לניקוד.
        -   `elif distance <= 10:`: בודק אם הנקודה נפלה באזור החיצוני של לוח המטרה (רדיוס 10). אם כן, מוספות 2 נקודות לניקוד.
        -   `else:`: אם הנקודה לא נפלה באף אחד מהאזורים, מוספות 0 נקודות לניקוד.
    -   **הצגת הניקוד הנוכחי**:
        -   `print(f"ניקוד נוכחי: {playerScore}")`: מציג את ניקוד השחקן הנוכחי לאחר כל יריה.
4. **הצגת הניקוד הסופי**:
    -   `print(f"YOU SCORED {playerScore} POINTS.")`: מציג הודעה עם הניקוד הסופי כאשר השחקן מגיע ל-100 נקודות או יותר.
"""