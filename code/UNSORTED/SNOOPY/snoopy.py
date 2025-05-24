<SNOOPY>:
=================
מורכבות: 4
-----------------
המשחק "סנופי" הוא משחק ניחוש מילים, בו המחשב בוחר מילה אקראית מתוך רשימה, והשחקן מנסה לנחש אותה באמצעות הזנת אות אחת בכל פעם. לאחר כל ניסיון, המחשב מציג אילו אותיות נוחשו נכון והיכן הן ממוקמות במילה.

כללי המשחק:
1.  המחשב בוחר מילה אקראית מתוך הרשימה.
2.  השחקן מזין אות אחת.
3.  המחשב משווה את האות המוזנת למילה, ואם היא קיימת, הוא מציג את מיקומה.
4.  המשחק נמשך עד שהשחקן מנחש את כל אותיות המילה.
5.  אם השחקן מנחש את המילה, המשחק מסתיים ומוצגת הודעת ניצחון.
-----------------
אלגוריתם:
1.  הגדרת רשימת מילים לבחירה.
2.  בחירת מילה אקראית מתוך הרשימה.
3.  יצירת מסכה למילה (לדוגמה, "----" אם המילה היא "SNOOPY").
4.  אתחול מונה הניסיונות ל-0.
5.  התחלת לולאה "כל עוד המילה לא נוחשה":
    5.1. הצגת המצב הנוכחי של המסכה.
    5.2. הגדלת מונה הניסיונות.
    5.3. בקשת הזנת אות מהשחקן.
    5.4. אם האות המוזנת קיימת במילה, אז:
        5.4.1. עדכון המסכה, הצגת מיקום האות.
    5.5. אם המסכה אינה מכילה את התו "-", עבור לשלב 6.
6.  הצגת ההודעה "YOU GOT IT IN {מספר הניסיונות} GUESSES!" והמילה שנבחרה.
7.  סיום המשחק.
-----------------
דיאגרמת זרימה:
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
    LoopStart --> OutputMask["הצגת מסכת המילה: <code><b>wordMask</b></code>"]
    OutputMask --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputLetter["קלט אות מהמשתמש: <code><b>userLetter</b></code>"]
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
    InitializeVariables - אתחול משתנים: wordList (רשימת מילים), targetWord (המילה שנבחרה באקראי), wordMask (מסכת המילה, הממולאת תחילה במקפים), numberOfGuesses (מספר הניסיונות) מוגדר ל-0.
    LoopStart - תחילת לולאה, הנמשכת כל עוד המילה לא נוחשה.
    OutputMask - הצגת המצב הנוכחי של מסכת המילה על המסך (לדוגמה, "S---P-").
    IncreaseGuesses - הגדלת מונה מספר הניסיונות ב-1.
    InputLetter - בקשת הזנת אות מהמשתמש.
    CheckLetter - בדיקה, האם האות המוזנת קיימת במילה שנבחרה.
    UpdateMask - עדכון מסכת המילה, החלפת מקפים באותיות נוחשות.
    CheckWin - בדיקה, האם נותרו במסיכת המילה מקפים (-).
    OutputWin - הצגת הודעת ניצחון, אם כל האותיות נוחשו, בציון מספר הניסיונות והמילה שנבחרה.
    End - סיום התוכנית.
```

```python
import random

# פונקציה לבחירת מילה אקראית מתוך רשימה
def choose_word(word_list):
    """בוחרת מילה אקראית מתוך הרשימה."""
    return random.choice(word_list)

# פונקציה ליצירת מסכת מילה
def create_mask(word):
    """יוצרת מסכת מילה, מחליפה אותיות במקפים."""
    return ["-" for _ in word]

# פונקציה לעדכון מסכת המילה
def update_mask(mask, word, letter):
    """מעדכנת את מסכת המילה, מציגה את האותיות הנוחשות."""
    for i, char in enumerate(word):
        if char == letter:
            mask[i] = letter
    return mask

# הפונקציה הראשית של המשחק
def play_snoopy_game():
    """מריצה את המשחק 'סנופי'."""
    # רשימת מילים לבחירה
    word_list = ["SNOOPY", "PEANUTS", "CHARLIE"]
    # בוחרים מילה אקראית מתוך הרשימה
    target_word = choose_word(word_list).upper()
    # יוצרים מסכה למילה
    word_mask = create_mask(target_word)
    # אתחול מונה הניסיונות
    number_of_guesses = 0

    # לולאת המשחק הראשית
    while True:
        # הצגת מסכת המילה הנוכחית
        print(" ".join(word_mask))
        # מגדילים את מונה הניסיונות
        number_of_guesses += 1
        # בקשת קלט אות מהמשתמש
        user_letter = input("הזן אות: ").upper()

        # בודקים קיום האות המוזנת במילה
        if user_letter in target_word:
            # מעדכנים את מסכת המילה
            word_mask = update_mask(word_mask, target_word, user_letter)

        # בודקים האם המילה נוחשה
        if "-" not in word_mask:
            print(f"כל הכבוד! ניחשת את המילה ב- {number_of_guesses} ניסיונות! המילה הייתה: {target_word}")
            break

# מריצים את המשחק
if __name__ == "__main__":
    play_snoopy_game()
```
```
הסבר הקוד:
1.  **ייבוא מודול \`random\`**:
   -  \`import random\`: מייבא את מודול \`random\`, המשמש ליצירת מילה אקראית מתוך הרשימה.

2.  **פונקציה \`choose_word(word_list)\`**:
    -   \`def choose_word(word_list):\`: מגדירה פונקציה המקבלת רשימת מילים \`word_list\`.
    -   \`return random.choice(word_list)\`: מחזירה מילה אקראית מתוך הרשימה שהועברה, באמצעות שימוש במתודה \`random.choice()\`.

3.  **פונקציה \`create_mask(word)\`**:
    -   \`def create_mask(word):\`: מגדירה פונקציה המקבלת מילה \`word\`.
    -   \`return ["-" for _ in word]\`: מחזירה רשימה שבה מספר המקפים שווה לאורך המילה, ויוצרת מסכה.

4.  **פונקציה \`update_mask(mask, word, letter)\`**:
    -  \`def update_mask(mask, word, letter):\`: מגדירה פונקציה המקבלת את מסכת המילה \`mask\`, את המילה המקורית \`word\` ואת האות המוזנת \`letter\`.
    -   \`for i, char in enumerate(word):\`: מבצע איטרציה על תווי המילה יחד עם האינדקסים שלהם, תוך שימוש בפונקציה \`enumerate\`.
    -   \`if char == letter:\`: בודקת האם התו הנוכחי במילה שווה לאות המוזנת.
    -  \`mask[i] = letter\`: אם התו שווה לאות המוזנת, אז היא מעדכנת את המסכה, ומחליפה את המקף באות.
    -   \`return mask\`: מחזירה את המסכה המעודכנת.

5.  **פונקציה \`play_snoopy_game()\`**:
    -   \`def play_snoopy_game():\`: מגדירה פונקציה המכילה את לוגיקת המשחק "סנופי".
    -   \`word_list = ["SNOOPY", "PEANUTS", "CHARLIE"]\`: רשימת מילים, מתוכן תיבחר המילה לנחש.
    -   \`target_word = choose_word(word_list).upper()\`: בוחרת מילה אקראית מתוך הרשימה וממירה אותה לאותיות גדולות.
    -   \`word_mask = create_mask(target_word)\`: יוצרת מסכה למילה הנבחרת, תוך שימוש בפונקציה \`create_mask()\`.
    -   \`number_of_guesses = 0\`: מאתחלת את מונה הניסיונות.

6.  **לולאת המשחק הראשית \`while True:\`**:
   -   \`while True:\`: מריצה לולאה אינסופית, הנמשכת כל עוד השחקן לא ניחש את המילה.
   -   \`print(" ".join(word_mask))\`: מציגה את המצב הנוכחי של מסכת המילה על המסך. \`join\` ממירה רשימת אותיות למחרוזת המופרדת באמצעות רווחים.
   -   \`number_of_guesses += 1\`: מגדילה את מונה הניסיונות ב-1.
   -   \`user_letter = input("הזן אות: ").upper()\`: מבקשת קלט אות מהמשתמש וממירה אותה לאותיות גדולות.
   -   \`if user_letter in target_word:\`: בודקת האם האות המוזנת קיימת במילה לנחש.
   -   \`word_mask = update_mask(word_mask, target_word, user_letter)\`: מעדכנת את המסכה, מציגה את האות שנוחשה במיקומה, תוך שימוש בפונקציה \`update_mask()\`.
   -   \`if "-" not in word_mask:\`: בודקת האם נותרו במסכה אותיות שעדיין לא נוחשו, המיוצגות על ידי מקפים.
   -   \`print(f"כל הכבוד! ניחשת את המילה ב- {number_of_guesses} ניסיונות! המילה הייתה: {target_word}")\`: מציגה הודעת ניצחון עם מספר הניסיונות והמילה שנבחרה.
   -   \`break\`: יציאה מהלולאה.

7. **הפעלת המשחק**:
   -  \`if __name__ == "__main__":\`: בלוק זה מבטיח שהפונקציה \`play_snoopy_game()\` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
   -  \`play_snoopy_game()\`: קוראת לפונקציה כדי להתחיל את המשחק.