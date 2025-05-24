"""
SPLAT:
=================
דרגת קושי: 3
-----------------
המשחק "SPLAT" מדמה מצב בו על השחקן לנחש את נקודת הנפילה של "טיפה" על ציר מספרים מ-0 עד 100. השחקן מזין את השערותיו, והמשחק מדווח עד כמה ההשערה קרובה למטרה, תוך שימוש במונחים "Far Out", "Close", או "SPLAT!!!" במקרה של פגיעה מדויקת.

כללי המשחק:
1. המחשב מייצר מספר שלם אקראי מ-0 עד 100, המשמש כמטרה.
2. השחקן מזין את השערתו לגבי מיקום הטיפה על ציר המספרים.
3. אם ההשערה נמצאת במרחק של 10 יחידות או יותר מהמטרה, מוצגת ההודעה "Far Out".
4. אם ההשערה נמצאת במרחק של פחות מ-10 יחידות מהמטרה, מוצגת ההודעה "Close".
5. אם ההשערה תואמת בדיוק את המטרה, מוצגת ההודעה "SPLAT!!!" והמשחק מסתיים.
6. המשחק נמשך עד שהשחקן מנחש את המיקום המדויק של הטיפה.
-----------------
אלגוריתם:
1. ייצור מספר שלם אקראי בטווח שבין 0 ל-100 והקצאתו למשתנה targetNumber.
2. התחלת לולאה "עד לניחוש נכון":
    2.1 בקשת קלט מספר מהשחקן (userGuess).
    2.2 חישוב הערך המוחלט של ההפרש בין userGuess ל-targetNumber והקצאתו למשתנה distance.
    2.3 אם distance שווה ל-0, הצגת ההודעה "SPLAT!!!" וסיום המשחק.
    2.4 אם distance גדול או שווה ל-10, הצגת ההודעה "Far Out".
    2.5 אם distance קטן מ-10, הצגת ההודעה "Close".
3. חזרה לשלב 2.
-----------------
בלוק-סכמה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeTarget["<p align='left'>התחלה: 
    <code><b>
    targetNumber = random(0, 100)
    </b></code></p>"]
    InitializeTarget --> LoopStart{"תחילת לולאה: עד לניחוש נכון"}
    LoopStart --> InputGuess["קלט מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CalculateDistance["<code><b>distance = abs(userGuess - targetNumber)</b></code>"]
    CalculateDistance --> CheckSplat{"בדיקה: <code><b>distance == 0?</b></code>"}
    CheckSplat -- כן --> OutputSplat["פלט: <b>SPLAT!!!</b>"]
    OutputSplat --> End["סיום"]
    CheckSplat -- לא --> CheckFarOut{"בדיקה: <code><b>distance &gt;= 10?</b></code>"}
    CheckFarOut -- כן --> OutputFarOut["פלט: <b>Far Out</b>"]
    OutputFarOut --> LoopStart
    CheckFarOut -- לא --> OutputClose["פלט: <b>Close</b>"]
    OutputClose --> LoopStart
    
```
מקרא:
    Start - התחלת התוכנית.
    InitializeTarget - אתחול: מספר אקראי בין 0 ל-100 נוצר ומוקצה למשתנה targetNumber.
    LoopStart - התחלת הלולאה, הנמשכת עד שהשחקן מנחש את המספר (distance לא הופך ל-0).
    InputGuess - בקשת קלט מספר מהמשתמש (מיקום הנפילה המשוער) ושמירתו במשתנה userGuess.
    CalculateDistance - חישוב הערך המוחלט של ההפרש בין המספר שהוכנס userGuess למספר המטרה targetNumber, התוצאה נשמרת במשתנה distance.
    CheckSplat - בדיקה האם distance שווה ל-0.
    OutputSplat - הצגת ההודעה "SPLAT!!!" במקרה ש-distance שווה ל-0.
    End - סיום התוכנית.
    CheckFarOut - בדיקה האם distance גדול או שווה ל-10.
    OutputFarOut - הצגת ההודעה "Far Out", אם distance גדול או שווה ל-10.
    OutputClose - הצגת ההודעה "Close", אם distance קטן מ-10 ואינו שווה ל-0.
"""
import random

# מייצר מספר אקראי בין 0 ל-100
targetNumber = random.randint(0, 100)

# לולאה אינסופית עד שהשחקן ינחש את המספר
while True:
    # מבקש קלט מספר מהמשתמש
    try:
        userGuess = int(input("Введите ваше предположение (от 0 до 100): "))
    except ValueError:
        print("אנא הכנס מספר שלם.")
        continue
    
    # מחשב את המרחק בין המספר שהוכנס למספר המטרה
    distance = abs(userGuess - targetNumber)

    # בודק אם המספר נוחש
    if distance == 0:
        print("SPLAT!!!")
        break  # מסיים את הלולאה אם המספר נוחש
    elif distance >= 10:
        print("Far Out")  # מודיע שהמספר רחוק מהמטרה
    else:
        print("Close")  # מודיע שהמספר קרוב למטרה

"""
הסבר קוד:
1.  **ייבוא המודול `random`**:
   -   `import random`: מייבא את המודול `random`, המשמש לייצור מספרים אקראיים.
2.  **ייצור מספר אקראי**:
   -   `targetNumber = random.randint(0, 100)`: מייצר מספר שלם אקראי בטווח שבין 0 ל-100 (כולל) ושומר אותו במשתנה `targetNumber`. מספר זה יהיה "נקודת הנפילה של הטיפה".
3.  **לולאת המשחק הראשית `while True:`**:
   -   לולאה זו תתבצע עד שהשחקן ינחש את המספר.
4.  **קלט נתונים**:
    -   `try...except ValueError`: בלוק `try-except` מטפל בשגיאות קלט אפשריות. אם המשתמש יכניס קלט שאינו מספר שלם, תוצג הודעת שגיאה.
    -   `userGuess = int(input("Введите ваше предположение (от 0 до 100): "))`: מבקש מהמשתמש מספר וממיר אותו למספר שלם, שומר את התוצאה ב-`userGuess`. זוהי השערת השחקן לנקודת הנפילה של הטיפה.
5.  **חישוב המרחק**:
    -   `distance = abs(userGuess - targetNumber)`: מחשב את הערך המוחלט של ההפרש בין המספר שהוכנס `userGuess` למספר המטרה `targetNumber`. זהו המרחק בין השערת השחקן לנקודת הנפילה בפועל של הטיפה.
6.  **בדיקה על פגיעה**:
   -   `if distance == 0:`: בודק האם המרחק שווה לאפס. אם כן, משמע שהשחקן ניחש את נקודת הנפילה המדויקת.
    - `print("SPLAT!!!")`: מציג את ההודעה "SPLAT!!!", כאשר השחקן ניחש נכון.
    - `break`: מסיים את הלולאה כאשר השחקן ניחש נכון.
7. **בדיקת מרחק**
    - `elif distance >= 10:`: בודק האם המרחק גדול או שווה ל-10.
    - `print("Far Out")`: מציג את ההודעה "Far Out", כאשר השחקן רחוק מהמטרה.
    - `else:`: אם המרחק קטן מ-10, אז:
    - `print("Close")`: מציג את ההודעה "Close", כאשר השחקן קרוב למטרה.
"""