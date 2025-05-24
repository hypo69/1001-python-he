FURS:
=================
רמת קושי: 4
-----------------
המשחק "מכא" הוא משחק מבוסס טקסט שבו המחשב מייצר טקסט אקראי המורכב ממילים וספרות אקראיות. השחקן מנסה לנחש אילו מילים וספרות אקראיות נוצרו. המשחק נמשך עד שהשחקן מנחש את כל המילים והספרות שנוצרו.

כללי המשחק:
1. המחשב בוחר 4 מילים אקראיות מתוך רשימה (במקרה זה, רשימה מוגדרת מראש).
2. המחשב בוחר 4 ספרות אקראיות מתוך הטווח שבין 0 ל-9.
3. על השחקן להזין את המילים והספרות שלדעתו נבחרו על ידי המחשב.
4. אם השחקן מנחש מילה אחת או יותר, או ספרה אחת או יותר, המחשב מציין באיזה מיקום/עמדה הוא ניחש נכון.
5. המשחק נמשך עד שהשחקן מנחש את כל המילים והספרות.
-----------------
אלגוריתם:
1. אתחול רשימת המילים ורשימות ריקות לאחסון המילים והספרות שנבחרו.
2. בחירה אקראית של 4 מילים מתוך הרשימה.
3. בחירה אקראית של 4 ספרות מתוך הטווח שבין 0 ל-9.
4. תחילת לולאה "עד שניחוש הכל".
  4.1 בקשת קלט מהשחקן, בצורה של 4 מילים ו-4 ספרות מופרדות ברווח.
  4.2 המרת המחרוזת שהוזנה לרשימת מילים ולרשימת ספרות.
  4.3 מעבר באיטרציה על רשימת המילים ורשימת הספרות שהוזנו, והשוואתן למילים ולספרות שנבחרו, תוך הדפסת הודעה במקרה של ניחוש נכון.
5. הדפסת ההודעה "YOU GOT IT!"
6. סיום המשחק.
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
    InitializeGame --> ChooseWordsDigits["<p align='left'>בחירה אקראית של 4 מילים ו-4 ספרות:
    <code><b>
    chosenWords = random.sample(words, 4)
    chosenDigits = [random.randint(0, 9) for _ in range(4)]
    </b></code></p>"]
    ChooseWordsDigits --> GameLoopStart{"תחילת לולאה: עד שניחוש הכל"}
    GameLoopStart -- כן --> InputUserGuess["קלט מהמשתמש: 4 מילים ו-4 ספרות"]
    InputUserGuess --> ParseInput["ניתוח קלט המשתמש: מילים וספרות"]
    ParseInput --> CheckGuess{"<p align='left'>בדיקת התאמה:
    <code><b>
    for each word in userWords, digit in userDigits:
        if word == chosenWord:
            print('מילה נוחשה נכונה...')
        if digit == chosenDigit:
            print('ספרה נוחשה נכונה...')
    </b></code></p>"}
    CheckGuess --> CheckWin{"<p align='left'>בדיקת ניצחון:
     <code><b>
    all words and digits correct?
    </b></code></p>"}
    CheckWin -- כן --> OutputWin["פלט: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סיום"]
    CheckWin -- לא --> GameLoopStart
    GameLoopStart -- לא --> End
```

מקרא:
    Start - תחילת התוכנית.
    InitializeGame - אתחול המשתנים: הרשימה words (רשימת מילים אפשריות), chosenWords (רשימת מילים שנבחרו) ו-chosenDigits (רשימת ספרות שנבחרו).
    ChooseWordsDigits - בחירה אקראית של 4 מילים מתוך הרשימה words ו-4 ספרות אקראיות.
    GameLoopStart - תחילת הלולאה, הנמשכת עד שכל המילים והספרות מנוחשות.
    InputUserGuess - בקשת קלט מהמשתמש עבור 4 מילים ו-4 ספרות.
    ParseInput - ניתוח המחרוזת שהוזנה על ידי המשתמש לרשימת מילים ורשימת ספרות.
    CheckGuess - בדיקת ההתאמה בין המילים והספרות שהוזנו על ידי המשתמש לבין המילים והספרות שנבחרו. הדפסת רמזים במקרה של התאמה.
    CheckWin - בדיקה האם כל המילים והספרות נוחשו.
    OutputWin - הדפסת הודעת ניצחון.
    End - סיום התוכנית.

```python
import random

# רשימת מילים אפשריות
words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# רשימה ריקה לאחסון המילים שנבחרו
chosenWords = []
# רשימה ריקה לאחסון הספרות שנבחרו
chosenDigits = []

# בוחרים אקראית 4 מילים מהרשימה
chosenWords = random.sample(words, 4)
# בוחרים אקראית 4 ספרות מ-0 עד 9
chosenDigits = [random.randint(0, 9) for _ in range(4)]

# לולאת המשחק הראשית
while True:
    # מבקשים קלט מהמשתמש
    user_input = input("הזן 4 מילים (A-J) ו-4 ספרות (0-9) מופרדות ברווח: ").upper()
    # מפצלים את הקלט לרשימת מילים ורשימת ספרות
    userWords = user_input.split()[:4]  # לוקחים את 4 האלמנטים הראשונים כמילים
    userDigits = user_input.split()[4:]  # לוקחים את 4 האלמנטים הבאים כספרות

    # דגל למעקב אם המשתמש ניחש הכל
    all_correct = True
    
    # בודקים התאמה עבור המילים
    for i in range(4):
      if userWords[i] == chosenWords[i]:
        print(f"המילה {userWords[i]} במיקום {i+1} נוחשה נכון")
      else:
        all_correct = False
    # בודקים התאמה עבור הספרות
    for i in range(4):
      try:
        if int(userDigits[i]) == chosenDigits[i]:
            print(f"הספרה {userDigits[i]} במיקום {i+1} נוחשה נכון")
        else:
          all_correct = False
      except ValueError:
         print(f"שגיאה: '{userDigits[i]}' אינה ספרה. נסה שוב.")
         all_correct = False
         break
      
    # אם כל המילים והספרות נוחשו, מסיימים את המשחק
    if all_correct:
        print("YOU GOT IT!")
        break
```

"""
הסבר קוד:
1.  **ייבוא המודול `random`**:
    - `import random`: מייבא את המודול לעבודה עם מספרים אקראיים ודגימות.

2.  **אתחול משתנים**:
    - `words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']`: רשימת המילים האפשריות לבחירה.
    - `chosenWords = []`: רשימה ריקה לאחסון המילים שנבחרו.
    - `chosenDigits = []`: רשימה ריקה לאחסון הספרות שנבחרו.
3.  **בחירה אקראית של מילים וספרות**:
    - `chosenWords = random.sample(words, 4)`: בוחר 4 מילים אקראיות מתוך הרשימה `words` ללא חזרות.
    - `chosenDigits = [random.randint(0, 9) for _ in range(4)]`: מייצר רשימה של 4 ספרות אקראיות בטווח שבין 0 ל-9.
4.  **לולאת המשחק הראשית `while True:`**:
    - לולאה אינסופית שנמשכת עד שהשחקן מנחש את כל המילים והספרות (התנאי `all_correct` הופך להיות `True`).
    - `user_input = input("הזן 4 מילים (A-J) ו-4 ספרות (0-9) מופרדות ברווח: ").upper()`: מבקש קלט מהמשתמש, וממיר אותו לאותיות גדולות.
    - `userWords = user_input.split()[:4]`: מפצל את הקלט למילים (לוקח את 4 האלמנטים הראשונים).
    - `userDigits = user_input.split()[4:]`: מפצל את הקלט לספרות (לוקח את 4 האלמנטים הבאים).
5.  **בדיקת התאמה**:
    -  `all_correct = True`: מגדירים את הדגל `all_correct` ל-`True` לפני הבדיקה.
    -  **לולאת בדיקת מילים**:
        -  `for i in range(4):` לולאה על 4 מיקומי המילים.
        -  `if userWords[i] == chosenWords[i]:` בדיקת התאמה של המילה במיקום.
        - `print(f"המילה {userWords[i]} במיקום {i+1} נוחשה נכון")`: מדפיס הודעה אם המילה נוחשה נכון.
        - `else: all_correct = False`: אם מילה אחת לפחות לא נוחשה, הדגל `all_correct` מוגדר ל-`False`.
    -  **לולאת בדיקת ספרות**:
        - `for i in range(4):` לולאה על 4 מיקומי הספרות.
        - `try...except ValueError`: טיפול בשגיאות קלט, אם המשתמש הזין תו שאינו ספרה.
        - `if int(userDigits[i]) == chosenDigits[i]:` בדיקת התאמה של הספרה במיקום.
        -  `print(f"הספרה {userDigits[i]} במיקום {i+1} נוחשה נכון")`: מדפיס הודעה אם הספרה נוחשה נכון.
        - `else: all_correct = False`: אם ספרה אחת לפחות לא נוחשה, הדגל `all_correct` מוגדר ל-`False`.
        - `if not all_correct: break`: אם אירעה שגיאה בקלט, מפסיקים את לולאת בדיקת הספרות.
6.  **בדיקת ניצחון וסיום המשחק**:
    - `if all_correct:`: אם הדגל `all_correct` נשאר `True`, פירושו שכל הניחושים נכונים.
    -  `print("YOU GOT IT!")`: מדפיס הודעת ניצחון.
    - `break`: מסיים את הלולאה הראשית ואת המשחק.
"""