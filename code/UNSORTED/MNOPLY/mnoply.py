**MNOPLY:**
=================
**מורכבות:** 5
-----------------
המשחק "מונופולי" הוא גרסה פשוטה של משחק לוח, שבו שני שחקנים מטילים קובייה לסירוגין ונעים על פני לוח משחק המורכב מ-24 תאים.
לכל תא יש עלות מסוימת, אותה השחקן משלם או מקבל.
מטרת המשחק היא להישאר עם הסכום הכספי הגדול ביותר לאחר מספר מוגדר של סיבובים.

**כללי המשחק:**
1. השחקנים מתחילים את המשחק עם סכום כסף התחלתי.
2. השחקנים מטילים קובייה לסירוגין (מספר מ-1 עד 6) ונעים על פני לוח המשחק (24 תאים).
3. לכל תא יש עלות משלו (חיובית או שלילית). כאשר שחקן נוחת על תא, הוא משלם או מקבל עלות זו.
4. השחקנים משחקים מספר מוגדר של סיבובים.
5. לאחר כל הסיבובים, השחקן עם סכום הכסף הגדול ביותר מנצח.
-----------------
**אלגוריתם:**
1. קביעת הון התחלתי לשני השחקנים.
2. אתחול עלויות תאי לוח המשחק.
3. קביעת מספר הסיבובים.
4. עבור כל סיבוב:
    4.1 עבור כל שחקן:
        4.1.1 הטלת קובייה (מספר אקראי מ-1 עד 6).
        4.1.2 הזזת השחקן במספר התאים המתאים (תוך התחשבות בלוח המעגלי).
        4.1.3 החלת עלות התא על הון השחקן.
        4.1.4 הצגת מיקום והון השחקן הנוכחיים על המסך.
5. לאחר כל הסיבובים, זיהוי והצגת המנצח.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["התחלה"] --> Initialize["<p align='left'>אתחול:
    <code><b>player1Money = 1500<br>player2Money = 1500<br>boardValues = [...]<br>numberOfRounds = 10</b></code></p>"]
    Initialize --> RoundLoopStart{"התחלת לולאה: עבור כל סיבוב"}
    RoundLoopStart -- כן --> PlayerLoopStart{"התחלת לולאה: עבור כל שחקן"}
    PlayerLoopStart -- כן --> RollDice["הטלת קובייה: <code><b>diceRoll = random(1, 6)</b></code>"]
    RollDice --> MovePlayer["הזזת שחקן: <code><b>currentPlayerPosition = (currentPlayerPosition + diceRoll) % 24</b></code>"]
    MovePlayer --> UpdateMoney["עדכון כסף שחקן: <code><b>currentPlayerMoney = currentPlayerMoney + boardValues[currentPlayerPosition]</b></code>"]
    UpdateMoney --> DisplayStatus["הצגת מיקום וכסף שחקן"]
    DisplayStatus --> PlayerLoopEnd{"סוף לולאה: עבור כל שחקן"}
    PlayerLoopEnd -- כן --> PlayerLoopStart
    PlayerLoopEnd -- לא --> RoundLoopEnd{"סוף לולאה: עבור כל סיבוב"}
    RoundLoopEnd -- כן --> RoundLoopStart
    RoundLoopEnd -- לא --> DetermineWinner["זיהוי המנצח"]
    DetermineWinner --> OutputWinner["הצגת המנצח"]
    OutputWinner --> End["סיום"]
    PlayerLoopStart -- לא --> RoundLoopEnd

```

**מקרא:**
    Start - התחלת התוכנית.
    Initialize - אתחול ערכים התחלתיים: כסף התחלתי של השחקנים (player1Money, player2Money), עלויות תאי לוח המשחק (boardValues) ומספר הסיבובים (numberOfRounds).
    RoundLoopStart - התחלת לולאה שחוזרת על עצמה עבור כל סיבוב של המשחק.
    PlayerLoopStart - התחלת לולאה שחוזרת על עצמה עבור כל שחקן בסיבוב הנוכחי.
    RollDice - הטלת קובייה, שתוצאתה היא מספר אקראי בין 1 ל-6 (diceRoll).
    MovePlayer - הזזת השחקן הנוכחי על לוח המשחק במספר עמדות לפי diceRoll, תוך התחשבות בלוח המחזורי (24 תאים).
    UpdateMoney - עדכון סכום הכסף של השחקן הנוכחי בהתאם לעלות התא עליו הוא עצר.
    DisplayStatus - הצגת המיקום הנוכחי וסכום הכסף של השחקן הנוכחי.
    PlayerLoopEnd - סוף הלולאה עבור כל שחקן.
    RoundLoopEnd - סוף הלולאה עבור כל סיבוב.
    DetermineWinner - זיהוי המנצח לאחר השלמת כל הסיבובים.
    OutputWinner - הצגת שם המנצח במשחק.
    End - סוף התוכנית.
"""
import random

# אתחול פרמטרים התחלתיים של המשחק
player1Money = 1500  # הון התחלתי של השחקן הראשון
player2Money = 1500  # הון התחלתי של השחקן השני
boardValues = [  # עלות כל תא בלוח המשחק
    -200, 100, -100, 200, -50, 50, -150, 150, 0,
    -200, 100, -100, 200, -50, 50, -150, 150, 0,
    -200, 100, -100, 200, -50, 50
]
numberOfRounds = 10  # מספר הסיבובים במשחק
player1Position = 0 # מיקום התחלתי של השחקן הראשון
player2Position = 0 # מיקום התחלתי של השחקן השני


# לולאת המשחק הראשית לפי סיבובים
for roundNumber in range(1, numberOfRounds + 1):
    print(f"\nסיבוב {roundNumber}") # הצגת מספר הסיבוב
    # לולאה עבור כל שחקן
    for player in range(1, 3):
        print(f"שחקן {player}:")
        # הטלת קובייה
        diceRoll = random.randint(1, 6)
        print(f"   תוצאת קובייה: {diceRoll}")

        # הזזת שחקן
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

# זיהוי המנצח לאחר כל הסיבובים
print("\nהמשחק הסתיים!")
if player1Money > player2Money:
    print(f"שחקן 1 ניצח עם {player1Money} כסף!")
elif player2Money > player1Money:
    print(f"שחקן 2 ניצח עם {player2Money} כסף!")
else:
    print(f"תיקו, לשני השחקנים {player1Money} כסף")


"""
**הסבר קוד:**

1.  **אתחול משתנים**:
    -   `player1Money = 1500`: מגדיר את ההון ההתחלתי של השחקן הראשון.
    -   `player2Money = 1500`: מגדיר את ההון ההתחלתי של השחקן השני.
    -   `boardValues`: רשימה המייצגת את עלויות תאי לוח המשחק (חיוביות או שליליות).
    -   `numberOfRounds = 10`: מגדיר את מספר הסיבובים הכולל של המשחק.
     -   `player1Position = 0`: מיקום התחלתי של השחקן הראשון.
    -   `player2Position = 0`: מיקום התחלתי של השחקן השני.

2.  **לולאת המשחק הראשית**:
    -   `for roundNumber in range(1, numberOfRounds + 1):`: לולאה שעוברת על כל סיבוב במשחק.
        -   הצגת מספר הסיבוב הנוכחי.
    -   `for player in range(1, 3):`: לולאה שעוברת על כל שחקן בכל סיבוב.
        -   הצגת מידע על השחקן הנוכחי.
        -   `diceRoll = random.randint(1, 6)`: מייצר מספר אקראי (תוצאת הטלת קובייה).
        -   הצגת תוצאת הטלת הקובייה.
       -  **הזזת שחקן**:
          - `if player == 1:`: בדיקה מי השחקן הנוכחי.
          - `player1Position = (player1Position + diceRoll) % 24`: חישוב המיקום החדש של השחקן הראשון, תוך התחשבות במחזוריות לוח המשחק.
          -  `currentPosition = player1Position`: המיקום הנוכחי של השחקן הראשון.
          -  `player1Money += boardValues[currentPosition]`: עדכון הון השחקן הראשון, על ידי הוספה או הפחתה של עלות התא.
          - `currentMoney = player1Money`: סכום הכסף הנוכחי של השחקן הראשון.
          - `else:`: פעולות עבור השחקן השני דומות, תוך שימוש במשתנים המתאימים.
        -   `print(f"   מיקום: {currentPosition + 1}, כסף: {currentMoney}")`: הצגת מיקום השחקן הנוכחי וההון שלו.

3.  **זיהוי המנצח**:
    -  `print("\nהמשחק הסתיים!")`: הצגת הודעה על סיום המשחק.
    -   `if player1Money > player2Money:`: השוואת הון השחקנים לזיהוי המנצח.
        -   הצגת מידע על המנצח או על תיקו.
"""