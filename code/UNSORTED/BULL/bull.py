"""
<BULL>:
=================
רמת קושי: 4
-----------------
המשחק "BULL" הוא משחק היגיון מספרי שבו המחשב מגריל מספר אקראי בן ארבע ספרות, כאשר כל הספרות שונות, והשחקן מנסה לנחש את המספר הזה. לאחר כל ניסיון, המחשב מדווח על מספר ה"פרים" (ספרה נוחשה ונמצאת במקום הנכון) ו"פרות" (ספרה נוחשה אך נמצאת במקום שגוי).

חוקי המשחק:
1.  המחשב מגריל מספר אקראי בן ארבע ספרות, שכל ספרותיו שונות.
2.  השחקן מבצע ניסיונות ניחוש, באמצעות קלט של מספרים בני ארבע ספרות.
3.  לאחר כל ניסיון, המחשב מציג את כמות ה"פרים" וה"פרות".
    *   "פר" - זו ספרה שנוחשה ונמצאת במיקום הנכון.
    *   "פרה" - זו ספרה שנוחשה אך נמצאת במיקום שגוי.
4.  המשחק ממשיך עד אשר השחקן ינחש את המספר (כלומר, יקבל 4 "פרים").
-----------------
אלגוריתם:
1.  לייצר מספר אקראי בן ארבע ספרות עם ספרות שונות.
2.  התחל לולאה "כל עוד מספר הפרים אינו שווה ל-4":
    2.1 בקש קלט מספר בן ארבע ספרות מהשחקן.
    2.2 בדוק את תקינות המספר שהוזן (4 ספרות).
    2.3 אתחל מוני פרים ופרות ל-0.
    2.4 עבור כל ספרה במספר שהוזן:
        2.4.1 אם הספרה תואמת לספרה במספר המטרה באותה עמדה, הגדל את מונה הפרים.
        2.4.2 אחרת, אם הספרה קיימת במספר המטרה במיקום אחר, הגדל את מונה הפרות.
    2.5 הצג את כמות הפרים והפרות.
3.  הצג הודעת ניצחון.
4.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateTargetNumber["<p align='left'>הגרל מספר אקראי בן 4 ספרות עם ספרות שונות:
    <code><b>targetNumber</b></code></p>"]
    GenerateTargetNumber --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> InputGuess["קלט מספר מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> ValidateGuess["בדיקה: <code><b>len(userGuess) == 4?</b></code>"]
     ValidateGuess -- לא --> OutputInvalid["הצגת הודעה: <b>מספר שגוי</b>"]
     OutputInvalid --> LoopStart
    ValidateGuess -- כן --> InitializeCounts["<p align='left'>אתחול מוני:
    <code><b>
    bulls = 0
    cows = 0
    </b></code></p>"]
    InitializeCounts --> CheckDigits{"לולאה על ספרות <code><b>userGuess</b></code>"}
    CheckDigits --> CheckBull{"בדיקה: ספרה <code><b>userGuess[i]</b></code> == <code><b>targetNumber[i]</b></code>"}
    CheckBull -- כן --> IncreaseBulls["<code><b>bulls = bulls + 1</b></code>"]
        IncreaseBulls --> CheckNextDigit["ספרה הבאה?"]
    CheckBull -- לא --> CheckCow{"בדיקה: <code><b>userGuess[i]</b></code> בתוך <code><b>targetNumber</b></code>?"}
    CheckCow -- כן --> IncreaseCows["<code><b>cows = cows + 1</b></code>"]
        IncreaseCows --> CheckNextDigit
    CheckCow -- לא --> CheckNextDigit
    CheckNextDigit -- כן --> CheckDigits
    CheckNextDigit -- לא --> OutputResult["הצגה: <code><b>{bulls} פרים, {cows} פרות</b></code>"]
    OutputResult --> CheckWin{"בדיקה: <code><b>bulls == 4?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>ניחשת נכון!</b>"]
    OutputWin --> End["סיום"]
    CheckWin -- לא --> LoopStart
    LoopStart -- לא --> End
```
מקרא:
    Start - התחלת התוכנית.
    GenerateTargetNumber - הגרלת מספר אקראי בן 4 ספרות עם ספרות שונות, שמירה במשתנה targetNumber.
    LoopStart - תחילת הלולאה, אשר מתבצעת כל עוד מספר ה"פרים" אינו שווה ל-4.
    InputGuess - בקשת קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
    ValidateGuess - בדיקה שהמספר שהוזן על ידי המשתמש מורכב מ-4 ספרות.
    OutputInvalid - הצגת הודעת שגיאה אם המספר שהוזן אינו מורכב מ-4 ספרות.
    InitializeCounts - אתחול מוני bulls (פרים) ו-cows (פרות) לאפס.
    CheckDigits - תחילת לולאה למעבר על ספרות המספר שהוזן.
    CheckBull - בדיקה האם הספרה מתוך userGuess תואמת לספרה מתוך targetNumber באותה עמדה.
    IncreaseBulls - הגדלת מונה הפרים ב-1.
    CheckCow - בדיקה האם הספרה מתוך userGuess קיימת בתוך targetNumber, אך לא באותה עמדה.
    IncreaseCows - הגדלת מונה הפרות ב-1.
    CheckNextDigit - בדיקה האם יש ספרה הבאה לבדיקה; אם כן, עובר לתחילת הלולאה, אחרת ממשיך הלאה בתרשים הזרימה.
    OutputResult - הצגת כמות ה"פרים" וה"פרות" לאחר כל ניסיון.
    CheckWin - בדיקה האם כמות ה"פרים" שווה ל-4.
    OutputWin - הצגת הודעת ניצחון אם המספר נוחש.
    End - סיום התוכנית.
"""
import random

def generate_target_number():
    """מגרילה מספר אקראי בן ארבע ספרות עם ספרות ייחודיות."""
    digits = list(range(10))
    random.shuffle(digits)
    # Отбрасываем числа с лидирующим нулем
    while digits[0] == 0:
        random.shuffle(digits)

    return "".join(map(str, digits[:4]))

def get_bulls_and_cows(user_guess, target_number):
    """מחשבת את כמות ה"פרים" וה"פרות"."""
    bulls = 0
    cows = 0
    for i, digit in enumerate(user_guess):
        if digit == target_number[i]:
            bulls += 1
        elif digit in target_number:
            cows += 1
    return bulls, cows

# Генерируем загаданное число
target_number = generate_target_number()

# Основной игровой цикл
while True:
    user_guess = input("הזן מספר בן ארבע ספרות: ")

    # Проверка корректности ввода
    if not user_guess.isdigit() or len(user_guess) != 4:
        print("אנא הזן מספר תקין בן ארבע ספרות.")
        continue

    # Подсчет быков и коров
    bulls, cows = get_bulls_and_cows(user_guess, target_number)
    print(f"{bulls} פרים, {cows} פרות")

    # Проверка на победу
    if bulls == 4:
        print("מזל טוב, ניחשת את המספר!")
        break

"""
הסבר קוד:
1.  **ייבוא המודול `random`**:
    *   `import random`: מייבא את המודול `random`, המשמש להגרלת מספרים אקראיים.

2.  **פונקציה `generate_target_number()`**:
    *   `digits = list(range(10))`: יוצרת רשימת ספרות מ-0 עד 9.
    *   `random.shuffle(digits)`: מערבבת את הספרות בסדר אקראי.
    *   לולאה `while digits[0] == 0:`:
        *   בודקת האם הספרה הראשונה היא 0. אם כן, מערבבת את הספרות שוב.
        *   מבטיחה שמספר המטרה לא יתחיל ב-0.
    *   `return "".join(map(str, digits[:4]))`: מחזירה מחרוזת המורכבת מ-4 הספרות הראשונות שערבבו (מספר המטרה).

3.  **פונקציה `get_bulls_and_cows(user_guess, target_number)`**:
    *   `bulls = 0` ו-`cows = 0`: מאתחלת את מוני ה"פרים" וה"פרות" לאפס.
    *   לולאה `for i, digit in enumerate(user_guess)`:
        *   עוברת על הספרות במספר שהוזן על ידי המשתמש עם האינדקסים שלהן.
        *   `if digit == target_number[i]`: בודקת האם הספרה תואמת באותה עמדה במספר המטרה. אם כן, מגדילה את מונה הפרים ב-1.
        *   `elif digit in target_number`: אם הספרה אינה תואמת בעמדה, אך קיימת במספר המטרה, מגדילה את מונה הפרות ב-1.
    *   `return bulls, cows`: מחזירה את כמות ה"פרים" וה"פרות".

4.  **החלק העיקרי של התוכנית**:
    *   `target_number = generate_target_number()`: מגרילה את מספר המטרה בן ארבע הספרות עם ספרות שונות.
    *   `while True`: לולאה אינסופית, שממשיכה כל עוד השחקן לא מנחש את המספר.
    *   `user_guess = input("הזן מספר בן ארבע ספרות: ")`: מבקשת קלט מספר בן ארבע ספרות מהמשתמש.
    *   `if not user_guess.isdigit() or len(user_guess) != 4:`: בודקת האם הקלט תקין (מורכב מ-4 ספרות).
        *   אם הקלט אינו תקין, מציגה הודעת שגיאה ומתחילה סיבוב חדש של הלולאה.
    *   `bulls, cows = get_bulls_and_cows(user_guess, target_number)`: סופרת את כמות הפרים והפרות.
    *   `print(f"{bulls} פרים, {cows} פרות")`: מציגה את כמות ה"פרים" וה"פרות".
    *   `if bulls == 4`: בודקת האם כמות הפרים שווה ל-4.
        *   אם כן, מציגה הודעת ניצחון ומסיימת את הלולאה באמצעות `break`.
"""