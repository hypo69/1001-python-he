רכבת:
=================
מורכבות: 4
-----------------
המשחק "רכבת" הוא משחק סימולציה שבו השחקן שולט ברכבת, מאיץ ומאט, בניסיון להגיע למהירות מסוימת במרחק מסוים.
השחקן מזין ערכים עבור תאוצה ותאוטה, והמשחק מציג את המהירות הנוכחית ואת המרחק שעברה הרכבת.
המטרה היא להגיע למהירות יעד במרחק יעד.
המשחק מציג את המרחק שעבר ואת המהירות הנוכחית, ומסתיים כאשר מרחק היעד מושג.

כללי המשחק:
1. המשחק מתחיל במהירות אפס ובמרחק שעבר אפס.
2. השחקן מזין את גודל התאוצה.
3. השחקן מזין את גודל התאוטה.
4. המשחק מחשב את המהירות החדשה ואת המרחק שעבר, תוך שימוש בערכי התאוצה והתאוטה שהוזנו.
5. המשחק מציג את המהירות הנוכחית ואת המרחק שעבר.
6. המשחק נמשך עד שהמרחק שעבר מגיע למרחק היעד.
-----------------
אלגוריתם:
1.  להגדיר את המהירות ההתחלתית (speed) ואת המרחק שעבר (distance) ל-0.
2.  להגדיר את מרחק היעד (targetDistance) ל-100.
3.  להתחיל לולאה "כל עוד המרחק שעבר קטן ממרחק היעד":
    3.1 לבקש מהשחקן תאוצה (acceleration).
    3.2 לבקש מהשחקן תאוטה (deceleration).
    3.3 לחשב את המהירות החדשה: speed = speed + acceleration - deceleration.
    3.4 אם המהירות שלילית, להגדיר אותה ל-0.
    3.5 לחשב את המרחק החדש: distance = distance + speed.
    3.6 להציג את המהירות הנוכחית (speed) ואת המרחק שעבר (distance).
4. להציג הודעה "TARGET DISTANCE REACHED".
5. סוף המשחק.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    speed = 0
    distance = 0
    targetDistance = 100
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד <code><b>distance < targetDistance</b></code>"}
    LoopStart -- Да --> InputAcceleration["קלט תאוצה: <code><b>acceleration</b></code>"]
    InputAcceleration --> InputDeceleration["קלט תאוטה: <code><b>deceleration</b></code>"]
    InputDeceleration --> CalculateSpeed["<code><b>speed = speed + acceleration - deceleration</b></code>"]
    CalculateSpeed --> CheckSpeed["בדיקה: <code><b>speed < 0</b></code>?"]
     CheckSpeed -- כן --> SetSpeedZero["<code><b>speed = 0</b></code>"]
    SetSpeedZero --> CalculateDistance["<code><b>distance = distance + speed</b></code>"]
    CheckSpeed -- לא --> CalculateDistance
    CalculateDistance --> OutputStatus["פלט: <b>מהירות נוכחית: <code>{speed}</code>, מרחק שעבר: <code>{distance}</code></b>"]
    OutputStatus --> LoopStart
    LoopStart -- לא --> OutputEnd["פלט: <b>TARGET DISTANCE REACHED</b>"]
    OutputEnd --> End["סוף"]
```

Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: speed (מהירות) מוגדר ל-0, distance (מרחק שעבר) מוגדר ל-0, targetDistance (מרחק יעד) מוגדר ל-100.
    LoopStart - התחלת לולאה, הנמשכת כל עוד distance קטן מ-targetDistance.
    InputAcceleration - בקשת קלט תאוצה מהמשתמש ושמירתו במשתנה acceleration.
    InputDeceleration - בקשת קלט תאוטה מהמשתמש ושמירתו במשתנה deceleration.
    CalculateSpeed - חישוב מהירות חדשה: speed = speed + acceleration - deceleration.
    CheckSpeed - בדיקה: אם המהירות שלילית, עבור ל-SetSpeedZero.
    SetSpeedZero - אם המהירות קטנה מ-0, הגדר את המהירות ל-0.
    CalculateDistance - חישוב מרחק שעבר חדש: distance = distance + speed.
    OutputStatus - פלט המהירות הנוכחית speed והמרחק שעבר distance.
    OutputEnd - פלט הודעה על השגת מרחק היעד "TARGET DISTANCE REACHED".
    End - סוף התוכנית.
"""


# אתחול ערכים ראשוניים
speed = 0  # מהירות התחלתית של הרכבת
distance = 0  # מרחק התחלתי שעברה הרכבת
targetDistance = 100  # מרחק היעד שיש להשיג

# לולאת המשחק הראשית
while distance < targetDistance:
    # בקשת ערכי תאוצה ותאוטה מהמשתמש
    try:
        acceleration = float(input("הזן תאוצה: "))
        deceleration = float(input("הזן תאוטה: "))
    except ValueError:
        print("אנא הזן ערכים מספריים.")
        continue

    # חישוב המהירות החדשה
    speed = speed + acceleration - deceleration
    
    # בדיקה: אם המהירות הפכה לשלילית, הגדר את המהירות ל-0
    if speed < 0:
        speed = 0
    
    # חישוב המרחק החדש שעברה הרכבת
    distance = distance + speed
    
    # הצגת המהירות הנוכחית והמרחק שעברה הרכבת
    print(f"מהירות נוכחית: {speed}, מרחק שעבר: {distance}")

# כאשר מרחק היעד הושג, הצג הודעה
print("TARGET DISTANCE REACHED")
"""
הסבר קוד:
1.  **אתחול משתנים**:
    -   `speed = 0`: מאתחל את המשתנה `speed` לאחסון המהירות הנוכחית של הרכבת. המהירות ההתחלתית היא 0.
    -   `distance = 0`: מאתחל את המשתנה `distance` לאחסון המרחק שעברה הרכבת. המרחק ההתחלתי הוא 0.
    -   `targetDistance = 100`: מאתחל את המשתנה `targetDistance` לאחסון מרחק היעד שיש להשיג. מרחק היעד הוא 100.

2. **לולאת המשחק הראשית `while distance < targetDistance:`**:
    -   הלולאה נמשכת כל עוד המרחק הנוכחי שעברה הרכבת (`distance`) קטן ממרחק היעד (`targetDistance`).
    -   **קלט נתונים**:
         - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך שאינו מספר, תוצג הודעת שגיאה.
        -   `acceleration = float(input("הזן תאוצה: "))`: מבקש מהמשתמש את ערך התאוצה וממיר אותו למספר עשרוני (float).
        -   `deceleration = float(input("הזן תאוטה: "))`: מבקש מהמשתמש את ערך התאוטה וממיר אותו למספר עשרוני (float).
    -   **חישוב מהירות**:
        -   `speed = speed + acceleration - deceleration`: מחשב את המהירות החדשה, על ידי הוספת התאוצה והחסרת התאוטה מהמהירות הנוכחית.
    -  **בדיקת מהירות**:
        - `if speed < 0:`: בודק האם המהירות שלילית.
        - `speed = 0`: אם המהירות שלילית, מגדיר אותה ל-0.
    -   **חישוב מרחק**:
        -   `distance = distance + speed`: מחשב את המרחק החדש שעברה הרכבת, על ידי הוספת המהירות הנוכחית למרחק הנוכחי.
    -   **פלט נתונים**:
        -   `print(f"מהירות נוכחית: {speed}, מרחק שעבר: {distance}")`: מציג את המהירות הנוכחית ואת המרחק שעברה הרכבת על המסך.
    -   הלולאה נמשכת, עד שיגיע ל-`targetDistance`.

3.  **פלט הודעה על השגת היעד**:
    -   `print("TARGET DISTANCE REACHED")`: מציג הודעה על כך שמרחק היעד הושג, לאחר היציאה מהלולאה.
"""