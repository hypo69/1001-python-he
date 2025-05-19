CHIEF:
=================
מורכבות: 4
-----------------
המשחק "CHIEF" הוא משחק שבו השחקן מגלם תפקיד של מנהל שתפקידו לתכנן את הייצור במפעל. השחקן קובע את כמות הפריטים המיוצרים מכל סוג, והמחשב קובע האם ערכים אלה עומדים בדרישות הנדרשות. במידה ולא, השחקן מקבל מידע אילו ערכים בדיוק היו שגויים. מטרת המשחק היא להגיע לייצור אופטימלי באמצעות ניחוש נכון של כמות הפריטים.

כללי המשחק:
1.  המחשב מגריל שלושה ערכים בטווח שבין 1 ל-10: `targetA`, `targetB` ו-`targetC`.
2.  השחקן מזין את ניחושיו עבור הערכים `userA`, `userB` ו-`userC`.
3.  המחשב בודק האם הערכים שהוזנו תואמים לערכים שהוגרלו.
4.  אם כל שלושת הערכים נוחשו נכונה, המשחק מסתיים בניצחון.
5.  אם לפחות ערך אחד אינו תואם, המחשב מציג אילו ערכים בדיוק היו שגויים.
6.  המשחק ממשיך עד שהשחקן מנחש את כל שלושת הערכים.
-----------------
אלגוריתם:
1.  להגריל מספרים שלמים אקראיים `targetA`, `targetB` ו-`targetC` בטווח שבין 1 ל-10.
2.  להתחיל לולאת "כל עוד לא נוחשו כל המספרים":
    2.1 לבקש מהשחקן להזין שלושה מספרים שלמים: `userA`, `userB` ו-`userC`.
    2.2 לאתחל את המחרוזת `message` כמחרוזת ריקה.
    2.3 אם `userA` אינו שווה ל-`targetA`, להוסיף "A" ל-`message`.
    2.4 אם `userB` אינו שווה ל-`targetB`, להוסיף "B" ל-`message`.
    2.5 אם `userC` אינו שווה ל-`targetC`, להוסיף "C" ל-`message`.
    2.6 אם `message` אינה ריקה, להציג את ההודעה "WRONG ON " ואת תוכן `message`.
    2.7 אחרת, להציג את ההודעה "YOU GOT IT!".
3. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    targetA = random(1, 10)
    targetB = random(1, 10)
    targetC = random(1, 10)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד לא נוחש"}
    LoopStart --> InputValues["<p align='left'>קלט מספרים על ידי המשתמש:
    <code><b>
    userA
    userB
    userC
    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"בדיקה: <code><b>userA == targetA?</b></code>"}
    CheckA -- Нет --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"בדיקה: <code><b>userB == targetB?</b></code>"}
    CheckA -- Да --> CheckB
    CheckB -- Нет --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"בדיקה: <code><b>userC == targetC?</b></code>"}
    CheckB -- Да --> CheckC
    CheckC -- Нет --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"בדיקה: <code><b>message != "" ?</b></code>"}
    CheckC -- Да --> CheckMessage
    CheckMessage -- Да --> OutputWrong["פלט הודעה: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- Нет --> OutputWin["פלט הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    LoopStart -- Нет --> End
```
מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: `targetA`, `targetB`, `targetC` מוגרלים באקראי מ-1 עד 10.
    LoopStart - התחלת הלולאה, הנמשכת עד שהשחקן מנחש את כל המספרים.
    InputValues - בקשה מהמשתמש להזין שלושה מספרים `userA`, `userB`, `userC`.
    InitializeMessage - אתחול מחרוזת ריקה בשם `message`.
    CheckA - בדיקה האם המספר שהוזן `userA` שווה למספר שהוגרל `targetA`.
    AppendA - הוספת 'A' ל-`message` אם `userA` אינו שווה ל-`targetA`.
    CheckB - בדיקה האם המספר שהוזן `userB` שווה למספר שהוגרל `targetB`.
    AppendB - הוספת 'B' ל-`message` אם `userB` אינו שווה ל-`targetB`.
    CheckC - בדיקה האם המספר שהוזן `userC` שווה למספר שהוגרל `targetC`.
    AppendC - הוספת 'C' ל-`message` אם `userC` אינו שווה ל-`targetC`.
    CheckMessage - בדיקה האם המחרוזת `message` ריקה.
    OutputWrong - פלט ההודעה "WRONG ON" ותוכן `message` אם המחרוזת אינה ריקה.
    OutputWin - פלט ההודעה "YOU GOT IT!" אם המחרוזת `message` ריקה.
    End - סוף התוכנית.