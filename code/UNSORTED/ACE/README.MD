ACE:
=================
מורכבות: 7
-----------------
המשחק "ACE" הוא משחק שבו שני שחקנים שולפים קלפים בתורם מחפיסה ומנסים לצבור יותר נקודות. אס נחשב כנקודה 1, קלפים ממוספרים מ-2 עד 10 נחשבים לפי ערכם הנקוב, ונסיך, מלכה ומלך נחשבים כ-10 נקודות. השחקן שצבר את מירב הנקודות מנצח. המשחק נמשך עד שישוחק מספר מוגדר של סבבים.

חוקי המשחק:
1.  משחקים שני שחקנים.
2.  השחקנים שולפים קלפים בתורם מחפיסה.
3.  לכל קלף מספר מוגדר של נקודות: אס - 1, קלפים מ-2 עד 10 - לפי ערכם הנקוב, נסיך, מלכה ומלך - 10.
4.  כל שחקן שואף לצבור כמה שיותר נקודות בסבב.
5.  בסוף הסבב מושווים ניקודי השחקנים.
6.  המשחק מורכב ממספר מוגדר של סבבים.
7.  המנצח במשחק מוכרז השחקן שצבר את מירב הנקודות על פני כל הסבבים.
-----------------
אלגוריתם:
1.  אתחול ניקודי שחקנים 1 ו-2 לאפס.
2.  בקשת מספר הסבבים.
3.  התחלת לולאה לפי מספר הסבבים:
    3.1. שחקן 1 שולף קלף.
    3.2. הצגת קלף שחקן 1 ומספר הנקודות עבור הקלף.
    3.3. הוספת הנקודות עבור הקלף לניקוד הכולל של שחקן 1.
    3.4. שחקן 2 שולף קלף.
    3.5. הצגת קלף שחקן 2 ומספר הנקודות עבור הקלף.
    3.6. הוספת הנקודות עבור הקלף לניקוד הכולל של שחקן 2.
    3.7. אם ניקוד שחקן 1 גבוה מניקוד שחקן 2, הצגת הודעה "PLAYER 1 WINS THE ROUND".
    3.8. אם ניקוד שחקן 2 גבוה מניקוד שחקן 1, הצגת הודעה "PLAYER 2 WINS THE ROUND".
    3.9. אם ניקוד שחקן 1 שווה לניקוד שחקן 2, הצגת הודעה "TIE GAME THIS ROUND".
4.  הצגת הניקוד הכולל של שחקן 1.
5.  הצגת הניקוד הכולל של שחקן 2.
6.  אם הניקוד הכולל של שחקן 1 גבוה מהניקוד הכולל של שחקן 2, הצגת הודעה "PLAYER 1 WINS THE GAME".
7.  אם הניקוד הכולל של שחקן 2 גבוה מהניקוד הכולל של שחקן 1, הצגת הודעה "PLAYER 2 WINS THE GAME".
8.  אם הניקוד הכולל של שחקן 1 שווה לניקוד הכולל של שחקן 2, הצגת הודעה "TIE GAME".
9.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeScores["<p align='left'>Инициализация переменных:<br><code><b>player1Score = 0</b></code><br><code><b>player2Score = 0</b></code></p>"]
    InitializeScores --> InputRounds["Ввод количества раундов: <code><b>numberOfRounds</b></code>"]
    InputRounds --> RoundLoopStart{"Начало цикла по раундам"}
    RoundLoopStart -- Да --> Player1DrawsCard["Игрок 1 тянет карту: <code><b>card1, card1Value</b></code>"]
    Player1DrawsCard --> OutputPlayer1Card["Вывод карты и очков игрока 1: <code><b>card1, card1Value</b></code>"]
    OutputPlayer1Card --> UpdatePlayer1Score["<code><b>player1Score = player1Score + card1Value</b></code>"]
    UpdatePlayer1Score --> Player2DrawsCard["Игрок 2 тянет карту: <code><b>card2, card2Value</b></code>"]
    Player2DrawsCard --> OutputPlayer2Card["Вывод карты и очков игрока 2: <code><b>card2, card2Value</b></code>"]
    OutputPlayer2Card --> UpdatePlayer2Score["<code><b>player2Score = player2Score + card2Value</b></code>"]
    UpdatePlayer2Score --> CompareScores{"Сравнение очков за раунд: <code><b>card1Value > card2Value?</b></code>"}
    CompareScores -- Да --> OutputPlayer1RoundWin["Вывод: <b>PLAYER 1 WINS THE ROUND</b>"]
    CompareScores -- Нет --> CompareScores2{"Сравнение очков за раунд: <code><b>card2Value > card1Value?</b></code>"}
    CompareScores2 -- Да --> OutputPlayer2RoundWin["Вывод: <b>PLAYER 2 WINS THE ROUND</b>"]
    CompareScores2 -- Нет --> OutputTieRound["Вывод: <b>TIE GAME THIS ROUND</b>"]
    OutputPlayer1RoundWin --> RoundLoopEnd
    OutputPlayer2RoundWin --> RoundLoopEnd
    OutputTieRound --> RoundLoopEnd
     RoundLoopEnd --> RoundLoopStart {"Начало цикла по раундам"}

    RoundLoopStart -- Нет --> OutputTotalPlayer1Score["Вывод общего количества очков игрока 1: <code><b>player1Score</b></code>"]
    OutputTotalPlayer1Score --> OutputTotalPlayer2Score["Вывод общего количества очков игрока 2: <code><b>player2Score</b></code>"]
    OutputTotalPlayer2Score --> CompareTotalScores{"Сравнение общих очков: <code><b>player1Score > player2Score?</b></code>"}
    CompareTotalScores -- Да --> OutputPlayer1GameWin["Вывод: <b>PLAYER 1 WINS THE GAME</b>"]
    CompareTotalScores -- Нет --> CompareTotalScores2{"Сравнение общих очков: <code><b>player2Score > player1Score?</b></code>"}
     CompareTotalScores2 -- Да --> OutputPlayer2GameWin["Вывод: <b>PLAYER 2 WINS THE GAME</b>"]
    CompareTotalScores2 -- Нет --> OutputTieGame["Вывод: <b>TIE GAME</b>"]
    OutputPlayer1GameWin --> End["Конец"]
    OutputPlayer2GameWin --> End
    OutputTieGame --> End
```
**מקרא**
Start - התחלת התוכנית.
InitializeScores - אתחול משתני הניקוד לשחקנים player1Score ו-player2Score לאפס.
InputRounds - בקשת מספר הסבבים numberOfRounds מהמשתמש עבור המשחק.
RoundLoopStart - התחלת לולאה עבור כל סבב משחק. הלולאה מתבצעת numberOfRounds פעמים.
Player1DrawsCard - שחקן 1 שולף קלף card1 ונקבע ערכו card1Value.
OutputPlayer1Card - הצגת המידע על קלף שחקן 1 card1 וערכו card1Value על המסך.
UpdatePlayer1Score - עדכון הניקוד הכולל של שחקן 1, על ידי הוספת הערך card1Value ל-player1Score.
Player2DrawsCard - שחקן 2 שולף קלף card2 ונקבע ערכו card2Value.
OutputPlayer2Card - הצגת המידע על קלף שחקן 2 card2 וערכו card2Value על המסך.
UpdatePlayer2Score - עדכון הניקוד הכולל של שחקן 2, על ידי הוספת הערך card2Value ל-player2Score.
CompareScores - השוואת ערכי הקלפים card1Value ו-card2Value לקביעת מנצח הסבב.
OutputPlayer1RoundWin - הצגת הודעה על ניצחון שחקן 1 בסבב.
CompareScores2 - השוואת ערכי הקלפים card2Value ו-card1Value לקביעת מנצח הסבב.
OutputPlayer2RoundWin - הצגת הודעה על ניצחון שחקן 2 בסבב.
OutputTieRound - הצגת הודעה על תיקו בסבב.
RoundLoopEnd - סוף הלולאה של הסבבים.
OutputTotalPlayer1Score - הצגת הניקוד הכולל של שחקן 1 player1Score על המסך.
OutputTotalPlayer2Score - הצגת הניקוד הכולל של שחקן 2 player2Score על המסך.
CompareTotalScores - השוואת הניקוד הכולל של השחקנים player1Score ו-player2Score לקביעת מנצח המשחק.
OutputPlayer1GameWin - הצגת הודעה על ניצחון שחקן 1 במשחק.
CompareTotalScores2 - השוואת הניקוד הכולל של השחקנים player2Score ו-player1Score לקביעת מנצח המשחק.
OutputPlayer2GameWin - הצגת הודעה על ניצחון שחקן 2 במשחק.
OutputTieGame - הצגת הודעה על תיקו במשחק.
End - סוף התוכנית.