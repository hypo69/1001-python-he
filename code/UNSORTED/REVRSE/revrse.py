REVRSE:
=================
מורכבות: 5
-----------------
המשחק "REVRSE" מציע לשחקן לנחש רצף של 4 ספרות, שמיקומן ברצף קבוע, כאשר הספרות יכולות לחזור על עצמן.
לאחר כל מהלך של השחקן, המחשב מציג את מספר הספרות שנוחשו נכונה ואת מספר הספרות הקיימות ברצף הנסתר, אך אינן נמצאות במיקומן הנכון.
המשחק נמשך עד שהשחקן מנחש את רצף הספרות, או עד שמספר הניסיונות מסתיים.

חוקי המשחק:
1.  המחשב מייצר רצף אקראי של 4 ספרות בין 1 ל-6, כאשר הספרות יכולות לחזור על עצמן.
2.  השחקן מזין את הרצף שלו המורכב מ-4 ספרות, גם כן בין 1 ל-6, ומפריד בין הספרות באמצעות רווחים.
3.  לאחר כל ניסיון, המחשב מציג:
    -   מספר הספרות שנוחשו נכונה במיקומן הנכון (פגיעה ישירה).
    -   מספר הספרות שנוחשו נכונה ואשר קיימות ברצף הנסתר, אך אינן נמצאות במיקומן הנכון (פגיעה עקיפה).
4.  המשחק מסתיים כאשר השחקן מנחש את הרצף או לאחר 10 ניסיונות.
-----------------
אלגוריתם:
1.  מאתחלים את מונה הניסיונות ל-0.
2.  מייצרים רצף אקראי של 4 ספרות בין 1 ל-6 (targetSequence).
3.  מתחילים לולאה "כל עוד מספר הניסיונות קטן מ-10":
    3.1 מגדילים את מספר הניסיונות ב-1.
    3.2 מבקשים מהשחקן להזין רצף של 4 ספרות (userSequence).
    3.3 משווים את userSequence ל-targetSequence:
        -   סופרים את מספר הפגיעות הישירות (ספרות במיקומן הנכון).
        -   סופרים את מספר הפגיעות העקיפות (ספרות קיימות, אך לא במיקומן הנכון).
    3.4 מציגים את מספר הפגיעות הישירות והעקיפות.
    3.5 אם מספר הפגיעות הישירות שווה ל-4, מציגים הודעת ניצחון ומסיימים את המשחק.
4.  אם הלולאה הסתיימה (לאחר 10 ניסיונות), מציגים הודעת הפסד ומראים את הרצף הנכון.
5.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    numberOfGuesses = 0
    targetSequence = random sequence of 4 numbers (1 to 6)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока numberOfGuesses < 10"}
    LoopStart -- Да --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputSequence["Ввод последовательности пользователем: <code><b>userSequence</b></code>"]
    InputSequence --> CompareSequences["<p align='left'>Сравнение последовательностей:<br><code><b>
    directHits = count of numbers in correct position<br>
    indirectHits = count of numbers present but in wrong position
    </b></code></p>"]
    CompareSequences --> OutputHits["Вывод: <b>directHits, indirectHits</b>"]
    OutputHits --> CheckWin{"Проверка: <code><b>directHits == 4?</b></code>"}
    CheckWin -- Да --> OutputWin["Вывод сообщения о победе"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> LoopStart
    LoopStart -- Нет --> OutputLose["Вывод сообщения о проигрыше"]
    OutputLose --> ShowTarget["Вывод: <b>targetSequence</b>"]
    ShowTarget --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מספר ניסיונות) מאותחל ל-0, ו-targetSequence (הרצף הנסתר) מיוצר באופן אקראי מ-4 מספרים בין 1 ל-6.
    LoopStart - התחלת לולאה שנמשכת כל עוד מספר הניסיונות numberOfGuesses קטן מ-10.
    IncreaseGuesses - הגדלת מונה מספר הניסיונות ב-1.
    InputSequence - בקשה מהמשתמש להזין רצף של 4 מספרים.
    CompareSequences - השוואת הרצף שהוזן לרצף הנסתר וספירת הפגיעות הישירות והעקיפות.
    OutputHits - הצגת מספר הפגיעות הישירות והעקיפות.
    CheckWin - בדיקה האם מספר הפגיעות הישירות שווה ל-4.
    OutputWin - הצגת הודעה על ניצחון.
    End - סוף התוכנית.
    OutputLose - הצגת הודעה על הפסד.
    ShowTarget - הצגת הרצף הנסתר.
```python
import random

# Function to generate a random sequence of 4 digits from 1 to 6
def generate_target_sequence():
    return [random.randint(1, 6) for _ in range(4)]

# Function to compare sequences and count hits
def compare_sequences(target, user):
    direct_hits = 0 # Direct hits (number in the correct position)
    indirect_hits = 0 # Indirect hits (number is present but not in the correct position)
    target_copy = list(target) # Create a copy of the target sequence to avoid modifying the original
    user_copy = list(user) # Create a copy of the user sequence to avoid modifying the original

    # Counting direct hits and removing them from the copy
    for i in range(4):
        if user_copy[i] == target_copy[i]:
            direct_hits += 1
            target_copy[i] = None # Mark as used to avoid counting again
            user_copy[i] = None # Mark as used to avoid counting again

    # Counting indirect hits
    for i in range(4):
      if user_copy[i] is not None:
        for j in range(4):
            if user_copy[i] == target_copy[j]:
                indirect_hits += 1
                target_copy[j] = None # Mark as used to avoid counting again
                break # Move to the next number in the user sequence
    return direct_hits, indirect_hits

# Main game logic
def play_reverse_game():
    numberOfGuesses = 0  # Attempt counter
    targetSequence = generate_target_sequence()  # Target sequence

    print("Добро пожаловать в игру REVRSE!") # Welcome message in Russian
    print("Я загадал последовательность из 4 цифр (от 1 до 6).") # Game description in Russian
    print("Попробуй ее отгадать. У тебя есть 10 попыток.") # Instructions in Russian

    while numberOfGuesses < 10:
        numberOfGuesses += 1
        try:
            user_input = input(f"Попытка {numberOfGuesses}. Введи 4 цифры через пробел (например, 1 2 3 4): ") # Prompt for input in Russian
            userSequence = [int(x) for x in user_input.split()]
            if len(userSequence) != 4 or not all(1 <= x <= 6 for x in userSequence):
                print("Пожалуйста, введи ровно 4 цифры от 1 до 6, разделенные пробелами.") # Error message in Russian
                continue
        except ValueError:
            print("Пожалуйста, введи целые числа.") # Error message in Russian
            continue
            
        directHits, indirectHits = compare_sequences(targetSequence, userSequence)
        print(f"Прямые попадания: {directHits}, Косвенные попадания: {indirectHits}") # Output hits in Russian
        if directHits == 4:
            print("Поздравляю! Ты угадал последовательность!") # Win message in Russian
            return

    print("Увы, попытки закончились. Ты не угадал последовательность.") # Lose message in Russian
    print(f"Правильная последовательность: {targetSequence}") # Show target sequence in Russian
# Running the game
if __name__ == "__main__":
    play_reverse_game()
```
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש לייצור מספרים אקראיים.
2.  **הפונקציה `generate_target_sequence()`**:
    -   `def generate_target_sequence():`: מגדירה פונקציה לייצור רצף אקראי של 4 ספרות מ-1 עד 6.
    -   `return [random.randint(1, 6) for _ in range(4)]`: משתמשת בהבנת רשימה (list comprehension) ליצירת רשימה של 4 מספרים שלמים אקראיים, כל אחד בטווח שבין 1 ל-6.
3.  **הפונקציה `compare_sequences(target, user)`**:
    -   `def compare_sequences(target, user):`: מגדירה פונקציה להשוואת שני רצפים וספירת פגיעות ישירות ועקיפות.
    -   `direct_hits = 0`: מאתחלת משתנה לספירת פגיעות ישירות.
    -   `indirect_hits = 0`: מאתחלת משתנה לספירת פגיעות עקיפות.
    -   `target_copy = list(target)`: יוצרת עותק של הרצף הנסתר כדי לא לשנות את הרשימה המקורית.
    -   `user_copy = list(user)`: יוצרת עותק של רצף המשתמש כדי לא לשנות את הרשימה המקורית.
    -   **ספירת פגיעות ישירות**:
        -   `for i in range(4):`: לולאה למעבר על כל עמדה ברצף.
        -   `if user_copy[i] == target_copy[i]:`: בודקת האם הספרה בעמדה הנוכחית זהה בשני הרצפים.
        -   `direct_hits += 1`: מגדילה את מספר הפגיעות הישירות ב-1.
        -   `target_copy[i] = None` ו-`user_copy[i] = None`: מסמנת את הספרה כ"בשימוש" כדי לא לספור אותה שוב בעת ספירת פגיעות עקיפות.
    -   **ספירת פגיעות עקיפות**:
        -   `for i in range(4):`: לולאה למעבר על כל עמדה ברצף המשתמש.
        -   `if user_copy[i] is not None:`: בודקת שהספרה לא נוצלה בפגיעות ישירות.
        -   `for j in range(4):`: לולאה למעבר על כל עמדה בעותק של הרצף הנסתר.
        -   `if user_copy[i] == target_copy[j]:`: בודקת האם הספרה מרצף המשתמש קיימת בעותק של הרצף הנסתר.
        -   `indirect_hits += 1`: מגדילה את מספר הפגיעות העקיפות ב-1.
        -   `target_copy[j] = None`: מסמנת את הספרה כ"בשימוש" כדי לא לספור אותה שוב.
        -   `break`: עוברת לספרה הבאה ברצף המשתמש.
    -   `return direct_hits, indirect_hits`: מחזירה את מספר הפגיעות הישירות והעקיפות.
4.  **הפונקציה `play_reverse_game()`**:
    -   `def play_reverse_game():`: מגדירה את פונקציית המשחק הראשית.
    -   `numberOfGuesses = 0`: מאתחלת את מספר הניסיונות.
    -   `targetSequence = generate_target_sequence()`: מייצרת את הרצף הנסתר.
    -   מציגה הודעת קבלת פנים והוראות.
    -   **הלולאה הראשית `while numberOfGuesses < 10:`**:
        -   `numberOfGuesses += 1`: מגדילה את מונה הניסיונות ב-1.
        -   **קלט נתונים**:
            -   `try ... except ValueError`: בלוק לטיפול בשגיאות קלט אפשריות.
            -   `user_input = input(f"...")`: מבקשת מהמשתמש להזין רצף של 4 מספרים המופרדים ברווח. (הודעה ברוסית נשמרה כהוראה, הטקסט עצמו הוא חלק מהקוד)
            -   `userSequence = [int(x) for x in user_input.split()]`: ממירה את המחרוזת שהוזנה לרשימת מספרים שלמים.
            -   `if len(userSequence) != 4 or not all(1 <= x <= 6 for x in userSequence):`: בודקת האם הקלט הוזן כהלכה.
            -   `continue`: מדלגת על איטרציה זו של הלולאה ומבקשת קלט שוב.
        -   `directHits, indirectHits = compare_sequences(targetSequence, userSequence)`: קוראת לפונקציה להשוואת הרצפים.
        -   `print(f"...")`: מציגה את תוצאות ההשוואה. (הודעה ברוסית נשמרה כהוראה, הטקסט עצמו הוא חלק מהקוד)
        -   `if directHits == 4`: בודקת האם הרצף נוחש.
        -   `print("...")`: מציגה הודעה על ניצחון. (הודעה ברוסית נשמרה כהוראה, הטקסט עצמו הוא חלק מהקוד)
        -   `return`: מסיימת את המשחק.
    -   **אם הניסיונות הסתיימו**:
        -   `print("...")`: מציגה הודעה על הפסד. (הודעה ברוסית נשמרה כהוראה, הטקסט עצמו הוא חלק מהקוד)
        -   `print(f"...")`: מציגה את הרצף הנסתר. (הודעה ברוסית נשמרה כהוראה, הטקסט עצמו הוא חלק מהקוד)
5.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בודקת האם הקובץ הופעל כתוכנית ראשית.
    -   `play_reverse_game()`: קוראת לפונקציה כדי להתחיל את המשחק.