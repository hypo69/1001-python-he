CHIEF:
=================
רמת מורכבות: 4
-----------------
המשחק "צ'יף" הוא משחק שבו השחקן מגלם את תפקיד המנהל המתכנן את הייצור במפעל. השחקן קובע את כמות המוצרים המיוצרים מכל סוג, והמחשב קובע אם ערכים אלו עומדים בדרישות הנדרשות. אם לא, השחקן מקבל מידע אילו ערכים בדיוק היו שגויים. מטרת המשחק היא להגיע לייצור אופטימלי על ידי ניחוש נכון של כמות המוצרים.

כללי המשחק:
1.  המחשב מגריל שלושה ערכים בטווח שבין 1 ל-10: `targetA`, `targetB` ו-`targetC`.
2.  השחקן מזין את ניחושיו לגבי הערכים: `userA`, `userB` ו-`userC`.
3.  המחשב בודק אם הערכים שהוזנו תואמים לערכים שהוגרלו.
4.  אם כל שלושת הערכים נוחשו נכונה, המשחק מסתיים בניצחון.
5.  אם לפחות ערך אחד אינו תואם, המחשב מציג אילו ערכים בדיוק היו שגויים.
6.  המשחק נמשך עד שהשחקן מנחש את כל שלושת הערכים.
-----------------
אלגוריתם:
1.  הגרל שלושה מספרים שלמים אקראיים: `targetA`, `targetB` ו-`targetC`, בטווח שבין 1 ל-10.
2.  התחל לולאה "כל עוד לא נוחשו כל המספרים":
    2.1 בקש מהשחקן להזין שלושה מספרים שלמים: `userA`, `userB` ו-`userC`.
    2.2 אתחל את המחרוזת `message` כמחרוזת ריקה.
    2.3 אם `userA` אינו שווה ל-`targetA`, הוסף "A" ל-`message`.
    2.4 אם `userB` אינו שווה ל-`targetB`, הוסף "B" ל-`message`.
    2.5 אם `userC` אינו שווה ל-`targetC`, הוסף "C" ל-`message`.
    2.6 אם `message` אינה ריקה, הצג את ההודעה "WRONG ON " ואת תוכן `message`.
    2.7 אחרת, הצג את ההודעה "YOU GOT IT!".
3. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:\u200f
    <code><b>
    targetA = random(1, 10)
    targetB = random(1, 10)
    targetC = random(1, 10)\u200f
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד לא נוחש\u200f"}
    LoopStart --> InputValues["<p align='left'>קלט מספרים מהמשתמש:\u200f
    <code><b>
    userA\u200f
    userB\u200f
    userC\u200f
    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"בדיקה: <code><b>userA == targetA?</b></code>"}
    CheckA -- לא --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"בדיקה: <code><b>userB == targetB?</b>marble</code>"}
    CheckA -- כן --> CheckB
    CheckB -- לא --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"בדיקה: <code><b>userC == targetC?</b></code>"}
    CheckB -- כן --> CheckC
    CheckC -- לא --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"בדיקה: <code><b>message != "" ?</b></code>"}
    CheckC -- כן --> CheckMessage
    CheckMessage -- כן --> OutputWrong["הצגת הודעה: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- לא --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סיום"]
    LoopStart -- לא --> End
```
מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול המשתנים: `targetA`, `targetB`, `targetC` מוגרלים באקראי בטווח שבין 1 ל-10.
    LoopStart - תחילת הלולאה, הנמשכת כל עוד השחקן לא ניחש את כל המספרים.
    InputValues - בקשה מהמשתמש להזין שלושה מספרים: `userA`, `userB`, `userC`.
    InitializeMessage - אתחול המחרוזת הריקה `message`.
    CheckA - בדיקה האם המספר המוזן `userA` שווה למספר שהוגרל `targetA`.
    AppendA - הוספת 'A' למחרוזת `message`, אם `userA` אינו שווה ל-`targetA`.
    CheckB - בדיקה האם המספר המוזן `userB` שווה למספר שהוגרל `targetB`.
    AppendB - הוספת 'B' למחרוזת `message`, אם `userB` אינו שווה ל-`targetB`.
    CheckC - בדיקה האם המספר המוזן `userC` שווה למספר שהוגרל `targetC`.
    AppendC - הוספת 'C' למחרוזת `message`, אם `userC` אינו שווה ל-`targetC`.
    CheckMessage - בדיקה האם המחרוזת `message` ריקה.
    OutputWrong - הצגת ההודעה "WRONG ON" ותוכן המחרוזת `message`, אם המחרוזת אינה ריקה.
    OutputWin - הצגת ההודעה "YOU GOT IT!", אם המחרוזת `message` ריקה.
    End - סיום התוכנית.