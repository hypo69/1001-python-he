רַקֶטָה:
=================
דרגת קושי: 7
-----------------
המשחק "רקטָה" הוא משחק שבו השחקן מנווט רקטה, במטרה להגיע לגובה נתון, תוך שימוש בדלק. מטרת המשחק היא להגיע לגובה 100 לפני שייגמר הדלק. השחקן יכול לבחור כמה דלק לצרוך בכל צעד. בהתאם לבחירה, הרקטה עולה לגובה אקראי.

כללי המשחק:
1. השחקן מתחיל עם 100 יחידות דלק.
2. על השחקן להגיע לגובה 100.
3. בכל צעד, השחקן מזין את כמות הדלק שהוא רוצה לצרוך לצורך עלייה.
4. עליית הרקטה תלויה בכמות הדלק שנצרכה והיא מספר אקראי בטווח מ-0 ועד 2 * כמות הדלק.
5. המשחק מסתיים כאשר השחקן מגיע לגובה 100 או כאשר נגמר הדלק.
-----------------
אלגוריתם:
1. הגדר את גובה הרקטה ההתחלתי ל-0.
2. הגדר את כמות הדלק ההתחלתית ל-100.
3. התחל בלולאת "כל עוד גובה הרקטה אינו שווה ל-100 וכמות הדלק גדולה מ-0":
   3.1 הצג את גובה הרקטה הנוכחי ואת יתרת הדלק.
   3.2 בקש מהשחקן את כמות הדלק לשריפה.
   3.3 אם כמות הדלק שהוזנה גדולה מהכמות הקיימת, הצג את ההודעה "אין לכם מספיק דלק".
   3.4 אחרת:
     3.4.1 הפחת את כמות הדלק בערך שהוזן.
     3.4.2 חשב את עליית הרקטה כמספר שלם אקראי מ-0 ועד 2 * ערך הדלק שהוזן.
     3.4.3 הגדל את גובה הרקטה הנוכחי בערך העלייה שחושב.
4. אם גובה הרקטה שווה ל-100, הצג את ההודעה "ברכות! הגעתם לגובה 100!".
5. אחרת, אם כמות הדלק שווה ל-0, הצג את ההודעה "מיציתם את הדלק. לא הגעתם לגובה 100!".
6. סוף המשחק.
-----------------
דיאגרמת זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    rocketHeight = 0
    fuel = 100
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: 
    כל עוד <code><b>rocketHeight < 100</b></code> וגם <code><b>fuel > 0</b></code>"}
    LoopStart -- Да --> OutputStatus["פלט: 
    <code><b>
    גובה: {rocketHeight}
    דלק: {fuel}
    </b></code>"]
    OutputStatus --> InputFuel["בקשת קלט דלק: <code><b>fuelToBurn</b></code>"]
    InputFuel --> CheckFuel["בדיקה: <code><b>fuelToBurn > fuel?</b></code>"]
    CheckFuel -- Да --> OutputError["פלט: <b>אין לכם מספיק דלק!</b>"]
    OutputError --> LoopStart
    CheckFuel -- Нет --> BurnFuel["<code><b>fuel = fuel - fuelToBurn</b></code>"]
    BurnFuel --> CalculateRise["חישוב עלייה:
    <code><b>
    rise = random(0, 2 * fuelToBurn)
    </b></code>"]
    CalculateRise --> IncreaseHeight["<code><b>rocketHeight = rocketHeight + rise</b></code>"]
    IncreaseHeight --> CheckWin{"בדיקה: <code><b>rocketHeight >= 100</b></code>"}
    CheckWin -- Да --> OutputWin["פלט: <b>ברכות! הגעתם לגובה 100!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- Нет --> LoopStart
     LoopStart -- Нет --> CheckFuelEmpty{"בדיקה: <code><b>fuel == 0</b></code>"}
    CheckFuelEmpty -- Да --> OutputLose["פלט: <b>מיציתם את הדלק. לא הגעתם לגובה 100!</b>"]
    OutputLose --> End
     CheckFuelEmpty -- Нет --> End

```
**מקרא:**
    Start - תחילת המשחק.
    InitializeVariables - אתחול משתנים: `rocketHeight` (גובה הרקטה) מוגדר ל-0, ו-`fuel` (כמות הדלק) מוגדר ל-100.
    LoopStart - תחילת לולאה, הנמשכת כל עוד גובה הרקטה קטן מ-100 וכמות הדלק גדולה מ-0.
    OutputStatus - פלט של גובה הרקטה הנוכחי ויתרת הדלק.
    InputFuel - בקשה מהמשתמש את כמות הדלק לשריפה.
    CheckFuel - בדיקה האם כמות הדלק המבוקשת גדולה מהכמות הזמינה.
    OutputError - פלט הודעת שגיאה אם כמות הדלק המבוקשת גדולה מהכמות הזמינה.
    BurnFuel - הפחתת כמות הדלק בערך שהוזן.
    CalculateRise - חישוב עליית הרקטה כמספר אקראי מ-0 ועד 2 * כמות הדלק שהוזנה.
    IncreaseHeight - הגדלת גובה הרקטה בערך העלייה שחושב.
    CheckWin - בדיקה האם הרקטה הגיעה לגובה 100.
    OutputWin - פלט הודעה על ניצחון אם הרקטה הגיעה לגובה 100.
    End - סוף המשחק.
    CheckFuelEmpty - בדיקה האם נגמר הדלק.
    OutputLose - פלט הודעה על הפסד אם נגמר הדלק.
"""
import random

# Initialize rocket height and fuel amount
rocketHeight = 0
fuel = 100

# Main game loop
while rocketHeight < 100 and fuel > 0:
    print(f"גובה: {rocketHeight}, דלק: {fuel}")
    try:
        fuelToBurn = int(input("כמה דלק לשרוף?: "))
    except ValueError:
        print("אנא הזינו מספר שלם.")
        continue
    if fuelToBurn > fuel:
        print("אין לכם מספיק דלק!")
    else:
        fuel -= fuelToBurn
        rise = random.randint(0, 2 * fuelToBurn)
        rocketHeight += rise

# Check game end conditions and print message
if rocketHeight >= 100:
    print("ברכות! הגעתם לגובה 100!")
else:
    print("מיציתם את הדלק. לא הגעתם לגובה 100!")

"""
הסבר על הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים.
2.  **אתחול משתנים**:
    -   `rocketHeight = 0`: מאתחל את המשתנה `rocketHeight` לאחסון גובה הרקטה הנוכחי.
    -   `fuel = 100`: מאתחל את המשתנה `fuel` לאחסון כמות הדלק הנוכחית.
3.  **לולאת המשחק הראשית `while rocketHeight < 100 and fuel > 0:`**:
    -   הלולאה נמשכת כל עוד הרקטה לא הגיעה לגובה 100 או שלא נגמר הדלק.
    -   `print(f"גובה: {rocketHeight}, דלק: {fuel}")`: מציג את הגובה הנוכחי ואת כמות הדלק.
    -   **קלט נתונים**:
        - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך שאינו מספר שלם, תוצג הודעת שגיאה.
        -   `fuelToBurn = int(input("כמה דלק לשרוף?: "))`: מבקש מהמשתמש את כמות הדלק לשריפה.
    -   **בדיקת זמינות דלק**:
        -   `if fuelToBurn > fuel:`: בודק האם כמות הדלק לשריפה מספיקה.
        -   `print("אין לכם מספיק דלק!")`: מציג הודעת שגיאה אם אין מספיק דלק.
    -   **שריפת דלק וחישוב עלייה**:
        -   `else:`: אם יש מספיק דלק, מבוצע הבלוק הבא.
        -   `fuel -= fuelToBurn`: מפחית את כמות הדלק בכמות שנצרכה.
        -   `rise = random.randint(0, 2 * fuelToBurn)`: מחשב עלייה אקראית בטווח מ-0 ועד 2 * `fuelToBurn`.
        -   `rocketHeight += rise`: מגדיל את גובה הרקטה בערך העלייה.
4.  **בדיקת תנאי סיום המשחק והצגת הודעה**:
    -   `if rocketHeight >= 100:`: בודק האם הרקטה הגיעה לגובה 100.
    -   `print("ברכות! הגעתם לגובה 100!")`: מציג הודעה על ניצחון אם הרקטה הגיעה לגובה 100.
    -   `else:`: אם הרקטה לא הגיעה לגובה 100.
    -   `print("מיציתם את הדלק. לא הגעתם לגובה 100!")`: מציג הודעה על הפסד אם נגמר הדלק.