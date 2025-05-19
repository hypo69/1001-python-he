"""
REVRSE:
=================
קושי: 5
-----------------
המשחק "REVRSE" מזמין את השחקן לנחש רצף של 4 ספרות, אשר ממוקמות בסדר מסוים, תוך אפשרות לחזרה על ספרות.
לאחר כל מהלך של השחקן, המחשב מציג את כמות הספרות שנניח כהלכה ואת כמות הספרות הקיימות ברצף המבוקש אך אינן נמצאות במקומן הנכון.
המשחק נמשך עד שהשחקן מנחש את רצף הספרות, או עד שנגמר מספר הניסיונות.

חוקי המשחק:
1.  המחשב מייצר רצף אקראי של 4 ספרות מ-1 עד 6, הספרות עשויות לחזור על עצמן.
2.  השחקן מזין את הרצף שלו המורכב מ-4 ספרות, גם כן מ-1 עד 6, ומפריד בין הספרות ברווחים.
3.  לאחר כל ניסיון, המחשב מציג:
    -   כמות הספרות שנניח כהלכה במקומן (התאמה מדויקת).
    -   כמות הספרות שנניח כהלכה אך קיימות ברצף המבוקש ולא במקומן הנכון (התאמה חלקית).
4.  המשחק מסתיים כאשר השחקן מנחש את הרצף או לאחר 10 ניסיונות.
-----------------
אלגוריתם:
1.  אפס את מונה הניסיונות (numberOfGuesses).
2.  הפק רצף אקראי של 4 ספרות מ-1 עד 6 (targetSequence).
3.  התחל בלולאה "כל עוד מספר הניסיונות קטן מ-10":
    3.1 הגדל את מונה הניסיונות ב-1.
    3.2 בקש מהשחקן להזין רצף של 4 ספרות (userSequence).
    3.3 השווה את userSequence ל-targetSequence:
        -   ספור את מספר ההתאמות המדויקות (ספרות במקומן).
        -   ספור את מספר ההתאמות החלקיות (ספרות קיימות אך לא במקומן).
    3.4 הצג את מספר ההתאמות המדויקות והחלקיות.
    3.5 אם מספר ההתאמות המדויקות שווה ל-4, הצג הודעת ניצחון וסיים את המשחק.
4.  אם הלולאה הסתיימה (לאחר 10 ניסיונות), הצג הודעת הפסד והראה את הרצף הנכון.
5.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code><b>
    numberOfGuesses = 0
    targetSequence = random sequence of 4 numbers (1 to 6)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד numberOfGuesses < 10"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputSequence["קלט רצף מהמשתמש: <code><b>userSequence</b></code>"]
    InputSequence --> CompareSequences["<p align='left'>השוואת רצפים:<br><code><b>
    directHits = count of numbers in correct position<br>
    indirectHits = count of numbers present but in wrong position
    </b></code></p>"]
    CompareSequences --> OutputHits["פלט: <b>directHits, indirectHits</b>"]
    OutputHits --> CheckWin{"בדיקה: <code><b>directHits == 4?</b></code>"}
    CheckWin -- כן --> OutputWin["פלט הודעת ניצחון"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> LoopStart
    LoopStart -- לא --> OutputLose["פלט הודעת הפסד"]
    OutputLose --> ShowTarget["פלט: <b>targetSequence</b>"]
    ShowTarget --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מונה ניסיונות) מאופס ל-0, ו-targetSequence (הרצף המבוקש) נוצר באופן אקראי מ-4 מספרים מ-1 עד 6.
    LoopStart - התחלת הלולאה, שנמשכת כל עוד מספר הניסיונות numberOfGuesses קטן מ-10.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputSequence - בקשת קלט רצף של 4 מספרים מהמשתמש.
    CompareSequences - השוואת הרצף שהוזן לרצף המבוקש וספירת התאמות מדויקות וחלקיות.
    OutputHits - הצגת מספר ההתאמות המדויקות והחלקיות.
    CheckWin - בדיקה האם מספר ההתאמות המדויקות שווה ל-4.
    OutputWin - הצגת הודעת ניצחון.
    End - סוף התוכנית.
    OutputLose - הצגת הודעת הפסד.
    ShowTarget - הצגת הרצף המבוקש.
"""
import random

# פונקציה ליצירת רצף אקראי של 4 ספרות מ-1 עד 6
def generate_target_sequence():
    return [random.randint(1, 6) for _ in range(4)]

# פונקציה להשוואת רצפים וספירת התאמות
def compare_sequences(target, user):
    direct_hits = 0 # התאמות מדויקות (ספרה במקומה)
    indirect_hits = 0 # התאמות חלקיות (ספרה קיימת, אך לא במקומה)
    target_copy = list(target) # יוצרים עותק של הרצף המבוקש כדי לא לשנות את המקור

    # סופרים התאמות מדויקות ומסמנים אותן בעותק
    for i in range(4):
        if user[i] == target_copy[i]:
            direct_hits += 1
            target_copy[i] = None # מסמנים כדי לא לספור שנית
            user[i] = None # מסמנים כדי לא לספור שנית

    # סופרים התאמות חלקיות
    for i in range(4):
      if user[i] is not None:
        for j in range(4):
            if user[i] == target_copy[j]:
                indirect_hits += 1
                target_copy[j] = None
                break
    return direct_hits, indirect_hits

# לוגיקת המשחק העיקרית
def play_reverse_game():
    numberOfGuesses = 0  # מונה ניסיונות
    targetSequence = generate_target_sequence()  # הרצף המבוקש

    print("ברוכים הבאים למשחק REVRSE!")
    print("חישבתי רצף של 4 ספרות (מ-1 עד 6).")
    print("נסה לנחש אותו. יש לך 10 ניסיונות.")

    while numberOfGuesses < 10:
        numberOfGuesses += 1
        try:
            user_input = input(f"ניסיון {numberOfGuesses}. הזן 4 ספרות עם רווח ביניהן (לדוגמה, 1 2 3 4): ")
            userSequence = [int(x) for x in user_input.split()]
            if len(userSequence) != 4 or not all(1 <= x <= 6 for x in userSequence):
                print("אנא הזן בדיוק 4 ספרות מ-1 עד 6, מופרדות ברווחים.")
                continue
        except ValueError:
            print("אנא הזן מספרים שלמים.")
            continue
            
        directHits, indirectHits = compare_sequences(targetSequence, userSequence)
        print(f"התאמות מדויקות: {directHits}, התאמות חלקיות: {indirectHits}")
        if directHits == 4:
            print("ברכות! ניחשת את הרצף!")
            return

    print("למרבה הצער, הניסיונות נגמרו. לא ניחשת את הרצף.")
    print(f"הרצף הנכון: {targetSequence}")
# הפעלת המשחק
if __name__ == "__main__":
    play_reverse_game()
"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים.
2.  **פונקציה `generate_target_sequence()`**:
    -   `def generate_target_sequence():`: מגדירה פונקציה ליצירת רצף אקראי של 4 ספרות מ-1 עד 6.
    -   `return [random.randint(1, 6) for _ in range(4)]`: משתמשת בהבנת רשימות (list comprehension) ליצירת רשימה של 4 מספרים שלמים אקראיים, כל אחד בטווח מ-1 עד 6.
3.  **פונקציה `compare_sequences(target, user)`**:
    -   `def compare_sequences(target, user):`: מגדירה פונקציה להשוואת שני רצפים וספירת התאמות מדויקות וחלקיות.
    -   `direct_hits = 0`: מאתחל משתנה לספירת התאמות מדויקות.
    -   `indirect_hits = 0`: מאתחל משתנה לספירת התאמות חלקיות.
    -   `target_copy = list(target)`: יוצרת עותק של הרצף המבוקש כדי לא לשנות את הרשימה המקורית.
    -   **ספירת התאמות מדויקות**:
        -   `for i in range(4):`: לולאה לעבור על כל עמדה ברצף.
        -   `if user[i] == target_copy[i]:`: בודקת האם הספרה בעמדה הנוכחית זהה בשני הרצפים.
        -   `direct_hits += 1`: מגדילה את מספר ההתאמות המדויקות ב-1.
        -   `target_copy[i] = None` וגם `user[i] = None`: מסמנת את הספרה ככזו שנוצלה, כדי לא לספור אותה שנית בעת ספירת התאמות חלקיות.
    -   **ספירת התאמות חלקיות**:
        -   `for i in range(4):`: לולאה לעבור על כל עמדה ברצף המשתמש.
        -   `if user[i] is not None:`: בודקת שהספרה לא נוצלה בהתאמות מדויקות
        -   `for j in range(4):`: לולאה לעבור על כל עמדה בעותק של הרצף המבוקש.
        -   `if user[i] == target_copy[j]:`: בודקת האם הספרה מרצף המשתמש קיימת בעותק של הרצף המבוקש
        -   `indirect_hits += 1`: מגדילה את מספר ההתאמות החלקיות ב-1
        -   `target_copy[j] = None`: מסמנת את הספרה ככזו שנוצלה, כדי לא לספור שנית.
        -   `break`: עוברת לספרה הבאה ברצף המשתמש.
    -   `return direct_hits, indirect_hits`: מחזירה את מספר ההתאמות המדויקות והחלקיות.
4.  **פונקציה `play_reverse_game()`**:
    -   `def play_reverse_game():`: מגדירה את פונקציית המשחק העיקרית.
    -   `numberOfGuesses = 0`: מאתחל את מונה הניסיונות.
    -   `targetSequence = generate_target_sequence()`: יוצר את הרצף המבוקש.
    -   הצגת הודעת פתיחה והוראות.
    -   **הלולאה הראשית `while numberOfGuesses < 10:`**:
        -   `numberOfGuesses += 1`: מגדילה את מונה הניסיונות ב-1.
        -   **קלט נתונים**:
            -   `try ... except ValueError`: בלוק לטיפול בשגיאות קלט אפשריות.
            -   `user_input = input(f"ניסיון {numberOfGuesses}. הזן 4 ספרות עם רווח ביניהן (לדוגמה, 1 2 3 4): ")`: מבקש מהמשתמש להזין רצף של 4 מספרים מופרדים ברווח.
            -   `userSequence = [int(x) for x in user_input.split()]`: ממירה את המחרוזת שהוזנה לרשימה של מספרים שלמים.
            -   `if len(userSequence) != 4 or not all(1 <= x <= 6 for x in userSequence):`: בודקת האם הנתונים הוזנו כראוי.
            -   `continue`: מדלגת על איטרציית הלולאה הנוכחית ומבקשת נתונים שוב.
        -   `directHits, indirectHits = compare_sequences(targetSequence, userSequence)`: קוראת לפונקציה להשוואת רצפים.
        -   `print(f"התאמות מדויקות: {directHits}, התאמות חלקיות: {indirectHits}")`: מציגה את תוצאות ההשוואה.
        -   `if directHits == 4`: בודקת האם הרצף נוחש.
        -   `print("ברכות! ניחשת את הרצף!")`: מציגה הודעת ניצחון.
        -   `return`: מסיימת את המשחק.
    -   **אם הניסיונות הסתיימו**:
        -   `print("למרבה הצער, הניסיונות נגמרו. לא ניחשת את הרצף.")`: מציגה הודעת הפסד.
        -   `print(f"הרצף הנכון: {targetSequence}")`: מציגה את הרצף המבוקש.
5.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בודקת האם הקובץ הופעל כתוכנית ראשית.
    -   `play_reverse_game()`: קוראת לפונקציה להפעלת המשחק.
"""