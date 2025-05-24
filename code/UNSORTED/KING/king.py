KING:
=================
מורכבות: 6
-----------------
המשחק "מלך" הוא משחק מילים שבו שחקנים אומרים מילים בתורם, כאשר כל מילה מתחילה באות האחרונה של המילה הקודמת.
המשחק נמשך עד שאחד השחקנים נכנע או אינו מצליח למצוא מילה.

כללי המשחק:
1.  שחקן 1 מזין מילה כלשהי.
2.  שחקן 2 חייב להזין מילה המתחילה באות האחרונה של המילה שהזין שחקן 1.
3.  השחקנים מזינים מילים בתורם, תוך שמירה על כלל האות הראשונה.
4.  המשחק מסתיים כאשר שחקן מזין '0' או אם אינו מצליח למצוא מילה מתאימה.
-----------------
אלגוריתם:
1. הצג הנחיה עבור השחקן הראשון.
2. קלוט את המילה הראשונה.
3. קבע את השחקן הנוכחי ל-2.
4. התחל לולאה עד לסיום המשחק:
    4.1. הצג הנחיה עבור השחקן הנוכחי.
    4.2. קלוט מילה חדשה.
    4.3. אם המילה החדשה שווה ל-'0', עבור לשלב 7.
    4.4. אם האות הראשונה של המילה החדשה אינה שווה לאות האחרונה של המילה הקודמת, הצג הודעת שגיאה.
    4.5. אם השחקן הזין מילה נכונה, אז:
         4.5.1. קבע את המילה הקודמת להיות המילה הנוכחית.
         4.5.2. החלף את השחקן הנוכחי.
5. הצג הודעה על סיום המשחק.
6. הצג הודעה על ניצחון השחקן הקודם.
7. סיום המשחק.
-----------------
```mermaid
flowchart TD
    Start["Начало"] --> InputFirstWord["Ввод первого слова от игрока 1"]
    InputFirstWord --> SetCurrentPlayer["<code><b>currentPlayer = 2</b></code>"]
    SetCurrentPlayer --> GameLoopStart{"Начало цикла игры"}
    GameLoopStart -- "Да" --> InputWord["Ввод слова от <code><b>currentPlayer</b></code>"]
    InputWord --> CheckQuit{"Проверка: <code><b>word == '0'?</b></code>"}
    CheckQuit -- Да --> GameOver["Конец игры"]
    CheckQuit -- Нет --> CheckFirstLetter{"Проверка: <code><b>firstLetter(word) == lastLetter(previousWord)?</b></code>"}
    CheckFirstLetter -- Нет --> OutputError["Вывод ошибки: <b>INCORRECT WORD</b>"]
    OutputError --> GameLoopStart
    CheckFirstLetter -- Да --> UpdatePreviousWord["<code><b>previousWord = word</b></code>"]
    UpdatePreviousWord --> SwitchPlayer["<code><b>currentPlayer = 3 - currentPlayer</b></code>"]
     SwitchPlayer --> GameLoopStart
    GameLoopStart -- "Нет" --> OutputEndMessage["Вывод: <b>GAME OVER</b>"]
    OutputEndMessage --> OutputWinner["Вывод победителя: <b>Player {3 - currentPlayer} WINS!</b>"]
    OutputWinner --> End["Конец"]
```
מקרא:
    Start - התחלת התוכנית.
    InputFirstWord - בקשת הזנת המילה הראשונה משחקן 1.
    SetCurrentPlayer - קביעת השחקן הנוכחי ל-2.
    GameLoopStart - התחלת לולאת המשחק הראשית.
    InputWord - בקשת הזנת מילה מהשחקן הנוכחי.
    CheckQuit - בדיקה האם הוזנה המילה '0' לסיום המשחק.
    GameOver - סיום המשחק.
    CheckFirstLetter - בדיקה האם האות הראשונה של המילה שהוזנה תואמת את האות האחרונה של המילה הקודמת.
    OutputError - הצגת הודעת שגיאה אם המילה שגויה.
    UpdatePreviousWord - עדכון המילה הקודמת במילה הנוכחית.
    SwitchPlayer - החלפת השחקן הנוכחי.
    OutputEndMessage - הצגת הודעה על סיום המשחק.
    OutputWinner - הצגת מנצח המשחק.
    End - סוף התוכנית.
"""

# אתחול משתנים ראשוניים
previousWord = ""
currentPlayer = 1

# בקשת המילה הראשונה
previousWord = input("Игрок 1, введите первое слово: ").strip() # מסיר רווחים
currentPlayer = 2 # עוברים לשחקן השני

# מתחילים את המשחק
while True:
    currentWord = input(f"Игрок {currentPlayer}, введите слово: ").strip() # מסיר רווחים

    # בדיקה על יציאה מהמשחק
    if currentWord == '0':
        print("Игра окончена.")
        break

    # בדיקת האות הראשונה
    if previousWord and currentWord[0].lower() != previousWord[-1].lower():
        print("Неверное слово, первая буква должна совпадать с последней буквой предыдущего слова.")
        continue

    # הכנה לתור הבא
    previousWord = currentWord
    currentPlayer = 3 - currentPlayer  # מחליפים שחקן

print(f"Игрок {3 - currentPlayer} победил!")

"""
הסבר על הקוד:
1. **אתחול משתנים**:
   -  `previousWord = ""`: משתנה לאחסון המילה האחרונה שהוזנה. בהתחלה זו מחרוזת ריקה.
   -  `currentPlayer = 1`: משתנה לאחסון מספר השחקן הנוכחי. מתחילים עם שחקן 1.
2. **בקשת המילה הראשונה**:
   -  `previousWord = input("Игрок 1, введите первое слово: ").strip()`: מבקש משחקן 1 להזין את המילה הראשונה ושומר אותה ב-`previousWord`, תוך הסרת רווחים בתחילת ובסוף המחרוזת.
   -  `currentPlayer = 2`: מחליף את השחקן הנוכחי לשחקן 2.
3. **לולאת המשחק הראשית**:
    -  `while True:`: מתחילה לולאה אינסופית הנמשכת עד שאחד השחקנים מזין '0'.
    - `currentWord = input(f"Игрок {currentPlayer}, введите слово: ").strip()`: מבקש מהשחקן הנוכחי להזין מילה, שומר אותה ב-`currentWord`, תוך הסרת רווחים בתחילת ובסוף המחרוזת.
   -  **בדיקת יציאה**:
      -  `if currentWord == '0':`: בודק האם השחקן הזין '0'. אם כן, המשחק מסתיים.
      - `print("Игра окончена.")`: מציג הודעה על סיום המשחק.
      -  `break`: מסיים את הלולאה.
   - **בדיקת האות הראשונה**:
      -   `if previousWord and currentWord[0].lower() != previousWord[-1].lower():`: בודק האם האות הראשונה של המילה הנוכחית תואמת את האות האחרונה של המילה הקודמת (ללא הבדלי רישיות).
      -   `print("Неверное слово, первая буква должна совпадать с последней буквой предыдущего слова.")`: מציג הודעת שגיאה אם הבדיקה נכשלה.
      -   `continue`: עובר לאיטרציה (סבב) הבאה של הלולאה.
   -   **הכנה לתור הבא**:
      - `previousWord = currentWord`: מעדכן את `previousWord` עם המילה הנוכחית.
      - `currentPlayer = 3 - currentPlayer`: מחליף את השחקן הנוכחי (אם היה שחקן 1, יהפוך לשחקן 2, ולהיפך).
4. **הכרזת המנצח**:
    - `print(f"Игрок {3 - currentPlayer} победил!")`: מציג הודעה על ניצחון השחקן הקודם (מכיוון שהחלפת השחקן הבא כבר התרחשה).
"""