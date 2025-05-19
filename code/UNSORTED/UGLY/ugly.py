"""
UGLY:
=================
מורכבות: 4
-----------------
המשחק "UGLY" הוא משחק ניחוש פשוט, שבו המחשב מייצר מספר אקראי, והשחקן צריך לנחש את המספר הזה. לאחר כל ניסיון, השחקן מקבל הודעה האם הניחוש שלו היה גבוה או נמוך מהמספר שנגרל.

כללי המשחק:
1.  המחשב מייצר מספר שלם אקראי בטווח שבין 1 ל-100.
2.  השחקן מזין את ניחושו לגבי המספר שנגרל.
3.  לאחר כל ניסיון, המחשב מודיע האם המספר שהוזן היה "TOO HIGH" (גבוה מדי) או "TOO LOW" (נמוך מדי).
4.  המשחק מסתיים כאשר השחקן מנחש את המספר.
-----------------
אלגוריתם:
1.  הפק מספר אקראי בטווח שבין 1 ל-100 ושמור אותו במשתנה `targetNumber`.
2.  התחל בלולאה "כל עוד לא נוחש":
    2.1 בקש מהשחקן להזין מספר ושמור אותו במשתנה `userGuess`.
    2.2 אם `userGuess` שווה ל-`targetNumber`, הצג את ההודעה "YOU GOT IT!" ועבור לשלב 3.
    2.3 אם `userGuess` קטן מ-`targetNumber`, הצג את ההודעה "TOO LOW".
    2.4 אם `userGuess` גדול מ-`targetNumber`, הצג את ההודעה "TOO HIGH".
3.  סיים את המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeTargetNumber["<p align='left'>Инициализация:
    <code><b>targetNumber = random(1, 100)</b></code></p>"]
    InitializeTargetNumber --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart --> InputGuess["Ввод числа пользователем: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"Проверка: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT!</b>"]
    OutputWin --> End["Конец"]
    CheckGuess -- Нет --> CheckLow{"Проверка: <code><b>userGuess &lt; targetNumber?</b></code>"}
    CheckLow -- Да --> OutputLow["Вывод сообщения: <b>TOO LOW</b>"]
    OutputLow --> LoopStart
    CheckLow -- Нет --> OutputHigh["Вывод сообщения: <b>TOO HIGH</b>"]
    OutputHigh --> LoopStart
```
מקרא:
    Start - תחילת התוכנית.
    InitializeTargetNumber - אתחול המשתנה targetNumber במספר שלם אקראי בטווח מ-1 עד 100.
    LoopStart - תחילת הלולאה שנמשכת כל עוד המספר לא נוחש.
    InputGuess - בקשת קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר שהוזן userGuess שווה למספר שנגרל targetNumber.
    OutputWin - הצגת הודעת ניצחון אם המספרים שווים.
    End - סיום התוכנית.
    CheckLow - בדיקה האם המספר שהוזן userGuess קטן מהמספר שנגרל targetNumber.
    OutputLow - הצגת ההודעה "TOO LOW" אם המספר שהוזן קטן מהמספר שנגרל.
    OutputHigh - הצגת ההודעה "TOO HIGH" אם המספר שהוזן גדול מהמספר שנגרל.
"""
import random

# מייצרים מספר אקראי מ-1 עד 100
targetNumber = random.randint(1, 100)

# לולאה אינסופית עד שהשחקן ינחש את המספר
while True:
    # מבקשים מהמשתמש להזין מספר
    try:
        userGuess = int(input("Угадай число: ")) # השארת "Угадай число: " ברוסית כחלק מהקלט הצפוי
    except ValueError:
        print("Пожалуйста, введите целое число.") # השארת "Пожалуйста, введите целое число." ברוסית כחלק מהפלט הצפוי
        continue

    # בודקים אם המספר נוחש
    if userGuess == targetNumber:
        print("YOU GOT IT!")
        break  # מסיימים את הלולאה אם ניחשנו
    # בודקים אם המספר שהוזן קטן מהמספר שנגרל
    elif userGuess < targetNumber:
        print("TOO LOW")
    # אם לא קטן ולא נוחש, משמע גדול
    else:
        print("TOO HIGH")
"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, המשמש להפקת מספר אקראי.
2.  **הפקת מספר אקראי**:
    -   `targetNumber = random.randint(1, 100)`: מפיק מספר שלם אקראי בטווח שבין 1 ל-100 ושומר אותו במשתנה `targetNumber`.
3.  **הלולאה הראשית `while True:`**:
    -   `while True:`: יוצרת לולאה אינסופית, הנמשכת עד שהשחקן מנחש את המספר.
    -  **קלט נתונים**:
        - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין קלט שאינו מספר שלם, תוצג הודעת שגיאה.
        -   `userGuess = int(input("Угадай число: "))`: מבקש מהמשתמש להזין מספר ושומר אותו במשתנה `userGuess`.
    -   **בדיקת תנאי הניצחון**:
        -   `if userGuess == targetNumber:`: בודק האם המספר שהוזן שווה למספר שנגרל.
        -   `print("YOU GOT IT!")`: מציג הודעת ניצחון.
        -   `break`: מסיים את הלולאה (ואת המשחק) אם המספר נוחש.
    -   **רמזים**:
        -   `elif userGuess < targetNumber:`: בודק האם המספר שהוזן קטן מהמספר שנגרל.
        -   `print("TOO LOW")`: מציג רמז שיש להזין מספר גדול יותר.
        -   `else:`: אם המספר לא נוחש ואינו קטן מהמספר שנגרל, אזי הוא גדול ממנו.
        -   `print("TOO HIGH")`: מציג רמז שיש להזין מספר קטן יותר.
"""