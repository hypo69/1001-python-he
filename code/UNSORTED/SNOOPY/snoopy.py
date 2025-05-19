<SNOOPY>:
=================
דרגת קושי: 4
-----------------
המשחק "סנופי" הוא משחק ניחוש מילה, שבו המחשב בוחר מילה אקראית מרשימה, והשחקן מנסה לנחש אותה באמצעות הזנת אות אחת בכל פעם. לאחר כל ניסיון, המחשב מציג אילו אותיות נוחשו נכונה והיכן הן ממוקמות במילה.

חוקי המשחק:
1. המחשב בוחר מילה אקראית מרשימה.
2. השחקן מזין אות אחת.
3. המחשב משווה את האות שהוזנה למילה, ואם היא קיימת, מציג את מיקומה.
4. המשחק ממשיך עד אשר השחקן ינחש את כל אותיות המילה.
5. אם השחקן מנחש את המילה, המשחק מסתיים, ומוצגת הודעת ניצחון.
-----------------
אלגוריתם:
1. הגדרת רשימת מילים לבחירה.
2. בחירת מילה אקראית מהרשימה.
3. יצירת מסיכה עבור המילה (לדוגמה, "----" אם המילה היא "SNOOPY").
4. הגדרת מונה ניסיונות לאפס.
5. התחלת לולאה "כל עוד המילה לא נוחשה":
    5.1. הצגת המצב הנוכחי של המסיכה.
    5.2. הגדלת מונה הניסיונות.
    5.3. בקשת הזנת אות מהשחקן.
    5.4. אם האות שהוזנה קיימת במילה, אז:
        5.4.1. עדכון המסיכה, תוך הצגת מיקום האות.
    5.5. אם המסיכה אינה מכילה את התו "-", לעבור לשלב 6.
6. הצגת ההודעה "YOU GOT IT IN {מספר הניסיונות} GUESSES!" והמילה שנבחרה.
7. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    wordList = ['SNOOPY', 'PEANUTS', 'CHARLIE']
    targetWord = random_word(wordList)
    wordMask = create_mask(targetWord)
    numberOfGuesses = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart --> OutputMask["הצגת מסיכת המילה: <code><b>wordMask</b></code>"]
    OutputMask --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputLetter["הזנת אות מהמשתמש: <code><b>userLetter</b></code>"]
    InputLetter --> CheckLetter{"בדיקה: <code><b>userLetter in targetWord?</b></code>"}
    CheckLetter -- כן --> UpdateMask["<code><b>עדכון wordMask</b></code>"]
    UpdateMask --> CheckWin{"בדיקה: <code><b>'-' in wordMask?</b></code>"}
    CheckWin -- כן --> LoopStart
     CheckWin -- לא --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES! The word was <code>{targetWord}</code></b>"]
    OutputWin --> End["סיום"]
     CheckLetter -- לא --> LoopStart

```
מקרא:
    Start - תחילת התוכנית.
    InitializeVariables - אתחול משתנים: wordList (רשימת מילים), targetWord (המילה שנבחרה נקבעת באופן אקראי), wordMask (מסיכת המילה, מלאה בתווים מקפים (דאשים) בתחילה), numberOfGuesses (מספר הניסיונות) מוגדרת לאפס.
    LoopStart - תחילת הלולאה, שנמשכת, כל עוד המילה לא נוחשה.
    OutputMask - הצגת המצב הנוכחי של מסיכת המילה על המסך (לדוגמה, "S---P-").
    IncreaseGuesses - הגדלת מונה מספר הניסיונות ב-1.
    InputLetter - בקשת הזנת אות מהמשתמש.
    CheckLetter - בדיקה האם האות שהוזנה קיימת במילה שנבחרה.
    UpdateMask - עדכון מסיכת המילה, תוך החלפת מקפים באותיות שנוחשו.
    CheckWin - בדיקה האם נותרו מקפים (-) במסיכת המילה.
    OutputWin - הצגת הודעת ניצחון, אם כל האותיות נוחשו, עם ציון מספר הניסיונות והמילה שנבחרה.
    End - סיום התוכנית.
"""

import random

# פונקציה לבחירת מילה אקראית מרשימה
def choose_word(word_list):
    """בוחרת מילה אקראית מרשימה."""
    return random.choice(word_list)

# פונקציה ליצירת מסיכת מילה
def create_mask(word):
    """יוצרת מסיכת מילה, תוך החלפת אותיות במקפים."""
    return ["-" for _ in word]

# פונקציה לעדכון מסיכת המילה
def update_mask(mask, word, letter):
    """מעדכנת את מסיכת המילה, תוך הצגת האותיות שנוחשו."""
    for i, char in enumerate(word):
        if char == letter:
            mask[i] = letter
    return mask

# פונקציית המשחק הראשית
def play_snoopy_game():
    """מריצה את המשחק "סנופי"."""
    # רשימת מילים לבחירה
    word_list = ["SNOOPY", "PEANUTS", "CHARLIE"]
    # בוחרים מילה אקראית מהרשימה
    target_word = choose_word(word_list).upper()
    # יוצרים מסיכה עבור המילה
    word_mask = create_mask(target_word)
    # אתחול מונה הניסיונות
    number_of_guesses = 0

    # לולאת המשחק הראשית
    while True:
        # הצגת מסיכת המילה הנוכחית
        print(" ".join(word_mask))
        # מגדילים את מונה הניסיונות
        number_of_guesses += 1
        # בקשת הזנת אות מהמשתמש
        user_letter = input("Введите букву: ").upper()

        # בודקים נוכחות של האות שהוזנה במילה
        if user_letter in target_word:
            # מעדכנים את מסיכת המילה
            word_mask = update_mask(word_mask, target_word, user_letter)

        # בודקים האם המילה נוחשה
        if "-" not in word_mask:
            print(f"ПОЗДРАВЛЯЮ! Вы угадали слово за {number_of_guesses} попыток! Слово было: {target_word}")
            break

# מריצים את המשחק
if __name__ == "__main__":
    play_snoopy_game()
"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
   -  `import random`: מייבא את מודול `random`, המשמש ליצירת מילה אקראית מרשימה.

2.  **פונקציה `choose_word(word_list)`**:
    -   `def choose_word(word_list):`: מגדירה פונקציה המקבלת רשימת מילים, `word_list`.
    -   `return random.choice(word_list)`: מחזירה מילה אקראית מהרשימה שהועברה, באמצעות השיטה `random.choice()`.

3.  **פונקציה `create_mask(word)`**:
    -   `def create_mask(word):`: מגדירה פונקציה המקבלת מילה, `word`.
    -   `return ["-" for _ in word]`: מחזירה רשימה שבה מספר המקפים שווה לאורך המילה, ויוצרת מסיכה.

4.  **פונקציה `update_mask(mask, word, letter)`**:
    -  `def update_mask(mask, word, letter):`: מגדירה פונקציה המקבלת את מסיכת המילה `mask`, המילה המקורית `word`, והאות שהוזנה `letter`.
    -   `for i, char in enumerate(word):`: מבצעת איטרציה על תווי המילה עם האינדקסים שלהם, באמצעות הפונקציה `enumerate`.
    -   `if char == letter:`: בודקת האם התו הנוכחי של המילה שווה לאות שהוזנה.
    -  `mask[i] = letter`: אם התו שווה לאות שהוזנה, אז מעדכנת את המסיכה, תוך החלפת המקף באות.
    -   `return mask`: מחזירה את המסיכה המעודכנת.

5.  **פונקציה `play_snoopy_game()`**:
    -   `def play_snoopy_game():`: מגדירה פונקציה המכילה את לוגיקת המשחק "סנופי".
    -   `word_list = ["SNOOPY", "PEANUTS", "CHARLIE"]`: רשימת המילים, שמתוכן תיבחר המילה שנבחרה.
    -   `target_word = choose_word(word_list).upper()`: בוחרת מילה אקראית מהרשימה וממירה אותה לאותיות גדולות.
    -   `word_mask = create_mask(target_word)`: יוצרת מסיכה עבור המילה שנבחרה, באמצעות הפונקציה `create_mask()`.
    -   `number_of_guesses = 0`: מאתחלת את מונה הניסיונות.
   
6.  **לולאת המשחק הראשית `while True:`**:
   -   `while True:`: מריצה לולאה אינסופית, שנמשכת כל עוד השחקן לא ניחש את המילה.
   -   `print(" ".join(word_mask))`: מציגה את המצב הנוכחי של מסיכת המילה על המסך. `join` ממירה רשימת אותיות למחרוזת, מופרדת ברווחים.
   -   `number_of_guesses += 1`: מגדילה את מונה הניסיונות ב-1.
   -   `user_letter = input("Введите букву: ").upper()`: מבקשת הזנת אות מהמשתמש וממירה אותה לאותיות גדולות.
   -   `if user_letter in target_word:`: בודקת האם האות שהוזנה קיימת במילה שנבחרה.
   -   `word_mask = update_mask(word_mask, target_word, user_letter)`: מעדכנת את המסיכה, תוך הצגת האות שנוחשה במיקומה, באמצעות הפונקציה `update_mask()`.
   -   `if "-" not in word_mask:`: בודקת האם במסיכה נותרו עדיין אותיות לא נוחשות, המיוצגות על ידי מקפים.
   -   `print(f"ПОЗДРАВЛЯЮ! Вы угадали слово за {number_of_guesses} попыток! Слово было: {target_word}")`: מציגה הודעת ניצחון עם מספר הניסיונות והמילה שנבחרה.
   -   `break`: יציאה מהלולאה.

7. **הרצת המשחק**:
   -  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_snoopy_game()` תרוץ רק אם הקובץ מבוצע ישירות, ולא מיובא כמודול.
   -  `play_snoopy_game()`: קוראת לפונקציה כדי להתחיל את המשחק.