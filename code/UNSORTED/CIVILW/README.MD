CIVILW:
=================
רמת קושי: 7
-----------------
המשחק "מלחמת האזרחים" (Гражданская война) הוא סימולציה של קרב בין שני צבאות: הקונפדרציה (Конфедерацией) והאיחוד (Союзом). השחקן שולט בצבא הקונפדרציה (Конфедерацией) ומקבל החלטות לגבי גודל כוחותיו וסוגי ההתקפות (התקפה ישירה או תמרון עקיף). מטרת המשחק היא להביס את צבא האיחוד (Союза), תוך מזעור האבדות של השחקן. המשחק לוקח בחשבון גורמים אקראיים המשפיעים על תוצאת הקרב, מה שהופך כל קרב לייחודי.

כללי המשחק:
1.  השחקן שולט בצבא הקונפדרציה ועליו להביס את צבא האיחוד.
2.  השחקן מזין את מספר החיילים להתקפה.
3.  השחקן בוחר את סוג ההתקפה: ישירה (1) או עקיפה (2).
4.  בהתאם לבחירת השחקן ולגורמים אקראיים, מחושבות האבדות לשני הצדדים.
5.  לאחר כל קרב, המשחק מציג את גודל הכוחות הנוכחי של שני הצבאות.
6.  המשחק מסתיים בניצחון של אחד הצדדים, כאשר גודל כוחות האויב הופך להיות שווה או קטן מ-0.
-----------------
אלגוריתם:
1. הגדר את גודל הכוחות ההתחלתי של צבא האיחוד (UnionForce) ל-1000 ושל צבא הקונפדרציה (ConfederateForce) ל-800.
2. התחל לולאה "כל עוד גודל שני הצבאות גדול מ-0":
    2.1. בקש מהשחקן את מספר החיילים שברצונו לשלוח להתקפה (AttackForce).
        2.1.1. אם AttackForce גדול מגודל הכוחות הקיימים של הקונפדרציה (ConfederateForce), הצג הודעה "אין מספיק כוחות" וחזור לתחילת שלב 2.1.
    2.2. בקש מהשחקן את סוג ההתקפה: ישירה (1) או עקיפה (2) (AttackType).
    2.3. חשב את אבדות הקונפדרציה (ConfederateLosses) באופן אקראי, על ידי הכפלת AttackForce במספר אקראי מ-0 עד 0.4 (עבור התקפה ישירה) או במספר אקראי מ-0 עד 0.2 (עבור תמרון עקיף).
        2.3.1. אם ConfederateLosses גדול מ-AttackForce, הגדר את ConfederateLosses לשווה ל-AttackForce.
    2.4. חשב את אבדות האיחוד (UnionLosses) באופן אקראי, על ידי הכפלת AttackForce במספר אקראי מ-0 עד 0.3.
        2.4.1. אם AttackType שווה ל-2, הגדל את UnionLosses במספר אקראי מ-0 עד 100.
    2.5. עדכן את גודל הצבאות:
        ConfederateForce = ConfederateForce - ConfederateLosses
        UnionForce = UnionForce - UnionLosses
    2.6. הצג את גודל הכוחות הנוכחי של שני הצבאות.
    2.7. בדוק תנאי ניצחון:
        2.7.1. אם UnionForce קטן או שווה ל-0, הצג הודעה "הקונפדרציה ניצחה!" וסיים את המשחק.
        2.7.2. אם ConfederateForce קטן או שווה ל-0, הצג הודעה "האיחוד ניצח!" וסיים את המשחק.
3. סוף המשחק.
-----------------
דיאגרמת זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeForces["<p align='left'>אתחול משתנים:<br><code><b>unionForce = 1000</b></code><br><code><b>confederateForce = 800</b></code></p>"]
    InitializeForces --> LoopStart{"תחילת לולאה: כל עוד שני הצבאות > 0"}
    LoopStart -- Да --> InputAttackForce["<p align='left'>הזנת כמות תוקפים:<br><code><b>attackForce</b></code></p>"]
    InputAttackForce --> CheckForce{"בדיקה:<br><code><b>attackForce > confederateForce?</b></code>"}
    CheckForce -- Да --> OutputInsufficient["הצגת הודעה: <b>אין מספיק כוחות</b>"]
    OutputInsufficient --> InputAttackForce
    CheckForce -- Нет --> InputAttackType["<p align='left'>הזנת סוג התקפה:<br><b>1 - ישירה</b>, <b>2 - עקיפה</b><br><code><b>attackType</b></code></p>"]
    InputAttackType --> CalculateConfederateLosses["<p align='left'>חישוב אבדות הקונפדרציה:<br><code><b>confederateLosses = attackForce * random(0, 0.4)</b></code><br>(או <code><b>random(0, 0.2)</b></code> עבור התקפה עקיפה)<br>אם <code><b>confederateLosses > attackForce</b></code>, אז <code><b>confederateLosses = attackForce</b></code></p>"]
    CalculateConfederateLosses --> CalculateUnionLosses["<p align='left'>חישוב אבדות האיחוד:<br><code><b>unionLosses = attackForce * random(0, 0.3)</b></code><br>אם <code><b>attackType = 2</b></code>, אז <code><b>unionLosses += random(0, 100)</b></code></p>"]
    CalculateUnionLosses --> UpdateForces["<p align='left'>עדכון גודל הצבאות:<br><code><b>confederateForce -= confederateLosses</b></code><br><code><b>unionForce -= unionLosses</b></code></p>"]
    UpdateForces --> OutputForces["<p align='left'>הצגת גודל הצבאות:<br><code><b>confederateForce</b></code>, <code><b>unionForce</b></code></p>"]
    OutputForces --> CheckUnionWin{"בדיקה:<br><code><b>unionForce <= 0?</b></code>"}
    CheckUnionWin -- Да --> OutputConfederateWin["הצגת הודעה: <b>הקונפדרציה ניצחה!</b>"]
    OutputConfederateWin --> End["סוף"]
    CheckUnionWin -- Нет --> CheckConfederateWin{"בדיקה:<br><code><b>confederateForce <= 0?</b></code>"}
     CheckConfederateWin -- Да --> OutputUnionWin["הצגת הודעה: <b>האיחוד ניצח!</b>"]
    OutputUnionWin --> End
    CheckConfederateWin -- Нет --> LoopStart
    LoopStart -- Нет --> End
```
    
מקרא:
    Start - תחילת התוכנית.
    InitializeForces - אתחול גודל הכוחות ההתחלתי של צבא האיחוד (unionForce = 1000) ושל הקונפדרציה (confederateForce = 800).
    LoopStart - תחילת הלולאה, הנמשכת כל עוד גודל שני הצבאות גדול מ-0.
    InputAttackForce - בקשת מספר החיילים להתקפה (attackForce) מהשחקן.
    CheckForce - בדיקה האם לקונפדרציה יש מספיק כוחות להתקפה (attackForce > confederateForce).
    OutputInsufficient - הצגת הודעה "אין מספיק כוחות", אם כמות התוקפים גדולה מהכוחות הזמינים.
    InputAttackType - בקשת בחירת סוג ההתקפה מהשחקן: ישירה (1) או עקיפה (2).
    CalculateConfederateLosses - חישוב אבדות הקונפדרציה (confederateLosses) על בסיס attackForce וסוג ההתקפה, תוך התחשבות בגורם אקראי. אם האבדות עולות על attackForce, האבדות מוגדרות להיות שוות ל-attackForce.
    CalculateUnionLosses - חישוב אבדות האיחוד (unionLosses) על בסיס attackForce וסוג ההתקפה, תוך התחשבות בגורם אקראי. בתמרון עקיף, אבדות האיחוד גדלות בנוסף במספר אקראי.
    UpdateForces - עדכון גודל כוחות שני הצבאות לאחר הקרב.
    OutputForces - הצגת גודל הכוחות הנוכחי של צבאות הקונפדרציה והאיחוד.
    CheckUnionWin - בדיקה האם הקונפדרציה ניצחה (גודל צבא האיחוד <= 0).
    OutputConfederateWin - הצגת הודעה על ניצחון הקונפדרציה.
    CheckConfederateWin - בדיקה האם האיחוד ניצח (גודל צבא הקונפדרציה <= 0).
    OutputUnionWin - הצגת הודעה על ניצחון האיחוד.
    End - סוף התוכנית.