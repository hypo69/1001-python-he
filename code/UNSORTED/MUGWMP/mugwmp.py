MUGWMP:
=================
רמת קושי: 4
-----------------
המשחק "MUGWMP" הוא משחק טקסט שבו השחקן מנחש מספר בן ארבע ספרות שנוצר על ידי המחשב. לאחר כל ניסיון, השחקן מקבל רמזים בצורת מספר הספרות שנוחשו נכונה ובמקומן הנכון (MUG) ומספר הספרות שנוחשו נכונה אך אינן במקומן הנכון (WMP). המטרה היא לנחש את המספר במספר המינימלי של ניסיונות.

כללי המשחק:
1.  המחשב מייצר מספר ארבע-ספרתי אקראי שבו כל הספרות ייחודיות.
2.  השחקן מזין את השערותיו בנות ארבע הספרות.
3.  לאחר כל ניסיון, המחשב מדווח על מספר ה-"MUG" (ספרות נכונות במקומות נכונים) ועל מספר ה-"WMP" (ספרות נכונות במקומות שאינם נכונים).
4.  המשחק ממשיך עד שהשחקן מנחש את המספר.

-----------------
אלגוריתם:
1.  מייצר מספר ארבע-ספרתי אקראי שבו כל הספרות ייחודיות.
2.  מאתחל את מספר הניסיונות ל-0.
3.  מתחיל לולאה "כל עוד המספר לא נוחש":
    3.1.  מגדיל את מספר הניסיונות ב-1.
    3.2.  מבקש מהשחקן מספר ארבע-ספרתי.
    3.3.  בודק האם המספר שהוזן תקין (בן ארבע ספרות ועם ספרות ייחודיות). אם לא, מציג הודעת שגיאה ומבקש קלט מחדש.
    3.4.  אם המספר שהוזן תואם למספר הסודי, עובר לשלב 4.
    3.5.  סופר את כמות ה-MUG (ספרות במקומן הנכון) ואת כמות ה-WMP (ספרות שאינן במקומן הנכון).
    3.6.  מציג רמז בפורמט "MUG = X, WMP = Y".
4.  מציג הודעה "YOU GOT IT IN {מספר הניסיונות} GUESSES!"
5.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateSecretNumber["<p align='left'>יצירת מספר סודי בן 4 ספרות
    <code><b>secretNumber</b></code></p>"]
    GenerateSecretNumber --> InitializeAttempts["<code><b>numberOfGuesses = 0</b></code>"]
    InitializeAttempts --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מספר בן 4 ספרות: <code><b>userGuess</b></code>"]
    InputGuess --> ValidateGuess["<p align='left'>בדיקת תקינות קלט:
    <code><b>len(userGuess) == 4 &amp;&amp; unique(userGuess)</b></code></p>"]
    ValidateGuess -- לא --> InputError["הצגת הודעת שגיאת קלט"]
    InputError --> InputGuess
    ValidateGuess -- כן --> CheckWin["בדיקה: <code><b>userGuess == secretNumber</b></code>?"]
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> CalculateMugWmp["<p align='left'>חישוב MUG (התאמות במיקום) ו-WMP (התאמות שאינן במיקום):
    <code><b>mug = countMug(userGuess, secretNumber)
    wmp = countWmp(userGuess, secretNumber)</b></code></p>"]
    CalculateMugWmp --> OutputMugWmp["הצגה: <b>MUG = <code>{mug}</code>, WMP = <code>{wmp}</code></b>"]
    OutputMugWmp --> LoopStart
    LoopStart -- לא --> End
```
מקרא:
    Start - תחילת התוכנית.
    GenerateSecretNumber - יצירת מספר סודי ארבע-ספרתי עם ספרות ייחודיות.
    InitializeAttempts - אתחול מונה כמות הניסיונות (numberOfGuesses) ל-0.
    LoopStart - תחילת הלולאה שנמשכת עד שהמספר נוחש.
    IncreaseGuesses - הגדלת מונה כמות הניסיונות ב-1.
    InputGuess - בקשת קלט של מספר ארבע-ספרתי מהמשתמש.
    ValidateGuess - בדיקת תקינות המספר שהוזן (4 תווים, כל הספרות ייחודיות).
    InputError - הצגת הודעת שגיאת קלט, אם הנתונים שהוזנו אינם תקינים.
    CheckWin - בדיקה האם המספר שהוזן תואם למספר הסודי.
    OutputWin - הצגת הודעת ניצחון, אם המספרים תואמים, עם ציון כמות הניסיונות.
    End - סוף התוכנית.
    CalculateMugWmp - חישוב כמות ה-MUG (התאמות במיקומן הנכון) וכמות ה-WMP (התאמות שאינן במיקומן הנכון).
    OutputMugWmp - הצגת רמזי MUG ו-WMP.
"""
import random

def generate_secret_number():
    """מייצר מספר ארבע-ספרתי אקראי עם ספרות ייחודיות."""
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def count_mug_wmp(secret, guess):
    """
    מחשב את כמות ה-MUG (התאמות במיקומן הנכון) ואת כמות ה-WMP (התאמות שאינן במיקומן הנכון).

    Args:
    secret (str): המספר הסודי.
    guess (str): ההשערה של השחקן.

    Returns:
    tuple: טאפל המכיל את כמות ה-MUG ואת כמות ה-WMP.
    """
    mug = 0
    wmp = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            mug += 1
        elif guess[i] in secret:
            wmp += 1
    return mug, wmp

# 1. מייצרים מספר ארבע-ספרתי אקראי עם ספרות ייחודיות
secret_number = generate_secret_number()

# 2. מאתחלים את מונה הניסיונות
number_of_guesses = 0

# 3. לולאת המשחק הראשית
while True:
    # 3.1. מגדילים את מונה הניסיונות
    number_of_guesses += 1

    # 3.2. מבקשים קלט מספר מהמשתמש
    while True:
        user_guess = input("הכנס מספר ארבע-ספרתי עם ספרות ייחודיות: ")

        # 3.3. בודקים את תקינות הקלט
        if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:
            print("שגיאת קלט. נא להכניס מספר ארבע-ספרתי תקין עם ספרות ייחודיות.")
        else:
            break

    # 3.4. בודקים האם המספר נוחש
    if user_guess == secret_number:
        print(f"מזל טוב! ניחשת את המספר ב- {number_of_guesses} ניסיונות!")
        break  # מסיימים את הלולאה אם המספר נוחש

    # 3.5. סופרים MUG ו-WMP
    mug, wmp = count_mug_wmp(secret_number, user_guess)

    # 3.6. מציגים את הרמז
    print(f"MUG = {mug}, WMP = {wmp}")

"""
הסבר על הקוד:
1.  **ייבוא מודול `random`**:
    - `import random`: מייבא את מודול `random`, המשמש ליצירת מספר אקראי.

2.  **פונקציה `generate_secret_number()`**:
    -  `def generate_secret_number():`: מגדיר פונקציה ליצירת מספר סודי ארבע-ספרתי עם ספרות ייחודיות.
    -  `digits = list(range(10))`: יוצר רשימה של ספרות מ-0 עד 9.
    -  `random.shuffle(digits)`: מערבב את הספרות באופן אקראי.
    -  `return "".join(map(str, digits[:4]))`: מחזיר מחרוזת מארבע הספרות הראשונות המעורבבות, ויוצר מספר ארבע-ספרתי.

3.  **פונקציה `count_mug_wmp(secret, guess)`**:
    - `def count_mug_wmp(secret, guess):`: מגדיר פונקציה לחישוב MUG ו-WMP.
    - `mug = 0`, `wmp = 0`: מאתחל את מוני ה-MUG וה-WMP.
    - `for i in range(len(secret)):`: עובר בלולאה על ספרות המספר הסודי.
        - `if secret[i] == guess[i]:`: אם הספרה במיקום הנוכחי זהה, מגדיל את מונה ה-MUG.
        - `elif guess[i] in secret:`: אם הספרה מההשערה קיימת במספר הסודי, אך אינה במיקומה הנוכחי, מגדיל את מונה ה-WMP.
    - `return mug, wmp`: מחזיר טאפל עם MUG ו-WMP.

4.  **החלק העיקרי של התוכנית**:
   - `secret_number = generate_secret_number()`: מייצר את המספר הסודי באמצעות הפונקציה `generate_secret_number()`.
    - `number_of_guesses = 0`: מאתחל את מונה הניסיונות.
    - `while True:`: מתחיל לולאה אינסופית, עד שהשחקן ינחש את המספר.
        - `number_of_guesses += 1`: מגדיל את מונה הניסיונות.
        - `while True:`: לולאה פנימית לבדיקת קלט המשתמש.
            - `user_guess = input("הכנס מספר ארבע-ספרתי עם ספרות ייחודיות: ")`: מבקש קלט מהמשתמש.
            - `if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:`: בודק את הקלט על תקינותו (ארבע ספרות, כל הספרות ייחודיות).
            - `else: break`: אם הקלט תקין, יוצא מהלולאה הפנימית.
        - `if user_guess == secret_number:`: בודק האם המספר נוחש.
            - `print(f"מזל טוב! ניחשת את המספר ב- {number_of_guesses} ניסיונות!")`: מציג הודעת ניצחון.
            - `break`: יוצא מהלולאה הראשית.
        - `mug, wmp = count_mug_wmp(secret_number, user_guess)`: קורא לפונקציה `count_mug_wmp` לחישוב MUG ו-WMP.
        - `print(f"MUG = {mug}, WMP = {wmp}")`: מציג את הרמז עם MUG ו-WMP.

"""