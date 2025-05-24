"""
RUSROU:
=================
רמת קושי: 3
-----------------
משחק "רולטה רוסית" הוא משחק פשוט שבו המחשב מדמה סיבוב של תוף רבולבר המכיל קליע אחד. השחקן בוחר בין לחיצה על ההדק לבין עצירה. מטרת המשחק היא להימנע מהירי. אם השחקן ממשיך לשחק ולוחץ על ההדק ברגע שבו הקליע נמצא בתוף, הוא מפסיד.

כללי המשחק:
1.  המחשב מדמה תוף רבולבר עם שישה תאים, ובאחד מהם מוכנס קליע באופן אקראי.
2.  השחקן מחליט, האם ללחוץ על ההדק ("ללחוץ" או "כן") או לעצור את המשחק ("לא").
3.  אם השחקן מחליט ללחוץ על ההדק, מתבצעת בדיקה האם הקליע היה בתא הנוכחי.
4.  אם הקליע היה, השחקן מפסיד.
5.  אם הקליע לא היה, המשחק נמשך, והמחשב מדמה את הסיבוב הבא של התוף.
6.  אם השחקן מחליט לעצור את המשחק, הוא נחשב למנצח.
-----------------
אלגוריתם:
1.  לאתחל את המשתנה `bullet` במספר אקראי בין 1 ל-6 (מספר התא עם הקליע).
2.  להתחיל לולאה "כל עוד המשחק לא הסתיים":
    2.1. לשאול את השחקן האם הוא רוצה ללחוץ על ההדק ("ללחוץ" או "כן") או לעצור ("לא").
    2.2. אם השחקן בוחר "לא", להציג הודעת ניצחון ולסיים את המשחק.
    2.3. אם השחקן בוחר "כן", ליצור מספר אקראי בין 1 ל-6 (מספר התא הנוכחי).
    2.4. אם מספר התא עם הקליע (`bullet`) זהה למספר התא הנוכחי, להציג הודעת הפסד ולסיים את המשחק.
    2.5. אם מספר התא עם הקליע (`bullet`) אינו זהה למספר התא הנוכחי, להודיע ש"לחץ ריק" ולהמשיך במשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBullet["<p align='left'>אתחול משתנה <code><b>bullet</b></code>:
    <code><b>bullet = random(1, 6)</b></code></p>"]
    InitializeBullet --> LoopStart{"תחילת לולאה: כל עוד המשחק לא הסתיים"}
    LoopStart --> InputChoice["בקשת קלט: ללחוץ או לא?"]
    InputChoice -- "לא" --> OutputWin["הצגת הודעה: <b>YOU'RE SAFE</b>"]
    OutputWin --> End["סיום"]
    InputChoice -- "כן" --> GenerateChamber["<code><b>currentChamber = random(1, 6)</b></code>"]
     GenerateChamber --> CheckChamber{"בדיקה: <code><b>currentChamber == bullet?</b></code>"}
    CheckChamber -- כן --> OutputLose["הצגת הודעה: <b>BANG-YOU'RE DEAD</b>"]
    OutputLose --> End
    CheckChamber -- לא --> OutputClick["הצגת הודעה: <b>CLICK</b>"]
    OutputClick --> LoopStart
```
מקרא:
   Start - תחילת המשחק.
    InitializeBullet - אתחול המשתנה `bullet` במספר אקראי מ-1 עד 6, המייצג את התא עם הקליע.
    LoopStart - תחילת לולאה, הנמשכת עד שהשחקן מחליט לעצור או מפסיד.
    InputChoice - בקשת קלט מהשחקן: "ללחוץ" או "לא".
    OutputWin - הצגת ההודעה "YOU'RE SAFE", אם השחקן בוחר "לא", וסיום המשחק.
    End - סיום המשחק.
    GenerateChamber - יצירת מספר אקראי `currentChamber` מ-1 עד 6, המייצג את התא הנוכחי.
    CheckChamber - בדיקה האם `currentChamber` זהה לתא עם הקליע `bullet`.
    OutputLose - הצגת ההודעה "BANG-YOU'RE DEAD" וסיום המשחק, אם התא עם הקליע היה זהה.
    OutputClick - הצגת ההודעה "CLICK", אם הקליע לא נתקל, והמשך הלולאה.
"""
import random

# Generate a random number from 1 to 6 for the bullet chamber
bullet = random.randint(1, 6)

# Start the main game loop
while True:
    # Ask the user for their choice: press or not
    choice = input("ללחוץ על ההדק? (כן/לא): ").lower()

    # If the user chooses "לא" (no), they win
    if choice == "לא":
        print("אתה בטוח!")
        break  # End the game

    # If the user chooses "כן" (yes), continue the game
    if choice == "כן":
        # Generate a random number from 1 to 6 for the current chamber
        current_chamber = random.randint(1, 6)

        # Check if the bullet is in the current chamber
        if current_chamber == bullet:
            print("באנג-אתה מת!")  # If it is, the player loses
            break  # End the game
        else:
            print("לחץ ריק")  # If not, the game continues
    else:
         print("קלט שגוי. אנא הזן 'כן' או 'לא'.")

"""
הסבר קוד:

1.  **ייבוא מודול `random`:**
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים.
2.  **אתחול מיקום הקליע:**
    -   `bullet = random.randint(1, 6)`: יוצר מספר שלם אקראי בין 1 ל-6, המייצג את מספר התא בו נמצא הקליע. משתנה זה שומר את התא "הטעון".
3.  **לולאת המשחק הראשית:**
    -   `while True:`: לולאה אינסופית, הנמשכת עד שהמשחק מסתיים (השחקן מחליט לעצור או מפסיד).
    -   **בקשת בחירה מהשחקן:**
        -   `choice = input("ללחוץ על ההדק? (כן/לא): ").lower()`: מבקש קלט מהמשתמש (ללחוץ או לא) וממיר את הקלט לאותיות קטנות לפישוט ההשוואה.
    -   **תנאי ניצחון (בחירה "לא"):**
        -   `if choice == "לא":`: אם השחקן מזין "לא", הוא מנצח.
        -   `print("אתה בטוח!")`: מציג הודעה על ניצחון.
        -   `break`: מסיים את הלולאה, כלומר המשחק מסתיים.
    -   **תנאי המשך משחק (בחירה "כן"):**
        -   `if choice == "כן":`: אם השחקן מזין "כן", המשחק נמשך.
        -   `current_chamber = random.randint(1, 6)`: יוצר מספר שלם אקראי בין 1 ל-6, המייצג את מספר התא הנוכחי.
        -   **בדיקת הפסד:**
            -   `if current_chamber == bullet:`: בודק האם מספר התא הנוכחי זהה למספר התא בו נמצא הקליע.
            -   `print("באנג-אתה מת!")`: אם התא עם הקליע היה זהה, השחקן מפסיד ומוצגת הודעה על הפסד.
            -   `break`: מסיים את הלולאה, כלומר המשחק מסתיים.
        -   **המשך משחק:**
            -   `else:`: אם הקליע לא היה בתא הנוכחי.
            -   `print("לחץ ריק")`: מוצגת הודעה שהקליע לא היה והמשחק נמשך.
    -   **טיפול בקלט שגוי:**
        - `else:`:  אם הקלט אינו "כן" ואינו "לא"
        - `print("קלט שגוי. אנא הזן 'כן' או 'לא'.")`: מוצגת הודעה על קלט שגוי.
"""