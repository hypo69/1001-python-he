**BASEBL:**
=================
רמת קושי: 5
-----------------
המשחק "בייסבול" הוא משחק פאזל שבו השחקן מנסה לנחש מספר בן ארבע ספרות, שנוצר על ידי המחשב. לאחר כל ניסיון, השחקן מקבל רמזים בצורת כמות ספרות "נכונות" במיקום "נכון" (סטרייק) וכמות ספרות "נכונות" במיקום לא נכון (בול).

**כללי המשחק:**
1.  המחשב מייצר מספר אקראי בן 4 ספרות, שבו כל הספרות שונות.
2.  השחקן מזין את ניחושיו לגבי המספר הנעלם.
3.  לאחר כל ניסיון, המחשב מדווח על כמות ה"סטרייקים" (ספרות במיקום הנכון) ועל כמות ה"בולים" (ספרות הקיימות במספר הנעלם, אך במיקום לא נכון).
4.  המשחק נמשך עד אשר השחקן ינחש נכון את המספר הנעלם (4 סטרייקים).
-----------------
**אלגוריתם:**
1.  הגרלת מספר אקראי בן 4 ספרות (מספר יעד), שבו כל הספרות ייחודיות.
2.  הצגת הודעה על תחילת המשחק.
3.  התחלת לולאה, כל עוד לא נוחש המספר:
    3.1. קבלת קלט מספר בן 4 ספרות מהשחקן.
    3.2. בדיקה האם המספר שהוזן הוא בן 4 ספרות, אם לא - לבקש קלט שוב.
    3.3. אתחול מוני הסטרייקים והבולים ב-0.
    3.4. עבור כל ספרה במספר שהוזן:
        -   אם הספרה ומיקומה תואמים למספר היעד - להגדיל את מונה הסטרייקים.
        -   אם הספרה קיימת במספר היעד, אך במיקום אחר, להגדיל את מונה הבולים.
    3.5. הצגת כמות הסטרייקים והבולים.
    3.6. אם כמות הסטרייקים שווה ל-4, להציג הודעה על ניצחון וסיום המשחק.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateTargetNumber["הגרלת מספר אקראי בן 4 ספרות <code><b>targetNumber</b></code> עם ספרות ייחודיות"]
    GenerateTargetNumber --> OutputGameStartMessage["הצגת הודעה על תחילת המשחק"]
    OutputGameStartMessage --> LoopStart{"תחילת לולאה: כל עוד לא נוחש (סטרייקים != 4)"}
    LoopStart -- כן --> InputGuess["קלט מספר בן 4 ספרות מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> ValidateGuess{"בדיקה: האם <code><b>userGuess</b></code> הוא מספר בן 4 ספרות?"}
    ValidateGuess -- לא --> InputGuess
    ValidateGuess -- כן --> InitializeCounters["אתחול: <code><b>strikes = 0, balls = 0</b></code>"]
    InitializeCounters --> LoopDigits{"לולאה על כל ספרה ב-<code><b>userGuess</b></code>"}
    LoopDigits -- כן --> CheckStrike{"בדיקה: האם <code><b>userGuess[i] == targetNumber[i]</b></code>?"}
     CheckStrike -- כן --> IncreaseStrikes["<code><b>strikes = strikes + 1</b></code>"]
    IncreaseStrikes --> LoopDigitsNext{"הספרה הבאה ב-<code><b>userGuess</b></code>"}
     CheckStrike -- לא --> CheckBall{"בדיקה: האם <code><b>userGuess[i] in targetNumber</b></code>?"}
    CheckBall -- כן --> IncreaseBalls["<code><b>balls = balls + 1</b></code>"]
    IncreaseBalls --> LoopDigitsNext
    CheckBall -- לא --> LoopDigitsNext
    LoopDigitsNext --> LoopDigits{"האם יש ספרות נוספות ב-<code><b>userGuess</b></code>?"}
     LoopDigits -- לא --> OutputScore["הצגה: <code><b>{strikes}</b></code> סטרייקים, <code><b>{balls}</b></code> בולים"]
    OutputScore --> CheckWin{"בדיקה: האם <code><b>strikes == 4?</b></code>"}
     CheckWin -- כן --> OutputWin["הצגת הודעה: <b>ניצחת!</b>"]
    OutputWin --> End["סיום"]
    CheckWin -- לא --> LoopStart
     LoopStart -- לא --> End

```
**מקרא**:
*   **Start** - התחלת התוכנית.
*   **GenerateTargetNumber** - הגרלת מספר אקראי בן 4 ספרות `targetNumber` עם ספרות ייחודיות.
*   **OutputGameStartMessage** - הצגת הודעה על תחילת המשחק.
*   **LoopStart** - תחילת לולאה שנמשכת כל עוד המספר לא נוחש (כמות הסטרייקים אינה שווה ל-4).
*   **InputGuess** - בקשת קלט מספר בן 4 ספרות מהמשתמש ושמירתו ב-`userGuess`.
*  **ValidateGuess** - בדיקה האם המספר שהוזן `userGuess` הוא בן 4 ספרות. אם לא, מתבצעת בקשת קלט חוזרת `InputGuess`.
*   **InitializeCounters** - אתחול מוני הסטרייקים (`strikes`) והבולים (`balls`) ל-0.
*   **LoopDigits** - תחילת לולאה שעוברת על כל ספרה ב-`userGuess`.
*   **CheckStrike** - בדיקה האם הספרה ומיקומה ב-`userGuess` תואמים ל-`targetNumber`.
*   **IncreaseStrikes** - הגדלת מונה הסטרייקים ב-1, אם קיימת התאמה.
*  **CheckBall** - בדיקה האם הספרה מתוך `userGuess` קיימת ב-`targetNumber`, אך במיקום אחר.
*   **IncreaseBalls** - הגדלת מונה הבולים ב-1, אם הספרה קיימת, אך במיקום אחר.
*  **LoopDigitsNext** - מעבר לספרה הבאה.
*   **OutputScore** - הצגת כמות הסטרייקים והבולים.
*   **CheckWin** - בדיקה האם כמות הסטרייקים שווה ל-4 (ניצחון).
*   **OutputWin** - הצגת הודעה על ניצחון, אם כמות הסטרייקים שווה ל-4.
*   **End** - סיום התוכנית.

"""
import random

def generate_target_number():
    """מייצר מספר אקראי בן 4 ספרות עם ספרות ייחודיות."""
    digits = list(range(10)) # יצירת רשימת ספרות מ-0 עד 9
    random.shuffle(digits)  # ערבוב הספרות באופן אקראי
    # לקיחת 4 הספרות הראשונות והמרתן למחרוזת
    return "".join(map(str, digits[:4]))


def get_user_guess():
    """מבקש קלט מספר בן 4 ספרות מהמשתמש ובודק את תקינותו."""
    while True:
        guess = input("Введите 4-значное число: ") # בקשת קלט מספר בן 4 ספרות
        if len(guess) == 4 and guess.isdigit(): # בדיקה שהקלט מורכב מ-4 ספרות בלבד
            return guess
        else:
            print("קלט לא תקין. אנא הזן מספר בן 4 ספרות.")


def calculate_score(target, guess):
    """מחליש את כמות הסטרייקים והבולים."""
    strikes = 0  # אתחול מונה הסטרייקים
    balls = 0  # אתחול מונה הבולים
    for i in range(4):
        if guess[i] == target[i]:
            strikes += 1  # הגדלת מונה הסטרייקים אם הספרה והמיקום תואמים
        elif guess[i] in target:
            balls += 1  # הגדלת מונה הבולים אם הספרה קיימת במספר היעד, אך במיקום לא נכון
    return strikes, balls


# Основная логика игры
def play_baseball():
    """מפעיל את המשחק "בייסבול"."""
    target_number = generate_target_number() # הגרלת המספר הנעלם
    print("Добро пожаловать в игру Бейсбол!") # הצגת הודעת פתיחה
    print("Я загадал 4-значное число. Попробуй угадать его.") # הודעה על מטרת המשחק

    while True: # התחלת לולאת המשחק הראשית
        user_guess = get_user_guess() # קבלת קלט מהמשתמש
        strikes, balls = calculate_score(target_number, user_guess) # חישוב כמות הסטרייקים והבולים

        print(f"{strikes} страйков, {balls} боллов") # הצגת תוצאת הניסיון הנוכחי
        if strikes == 4: # בדיקה האם המספר נוחש
            print("ПОЗДРАВЛЯЮ! Вы угадали число!") # הצגת הודעת ניצחון וסיום המשחק
            break

if __name__ == "__main__":
    play_baseball() # הפעלת המשחק

"""
**הסבר על הקוד:**

1.  **ייבוא המודול `random`:**
    -   `import random`: מייבא את המודול ליצירת מספרים אקראיים.

2.  **הפונקציה `generate_target_number()`:**
    -   `digits = list(range(10))`: יוצרת רשימה של ספרות מ-0 עד 9.
    -   `random.shuffle(digits)`: מערבבת את הספרות באופן אקראי.
    -   `return "".join(map(str, digits[:4]))`: לוקחת את 4 הספרות הראשונות מהרשימה המעורבבת, ממירה אותן למחרוזות ומאחדת אותן למחרוזת אחת, אשר מוחזרת כמספר הנעלם.

3.  **הפונקציה `get_user_guess()`:**
    -   `while True:`: מפעילה לולאה אינסופית עד שהמשתמש מזין מספר תקין.
    -   `guess = input("Введите 4-значное число: ")`: מבקשת קלט מספר בן 4 ספרות מהמשתמש.
    -   `if len(guess) == 4 and guess.isdigit()`: בודקת האם אורך הקלט הוא 4 תווים והאם הוא מורכב מספרות בלבד.
    -   `return guess`: מחזירה את המספר שהוזן, אם הוא תקין.
    -   `else`: אם הקלט לא תקין, מציגה הודעת שגיאה.

4.  **הפונקציה `calculate_score(target, guess)`:**
    -   `strikes = 0` ו-`balls = 0`: מאתחלת את מוני הסטרייקים והבולים.
    -   `for i in range(4)`: עוברת על כל ספרה במספר שהוזן.
    -   `if guess[i] == target[i]`: בודקת האם הספרה ומיקומה תואמים. אם כן, מגדילה את מונה הסטרייקים.
    -   `elif guess[i] in target`: בודקת האם הספרה מהמספר שהוזן קיימת במספר הנעלם, אך במיקום אחר. אם כן, מגדילה את מונה הבולים.
    -   `return strikes, balls`: מחזירה את כמות הסטרייקים והבולים.

5.  **הפונקציה `play_baseball()`:**
    -   `target_number = generate_target_number()`: מייצרת/מגרילה את המספר הנעלם.
    -   `print("Добро пожаловать в игру Бейсбол!")` ו-`print("Я загадал 4-значное число. Попробуй угадать его.")`: מציגות הודעת פתיחה והודעה על מטרת המשחק.
    -   `while True:`: לולאת המשחק הראשית.
    -   `user_guess = get_user_guess()`: מקבלת קלט מהמשתמש.
    -   `strikes, balls = calculate_score(target_number, user_guess)`: מחלישה את כמות הסטרייקים והבולים.
    -   `print(f"{strikes} страйков, {balls} боллов")`: מציגה את תוצאת הניסיון הנוכחי.
    -   `if strikes == 4:`: בודקת האם המספר נוחש.
    -   `print("ПОЗДРАВЛЯЮ! Вы угадали число!")` ו-`break`: מציגה הודעה על ניצחון ומסיימת את הלולאה.

6.  **התנאי `if __name__ == "__main__":`:**
    -   `if __name__ == "__main__":`: מבטיח שהפונקציה `play_baseball()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    -   `play_baseball()`: קוראת לפונקציה להפעלת המשחק.
"""