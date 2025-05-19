FURS:
=================
רמת קושי: 4
-----------------
המשחק 'מכא' הוא משחק טקסטואלי שבו המחשב מייצר טקסט אקראי, המורכב ממילים ומספרים אקראיים. השחקן מנסה לנחש אילו מילים ומספרים אקראיים נוצרו. המשחק נמשך עד אשר השחקן ינחש את כל המילים והמספרים שנוצרו.

חוקי המשחק:
1. המחשב בוחר 4 מילים אקראיות מרשימה (במקרה זה, רשימה שהוגדרה מראש).
2. המחשב בוחר 4 ספרות אקראיות מהטווח 0 עד 9.
3. השחקן צריך להזין את המילים והספרות, שלדעתו נבחרו על ידי המחשב.
4. אם השחקן מנחש מילה או ספרה אחת או יותר, המחשב מציג באיזו עמדה הוא ניחש נכון.
5. המשחק נמשך עד אשר השחקן ינחש את כל המילים והספרות.
-----------------
אלגוריתם:
1. לאתחל רשימת מילים ורשימה ריקה לאחסון המילים והספרות שנבחרו.
2. לבחור באופן אקראי 4 מילים מהרשימה.
3. לבחור באופן אקראי 4 ספרות מהטווח 0 עד 9.
4. להתחיל בלולאה "כל עוד לא הכל נוחש".
  4.1 לבקש קלט מהשחקן, בצורה של 4 מילים ו-4 ספרות המופרדות ברווח.
  4.2 להמיר את המחרוזת שהוזנה לרשימת מילים ולרשימת ספרות.
  4.3 לעבור בלולאה על רשימת המילים והספרות, ולהשוות עם המילים והספרות שנבחרו, ולהציג הודעה אם נוחש נכון.
5. להציג את ההודעה "YOU GOT IT!".
6. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["<p align='left'>אתחול:
    <code><b>
    words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    chosenWords = []
    chosenDigits = []
    </b></code></p>"]
    InitializeGame --> ChooseWordsDigits["<p align='left'>בחירת אקראיים 4 מילים ו-4 ספרות:
    <code><b>
    chosenWords = random.sample(words, 4)
    chosenDigits = [random.randint(0, 9) for _ in range(4)]
    </b></code></p>"]
    ChooseWordsDigits --> GameLoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    GameLoopStart -- Да --> InputUserGuess["קלט מהמשתמש: 4 מילים ו-4 ספרות"]
    InputUserGuess --> ParseInput["ניתוח קלט משתמש: מילים וספרות"]
    ParseInput --> CheckGuess{"<p align='left'>בדיקת התאמה:
    <code><b>
    for each word in userWords, digit in userDigits:
        if word == chosenWord:
            print('מילה נוחשה...')
        if digit == chosenDigit:
            print('ספרה נוחשה...')
    </b></code></p>"}
    CheckGuess --> CheckWin{"<p align='left'>בדיקת ניצחון:
     <code><b>
    all words and digits correct?
    </b></code></p>"}
    CheckWin -- Да --> OutputWin["פלט: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- Нет --> GameLoopStart
    GameLoopStart -- Нет --> End
```

מקרא:
    Start - תחילת התוכנית.
    InitializeGame - אתחול משתנים: רשימת words (רשימה של מילים אפשריות), chosenWords (רשימה של מילים שנבחרו) ו- chosenDigits (רשימה של ספרות שנבחרו).
    ChooseWordsDigits - בחירת 4 מילים אקראיות מרשימת words ו-4 ספרות אקראיות.
    GameLoopStart - תחילת לולאה, שנמשכת כל עוד כל המילים והספרות לא נוחשו.
    InputUserGuess - בקשת קלט מהמשתמש עבור 4 מילים ו-4 ספרות.
    ParseInput - ניתוח המחרוזת שהוזנה על ידי המשתמש לרשימת מילים ולרשימת ספרות.
    CheckGuess - בדיקת התאמה בין המילים והספרות שהוזנו על ידי המשתמש לבין אלה שנבחרו. הצגת רמזים במקרה של התאמה.
    CheckWin - בדיקה האם כל המילים והספרות נוחשו.
    OutputWin - הצגת הודעה על הניצחון.
    End - סוף התוכנית.
```
import random

# רשימת מילים אפשריות
words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# רשימה ריקה לאחסון המילים שנבחרו
chosenWords = []
# רשימה ריקה לאחסון הספרות שנבחרו
chosenDigits = []

# בוחרים באופן אקראי 4 מילים מהרשימה
chosenWords = random.sample(words, 4)
# בוחרים באופן אקראי 4 ספרות מהטווח 0 עד 9
chosenDigits = [random.randint(0, 9) for _ in range(4)]

# לולאת המשחק הראשית
while True:
    # מבקשים קלט מהמשתמש
    user_input = input("הזן 4 מילים (A-J) ו-4 ספרות (0-9) מופרדות ברווח: ").upper()
    # מפצלים את הקלט לרשימת מילים ולרשימת ספרות
    userWords = user_input.split()[:4]  # לוקחים את 4 האיברים הראשונים כמילים
    userDigits = user_input.split()[4:]  # לוקחים את 4 האיברים הבאים כספרות

    # דגל למעקב האם המשתמש ניחש הכל
    all_correct = True

    # בודקים התאמה של המילים
    for i in range(4):
      if userWords[i] == chosenWords[i]:
        print(f"המילה {userWords[i]} בעמדה {i+1} נוחשה")
      else:
        all_correct = False
    # בודקים התאמה של הספרות
    for i in range(4):
      try:
        if int(userDigits[i]) == chosenDigits[i]:
            print(f"הספרה {userDigits[i]} בעמדה {i+1} נוחשה")
        else:
          all_correct = False
      except ValueError:
         print(f"שגיאה: '{userDigits[i]}' אינו ספרה. נסה שוב.")
         all_correct = False
         break

    # אם כל המילים והספרות נוחשו, מסיימים את המשחק
    if all_correct:
        print("YOU GOT IT!")
        break


"""
הסבר קוד:
1.  **ייבוא מודול `random`**:
    - `import random`: מייבא את המודול לעבודה עם מספרים אקראיים ודגימות.

2.  **אתחול משתנים**:
    - `words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']`: רשימת מילים אפשריות לבחירה.
    - `chosenWords = []`: רשימה ריקה לאחסון המילים שנבחרו.
    - `chosenDigits = []`: רשימה ריקה לאחסון הספרות שנבחרו.
3.  **בחירת מילים וספרות אקראיות**:
    - `chosenWords = random.sample(words, 4)`: בוחר 4 מילים אקראיות מהרשימה `words` ללא חזרות.
    - `chosenDigits = [random.randint(0, 9) for _ in range(4)]`: מייצר רשימה של 4 ספרות אקראיות בטווח שבין 0 ל-9.
4.  **לולאת המשחק הראשית `while True:`**:
    - לולאה אינסופית שנמשכת כל עוד השחקן לא ניחש את כל המילים והספרות (התנאי `all_correct` יהפוך ל-`True`).
    - `user_input = input("הזן 4 מילים (A-J) ו-4 ספרות (0-9) מופרדות ברווח: ").upper()`: מבקש קלט מהמשתמש, וממיר אותו לאותיות גדולות.
    - `userWords = user_input.split()[:4]`: מפצל את הקלט למילים (נלקחים 4 האיברים הראשונים).
    - `userDigits = user_input.split()[4:]`: מפצל את הקלט לספרות (נלקחים 4 האיברים הבאים).
5.  **בדיקת התאמה**:
    -  `all_correct = True`: מגדירים את הדגל `all_correct` ל-`True` לפני הבדיקה.
    -  **לולאת בדיקת מילים**:
        -  `for i in range(4):` לולאה על 4 עמדות המילים.
        -  `if userWords[i] == chosenWords[i]:` בדיקת התאמה של המילה בעמדה.
        - `print(f"המילה {userWords[i]} בעמדה {i+1} נוחשה")`: מציג הודעה אם המילה נוחשה.
        - `else: all_correct = False`: אם מילה אחת לפחות לא נוחשה, דגל `all_correct` נקבע ל-`False`.
    -  **לולאת בדיקת ספרות**:
        - `for i in range(4):` לולאה על 4 עמדות הספרות.
        - `try...except ValueError`: טיפול בשגיאות קלט, אם המשתמש הזין לא ספרה.
        - `if int(userDigits[i]) == chosenDigits[i]:` בדיקת התאמה של הספרה בעמדה.
        -  `print(f"הספרה {userDigits[i]} בעמדה {i+1} נוחשה")`: הצגת הודעה אם הספרה נוחשה.
        - `else: all_correct = False`: אם ספרה אחת לפחות לא נוחשה, דגל `all_correct` נקבע ל-`False`.
        - `if not all_correct: break`: אם יש שגיאה בקלט, מפסיק את לולאת בדיקת הספרות.
6.  **בדיקת ניצחון וסיום המשחק**:
    - `if all_correct:`: אם הדגל `all_correct` נשאר `True`, זה אומר שהכל נוחש.
    -  `print("YOU GOT IT!")`: מציג הודעה על הניצחון.
    - `break`: מסיים את הלולאה הראשית ואת המשחק.
"""