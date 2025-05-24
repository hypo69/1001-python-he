<23 MTH>:
=================
מורכבות: 3
-----------------
המשחק "ניחוש המספר" הוא משחק קלאסי שבו המחשב בוחר מספר אקראי בטווח של 1 עד 100, והשחקן צריך לנחש את המספר הזה, תוך קבלת רמזים "נמוך מדי" או "גבוה מדי" אחרי כל ניסיון.
המשחק ממשיך עד שהשחקן מנחש את המספר.

כללי המשחק:
1.  המחשב בוחר מספר שלם אקראי מ-1 עד 100.
2.  השחקן מזין את ניחושיו לגבי המספר שנגאלו.
3.  אחרי כל ניסיון, המחשב מודיע אם המספר שהוזן היה נמוך מדי, גבוה מדי, או שנוחש נכונה.
4.  המשחק ממשיך עד שהשחקן מנחש את המספר שנגאלו.
-----------------
אלגוריתם:
1.  אפס את מונה הניסיונות ל-0.
2.  צור מספר אקראי בטווח של 1 עד 100.
3.  התחל לולאה "כל עוד המספר לא נוחש":
    3.1 הגדל את מונה הניסיונות ב-1.
    3.2 בקש מהשחקן להזין מספר.
    3.3 אם המספר שהוזן שווה למספר שנגאלו, עבור לשלב 4.
    3.4 אם המספר שהוזן קטן מהמספר שנגאלו, הצג את ההודעה "TOO LOW".
    3.5 אם המספר שהוזן גדול מהמספר שנגאלו, הצג את ההודעה "TOO HIGH".
4. הצג את ההודעה "YOU GOT IT IN {число попыток} GUESSES!"
5. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    numberOfGuesses = 0
    targetNumber = random(1, 100)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart -- Да --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["Ввод числа пользователем: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"Проверка: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["Конец"]
    CheckGuess -- Нет --> CheckLow{"Проверка: <code><b>userGuess &lt; targetNumber</b></code>?"}
    CheckLow -- Да --> OutputLow["Вывод сообщения: <b>TOO LOW</b>"]
    OutputLow --> LoopStart
    CheckLow -- Нет --> OutputHigh["Вывод сообщения: <b>TOO HIGH</b>"]
    OutputHigh --> LoopStart
    LoopStart -- Нет --> End
```
**מקרא:**
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מספר הניסיונות) מאופס ל-0, ו-targetNumber (המספר שנגאלו) נוצר באופן אקראי מ-1 עד 100.
    LoopStart - תחילת הלולאה, שנמשכת כל עוד המספר לא נוחש.
    IncreaseGuesses - הגדלת מונה מספר הניסיונות ב-1.
    InputGuess - בקשת קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר שהוזן userGuess שווה למספר שנגאלו targetNumber.
    OutputWin - הצגת הודעת ניצחון, אם המספרים שווים, עם ציון מספר הניסיונות.
    End - סיום התוכנית.
    CheckLow - בדיקה האם המספר שהוזן userGuess קטן מהמספר שנגאלו targetNumber.
    OutputLow - הצגת ההודעה "TOO LOW", אם המספר שהוזן קטן יותר מהנגאלו.
    OutputHigh - הצגת ההודעה "TOO HIGH", אם המספר שהוזן גדול יותר מהנגאלו.
"""
import random

# אתחול מונה הניסיונות
numberOfGuesses = 0
# יצירת מספר אקראי מ-1 עד 100
targetNumber = random.randint(1, 100)

# לולאת המשחק הראשית
while True:
    # הגדלת מספר הניסיונות
    numberOfGuesses += 1
    # בקשת קלט מספר מהמשתמש
    try:
        userGuess = int(input("Угадай число от 1 до 100: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    # בדיקה האם המספר נוחש
    if userGuess == targetNumber:
        print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {numberOfGuesses} попыток!")
        break  # סיום הלולאה אם המספר נוחש
    elif userGuess < targetNumber:
        print("Слишком низко")  # הודעה שהמספר שנגאלו גדול יותר
    else:
        print("Слишком высоко")  # הודעה שהמספר שנגאלו קטן יותר
```
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספר אקראי.
2.  **אתחול משתנים**:
    -   `numberOfGuesses = 0`: מאתחל את המשתנה `numberOfGuesses` לספירת מספר ניסיונות השחקן.
    -   `targetNumber = random.randint(1, 100)`: יוצר מספר שלם אקראי בטווח של 1 עד 100 ושומר אותו במשתנה `targetNumber`. זהו המספר שהשחקן צריך לנחש.
3.  **לולאת המשחק הראשית `while True:`**:
    -   `while True:`: מתחילה לולאה אינסופית שתמשיך כל עוד השחקן לא ניחש את המספר.
    -   `numberOfGuesses += 1`: מגדילה את מונה הניסיונות ב-1.
    -   **טיפול בקלט מהמשתמש**:
        -   `try...except ValueError:`: משמש לטיפול בשגיאות אפשריות בעת הזנת נתונים על ידי המשתמש.
        -   `userGuess = int(input("Угадай число от 1 до 100: "))`: מציג הודעה המבקשת להזין מספר מ-1 עד 100 ושומר את התוצאה ב-`userGuess`. הפונקציה `int()` ממירה את המחרוזת שהוזנה על ידי המשתמש למספר שלם.
        -   `except ValueError:`: אם המשתמש מזין משהו שאינו ניתן להמרה למספר שלם, מוצגת הודעת שגיאה והתוכנית ממשיכה לאיטרציה הבאה של הלולאה.
    -   **בדיקת תנאי הניצחון**:
        -   `if userGuess == targetNumber:`: בודק האם המספר שהוזן על ידי המשתמש (`userGuess`) שווה למספר שנגאלו (`targetNumber`).
        -   `print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {numberOfGuesses} попыток!")`: אם המספרים שווים, מוצגת הודעת ברכה המציינת את מספר הניסיונות.
        -   `break`: מסיים את לולאת `while`, והמשחק מסתיים.
    -   **רמזים למשתמש**:
        -   `elif userGuess < targetNumber:`: אם המספר שהוזן קטן מהמספר שנגאלו, מוצגת ההודעה "סליחה, נמוך מדי".
        -   `else:`: אם המספר שהוזן אינו שווה ואינו קטן מהמספר שנגאלו, אזי הוא גדול יותר, ומוצגת ההודעה "סליחה, גבוה מדי".
```