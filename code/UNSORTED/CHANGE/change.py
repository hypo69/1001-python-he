HURKLE:
=================
רמת קושי: 6
-----------------
המשחק "הֶרְקְל" הוא משחק חיפוש, שבו השחקן מנסה למצוא מחשב ה"מתחבא" במיקום אקראי על רשת בגודל 10x10. לאחר כל מהלך, השחקן מקבל רמזים לגבי הכיוון (צפון, דרום, מזרח, מערב) והמרחק לֶהֶרְקְל. השחקן מנצח כאשר הוא מוצא את הֶרְקְל.

כללי המשחק:
1. המחשב ממקם את הֶרְקְל בנקודה אקראית על רשת 10x10 (קואורדינטות בין 1 ל-10 עבור x ו-y).
2. השחקן מזין את קואורדינטות הניסיון שלו למצוא את הֶרְקְל.
3. המחשב מחשב את המרחק בין מיקום השחקן למיקום הֶרְקְל ומספק רמזים:
    - כיוון (צפון, דרום, מזרח, מערב או צירופיהם).
    - מרחק אל הֶרְקְל.
4. השחקן ממשיך לבצע ניסיונות עד שהוא מוצא את הֶרְקְל, כלומר, קואורדינטות הניסיון שלו תואמות את קואורדינטות הֶרְקְל.
-----------------
אלגוריתם:
1.  אתחול קואורדינטות הֶרְקְל במספרים שלמים אקראיים בין 1 ל-10 עבור x ו-y.
2.  התחלת לולאה "כל עוד הֶרְקְל לא נמצא":
    2.1 בקשת קואורדינטות הניסיון של השחקן (x ו-y).
    2.2 אם קואורדינטות השחקן תואמות את קואורדינטות הֶרְקְל, הצג הודעת ניצחון וסיים את המשחק.
    2.3 אחרת, חשב את המרחק בין קואורדינטות השחקן לקואורדינטות הֶרְקְל.
    2.4 חשב והצג את הכיוון אל הֶרְקְל (צירוף של N, S, E, W).
    2.5 הצג את המרחק אל הֶרְקְל.
3. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeHurklePosition["<p align='left'>אתחול:
    <code><b>
    hurkleX = random(1, 10)
    hurkleY = random(1, 10)
    </b></code></p>"]
    InitializeHurklePosition --> GameLoopStart{"התחלת לולאה: כל עוד הֶרְקְל לא נמצא"}
    GameLoopStart -- כן --> InputGuess["קלט קואורדינטות השחקן: <code><b>userX, userY</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userX == hurkleX and userY == hurkleY</b></code>?"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU FOUND HIM!</b>"]
    OutputWin --> End["סיום"]
    CheckGuess -- לא --> CalculateDistance["<p align='left'>חישוב:
    <code><b>
    distanceX = userX - hurkleX
    distanceY = userY - hurkleY
    distance = sqrt(distanceX^2 + distanceY^2)
    </b></code></p>"]
    CalculateDistance --> CalculateDirection["<p align='left'>קביעת הכיוון:
     <code><b>
    direction = ''
    if distanceY > 0: direction = direction + 'N'
    if distanceY < 0: direction = direction + 'S'
    if distanceX > 0: direction = direction + 'E'
    if distanceX < 0: direction = direction + 'W'
    </b></code></p>"]
    CalculateDirection --> OutputClue["הצגת הודעה: <b>{direction}, מרחק: {distance}</b>"]
     OutputClue --> GameLoopStart
    GameLoopStart -- לא --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeHurklePosition - אתחול קואורדינטות הֶרְקְל hurkleX ו-hurkleY במספרים שלמים אקראיים בין 1 ל-10.
    GameLoopStart - התחלת לולאה שנמשכת כל עוד הֶרְקְל לא נמצא.
    InputGuess - בקשת קואורדינטות הניסיון של המשתמש (userX, userY).
    CheckGuess - בדיקה האם קואורדינטות השחקן תואמות את קואורדינטות הֶרְקְל.
    OutputWin - הצגת הודעת הניצחון "YOU FOUND HIM!" וסיום המשחק.
    End - סיום התוכנית.
    CalculateDistance - חישוב המרחק בין מיקום השחקן למיקום הֶרְקְל.
    CalculateDirection - קביעת הכיוון אל הֶרְקְל (צירוף של N, S, E, W).
    OutputClue - הצגת הרמז (כיוון ומרחק) אל הֶרְקְל.
```
import random
import math

# 1. אתחול קואורדינטות הֶרְקְל במספרים שלמים אקראיים בין 1 ל-10
hurkleX = random.randint(1, 10)
hurkleY = random.randint(1, 10)

# 2. לולאת המשחק הראשית (כל עוד הֶרְקְל לא נמצא)
while True:
    # 2.1 בקשת קואורדינטות הניסיון מהשחקן
    try:
        userX = int(input("הכנס קואורדינטת X (בין 1 ל-10): "))
        userY = int(input("הכנס קואורדינטת Y (בין 1 ל-10): "))
    except ValueError:
        print("אנא הכנס מספרים שלמים.")
        continue

    # בדיקת תקינות קואורדינטות הקלט
    if not (1 <= userX <= 10 and 1 <= userY <= 10):
            print("קואורדינטות חייבות להיות בטווח בין 1 ל-10.")
            continue
    # 2.2 בדיקה האם השחקן ניחש את מיקום הֶרְקְל
    if userX == hurkleX and userY == hurkleY:
        print("YOU FOUND HIM!")
        break  # סיום המשחק אם הֶרְקְל נמצא

    # 2.3 חישוב המרחק בין מיקום השחקן למיקום הֶרְקְל
    distanceX = userX - hurkleX
    distanceY = userY - hurkleY
    distance = math.sqrt(distanceX**2 + distanceY**2)

    # 2.4 קביעת הכיוון אל הֶרְקְל (צירוף של N, S, E, W)
    direction = ""
    if distanceY > 0:
        direction += "N"
    if distanceY < 0:
        direction += "S"
    if distanceX > 0:
        direction += "E"
    if distanceX < 0:
        direction += "W"

    # 2.5 הצגת הרמז (כיוון ומרחק) אל הֶרְקְל
    print(f"{direction if direction else 'כאן'}, מרחק: {distance:.2f}")

"""
הסבר הקוד:
1.  **ייבוא המודולים `random` ו-`math`**:
   - `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים.
   - `import math`: מייבא את המודול `math`, המשמש לחישוב שורש ריבועי.
2.  **אתחול קואורדינטות הֶרְקְל**:
    -   `hurkleX = random.randint(1, 10)`: יוצר מספר שלם אקראי בין 1 ל-10 עבור קואורדינטת X של הֶרְקְל.
    -   `hurkleY = random.randint(1, 10)`: יוצר מספר שלם אקראי בין 1 ל-10 עבור קואורדינטת Y של הֶרְקְל.
3.  **לולאת המשחק הראשית `while True:`**:
    - לולאה אינסופית הנמשכת כל עוד השחקן לא מוצא את הֶרְקְל (עד לביצוע פקודת `break`).
    -  **קלט קואורדינטות השחקן**:
        -   `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין קלט שאינו מספר שלם, תוצג הודעת שגיאה.
        - `userX = int(input("הכנס קואורדינטת X (בין 1 ל-10): "))`: מבקש מהשחקן קואורדינטת X.
        -  `userY = int(input("הכנס קואורדינטת Y (בין 1 ל-10): "))`: מבקש מהשחקן קואורדינטת Y.
    -   **בדיקת תקינות הקלט**:
        -   `if not (1 <= userX <= 10 and 1 <= userY <= 10):`: בודק שהקואורדינטות נמצאות בטווח בין 1 ל-10.
        -   `print("קואורדינטות חייבות להיות בטווח בין 1 ל-10.")`: מציג הודעת שגיאה אם הקואורדינטות אינן תקינות.
        -    `continue`: ממשיך לאיטרציה הבאה של הלולאה.
    -   **בדיקה האם השחקן ניחש את מיקום הֶרְקְל**:
        -   `if userX == hurkleX and userY == hurkleY:`: בודק האם קואורדינטות השחקן והֶרְקְל תואמות.
        -   `print("YOU FOUND HIM!")`: מציג הודעת ניצחון.
        -   `break`: מסיים את הלולאה (ואת המשחק), אם הֶרְקְל נמצא.
    -  **חישוב המרחק**:
        -   `distanceX = userX - hurkleX`: מחשב את ההפרש בקואורדינטת X.
        -  `distanceY = userY - hurkleY`: מחשב את ההפרש בקואורדינטת Y.
        -   `distance = math.sqrt(distanceX**2 + distanceY**2)`: מחשב את המרחק לפי משפט פיתגורס.
    - **קביעת הכיוון**:
        -   `direction = ""`: מאתחל מחרוזת ריקה לאחסון הכיוון.
        -   `if distanceY > 0: direction += "N"`: אם הפרש Y חיובי, מוסיף "N" (צפון).
        -   `if distanceY < 0: direction += "S"`: אם הפרש Y שלילי, מוסיף "S" (דרום).
        -   `if distanceX > 0: direction += "E"`: אם הפרש X חיובי, מוסיף "E" (מזרח).
        -   `if distanceX < 0: direction += "W"`: אם הפרש X שלילי, מוסיף "W" (מערב).
    - **הצגת הרמז**:
        -  `print(f"{direction if direction else 'כאן'}, מרחק: {distance:.2f}")`: מציג את הכיוון (אם קיים, אחרת מציג "כאן") ואת המרחק אל הֶרְקְל.
"""