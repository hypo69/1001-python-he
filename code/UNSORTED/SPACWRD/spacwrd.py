**SPACWRD:**
=================
**דרגת קושי:** 4
-----------------
המשחק "מילת חלל" (Spaceword) הוא משחק טקסטואלי שבו השחקן מנסה לנחש מילה שנבחרה על ידי המחשב, באמצעות הקלדת אותיות. המחשב מציג את המילה עם רווחים במקום האותיות שלא נוחשו. לאחר כל ניסיון, השחקן מקבל מידע אודות מספר האותיות שהוא ניחש נכונה, ויכול להמשיך ולנחש את האותיות שנותרו. המשחק מסתיים כאשר השחקן מנחש את כל אותיות המילה.

**כללי המשחק:**
1. המחשב בוחר מילה אקראית מתוך רשימה נתונה.
2. השחקן רואה את המילה, כאשר כל האותיות הוחלפו ברווחים תחתונים (underscore).
3. השחקן מקליד אות.
4. המחשב בודק האם האות קיימת במילה שנבחרה.
5. אם האות קיימת, המחשב חושף את כל המופעים שלה במילה.
6. אם האות אינה קיימת, לא מוצגת הודעה על כך.
7. המשחק ממשיך עד שכל אותיות המילה נוחשו.
8. לאחר כל ניסיון מוצג המצב הנוכחי של המילה עם האותיות הגלויות ומספר האותיות שנוחשו.
-----------------
**אלגוריתם:**
1. הגדרת רשימת מילים למשחק.
2. בחירת מילה אקראית מהרשימה.
3. אתחול משתנים:
   - מילה עם רווחים תחתונים (המילה הסמויה).
   - מספר האותיות שנוחשו נכונה.
   - מערך של האותיות שנוחשו.
4. התחלת לולאה "כל עוד המילה לא נוחשה":
   4.1 הצגת המצב הנוכחי של המילה (עם אותיות גלויות).
   4.2 בקשת קלט אות מהשחקן.
   4.3 בדיקת קיום האות במילה שנבחרה.
   4.4 אם האות קיימת:
       4.4.1 עדכון המילה הסמויה: חשיפת כל מופעי האות.
       4.4.2 עדכון מערך האותיות שנוחשו.
       4.4.3 עדכון מונה האותיות שנוחשו.
   4.5 אם כל אותיות המילה גלויות, עבור לשלב 5.
5. הצגת ההודעה "YOU GOT IT!".
6. סוף המשחק.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    wordList = ['APPLE', 'BANANA', 'CHERRY', ...]
    targetWord = random_word(wordList)
    guessedWord = '_' * len(targetWord)
    guessedLetters = []
    correctGuesses = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart -- Да --> OutputWord["Вывод: <code><b>guessedWord</b></code>"]
    OutputWord --> InputLetter["Ввод буквы пользователем: <code><b>userLetter</b></code>"]
    InputLetter --> CheckLetter{"Проверка: <code><b>userLetter in targetWord?</b></code>"}
    CheckLetter -- Да --> UpdateWord["<p align='left'>Обновление:
    <code><b>
    guessedWord = reveal_letters(targetWord, guessedWord, userLetter)
    guessedLetters.append(userLetter)
    correctGuesses = correct_guesses(guessedLetters,targetWord)

    </b></code></p>"]
     UpdateWord --> CheckWin{ "Проверка:<code><b>correctGuesses == len(targetWord)?</b></code>"}
    CheckLetter -- Нет --> CheckWin
    CheckWin -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT!</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> LoopStart
    LoopStart -- Нет --> End
    

```
**מקרא:**
   * **Start** - התחלת המשחק.
   * **InitializeVariables** - אתחול משתנים:
        - `wordList` - רשימת המילים למשחק.
        - `targetWord` - המילה שנבחרה באופן אקראי מהרשימה.
        - `guessedWord` - המילה שהשחקן רואה עם רווחים תחתונים במקום אותיות.
        - `guessedLetters` - רשימת האותיות שנוחשו.
        - `correctGuesses` - מספר האותיות שנוחשו נכונה.
   * **LoopStart** - התחלת לולאת המשחק, שנמשכת כל עוד המילה לא נוחשה.
   * **OutputWord** - הצגת המצב הנוכחי של המילה, עם האותיות הגלויות (אם נוחשו).
   * **InputLetter** - בקשת קלט של אות מהמשתמש.
   * **CheckLetter** - בדיקה האם האות שהוזנה קיימת במילה שנבחרה.
   * **UpdateWord** - עדכון המילה: חשיפת כל מופעי האות שהוזנה והוספתה לרשימת האותיות שנוחשו, וספירת האותיות שנוחשו.
   * **CheckWin** - בדיקה האם כל אותיות המילה נוחשו.
   * **OutputWin** - הצגת הודעת הניצחון.
   * **End** - סוף המשחק.
"""


import random

def choose_word(word_list):
    """בוחר מילה אקראית מתוך הרשימה."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
  """מציג את המילה, מסתיר אותיות שלא נוחשו."""
  display = ""
  for letter in word:
    if letter in guessed_letters:
      display += letter + " "
    else:
      display += "_ "
  return display.strip()

def update_word(word, guessed_word, user_letter):
    """מעדכן את המילה המוצגת, חושף אותיות שנוחשו."""
    updated_word = ""
    for i in range(len(word)):
        if word[i] == user_letter:
          updated_word += user_letter + " "
        else:
            updated_word += guessed_word[i*2] + " "
    return updated_word.strip()


def correct_guesses(guessed_letters, target_word):
    """
    סופר את מספר האותיות שנוחשו נכונה במילה.
    """
    count = 0
    unique_letters = set(target_word)
    for letter in guessed_letters:
        if letter in unique_letters:
            count += 1
            unique_letters.remove(letter)
    return len(set(target_word)) - len(unique_letters)


def play_spaceword_game():
    """הלוגיקה הראשית של המשחק "מילת חלל"."""
    word_list = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "KIWI", "LEMON", "MANGO",
    "ORANGE", "PEACH", "QUINCE", "RASPBERRY", "STRAWBERRY", "TANGERINE", "WATERMELON"
    ]
    target_word = choose_word(word_list) # בוחרים מילה
    guessed_word = "_ " * len(target_word) # יוצרים מילה סמויה
    guessed_letters = []  # רשימת אותיות שנוחשו
    correct_guesses_count = 0
    
    print("ברוכים הבאים למשחק 'מילת חלל'!")
    print("חשבתי על מילה. נסו לנחש אותה על ידי הקלדת אותיות אחת בכל פעם.")
    

    while correct_guesses_count < len(target_word):
        print("\nמילה:", guessed_word)
        user_letter = input("הקלידו אות: ").upper() # מבקשים אות
        
        if user_letter in target_word:
            guessed_letters.append(user_letter)
            guessed_word = update_word(target_word, guessed_word, user_letter)
            correct_guesses_count = correct_guesses(guessed_letters, target_word)
        else:
            print("האות הזו לא קיימת במילה.")

        
        if correct_guesses_count == len(target_word):
           print("\nYOU GOT IT!")
           break

if __name__ == "__main__":
    play_spaceword_game()
"""
**הסבר הקוד:**
1. **ייבוא מודול `random`**:
   - `import random`: מייבא את מודול `random` לבחירת מילה אקראית.

2. **פונקציה `choose_word(word_list)`**:
   - מקבלת רשימת מילים `word_list` כארגומנט.
   - `return random.choice(word_list)`: מחזירה מילה אקראית מהרשימה.

3. **פונקציה `display_word(word, guessed_letters)`**:
   - מקבלת את המילה `word` ואת רשימת האותיות שנוחשו `guessed_letters`.
   - יוצרת מחרוזת `display`, שבה מוצגות האותיות מתוך `word` אם הן נמצאות ב-`guessed_letters`, או התו `_` אחרת.
   - מחזירה את המילה להצגה.

4. **פונקציה `update_word(word, guessed_word, user_letter)`**:
    -   מקבלת את המילה שנבחרה `word`, את ההצגה הנוכחית של המילה `guessed_word`, ואת האות שהוזנה על ידי המשתמש `user_letter`.
    -   יוצרת מחרוזת `updated_word`, שבתחילה ריקה.
    -   באמצעות לולאת `for` בודקת כל אות במילה `word`.
    -   אם האות הנוכחית שווה ל-`user_letter`, היא מוסיפה אותה ל-`updated_word` עם רווח.
    -   אחרת, מוסיפה את התו מתוך `guessed_word` (התו במיקום המתאים, תוך התחשבות ברווחים).
    -   מחזירה את המחרוזת המעודכנת עם אותיות גלויות.

5. **פונקציה `correct_guesses(guessed_letters, target_word)`**:
    -  מקבלת רשימת אותיות שנוחשו `guessed_letters` ואת המילה שנבחרה `target_word`.
    -  יוצרת קבוצה (set) `unique_letters` מאותיות המילה `target_word` כדי לעקוב אחר אותיות ייחודיות.
    -  באמצעות לולאת `for` סופרת כמה אותיות מתוך `guessed_letters` קיימות במילה.
    -  מוציאה את האותיות שכבר נספרו מ-`unique_letters`.
    -  מחזירה את מספר האותיות שנוחשו, השווה להפרש בין אורך קבוצת האותיות הייחודיות לאורך הקבוצה שנותרה.

6. **פונקציה `play_spaceword_game()`**:
   - הפונקציה הראשית של המשחק.
   - `word_list`: רשימת מילים למשחק.
   - `target_word = choose_word(word_list)`: בוחרת מילה אקראית.
    -   `guessed_word = "_ " * len(target_word)`: יוצרת מחרוזת המייצגת את המילה, שבה כל האותיות מוחלפות ברווחים תחתונים.
   -   `guessed_letters = []`: יוצרת רשימה ריקה לאחסון האותיות שנוחשו.
   -   מציגה הודעת פתיחה ותיאור המשחק.
   -   **לולאת המשחק הראשית `while True`**:
      -   `print("\nמילה:", guessed_word)`: מציגה את המצב הנוכחי של המילה.
      -   `user_letter = input("הקלידו אות: ").upper()`: מבקשת קלט של אות וממירה אותה לאות גדולה.
      -    **בדיקת האות שהוזנה:**
        -   `if user_letter in target_word:`: אם האות קיימת במילה שנבחרה, מוסיפים אותה לרשימת האותיות שנוחשו, מעדכנים את המילה ואת המונה.
        -   `else:`: אם האות לא קיימת במילה, מציגים הודעת שגיאה.
        -   אם מספר האותיות שנוחשו שווה למספר האותיות במילה, מוצגת הודעת ניצחון והלולאה מסתיימת.

7. **הפעלת המשחק**:
   - `if __name__ == "__main__":`: מפעיל את הפונקציה `play_spaceword_game()` אם הסקריפט מורץ ישירות.
   - `play_spaceword_game()`: קריאה לפונקציה להתחלת המשחק.
"""
```