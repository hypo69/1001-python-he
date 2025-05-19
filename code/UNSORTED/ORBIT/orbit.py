**ORBIT:**
=================
**מורכבות:** 5
-----------------
המשחק "ORBIT" הוא משחק טקסטואלי שבו השחקן שולט בחללית המקיפה כוכב לכת. מטרת המשחק היא לקבוע מהירות התחלתית וזווית כך שהחללית תגיע למסלול (אורביטה) יציב. על השחקן לנחש את הערכים של המהירות ההתחלתית והזווית כדי להכניס את החללית למסלול. המשחק משתמש בסימולציה של כוח משיכה גרביטציוני לחישוב מסלול הטיסה של החללית.

**כללי המשחק:**
1. השחקן מזין מהירות התחלתית וזווית עבור החללית.
2. המשחק מדמה את מסלול הטיסה של החללית תחת השפעת כוח המשיכה.
3. אם החללית אינה מגיעה למסלול, השחקן מקבל הצעה להזין ערכי מהירות וזווית חדשים.
4. המשחק נמשך עד שהחללית מגיעה למסלול או שנגמר מספר הניסיונות.
5. אם החללית מגיעה למסלול, המשחק מודיע על כך לשחקן.
-----------------
**אלגוריתם:**
1. אתחול משתנים:
   - קביעת מספר הניסיונות ההתחלתי ל-0.
   - קביעת מספר הניסיונות המקסימלי (לדוגמה, 10).
2. התחלת לולאת "כל עוד מספר הניסיונות קטן ממספר המקסימלי":
    2.1. הגדלת מספר הניסיונות ב-1.
    2.2. בקשת קלט מהשחקן עבור מהירות התחלתית (V).
    2.3. בקשת קלט מהשחקן עבור זווית התחלתית (A).
    2.4. המרת הזווית ממעלות לרדיאנים.
    2.5. חישוב רכיבי המהירות ההתחלתית Vx ו-Vy (Vx = V * Cos(A), Vy = V * Sin(A)).
    2.6. קביעת קואורדינטות התחלתיות x ו-y.
    2.7. התחלת סימולציית התנועה (לולאה):
        2.7.1. חישוב המרחק לכוכב הלכת R (R = שורש(x*x + y*y)).
        2.7.2. חישוב התאוצה Ax ו-Ay (Ax = -x / R^3, Ay = -y / R^3).
        2.7.3. עדכון רכיבי המהירות (Vx = Vx + Ax, Vy = Vy + Ay).
        2.7.4. עדכון הקואורדינטות (x = x + Vx, y = y + Vy).
        2.7.5. בדיקה האם הגוף הגיע למסלול יציב (אם x^2 + y^2 בערך שווה ל-R^2 במשך זמן מה).
        2.7.6. אם הגוף הגיע למסלול או יצא מגבולות הסימולציה, יציאה מלולאת הסימולציה.
    2.8. אם הגוף הגיע למסלול יציב, הצגת ההודעה "ORBIT ESTABLISHED" ומעבר לשלב 3.
    2.9. אם הגוף לא הגיע למסלול, הצגת ההודעה "FAILED", וחזרה על הלולאה החל משלב 2.
3. סיום המשחק.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfTries = 0<br>
    maxTries = 10
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: <code><b>numberOfTries &lt; maxTries</b></code>"}
    LoopStart -- כן --> IncreaseTries["<code><b>numberOfTries = numberOfTries + 1</b></code>"]
    IncreaseTries --> InputVelocity["הכנס מהירות התחלתית: <code><b>initialVelocity</b></code>"]
    InputVelocity --> InputAngle["הכנס זווית התחלתית: <code><b>initialAngle</b></code>"]
    InputAngle --> CalculateVelocityComponents["<p align='left'>חישוב:
    <code><b>
    angleInRadians = initialAngle * PI / 180<br>
    velocityX = initialVelocity * cos(angleInRadians)<br>
    velocityY = initialVelocity * sin(angleInRadians)
    </b></code></p>"]
    CalculateVelocityComponents --> InitializePosition["<p align='left'>אתחול מיקום:
    <code><b>
    x = initialX<br>
    y = initialY
    </b></code></p>"]
    InitializePosition --> SimulationLoopStart{"תחילת סימולציה: כל עוד לא במסלול או יצאו מגבולות"}
    SimulationLoopStart --> CalculateDistance["<p align='left'>חישוב מרחק:
        <code><b>distance = sqrt(x^2 + y^2)</b></code></p>"]
    CalculateDistance --> CalculateAcceleration["<p align='left'>חישוב תאוצה:
        <code><b>
        accelerationX = -x / distance^3<br>
        accelerationY = -y / distance^3
        </b></code></p>"]
    CalculateAcceleration --> UpdateVelocity["<p align='left'>עדכון מהירות:
        <code><b>
        velocityX = velocityX + accelerationX<br>
        velocityY = velocityY + accelerationY
        </b></code></p>"]
    UpdateVelocity --> UpdatePosition["<p align='left'>עדכון מיקום:
        <code><b>
        x = x + velocityX<br>
        y = y + velocityY
        </b></code></p>"]
    UpdatePosition --> CheckOrbit{"בדיקה: <code><b>במסלול?</b></code>"}
    CheckOrbit -- כן --> OutputOrbitEstablished["פלט: <b>ORBIT ESTABLISHED</b>"]
    OutputOrbitEstablished --> End["סוף"]
    CheckOrbit -- לא --> CheckOutOfBound{"בדיקה: <code><b>יצאו מגבולות?</b></code>"}
    CheckOutOfBound -- כן --> SimulationLoopEnd["סוף לולאת סימולציה"]
    CheckOutOfBound -- לא --> SimulationLoopStart
     SimulationLoopEnd --> CheckTries{"בדיקה: <code><b>numberOfTries < maxTries?</b></code>"}
    CheckTries -- כן --> LoopStart
    CheckTries -- לא --> OutputFailed["פלט: <b>FAILED</b>"]
    OutputFailed --> End
    LoopStart -- לא --> End
```

**מקרא:**
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfTries (מספר הניסיונות) נקבע ל-0, maxTries (מספר הניסיונות המקסימלי) נקבע ל-10.
    LoopStart - תחילת הלולאה שנמשכת כל עוד מספר הניסיונות קטן מהמקסימלי.
    IncreaseTries - הגדלת מונה מספר הניסיונות ב-1.
    InputVelocity - בקשת קלט מהמשתמש עבור מהירות התחלתית ושמירתו במשתנה initialVelocity.
    InputAngle - בקשת קלט מהמשתמש עבור זווית התחלתית ושמירתו במשתנה initialAngle.
    CalculateVelocityComponents - חישוב רכיבי המהירות ההתחלתית: הזווית מומרת לרדיאנים, ומחושבים הרכיבים velocityX ו-velocityY.
    InitializePosition - אתחול הקואורדינטות ההתחלתיות x ו-y.
    SimulationLoopStart - תחילת לולאת הסימולציה, שנמשכת כל עוד לא הושג מסלול או שיצאו מגבולות.
    CalculateDistance - חישוב המרחק מהעצם למרכז כוכב הלכת.
    CalculateAcceleration - חישוב התאוצה על צירי x ו-y, המבוסס על המרחק לכוכב הלכת.
    UpdateVelocity - עדכון מהירות העצם על בסיס התאוצה.
    UpdatePosition - עדכון מיקום העצם על בסיס המהירות.
    CheckOrbit - בדיקה האם העצם הוכנס למסלול יציב.
    OutputOrbitEstablished - הצגת הודעה על כך שהמסלול הושג.
    End - סיום התוכנית.
    CheckOutOfBound - בדיקה האם העצם יצא מגבולות הסימולציה.
    SimulationLoopEnd - סיום לולאת הסימולציה.
    CheckTries - בדיקה האם מספר הניסיונות חרג מהערך המקסימלי.
    OutputFailed - הצגת הודעה על כך שלא עלה בידי להגיע למסלול.
```python
import math

# Constants for simulation
INITIAL_X = 100  # קואורדינטת X התחלתית
INITIAL_Y = 0   # קואורדינטת Y התחלתית
TIME_STEP = 0.1   # צעד הזמן עבור הסימולציה
ORBIT_TOLERANCE = 10  # סטיhה מותרת לקביעת מסלול יציב
MAX_STEPS = 1000  # מספר צעדי סימולציה מקסימלי
MAX_TRIES = 10 # מספר ניסיונות מקסימלי

def simulate_orbit(initial_velocity, initial_angle):
    """
    מדמה מסלול (אורביטה) של חללית סביב כוכב לכת.

    Args:
        initial_velocity (float): המהירות ההתחלתית של החללית.
        initial_angle (float): זווית הכיוון ההתחלתית של החללית במעלות.

    Returns:
         bool: True אם הושג מסלול יציב; False אחרת.
    """
    # ממיר את הזווית ממעלות לרדיאנים
    angle_in_radians = math.radians(initial_angle)

    # מחשב את רכיבי המהירות ההתחלתית
    velocity_x = initial_velocity * math.cos(angle_in_radians)
    velocity_y = initial_velocity * math.sin(angle_in_radians)

    # קואורדינטות התחלתיות
    x = INITIAL_X
    y = INITIAL_Y

    # משתנים לבדיקת מסלול יציב
    last_distance = 0
    orbit_count = 0

    # מודלינג תנועה
    for step in range(MAX_STEPS):
        # מחשב את המרחק לכוכב הלכת
        distance = math.sqrt(x * x + y * y)

        # מחשב תאוצה (כוח משיכה)
        acceleration_x = -x / (distance ** 3)
        acceleration_y = -y / (distance ** 3)

        # מעדכן מהירות
        velocity_x += acceleration_x * TIME_STEP
        velocity_y += acceleration_y * TIME_STEP

        # מעדכן מיקום
        x += velocity_x * TIME_STEP
        y += velocity_y * TIME_STEP

        # בודק יציבות מסלול.
        if abs(distance - last_distance) < ORBIT_TOLERANCE:
           orbit_count += 1
        else:
           orbit_count = 0

        if orbit_count > 50: # בודק שהמרחק לא השתנה 50 פעמים רצופות.
            return True # מסלול יציב

        last_distance = distance

        # בדיקת יציאה מגבולות
        if abs(x) > 500 or abs(y) > 500 :
            return False

    return False # לא עלה בידי להגיע למסלול

# לולאת המשחק הראשית
def play_orbit_game():
    """
    מפעיל את משחק סימולציית המסלול.
    """

    number_of_tries = 0

    while number_of_tries < MAX_TRIES:
        number_of_tries += 1

        try:
            # מבקש מהמשתמש להכניס מהירות התחלתית וזווית
            initial_velocity = float(input("הכנס מהירות התחלתית (למשל, 5): "))
            initial_angle = float(input("הכנס זווית התחלתית במעלות (למשל, 45): "))
        except ValueError:
            print("אנא הכנס ערכים מספריים תקינים.")
            continue

        # מפעיל את הסימולציה
        orbit_established = simulate_orbit(initial_velocity, initial_angle)

        if orbit_established:
            print("ORBIT ESTABLISHED")
            return  # מסיים את המשחק
        else:
             print("FAILED")
    print("GAME OVER")


# מפעיל את המשחק רק אם הסקריפט מופעל ישירות.
if __name__ == "__main__":
    play_orbit_game()

```

"""
**הסבר קוד:**

1. **ייבוא המודול `math`**:
   - `import math`: מייבא את המודול `math`, המשמש לפעולות מתמטיות כגון `cos`, `sin`, `sqrt` ו-`radians`.

2. **קבועים**:
    - `INITIAL_X`, `INITIAL_Y`: הקואורדינטות ההתחלתיות של החללית.
    - `TIME_STEP`: צעד הזמן עבור סימולציית התנועה.
    - `ORBIT_TOLERANCE`: סטיhה מותרת במרחק לצורך קביעת מסלול יציב.
    - `MAX_STEPS`: המספר המקסימלי של צעדי הסימולציה, כדי למנוע לולאה אינסופית.
    - `MAX_TRIES`: המספר המקסימלי של ניסיונות עבור המשתמש להכניס את החללית למסלול.

3. **פונקציה `simulate_orbit(initial_velocity, initial_angle)`**:
    -   `angle_in_radians = math.radians(initial_angle)`: ממיר את הזווית ממעלות לרדיאנים, שכן פונקציות טריגונומטריות בפייתון פועלות עם רדיאנים.
    -   `velocity_x = initial_velocity * math.cos(angle_in_radians)`: מחשב את רכיב המהירות ההתחלתית על ציר X.
    -   `velocity_y = initial_velocity * math.sin(angle_in_radians)`: מחשב את רכיב המהירות ההתחלתית על ציר Y.
    -   `x = INITIAL_X`, `y = INITIAL_Y`: קובע את הקואורדינטות ההתחלתיות של החללית.
    -   **לולאת הסימולציה**:
        -   `for step in range(MAX_STEPS)`: לולאה המדמה את תנועת החללית במשך `MAX_STEPS` צעדים.
        -   `distance = math.sqrt(x * x + y * y)`: מחשב את המרחק מהחללית למרכז כוכב הלכת.
        -   `acceleration_x = -x / (distance ** 3)`: מחשב את התאוצה על ציר X (כוח משיכה גרביטציוני).
        -   `acceleration_y = -y / (distance ** 3)`: מחשב את התאוצה על ציר Y (כוח משיכה גרביטציוני).
        -   `velocity_x += acceleration_x * TIME_STEP`: מעדכן את המהירות על ציר X.
        -   `velocity_y += acceleration_y * TIME_STEP`: מעדכן את המהירות על ציר Y.
        -   `x += velocity_x * TIME_STEP`: מעדכן את קואורדינטת X.
        -   `y += velocity_y * TIME_STEP`: מעדכן את קואורדינטת Y.
        -   **בדיקת מסלול יציב**:
            -   `if abs(distance - last_distance) < ORBIT_TOLERANCE:`: בודק אם המרחק למרכז כוכב הלכת השתנה בערך מותר.
            -   `orbit_count += 1` מגדיל מונה אם המרחק בטווח המותר.
            -   `else: orbit_count = 0`: מאפס את המונה אם המרחק משתנה.
            -   `if orbit_count > 50`: בודק שהמרחק לא השתנה 50 פעמים ברציפות.
            -   `return True`: מחזיר `True` אם החללית הגיעה למסלול יציב.
        -   `last_distance = distance`: שומר את ערך המרחק האחרון.
        -    **בדיקת יציאה מגבולות**:
            -  `if abs(x) > 500 or abs(y) > 500`: בודק אם החללית יצאה מגבולות הסימולציה.
            -  `return False`: מחזיר `False` אם החללית יצאה מגבולות.
    -  `return False`:  מחזיר `False` אם מסלול לא הושג בתוך `MAX_STEPS` צעדים.

4. **פונקציה `play_orbit_game()`**:
    -   `number_of_tries = 0`: מאתחל את מונה ניסיונות המשתמש.
    -   **לולאת `while number_of_tries < MAX_TRIES`**: לולאה הנמשכת כל עוד מספר הניסיונות לא הגיע ל-`MAX_TRIES`.
    -   `number_of_tries += 1`: מגדיל את מונה הניסיונות.
    -   `try...except ValueError`: טיפול בחריגות אם המשתמש הזין ערך לא תקין.
    -   `initial_velocity = float(input("הכנס מהירות התחלתית (למשל, 5): "))`: מבקש מהמשתמש להכניס מהירות התחלתית.
    -   `initial_angle = float(input("הכנס זווית התחלתית במעלות (למשל, 45): "))`: מבקש מהמשתמש להכניס זווית התחלתית במעלות.
    -   `orbit_established = simulate_orbit(initial_velocity, initial_angle)`: קורא לפונקציה `simulate_orbit` לדימוי המסלול.
    -   `if orbit_established: print("ORBIT ESTABLISHED"); return`: אם הושג מסלול, מוצגת הודעה והמשחק מסתיים.
    -   `else: print("FAILED")`: אם מסלול לא הושג, מוצגת הודעה על כישלון.
    -   `print("GAME OVER")`: מוצג בסוף המשחק אם לא עלה בידי להכניס למסלול בתוך `MAX_TRIES` ניסיונות.

5. **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בודק אם הסקריפט הופעל ישירות.
    -   `play_orbit_game()`: קורא לפונקציה `play_orbit_game` להתחלת המשחק.

"""