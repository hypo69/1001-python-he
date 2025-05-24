GOLF:
=================
רמת קושי: 3
-----------------
המשחק "גולף" הוא משחק טקסטואלי בו השחקן מנסה להגיע לגומה במספר המכות הנמוך ביותר האפשרי. השחקן מזין את המרחק הרצוי לגומה, והתוכנית מחשבת את תוצאת המכה על בסיס המרחק וגורם אקראי. מטרת המשחק היא לעבור את הגומה על ידי ביצוע מכות למרחקים שונים, ולסיים את המשחק עם מינימום מכות.

כללי המשחק:
1. השחקן מתחיל את המשחק עם אפס מכות.
2. השחקן מזין את המרחק אליו הוא רוצה לחבוט בכדור.
3. התוכנית מייצרת סטייה אקראית מהמרחק שהוזן, המדמה חוסר דיוק במכה.
4. התוכנית מודיעה לשחקן על המרחק בפועל אליו בוצעה המכה.
5. התוכנית מחשבת את המרחק שנותר לגומה.
6. המשחק נמשך עד שהמרחק לגומה שווה לאפס.
7. לאחר ההגעה לגומה, המשחק מסתיים, והתוכנית מודיעה על מספר המכות שנדרשו כדי להגיע למטרה.
-----------------
אלגוריתם:
1. הגדרת מספר המכות ל-0.
2. הגדרת המרחק לגומה ל-250 יארד.
3. התחלת לולאה כל עוד המרחק לגומה אינו שווה ל-0:
    3.1 בקשת קלט מהשחקן עבור מרחק המכה.
    3.2 יצירת מספר אקראי בטווח שבין -10 ל-10 (שגיאת המכה).
    3.3 הגדלת מספר המכות ב-1.
    3.4 חישוב מרחק המכה בפועל, על ידי הוספת השגיאה למרחק שהוזן.
    3.5 עדכון המרחק לגומה, על ידי חיסור מרחק המכה בפועל.
    3.6 הצגת הודעה המציינת את מרחק המכה בפועל ואת המרחק שנותר לגומה.
4. הצגת ההודעה "הידד! הגעת לגומה ב-{numberOfHits} מכות.".
5. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfHits = 0
    distanceToHole = 250
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד <code><b>distanceToHole > 0</b></code>"}
    LoopStart -- כן --> InputDistance["הזנת מרחק מכה: <code><b>userDistance</b></code>"]
    InputDistance --> GenerateError["יצירת שגיאה אקראית: <code><b>error = random(-10, 10)</b></code>"]
    GenerateError --> IncreaseHits["<code><b>numberOfHits = numberOfHits + 1</b></code>"]
    IncreaseHits --> CalculateActualDistance["חישוב מרחק בפועל: <code><b>actualDistance = userDistance + error</b></code>"]
    CalculateActualDistance --> UpdateDistanceToHole["עדכון מרחק לגומה: <code><b>distanceToHole = distanceToHole - actualDistance</b></code>"]
    UpdateDistanceToHole --> OutputDistance["הצגת הודעה: <code><b>actualDistance, distanceToHole</b></code>"]
    OutputDistance --> CheckHole{"בדיקה: <code><b>distanceToHole <= 0?</b></code>"}
     CheckHole -- כן --> OutputWin["הצגת הודעה: <b>הידד! הגעת לגומה ב-<code>{numberOfHits}</code> מכות.</b>"]
    OutputWin --> End["סיום"]
    CheckHole -- לא --> LoopStart
    LoopStart -- לא --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfHits (מספר המכות) מוגדר ל-0, ו-distanceToHole (מרחק לגומה) מוגדר ל-250.
    LoopStart - תחילת הלולאה, הנמשכת כל עוד distanceToHole גדול מ-0.
    InputDistance - בקשת קלט מהמשתמש עבור מרחק המכה ושמירתו במשתנה userDistance.
    GenerateError - יצירת מספר שלם אקראי בטווח שבין -10 ל-10 (שגיאת המכה) ושמירתו במשתנה error.
    IncreaseHits - הגדלת מונה מספר המכות ב-1.
    CalculateActualDistance - חישוב מרחק המכה בפועל על ידי חיבור המרחק שהוזן והשגיאה ושמירתו במשתנה actualDistance.
    UpdateDistanceToHole - עדכון המרחק לגומה על ידי חיסור מרחק המכה בפועל ושמירת התוצאה ב-distanceToHole.
    OutputDistance - הצגת הודעה המציינת את מרחק המכה בפועל ואת המרחק שנותר לגומה.
     CheckHole - בדיקה האם הגענו לגומה (distanceToHole <= 0).
     OutputWin - הצגת הודעה על ניצחון עם מספר המכות.
    End - סיום התוכנית.
```python
import random

# מאתחלים את מספר המכות
numberOfHits = 0
# מגדירים את המרחק ההתחלתי לגומה ל-250 יארד
distanceToHole = 250

# מתחילים את לולאת המשחק הראשית
while distanceToHole > 0:
    # מבקשים מהמשתמש את מרחק המכה
    try:
        userDistance = float(input("הזן מרחק מכה: "))
    except ValueError:
        print("אנא הזן מספר.")
        continue
    # מייצרים שגיאת מכה אקראית בטווח שבין -10 ל-10
    error = random.randint(-10, 10)
    # מגדילים את מונה המכות ב-1
    numberOfHits += 1
    # מחשבים את מרחק המכה בפועל, תוך התחשבות בשגיאה
    actualDistance = userDistance + error
    # מעדכנים את המרחק לגומה
    distanceToHole -= actualDistance

    # מציגים מידע על המכה הנוכחית והמרחק שנותר
    print(f"מרחק המכה בפועל: {actualDistance:.2f} יארד")
    print(f"מרחק לגומה: {distanceToHole:.2f} יארד")

# לאחר היציאה מהלולאה, מציגים הודעת ניצחון
print(f"הידד! הגעת לגומה ב-{numberOfHits} מכות.")
```

הסבר הקוד:
1. **ייבוא מודול random**:
   - `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים.
2. **אתחול משתנים**:
   - `numberOfHits = 0`: מאתחל את המשתנה `numberOfHits` לספירת מספר המכות.
   - `distanceToHole = 250`: מגדיר את המרחק ההתחלתי לגומה ל-250 יארד.
3. **לולאת המשחק הראשית `while distanceToHole > 0:`**:
   - לולאה זו נמשכת כל עוד המרחק לגומה `distanceToHole` גדול מ-0.
    -  **קלט נתונים**:
        -   `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך שאינו מספר, תוצג הודעת שגיאה.
        -   `userDistance = float(input("הזן מרחק מכה: "))`: מבקש מהמשתמש את מרחק המכה וממיר אותו למספר עשרוני (float).
    - `error = random.randint(-10, 10)`: מייצר מספר שלם אקראי מ-10- עד 10, המייצג את השגיאה במכה.
    - `numberOfHits += 1`: מגדיל את מונה המכות ב-1.
    - `actualDistance = userDistance + error`: מחשב את מרחק המכה בפועל, על ידי הוספת השגיאה למרחק שהוזן על ידי המשתמש.
    - `distanceToHole -= actualDistance`: מעדכן את המרחק לגומה, על ידי חיסור מרחק המכה בפועל ממנו.
    - `print(f"מרחק המכה בפועל: {actualDistance:.2f} יארד")`: מציג את מרחק המכה בפועל בדיוק של שתי ספרות אחרי הנקודה העשרונית.
    - `print(f"מרחק לגומה: {distanceToHole:.2f} יארד")`: מציג את המרחק שנותר לגומה בדיוק של שתי ספרות אחרי הנקודה העשרונית.
4. **הצגת הודעת ניצחון**:
   - `print(f"הידד! הגעת לגומה ב-{numberOfHits} מכות.")`: מציג הודעת ניצחון המציינת את מספר המכות שנדרשו כדי להגיע לגומה.