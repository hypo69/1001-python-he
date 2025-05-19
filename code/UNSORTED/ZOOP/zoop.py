ZOOP:
=================
רמת קושי: 5
-----------------
המשחק "ZOOP" הוא משחק טקסט פשוט, שבו השחקן מנסה לייצר סדרה של מספרים אקראיים שבה לא יופיעו שני מספרים זהים ברציפות. המשחק נמשך עד שהשחקן מייצר סדרה המפרה כלל זה, או שהוא מחליט לסיים את המשחק.

כללי המשחק:
1. המחשב מייצר מספר אקראי בין 1 ל-7.
2. אם המספר שנוצר זהה למספר שנוצר בפעם הקודמת, המשחק מסתיים.
3. המשחק נמשך עד שהשחקן מפר את הכלל או מזין '0' כדי לסיים את המשחק.
4. לאחר כל מהלך, המספר הנוכחי שנוצר מוצג.
-----------------
אלגוריתם:
1.  להגדיר את המספר הקודם (previousNumber) ל-0.
2.  להתחיל לולאה:
    2.1 לייצר מספר אקראי בין 1 ל-7 (currentNumber).
    2.2 אם המספר שנוצר שווה ל-0, לעבור לשלב 4.
    2.3 אם המספר שנוצר שווה למספר הקודם, לעבור לשלב 4.
    2.4 להציג את המספר הנוכחי שנוצר.
    2.5 להגדיר את המספר הקודם להיות שווה למספר הנוכחי.
3. לחזור על שלבים 2.1 עד 2.5
4. להציג את ההודעה "YOU BLEW IT!".
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializePreviousNumber["<p align='left'>אתחול:
    <code><b>previousNumber = 0</b></code></p>"]
    InitializePreviousNumber --> LoopStart{"תחילת לולאה"}
    LoopStart --> GenerateRandomNumber["יצירת מספר אקראי: <code><b>currentNumber = random(0, 7)</b></code>"]
    GenerateRandomNumber --> CheckQuit{"בדיקה: <code><b>currentNumber == 0</b></code>?"}
    CheckQuit -- כן --> OutputBlowIt["פלט: <b>YOU BLEW IT!</b>"]
    OutputBlowIt --> End["סיום"]
    CheckQuit -- לא --> CheckSame{"בדיקה: <code><b>currentNumber == previousNumber</b></code>?"}
    CheckSame -- כן --> OutputBlowIt
    CheckSame -- לא --> OutputCurrentNumber["פלט: <code><b>currentNumber</b></code>"]
    OutputCurrentNumber --> SetPreviousNumber["<code><b>previousNumber = currentNumber</b></code>"]
    SetPreviousNumber --> LoopStart
```

Legenda:
    Start - תחילת התוכנית.
    InitializePreviousNumber - אתחול המשתנה previousNumber (מספר קודם) בערך 0.
    LoopStart - תחילת לולאת המשחק הראשית.
    GenerateRandomNumber - יצירת מספר אקראי currentNumber בטווח שבין 0 ל-7.
    CheckQuit - בדיקה האם המספר שנוצר, currentNumber, שווה ל-0.
    OutputBlowIt - הדפסת ההודעה "YOU BLEW IT!" אם השחקן הפסיד.
    End - סיום התוכנית.
    CheckSame - בדיקה האם המספר שנוצר, currentNumber, שווה למספר הקודם previousNumber.
    OutputCurrentNumber - הדפסת המספר הנוכחי שנוצר, currentNumber.
    SetPreviousNumber - הגדרת ערך המשתנה previousNumber להיות שווה לערך המשתנה currentNumber.
"""
import random

# מאתחל את המשתנה לאחסון המספר הקודם.
previousNumber = 0

# מריץ את לולאת המשחק הראשית.
while True:
    # יוצר מספר אקראי מ-0 עד 7.
    currentNumber = random.randint(0, 7)

    # בודק האם המספר 0 נוצר, המעיד על סיום המשחק.
    if currentNumber == 0:
        print("YOU BLEW IT!") # מודיע על סיום המשחק.
        break  # יוצא מהלולאה.

    # בודק האם המספר הנוכחי שווה למספר הקודם.
    if currentNumber == previousNumber:
        print("YOU BLEW IT!") # מודיע על סיום המשחק.
        break  # יוצא מהלולאה.

    # מדפיס את המספר הנוכחי שנוצר.
    print(currentNumber)
    # שומר את המספר הנוכחי כמספר הקודם עבור האיטרציה הבאה.
    previousNumber = currentNumber

"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים.
2. **אתחול `previousNumber`**:
    -   `previousNumber = 0`: מאתחל את המשתנה `previousNumber` בערך אפס. משתנה זה יאחסן את המספר שנוצר בפעם הקודמת.
3. **לולאה אינסופית `while True:`**:
    -   לולאה זו נמשכת עד שתתבצע הפקודה `break` בתוך הלולאה.
4. **יצירת מספר אקראי**:
    -   `currentNumber = random.randint(0, 7)`: יוצר מספר שלם אקראי בטווח שבין 0 ל-7 (כולל) ושומר אותו במשתנה `currentNumber`.
5.  **בדיקה לסיום המשחק**:
    -   `if currentNumber == 0:`: בודק האם המספר שנוצר שווה ל-0. אם כן, הדבר מעיד על כך שהשחקן רצה לסיים את המשחק.
    -   `print("YOU BLEW IT!")`: מדפיס הודעה שהמשחק הסתיים.
    -   `break`: יוצא מהלולאה, ובכך מסיים את המשחק.
6.  **בדיקה לחזרה על מספר**:
    -   `if currentNumber == previousNumber:`: בודק האם המספר הנוכחי שנוצר שווה למספר שנוצר בפעם הקודמת.
    -   `print("YOU BLEW IT!")`: מדפיס הודעה שהמשחק הסתיים.
    -   `break`: יוצא מהלולאה, ובכך מסיים את המשחק.
7.  **הדפסת המספר הנוכחי**:
    -   `print(currentNumber)`: מדפיס את המספר שנוצר על המסך.
8.  **עדכון `previousNumber`**:
    -   `previousNumber = currentNumber`: שומר את המספר הנוכחי שנוצר במשתנה `previousNumber`, כך שניתן יהיה לבדוק אותו באיטרציה הבאה של הלולאה.
"""