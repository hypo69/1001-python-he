BULLCOW:
=================
רמת קושי: 5
-----------------
המשחק "שורות ופרות" (Быки и коровы) הוא משחק המיועד לשני שחקנים, בו שחקן אחד בוחר מספר בן ארבע ספרות, והשחקן השני מנסה לנחש אותו. לאחר כל ניסיון, השחקן המנחש מקבל רמזים בדמות מספר ה"שורות" (ספרות שנוחשו ונמצאות במיקומים הנכונים) ומספר ה"פרות" (ספרות שנוחשו אך נמצאות במיקומים שגויים).

כללי המשחק:
1. המחשב בוחר מספר בן ארבע ספרות, בו כל הספרות שונות.
2. השחקן מנסה לנחש את המספר על ידי הזנת ניחושים.
3. לאחר כל ניסיון, המחשב מדווח על מספר ה"שורות" וה"פרות".
    - "שורה" - ספרה שנוחשה ונמצאת במיקום הנכון.
    - "פרה" - ספרה שנוחשה אך נמצאת במיקום שגוי.
4. המשחק נמשך עד שהשחקן מנחש את המספר שנבחר (כלומר, מקבל 4 "שורות").
-----------------
אלגוריתם:
1. ליצור מספר אקראי בן 4 ספרות עם ספרות שונות.
2. לאפס את מונה הניסיונות ל-0.
3. להתחיל לולאה "כל עוד לא נוחש":
    3.1 להגדיל את מונה הניסיונות ב-1.
    3.2 לבקש מהשחקן להזין מספר בן 4 ספרות.
    3.3 לאפס מונים לשורות (B) ולפרות (C) ל-0.
    3.4 לעבור על כל ספרה במספר שנבחר ובהזנת השחקן:
        3.4.1 אם הספרות במיקום הנתון זהות, להגדיל את מונה השורות (B).
        3.4.2 אחרת, אם ספרת ההזנה קיימת במספר שנבחר (אך לא באותו מיקום), להגדיל את מונה הפרות (C).
    3.5 להציג את מספר השורות והפרות: "B שורות, C פרות".
    3.6 אם מספר השורות שווה ל-4, להציג את ההודעה "YOU GOT IT IN {מספר הניסיונות} GUESSES!" ולסיים את המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateTargetNumber["<p align='left'>ליצור מספר אקראי בן 4 ספרות <br>עם ספרות שונות: <code><b>targetNumber</b></code></p>"]
    GenerateTargetNumber --> InitializeGuesses["<code><b>numberOfGuesses = 0</b></code>"]
    InitializeGuesses --> LoopStart{"התחלת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["הזנת מספר בן 4 ספרות: <code><b>userGuess</b></code>"]
    InputGuess --> InitializeBullsCows["<code><b>bulls = 0, cows = 0</b></code>"]
    InitializeBullsCows --> CheckBullsCows{"<p align='left'>בדיקת <code><b>targetNumber</b></code> ו-<code><b>userGuess</b></code>:<br> ספירת <code><b>bulls</b></code> ו-<code><b>cows</b></code></p>"}
    CheckBullsCows --> OutputBullsCows["הצגה: <code><b>{bulls}</b></code> שורות, <code><b>{cows}</b></code> פרות"]
    OutputBullsCows --> CheckWin{"<code><b>bulls == 4</b></code>?"}
    CheckWin -- כן --> OutputWin["הצגת הודעה:<br> <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סיום"]
    CheckWin -- לא --> LoopStart
    LoopStart -- לא --> End
```
**מקרא**:
   - Start - התחלת התוכנית.
   - GenerateTargetNumber - יצירת מספר אקראי בן 4 ספרות עם ספרות ייחודיות.
   - InitializeGuesses - אתחול מונה הניסיונות `numberOfGuesses` ל-0.
   - LoopStart - התחלת הלולאה שנמשכת כל עוד המספר לא נוחש.
   - IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
   - InputGuess - בקשת הזנת מספר בן 4 ספרות מהמשתמש `userGuess`.
   - InitializeBullsCows - אתחול מוני `bulls` (שורות) ו-`cows` (פרות) ל-0.
   - CheckBullsCows - בדיקת התאמת הספרות ב-`userGuess` ו-`targetNumber` לצורך ספירת `bulls` ו-`cows`.
   - OutputBullsCows - הצגת מספר השורות והפרות על המסך.
   - CheckWin - בדיקה אם מספר השורות שווה ל-4.
   - OutputWin - הצגת הודעת הניצחון ומספר הניסיונות.
   - End - סיום התוכנית.
```
import random

def generate_target_number():
    """יוצר מספר אקראי בן 4 ספרות ללא ספרות חוזרות."""
    digits = list(range(10)) # יצירת רשימת ספרות מ-0 עד 9
    random.shuffle(digits)    # ערבוב הספרות באופן אקראי
    target = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3] # הרכבת מספר 4 ספרות מהספרות האקראיות
    # בדיקה שהספרה הראשונה אינה 0
    if digits[0] == 0:
        return generate_target_number()
    return target

# יצירת המספר המנוחש
targetNumber = generate_target_number()
# אתחול מונה ניסיונות
numberOfGuesses = 0

# לולאת המשחק הראשית
while True:
    # הגדלת מונה הניסיונות
    numberOfGuesses += 1
    # בקשת הזנת מספר מהמשתמש
    try:
        userGuess = int(input("הזן מספר בן 4 ספרות: "))
    except ValueError:
        print("אנא הזן מספר שלם בן 4 ספרות.")
        continue

    # בדיקה שהמספר בן 4 ספרות
    if not (1000 <= userGuess <= 9999):
        print("אנא הזן מספר בן 4 ספרות.")
        continue

    # אתחול מוני שורות ופרות
    bulls = 0
    cows = 0
    
    # המרת המספר המנוחש והזנת המשתמש למחרוזות, לצורך השוואת ספרות קלה יותר
    target_str = str(targetNumber)
    guess_str = str(userGuess)

    # מעבר על כל ספרה
    for i in range(4):
        if guess_str[i] == target_str[i]:
            # אם הספרות באותו מיקום זהות, זוהי "שורה"
            bulls += 1
        elif guess_str[i] in target_str:
            # אם הספרה מהמספר שהוזן קיימת במספר המנוחש, אך לא באותו מיקום, זוהי "פרה"
            cows += 1
            
    # הצגת מספר השורות והפרות
    print(f"{bulls} שורות, {cows} פרות")

    # בדיקה לניצחון
    if bulls == 4:
        print(f"ברכות! ניחשת את המספר ב- {numberOfGuesses} ניסיונות!")
        break  # סיום המשחק בזמן ניצחון

"""
הסבר על הקוד:
1.  **ייבוא המודול `random`**:
   -  `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים וערבוב פריטים ברשימה.
2.  **הפונקציה `generate_target_number()`**:
    -  יוצרת מספר אקראי בן 4 ספרות ללא ספרות חוזרות:
        - `digits = list(range(10))`: יוצרת רשימה של ספרות מ-0 עד 9.
        - `random.shuffle(digits)`: מערבבת את רשימת הספרות באופן אקראי.
        - `target = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]`: מרכיבה מספר בן 4 ספרות מארבע הספרות האקראיות הראשונות.
        - `if digits[0] == 0:`: בודקת שהספרה הראשונה אינה אפס, אם כן, הפונקציה נקראת באופן רקורסיבי ליצירת מספר חדש.
        - `return target`: מחזירה את המספר שנוצר.
3.  **אתחול משתנים**:
    -   `targetNumber = generate_target_number()`: יוצרת את המספר המנוחש בן 4 ספרות ושומרת אותו ב-`targetNumber`.
    -   `numberOfGuesses = 0`: מאתחלת את המשתנה `numberOfGuesses` לספירת מספר ניסיונות השחקן.
4.  **הלולאה הראשית `while True:`**:
    -   לולאה אינסופית שנמשכת עד שהשחקן מנחש את המספר (עד הפעלת הפקודה `break`).
    -   `numberOfGuesses += 1`: מגדילה את מונה הניסיונות ב-1.
    -   **הזנת נתונים**:
        -   `try...except ValueError`: בלוק try-except מטפל בשגיאות כאשר המשתמש מזין קלט שאינו מספר.
        -   `userGuess = int(input("הזן מספר בן 4 ספרות: "))`: מבקשת מהמשתמש מספר בן 4 ספרות ושומרת אותו ב-`userGuess`.
        - `if not (1000 <= userGuess <= 9999):`: בודקת שהמספר בן 4 ספרות.
    -   **אתחול מוני "שורות" ו"פרות"**:
        -   `bulls = 0`: מאתחלת את מונה ה"שורות" ל-0.
        -   `cows = 0`: מאתחלת את מונה ה"פרות" ל-0.
    -   **המרת מספרים למחרוזות**:
         - `target_str = str(targetNumber)`: ממירה את המספר המנוחש למחרוזת.
         - `guess_str = str(userGuess)`: ממירה את קלט המשתמש למחרוזת.
    -   **בדיקה ל"שורות" ו"פרות"**:
        -   `for i in range(4):`: לולאה לבדיקת כל ספרה במספר שהוזן:
            -   `if guess_str[i] == target_str[i]:`: אם הספרות במיקומים זהים תואמות, מגדילים את `bulls` ב-1.
            -  `elif guess_str[i] in target_str:`: אם הספרה מהמספר שהוזן קיימת במספר המנוחש, אך לא באותו מיקום, מגדילים את `cows` ב-1.
    -   **הצגת מספר ה"שורות" ו"פרות"**:
        -   `print(f"{bulls} שורות, {cows} פרות")`: מציגה על המסך את מספר ה"שורות" וה"פרות".
    -   **תנאי ניצחון**:
        -   `if bulls == 4:`: בודקת אם מספר ה"שורות" שווה ל-4 (כל הספרות נוחשו).
        -   `print(f"ברכות! ניחשת את המספר ב- {numberOfGuesses} ניסיונות!")`: מציגה הודעת ניצחון ומספר הניסיונות.
        -   `break`: מסיימת את הלולאה אם המספר נוחש.
"""