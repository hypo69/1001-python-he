MNOPLY:
=================
רמת מורכבות: 5
-----------------
המשחק "מונופולי" הינו גרסה מפושטת של משחק קופסה, בו שני שחקנים בתורם מטילים קובייה ונעים על פני לוח משחק בן 24 משבצות.
לכל משבצת על הלוח קיימת עלות מסוימת, אותה השחקן משלם או מקבל עם ההגעה אליה.
מטרת המשחק היא להישאר עם סכום הכסף הגדול ביותר בתום מספר מוגדר של סבבים.

כללי המשחק:
1. השחקנים פותחים את המשחק עם סכום כסף התחלתי.
2. שחקנים בתורם מטילים קובייה (מספר אקראי בין 1 ל-6) ומתקדמים על פני לוח המשחק (24 משבצות).
3. לכל משבצת עלות משלה (חיובית או שלילית). עם ההגעה למשבצת, השחקן משלם את העלות או מקבל אותה.
4. השחקנים משחקים מספר מוגדר של סבבים.
5. בתום כל הסבבים, השחקן בעל סכום הכסף הגבוה ביותר מנצח.
-----------------
אלגוריתם:
1. קביעת הון התחלתי עבור שני השחקנים.
2. אתחול עלויות משבצות לוח המשחק.
3. קביעת מספר הסבבים.
4. עבור כל סבב:
    4.1 עבור כל שחקן:
        4.1.1 הטלת קובייה (מספר אקראי בין 1 ל-6).
        4.1.2 הזזת השחקן מספר מתאים של משבצות (תוך התחשבות במבנה המעגלי של הלוח).
        4.1.3 החלת עלות המשבצת על הון השחקן.
        4.1.4 הצגת המיקום הנוכחי וההון של השחקן על המסך.
5. בתום כל הסבבים, קביעת המנצח והצגתו.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> Initialize["<p align='left'>אתחול:
    <code><b>player1Money = 1500<br>player2Money = 1500<br>boardValues = [...]<br>numberOfRounds = 10</b></code></p>"]
    Initialize --> RoundLoopStart{"התחלת לולאה: עבור כל סבב"}
    RoundLoopStart -- Да --> PlayerLoopStart{"התחלת לולאה: עבור כל שחקן"}
    PlayerLoopStart -- Да --> RollDice["הטלת קובייה: <code><b>diceRoll = random(1, 6)</b></code>"]
    RollDice --> MovePlayer["הזזת שחקן: <code><b>currentPlayerPosition = (currentPlayerPosition + diceRoll) % 24</b></code>"]
    MovePlayer --> UpdateMoney["עדכון כספי השחקן: <code><b>currentPlayerMoney = currentPlayerMoney + boardValues[currentPlayerPosition]</b></code>"]
    UpdateMoney --> DisplayStatus["הצגת מיקום וכספי השחקן"]
    DisplayStatus --> PlayerLoopEnd{"סיום לולאה: עבור כל שחקן"}
    PlayerLoopEnd -- Да --> PlayerLoopStart
    PlayerLoopEnd -- Нет --> RoundLoopEnd{"סיום לולאה: עבור כל סבב"}
    RoundLoopEnd -- Да --> RoundLoopStart
    RoundLoopEnd -- Нет --> DetermineWinner["קביעת המנצח"]
    DetermineWinner --> OutputWinner["הצגת המנצח"]
    OutputWinner --> End["סיום"]
    PlayerLoopStart -- Нет --> RoundLoopEnd

```

מקרא:
    Start - תחילת התוכנית.
    Initialize - אתחול ערכים התחלתיים: כספים התחלתיים של השחקנים (player1Money, player2Money), עלויות משבצות לוח המשחק (boardValues) ומספר הסבבים (numberOfRounds).
    RoundLoopStart - תחילת הלולאה החוזרת על עצמה עבור כל סבב משחק.
    PlayerLoopStart - תחילת הלולאה החוזרת על עצמה עבור כל שחקן בסבב הנוכחי.
    RollDice - הטלת קובייה, שתוצאתה מספר אקראי בין 1 ל-6 (diceRoll).
    MovePlayer - הזזת השחקן הנוכחי על פני לוח המשחק במספר עמדות השווה ל-diceRoll, תוך התחשבות במבנה המחזורי של הלוח (24 משבצות).
    UpdateMoney - עדכון סכום הכסף של השחקן הנוכחי בהתאם לעלות המשבצת עליה הוא נחת.
    DisplayStatus - הצגת המיקום הנוכחי וסכום הכסף של השחקן הנוכחי.
    PlayerLoopEnd - סיום הלולאה עבור כל שחקן.
    RoundLoopEnd - סיום הלולאה עבור כל סבב.
    DetermineWinner - קביעת המנצח לאחר סיום כל הסבבים.
    OutputWinner - הצגת שם המנצח במשחק.
    End - סיום התוכנית.
```
import random

# אתחול פרמטרים התחלתיים של המשחק
player1Money = 1500  # הון התחלתי של השחקן הראשון
player2Money = 1500  # הון התחלתי של השחקן השני
boardValues = [  # עלות כל משבצת בלוח המשחק
    -200, 100, -100, 200, -50, 50, -150, 150, 0,
    -200, 100, -100, 200, -50, 50, -150, 150, 0,
    -200, 100, -100, 200, -50, 50
]
numberOfRounds = 10  # מספר סבבי המשחק
player1Position = 0 # מיקום התחלתי של השחקן הראשון
player2Position = 0 # מיקום התחלתי של השחקן השני


# לולאת המשחק הראשית לפי סבבים
for roundNumber in range(1, numberOfRounds + 1):
    print(f"\nסבב {roundNumber}") # מציגים את מספר הסבב
    # לולאה עבור כל שחקן
    for player in range(1, 3):
        print(f"שחקן {player}:")
        # הטלת קובייה
        diceRoll = random.randint(1, 6)
        print(f"   הטלת קובייה: {diceRoll}")

        # הזזת השחקן
        if player == 1:
            player1Position = (player1Position + diceRoll) % 24
            currentPosition = player1Position
            player1Money += boardValues[currentPosition]
            currentMoney = player1Money
        else:
            player2Position = (player2Position + diceRoll) % 24
            currentPosition = player2Position
            player2Money += boardValues[currentPosition]
            currentMoney = player2Money
        
        print(f"   מיקום: {currentPosition + 1}, כסף: {currentMoney}")

# קביעת המנצח לאחר כל הסבבים
print("\nהמשחק הסתיים!")
if player1Money > player2Money:
    print(f"שחקן 1 ניצח עם {player1Money} כסף!")
elif player2Money > player1Money:
    print(f"שחקן 2 ניצח עם {player2Money} כסף!")
else:
    print(f"שוויון, לשני השחקנים {player1Money} כסף")


"""
הסבר הקוד:

1.  **אתחול משתנים**:
    -   `player1Money = 1500`: מגדיר את ההון ההתחלתי של השחקן הראשון.
    -   `player2Money = 1500`: מגדיר את ההון ההתחלתי של השחקן השני.
    -   `boardValues`: רשימה המייצגת את עלויות משבצות לוח המשחק (חיוביות או שליליות).
    -   `numberOfRounds = 10`: מגדיר את המספר הכולל של סבבי המשחק.
     -   `player1Position = 0`: מיקום התחלתי של השחקן הראשון.
    -   `player2Position = 0`: מיקום התחלתי של השחקן השני.

2.  **לולאת המשחק הראשית**:
    -   `for roundNumber in range(1, numberOfRounds + 1):`: לולאה החוזרת על עצמה עבור כל סבב משחק.
        -   מציג את מספר הסבב הנוכחי.
    -   `for player in range(1, 3):`: לולאה החוזרת על עצמה עבור כל שחקן בכל סבב.
        -   מציג מידע על השחקן הנוכחי.
        -   `diceRoll = random.randint(1, 6)`: מייצר מספר אקראי (תוצאת הטלת הקובייה).
        -   מציג את תוצאת הטלת הקובייה.
       -  **הזזת שחקן**:
          - `if player == 1:`: בדיקה איזה שחקן הוא השחקן הנוכחי.
          - `player1Position = (player1Position + diceRoll) % 24`: מחשב את המיקום החדש של השחקן הראשון, תוך התחשבות במחזוריות לוח המשחק.
          -  `currentPosition = player1Position`: המיקום הנוכחי של השחקן הראשון.
          -  `player1Money += boardValues[currentPosition]`: מעדכן את ההון של השחקן הראשון, מוסיף או מחסיר את עלות המשבצת.
          - `currentMoney = player1Money`: סכום הכסף הנוכחי של השחקן הראשון.
          - `else:`: פעולות עבור השחקן השני דומות, באמצעות המשתנים המתאימים.
        -   `print(f"   מיקום: {currentPosition + 1}, כסף: {currentMoney}")`: מציג את המיקום הנוכחי של השחקן ואת הונו.

3.  **קביעת המנצח**:
    -  `print("\nהמשחק הסתיים!")`: מציג הודעה על סיום המשחק.
    -   `if player1Money > player2Money:`: השוואת הון השחקנים לקביעת המנצח.
        -   מציג מידע על המנצח או על תוצאת שוויון.
"""