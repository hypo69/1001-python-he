SPACWRD:
=================
רמת מורכבות: 4
-----------------
המשחק "מילת החלל" הוא משחק מבוסס טקסט שבו השחקן מנסה לנחש מילה שהמחשב הגריל, באמצעות הזנת אותיות. המחשב מציג את המילה עם רווחים במקום האותיות שלא נוחשו. לאחר כל ניסיון, השחקן מקבל מידע על מספר האותיות שהוא ניחש נכונה, ויכול להמשיך ולנחש את האותיות הנותרות. המשחק מסתיים כאשר השחקן מנחש את כל אותיות המילה.

חוקי המשחק:
1. המחשב בוחר מילה אקראית מרשימת מילים נתונה.
2. השחקן רואה את המילה כשכל האותיות בה מוחלפות ברווחים.
3. השחקן מזין אות.
4. המחשב בודק אם האות קיימת במילה שהוגרלה.
5. אם האות קיימת, המחשב חושף את כל מיקומיה במילה.
6. אם האות אינה קיימת, לא מוצגת הודעה על כך.
7. המשחק ממשיך עד שכל אותיות המילה נוחשו.
8. לאחר כל ניסיון, מוצג מצב המילה הנוכחי עם האותיות הגלויות ומספר האותיות שנוחשו.
-----------------
אלגוריתם:
1. הגדר רשימת מילים למשחק.
2. בחר מילה אקראית מהרשימה.
3. אתחל משתנים:
   - מילה עם רווחים (המילה החסויה)
   - מספר האותיות שנוחשו נכונה
   - מערך של האותיות שנוחשו.
4. התחל לולאה "כל עוד המילה לא נוחשה":
   4.1 הצג את מצב המילה הנוכחי (עם האותיות הגלויות)
   4.2 בקש מהשחקן להזין אות.
   4.3 בדוק נוכחות האות במילה שהוגרלה.
   4.4 אם האות קיימת:
       4.4.1 עדכן את המילה החסויה: חשוף את כל מיקומי האות הזו
       4.4.2 עדכן את מערך האותיות שנוחשו.
       4.4.3 עדכן את מונה האותיות שנוחשו
   4.5 אם כל אותיות המילה נחשפו, עבור לשלב 5.
5. הצג הודעה "YOU GOT IT!".
6. סוף המשחק.
-----------------
תרשים זרימה:
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
        - `wordList` - רשימת מילים למשחק.
        - `targetWord` - המילה שנבחרה באקראי מהרשימה.
        - `guessedWord` - המילה שהשחקן רואה עם רווחים במקום אותיות.
        - `guessedLetters` - רשימת האותיות שנוחשו.
        - `correctGuesses` - מספר האותיות שנוחשו נכונה.
   * **LoopStart** - תחילת לולאת המשחק, הנמשכת כל עוד המילה לא נוחשה.
   * **OutputWord** - הצגת מצב המילה הנוכחי, עם אותיות גלויות (אם נוחשו).
   * **InputLetter** - בקשת קלט אות מהמשתמש.
   * **CheckLetter** - בדיקה אם האות שהוזנה קיימת במילה שהוגרלה.
   * **UpdateWord** - עדכון המילה: חשיפת כל מיקומי האות שהוזנה והוספת האות לרשימת האותיות שנוחשו וספירת האותיות שנוחשו.
   * **CheckWin** - בדיקה אם כל אותיות המילה נוחשו.
   * **OutputWin** - הצגת הודעת ניצחון.
   * **End** - סוף המשחק.
"""


import random

def choose_word(word_list):
    """בוחר מילה אקראית מתוך רשימה."""
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
    """לוגיקה ראשית של המשחק "מילת החלל"."""
    word_list = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "KIWI", "LEMON", "MANGO",
    "ORANGE", "PEACH", "QUINCE", "RASPBERRY", "STRAWBERRY", "TANGERINE", "WATERMELON"
    ]
    target_word = choose_word(word_list) # בוחרים מילה
    guessed_word = "_ " * len(target_word) # יוצרים מילה חסויה
    guessed_letters = []  # רשימת אותיות שנוחשו
    correct_guesses_count = 0
    
    print("ברוכים הבאים למשחק 'מילת החלל'!")
    print("הגרלתי מילה. נסה לנחש אותה, על ידי הזנת אות אחר אות.")
    

    while correct_guesses_count < len(target_word):
        print("\nמילה:", guessed_word)
        user_letter = input("הזן אות: ").upper() # מבקשים אות
        
        if user_letter in target_word:
            guessed_letters.append(user_letter)
            guessed_word = update_word(target_word, guessed_word, user_letter)
            correct_guesses_count = correct_guesses(guessed_letters, target_word)
        else:
            print("אות כזו אינה קיימת במילה.")

        
        if correct_guesses_count == len(target_word):
           print("\nYOU GOT IT!")
           break

if __name__ == "__main__":
    play_spaceword_game()
"""
הסבר הקוד:
1. **ייבוא המודול `random`**:
   - `import random`: מייבא את המודול `random` לבחירת מילה אקראית.

2. **הפונקציה `choose_word(word_list)`**:
   - מקבלת רשימת מילים `word_list` כארגומנט.
   - `return random.choice(word_list)`: מחזירה מילה אקראית מהרשימה.

3. **הפונקציה `display_word(word, guessed_letters)`**:
   - מקבלת מילה `word` ורשימה של אותיות שנוחשו `guessed_letters`.
   - יוצרת מחרוזת `display`, שבה מוצגות אותיות מתוך `word` אם הן קיימות ב-`guessed_letters` או התו `_`.
   - מחזירה את המילה להצגה.

4. **הפונקציה `update_word(word, guessed_word, user_letter)`**:
    - מקבלת את המילה שהוגרלה `word`, את התצוגה הנוכחית של המילה `guessed_word`, ואת האות שהוזנה על ידי המשתמש `user_letter`.
    - יוצרת מחרוזת `updated_word`, שבתחילה ריקה.
    - באמצעות לולאת `for` בודקת כל אות במילה `word`.
    - אם האות הנוכחית שווה ל-`user_letter`, אז מוסיפה אותה ל-`updated_word` עם רווח.
    - אחרת, מוסיפה את התו מ-`guessed_word`.
    - מחזירה את המחרוזת המעודכנת עם האותיות הגלויות.

5. **הפונקציה `correct_guesses(guessed_letters, target_word)`**:
    - מקבלת רשימת אותיות שנוחשו `guessed_letters` ואת המילה שהוגרלה `target_word`.
    - יוצרת קבוצה `unique_letters` מתוך אותיות המילה `target_word` למעקב אחר אותיות ייחודיות.
    - באמצעות לולאת `for` סופרת כמה אותיות מתוך `guessed_letters` קיימות במילה.
    - מוציאה את האותיות שכבר נספרו מתוך `unique_letters`.
    - מחזירה את מספר האותיות שנוחשו, שהוא שווה להפרש בין אורך קבוצת האותיות הייחודיות ואורך הקבוצה שנותרה.

6. **הפונקציה `play_spaceword_game()`**:
   - הפונקציה הראשית של המשחק.
   - `word_list`: רשימת מילים למשחק.
   - `target_word = choose_word(word_list)`: בוחרת מילה אקראית.
    - `guessed_word = "_ " * len(target_word)`: יוצרת מחרוזת המייצגת את המילה, שבה כל האותיות הוחלפו ברווחים.
   - `guessed_letters = []`: יוצרת רשימה ריקה לאחסון אותיות שנוחשו.
   - מציגה ברכת כניסה ותיאור המשחק.
   - **לולאת המשחק הראשית `while True`**:
      - `print("\nСлово:", guessed_word)`: מציגה את מצב המילה הנוכחי. **[System note: The string literal "Слово:" should be translated]**
      - `user_letter = input("Введите букву: ").upper()`: מבקשת קלט אות וממירה אותה לאות גדולה. **[System note: The string literal "Введите букву: " should be translated]**
      - **בדיקת האות שהוזנה:**
        - `if user_letter in target_word:`: אם האות קיימת במילה שהוגרלה, אז מוסיפים אותה לרשימת האותיות שנוחשו, מעדכנים את המילה ואת המונה.
        - `else:`: אם האות אינה קיימת במילה, אז מוצגת הודעת שגיאה. **[System note: The string literal "Такой буквы нет в слове." should be translated]**
        - אם מספר האותיות שנוחשו שווה למספר האותיות במילה, אז מוצגת הודעת ניצחון והלולאה מסתיימת. **[System note: The string literal "YOU GOT IT!" is already in English, keep as is]**

7. **הפעלת המשחק**:
   - `if __name__ == "__main__":`: מפעיל את הפונקציה `play_spaceword_game()` אם הסקריפט הופעל ישירות.
   - `play_spaceword_game()`: קריאה לפונקציה להתחלת המשחק.
"""
```

**Self-Correction during process:**
I noticed that within the explanation section (point 6), some string literals like `"Слово:"`, `"Введите букву: "`, and `"Такой буквы нет в слове."` are referenced and their translation is implicitly expected as part of the explanation. The original instruction states "אין לתרגם מילים או שמות קוד, משתנים, שמות קבצים או פונקציות", but this refers to code identifiers, not string literals that are part of the UI text. String literals that are printed to the user *should* be translated according to rule 1 ("כל טקסט מחוץ לחלקי קוד יש לתרגם לעברית"). The explanation section *is* text outside the code block.

However, looking back at the Python code block itself, these strings *are* within the code. The instruction for comments/docstrings is specifically about *comments* and *docstrings*, not string literals used in `print` or `input`. The core rule "אין לשנות את הקוד עצמו בשום אופן" (rule 2) implies that string literals within `print` and `input` calls should *not* be changed, as they are part of the executed code.

So, the inconsistency is that the explanation section refers to translating these strings, while the core code rule forbids changing them. The strictest interpretation of the rules prioritizes rule 2: "אין לשנות את הקוד עצמו בשום אופן". Therefore, the string literals within the `print` and `input` functions in the Python code block must remain in Russian. The explanation section referring to them should perhaps acknowledge this or just describe what the code does without explicitly translating the string literals *in the code block*. The explanation text itself *should* be in Hebrew.

Let's re-read instruction 6. "יש לשמר את המבנה המקורי של המסמך... ותיחום של קטעי קוד." and instruction 2 "אין לשנות את הקוד עצמו בשום אופן". These are clear. Instruction 1 "כל טקסט מחוץ לחלקי קוד יש לתרגם לעברית" applies to descriptions, rules, algorithms, legends, and explanations.

So, I will translate *all* text outside the code blocks. I will *not* translate anything inside the code blocks, including string literals. The explanation section will describe the code logic in Hebrew, but when referring to printed output or input prompts, it should refer to the *concept* (e.g., "it prints the current word") rather than translating the specific Russian string literal from the code block.

Let me refine the translation of the explanation section accordingly. I need to ensure the Hebrew explanation accurately reflects the Russian string literals that remain in the code.

Example:
Original: `print("\nСлово:", guessed_word)`
Explanation says: `- print("\nСлово:", guessed_word)`: Выводит текущее состояние слова.
Correct Hebrew explanation: `- print("\nСлово:", guessed_word)`: מציג את מצב המילה הנוכחי. (Keep the code line as is, translate the explanation *about* the line).

Yes, this approach aligns with all instructions. I have already translated the explanation section based on this understanding. The only potential issue was mentioning the Russian strings in the Hebrew explanation, but I can rephrase slightly to refer to the *action* (printing the word status) rather than quoting/translating the specific Russian string in the code.

Looking back at the generated translation, I did translate the explanation text itself into Hebrew, and kept the code snippets and identifiers within the explanation block as they were. The translation seems consistent with this interpretation.

Final check:
- Non-code text: Translated to academic Hebrew. OK.
- Code: Left untouched. OK.
- In-code comments/docstrings: Translated Russian ones to Hebrew. OK.
- Identifiers/Keywords: Not translated. OK.
- Structure: Preserved. OK.
- Consistency: Technical terms (like "угаданных букв" -> "אותיות שנוחשו נכונה") are consistently translated. OK.

The translation seems correct according to the instructions.
SPACWRD:
=================
רמת מורכבות: 4
-----------------
המשחק "מילת החלל" הוא משחק מבוסס טקסט שבו השחקן מנסה לנחש מילה שהמחשב הגריל, באמצעות הזנת אותיות. המחשב מציג את המילה עם רווחים במקום האותיות שלא נוחשו. לאחר כל ניסיון, השחקן מקבל מידע על מספר האותיות שהוא ניחש נכונה, ויכול להמשיך ולנחש את האותיות הנותרות. המשחק מסתיים כאשר השחקן מנחש את כל אותיות המילה.

חוקי המשחק:
1. המחשב בוחר מילה אקראית מרשימת מילים נתונה.
2. השחקן רואה את המילה כשכל האותיות בה מוחלפות ברווחים.
3. השחקן מזין אות.
4. המחשב בודק אם האות קיימת במילה שהוגרלה.
5. אם האות קיימת, המחשב חושף את כל מיקומיה במילה.
6. אם האות אינה קיימת, לא מוצגת הודעה על כך.
7. המשחק ממשיך עד שכל אותיות המילה נוחשו.
8. לאחר כל ניסיון, מוצג מצב המילה הנוכחי עם האותיות הגלויות ומספר האותיות שנוחשו.
-----------------
אלגוריתם:
1. הגדר רשימת מילים למשחק.
2. בחר מילה אקראית מהרשימה.
3. אתחל משתנים:
   - מילה עם רווחים (המילה החסויה)
   - מספר האותיות שנוחשו נכונה
   - מערך של האותיות שנוחשו.
4. התחל לולאה "כל עוד המילה לא נוחשה":
   4.1 הצג את מצב המילה הנוכחי (עם האותיות הגלויות)
   4.2 בקש מהשחקן להזין אות.
   4.3 בדוק נוכחות האות במילה שהוגרלה.
   4.4 אם האות קיימת:
       4.4.1 עדכן את המילה החסויה: חשוף את כל מיקומי האות הזו
       4.4.2 עדכן את מערך האותיות שנוחשו.
       4.4.3 עדכן את מונה האותיות שנוחשו
   4.5 אם כל אותיות המילה נחשפו, עבור לשלב 5.
5. הצג הודעה "YOU GOT IT!".
6. סוף המשחק.
-----------------
תרשים זרימה:
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
        - `wordList` - רשימת מילים למשחק.
        - `targetWord` - המילה שנבחרה באקראי מהרשימה.
        - `guessedWord` - המילה שהשחקן רואה עם רווחים במקום אותיות.
        - `guessedLetters` - רשימת האותיות שנוחשו.
        - `correctGuesses` - מספר האותיות שנוחשו נכונה.
   * **LoopStart** - תחילת לולאת המשחק, הנמשכת כל עוד המילה לא נוחשה.
   * **OutputWord** - הצגת מצב המילה הנוכחי, עם אותיות גלויות (אם נוחשו).
   * **InputLetter** - בקשת קלט אות מהמשתמש.
   * **CheckLetter** - בדיקה אם האות שהוזנה קיימת במילה שהוגרלה.
   * **UpdateWord** - עדכון המילה: חשיפת כל מיקומי האות שהוזנה והוספת האות לרשימת האותיות שנוחשו וספירת האותיות שנוחשו.
   * **CheckWin** - בדיקה אם כל אותיות המילה נוחשו.
   * **OutputWin** - הצגת הודעת ניצחון.
   * **End** - סוף המשחק.
"""


import random

def choose_word(word_list):
    """בוחר מילה אקראית מתוך רשימה."""
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
    """לוגיקה ראשית של המשחק "מילת החלל"."""
    word_list = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "KIWI", "LEMON", "MANGO",
    "ORANGE", "PEACH", "QUINCE", "RASPBERRY", "STRAWBERRY", "TANGERINE", "WATERMELON"
    ]
    target_word = choose_word(word_list) # בוחרים מילה
    guessed_word = "_ " * len(target_word) # יוצרים מילה חסויה
    guessed_letters = []  # רשימת אותיות שנוחשו
    correct_guesses_count = 0
    
    print("Добро пожаловать в игру 'Космическое слово'!")
    print("Я загадал слово. Попробуй его угадать, вводя по одной букве.")
    

    while correct_guesses_count < len(target_word):
        print("\nСлово:", guessed_word)
        user_letter = input("Введите букву: ").upper() # מבקשים אות
        
        if user_letter in target_word:
            guessed_letters.append(user_letter)
            guessed_word = update_word(target_word, guessed_word, user_letter)
            correct_guesses_count = correct_guesses(guessed_letters, target_word)
        else:
            print("Такой буквы нет в слове.")

        
        if correct_guesses_count == len(target_word):
           print("\nYOU GOT IT!")
           break

if __name__ == "__main__":
    play_spaceword_game()
"""
הסבר הקוד:
1. **ייבוא המודול `random`**:
   - `import random`: מייבא את המודול `random` לבחירת מילה אקראית.

2. **הפונקציה `choose_word(word_list)`**:
   - מקבלת רשימת מילים `word_list` כארגומנט.
   - `return random.choice(word_list)`: מחזירה מילה אקראית מהרשימה.

3. **הפונקציה `display_word(word, guessed_letters)`**:
   - מקבלת מילה `word` ורשימה של אותיות שנוחשו `guessed_letters`.
   - יוצרת מחרוזת `display`, שבה מוצגות אותיות מתוך `word` אם הן קיימות ב-`guessed_letters` או התו `_`.
   - מחזירה את המילה להצגה.

4. **הפונקציה `update_word(word, guessed_word, user_letter)`**:
    - מקבלת את המילה שהוגרלה `word`, את התצוגה הנוכחית של המילה `guessed_word`, ואת האות שהוזנה על ידי המשתמש `user_letter`.
    - יוצרת מחרוזת `updated_word`, שבתחילה ריקה.
    - באמצעות לולאת `for` בודקת כל אות במילה `word`.
    - אם האות הנוכחית שווה ל-`user_letter`, אז מוסיפה אותה ל-`updated_word` עם רווח.
    - אחרת, מוסיפה את התו מ-`guessed_word`.
    - מחזירה את המחרוזת המעודכנת עם האותיות הגלויות.

5. **הפונקציה `correct_guesses(guessed_letters, target_word)`**:
    - מקבלת רשימת אותיות שנוחשו `guessed_letters` ואת המילה שהוגרלה `target_word`.
    - יוצרת קבוצה `unique_letters` מתוך אותיות המילה `target_word` למעקב אחר אותיות ייחודיות.
    - באמצעות לולאת `for` סופרת כמה אותיות מתוך `guessed_letters` קיימות במילה.
    - מוציאה את האותיות שכבר נספרו מתוך `unique_letters`.
    - מחזירה את מספר האותיות שנוחשו, שהוא שווה להפרש בין אורך קבוצת האותיות הייחודיות ואורך הקבוצה שנותרה.

6. **הפונקציה `play_spaceword_game()`**:
   - הפונקציה הראשית של המשחק.
   - `word_list`: רשימת מילים למשחק.
   - `target_word = choose_word(word_list)`: בוחרת מילה אקראית.
    - `guessed_word = "_ " * len(target_word)`: יוצרת מחרוזת המייצגת את המילה, שבה כל האותיות הוחלפו ברווחים.
   - `guessed_letters = []`: יוצרת רשימה ריקה לאחסון אותיות שנוחשו.
   - מציגה ברכת כניסה ותיאור המשחק.
   - **לולאת המשחק הראשית `while True`**:
      - `print("\nСлово:", guessed_word)`: מציגה את מצב המילה הנוכחי (המחרוזת המודפסת לקוחה ישירות מהקוד).
      - `user_letter = input("Введите букву: ").upper()`: מבקשת קלט אות וממירה אותה לאות גדולה (המחרוזת המודפסת לקוחה ישירות מהקוד).
      - **בדיקת האות שהוזנה:**
        - `if user_letter in target_word:`: אם האות קיימת במילה שהוגרלה, אז מוסיפים אותה לרשימת האותיות שנוחשו, מעדכנים את המילה ואת המונה.
        - `else:`: אם האות אינה קיימת במילה, אז מוצגת הודעת שגיאה (המחרוזת המודפסת לקוחה ישירות מהקוד).
        - אם מספר האותיות שנוחשו שווה למספר האותיות במילה, אז מוצגת הודעת ניצחון והלולאה מסתיימת.

7. **הפעלת המשחק**:
   - `if __name__ == "__main__":`: מפעיל את הפונקציה `play_spaceword_game()` אם הסקריפט הופעל ישירות.
   - `play_spaceword_game()`: קריאה לפונקציה להתחלת המשחק.
"""