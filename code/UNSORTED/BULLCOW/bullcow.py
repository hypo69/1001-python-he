BULLCOW:
=================
רמת קושי: 5
-----------------
המשחק "שורות ופרות" הוא משחק לשני שחקנים, שבו שחקן אחד בוחר מספר בן ארבע ספרות, והשני מנסה לנחש אותו. לאחר כל ניסיון, השחקן המנחש מקבל רמזים בצורת מספר ה"שורות" (ספרות שנכחשו ונמצאות במיקומים הנכונים) ומספר ה"פרות" (ספרות שנכחשו אך נמצאות במיקומים שגויים).

כללי המשחק:
1. המחשב בוחר מספר בן ארבע ספרות שבו כל הספרות שונות זו מזו.
2. השחקן מנסה לנחש את המספר על ידי הזנת ההשערות שלו.
3. לאחר כל ניסיון, המחשב מדווח על מספר ה"שורות" וה"פרות".
    - "שור" - ספרה שנכחשה ונמצאת במיקום הנכון.
    - "פרה" - ספרה שנכחשה אך נמצאת במיקום שגוי.
4. המשחק נמשך עד שהשחקן מנחש את המספר שנבחר (כלומר, מקבל 4 "שורות").
-----------------
אלגוריתם:
1. יש ליצור מספר אקראי בן 4 ספרות עם ספרות שונות.
2. יש לאתחל את מונה הניסיונות ל-0.
3. יש להתחיל לולאה "עד שלא נוחש":
    3.1 הגדל את מונה הניסיונות ב-1.
    3.2 בקש מהשחקן להזין מספר בן 4 ספרות.
    3.3 אתחל את מוני השורות (B) והפרות (C) ל-0.
    3.4 עבור על כל ספרה במספר הנבחר ובהזנת השחקן:
        3.4.1 אם הספרות במיקום הנתון זהות, הגדל את מונה השורות (B).
        3.4.2 אחרת, אם הספרה מההזנה קיימת במספר הנבחר (אך לא באותו מיקום) הגדל את מונה הפרות (C).
    3.5 הדפס את מספר השורות והפרות: "B שורות, C פרות".
    3.6 אם מספר השורות שווה ל-4, הדפס את ההודעה "YOU GOT IT IN {מספר ניסיונות} GUESSES!" וסיים את המשחק.
-----------------
בלוק-תרשים:
```mermaid
flowchart TD
    Start["Начало"] --> GenerateTargetNumber["<p align='left'>Сгенерировать случайное 4-значное число <br>с разными цифрами: <code><b>targetNumber</b></code></p>"]
    GenerateTargetNumber --> InitializeGuesses["<code><b>numberOfGuesses = 0</b></code>"]
    InitializeGuesses --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart -- Да --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["Ввод 4-значного числа: <code><b>userGuess</b></code>"]
    InputGuess --> InitializeBullsCows["<code><b>bulls = 0, cows = 0</b></code>"]
    InitializeBullsCows --> CheckBullsCows{"<p align='left'>Проверка <code><b>targetNumber</b></code> и <code><b>userGuess</b></code>:<br> подсчет <code><b>bulls</b></code> и <code><b>cows</b></code></p>"}
    CheckBullsCows --> OutputBullsCows["Вывод: <code><b>{bulls}</b></code> быков, <code><b>{cows}</b></code> коров"]
    OutputBullsCows --> CheckWin{"<code><b>bulls == 4</b></code>?"}
    CheckWin -- Да --> OutputWin["Вывод сообщения:<br> <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> LoopStart
    LoopStart -- Нет --> End
```
**מקרא**:
   - Start - התחלת התוכנית.
   - GenerateTargetNumber - יצירת מספר אקראי בן 4 ספרות עם ספרות ייחודיות.
   - InitializeGuesses - אתחול מונה הניסיונות `numberOfGuesses` ל-0.
   - LoopStart - התחלת הלולאה, הנמשכת עד שהמספר נוחש.
   - IncreaseGuesses - הגדלת מונה מספר הניסיונות ב-1.
   - InputGuess - בקשת קלט מהמשתמש עבור מספר בן 4 ספרות `userGuess`.
   - InitializeBullsCows - אתחול מוני `bulls` (שורות) ו-`cows` (פרות) ל-0.
   - CheckBullsCows - בדיקת התאמת הספרות ב-`userGuess` וב-`targetNumber` לצורך ספירת `bulls` ו-`cows`.
   - OutputBullsCows - הדפסת מספר השורות והפרות למסך.
   - CheckWin - בדיקה האם מספר השורות שווה ל-4.
   - OutputWin - הדפסת הודעה על ניצחון ומספר הניסיונות.
   - End - סוף התוכנית.
```python
import random

def generate_target_number():
    """יוצר מספר אקראי בן 4 ספרות עם ספרות שאינן חוזרות על עצמן."""
    digits = list(range(10)) # יוצר רשימה של ספרות מ-0 עד 9
    random.shuffle(digits)    # מערבב את הספרות באופן אקראי
    target = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3] # מרכיב מספר בן 4 ספרות מהספרות האקראיות
    # בדיקה שהספרה הראשונה אינה 0
    if digits[0] == 0:
        return generate_target_number()
    return target

# יוצר את המספר הנבחר
targetNumber = generate_target_number()
# מאתחל את מונה הניסיונות
numberOfGuesses = 0

# לולאת המשחק הראשית
while True:
    # מגדיל את מספר הניסיונות
    numberOfGuesses += 1
    # מבקש קלט מספר מהמשתמש
    try:
        userGuess = int(input("הכנס מספר בן 4 ספרות: "))
    except ValueError:
        print("אנא הכנס מספר שלם בן 4 ספרות.")
        continue

    # בדיקה שהמספר הוא בן 4 ספרות
    if not (1000 <= userGuess <= 9999):
        print("אנא הכנס מספר בן 4 ספרות.")
        continue

    # אתחול מוני השורות והפרות
    bulls = 0
    cows = 0
    
    # ממיר את המספר הנבחר ואת קלט המשתמש למחרוזות כדי להקל על השוואת הספרות
    target_str = str(targetNumber)
    guess_str = str(userGuess)

    # עובר על כל ספרה
    for i in range(4):
        if guess_str[i] == target_str[i]:
            # אם הספרות באותו מיקום זהות, זה "שור"
            bulls += 1
        elif guess_str[i] in target_str:
            # אם ספרה מהמספר שהוזן קיימת במספר הנבחר, אך לא באותו מיקום, זו "פרה"
            cows += 1
            
    # הדפסת מספר השורות והפרות
    print(f"{bulls} שורות, {cows} פרות")

    # בדיקת ניצחון
    if bulls == 4:
        print(f"מזל טוב! ניחשת את המספר ב- {numberOfGuesses} ניסיונות!")
        break  # סיום המשחק במקרה של ניצחון

"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
   -  `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים ולערבוב אלמנטים ברשימה.
2.  **הפונקציה `generate_target_number()`**:
    -  יוצרת מספר אקראי בן 4 ספרות עם ספרות שאינן חוזרות על עצמן:
        - `digits = list(range(10))`: יוצרת רשימה של ספרות מ-0 עד 9.
        - `random.shuffle(digits)`: מערבבת את רשימת הספרות באופן אקראי.
        - `target = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]`: מרכיבה מספר בן 4 ספרות מארבע הספרות האקראיות הראשונות.
        - `if digits[0] == 0:`: בדיקה שהספרה הראשונה אינה אפס, ואם כן, הפונקציה נקראת רקורסיבית ליצירת מספר חדש.
        - `return target`: מחזירה את המספר שנוצר.
3.  **אתחול משתנים**:
    -   `targetNumber = generate_target_number()`: יוצרת את המספר הנבחר בן 4 ספרות ושומרת אותו ב-`targetNumber`.
    -   `numberOfGuesses = 0`: מאתחלת את המשתנה `numberOfGuesses` לספירת מספר הניסיונות של השחקן.
4.  **הלולאה הראשית `while True:`**:
    -   לולאה אינסופית, הנמשכת עד שהשחקן מנחש את המספר (עד שתתבצע הפקודה `break`).
    -   `numberOfGuesses += 1`: מגדילה את מונה הניסיונות ב-1.
    -   **קלט נתונים**:
        -   `try...except ValueError`: בלוק try-except מטפל בשגיאות כאשר המשתמש מזין קלט שאינו מספר.
        -   `userGuess = int(input("הכנס מספר בן 4 ספרות: "))`: מבקש מהמשתמש מספר בן 4 ספרות ושומר אותו ב-`userGuess`.
        - `if not (1000 <= userGuess <= 9999):`: בודקת שהמספר הוא בן 4 ספרות.
    -   **אתחול מוני "שורות" ו-"פרות"**:
        -   `bulls = 0`: מאתחל את מונה ה"שורות" ל-0.
        -   `cows = 0`: מאתחל את מונה ה"פרות" ל-0.
    -   **המרה של מספרים למחרוזות**:
         - `target_str = str(targetNumber)`: ממיר את המספר הנבחר למחרוזת.
         - `guess_str = str(userGuess)`: ממיר את קלט המשתמש למחרוזת.
    -   **בדיקה עבור "שורות" ו-"פרות"**:
        -   `for i in range(4):`:  לולאה לבדיקת כל ספרה במספר שהוזן:
            -   `if guess_str[i] == target_str[i]:`:  אם הספרות באותם מיקומים זהות, מגדילים את `bulls` ב-1.
            -  `elif guess_str[i] in target_str:`: אם ספרה מהמספר שהוזן קיימת במספר הנבחר, אך לא באותו מיקום, זו "פרה"
            - `cows += 1`
    -   **הדפסת מספר ה"שורות" ו-"הפרות"**:
        -   `print(f"{bulls} שורות, {cows} פרות")`: מדפיסה למסך את מספר ה"שורות" ו-"הפרות".
    -   **תנאי ניצחון**:
        -   `if bulls == 4:`: בודקת האם מספר ה"שורות" שווה ל-4 (כל הספרות נוחשו).
        -   `print(f"מזל טוב! ניחשת את המספר ב- {numberOfGuesses} ניסיונות!")`: מדפיסה הודעה על ניצחון ומספר הניסיונות.
        -   `break`: מסיימת את הלולאה אם המספר נוחש.
"""