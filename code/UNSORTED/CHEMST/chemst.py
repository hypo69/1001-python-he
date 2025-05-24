CHEMST:
=================
דרגת קושי: 7
-----------------
המשחק "CHEMST" (כימאי) הוא משחק בו השחקן מנסה לנחש יסודות כימיים בהתבסס על רמזים. המחשב בוחר יסוד אקראי מתוך רשימה נתונה, והשחקן מבצע ניסיונות לנחשו. המשחק אינו מהווה סימולטור כימיה ריאליסטי, אלא משחק ניחוש מילה עם כמות מוגבלת של ניסיונות. לאחר כל ניסיון, השחקן מקבל מידע אילו אותיות מהניחוש שלו מופיעות ביסוד שנבחר, ובאילו עמדות.

כללי המשחק:
1.  המחשב בוחר באופן אקראי יסוד כימי מתוך רשימה.
2.  השחקן מנסה לנחש את היסוד על ידי הזנת שמו.
3.  לאחר כל ניסיון, המחשב מציג כמה אותיות מתוך השערת השחקן תואמות לאותיות היסוד שנבחר, ובאילו עמדות הן נמצאות.
4.  לשחקן יש מקסימום 8 ניסיונות.
5.  המשחק מסתיים כאשר השחקן מנחש את היסוד או כאשר הוא מסיים את כל הניסיונות.
-----------------
אלגוריתם:
1.  הגדר רשימה של יסודות כימיים.
2.  בחר יסוד אקראי מתוך הרשימה.
3.  אפס את מונה הניסיונות.
4.  התחל לולאה "כל עוד מספר הניסיונות קטן מ-8":
    4.1 בקש מהשחקן להזין את שם היסוד.
    4.2 הגדל את מונה הניסיונות ב-1.
    4.3 אם שם היסוד שהוזן שווה ליסוד שנבחר, הצג הודעת ניצחון וצא מהלולאה.
    4.4 אחרת, צור מחרוזת רמז.
    4.5 השווה כל אות מהשערת השחקן לאות המתאימה ביסוד שנבחר.
        - אם האותיות תואמות ונמצאות באותן עמדות, הצב את האות באותה עמדה במחרוזת הרמז.
        - אם האותיות תואמות אך אינן נמצאות באותן עמדות, הצב את הסימן `+` באותה עמדה במחרוזת הרמז.
        - אם האותיות אינן תואמות, הצב את הסימן `-` באותה עמדה במחרוזת הרמז.
    4.6 הצג את מחרוזת הרמז.
5. אם הלולאה הסתיימה אך היסוד לא נוחש, הצג הודעת הפסד ואת התשובה הנכונה.
6. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>איתחול משתנים:
    <code><b>
    elements = ['HYDROGEN', 'HELIUM', ... ]
    targetElement = random(elements)
    numberOfGuesses = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: <code><b>numberOfGuesses < 8</b></code>"}
    LoopStart -- כן --> InputGuess["קלט יסוד מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> CheckGuess{"בדיקה: <code><b>userGuess == targetElement?</b></code>"}
    CheckGuess -- כן --> OutputWin["פלט הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> CreateHint["יצירת מחרוזת רמז"]
    CreateHint --> CompareLetters["השוואת אותיות:
     <code><b>
       for i in range(len(targetElement)):
         if userGuess[i] == targetElement[i]: hint += userGuess[i]
         elif userGuess[i] in targetElement: hint += '+'
         else: hint += '-'
       </b></code>
     "]
    CompareLetters --> OutputHint["הצגת מחרוזת הרמז <code><b>hint</b></code>"]
    OutputHint --> LoopStart
    LoopStart -- לא --> OutputLose["פלט הודעה: <b>YOU LOSE! The element was <code>{targetElement}</code></b>"]
    OutputLose --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - איתחול משתנים: רשימת האלמנטים elements, בחירת אלמנט אקראי targetElement, והגדרת מספר הניסיונות numberOfGuesses ל-0.
    LoopStart - התחלת הלולאה, הנמשכת כל עוד מספר הניסיונות numberOfGuesses קטן מ-8.
    InputGuess - בקשת קלט של שם יסוד מהמשתמש ושמירתו במשתנה userGuess.
    IncreaseGuesses - הגדלת מונה מספר הניסיונות numberOfGuesses ב-1.
    CheckGuess - בדיקה האם שם היסוד שהוזן userGuess שווה לאלמנט שנבחר targetElement.
    OutputWin - הצגת הודעה על ניצחון, אם שמות האלמנטים שווים, עם ציון מספר הניסיונות.
    End - סוף התוכנית.
    CreateHint - יצירת מחרוזת רמז עבור המשתמש.
    CompareLetters - השוואת האותיות באלמנט שהוזן עם האותיות באלמנט שנבחר ויצירת מחרוזת הרמז.
    OutputHint - הצגת מחרוזת הרמז.
    OutputLose - הצגת הודעה על הפסד, אם מספר הניסיונות מוצה, והצגת התשובה הנכונה.
"""
import random

# רשימת יסודות כימיים
elements = ['HYDROGEN', 'HELIUM', 'LITHIUM', 'BERYLLIUM', 'BORON', 'CARBON', 'NITROGEN', 'OXYGEN', 'FLUORINE', 'NEON', 'SODIUM', 'MAGNESIUM', 'ALUMINUM', 'SILICON', 'PHOSPHORUS', 'SULFUR', 'CHLORINE', 'ARGON', 'POTASSIUM', 'CALCIUM']
# בוחרים יסוד אקראי מהרשימה
targetElement = random.choice(elements)
# מאתחלים את מונה הניסיונות
numberOfGuesses = 0

# לולאת המשחק הראשית
while numberOfGuesses < 8:
    # מבקשים קלט יסוד מהמשתמש
    userGuess = input("הזן שם יסוד: ").upper()
    # מגדילים את מונה הניסיונות
    numberOfGuesses += 1

    # בודקים אם היסוד נוחש
    if userGuess == targetElement:
        print(f"ברכות! ניחשת את היסוד ב- {numberOfGuesses} ניסיונות!")
        break # מסיימים את הלולאה אם היסוד נוחש
    else:
        # יוצרים מחרוזת רמז
        hint = ""
        # משווים כל אות בניחוש עם האותיות ביסוד שנבחר
        for i in range(len(targetElement)):
            if i < len(userGuess):
              if userGuess[i] == targetElement[i]:
                  hint += userGuess[i]  # אם האותיות תואמות ובאותן עמדות, מוסיפים את האות
              elif userGuess[i] in targetElement:
                  hint += "+"   # אם האותיות תואמות, אך לא באותן עמדות, מוסיפים +
              else:
                  hint += "-"  # אם האותיות אינן תואמות, מוסיפים -
            else:
                hint += "-" # אם האינדקס חורג מאורך המילה שהוזנה, שמים "-"
        # מציגים את מחרוזת הרמז
        print(hint)

# אם הניסיונות נגמרו, והיסוד לא נוחש
if numberOfGuesses == 8:
    print(f"הפסדת! היסוד שנבחר היה {targetElement}")

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש לבחירת יסוד אקראי מתוך רשימה.

2.  **רשימת יסודות כימיים `elements`**:
    -   `elements = [...]`: יוצר רשימה של יסודות כימיים.

3.  **בחירת יסוד אקראי**:
    -   `targetElement = random.choice(elements)`: בוחר יסוד אקראי מתוך רשימת `elements` ושומר אותו במשתנה `targetElement`.

4.  **איתחול מונה הניסיונות**:
    -   `numberOfGuesses = 0`: מגדיר את מספר הניסיונות ההתחלתי ל-0.

5.  **לולאת המשחק הראשית `while numberOfGuesses < 8:`**:
    -   הלולאה מתבצעת כל עוד מספר הניסיונות `numberOfGuesses` קטן מ-8.

6.  **קלט השערת השחקן**:
    -   `userGuess = input("הזן שם יסוד: ").upper()`: מבקש מהמשתמש להזין שם יסוד, ממיר את הקלט לאותיות גדולות ושומר אותו במשתנה `userGuess`.

7.  **הגדלת מונה הניסיונות**:
    -   `numberOfGuesses += 1`: מגדיל את מונה הניסיונות ב-1.

8.  **בדיקת ניצחון**:
    -   `if userGuess == targetElement:`: בודק האם היסוד שהוזן על ידי המשתמש תואם ליסוד שנבחר.
    -   `print(f"ברכות! ניחשת את היסוד ב- {numberOfGuesses} ניסיונות!")`: מציג הודעת ניצחון עם מספר הניסיונות.
    -   `break`: מסיים את הלולאה אם היסוד נוחש.

9. **יצירת מחרוזת רמז**:
    -   `else:`: אם היסוד לא נוחש, מבוצע בלוק ה-else.
    -   `hint = ""`: מאתחל מחרוזת ריקה עבור הרמז.
    -   `for i in range(len(targetElement)):`: לולאה למעבר על כל האותיות ביסוד שנבחר.
        -  `if i < len(userGuess):`: בודק אם האינדקס אינו חורג מאורך המילה שהוזנה על ידי המשתמש.
        -   `if userGuess[i] == targetElement[i]:`: אם האותיות תואמות ובאותן עמדות, מוסיפים את האות למחרוזת hint.
        -    `elif userGuess[i] in targetElement:`: אם אות מהניחוש קיימת ביסוד שנבחר אך לא באותה עמדה, מוסיפים "+".
        -    `else:`: אם האותיות אינן תואמות, מוסיפים "-".
        -  `else:`: אם האינדקס חורג מאורך המילה שהוזנה, מציבים "-".
    -    `print(hint)`: מציג את מחרוזת הרמז.

10. **בדיקת הפסד**:
    -   `if numberOfGuesses == 8:`: לאחר סיום הלולאה, נבדק האם הניסיונות אזלו.
    -   `print(f"הפסדת! היסוד שנבחר היה {targetElement}")`: מציג הודעת הפסד ומציג את התשובה הנכונה.
"""