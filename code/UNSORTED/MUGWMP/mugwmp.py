MUGWMP:
=================
קושי: 4
-----------------
המשחק "MUGWMP" הוא משחק טקסטואלי שבו השחקן מנחש מספר בן ארבע ספרות שנוצר על ידי המחשב. לאחר כל ניסיון, השחקן מקבל רמזים בצורת מספר הספרות שניחשו נכונה ובמיקומן הנכון (MUG), ומספר הספרות שניחשו נכונה אך אינן במיקומן הנכון (WMP). המטרה היא לנחש את המספר במינימום ניסיונות.

כללי המשחק:
1.  המחשב מייצר מספר אקראי בן ארבע ספרות, כאשר כל הספרות ייחודיות.
2.  השחקן מזין את הניחוש שלו, מספר בן ארבע ספרות.
3.  לאחר כל ניסיון, המחשב מדווח על מספר ה-"MUG" (ספרות נכונות במקומות נכונים) ומספר ה-"WMP" (ספרות נכונות במקומות שגויים).
4.  המשחק ממשיך עד שהשחקן מנחש את המספר.

-----------------
אלגוריתם:
1.  יצירת מספר אקראי בן ארבע ספרות, כאשר כל הספרות ייחודיות.
2.  אתחול מונה הניסיונות ל-0.
3.  התחלת לולאה "כל עוד המספר לא נוחש":
    3.1. הגדלת מונה הניסיונות ב-1.
    3.2. בקשת מספר בן ארבע ספרות מהשחקן.
    3.3. בדיקת תקינות המספר שהוזן (האם הוא בן ארבע ספרות והאם הספרות ייחודיות). אם לא, הצגת הודעת שגיאה ובקשת קלט מחדש.
    3.4. אם המספר שהוזן זהה למספר הסודי, עבור לשלב 4.
    3.5. ספירת כמות ה-MUG (ספרות במיקומן הנכון) וכמות ה-WMP (ספרות במיקומן השגוי).
    3.6. הצגת רמז בפורמט "MUG = X, WMP = Y".
4.  הצגת הודעה "YOU GOT IT IN {מספר ניסיונות} GUESSES!"
5.  סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateSecretNumber["<p align='left'>יצירת מספר סודי בן 4 ספרות 
    <code><b>secretNumber</b></code></p>"]
    GenerateSecretNumber --> InitializeAttempts["<code><b>numberOfGuesses = 0</b></code>"]
    InitializeAttempts --> LoopStart{"התחלת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מספר בן 4 ספרות: <code><b>userGuess</b></code>"]
    InputGuess --> ValidateGuess["<p align='left'>בדיקת תקינות קלט: 
    <code><b>len(userGuess) == 4 &amp;&amp; unique(userGuess)</b></code></p>"]
    ValidateGuess -- לא --> InputError["הצגת הודעת שגיאת קלט"]
    InputError --> InputGuess
    ValidateGuess -- כן --> CheckWin["בדיקה: <code><b>userGuess == secretNumber</b></code>?"]
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סיום"]
    CheckWin -- לא --> CalculateMugWmp["<p align='left'>חישוב MUG (התאמות במיקום הנכון) ו-WMP (התאמות לא במיקום הנכון):
    <code><b>mug = countMug(userGuess, secretNumber)
    wmp = countWmp(userGuess, secretNumber)</b></code></p>"]
    CalculateMugWmp --> OutputMugWmp["הצגה: <b>MUG = <code>{mug}</code>, WMP = <code>{wmp}</code></b>"]
    OutputMugWmp --> LoopStart
    LoopStart -- לא --> End
```
מקרא:
    Start - התחלת התוכנית.
    GenerateSecretNumber - יצירת מספר סודי בן ארבע ספרות עם ספרות ייחודיות.
    InitializeAttempts - אתחול מונה מספר הניסיונות (numberOfGuesses) ל-0.
    LoopStart - התחלת לולאה שנמשכת עד שהמספר נוחש.
    IncreaseGuesses - הגדלת מונה מספר הניסיונות ב-1.
    InputGuess - בקשת קלט של מספר בן ארבע ספרות מהמשתמש.
    ValidateGuess - בדיקת תקינות המספר שהוזן (4 תווים, כל הספרות ייחודיות).
    InputError - הצגת הודעת שגיאת קלט אם הנתונים שהוזנו אינם תקינים.
    CheckWin - בדיקה האם המספר שהוזן זהה למספר הסודי.
    OutputWin - הצגת הודעת ניצחון אם המספרים זהים, בציון מספר הניסיונות.
    End - סיום התוכנית.
    CalculateMugWmp - חישוב כמות ה-MUG (התאמות במיקומן הנכון) וכמות ה-WMP (התאמות במיקומן השגוי).
    OutputMugWmp - הצגת רמזי MUG ו-WMP.
"""
import random

def generate_secret_number():
    """מייצר מספר אקראי בן ארבע ספרות עם ספרות ייחודיות."""
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def count_mug_wmp(secret, guess):
    """
    סופר את כמות ה-MUG (התאמות במיקומן הנכון) ואת כמות ה-WMP (התאמות במיקומן השגוי).

    Args:
    secret (str): המספר הסודי.
    guess (str): הניחוש של השחקן.

    Returns:
    tuple: זוג ערכים המכיל את כמות ה-MUG ואת כמות ה-WMP.
    """
    mug = 0
    wmp = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            mug += 1
        elif guess[i] in secret:
            wmp += 1
    return mug, wmp

# 1. יצירת מספר אקראי בן ארבע ספרות עם ספרות ייחודיות
secret_number = generate_secret_number()

# 2. אתחול מונה הניסיונות
number_of_guesses = 0

# 3. לולאת המשחק הראשית
while True:
    # 3.1. הגדלת מונה הניסיונות
    number_of_guesses += 1

    # 3.2. בקשת קלט מספר מהמשתמש
    while True:
        user_guess = input("הזן מספר בן ארבע ספרות עם ספרות ייחודיות: ")

        # 3.3. בדיקת תקינות הקלט
        if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:
            print("שגיאת קלט. אנא הזן מספר תקין בן ארבע ספרות עם ספרות ייחודיות.")
        else:
            break

    # 3.4. בדיקה האם המספר נוחש
    if user_guess == secret_number:
        print(f"מזל טוב! ניחשת את המספר ב-{number_of_guesses} ניסיונות!")
        break  # סיום הלולאה אם המספר נוחש

    # 3.5. ספירת MUG ו-WMP
    mug, wmp = count_mug_wmp(secret_number, user_guess)

    # 3.6. הצגת רמז
    print(f"MUG = {mug}, WMP = {wmp}")

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: מייבא את המודול `random`, המשמש ליצירת מספר אקראי.

2.  **הפונקציה `generate_secret_number()`**:
    -  `def generate_secret_number():`: מגדיר פונקציה ליצירת מספר סודי בן ארבע ספרות עם ספרות ייחודיות.
    -  `digits = list(range(10))`: יוצר רשימה של ספרות מ-0 עד 9.
    -  `random.shuffle(digits)`: מערבב את הספרות באופן אקראי.
    -  `return "".join(map(str, digits[:4]))`: מחזיר מחרוזת המורכבת מארבע הספרות הראשונות שערבובו, ויוצר מספר בן ארבע ספרות.

3.  **הפונקציה `count_mug_wmp(secret, guess)`**:
    - `def count_mug_wmp(secret, guess):`: מגדיר פונקציה לספירת MUG ו-WMP.
    - `mug = 0`, `wmp = 0`: מאתחל את מוני ה-MUG וה-WMP.
    - `for i in range(len(secret)):`: מבצע איטרציה על ספרות המספר הסודי.
        - `if secret[i] == guess[i]:`: אם הספרה במיקום הנוכחי זהה, מגדיל את מונה MUG.
        - `elif guess[i] in secret:`: אם הספרה מהניחוש קיימת במספר הסודי, אך לא במיקומה הנוכחי, מגדיל את מונה WMP.
    - `return mug, wmp`: מחזיר זוג ערכים המכיל את MUG ו-WMP.

4.  **החלק הראשי של התוכנית**:
   - `secret_number = generate_secret_number()`: יוצר את המספר הסודי באמצעות הפונקציה `generate_secret_number()`.
    - `number_of_guesses = 0`: מאתחל את מונה הניסיונות.
    - `while True:`: מתחיל לולאה אינסופית, עד שהשחקן מנחש את המספר.
        - `number_of_guesses += 1`: מגדיל את מונה הניסיונות.
        - `while True:`: לולאה פנימית לבדיקת קלט המשתמש.
            - `user_guess = input("הזן מספר בן ארבע ספרות עם ספרות ייחודיות: ")`: מבקש קלט מהמשתמש.
            - `if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:`: בודק את תקינות הקלט (ארבע ספרות, כל הספרות ייחודיות).
            - `else: break`: אם הקלט תקין, יוצא מהלולאה הפנימית.
        - `if user_guess == secret_number:`: בודק אם המספר נוחש.
            - `print(f"מזל טוב! ניחשת את המספר ב-{number_of_guesses} ניסיונות!")`: מציג הודעת ניצחון.
            - `break`: יוצא מהלולאה הראשית.
        - `mug, wmp = count_mug_wmp(secret_number, user_guess)`: קורא לפונקציה `count_mug_wmp` לספירת MUG ו-WMP.
        - `print(f"MUG = {mug}, WMP = {wmp}")`: מציג את הרמז עם MUG ו-WMP.

"""