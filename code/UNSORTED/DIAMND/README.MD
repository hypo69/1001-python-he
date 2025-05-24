DIAMND:
=================
מורכבות: 7
-----------------
המשחק DIAMND הוא משחק מבוסס טקסט שבו השחקן מנסה לצייר מעוין העשוי מכוכביות על ידי הגדרת גובהו.
המשחק מבקש תחילה מהמשתמש להזין גובה אי-זוגי למעוין. לאחר מכן, אם המספר שהוזן הוא אי-זוגי, המשחק בונה מעוין מכוכביות, תוך שימוש ברווחים ליצירת הגיאומטריה הנכונה של הצורה. אם המספר שהוזן הוא זוגי או קטן מ-1, מוצגת הודעת שגיאה.
כללי המשחק:
1. השחקן מזין מספר אי-זוגי שקובע את גובה המעוין.
2. אם הוזן מספר זוגי או מספר קטן מ-1, המשחק מציג הודעת שגיאה.
3. אם הוזן מספר תקין (אי-זוגי וגדול מ-0), המשחק מציג על המסך מעוין העשוי מכוכביות בגובה שצוין.
-----------------
אלגוריתם:
1. בקש מהמשתמש להזין את גובה המעוין (H).
2. בדוק אם H זוגי או קטן מ-1. אם כן, הצג הודעת שגיאה וחזור לשלב 1.
3. אם H אי-זוגי וגדול מ-0, אז:
   3.1. הגדר את המשתנה `space` ל- H // 2 (חילוק שלם).
   3.2. הגדר את המשתנה `stars` ל- 1.
   3.3. התחל לולאה מ-1 עד H כולל:
      3.3.1. הצג `space` רווחים.
      3.3.2. הצג `stars` כוכביות.
      3.3.3. הצג מעבר שורה.
      3.3.4. אם מספר השורה הנוכחי קטן מ- H // 2 + 1:
          3.3.4.1. הקטן את `space` ב-1.
          3.3.4.2. הגדל את `stars` ב-2.
       3.3.5. אחרת:
          3.3.5.1. הגדל את `space` ב-1.
          3.3.5.2. הקטן את `stars` ב-2.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InputHeight["הזנת גובה מעוין (height)"]
    InputHeight --> CheckHeight{"בדיקה: <code><b>height</b></code> אי-זוגי ו- > 0?"}
    CheckHeight -- Нет --> OutputError["הצגת הודעה: <b>הזן מספר אי-זוגי גדול מ-0</b>"]
    OutputError --> InputHeight
    CheckHeight -- Да --> InitializeVars["<p align='left'>אתחול משתנים: 
    <code><b>
    spaces = height // 2 <br>
    stars = 1
    </b></code></p>"]
    InitializeVars --> LoopStart{"תחילת לולאה: מ-1 עד <code><b>height</b></code>"}
    LoopStart -- Да --> OutputSpaces["הצגת <code><b>spaces</b></code> רווחים"]
    OutputSpaces --> OutputStars["הצגת <code><b>stars</b></code> כוכביות"]
     OutputStars --> OutputNewline["הצגת מעבר שורה"]
     OutputNewline --> CheckRow{"בדיקה: האם השורה הנוכחית <= <code><b>height // 2 + 1</b></code>"}
     CheckRow -- Да --> DecreaseSpaceIncreaseStars["<code><b>spaces = spaces - 1<br> stars = stars + 2</b></code>"]
     DecreaseSpaceIncreaseStars --> LoopStart
     CheckRow -- Нет --> IncreaseSpaceDecreaseStars["<code><b>spaces = spaces + 1<br> stars = stars - 2</b></code>"]
     IncreaseSpaceDecreaseStars --> LoopStart
     LoopStart -- Нет --> End["סיום"]
```
מקרא:
    Start - התחלת התוכנית.
    InputHeight - בקשה מהמשתמש להזין את גובה המעוין ושמירת הערך במשתנה `height`.
    CheckHeight - בדיקה האם הגובה שהוזן הוא מספר אי-זוגי גדול מ-0.
    OutputError - הצגת הודעת שגיאה אם הגובה אינו תואם את התנאי.
    InitializeVars - אתחול משתנים: `spaces` (מספר הרווחים) מוגדר ל- `height // 2`, ו- `stars` (מספר הכוכביות) מוגדר ל- 1.
    LoopStart - תחילת לולאה החוזרת על עצמה `height` פעמים.
    OutputSpaces - הצגת `spaces` רווחים.
    OutputStars - הצגת `stars` כוכביות.
    OutputNewline - הצגת תו מעבר שורה.
    CheckRow - בדיקה האם השורה הנוכחית קטנה או שווה לאמצע המעוין (`height // 2 + 1`).
    DecreaseSpaceIncreaseStars - הקטנת מספר הרווחים `spaces` ב-1 והגדלת מספר הכוכביות `stars` ב-2.
    IncreaseSpaceDecreaseStars - הגדלת מספר הרווחים `spaces` ב-1 והקטנת מספר הכוכביות `stars` ב-2.
    End - סיום התוכנית.