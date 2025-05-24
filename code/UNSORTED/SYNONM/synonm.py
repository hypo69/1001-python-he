**תותחן (GUNNER):**
=================
**רמת קושי:** 7
-----------------
המשחק "תותחן" הוא משחק שבו השחקן מנסה לפגוע במטרה הנמצאת במרחק מסוים, על ידי ירייה מתותח בזווית ומהירות התחלתית נתונות. המשחק לוקח בחשבון את הגרביטציה.
מטרת המשחק היא למצוא את הזווית והמהירות ההתחלתית הנכונות עבור הירייה, כך שהקליע יגיע למטרה.

**חוקי המשחק:**
1. המחשב קובע מרחק אקראי למטרה.
2. השחקן מזין את זווית הירייה (במעלות) ואת המהירות ההתחלתית של הקליע.
3. המחשב מחשב את מסלול הקליע, תוך התחשבות בגרביטציה.
4. אם הקליע פוגע במטרה (המרחק מהמטרה נמצא בטווח הסטייה המותר), השחקן מנצח.
5. אם הקליע לא פוגע במטרה, השחקן יכול לנסות שוב, עד שינצל את כל ניסיונותיו או יפגע במטרה.
-----------------
**אלגוריתם:**
1. קבע מספר מרבי של ניסיונות (לדוגמה, 10).
2. הגרל מרחק אקראי למטרה בטווח שבין 100 ל-1000.
3. התחל בלולאה "כל עוד לא אזלו הניסיונות":
    3.1 בקש מהשחקן להזין את זווית הירייה (במעלות) ואת המהירות ההתחלתית.
    3.2 המר את הזווית ממעלות לרדיאנים.
    3.3 חשב את טווח טיסת הקליע באמצעות הנוסחה:
        טווח = (מהירות_התחלתית^2 * sin(2 * זווית)) / גרביטציה
        כאשר גרביטציה = 32.2
    3.4 אם טווח טיסת הקליע נמצא בטווח סטייה של +/- 10% ממרחק היעד, הצג הודעה על פגיעה וסיים את המשחק.
    3.5 אם טווח טיסת הקליע קטן ממרחק היעד, הצג הודעה על כך שהטווח אינו מספיק.
    3.6 אם טווח טיסת הקליע גדול ממרחק היעד, הצג הודעה על חריגה (טווח ארוך מדי).
4. אם כל הניסיונות נוצלו, הצג הודעה על הפסד.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    maxAttempts = 10
    gravity = 32.2
    targetDistance = random(100, 1000)
    attempt = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד לא אזלו הניסיונות"}
    LoopStart -- כן --> IncreaseAttempts["<code><b>attempt = attempt + 1</b></code>"]
    IncreaseAttempts --> InputAngleSpeed["<p align='left'>הזנת זווית ירייה (במעלות)
    <code><b>angle</b></code> ומהירות התחלתית
    <code><b>initialSpeed</b></code></p>"]
    InputAngleSpeed --> ConvertAngle["<code><b>angle = angle * pi / 180</b></code>"]
    ConvertAngle --> CalculateDistance["<p align='left'>חישוב טווח הטיסה
    <code><b>distance = (initialSpeed^2 * sin(2 * angle)) / gravity</b></code></p>"]
    CalculateDistance --> CheckHit{"<p align='left'>בדיקה:
    <code><b>targetDistance - (targetDistance * 0.10)  &lt;= distance &lt;=  targetDistance + (targetDistance * 0.10) </b></code></p>"}
    CheckHit -- כן --> OutputWin["הצגת הודעה: <b>YOU HIT THE TARGET!</b>"]
    OutputWin --> End["סיום"]
    CheckHit -- לא --> CheckShort{"בדיקה: <code><b>distance &lt; targetDistance</b></code>?"}
    CheckShort -- כן --> OutputShort["הצגת הודעה: <b>TOO SHORT</b>"]
    OutputShort --> LoopStart
    CheckShort -- לא --> OutputLong["הצגת הודעה: <b>TOO LONG</b>"]
    OutputLong --> LoopStart
    LoopStart -- לא --> OutputLose["הצגת הודעה: <b>YOU LOSE!</b>"]
    OutputLose --> End
```
**מקרא:**
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: maxAttempts (מספר מרבי של ניסיונות) מוגדר ל-10, gravity (גרביטציה) מוגדר ל-32.2, targetDistance (מרחק היעד) מוגרל באופן אקראי בין 100 ל-1000, attempt (הניסיון הנוכחי) מוגדר ל-0.
    LoopStart - התחלת הלולאה, שנמשכת כל עוד לא אזלו הניסיונות.
    IncreaseAttempts - הגדלת מונה הניסיונות ב-1.
    InputAngleSpeed - בקשת הזנת זווית הירייה (במעלות) ומהירות התחלתית מהמשתמש.
    ConvertAngle - המרת הזווית ממעלות לרדיאנים.
    CalculateDistance - חישוב טווח טיסת הקליע.
    CheckHit - בדיקה האם הקליע פגע במטרה (הטווח נמצא בטווח סטייה של +/- 10% ממרחק היעד).
    OutputWin - הצגת הודעת ניצחון אם הקליע פגע במטרה.
    End - סיום התוכנית.
    CheckShort - בדיקה האם טווח הטיסה קטן ממרחק היעד.
    OutputShort - הצגת הודעה "TOO SHORT" אם הטווח קטן מהיעד.
    OutputLong - הצגת הודעה "TOO LONG" אם הטווח גדול מהיעד.
    OutputLose - הצגת הודעה "YOU LOSE!" אם כל הניסיונות נוצלו.
"""
import random
import math

# אתחול פרמטרי המשחק
maxAttempts = 10  # מספר מרבי של ניסיונות
gravity = 32.2  # גרביטציה
targetDistance = random.randint(100, 1000)  # מרחק אקראי למטרה
attempt = 0  # מונה ניסיונות
accuracy = 0.1  # טווח סטייה של 10%

print(f"מרחק היעד: {targetDistance}")

# לולאת המשחק הראשית
while attempt < maxAttempts:
    attempt += 1
    print(f"ניסיון {attempt} מתוך {maxAttempts}")

    # בקשת קלט נתונים מהמשתמש
    while True:
        try:
            angle = float(input("הכנס זווית ירייה (במעלות): "))
            initialSpeed = float(input("הכנס מהירות התחלתית: "))
            break
        except ValueError:
             print("אנא הכנס ערך מספרי")


    # המרת הזווית לרדיאנים
    angle = math.radians(angle)

    # חישוב טווח הטיסה
    distance = (initialSpeed ** 2 * math.sin(2 * angle)) / gravity

    # בדיקה האם הקליע פגע במטרה
    if targetDistance * (1- accuracy) <= distance <= targetDistance * (1 + accuracy):
        print("פגעת במטרה!")
        break
    elif distance < targetDistance:
        print("קצר מדי!")
    else:
        print("ארוך מדי!")

# הצגת הודעת הפסד, אם כל הניסיונות נוצלו
if attempt == maxAttempts:
    print("הפסדת!")
"""
**הסבר קוד:**
1. **ייבוא מודולים:**
   - `import random`: מייבא את המודול `random` להגרלת מספרים אקראיים.
   - `import math`: מייבא את המודול `math` עבור פעולות מתמטיות, כגון `sin` ו-`radians`.

2. **אתחול פרמטרי המשחק:**
   - `maxAttempts = 10`: קובע את המספר המרבי של ניסיונות ל-10.
   - `gravity = 32.2`: קובע את ערך הגרביטציה.
   - `targetDistance = random.randint(100, 1000)`: מגריל מרחק אקראי למטרה בטווח שבין 100 ל-1000.
   - `attempt = 0`: מאתחל את מונה הניסיונות.
   - `accuracy = 0.1`: קובע את טווח הסטייה ב-10% עבור פגיעה במטרה.

3. **לולאת המשחק הראשית `while attempt < maxAttempts:`:**
   - הלולאה נמשכת כל עוד מספר הניסיונות `attempt` קטן מהמספר המרבי של ניסיונות `maxAttempts`.
   - `attempt += 1`: מגדיל את מונה הניסיונות ב-1.
   - `print(f"ניסיון {attempt} מתוך {maxAttempts}")`: מציג את מספר הניסיון הנוכחי.
   - **קלט נתונים מהמשתמש:**
     - `while True:`: לולאה אינסופית לבדיקת תקינות הקלט.
     - `try...except ValueError`: מטפל בשגיאות אפשריות של הזנת ערכים שאינם מספריים.
     - `angle = float(input("הכנס זווית ירייה (במעלות): "))`: מבקש את זווית הירייה מהמשתמש.
     - `initialSpeed = float(input("הכנס מהירות התחלתית: "))`: מבקש את המהירות ההתחלתית של הירייה מהמשתמש.
     - `break`: יוצא מלולאת הקלט אם הנתונים הוזנו כהלכה.
   - **המרת זווית:**
     - `angle = math.radians(angle)`: ממיר את הזווית ממעלות לרדיאנים.
   - **חישוב טווח הטיסה:**
     - `distance = (initialSpeed ** 2 * math.sin(2 * angle)) / gravity`: מחשב את טווח טיסת הקליע, תוך שימוש בנוסחה מפיזיקה.
   - **בדיקת פגיעה:**
     - `if targetDistance * (1 - accuracy) <= distance <= targetDistance * (1 + accuracy):`: בודק האם טווח הטיסה נמצא בטווח סטייה של +/- 10% ממרחק היעד.
     - `print("פגעת במטרה!")`: מציג הודעת ניצחון אם הקליע פגע במטרה.
     - `break`: מסיים את הלולאה אם הקליע פגע במטרה.
     - `elif distance < targetDistance:`: בודק אם הקליע לא הגיע מספיק רחוק.
     - `print("קצר מדי!")`: מציג הודעה שהירייה הייתה קצרה מדי.
     - `else:`: אם הקליע עבר את המטרה.
     - `print("ארוך מדי!")`: מציג הודעה שהירייה הייתה ארוכה מדי.

4. **בדיקת הפסד:**
   - `if attempt == maxAttempts:`: בודק אם כל הניסיונות מוצו.
   - `print("הפסדת!")`: מציג הודעת הפסד.
"""