BASEBL:
=================
**רמת קושי:** 5
-----------------
המשחק "בייסבול" הוא משחק חידה שבו השחקן מנסה לנחש מספר בן ארבע ספרות שהוגרל על ידי המחשב. לאחר כל ניסיון, השחקן מקבל רמזים בדמות מספר הספרות ה"נכונות" במיקום ה"נכון" (страйк) ומספר הספרות ה"נכונות" במיקום שגוי (болл).

**חוקי המשחק:**
1.  המחשב מגריל מספר אקראי בן 4 ספרות שבו כל הספרות שונות זו מזו.
2.  השחקן מזין את הניחוש שלו למספר המוסתר.
3.  לאחר כל ניסיון, המחשב מדווח על מספר ה"страйקים" (ספרות במיקום הנכון) ומספר ה"בוללים" (ספרות שנמצאות במספר המוסתר אך במיקום שגוי).
4.  המשחק נמשך עד שהשחקן מנחש את המספר המוסתר (4 страйקים).
-----------------
**אלגוריתם:**
1.  הגרל מספר אקראי בן 4 ספרות (מטרה), שבו כל הספרות ייחודיות.
2.  הצג הודעה על תחילת המשחק.
3.  התחל לולאה, עד שהמספר ינוחש:
    3.1. בקש מהשחקן להזין מספר בן 4 ספרות.
    3.2. ודא שהמספר שהוזן הוא בן 4 ספרות; אם לא - בקש הזנה שוב.
    3.3. אתחל את מונים הстрайקים והבוללים ל-0.
    3.4. עבור כל ספרה במספר שהוזן:
        -   אם הספרה ומיקומה זהים לאלו שבמספר המטרה - הגדל את מונה הстрайקים.
        -   אם הספרה קיימת במספר המטרה, אך במיקום אחר, הגדל את מונה הבוללים.
    3.5. הצג את מספר הстрайקים והבוללים.
    3.6. אם מספר הстрайקים שווה ל-4, הצג הודעת ניצחון וסיים את המשחק.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateTargetNumber["הגרלת מספר אקראי בן 4 ספרות <code><b>targetNumber</b></code> עם ספרות ייחודיות"]
    GenerateTargetNumber --> OutputGameStartMessage["הצגת הודעה על תחילת המשחק"]
    OutputGameStartMessage --> LoopStart{"תחילת לולאה: כל עוד לא נוחש (страйקים != 4)"}
    LoopStart -- כן --> InputGuess["קלט מספר בן 4 ספרות מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> ValidateGuess{"בדיקה: <code><b>userGuess</b></code> הוא מספר בן 4 ספרות?"}
    ValidateGuess -- לא --> InputGuess
    ValidateGuess -- כן --> InitializeCounters["אתחול: <code><b>strikes = 0, balls = 0</b></code>"]
    InitializeCounters --> LoopDigits{"לולאה על כל ספרה ב-<code><b>userGuess</b></code>"}
    LoopDigits -- כן --> CheckStrike{"בדיקה: <code><b>userGuess[i] == targetNumber[i]</b></code>?"}
     CheckStrike -- כן --> IncreaseStrikes["<code><b>strikes = strikes + 1</b></code>"]
    IncreaseStrikes --> LoopDigitsNext{"הספרה הבאה ב-<code><b>userGuess</b></code>"}
     CheckStrike -- לא --> CheckBall{"בדיקה: <code><b>userGuess[i] in targetNumber</b></code>?"}
    CheckBall -- כן --> IncreaseBalls["<code><b>balls = balls + 1</b></code>"]
    IncreaseBalls --> LoopDigitsNext
    CheckBall -- לא --> LoopDigitsNext
    LoopDigitsNext --> LoopDigits{"עוד ספרות ב-<code><b>userGuess</b></code>?"}
     LoopDigits -- לא --> OutputScore["הצגה: <code><b>{strikes}</b></code> страйקים, <code><b>{balls}</b></code> בוללים"]
    OutputScore --> CheckWin{"בדיקה: <code><b>strikes == 4?</b></code>"}
     CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סיום"]
    CheckWin -- לא --> LoopStart
     LoopStart -- לא --> End

```
**מקרא**:
*   **Start** - התחלת התוכנית.
*   **GenerateTargetNumber** - הגרלת מספר אקראי בן 4 ספרות `targetNumber` עם ספרות ייחודיות.
*   **OutputGameStartMessage** - הצגת הודעה על תחילת המשחק.
*   **LoopStart** - תחילת לולאה שנמשכת כל עוד המספר לא נוחש (מספר הстрайקים אינו שווה ל-4).
*   **InputGuess** - בקשת מספר בן 4 ספרות מהמשתמש ושמירתו ב-`userGuess`.
*   **ValidateGuess** - בדיקה האם המספר שהוזן `userGuess` הוא בן 4 ספרות. אם לא, מתבצעת בקשה חוזרת להזנה `InputGuess`.
*   **InitializeCounters** - אתחול מוני הстрайקים (`strikes`) והבוללים (`balls`) ל-0.
*   **LoopDigits** - תחילת לולאה שעוברת על כל ספרה ב-`userGuess`.
*   **CheckStrike** - בדיקה האם הספרה ומיקומה ב-`userGuess` זהים לאלו שב-`targetNumber`.
*   **IncreaseStrikes** - הגדלת מונה הстрайקים ב-1, אם יש התאמה.
*   **CheckBall** - בדיקה האם הספרה מ-`userGuess` קיימת ב-`targetNumber` , אך במיקום אחר.
*   **IncreaseBalls** - הגדלת מונה הבוללים ב-1, אם הספרה קיימת, אך במיקום אחר.
*   **LoopDigitsNext** - מעבר לספרה הבאה.
*   **OutputScore** - הצגת מספר הстрайקים והבוללים.
*   **CheckWin** - בדיקה האם מספר הстрайקים שווה ל-4 (ניצחון).
*   **OutputWin** - הצגת הודעה על ניצחון, אם מספר הстрайקים שווה ל-4.
*   **End** - סיום התוכנית.

"""
import random

def generate_target_number():
    """מגריל מספר אקראי בן 4 ספרות עם ספרות ייחודיות."""
    digits = list(range(10)) # יוצר רשימה של ספרות מ-0 עד 9
    random.shuffle(digits)  # מערבב את הספרות באופן אקראי
    # לוקח את 4 הספרות הראשונות וממיר אותן למחרוזת
    return "".join(map(str, digits[:4]))


def get_user_guess():
    """מבקש מהמשתמש להזין מספר בן 4 ספרות ובודק את תקינותו."""
    while True:
        guess = input("Введите 4-значное число: ") # מבקש הזנה של מספר בן 4 ספרות
        if len(guess) == 4 and guess.isdigit(): # בודק שהקלט מורכב מ-4 ספרות
            return guess
        else:
            print("Некорректный ввод. Пожалуйста, введите 4-значное число.")


def calculate_score(target, guess):
    """מחשב את מספר הстрайקים והבוללים."""
    strikes = 0  # מאתחל את מונה הстрайקים
    balls = 0  # מאתחל את מונה הבוללים
    for i in range(4):
        if guess[i] == target[i]:
            strikes += 1  # מגדיל страйק אם הספרות והמיקומים זהים
        elif guess[i] in target:
            balls += 1  # מגדיל בולל אם הספרה קיימת, אך לא במיקומה
    return strikes, balls


# לוגיקת המשחק הראשית
def play_baseball():
    """מפעיל את המשחק "בייסבול"."""
    target_number = generate_target_number() # מגריל את המספר המוסתר
    print("Добро пожаловать в игру Бейсбол!") # מציג הודעת קבלת פנים
    print("Я загадал 4-значное число. Попробуй угадать его.") # מיידע על המשימה

    while True: # מתחיל לולאה אינסופית
        user_guess = get_user_guess() # מקבל את קלט המשתמש
        strikes, balls = calculate_score(target_number, user_guess) # מחשב страйקים ובוללים

        print(f"{strikes} страйков, {balls} боллов") # מציג את התוצאה
        if strikes == 4:
            print("ПОЗДРАВЛЯЮ! Вы угадали число!") # ברכה וסיום המשחק
            break

if __name__ == "__main__":
    play_baseball() # מפעיל את המשחק

"""
**הסבר על הקוד:**

1.  **ייבוא מודול `random`:**
    -   `import random`: מייבא את המודול להגרלת מספרים אקראיים.

2.  **פונקציה `generate_target_number()`:**
    -   `digits = list(range(10))`: יוצר רשימה של ספרות מ-0 עד 9.
    -   `random.shuffle(digits)`: מערבב את הספרות באופן אקראי.
    -   `return "".join(map(str, digits[:4]))`: לוקח את 4 הספרות הראשונות מהרשימה המעורבבת, ממיר אותן למחרוזות ומאחד אותן למחרוזת אחת, שמוחזרת כמספר המוסתר.

3.  **פונקציה `get_user_guess()`:**
    -   `while True:`: מפעיל לולאה אינסופית עד שהמשתמש יזין מספר תקין.
    -   `guess = input("Введите 4-значное число: ")`: מבקש מהמשתמש להזין מספר בן 4 ספרות.
    -   `if len(guess) == 4 and guess.isdigit()`: בודק האם אורך הקלט הוא 4 תווים והאם הוא מורכב מספרות בלבד.
    -   `return guess`: מחזיר את המספר שהוזן, אם הוא תקין.
    -   `else`: אם הקלט אינו תקין, מציג הודעת שגיאה.

4.  **פונקציה `calculate_score(target, guess)`:**
    -   `strikes = 0` ו-`balls = 0`: מאתחל את מוני הстрайקים והבוללים.
    -   `for i in range(4)`: עובר על כל ספרה במספר שהוזן.
    -   `if guess[i] == target[i]`: בודק האם הספרה ומיקומה זהים. אם כן, מגדיל את מונה הстрайקים.
    -   `elif guess[i] in target`: בודק האם הספרה מהמספר שהוזן קיימת במספר המוסתר, אך במיקום אחר. אם כן, מגדיל את מונה הבוללים.
    -   `return strikes, balls`: מחזיר את מספר הстрайקים והבוללים.

5.  **פונקציה `play_baseball()`:**
    -   `target_number = generate_target_number()`: מגריל את המספר המוסתר.
    -   `print("Добро пожаловать в игру Бейсбол!")` ו-`print("Я загадал 4-значное число. Попробуй угадать его.")`: מציגים הודעת קבלת פנים וחוקי משחק.
    -   `while True:`: לולאת המשחק הראשית.
    -   `user_guess = get_user_guess()`: מקבל קלט מהמשתמש.
    -   `strikes, balls = calculate_score(target_number, user_guess)`: מחשב страйקים ובוללים.
    -   `print(f"{strikes} страйков, {balls} боллов")`: מציג את תוצאת הניסיון הנוכחי.
    -   `if strikes == 4:`: בודק אם המספר נוחש.
    -   `print("ПОЗДРАВЛЯЮ! Вы угадали число!")` ו-`break`: מציג הודעת ניצחון ומסיים את הלולאה.

6.  **תנאי `if __name__ == "__main__":`:**
    -   `if __name__ == "__main__":`: מוודא שפונקציית `play_baseball()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    -   `play_baseball()`: קורא לפונקציה כדי להתחיל את המשחק.
"""