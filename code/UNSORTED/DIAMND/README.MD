DIAMND:
=================
רמת קושי: 7
-----------------
המשחק DIAMND הוא משחק טקסטואלי בו השחקן מנסה לצייר מעוין מכוכביות על ידי קביעת גובהו.
המשחק תחילה מבקש מהמשתמש להזין גובה אי-זוגי למעוין. לאחר מכן, אם המספר שהוזן הוא אי-זוגי, המשחק בונה מעוין מכוכביות תוך שימוש ברווחים ליצירת הגיאומטריה הנכונה של הצורה. אם המספר שהוזן הוא זוגי או קטן מ-1, מוצגת הודעת שגיאה.
חוקי המשחק:
1. השחקן מזין מספר אי-זוגי, אשר קובע את גובה המעוין.
2. אם מוזן מספר זוגי או מספר קטן מ-1, המשחק מציג הודעת שגיאה.
3. אם מוזן מספר תקין (אי-זוגי וגדול מ-0), המשחק מציג על המסך מעוין מכוכביות בגובה שהוזן.
-----------------
אלגוריתם:
1. בקש מהמשתמש להזין את גובה המעוין (H).
2. בדוק אם H הוא זוגי או קטן מ-1. אם כן, הצג הודעת שגיאה ועבור לשלב 1.
3. אם H הוא אי-זוגי וגדול מ-0, אז:
   3.1. הגדר את המשתנה `space` להיות H // 2 (חילוק שלם).
   3.2. הגדר את המשתנה `stars` להיות 1.
   3.3. התחל לולאה מ-1 עד H כולל:
      3.3.1. הצג `space` רווחים.
      3.3.2. הצג `stars` כוכביות.
      3.3.3. הצג מעבר שורה.
      3.3.4. אם מספר השורה הנוכחית קטן מ-H // 2 + 1:
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
    Start["התחלה"] --> InputHeight["קלט גובה מעוין (height)"]
    InputHeight --> CheckHeight{"בדיקה: <code><b>height</b></code> אי-זוגי ו > 0?"}
    CheckHeight -- לא --> OutputError["הצג הודעה: <b>הזן מספר אי-זוגי גדול מ-0</b>"]
    OutputError --> InputHeight
    CheckHeight -- כן --> InitializeVars["<p align='left'>אתחול משתנים: 
    <code><b>
    spaces = height // 2 <br>
    stars = 1
    </b></code></p>"]
    InitializeVars --> LoopStart{"התחלת לולאה: מ-1 עד <code><b>height</b></code>"}
    LoopStart -- כן --> OutputSpaces["הצג <code><b>spaces</b></code> רווחים"]
    OutputSpaces --> OutputStars["הצג <code><b>stars</b></code> כוכביות"]
     OutputStars --> OutputNewline["הצג מעבר שורה"]
     OutputNewline --> CheckRow{"בדיקה: שורה נוכחית <= <code><b>height // 2 + 1</b></code>"}
     CheckRow -- כן --> DecreaseSpaceIncreaseStars["<code><b>spaces = spaces - 1<br> stars = stars + 2</b></code>"]
     DecreaseSpaceIncreaseStars --> LoopStart
     CheckRow -- לא --> IncreaseSpaceDecreaseStars["<code><b>spaces = spaces + 1<br> stars = stars - 2</b></code>"]
     IncreaseSpaceDecreaseStars --> LoopStart
     LoopStart -- לא --> End["סוף"]
```
מקרא:
    Start - תחילת התוכנית.
    InputHeight - בקשת קלט מהמשתמש עבור גובה המעוין ושמירת הערך במשתנה `height`.
    CheckHeight - בדיקה האם הגובה שהוזן הוא מספר אי-זוגי גדול מ-0.
    OutputError - הצגת הודעת שגיאה אם הגובה אינו עומד בתנאי.
    InitializeVars - אתחול משתנים: `spaces` (מספר הרווחים) מוגדר ל-`height // 2`, ו-`stars` (מספר הכוכביות) מוגדר ל-1.
    LoopStart - תחילת לולאה החוזרת `height` פעמים.
    OutputSpaces - הצגת `spaces` רווחים.
    OutputStars - הצגת `stars` כוכביות.
    OutputNewline - הצגת תו שורה חדשה.
    CheckRow - בדיקה האם השורה הנוכחית קטנה או שווה לאמצע המעוין (`height // 2 + 1`).
    DecreaseSpaceIncreaseStars - הקטנת מספר הרווחים `spaces` ב-1 והגדלת מספר הכוכביות `stars` ב-2.
    IncreaseSpaceDecreaseStars - הגדלת מספר הרווחים `spaces` ב-1 והקטנת מספר הכוכביות `stars` ב-2.
    End - סוף התוכנית.