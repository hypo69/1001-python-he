CHEMST:
=================
רמת קושי: 7
-----------------
המשחק "CHEMST" (כימאי) - זהו משחק שבו השחקן מנסה לנחש יסודות כימיים על בסיס רמזים. המחשב בוחר יסוד אקראי מרשימה נתונה, והשחקן מבצע ניסיונות לנחש אותו. המשחק אינו סימולטור ריאליסטי של כימיה, אלא משחק ניחוש מילים עם כמות מוגבלת של ניסיונות. לאחר כל ניסיון, השחקן מקבל מידע האם בניחוש שלו קיימות אותיות מהיסוד שנבחר, ובאילו עמדות.

כללי המשחק:
1.  המחשב בוחר יסוד כימי אקראי מתוך הרשימה.
2.  השחקן מנסה לנחש את היסוד באמצעות הזנת שמו.
3.  לאחר כל ניסיון, המחשב מציג כמה אותיות מההשערה של השחקן תואמות לאותיות היסוד שנבחר, ובאילו עמדות הן נמצאות.
4.  לשחקן יש מקסימום 8 ניסיונות.
5.  המשחק מסתיים כאשר השחקן מנחש את היסוד או מסיים את כל הניסיונות.
-----------------
אלגוריתם:
1.  הגדרת רשימת יסודות כימיים.
2.  בחירת יסוד אקראי מהרשימה.
3.  קביעת מספר הניסיונות ל-0.
4.  התחלת לולאה "כל עוד מספר הניסיונות קטן מ-8":
    4.1 בקשת קלט מהשחקן עבור שם היסוד.
    4.2 הגדלת מספר הניסיונות ב-1.
    4.3 אם שם היסוד שהוזן שווה לשם היסוד שנבחר, הצגת הודעת ניצחון ויציאה מהלולאה.
    4.4 אחרת, יצירת מחרוזת רמז.
    4.5 השוואת כל אות מהשערת השחקן לאות המתאימה ביסוד שנבחר.
        - אם האותיות תואמות ונמצאות באותה עמדה, הצבת האות באותה עמדה במחרוזת הרמז.
        - אם האותיות תואמות אך אינן נמצאות באותה עמדה, הצבת הסימן `+` באותה עמדה במחרוזת הרמז.
        - אם האותיות אינן תואמות, הצבת הסימן `-` באותה עמדה במחרוזת הרמז.
    4.6 הצגת מחרוזת הרמז.
5. אם הלולאה הסתיימה אך היסוד לא נוחש, הצגת הודעת הפסד והתשובה הנכונה.
6. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало" תרגום: "התחלה"] --> InitializeVariables["<p align='left'>Инициализация переменных:" תרגום: "אתחול משתנים:
    <code><b>
    elements = ['HYDROGEN', 'HELIUM', ... ]
    targetElement = random(elements)
    numberOfGuesses = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: " תרגום: "התחלת לולאה: <code><b>numberOfGuesses < 8</b></code>"}
    LoopStart -- Да תרגום: כן --> InputGuess["Ввод элемента пользователем: " תרגום: "קלט יסוד על ידי משתמש: <code><b>userGuess</b></code>"]
    InputGuess --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> CheckGuess{"Проверка: " תרגום: "בדיקה: <code><b>userGuess == targetElement?</b></code>"}
    CheckGuess -- Да תרגום: כן --> OutputWin["Вывод сообщения: " תרגום: "הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["Конец" תרגום: "סוף"]
    CheckGuess -- Нет תרגום: לא --> CreateHint["Создать строку подсказки" תרגום: "יצירת מחרוזת רמז"]
    CreateHint --> CompareLetters["Сравнить буквы: " תרגום: "השוואת אותיות:
     <code><b>
       for i in range(len(targetElement)):
         if userGuess[i] == targetElement[i]: hint += userGuess[i]
         elif userGuess[i] in targetElement: hint += '+'
         else: hint += '-'
       </b></code>
     "]
    CompareLetters --> OutputHint["Вывести строку подсказки " תרגום: "הצגת מחרוזת רמז <code><b>hint</b></code>"]
    OutputHint --> LoopStart
    LoopStart -- Нет תרגום: לא --> OutputLose["Вывод сообщения: " תרגום: "הצגת הודעה: <b>YOU LOSE! The element was <code>{targetElement}</code></b>"]
    OutputLose --> End
```

Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: רשימת היסודות elements, בחירת יסוד אקראי targetElement, וקביעת מספר הניסיונות numberOfGuesses ל-0.
    LoopStart - תחילת הלולאה, אשר נמשכת כל עוד מספר הניסיונות numberOfGuesses קטן מ-8.
    InputGuess - בקשה מהמשתמש להזין את שם היסוד ושמירתו במשתנה userGuess.
    IncreaseGuesses - הגדלת מונה מספר הניסיונות numberOfGuesses ב-1.
    CheckGuess - בדיקה האם שם היסוד שהוזן userGuess שווה ליסוד שנבחר targetElement.
    OutputWin - הצגת הודעת ניצחון, אם שמות היסודות שווים, עם ציון מספר הניסיונות.
    End - סוף התוכנית.
    CreateHint - יצירת מחרוזת רמז למשתמש.
    CompareLetters - השוואת האותיות ביסוד שהוזן לאותיות ביסוד שנבחר ויצירת מחרוזת הרמז.
    OutputHint - הצגת מחרוזת הרמז.
    OutputLose - הצגת הודעת הפסד, אם מספר הניסיונות מוצה, והצגת התשובה הנכונה.
```
import random

# רשימת יסודות כימיים
elements = ['HYDROGEN', 'HELIUM', 'LITHIUM', 'BERYLLIUM', 'BORON', 'CARBON', 'NITROGEN', 'OXYGEN', 'FLUORINE', 'NEON', 'SODIUM', 'MAGNESIUM', 'ALUMINUM', 'SILICON', 'PHOSPHORUS', 'SULFUR', 'CHLORINE', 'ARGON', 'POTASSIUM', 'CALCIUM']
# בוחרים יסוד אקראי מהרשימה
targetElement = random.choice(elements)
# מאתחלים את מספר הניסיונות
numberOfGuesses = 0

# לולאת המשחק הראשית
while numberOfGuesses < 8:
    # מבקשים קלט יסוד מהמשתמש
    userGuess = input("Введите название элемента: ").upper()
    # מגדילים את מספר הניסיונות
    numberOfGuesses += 1

    # בודקים אם היסוד נוחש
    if userGuess == targetElement:
        print(f"ПОЗДРАВЛЯЮ! Вы угадали элемент за {numberOfGuesses} попыток!")
        break # מסיימים את הלולאה אם היסוד נוחש
    else:
        # יוצרים מחרוזת רמז
        hint = ""
        # משווים כל אות מההשערה לאותיות היסוד שנבחר
        for i in range(len(targetElement)):
            if i < len(userGuess):
              if userGuess[i] == targetElement[i]:
                  hint += userGuess[i]  # אם האותיות תואמות ונמצאות באותה עמדה, מוסיפים את האות
              elif userGuess[i] in targetElement:
                  hint += "+"   # אם האותיות תואמות, אך לא באותה עמדה, מוסיפים +
              else:
                  hint += "-"  # אם האותיות אינן תואמות, מוסיפים -
            else:
                hint += "-" # אם האינדקס חורג מאורך המילה שהוזנה, שמים "-"
        # מציגים את מחרוזת הרמז
        print(hint)

# אם הניסיונות נגמרו, והיסוד לא נוחש
if numberOfGuesses == 8:
    print(f"ВЫ ПРОИГРАЛИ! Загаданный элемент был {targetElement}")

"""
הסבר קוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש לבחירת יסוד אקראי מהרשימה.

2.  **רשימת יסודות כימיים `elements`**:
    -   `elements = [...]`: יוצר רשימה של יסודות כימיים.

3.  **בחירת יסוד אקראי**:
    -   `targetElement = random.choice(elements)`: בוחר יסוד אקראי מהרשימה `elements` ושומר אותו במשתנה `targetElement`.

4.  **אתחול מספר הניסיונות**:
    -   `numberOfGuesses = 0`: קובע את מספר הניסיונות ההתחלתי ל-0.

5.  **לולאת המשחק הראשית `while numberOfGuesses < 8:`**:
    -   הלולאה מתבצעת כל עוד מספר הניסיונות `numberOfGuesses` קטן מ-8.

6.  **קלט השערת השחקן**:
    -   `userGuess = input("Введите название элемента: ").upper()`: מבקש מהמשתמש להזין שם יסוד, ממיר את הקלט לאותיות גדולות ושומר במשתנה `userGuess`.

7.  **הגדלת מספר הניסיונות**:
    -   `numberOfGuesses += 1`: מגדיל את מונה מספר הניסיונות ב-1.

8.  **בדיקת ניצחון**:
    -   `if userGuess == targetElement:`: בודק האם היסוד שהוזן על ידי המשתמש תואם ליסוד שנבחר.
    -   `print(f"ПОЗДРАВЛЯЮ! Вы угадали элемент за {numberOfGuesses} попыток!")`: מציג הודעת ניצחון עם מספר הניסיונות.
    -   `break`: מסיים את הלולאה אם היסוד נוחש.

9. **יצירת מחרוזת רמז**:
    -   `else:`: אם היסוד לא נוחש, מתבצע בלוק ה- else.
    -   `hint = ""`: מאתחל מחרוזת ריקה לרמז.
    -   `for i in range(len(targetElement)):`: לולאה למעבר על כל האותיות ביסוד שנבחר.
        -  `if i < len(userGuess):`: בודק שהאינדקס אינו חורג מאורך המילה שהוזנה על ידי המשתמש.
        -   `if userGuess[i] == targetElement[i]:`: אם האותיות תואמות ובאותה עמדה, מוסיפים את האות למחרוזת hint.
        -    `elif userGuess[i] in targetElement:`: אם האות מההשערה קיימת ביסוד שנבחר אך לא באותה עמדה, מוסיפים "+".
        -    `else:`: אם האותיות אינן תואמות, מוסיפים "-".
        -  `else:`: אם האינדקס חורג מגודל המילה שהוזנה, שמים "-".
    -    `print(hint)`: מציג את מחרוזת הרמז.

10. **בדיקת הפסד**:
    -   `if numberOfGuesses == 8:`: לאחר סיום הלולאה, נבדק האם הניסיונות הסתיימו.
    -   `print(f"ВЫ ПРОИГРАЛИ! Загаданный элемент был {targetElement}")`: מציג הודעת הפסד ומראה את התשובה הנכונה.
"""