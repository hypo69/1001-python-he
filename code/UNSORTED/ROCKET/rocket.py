ROCKET:
=================
רמת קושי: 6
-----------------
המשחק "טיל" הוא משחק טקסטואלי שבו השחקן מנסה לשגר טיל על ידי הזנת מהירות התחלתית וזווית שיפוע. המחשב מחשב את מסלול הטיסה ומודיע האם הטיל הגיע למטרה או לא. השחקן נדרש להתאים את פרמטרי השיגור כדי להגיע למטרה.

כללי המשחק:
1. השחקן מתבקש להזין מהירות התחלתית (VELOCITY) וזווית שיפוע (ANGLE) לשיגור הטיל.
2. המחשב מחשב את מרחק הטיסה של הטיל, תוך שימוש בפרמטרים שסופקו ובנוסחה.
3. אם מרחק הטיסה שווה או עולה על 1000, המשחק מודיע שהטיל הגיע למטרה ומציג את המרחק.
4. אם מרחק הטיסה קטן מ-1000, המשחק מודיע שהטיל לא הגיע למטרה, ומציג גם כן את המרחק.
5. המשחק ממשיך עד שהשחקן ירצה לסיים את המשחק, על ידי הזנת מהירות שלילית.
-----------------
אלגוריתם:
1. התחל את לולאת המשחק.
2. בקש מהשחקן מהירות התחלתית (VELOCITY).
3. אם המהירות שלילית, סיים את המשחק.
4. בקש מהשחקן זווית שיפוע (ANGLE).
5. המר את זווית השיפוע ממעלות לרדיאנים.
6. חשב את מרחק טיסת הטיל (DISTANCE) לפי הנוסחה:
   `DISTANCE = (VELOCITY^2 * SIN(2 * זווית ברדיאנים)) / 32.2`
7. הצג את מרחק טיסת הטיל.
8. אם מרחק הטיסה גדול או שווה ל-1000, הצג את ההודעה "GOOD SHOT"
9. אם מרחק הטיסה קטן מ-1000, הצג את ההודעה "SHORT SHOT"
10. חזור על שלבים 2-9.

-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> LoopStart{"תחילת לולאת המשחק"}
    LoopStart --> InputVelocity["הזנת מהירות התחלתית: <code><b>velocity</b></code>"]
    InputVelocity --> CheckVelocity{"בדיקה: <code><b>velocity < 0?</b></code>"}
    CheckVelocity -- כן --> End["סיום"]
    CheckVelocity -- לא --> InputAngle["הזנת זווית שיפוע: <code><b>angle</b></code>"]
    InputAngle --> ConvertAngle["המרת זווית לרדיאנים: <code><b>angleRadians = angle * PI / 180</b></code>"]
    ConvertAngle --> CalculateDistance["חישוב מרחק: <code><b>distance = (velocity^2 * sin(2 * angleRadians)) / 32.2</b></code>"]
    CalculateDistance --> OutputDistance["הצגת מרחק הטיסה: <code><b>distance</b></code>"]
    OutputDistance --> CheckDistance{"בדיקה: <code><b>distance >= 1000?</b></code>"}
    CheckDistance -- כן --> OutputSuccess["הצגת הודעה: <b>GOOD SHOT</b>"]
    OutputSuccess --> LoopStart
    CheckDistance -- לא --> OutputFailure["הצגת הודעה: <b>SHORT SHOT</b>"]
    OutputFailure --> LoopStart

```
מקרא:
    Start - תחילת התוכנית.
    LoopStart - תחילת לולאת המשחק.
    InputVelocity - בקשה מהמשתמש להזין את מהירות הטיל ההתחלתית ושמירה במשתנה velocity.
    CheckVelocity - בדיקה האם המהירות שהוזנה שלילית.
    End - סיום התוכנית אם המהירות שלילית.
    InputAngle - בקשה מהמשתמש להזין את זווית השיפוע של הטיל ושמירה במשתנה angle.
    ConvertAngle - המרת זווית השיפוע ממעלות לרדיאנים.
    CalculateDistance - חישוב מרחק טיסת הטיל לפי הנוסחה.
    OutputDistance - הצגה על המסך של מרחק טיסת הטיל המחושב.
    CheckDistance - בדיקה האם הטיל הגיע למטרה (מרחק טיסה >= 1000).
    OutputSuccess - הצגת ההודעה "GOOD SHOT" אם הטיל הגיע למטרה.
    OutputFailure - הצגת ההודעה "SHORT SHOT" אם הטיל לא הגיע למטרה.
"""
import math


# Constant for acceleration due to gravity (in feet per second squared)
GRAVITY = 32.2

# Start of the game loop
while True:
    try:
        # Prompt the user for initial velocity
        velocity = float(input("הזן מהירות התחלתית לטיל (רגליים/שניה) (ערך שלילי ליציאה): "))

        # Check if the user wants to exit the game
        if velocity < 0:
            print("המשחק הסתיים.")
            break # If velocity is negative, exit the loop

        # Prompt the user for the angle
        angle = float(input("הזן זווית שיפוע (במעלות): "))

        # Convert the angle from degrees to radians
        angle_radians = math.radians(angle)

        # Calculate the rocket's flight distance using the formula
        distance = (velocity**2 * math.sin(2 * angle_radians)) / GRAVITY

        # Output the calculated distance
        print(f"מרחק טיסת הטיל: {distance:.2f} רגליים")

        # Check if the rocket reached the target
        if distance >= 1000:
            print("GOOD SHOT")
        else:
            print("SHORT SHOT")
    except ValueError:
        print("שגיאת קלט. אנא הזן ערך מספרי.")

"""
הסבר קוד:
1.  **ייבוא מודול `math`**:
    -   `import math`: מייבא את המודול `math`, המספק פונקציות מתמטיות, כגון `sin`, `radians`.
2. **קבוע `GRAVITY`**:
    -  `GRAVITY = 32.2`: מגדיר קבוע עבור תאוצת הכבידה ברגליים לשנייה בריבוע.
3. **תחילת לולאת המשחק `while True:`**:
    - לולאה אינסופית המאפשרת לשחקן להמשיך לשגר טילים עד שיזין מהירות שלילית.
4. **בלוק `try...except`**:
   -  `try...except ValueError`: בלוק זה משמש לטיפול בשגיאות קלט אפשריות של המשתמש. אם המשתמש מזין ערך שאינו מספרי (לדוגמה, אותיות), התוכנית לא תקרוס עם שגיאה, אלא תציג הודעת שגיאה.
5. **הזנת נתונים**:
   - `velocity = float(input("הזן מהירות התחלתית לטיל (רגליים/שניה) (ערך שלילי ליציאה): "))`: מבקש מהמשתמש את מהירות הטיל ההתחלתית, ממיר את הקלט למספר עשרוני ושומר במשתנה `velocity`.
   - `if velocity < 0`: בודק האם המשתמש הזין מהירות שלילית, המסמלת רצון לצאת מהמשחק.
   - `print("המשחק הסתיים.")`: מציג הודעה על סיום המשחק.
   - `break`: מסיים את הלולאה אם המהירות שלילית.
   - `angle = float(input("הזן זווית שיפוע (במעלות): "))`: מבקש מהמשתמש את זווית השיפוע, ממיר את הקלט למספר עשרוני ושומר במשתנה `angle`.
6. **המרה זווית**:
    - `angle_radians = math.radians(angle)`: ממיר את הזווית ממעלות לרדיאנים, מכיוון שפונקציות טריגונומטריות במודול `math` עובדות עם רדיאנים.
7. **חישוב מרחק הטיסה**:
    - `distance = (velocity**2 * math.sin(2 * angle_radians)) / GRAVITY`: מחשב את מרחק טיסת הטיל, תוך שימוש בנוסחה, הלקוחה מהתוכנית המקורית בשפת BASIC.
8. **הצגת התוצאות**:
    -  `print(f"מרחק טיסת הטיל: {distance:.2f} רגליים")`: מציג את מרחק הטיסה המחושב עם שתי ספרות אחרי הנקודה העשרונית.
9. **בדיקת הגעה למטרה**:
   - `if distance >= 1000`: בודק האם הטיל הגיע למטרה (מרחק 1000 רגליים ומעלה).
   -  `print("GOOD SHOT")`: מציג הודעה שהטיל הגיע למטרה.
   - `else`: אם מרחק הטיסה קטן מ-1000 רגליים.
   -  `print("SHORT SHOT")`: מציג הודעה שהטיל לא הגיע למטרה.
"""