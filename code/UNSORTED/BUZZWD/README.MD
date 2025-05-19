BUZZWD:
=================
רמת מורכבות: 4
-----------------
המשחק "BUZZWD" הוא משחק מספרים פשוט, שבו המחשב יוצר מספר אקראי, והשחקן נדרש לנחש אותו על ידי הזנת מספרים ברצף. לאחר כל קלט, התוכנית מודיעה האם המספר שהוזן הוא "גבוה מדי", "נמוך מדי", או שהוא נתגלה. המשחק מסתיים כאשר השחקן מנחש את המספר הנכון.

כללי המשחק:
1. המחשב בוחר מספר שלם אקראי בטווח 1 עד 100.
2. השחקן מזין את ניחושיו לגבי המספר הנבחר.
3. לאחר כל ניסיון, המחשב מודיע האם המספר שהוזן היה נמוך מדי, גבוה מדי, או שהוא נתגלה.
4. המשחק נמשך עד שהשחקן מנחש את המספר הנבחר כהלכה.
-----------------
אלגוריתם:
1.  אפס את מונה הניסיונות ל-0.
2.  צור מספר אקראי בטווח 1 עד 100.
3.  התחל לולאה "כל עוד המספר לא נתגלה":
    3.1 הגדל את מונה הניסיונות ב-1.
    3.2 בקש מהשחקן להזין מספר.
    3.3 אם המספר שהוזן שווה למספר הנבחר, הצג הודעה "נתגלה" ועבור לשלב 4.
    3.4 אם המספר שהוזן קטן מהמספר הנבחר, הצג הודעה "נמוך מדי".
    3.5 אם המספר שהוזן גדול מהמספר הנבחר, הצג הודעה "גבוה מדי".
4. הצג הודעה "ניסיונות {מונה ניסיונות}"
5. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfGuesses = 0
    targetNumber = random(1, 100)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד לא נתגלה"}
    LoopStart -- Да --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מספר מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- Да --> OutputWin["הצגת הודעה: <b>נתגלה</b>"]
    OutputWin --> OutputAttempts["הצגת הודעה: <b>ניסיונות {numberOfGuesses}</b>"]
    OutputAttempts --> End["סיום"]
    CheckGuess -- Нет --> CheckLow{"בדיקה: <code><b>userGuess &lt; targetNumber</b></code>?"}
    CheckLow -- Да --> OutputLow["הצגת הודעה: <b>נמוך מדי</b>"]
    OutputLow --> LoopStart
    CheckLow -- Нет --> OutputHigh["הצגת הודעה: <b>גבוה מדי</b>"]
    OutputHigh --> LoopStart
    LoopStart -- Нет --> End

```

מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מונה ניסיונות) מאופס ל-0, ו- targetNumber (המספר הנבחר) נוצר באופן אקראי בטווח 1 עד 100.
    LoopStart - התחלת לולאה הנמשכת כל עוד המספר לא נתגלה.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - בקשת קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר userGuess שהוזן שווה למספר targetNumber הנבחר.
    OutputWin - הצגת ההודעה "נתגלה" אם המספרים שווים.
    OutputAttempts - הצגת ההודעה "ניסיונות {numberOfGuesses}", עם ציון מספר הניסיונות.
    End - סיום התוכנית.
    CheckLow - בדיקה האם המספר userGuess שהוזן קטן מהמספר targetNumber הנבחר.
    OutputLow - הצגת ההודעה "נמוך מדי" אם המספר שהוזן קטן מהנבחר.
    OutputHigh - הצגת ההודעה "גבוה מדי" אם המספר שהוזן גדול מהנבחר.