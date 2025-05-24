BOMBER:
=================
**רמת קושי: 5**
-----------------
המשחק "בומבר" הוא משחק חידה בו השחקן מנסה להטיל פצצה על מטרה הממוקמת במרחק שנוצר באופן אקראי. השחקן מזין את זווית ההטלה ואת מרחק ההטלה, והמחשב מחשב את מסלול הפצצה. מטרת המשחק היא לפגוע במטרה בצורה המדויקת ביותר האפשרית.

**כללי המשחק:**
1.  המחשב מייצר מרחק אקראי למטרה בטווח של 100 עד 1000.
2.  השחקן מזין את זווית הטלת הפצצה (במעלות) ואת מרחק הטלת הפצצה.
3.  המחשב מחשב את המרחק אליו תנחת הפצצה.
4.  אם מרחק נפילת הפצצה נמצא בטווח של 10 יחידות מהמרחק למטרה, השחקן מנצח.
5.  אם מרחק נפילת הפצצה אינו בטווח זה, השחקן מפסיד.
-----------------
**אלגוריתם:**
1.  יצירת מרחק אקראי למטרה בטווח של 100 עד 1000 והקצאתו למשתנה `targetDistance`.
2.  בקשת זווית הטלת פצצה במעלות (`angle`) ומרחק הטלה (`distance`) מהשחקן.
3.  המרת הזווית ממעלות לרדיאנים: `angleInRadians = angle * 3.14159 / 180`.
4.  חישוב מרחק נפילת הפצצה לפי הנוסחה: `dropDistance = distance * cos(angleInRadians)`.
5.  חישוב ההפרש בין מרחק נפילת הפצצה למרחק למטרה: `distanceDifference = abs(dropDistance - targetDistance)`.
6.  אם ההפרש בין המרחקים קטן או שווה ל-10, הצגת הודעת ניצחון.
7.  אחרת, הצגת הודעת הפסד.
8.  סוף המשחק.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeTargetDistance["אתחול: <code><b>targetDistance = random(100, 1000)</b></code>"]
    InitializeTargetDistance --> InputAngleDistance["קלט: <code><b>angle, distance</b></code>"]
    InputAngleDistance --> ConvertAngle["המרה: <code><b>angleInRadians = angle * PI / 180</b></code>"]
    ConvertAngle --> CalculateDropDistance["חישוב: <code><b>dropDistance = distance * cos(angleInRadians)</b></code>"]
    CalculateDropDistance --> CalculateDistanceDifference["חישוב: <code><b>distanceDifference = abs(dropDistance - targetDistance)</b></code>"]
    CalculateDistanceDifference --> CheckDistanceDifference{"בדיקה: <code><b>distanceDifference <= 10</b></code>"}
    CheckDistanceDifference -- כן --> OutputWin["פלט: <b>YOU HIT THE TARGET!</b>"]
    OutputWin --> End["סוף"]
    CheckDistanceDifference -- לא --> OutputLose["פלט: <b>YOU MISSED IT!</b>"]
    OutputLose --> End
```
**מקרא:**
    Start - התחלת התוכנית.
    InitializeTargetDistance - אתחול: יצירת מרחק אקראי למטרה (targetDistance) בין 100 ל-1000.
    InputAngleDistance - בקשת זווית הטלה (angle) ומרחק הטלה (distance) מהמשתמש.
    ConvertAngle - המרת הזווית ממעלות לרדיאנים (angleInRadians).
    CalculateDropDistance - חישוב מרחק נפילת הפצצה (dropDistance) על סמך הנתונים שהוזנו.
    CalculateDistanceDifference - חישוב ההפרש המוחלט בין מרחק נפילת הפצצה (dropDistance) למרחק למטרה (targetDistance).
    CheckDistanceDifference - בדיקה האם ההפרש בין המרחקים נמצא בטווח של 10 יחידות (distanceDifference <= 10).
    OutputWin - הצגת הודעת ניצחון אם ההפרש בטווח 10 יחידות.
    End - סוף התוכנית.
    OutputLose - הצגת הודעת הפסד אם ההפרש גדול מ-10 יחידות.