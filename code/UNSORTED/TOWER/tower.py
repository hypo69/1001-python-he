TOWER:
=================
רמת קושי: 4
-----------------
המשחק "מגדל" הוא משחק בו השחקן מנסה לבנות מגדל על ידי הזנת גובה כל קומה. המטרה היא לבנות מגדל גבוה ככל הניתן, אך קיימת הגבלה: אם גובה הקומה הנוכחית קטן מגובה הקומה הקודמת, המגדל קורס.

כללי המשחק:
1.  השחקן מתחיל עם גובה עבור הקומה הראשונה.
2.  בכל שלב עוקב, השחקן מזין את גובה הקומה הבאה.
3.  אם גובה הקומה הנוכחית גדול מגובה הקומה הקודמת, הקומה מתווספת למגדל, והמשחק ממשיך.
4.  אם גובה הקומה הנוכחית שווה או קטן מגובה הקומה הקודמת, המגדל קורס, והמשחק מסתיים.
5.  מטרת המשחק היא לבנות מגדל גבוה ככל הניתן, כלומר, עם מספר מרבי של קומות.
-----------------
אלגוריתם:
1.  אפס את הגובה ההתחלתי של המגדל ל-0.
2.  אפס את הגובה ההתחלתי של הקומה הקודמת ל-0.
3.  אפס את מספר הקומה ל-0.
4.  התחל לולאה:
    4.1 הגדל את מספר הקומה ב-1.
    4.2 בקש מהשחקן להזין את גובה הקומה הנוכחית.
    4.3 אם גובה הקומה הנוכחית גדול מגובה הקומה הקודמת:
        4.3.1 הגדר את גובה הקומה הקודמת להיות שווה לגובה הקומה הנוכחית.
    4.4 אחרת:
       4.4.1 הצג הודעה שהמגדל קרס.
       4.4.2 הצג הודעה על גובה המגדל, שהוא מספר הקומה פחות 1.
       4.4.3 סיים את המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code><b>towerHeight = 0</b></code><br><code><b>previousFloorHeight = 0</b></code><br><code><b>floorNumber = 0</b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה"}
    LoopStart --> IncreaseFloorNumber["<code><b>floorNumber = floorNumber + 1</b></code>"]
    IncreaseFloorNumber --> InputFloorHeight["קלט גובה קומה נוכחית: <code><b>currentFloorHeight</b></code>"]
    InputFloorHeight --> CheckFloorHeight{"בדיקה: <code><b>currentFloorHeight > previousFloorHeight</b></code>?"}
    CheckFloorHeight -- כן --> UpdatePreviousFloorHeight["<code><b>previousFloorHeight = currentFloorHeight</b></code>"]
    UpdatePreviousFloorHeight --> LoopStart
    CheckFloorHeight -- לא --> OutputGameOver["הצגת הודעה: <b>TOWER COLLAPSED!</b>"]
    OutputGameOver --> OutputTowerHeight["הצגת הודעה: <b>TOWER HEIGHT IS <code>{floorNumber - 1}</code></b>"]
    OutputTowerHeight --> End["סיום"]
```
מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: towerHeight (גובה המגדל) מאותחל ל-0, previousFloorHeight (גובה הקומה הקודמת) מאותחל ל-0, floorNumber (מספר הקומה) מאותחל ל-0.
    LoopStart - התחלת הלולאה, הנמשכת עד שהמגדל קורס.
    IncreaseFloorNumber - הגדלת מספר הקומה ב-1.
    InputFloorHeight - בקשת קלט מהמשתמש עבור גובה הקומה הנוכחית ושמירתו במשתנה currentFloorHeight.
    CheckFloorHeight - בדיקה האם גובה הקומה הנוכחית currentFloorHeight גדול מגובה הקומה הקודמת previousFloorHeight.
    UpdatePreviousFloorHeight - עדכון גובה הקומה הקודמת previousFloorHeight בערך גובה הקומה הנוכחית currentFloorHeight.
    OutputGameOver - הצגת הודעה המציינת שהמגדל קרס.
    OutputTowerHeight - הצגת הודעה על גובה המגדל (floorNumber - 1).
    End - סיום התוכנית.

```python
# אתחול משתנים
towerHeight = 0 # גובה המגדל הנוכחי
previousFloorHeight = 0 # גובה הקומה הקודמת
floorNumber = 0 # מספר הקומה הנוכחית

# התחלת לולאת המשחק הראשית
while True:
    # מגדילים את מספר הקומה
    floorNumber += 1

    try:
        # מבקשים את גובה הקומה הנוכחית
        currentFloorHeight = int(input(f"Введите высоту этажа {floorNumber}: "))
    except ValueError:
        print("אנא הכנס מספר שלם.")
        continue

    # בודקים האם גובה הקומה הנוכחית גדול מהקודמת
    if currentFloorHeight > previousFloorHeight:
        # אם גדול יותר, מעדכנים את גובה הקומה הקודמת
        previousFloorHeight = currentFloorHeight
    else:
        # אם הגובה הנוכחי קטן או שווה לקודם, המגדל קורס
        print("הַמִּגְדָּל קָרַס!")
        print(f"גובה המגדל: {floorNumber - 1}")
        break  # מסיימים את המשחק
```

הסבר הקוד:
1.  **אתחול משתנים:**
    -   `towerHeight = 0`: המשתנה `towerHeight` (גובה המגדל) מאותחל לאפס.
    -   `previousFloorHeight = 0`: המשתנה `previousFloorHeight` (גובה הקומה הקודמת) מאותחל לאפס.
    -   `floorNumber = 0`: המשתנה `floorNumber` (מספר הקומה הנוכחית) מאותחל לאפס.
2.  **לולאת המשחק הראשית `while True:`**:
    -   הלולאה נמשכת כל עוד המגדל לא קרס (כלומר, עד לפקודת `break`).
    -   `floorNumber += 1`: מגדיל את מספר הקומה ב-1 לפני כל איטרציה חדשה של הלולאה.
    -   **קלט נתונים**:
        -   `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך שאינו מספר שלם, תוצג הודעת שגיאה.
        -   `currentFloorHeight = int(input(f"Введите высоту этажа {floorNumber}: "))`: מבקש קלט מהמשתמש עבור גובה הקומה הנוכחית ושומר אותו ב-`currentFloorHeight`.
    -   **בדיקת תנאי קריסת המגדל**:
        -   `if currentFloorHeight > previousFloorHeight:`: בודק האם גובה הקומה הנוכחית גדול מגובה הקומה הקודמת.
        -   אם התנאי מתקיים, אז: `previousFloorHeight = currentFloorHeight` - גובה הקומה הקודמת מתעדכן לגובה הקומה הנוכחית.
        -   `else`: אם התנאי אינו מתקיים (גובה הקומה הנוכחית קטן או שווה לקודמת), אז:
            -   `print("הַמִּגְדָּל קָרַס!")`: מוצגת הודעה על קריסת המגדל.
            -   `print(f"גובה המגדל: {floorNumber - 1}")`: מוצגת הודעה על גובה המגדל הסופי.
            -   `break`: הלולאה מסתיימת.