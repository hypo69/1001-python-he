"""
UGLY:
=================
מורכבות: 4
-----------------
המשחק "UGLY" הוא משחק ניחושים פשוט, בו המחשב מייצר מספר אקראי, והשחקן צריך לנחש מספר זה. לאחר כל ניסיון, השחקן מקבל משוב האם הניחוש שלו היה גבוה או נמוך מהמספר שהוגרל.

כללי המשחק:
1. המחשב מייצר מספר שלם אקראי בטווח שבין 1 ל-100.
2. השחקן מזין את ניחושו לגבי המספר שהוגרל.
3. לאחר כל ניסיון, המחשב מודיע האם המספר שהוזן היה "TOO HIGH" (גבוה מדי) או "TOO LOW" (נמוך מדי).
4. המשחק מסתיים כאשר השחקן מנחש את המספר.
-----------------
אלגוריתם:
1. יצר מספר אקראי בטווח שבין 1 ל-100 ושמור אותו במשתנה `targetNumber`.
2. התחל לולאה "עד שניחוש נכון":
    2.1 בקש מהשחקן להזין מספר ושמור אותו במשתנה `userGuess`.
    2.2 אם `userGuess` שווה ל-`targetNumber`, הצג את ההודעה "YOU GOT IT!" ועבור לשלב 3.
    2.3 אם `userGuess` קטן מ-`targetNumber`, הצג את ההודעה "TOO LOW".
    2.4 אם `userGuess` גדול מ-`targetNumber`, הצג את ההודעה "TOO HIGH".
3. סיים את המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeTargetNumber["<p align='left'>אתחול: 
    <code><b>targetNumber = random(1, 100)</b></code></p>"]
    InitializeTargetNumber --> LoopStart{"תחילת לולאה: עד שלא ניחוש נכון"}
    LoopStart --> InputGuess["קלט מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סיום"]
    CheckGuess -- לא --> CheckLow{"בדיקה: <code><b>userGuess &lt; targetNumber?</b></code>"}
    CheckLow -- כן --> OutputLow["הצגת הודעה: <b>TOO LOW</b>"]
    OutputLow --> LoopStart
    CheckLow -- לא --> OutputHigh["הצגת הודעה: <b>TOO HIGH</b>"]
    OutputHigh --> LoopStart
```
מקרא:
    Start - התחלת התוכנית.
    InitializeTargetNumber - אתחול המשתנה targetNumber במספר שלם אקראי בין 1 ל-100.
    LoopStart - תחילת הלולאה שנמשכת עד שהמספר מנוחש.
    InputGuess - בקשת קלט מהמשתמש (מספר) ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר המוזן userGuess שווה למספר שהוגרל targetNumber.
    OutputWin - הצגת הודעת ניצחון אם המספרים שווים.
    End - סיום התוכנית.
    CheckLow - בדיקה האם המספר המוזן userGuess קטן מהמספר שהוגרל targetNumber.
    OutputLow - הצגת ההודעה "TOO LOW" אם המספר המוזן קטן מהמספר שהוגרל.
    OutputHigh - הצגת ההודעה "TOO HIGH" אם המספר המוזן גדול מהמספר שהוגרל.
"""
import random

# מייצר מספר אקראי בין 1 ל-100
targetNumber = random.randint(1, 100)

# לולאה אינסופית עד שהשחקן ינחש את המספר
while True:
    # מבקש מהמשתמש להזין מספר
    try:
        userGuess = int(input("נחש מספר: "))
    except ValueError:
        print("אנא הזן מספר שלם.")
        continue

    # בודק אם המספר נוחש
    if userGuess == targetNumber:
        print("YOU GOT IT!")
        break  # מסיים את הלולאה אם המספר נוחש
    # בודק אם המספר שהוזן קטן מהמספר שהוגרל
    elif userGuess < targetNumber:
        print("TOO LOW")
    # אם הוא לא קטן ולא נוחש, משמע שהוא גדול
    else:
        print("TOO HIGH")
"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבוא את מודול `random`, המשמש לייצור מספרים אקראיים.
2.  **ייצור מספר אקראי**:
    -   `targetNumber = random.randint(1, 100)`: מייצר מספר שלם אקראי בטווח שבין 1 ל-100 ושומר אותו במשתנה `targetNumber`.
3.  **הלולאה הראשית `while True:`**:
    -   `while True:`: יוצר לולאה אינסופית שנמשכת כל עוד השחקן לא ניחש את המספר.
    -  **קלט נתונים**:
        - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין קלט שאינו מספר שלם, תוצג הודעת שגיאה.
        -   `userGuess = int(input("נחש מספר: "))`: מבקש קלט מהמשתמש (מספר) ושומר אותו במשתנה `userGuess`.
    -   **בדיקת תנאי הניצחון**:
        -   `if userGuess == targetNumber:`: בודק האם המספר שהוזן שווה למספר שהוגרל.
        -   `print("YOU GOT IT!")`: מציג את הודעת הניצחון.
        -   `break`: מסיים את הלולאה (ואת המשחק) אם המספר נוחש.
    -   **רמזים**:
        -   `elif userGuess < targetNumber:`: בודק האם המספר שהוזן קטן מהמספר שהוגרל.
        -   `print("TOO LOW")`: מציג רמז שיש להזין מספר גדול יותר.
        -   `else:`: אם המספר לא נוחש ואינו קטן מהמספר שהוגרל, הרי שהוא גדול יותר.
        -   `print("TOO HIGH")`: מציג רמז שיש להזין מספר קטן יותר.
"""