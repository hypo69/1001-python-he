GOLF:
=================
רמת קושי: 3
-----------------
המשחק "גולף" הוא משחק טקסטואלי שבו השחקן מנסה להגיע לגומחה במספר החבטות הנמוך ביותר. השחקן מזין את המרחק לגומחה, והתוכנית מחשבת את תוצאת החבטה על סמך המרחק וגורם אקראי. מטרת המשחק היא להשלים את הגומחה על ידי ביצוע חבטות במרחקים שונים, ולסיים את המשחק עם מספר מינימלי של חבטות.

כללי המשחק:
1. השחקן מתחיל את המשחק עם אפס חבטות.
2. השחקן מזין את המרחק אליו הוא רוצה לחבוט בכדור.
3. התוכנית מייצרת הטיה אקראית מהמרחק המוגדר, המדמה אי-דיוק בחבטה.
4. התוכנית מודיעה לשחקן את המרחק בפועל אליו בוצעה החבטה.
5. התוכנית מחשבת את המרחק לגומחה.
6. המשחק נמשך עד אשר המרחק לגומחה יהיה שווה לאפס.
7. לאחר הגעה לגומחה, המשחק מסתיים והתוכנית מודיעה על מספר החבטות שנדרשו להשגת המטרה.
-----------------
אלגוריתם:
1. הגדרת מספר החבטות ל-0.
2. הגדרת המרחק לגומחה ל-250 יארדים.
3. התחלת לולאה, כל עוד המרחק לגומחה אינו שווה ל-0:
    3.1 בקשת קלט מהשחקן עבור מרחק החבטה.
    3.2 ייצור מספר אקראי בטווח של -10 עד 10 (שגיאת חבטה).
    3.3 הגדלת מספר החבטות ב-1.
    3.4 חישוב המרחק בפועל של החבטה, על ידי הוספת השגיאה למרחק המוזן.
    3.5 עדכון המרחק לגומחה, על ידי חיסור מרחק החבטה בפועל.
    3.6 הצגת הודעה המציינת את מרחק החבטה בפועל ואת המרחק הנותר לגומחה.
4. הצגת הודעה "הידד! הגעת לגומחה ב-{מספר החבטות} חבטות."
5. סוף המשחק.
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
    LoopStart -- כן --> InputDistance["קלט מרחק חבטה: <code><b>userDistance</b></code>"]
    InputDistance --> GenerateError["ייצור שגיאה אקראית: <code><b>error = random(-10, 10)</b></code>"]
    GenerateError --> IncreaseHits["<code><b>numberOfHits = numberOfHits + 1</b></code>"]
    IncreaseHits --> CalculateActualDistance["חישוב מרחק בפועל: <code><b>actualDistance = userDistance + error</b></code>"]
    CalculateActualDistance --> UpdateDistanceToHole["עדכון מרחק לגומחה: <code><b>distanceToHole = distanceToHole - actualDistance</b></code>"]
    UpdateDistanceToHole --> OutputDistance["הצגת הודעה: <code><b>actualDistance, distanceToHole</b></code>"]
    OutputDistance --> CheckHole{"בדיקה: <code><b>distanceToHole <= 0?</b></code>"}
     CheckHole -- כן --> OutputWin["הצגת הודעה: <b>הידד! הגעת לגומחה ב-<code>{numberOfHits}</code> חבטות.</b>"]
    OutputWin --> End["סוף"]
    CheckHole -- לא --> LoopStart
    LoopStart -- לא --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfHits (מספר חבטות) מוגדר ל-0, ו-distanceToHole (מרחק לגומחה) מוגדר ל-250.
    LoopStart - התחלת לולאה, הנמשכת כל עוד distanceToHole גדול מ-0.
    InputDistance - בקשת קלט מהמשתמש עבור מרחק החבטה ושמירתו במשתנה userDistance.
    GenerateError - ייצור מספר שלם אקראי בטווח של -10 עד 10 (שגיאת חבטה) ושמירתו במשתנה error.
    IncreaseHits - הגדלת מונה מספר החבטות ב-1.
    CalculateActualDistance - חישוב מרחק החבטה בפועל על ידי חיבור המרחק המוזן והשגיאה ושמירה במשתנה actualDistance.
    UpdateDistanceToHole - עדכון המרחק לגומחה על ידי חיסור מרחק החבטה בפועל ושמירת התוצאה ב-distanceToHole.
    OutputDistance - הצגת הודעה המציינת את מרחק החבטה בפועל ואת המרחק הנותר לגומחה.
     CheckHole - בדיקה האם הגענו לגומחה (distanceToHole <= 0).
     OutputWin - הצגת הודעה על ניצחון עם מספר החבטות.
    End - סוף התוכנית.
```
import random

# מאתחל את מספר החבטות
numberOfHits = 0
# מגדיר את המרחק ההתחלתי לגומחה ל-250 יארדים
distanceToHole = 250

# מתחיל את לולאת המשחק הראשית
while distanceToHole > 0:
    # מבקש מהמשתמש את מרחק החבטה
    try:
        userDistance = float(input("הזן מרחק חבטה: "))
    except ValueError:
        print("אנא הזן מספר.")
        continue
    # מייצר שגיאת חבטה אקראית בטווח של -10 עד 10
    error = random.randint(-10, 10)
    # מגדיל את מספר החבטות ב-1
    numberOfHits += 1
    # מחשב את מרחק החבטה בפועל, תוך התחשבות בשגיאה
    actualDistance = userDistance + error
    # מעדכן את המרחק לגומחה
    distanceToHole -= actualDistance

    # מציג מידע על החבטה הנוכחית והמרחק הנותר
    print(f"מרחק חבטה בפועל: {actualDistance:.2f} יארדים")
    print(f"מרחק לגומחה: {distanceToHole:.2f} יארדים")

# לאחר היציאה מהלולאה מציג הודעת ניצחון
print(f"הידד! הגעת לגומחה ב-{numberOfHits} חבטות.")

```
הסבר הקוד:
1. **ייבוא מודול random**:
   - `import random`: מייבא את המודול `random`, המשמש לייצור מספרים אקראיים.
2. **אתחול משתנים**:
   - `numberOfHits = 0`: מאתחל את המשתנה `numberOfHits` לצורך ספירת החבטות.
   - `distanceToHole = 250`: מגדיר את המרחק ההתחלתי לגומחה ל-250 יארדים.
3. **לולאת המשחק הראשית `while distanceToHole > 0:`**:
   - לולאה זו נמשכת כל עוד המרחק לגומחה `distanceToHole` אינו קטן או שווה ל-0.
    -  **קלט נתונים**:
        -   `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך שאינו מספר, תוצג הודעת שגיאה.
        -   `userDistance = float(input("הזן מרחק חבטה: "))`: מבקש מהמשתמש את מרחק החבטה וממיר אותו למספר נקודה צפה.
    - `error = random.randint(-10, 10)`: מייצר מספר שלם אקראי בין -10 ל-10, המייצג את השגיאה בחבטה.
    - `numberOfHits += 1`: מגדיל את מונה מספר החבטות ב-1.
    - `actualDistance = userDistance + error`: מחשב את מרחק החבטה בפועל, על ידי הוספת השגיאה למרחק שהוזן על ידי המשתמש.
    - `distanceToHole -= actualDistance`: מעדכן את המרחק לגומחה, על ידי חיסור מרחק החבטה בפועל ממנו.
    - `print(f"מרחק חבטה בפועל: {actualDistance:.2f} יארדים")`: מציג את מרחק החבטה בפועל בדיוק של שתי ספרות אחרי הנקודה העשרונית.
    - `print(f"מרחק לגומחה: {distanceToHole:.2f} יארדים")`: מציג את המרחק הנותר לגומחה בדיוק של שתי ספרות אחרי הנקודה העשרונית.
4. **הצגת הודעת ניצחון**:
   - `print(f"הידד! הגעת לגומחה ב-{numberOfHits} חבטות.")`: מציג הודעת ניצחון המציינת את מספר החבטות שנדרשו להשגת הגומחה.