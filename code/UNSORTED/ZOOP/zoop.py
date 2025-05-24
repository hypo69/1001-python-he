ZOOP:
=================
רמת קושי: 5
-----------------
המשחק "ZOOP" הוא משחק טקסט פשוט שבו השחקן מנסה ליצור רצף של מספרים אקראיים שבו לא יהיו שני מספרים זהים ברצף. המשחק נמשך עד שהשחקן מייצר רצף שמפר את הכלל הזה, או מחליט לסיים את המשחק.

חוקי המשחק:
1. המחשב מייצר מספר אקראי בין 1 ל-7.
2. אם המספר שנוצר זהה למספר שנוצר בסבב הקודם, המשחק מסתיים.
3. המשחק נמשך עד שהשחקן מפר את הכלל או מזין '0' כדי לסיים את המשחק.
4. לאחר כל מהלך, מוצג המספר הנוכחי שנוצר.
-----------------
אלגוריתם:
1.  מאתחל את המספר הקודם (previousNumber) ל-0.
2.  מתחיל לולאה:
    2.1 מייצר מספר אקראי בין 1 ל-7 (currentNumber).
    2.2 אם המספר שנוצר שווה ל-0, עבור לשלב 4.
    2.3 אם המספר שנוצר שווה למספר הקודם, עבור לשלב 4.
    2.4 מציג את המספר הנוכחי שנוצר.
    2.5 קובע את המספר הקודם להיות שווה למספר הנוכחי.
3. חוזר על השלבים מ-2.1 עד 2.5.
4. מציג הודעה "YOU BLEW IT!".
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
    CheckQuit -- Yes --> OutputBlowIt["פלט: <b>YOU BLEW IT!</b>"]
    OutputBlowIt --> End["סיום"]
    CheckQuit -- No --> CheckSame{"בדיקה: <code><b>currentNumber == previousNumber</b></code>?"}
    CheckSame -- Yes --> OutputBlowIt
    CheckSame -- No --> OutputCurrentNumber["פלט: <code><b>currentNumber</b></code>"]
    OutputCurrentNumber --> SetPreviousNumber["<code><b>previousNumber = currentNumber</b></code>"]
    SetPreviousNumber --> LoopStart
```

מקרא:
    Start - התחלת התוכנית.
    InitializePreviousNumber - אתחול המשתנה previousNumber (מספר קודם) בערך 0.
    LoopStart - תחילת הלולאה הראשית של המשחק.
    GenerateRandomNumber - יצירת מספר אקראי currentNumber בטווח שבין 0 ל-7.
    CheckQuit - בדיקה אם המספר שנוצר currentNumber שווה ל-0.
    OutputBlowIt - הצגת ההודעה "YOU BLEW IT!" אם השחקן הפסיד.
    End - סיום התוכנית.
    CheckSame - בדיקה אם המספר שנוצר currentNumber שווה למספר הקודם previousNumber.
    OutputCurrentNumber - הצגת המספר הנוכחי שנוצר currentNumber.
    SetPreviousNumber - קביעת ערך המשתנה previousNumber להיות שווה לערך המשתנה currentNumber.
"""
import random

# מאתחל את המשתנה לאחסון המספר הקודם.
previousNumber = 0

# מפעיל את הלולאה הראשית של המשחק.
while True:
    # יוצר מספר אקראי בין 0 ל-7.
    currentNumber = random.randint(0, 7)

    # בודק אם המשתמש הזין 0 לסיום המשחק.
    if currentNumber == 0:
        print("YOU BLEW IT!") # מודיע על סיום המשחק.
        break  # יוצא מהלולאה.

    # בודק אם המספר הנוכחי שווה למספר הקודם.
    if currentNumber == previousNumber:
        print("YOU BLEW IT!") # מודיע על סיום המשחק.
        break  # יוצא מהלולאה.

    # מציג את המספר הנוכחי שנוצר.
    print(currentNumber)
    # שומר את המספר הנוכחי כמספר הקודם עבור האיטרציה הבאה.
    previousNumber = currentNumber

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים.
2. **אתחול `previousNumber`**:
    -   `previousNumber = 0`: מאתחל את המשתנה `previousNumber` באפס. משתנה זה ישמור את המספר האקראי שנוצר בסבב הקודם.
3. **לולאה אינסופית `while True:`**:
    -   לולאה זו נמשכת עד אשר מבוצעת הפקודה `break` בתוך הלולאה.
4. **יצירת מספר אקראי**:
    -   `currentNumber = random.randint(0, 7)`: יוצר מספר שלם אקראי בטווח שבין 0 ל-7 (כולל הקצוות) ושומר אותו במשתנה `currentNumber`.
5.  **בדיקה לסיום המשחק**:
    -   `if currentNumber == 0:`: בודק אם המספר שנוצר שווה ל-0. אם כן, הדבר מצביע על כך שהשחקן רצה לסיים את המשחק.
    -   `print("YOU BLEW IT!")`: מציג הודעה המציינת שהמשחק הסתיים.
    -   `break`: יוצא מהלולאה, ובכך מסיים את המשחק.
6.  **בדיקה לחזרה על מספר**:
    -   `if currentNumber == previousNumber:`: בודק אם המספר הנוכחי שנוצר שווה למספר שנוצר בסבב הקודם.
    -   `print("YOU BLEW IT!")`: מציג הודעה המציינת שהמשחק הסתיים.
    -   `break`: יוצא מהלולאה, ובכך מסיים את המשחק.
7.  **הצגת המספר הנוכחי**:
    -   `print(currentNumber)`: מציג את המספר שנוצר על המסך.
8.  **עדכון `previousNumber`**:
    -   `previousNumber = currentNumber`: שומר את המספר הנוכחי שנוצר במשתנה `previousNumber`, כך שניתן יהיה לבדוק אותו באיטרציה הבאה של הלולאה.
"""