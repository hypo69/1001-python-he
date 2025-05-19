<BULL>:
=================
מורכבות: 4
-----------------
המשחק "BULL" הוא משחק לוגי מספרי שבו המחשב מייצר מספר אקראי בן ארבע ספרות, שכל ספרותיו שונות, והשחקן מנסה לנחש את המספר הזה. לאחר כל ניסיון, המחשב מדווח על מספר "שורות" (ספרה נוחשה ונמצאת במקום הנכון) ו"פרות" (ספרה נוחשה אך נמצאת במקום שגוי).

כללי המשחק:
1. המחשב מייצר מספר אקראי בן ארבע ספרות, שכל ספרותיו שונות.
2. השחקן מנסה לנחש את המספר על ידי הכנסת מספרים משלו בני ארבע ספרות.
3. לאחר כל ניסיון, המחשב מציג את מספר ה"שורות" וה"פרות".
   - "שור" - הוא ספרה שנוחשה ונמצאת במיקום הנכון.
   - "פרה" - היא ספרה שנוחשה אך נמצאת במיקום שגוי.
4. המשחק נמשך עד שהשחקן מנחש את המספר (כלומר, מקבל 4 "שורות").
-----------------
אלגוריתם:
1. יצירת מספר אקראי בן ארבע ספרות עם ספרות שונות.
2. התחלת לולאה "כל עוד מספר השורות אינו שווה ל-4":
   2.1 בקשת קלט מספר בן ארבע ספרות מהשחקן.
   2.2 בדיקת תקינות המספר שהוכנס (4 ספרות).
   2.3 אתחול מוני השורות והפרות ל-0.
   2.4 עבור כל ספרה במספר שהוכנס:
        2.4.1 אם הספרה זהה לספרה במספר המטרה באותו מיקום, הגדלת מונה השורות.
        2.4.2 אחרת, אם הספרה קיימת במספר המטרה במיקום אחר, הגדלת מונה הפרות.
   2.5 הצגת מספר השורות והפרות.
3. הצגת הודעת ניצחון.
4. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateTargetNumber["<p align='left'>יצירת מספר אקראי בן 4 ספרות עם ספרות שונות:<br/><code><b>targetNumber</b></code></p>"]
    GenerateTargetNumber --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> InputGuess["קלט מספר ממשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> ValidateGuess["בדיקה: <code><b>len(userGuess) == 4?</b></code>"]
     ValidateGuess -- לא --> OutputInvalid["פלט הודעה: <b>INVALID NUMBER</b>"]
     OutputInvalid --> LoopStart
    ValidateGuess -- כן --> InitializeCounts["<p align='left'>אתחול מונים:<br/><code><b>
    bulls = 0
    cows = 0
    </b></code></p>"]
    InitializeCounts --> CheckDigits{"לולאה על ספרות <code><b>userGuess</b></code>"}
    CheckDigits --> CheckBull{"בדיקה: ספרה <code><b>userGuess[i]</b></code> == <code><b>targetNumber[i]</b></code>"}
    CheckBull -- כן --> IncreaseBulls["<code><b>bulls = bulls + 1</b></code>"]
        IncreaseBulls --> CheckNextDigit["הספרה הבאה?"]
    CheckBull -- לא --> CheckCow{"בדיקה: <code><b>userGuess[i]</b></code> ב-<code><b>targetNumber</b></code>?"}
    CheckCow -- כן --> IncreaseCows["<code><b>cows = cows + 1</b></code>"]
        IncreaseCows --> CheckNextDigit
    CheckCow -- לא --> CheckNextDigit
    CheckNextDigit -- כן --> CheckDigits
    CheckNextDigit -- לא --> OutputResult["פלט: <code><b>{bulls} Bulls, {cows} Cows</b></code>"]
    OutputResult --> CheckWin{"בדיקה: <code><b>bulls == 4?</b></code>"}
    CheckWin -- כן --> OutputWin["פלט הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סיום"]
    CheckWin -- לא --> LoopStart
    LoopStart -- לא --> End
```
מקרא:
    Start - התחלת התוכנית.
    GenerateTargetNumber - יצירת מספר אקראי בן 4 ספרות עם ספרות שונות, ושמירתו במשתנה targetNumber.
    LoopStart - תחילת הלולאה, אשר מתבצעת כל עוד מספר ה"שורות" אינו שווה ל-4.
    InputGuess - בקשת קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
    ValidateGuess - בדיקה שהמספר שהוכנס על ידי המשתמש מורכב מ-4 ספרות.
    OutputInvalid - הצגת הודעת שגיאה אם המספר שהוכנס אינו מורכב מ-4 ספרות.
    InitializeCounts - אתחול מוני bulls (שורות) ו-cows (פרות) לאפס.
    CheckDigits - תחילת לולאה למעבר על ספרות המספר שהוכנס.
    CheckBull - בדיקה האם הספרה מתוך userGuess זהה לספרה מתוך targetNumber באותו מיקום.
    IncreaseBulls - הגדלת מונה השורות ב-1.
    CheckCow - בדיקה האם הספרה מתוך userGuess קיימת ב-targetNumber, אך לא באותו מיקום.
    IncreaseCows - הגדלת מונה הפרות ב-1.
    CheckNextDigit - בדיקה האם קיימת ספרה נוספת לבדיקה, אם כן אז עובר לתחילת הלולאה, אחרת ממשיך הלאה בתרשים הזרימה.
    OutputResult - הצגת מספר ה"שורות" וה"פרות" לאחר כל ניסיון.
    CheckWin - בדיקה האם מספר ה"שורות" שווה ל-4.
    OutputWin - הצגת הודעת ניצחון אם המספר נוחש.
    End - סיום התוכנית.
```python
import random

def generate_target_number():
    """יוצר מספר אקראי בן ארבע ספרות עם ספרות ייחודיות."""
    digits = list(range(10))
    random.shuffle(digits)
    # השמטת מספרים עם אפס מוביל
    while digits[0] == 0:
        random.shuffle(digits)

    return "".join(map(str, digits[:4]))

def get_bulls_and_cows(user_guess, target_number):
    """סופר את מספר ה'שורות' וה'פרות'."""
    bulls = 0
    cows = 0
    for i, digit in enumerate(user_guess):
        if digit == target_number[i]:
            bulls += 1
        elif digit in target_number:
            cows += 1
    return bulls, cows

# יצירת מספר המטרה
target_number = generate_target_number()

# לולאת המשחק הראשית
while True:
    user_guess = input("אנא הכנס מספר בן ארבע ספרות: ")

    # בדיקת תקינות הקלט
    if not user_guess.isdigit() or len(user_guess) != 4:
        print("אנא הכנס מספר תקין בן ארבע ספרות.")
        continue

    # ספירת שורות ופרות
    bulls, cows = get_bulls_and_cows(user_guess, target_number)
    print(f"{bulls} שורות, {cows} פרות")

    # בדיקת ניצחון
    if bulls == 4:
        print("ברכות, ניחשת את המספר!")
        break

"""
הסבר הקוד:
1. **ייבוא המודול `random`**:
   - `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים.

2. **הפונקציה `generate_target_number()`**:
    -   `digits = list(range(10))`: יוצרת רשימת ספרות מ-0 עד 9.
    -   `random.shuffle(digits)`: מערבבת את הספרות בסדר אקראי.
    -   לולאת `while digits[0] == 0:`:
        -   בודקת אם הספרה הראשונה היא 0. אם כן, מערבבת את הספרות מחדש.
        -   מבטיחה שהמספר שנוצר לא יתחיל ב-0.
    -   `return "".join(map(str, digits[:4]))`: מחזירה מחרוזת המורכבת מ-4 הספרות המעורבבות הראשונות (מספר המטרה).

3.  **הפונקציה `get_bulls_and_cows(user_guess, target_number)`**:
    -   `bulls = 0` ו-`cows = 0`: מאתחלת את מוני ה"שורות" וה"פרות" לאפס.
    -   לולאת `for i, digit in enumerate(user_guess)`:
        -   עוברת על הספרות במספר שהוכנס על ידי המשתמש יחד עם האינדקסים שלהן.
        -   `if digit == target_number[i]`: בודקת אם הספרה באותה מיקום זהה במספר המטרה. אם כן, מגדילה את מונה השורות ב-1.
        -   `elif digit in target_number`: אם הספרה אינה זהה במיקום, אך קיימת במספר המטרה, מגדילה את מונה הפרות ב-1.
    -   `return bulls, cows`: מחזירה את מספר ה"שורות" וה"פרות".

4.  **החלק העיקרי של התוכנית**:
    -   `target_number = generate_target_number()`: יוצרת את מספר המטרה בן ארבע הספרות עם ספרות שונות.
    -   `while True`: לולאה אינסופית הנמשכת עד שהשחקן מנחש את המספר.
    -   `user_guess = input("אנא הכנס מספר בן ארבע ספרות: ")`: מבקשת מהמשתמש להכניס מספר בן ארבע ספרות.
    -   `if not user_guess.isdigit() or len(user_guess) != 4:`: בודקת האם הקלט תקין (מורכב מ-4 ספרות).
        -   אם הקלט אינו תקין, מציגה הודעת שגיאה ומתחילה סיבוב חדש של הלולאה.
    -   `bulls, cows = get_bulls_and_cows(user_guess, target_number)`: סופרת את מספר השורות והפרות.
    -   `print(f"{bulls} שורות, {cows} פרות")`: מציגה את מספר ה"שורות" וה"פרות".
    -   `if bulls == 4`: בודקת האם מספר השורות שווה ל-4.
        -   אם כן, מציגה הודעת ניצחון ומסיימת את הלולאה באמצעות `break`.
"""