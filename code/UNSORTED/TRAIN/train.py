TRAIN:
=================
מורכבות: 4
-----------------
המשחק "רכבת" הוא משחק סימולציה שבו השחקן מנהל רכבת, מאיץ ומאט אותה, במטרה להגיע למהירות מסוימת במרחק נתון.
השחקן מזין ערכים עבור האצה והאטה, והמשחק מציג את המהירות הנוכחית ואת המרחק שעברה הרכבת.
המטרה היא להגיע למהירות יעד במרחק יעד.
המשחק מציג את המרחק שעבר ואת המהירות הנוכחית, ומסתיים כאשר מרחק היעד מושג.
-----------------
אלגוריתם:
1.  להגדיר את המהירות ההתחלתית (speed) ואת המרחק שעבר (distance) ל-0.
2.  להגדיר את מרחק היעד (targetDistance) ל-100.
3.  להתחיל בלולאה "כל עוד המרחק שעבר קטן ממרחק היעד":
    3.1 לבקש מהשחקן את ערך ההאצה (acceleration).
    3.2 לבקש מהשחקן את ערך ההאטה (deceleration).
    3.3 לחשב את המהירות החדשה: speed = speed + acceleration - deceleration.
    3.4 אם המהירות שלילית, להגדיר אותה ל-0.
    3.5 לחשב את המרחק החדש: distance = distance + speed.
    3.6 להדפיס את המהירות הנוכחית (speed) ואת המרחק שעבר (distance).
4. להדפיס את ההודעה "TARGET DISTANCE REACHED".
5. סיום המשחק.
-----------------
דיאגרמת זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    speed = 0
    distance = 0
    targetDistance = 100
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד <code><b>distance < targetDistance</b></code>"}
    LoopStart -- כן --> InputAcceleration["הזנת האצה: <code><b>acceleration</b></code>"]
    InputAcceleration --> InputDeceleration["הזנת האטה: <code><b>deceleration</b></code>"]
    InputDeceleration --> CalculateSpeed["<code><b>speed = speed + acceleration - deceleration</b></code>"]
    CalculateSpeed --> CheckSpeed["בדיקה: <code><b>speed < 0</b></code>?"]
     CheckSpeed -- כן --> SetSpeedZero["<code><b>speed = 0</b></code>"]
    SetSpeedZero --> CalculateDistance["<code><b>distance = distance + speed</b></code>"]
    CheckSpeed -- לא --> CalculateDistance
    CalculateDistance --> OutputStatus["הדפסה: <b>מהירות נוכחית: <code>{speed}</code>, מרחק שעבר: <code>{distance}</code></b>"]
    OutputStatus --> LoopStart
    LoopStart -- לא --> OutputEnd["הדפסה: <b>TARGET DISTANCE REACHED</b>"]
    OutputEnd --> End["סיום"]
```

מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: speed (מהירות) מוגדר ל-0, distance (מרחק שעבר) מוגדר ל-0, targetDistance (מרחק יעד) מוגדר ל-100.
    LoopStart - התחלת לולאה הנמשכת כל עוד distance קטן מ- targetDistance.
    InputAcceleration - בקשה מהמשתמש להזנת האצה ושמירתה במשתנה acceleration.
    InputDeceleration - בקשה מהמשתמש להזנת האטה ושמירתה במשתנה deceleration.
    CalculateSpeed - חישוב מהירות חדשה: speed = speed + acceleration - deceleration.
    CheckSpeed - בדיקה: אם המהירות שלילית, עבור ל- SetSpeedZero.
    SetSpeedZero - אם המהירות קטנה מ-0, הגדר את המהירות ל-0.
    CalculateDistance - חישוב מרחק חדש שעבר: distance = distance + speed.
    OutputStatus - הדפסת המהירות הנוכחית speed והמרחק שעבר distance.
    OutputEnd - הדפסת הודעה על השגת מרחק היעד "TARGET DISTANCE REACHED".
    End - סיום התוכנית.
"""


# אתחול ערכים התחלתיים
speed = 0  # מהירות התחלתית של הרכבת
distance = 0  # מרחק התחלתי שעבר
targetDistance = 100  # מרחק יעד שיש להגיע אליו

# לולאת המשחק הראשית
while distance < targetDistance:
    # בקשת ערכי האצה והאטה מהמשתמש
    try:
        acceleration = float(input("Введите ускорение: "))
        deceleration = float(input("Введите замедление: "))
    except ValueError:
        print("Пожалуйста, введите числовые значения.")
        continue

    # חישוב המהירות החדשה
    speed = speed + acceleration - deceleration
    
    # בדיקה: אם המהירות שלילית, הגדר אותה ל-0
    if speed < 0:
        speed = 0
    
    # חישוב המרחק החדש שעבר
    distance = distance + speed
    
    # הדפסת המהירות הנוכחית והמרחק שעבר
    print(f"Текущая скорость: {speed}, Пройденное расстояние: {distance}")

# כאשר מרחק היעד הושג, הדפסת הודעה
print("TARGET DISTANCE REACHED")
"""
הסבר על הקוד:
1.  **אתחול משתנים**:
    -   `speed = 0`: מאתחל את המשתנה `speed` לאחסון המהירות הנוכחית של הרכבת. המהירות ההתחלתית היא 0.
    -   `distance = 0`: מאתחל את המשתנה `distance` לאחסון המרחק שעבר. המרחק ההתחלתי הוא 0.
    -   `targetDistance = 100`: מאתחל את המשתנה `targetDistance` לאחסון מרחק היעד שיש להגיע אליו. מרחק היעד הוא 100.

2. **לולאת המשחק הראשית `while distance < targetDistance:`**:
    -   הלולאה נמשכת כל עוד המרחק הנוכחי שעבר (`distance`) קטן ממרחק היעד (`targetDistance`).
    -   **קלט נתונים**:
         - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך שאינו מספר, תודפס הודעת שגיאה.
        -   `acceleration = float(input("Введите ускорение: "))`: מבקש מהמשתמש את ערך ההאצה וממיר אותו למספר עם נקודה עשרונית (float).
        -   `deceleration = float(input("Введите замедление: "))`: מבקש מהמשתמש את ערך ההאטה וממיר אותו למספר עם נקודה עשרונית (float).
    -   **חישוב מהירות**:
        -   `speed = speed + acceleration - deceleration`: מחשב את המהירות החדשה, על ידי הוספת האצה והחסרת האטה מהמהירות הנוכחית.
    -  **בדיקת מהירות**:
        - `if speed < 0:`: בודק האם המהירות שלילית.
        - `speed = 0`: אם המהירות שלילית, מגדיר אותה ל-0.
    -   **חישוב מרחק**:
        -   `distance = distance + speed`: מחשב את המרחק החדש שעבר, על ידי הוספת המהירות הנוכחית למרחק הנוכחי.
    -   **הדפסת נתונים**:
        -   `print(f"Текущая скорость: {speed}, Пройденное расстояние: {distance}")`: מדפיס את המהירות הנוכחית ואת המרחק שעבר למסך.
    -   הלולאה ממשיכה עד שמושג `targetDistance`.

3.  **הדפסת הודעה על השגת היעד**:
    -   `print("TARGET DISTANCE REACHED")`: מדפיס הודעה כי מרחק היעד הושג, לאחר היציאה מהלולאה.
"""