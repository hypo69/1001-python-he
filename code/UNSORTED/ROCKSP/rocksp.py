<ROCKSP>:
=================
דרגת קושי: 2
-----------------
המשחק "אבן, נייר, מספריים" הוא משחק קלאסי לשני שחקנים, שבו כל שחקן בוחר אחת משלוש אפשרויות: אבן, מספריים או נייר. המנצח נקבע לפי הכללים הבאים: אבן מנצחת מספריים, מספריים מנצחים נייר, ונייר מנצח אבן. אם שני השחקנים בוחרים באותה אפשרות, מוכרז תיקו.
כללי המשחק:
1.  השחקן והמחשב בוחרים אחת משלוש אפשרויות: 1 - אבן, 2 - מספריים, 3 - נייר.
2.  המחשב בוחר באופן אקראי.
3.  המנצח נקבע לפי הכללים הבאים:
    *   אבן (1) מנצחת מספריים (2).
    *   מספריים (2) מנצחים נייר (3).
    *   נייר (3) מנצח אבן (1).
4.  אם שני הצדדים בוחרים באותה אפשרות, זהו תיקו.
5.  תוצאת כל סיבוב מוצגת על המסך.
6.  המשחק מסתיים לאחר כל סיבוב.
-----------------
אלגוריתם:
1.  בקש מהשחקן לבחור: 1 - אבן, 2 - מספריים, 3 - נייר.
2.  אם קלט השחקן אינו 1, 2 או 3, הצג הודעת שגיאת קלט וחזור לשלב 1.
3.  הגרל בחירה אקראית עבור המחשב: 1, 2 או 3.
4.  הצג על המסך את בחירת השחקן והמחשב.
5.  השווה את בחירת השחקן והמחשב:
    5.1 אם שתי הבחירות זהות, הצג "TIE".
    5.2 אם השחקן בוחר 1 (אבן) והמחשב 2 (מספריים), הצג "YOU WIN".
    5.3 אם השחקן בוחר 1 (אבן) והמחשב 3 (נייר), הצג "I WIN".
    5.4 אם השחקן בוחר 2 (מספריים) והמחשב 1 (אבן), הצג "I WIN".
    5.5 אם השחקן בוחר 2 (מספריים) והמחשב 3 (נייר), הצג "YOU WIN".
    5.6 אם השחקן בוחר 3 (נייר) והמחשב 1 (אבן), הצג "YOU WIN".
    5.7 אם השחקן בוחר 3 (נייר) והמחשב 2 (מספריים), הצג "I WIN".
6.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InputUserChoice["<p align='left'>בקשת בחירת משתמש:<br>
    <code><b>
    userChoice = input('1-ROCK, 2-SCISSORS, 3-PAPER?')
    </b></code></p>"]
    InputUserChoice --> ValidateInput{"בדיקה: <code><b>userChoice in [1, 2, 3]?</b></code>"}
    ValidateInput -- לא --> ErrorMessage["הצגת הודעה: <b>INVALID INPUT</b>"]
    ErrorMessage --> InputUserChoice
    ValidateInput -- כן --> GenerateComputerChoice["<p align='left'>הגרלת בחירה אקראית עבור המחשב:<br>
    <code><b>
    computerChoice = random(1, 3)
    </b></code></p>"]
    GenerateComputerChoice --> OutputChoices["<p align='left'>הצגת בחירת המשתמש והמחשב</p>"]
    OutputChoices --> CompareChoices{"השוואת בחירת המשתמש והמחשב"}
    CompareChoices -- "userChoice == computerChoice" --> OutputTie["הצגת הודעה: <b>TIE</b>"]
    CompareChoices -- "userChoice == 1 AND computerChoice == 2" --> OutputUserWin1["הצגת הודעה: <b>YOU WIN</b>"]
    CompareChoices -- "userChoice == 1 AND computerChoice == 3" --> OutputComputerWin1["הצגת הודעה: <b>I WIN</b>"]
    CompareChoices -- "userChoice == 2 AND computerChoice == 1" --> OutputComputerWin2["הצגת הודעה: <b>I WIN</b>"]
    CompareChoices -- "userChoice == 2 AND computerChoice == 3" --> OutputUserWin2["הצגת הודעה: <b>YOU WIN</b>"]
    CompareChoices -- "userChoice == 3 AND computerChoice == 1" --> OutputUserWin3["הצגת הודעה: <b>YOU WIN</b>"]
    CompareChoices -- "userChoice == 3 AND computerChoice == 2" --> OutputComputerWin3["הצגת הודעה: <b>I WIN</b>"]
    OutputTie --> End["סוף"]
    OutputUserWin1 --> End
    OutputComputerWin1 --> End
    OutputComputerWin2 --> End
    OutputUserWin2 --> End
    OutputUserWin3 --> End
    OutputComputerWin3 --> End
```

מקרא:
    Start - התחלת המשחק.
    InputUserChoice - בקשת קלט מהמשתמש: 1 - אבן, 2 - מספריים, 3 - נייר.
    ValidateInput - בדיקת תקינות קלט המשתמש: חייב להיות 1, 2 או 3.
    ErrorMessage - הצגת הודעה על שגיאת קלט.
    GenerateComputerChoice - הגרלת בחירה אקראית עבור המחשב: 1, 2 או 3.
    OutputChoices - הצגה על המסך של בחירת המשתמש והמחשב.
    CompareChoices - השוואת בחירת המשתמש והמחשב לקביעת המנצח.
    OutputTie - הצגת הודעה על תיקו (TIE).
    OutputUserWin1 - הצגת הודעה על ניצחון המשתמש (YOU WIN) (המשתמש בחר אבן, המחשב - מספריים).
    OutputComputerWin1 - הצגת הודעה על ניצחון המחשב (I WIN) (המשתמש בחר אבן, המחשב - נייר).
    OutputComputerWin2 - הצגת הודעה על ניצחון המחשב (I WIN) (המשתמש בחר מספריים, המחשב - אבן).
    OutputUserWin2 - הצגת הודעה על ניצחון המשתמש (YOU WIN) (המשתמש בחר מספריים, המחשב - נייר).
    OutputUserWin3 - הצגת הודעה על ניצחון המשתמש (YOU WIN) (המשתמש בחר נייר, המחשב - אבן).
    OutputComputerWin3 - הצגת הודעה על ניצחון המחשב (I WIN) (המשתמש בחר נייר, המחשב - מספריים).
    End - סוף המשחק.
"""
import random

# פונקציה להפעלת המשחק
def play_rock_paper_scissors():
    while True:
        # מבקשים את בחירת המשתמש
        try:
            user_choice = int(input("Введите ваш выбор (1 - Камень, 2 - Ножницы, 3 - Бумага): "))
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число 1, 2 или 3.")
            continue

        # בודקים את תקינות הקלט
        if user_choice not in [1, 2, 3]:
            print("Неверный ввод. Пожалуйста, введите число 1, 2 или 3.")
            continue

        # מגרלים בחירה אקראית עבור המחשב
        computer_choice = random.randint(1, 3)

        # מציגים את בחירת השחקן והמחשב
        print("Ваш выбор:", user_choice)
        print("Выбор компьютера:", computer_choice)

        # קובעים את המנצח
        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == 1 and computer_choice == 2) or \
             (user_choice == 2 and computer_choice == 3) or \
             (user_choice == 3 and computer_choice == 1):
            print("Вы выиграли!")
        else:
            print("Вы проиграли!")
        break

# מפעילים את המשחק
if __name__ == "__main__":
    play_rock_paper_scissors()
"""
הסבר קוד:
1. **ייבוא מודול `random`**:
   - `import random`: מייבא את המודול `random`, המשמש להגרלת בחירה אקראית עבור המחשב.

2. **פונקציה `play_rock_paper_scissors()`**:
   - מגדירה פונקציה המכילה את לוגיקת המשחק "אבן, נייר, מספריים".

3. **לולאת `while True:`**:
   - לולאה אינסופית הנמשכת עד לקלט תקין וקביעת מנצח.

4. **קלט נתונים ובדיקת תקינות**:
    - `try...except ValueError`: מטפל בשגיאות אפשריות אם המשתמש מזין קלט שאינו מספר.
   -   `user_choice = int(input("Введите ваш выбор (1 - Камень, 2 - Ножницы, 3 - Бумага): "))`: מבקש מהמשתמש את בחירתו וממיר אותה למספר שלם.
    -  `if user_choice not in [1, 2, 3]:`: בודק שהמספר שהוזן הוא 1, 2 או 3. אם הקלט אינו תקין, מוצגת הודעת שגיאה, והלולאה מתחילה מחדש.

5. **הגרלת בחירת המחשב**:
   - `computer_choice = random.randint(1, 3)`: מגרל מספר שלם אקראי בין 1 ל-3 כולל ושומר אותו במשתנה `computer_choice`.

6.  **הצגת בחירת המשתמש והמחשב**:
     -  `print("Ваш выбор:", user_choice)`: מציג על המסך את בחירת המשתמש.
     -  `print("Выбор компьютера:", computer_choice)`: מציג על המסך את בחירת המחשב.

7. **קביעת המנצח**:
   -   `if user_choice == computer_choice:`: בודק אם הבחירות זהות. אם כן, מוצגת הודעה על תיקו.
   -  `elif (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 3) or \
         (user_choice == 3 and computer_choice == 1):`: בודק את כל המקרים בהם המשתמש מנצח.
   -    `print("Вы выиграли!")`: מציג הודעה על ניצחון המשתמש.
   -    `else:`: אם אף אחד מהתנאים הקודמים לא התקיים, המחשב ניצח.
        - `print("Вы проиграли!")`: מציג הודעה על הפסד המשתמש.

8. **סיום המשחק**:
   -   `break`: מסיים את סיבוב המשחק הנוכחי.
9. **הפעלת המשחק**:
   -  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_rock_paper_scissors()` תופעל רק אם הקובץ מורץ ישירות ולא מיובא כמודול.
   -  `play_rock_paper_scissors()`: קריאה לפונקציה להפעלת המשחק.