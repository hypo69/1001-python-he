ACE:
=================
רמת מורכבות: 7
-----------------
המשחק "ACE" הוא משחק שבו שני שחקנים שולפים לסירוגין קלפים מחפיסה ומנסים לצבור ניקוד גבוה יותר. אס נחשב נקודה אחת, קלפים עם מספרים מ-2 עד 10 נחשבים לפי ערכם הנקוב, ונסיך, מלכה ומלך נחשבים 10 נקודות. השחקן שצובר ניקוד גבוה יותר מנצח. המשחק נמשך עד שמספר קבוע של סבבים מסתיים.

כללי המשחק:
1.  משחקים שני שחקנים.
2.  שחקנים שולפים קלפים מהחפיסה לסירוגין.
3.  לכל קלף יש מספר נקודות מסוים: אס - 1, קלפים מ-2 עד 10 - לפי ערכם הנקוב, נסיך, מלכה ומלך - 10.
4.  כל שחקן שואף לצבור כמה שיותר נקודות בסבב.
5.  בסוף הסבב, נקודות השחקנים מושוות.
6.  המשחק מורכב ממספר קבוע של סבבים.
7.  מנצח המשחק מוכרז השחקן שצבר את סך הניקוד הגבוה ביותר בכל הסבבים.
-----------------
אלגוריתם:
1.  אתחול נקודות של שחקנים 1 ו-2 לאפס.
2.  בקשת קלט למספר הסבבים.
3.  התחלת לולאה לפי מספר הסבבים:
    3.1. שחקן 1 שולף קלף.
    3.2. הצגת קלף שחקן 1 ומספר הנקודות עבור הקלף.
    3.3. הוספת נקודות הקלף לסך הנקודות של שחקן 1.
    3.4. שחקן 2 שולף קלף.
    3.5. הצגת קלף שחקן 2 ומספר הנקודות עבור הקלף.
    3.6. הוספת נקודות הקלף לסך הנקודות של שחקן 2.
    3.7. אם נקודות שחקן 1 גבוהות מנקודות שחקן 2, הצגת הודעה "PLAYER 1 WINS THE ROUND".
    3.8. אם נקודות שחקן 2 גבוהות מנקודות שחקן 1, הצגת הודעה "PLAYER 2 WINS THE ROUND".
    3.9. אם נקודות שחקן 1 שוות לנקודות שחקן 2, הצגת הודעה "TIE GAME THIS ROUND".
4.  הצגת סך הנקודות הכולל של שחקן 1.
5.  הצגת סך הנקודות הכולל של שחקן 2.
6.  אם סך הנקודות הכולל של שחקן 1 גבוה מסך הנקודות הכולל של שחקן 2, הצגת הודעה "PLAYER 1 WINS THE GAME".
7.  אם סך הנקודות הכולל של שחקן 2 גבוה מסך הנקודות הכולל של שחקן 1, הצגת הודעה "PLAYER 2 WINS THE GAME".
8.  אם סך הנקודות הכולל של שחקן 1 שווה לסך הנקודות הכולל של שחקן 2, הצגת הודעה "TIE GAME".
9.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeScores["<p align='left'>אתחול משתנים:<br><code><b>player1Score = 0</b></code><br><code><b>player2Score = 0</b></code></p>"]
    InitializeScores --> InputRounds["קלט מספר סבבים: <code><b>numberOfRounds</b></code>"]
    InputRounds --> RoundLoopStart{"התחלת לולאת הסבבים"}
    RoundLoopStart -- Yes --> Player1DrawsCard["שחקן 1 שולף קלף: <code><b>card1, card1Value</b></code>"]
    Player1DrawsCard --> OutputPlayer1Card["פלט קלף וניקוד שחקן 1: <code><b>card1, card1Value</b></code>"]
    OutputPlayer1Card --> UpdatePlayer1Score["<code><b>player1Score = player1Score + card1Value</b></code>"]
    UpdatePlayer1Score --> Player2DrawsCard["שחקן 2 שולף קלף: <code><b>card2, card2Value</b></code>"]
    Player2DrawsCard --> OutputPlayer2Card["פלט קלף וניקוד שחקן 2: <code><b>card2, card2Value</b></code>"]
    OutputPlayer2Card --> UpdatePlayer2Score["<code><b>player2Score = player2Score + card2Value</b></code>"]
    UpdatePlayer2Score --> CompareScores{"השוואת ניקוד בסבב: <code><b>card1Value > card2Value?</b></code>"}
    CompareScores -- Yes --> OutputPlayer1RoundWin["פלט: <b>שחקן 1 מנצח בסבב</b>"]
    CompareScores -- No --> CompareScores2{"השוואת ניקוד בסבב: <code><b>card2Value > card1Value?</b></code>"}
    CompareScores2 -- Yes --> OutputPlayer2RoundWin["פלט: <b>שחקן 2 מנצח בסבב</b>"]
    CompareScores2 -- No --> OutputTieRound["פלט: <b>שוויון בסבב זה</b>"]
    OutputPlayer1RoundWin --> RoundLoopEnd
    OutputPlayer2RoundWin --> RoundLoopEnd
    OutputTieRound --> RoundLoopEnd
     RoundLoopEnd --> RoundLoopStart {"התחלת לולאת הסבבים"}

    RoundLoopStart -- No --> OutputTotalPlayer1Score["פלט סך הניקוד של שחקן 1: <code><b>player1Score</b></code>"]
    OutputTotalPlayer1Score --> OutputTotalPlayer2Score["פלט סך הניקוד של שחקן 2: <code><b>player2Score</b></code>"]
    OutputTotalPlayer2Score --> CompareTotalScores{"השוואת סך הניקוד: <code><b>player1Score > player2Score?</b></code>"}
    CompareTotalScores -- Yes --> OutputPlayer1GameWin["פלט: <b>שחקן 1 מנצח במשחק</b>"]
    CompareTotalScores -- No --> CompareTotalScores2{"השוואת סך הניקוד: <code><b>player2Score > player1Score?</b></code>"}
     CompareTotalScores2 -- Yes --> OutputPlayer2GameWin["פלט: <b>שחקן 2 מנצח במשחק</b>"]
    CompareTotalScores2 -- No --> OutputTieGame["פלט: <b>שוויון במשחק</b>"]
    OutputPlayer1GameWin --> End["סוף"]
    OutputPlayer2GameWin --> End
    OutputTieGame --> End
```
**מקרא**
    Start - התחלת התוכנית.
    InitializeScores - אתחול משתני הניקוד של שחקנים player1Score ו-player2Score לאפס.
    InputRounds - בקשת קלט ממשתמש למספר הסבבים numberOfRounds של המשחק.
    RoundLoopStart - התחלת לולאה עבור כל סבב משחק. הלולאה מבוצעת numberOfRounds פעמים.
    Player1DrawsCard - שחקן 1 שולף קלף card1 ונקבע ערכו card1Value.
    OutputPlayer1Card - פלט למסך של מידע אודות קלף שחקן 1 card1 וערכו card1Value.
    UpdatePlayer1Score - עדכון סך הניקוד של שחקן 1, על ידי הוספת ערך הקלף card1Value ל-player1Score.
    Player2DrawsCard - שחקן 2 שולף קלף card2 ונקבע ערכו card2Value.
    OutputPlayer2Card - פלט למסך של מידע אודות קלף שחקן 2 card2 וערכו card2Value.
    UpdatePlayer2Score - עדכון סך הניקוד של שחקן 2, על ידי הוספת ערך הקלף card2Value ל-player2Score.
    CompareScores - השוואת ערכי הקלפים card1Value ו-card2Value לקביעת מנצח הסבב.
    OutputPlayer1RoundWin - פלט הודעה אודות ניצחון שחקן 1 בסבב.
    CompareScores2 - השוואת ערכי הקלפים card2Value ו-card1Value לקביעת מנצח הסבב.
    OutputPlayer2RoundWin - פלט הודעה אודות ניצחון שחקן 2 בסבב.
    OutputTieRound - פלט הודעה אודות שוויון בסבב.
    RoundLoopEnd - סוף לולאת הסבבים.
    OutputTotalPlayer1Score - פלט למסך של סך הניקוד הכולל של שחקן 1 player1Score.
    OutputTotalPlayer2Score - פלט למסך של סך הניקוד הכולל של שחקן 2 player2Score.
    CompareTotalScores - השוואת סך הניקוד הכולל של שחקנים player1Score ו-player2Score לקביעת מנצח המשחק.
    OutputPlayer1GameWin - פלט הודעה אודות ניצחון שחקן 1 במשחק.
     CompareTotalScores2 - השוואת סך הניקוד הכולל של שחקנים player2Score ו-player1Score לקביעת מנצח המשחק.
    OutputPlayer2GameWin - פלט הודעה אודות ניצחון שחקן 2 במשחק.
    OutputTieGame - פלט הודעה אודות שוויון במשחק.
    End - סוף התוכנית.