<BULLEYE>:
=================
קושי: 4
-----------------
המשחק "בול פגיעה" הוא משחק שבו השחקן מנסה לנחש קואורדינטות על מטרה. המטרה היא מעגל המחולק למספר אזורים, שכל אחד מהם מעניק לשחקן כמות שונה של נקודות. השחקן מזין קואורדינטות (x, y) ומקבל נקודות בהתאם לאזור המטרה שאליו הגיעה הפגיעה שלו. המשחק מסתיים כאשר השחקן צובר 100 נקודות או יותר.

חוקי המשחק:
1. המטרה היא עיגול ברדיוס 10.
2. מרכז המטרה נמצא בקואורדינטות (0, 0).
3. המטרה מחולקת לאזורים הבאים:
    - פגיעה במרכז (רדיוס 1): 10 נקודות.
    - פגיעה בעיגול הפנימי (רדיוס 5): 5 נקודות.
    - פגיעה בעיגול החיצוני (רדיוס 10): 2 נקודות.
    - החטאה (מחוץ לרדיוס 10): 0 נקודות.
4. השחקן מזין את קואורדינטות הפגיעה (x, y).
5. המשחק נמשך עד שהשחקן צובר 100 נקודות או יותר.
-----------------
אלגוריתם:
1. הגדרת ניקוד השחקן ל-0.
2. התחלת לולאה "כל עוד ניקוד השחקן קטן מ-100":
   2.1 בקשת קואורדינטות x ו-y מהשחקן.
   2.2 חישוב המרחק מהנקודה (x, y) למרכז (0, 0).
   2.3 בהתאם למרחק, צבירת נקודות:
        - אם המרחק <= 1, הוסף 10 נקודות.
        - אחרת אם המרחק <= 5, הוסף 5 נקודות.
        - אחרת אם המרחק <= 10, הוסף 2 נקודות.
        - אחרת הוסף 0 נקודות.
   2.4 הדפסת הניקוד הנוכחי של השחקן.
3. הדפסת ההודעה "YOU SCORED {ניקוד השחקן} POINTS.".
4. סוף המשחק.
-----------------
דיאגרמת זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeScore["<code><b>playerScore = 0</b></code>"]
    InitializeScore --> LoopStart{"התחלת לולאה: כל עוד <code><b>playerScore < 100</b></code>"}
    LoopStart -- Да --> InputCoordinates["הזנת קואורדינטות <code><b>x, y</b></code>"]
    InputCoordinates --> CalculateDistance["<code><b>distance = sqrt(x^2 + y^2)</b></code>"]
    CalculateDistance --> CheckCenter{"בדיקה: <code><b>distance <= 1?</b></code>"}
    CheckCenter -- Да --> Add10Points["<code><b>playerScore = playerScore + 10</b></code>"]
    Add10Points --> OutputScore["הצגת הניקוד הנוכחי <code><b>playerScore</b></code>"]
    OutputScore --> LoopStart
    CheckCenter -- Нет --> CheckInner{"בדיקה: <code><b>distance <= 5?</b></code>"}
    CheckInner -- Да --> Add5Points["<code><b>playerScore = playerScore + 5</b></code>"]
    Add5Points --> OutputScore
    OutputScore --> LoopStart
    CheckInner -- Нет --> CheckOuter{"בדיקה: <code><b>distance <= 10?</b></code>"}
    CheckOuter -- Да --> Add2Points["<code><b>playerScore = playerScore + 2</b></code>"]
    Add2Points --> OutputScore
    OutputScore --> LoopStart
    CheckOuter -- Нет --> Add0Points["<code><b>playerScore = playerScore + 0</b></code>"]
    Add0Points --> OutputScore
    OutputScore --> LoopStart
    LoopStart -- Нет --> OutputFinalScore["הצגת הודעה: <b>YOU SCORED <code>{playerScore}</code> POINTS.</b>"]
    OutputFinalScore --> End["סוף"]
```

Legenda:
    Start - התחלת המשחק.
    InitializeScore - אתחול המשתנה playerScore (ניקוד השחקן) ל-0.
    LoopStart - התחלת הלולאה, הנמשכת כל עוד ניקוד השחקן קטן מ-100.
    InputCoordinates - בקשת הזנת קואורדינטות x ו-y מהמשתמש.
    CalculateDistance - חישוב המרחק מהנקודה (x, y) למרכז (0, 0).
    CheckCenter - בדיקה האם המרחק נמצא בטווח האזור המרכזי (רדיוס 1).
    Add10Points - הוספת 10 נקודות לניקוד השחקן, אם הפגיעה היא במרכז.
    OutputScore - הצגת הניקוד הנוכחי של השחקן.
    CheckInner - בדיקה האם המרחק נמצא בטווח העיגול הפנימי (רדיוס 5).
    Add5Points - הוספת 5 נקודות לניקוד השחקן, אם הפגיעה היא בעיגול הפנימי.
    CheckOuter - בדיקה האם המרחק נמצא בטווח העיגול החיצוני (רדיוס 10).
    Add2Points - הוספת 2 נקודות לניקוד השחקן, אם הפגיעה היא בעיגול החיצוני.
    Add0Points - הוספת 0 נקודות לניקוד השחקן, אם זו החטאה.
    OutputFinalScore - הצגת הודעה אודות הניקוד הסופי של השחקן לאחר סיום המשחק.
    End - סיום המשחק.
```python
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

    # צבירת נקודות בהתאם לאזור הפגיעה
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
```
הסבר הקוד:
1.  **ייבוא המודול `math`**:
    -  `import math`: מייבא את המודול `math`, המשמש לפעולות מתמטיות, כגון חישוב שורש ריבועי.
2.  **אתחול ניקוד השחקן**:
    - `playerScore = 0`: מאתחל את המשתנה `playerScore`, המאחסן את ניקוד השחקן הנוכחי, החל מ-0.
3.  **לולאת המשחק הראשית `while playerScore < 100:`**:
    -   הלולאה מתבצעת כל עוד ניקוד השחקן קטן מ-100.
    -   **הזנת קואורדינטות**:
        -   `try...except ValueError:`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש מזין ערכים שאינם מספריים, מוצגת הודעת שגיאה.
        -   `x = float(input("הזן קואורדינטה x: "))`: מבקש מהמשתמש את קואורדינטה x וממיר אותה למספר עשרוני (עם נקודה צפה).
        -   `y = float(input("הזן קואורדינטה y: "))`: מבקש מהמשתמש את קואורדינטה y וממיר אותה למספר עשרוני.
    -   **חישוב מרחק**:
        -   `distance = math.sqrt(x**2 + y**2)`: מחשב את המרחק מהנקודה (x, y) למרכז (0, 0) לפי הנוסחה sqrt(x^2 + y^2).
    -   **צבירת נקודות**:
        -   `if distance <= 1:`: בודק האם הנקודה פגעה במרכז המטרה (רדיוס 1). אם כן, 10 נקודות מתווספות לניקוד.
        -   `elif distance <= 5:`: בודק האם הנקודה פגעה באזור הפנימי של המטרה (רדיוס 5). אם כן, 5 נקודות מתווספות לניקוד.
        -   `elif distance <= 10:`: בודק האם הנקודה פגעה באזור החיצוני של המטרה (רדיוס 10). אם כן, 2 נקודות מתווספות לניקוד.
        -   `else:`: אם הנקודה לא פגעה באף אחד מהאזורים, 0 נקודות מתווספות לניקוד.
    -   **הצגת הניקוד הנוכחי**:
         -   `print(f"ניקוד נוכחי: {playerScore}")`: מציג את ניקוד השחקן הנוכחי לאחר כל פגיעה.
4. **הצגת הניקוד הסופי**:
     -   `print(f"YOU SCORED {playerScore} POINTS.")`: מציג הודעה עם הניקוד הסופי, כאשר השחקן צובר 100 נקודות או יותר.