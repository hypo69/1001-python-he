"""
HURKLE:
=================
רמת מורכבות: 6
-----------------
המשחק "הורקל" הוא משחק חיפוש, שבו השחקן מנסה למצוא מחשב אשר "מתחבא" במיקום אקראי על רשת בגודל 10x10. השחקן מקבל רמזים אודות הכיוון (צפון, דרום, מזרח, מערב) והמרחק להורקל לאחר כל ניחוש. השחקן מנצח כאשר הוא מוצא את ההורקל.

חוקי המשחק:
1.  המחשב ממקם את ההורקל בנקודה אקראית על רשת 10x10 (קואורדינטות בין 1 ל-10 בציר x ו-y).
2.  השחקן מזין את קואורדינטות הניסיון שלו למצוא את ההורקל.
3.  המחשב מחשב את המרחק בין מיקום השחקן למיקום ההורקל ומספק רמזים:
    -   כיוון (צפון, דרום, מזרח, מערב או שילוב שלהם).
    -   מרחק להורקל.
4.  השחקן ממשיך לנסות עד שהוא מוצא את ההורקל, כלומר, כאשר קואורדינטות הניחוש שלו תואמות את קואורדינטות ההורקל.
-----------------
אלגוריתם:
1.  אתחול קואורדינטות ההורקל למספרים שלמים אקראיים בין 1 ל-10 עבור x ו-y.
2.  התחלת לולאה "כל עוד ההורקל לא נמצא":
    2.1 בקשת קואורדינטות הניחוש של השחקן (x ו-y).
    2.2 אם קואורדינטות השחקן תואמות את קואורדינטות ההורקל, הצגת הודעת ניצחון וסיום המשחק.
    2.3 אחרת, חישוב המרחק בין קואורדינטות השחקן לקואורדינטות ההורקל.
    2.4 חישוב והצגת הכיוון להורקל (שילוב של N, S, E, W).
    2.5 הצגת המרחק להורקל.
3.  סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeHurklePosition["<p align='left'>אתחול:
    <code><b>
    hurkleX = random(1, 10)
    hurkleY = random(1, 10)
    </b></code></p>"]
    InitializeHurklePosition --> GameLoopStart{"התחלת לולאה: כל עוד ההורקל לא נמצא"}
    GameLoopStart -- כן --> InputGuess["הזנת קואורדינטות השחקן: <code><b>userX, userY</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userX == hurkleX and userY == hurkleY</b></code>?"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU FOUND HIM!</b>"]
    OutputWin --> End["סיום"]
    CheckGuess -- לא --> CalculateDistance["<p align='left'>חישוב:
    <code><b>
    distanceX = userX - hurkleX
    distanceY = userY - hurkleY
    distance = sqrt(distanceX^2 + distanceY^2)
    </b></code></p>"]
    CalculateDistance --> CalculateDirection["<p align='left'>קביעת כיוון:
     <code><b>
    direction = ''
    if distanceY > 0: direction = direction + 'N'
    if distanceY < 0: direction = direction + 'S'
    if distanceX > 0: direction = direction + 'E'
    if distanceX < 0: direction = direction + 'W'
    </b></code></p>"]
    CalculateDirection --> OutputClue["הצגת הודעה: <b>{direction}, distance: {distance}</b>"]
     OutputClue --> GameLoopStart
    GameLoopStart -- לא --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeHurklePosition - אתחול קואורדינטות ההורקל hurkleX ו-hurkleY למספרים שלמים אקראיים מ-1 עד 10.
    GameLoopStart - התחלת הלולאה, אשר נמשכת כל עוד ההורקל לא נמצא.
    InputGuess - בקשת קואורדינטות הניחוש מהמשתמש (userX, userY).
    CheckGuess - בדיקה האם קואורדינטות השחקן תואמות את קואורדינטות ההורקל.
    OutputWin - הצגת הודעת ניצחון "YOU FOUND HIM!" וסיום המשחק.
    End - סיום התוכנית.
    CalculateDistance - חישוב המרחק בין מיקום השחקן למיקום ההורקל.
    CalculateDirection - קביעת הכיוון להורקל (שילוב של N, S, E, W).
    OutputClue - הצגת הרמז (כיוון ומרחק) להורקל.
```
import random
import math

# 1. אתחול קואורדינטות הורקל למספרים שלמים אקראיים מ-1 עד 10
hurkleX = random.randint(1, 10)
hurkleY = random.randint(1, 10)

# 2. לולאת המשחק הראשית (כל עוד הורקל לא נמצא)
while True:
    # 2.1 בקשת קואורדינטות הניחוש מהשחקן
    try:
        userX = int(input("הזן קואורדינטת X (מ-1 עד 10): "))
        userY = int(input("הזן קואורדינטת Y (מ-1 עד 10): "))
    except ValueError:
        print("אנא הזן מספרים שלמים.")
        continue

    # אימות קלט הקואורדינטות
    if not (1 <= userX <= 10 and 1 <= userY <= 10):
            print("הקואורדינטות חייבות להיות בטווח 1 עד 10.")
            continue
    # 2.2 בדיקה האם השחקן ניחש את מיקום הורקל
    if userX == hurkleX and userY == hurkleY:
        print("YOU FOUND HIM!")
        break  # סיום המשחק, אם הורקל נמצא

    # 2.3 חישוב המרחק בין מיקום השחקן למיקום הורקל
    distanceX = userX - hurkleX
    distanceY = userY - hurkleY
    distance = math.sqrt(distanceX**2 + distanceY**2)

    # 2.4 קביעת הכיוון להורקל (שילוב של N, S, E, W)
    direction = ""
    if distanceY > 0:
        direction += "N"
    if distanceY < 0:
        direction += "S"
    if distanceX > 0:
        direction += "E"
    if distanceX < 0:
        direction += "W"

    # 2.5 הדפסת הרמז (כיוון ומרחק) להורקל
    print(f"{direction if direction else 'כאן'}, מרחק: {distance:.2f}")

"""
הסבר קוד התוכנה:
1.  **ייבוא המודולים `random` ו-`math`**:
   -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים.
   -   `import math`: מייבא את המודול `math`, המשמש לחישוב שורש ריבועי.
2.  **אתחול קואורדינטות ההורקל**:
    -   `hurkleX = random.randint(1, 10)`: יוצר מספר שלם אקראי בין 1 ל-10 עבור קואורדינטת X של ההורקל.
    -   `hurkleY = random.randint(1, 10)`: יוצר מספר שלם אקראי בין 1 ל-10 עבור קואורדינטת Y של ההורקל.
3.  **לולאת המשחק הראשית `while True:`**:
    -   לולאה אינסופית הנמשכת עד שהשחקן מוצא את ההורקל (כלומר, עד לביצוע הפקודה `break`).
    -   **הזנת קואורדינטות השחקן**:
        -   `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין קלט שאינו מספרים שלמים, תוצג הודעת שגיאה.
        -   `userX = int(input("הזן קואורדינטת X (מ-1 עד 10): "))`: מבקש מהשחקן את קואורדינטת X.
        -   `userY = int(input("הזן קואורדינטת Y (מ-1 עד 10): "))`: מבקש מהשחקן את קואורדינטת Y.
    -   **אימות תקינות הקלט**:
        -   `if not (1 <= userX <= 10 and 1 <= userY <= 10):`: בודק שהקואורדינטות נמצאות בטווח 1 עד 10.
        -   `print("הקואורדינטות חייבות להיות בטווח 1 עד 10.")`: מציג הודעת שגיאה אם הקואורדינטות אינן חוקיות.
        -   `continue`: עובר לאיטרציה הבאה של הלולאה.
    -   **בדיקה האם השחקן ניחש את מיקום ההורקל**:
        -   `if userX == hurkleX and userY == hurkleY:`: בודק האם קואורדינטות השחקן וההורקל תואמות.
        -   `print("YOU FOUND HIM!")`: מציג הודעת ניצחון.
        -   `break`: מסיים את הלולאה (ואת המשחק), אם ההורקל נמצא.
    -   **חישוב המרחק**:
        -   `distanceX = userX - hurkleX`: מחשב את הפרש קואורדינטות X.
        -   `distanceY = userY - hurkleY`: מחשב את הפרש קואורדינטות Y.
        -   `distance = math.sqrt(distanceX**2 + distanceY**2)`: מחשב את המרחק באמצעות משפט פיתגורס.
    -   **קביעת כיוון**:
        -   `direction = ""`: מאתחל מחרוזת ריקה לאחסון הכיוון.
        -   `if distanceY > 0: direction += "N"`: אם הפרש Y חיובי, מוסיף "N" (צפון).
        -   `if distanceY < 0: direction += "S"`: אם הפרש Y שלילי, מוסיף "S" (דרום).
        -   `if distanceX > 0: direction += "E"`: אם הפרש X חיובי, מוסיף "E" (מזרח).
        -   `if distanceX < 0: direction += "W"`: אם הפרש X שלילי, מוסיף "W" (מערב).
    -   **הצגת רמז**:
        -   `print(f"{direction if direction else 'כאן'}, מרחק: {distance:.2f}")`: מציג את הכיוון (אם קיים, אחרת מציג "כאן") ואת המרחק להורקל.
"""