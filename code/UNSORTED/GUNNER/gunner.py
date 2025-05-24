**GUNNER:**
=================
**רמת מורכבות: 4**
-----------------
המשחק "GUNNER" הוא סימולציית ירי אל מטרה. השחקן מזין את זווית הירי ואת מהירותו, והמחשב מחשב האם הפגז יפגע במטרה.
לשחקן יש 5 ניסיונות ולאחר כל ניסיון הוא מקבל רמז:
- "TOO LOW" – אם הפגז לא הגיע למטרה.
- "TOO HIGH" – אם הפגז עבר מעבר למטרה.
- "BINGO" – אם הפגז פגע במטרה.

**כללי המשחק:**
1. המחשב קובע מרחק אקראי למטרה בטווח של 100 עד 1000 רגל.
2. השחקן מזין את זווית הירי במעלות (בין 0 ל-90) ואת מהירות הירי ברגל לשנייה.
3. המחשב מחשב את טווח מעוף הפגז באמצעות הנוסחה: טווח = (מהירות^2 * סינוס(2 * זווית)) / 32.2
4. המחשב משווה את טווח המעוף עם המרחק למטרה ומודיע על התוצאה: "TOO LOW", "TOO HIGH" או "BINGO".
5. לשחקן יש 5 ניסיונות.
6. המשחק מסתיים לאחר 5 ניסיונות או אם השחקן פגע במטרה.
-----------------
**אלגוריתם:**
1. קבע את מספר הניסיונות ל-5.
2. צור באופן אקראי מרחק למטרה בטווח בין 100 ל-1000.
3. התחל לולאה כל עוד נותרו ניסיונות:
    3.1. בקש מהשחקן את זווית הירי ואת מהירות הירי.
    3.2. חשב את טווח מעוף הפגז באמצעות הנוסחה: טווח = (מהירות^2 * סינוס(2 * זווית ברדיאנים)) / 32.2.
    3.3. אם טווח המעוף שווה למרחק אל המטרה, הצג "BINGO" וסיים את המשחק.
    3.4. אם טווח המעוף קטן מהמרחק אל המטרה, הצג "TOO LOW".
    3.5. אם טווח המעוף גדול מהמרחק אל המטרה, הצג "TOO HIGH".
    3.6. הקטן את מספר הניסיונות הנותרים.
4. אם לאחר 5 ניסיונות המטרה לא נפגעה, הצג הודעה על הפסד.
5. סוף המשחק.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>איתחול משתנים:
    <code><b>
    attemptsLeft = 5
    targetDistance = random(100, 1000)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד <code><b>attemptsLeft > 0</b></code>"}
    LoopStart -- כן --> InputAngleSpeed["קלט זווית (<code><b>angle</b></code>) ומהירות (<code><b>speed</b></code>)"]
    InputAngleSpeed --> CalculateDistance["<p align='left'>חישוב טווח:
        <code><b>
        distance = (speed<sup>2</sup> * sin(2 * angle * pi / 180)) / 32.2
        </b></code></p>"]
    CalculateDistance --> CheckHit{"בדיקה: <code><b>distance == targetDistance</b></code>?"}
    CheckHit -- כן --> OutputBingo["פלט הודעה: <b>BINGO</b>"]
    OutputBingo --> End["סוף"]
    CheckHit -- לא --> CheckLow{"בדיקה: <code><b>distance < targetDistance</b></code>?"}
    CheckLow -- כן --> OutputLow["פלט הודעה: <b>TOO LOW</b>"]
    OutputLow --> DecreaseAttempts["<code><b>attemptsLeft = attemptsLeft - 1</b></code>"]
    DecreaseAttempts --> LoopStart
    CheckLow -- לא --> OutputHigh["פלט הודעה: <b>TOO HIGH</b>"]
    OutputHigh --> DecreaseAttempts
    LoopStart -- לא --> OutputLose["פלט הודעה: <b>YOU LOSE</b>"]
    OutputLose --> End
```

**מקרא:**
    Start - תחילת התוכנית.
    InitializeVariables - איתחול משתנים: attemptsLeft (מספר הניסיונות) נקבע ל-5, ו- targetDistance (המרחק אל המטרה) נוצר באופן אקראי בין 100 ל-1000.
    LoopStart - תחילת לולאה, הנמשכת כל עוד מספר הניסיונות הנותרים (attemptsLeft) גדול מ-0.
    InputAngleSpeed - בקשת קלט מהמשתמש עבור זווית הירי (angle) ומהירותו (speed).
    CalculateDistance - חישוב טווח מעוף הפגז (distance) באמצעות הנוסחה.
    CheckHit - בדיקה האם המרחק המחושב (distance) שווה למרחק הקבוע אל המטרה (targetDistance).
    OutputBingo - פלט ההודעה "BINGO" אם הטווח שווה למרחק אל המטרה.
    End - סוף התוכנית.
    CheckLow - בדיקה האם טווח המעוף (distance) קטן מהמרחק אל המטרה (targetDistance).
    OutputLow - פלט ההודעה "TOO LOW" אם הטווח קטן מהמטרה.
    OutputHigh - פלט ההודעה "TOO HIGH" אם הטווח גדול מהמטרה.
    DecreaseAttempts - הקטנת מספר הניסיונות הנותרים ב-1.
    OutputLose - פלט ההודעה "YOU LOSE" אם לאחר 5 ניסיונות המטרה לא נפגעה.
"""
import random
import math

# איתחול מספר הניסיונות
attemptsLeft = 5
# יצירת מרחק אקראי אל המטרה בין 100 ל-1000 רגל
targetDistance = random.randint(100, 1000)

# לולאת המשחק הראשית
while attemptsLeft > 0:
    # בקשת קלט עבור זווית הירי והמהירות
    try:
        angle = float(input("Введите угол выстрела в градусах (0-90): "))
        speed = float(input("Введите скорость выстрела в футах в секунду: "))
    except ValueError:
        print("Пожалуйста, введите числовые значения.")
        continue

    # בדיקת תקינות קלט הזווית
    if not (0 <= angle <= 90):
        print("Угол должен быть в диапазоне от 0 до 90 градусов.")
        continue

    # חישוב טווח מעוף הפגז
    # המרת הזווית לרדיאנים
    angle_radians = math.radians(angle)
    distance = (speed**2 * math.sin(2 * angle_radians)) / 32.2

    # בדיקת פגיעה
    if abs(distance - targetDistance) < 0.01: # שימוש בשגיאה קטנה להשוואה
        print("BINGO!")
        break  # סיום המשחק עם פגיעה במטרה
    elif distance < targetDistance:
        print("TOO LOW") # הודעה שהפגז לא הגיע
    else:
        print("TOO HIGH") # הודעה שהפגז עבר

    # הקטנת מספר הניסיונות הנותרים
    attemptsLeft -= 1

# הצגת הודעת הפסד אם הניסיונות אזלו
if attemptsLeft == 0:
    print("YOU LOSE")

"""
**הסבר הקוד:**
1.  **ייבוא מודולים**:
    *   `import random`: מייבא את מודול `random`, המשמש ליצירת מרחק אקראי אל המטרה.
    *   `import math`: מייבא את מודול `math`, המשמש לחישובים מתמטיים (סינוס והמרת מעלות לרדיאנים).

2.  **איתחול משתנים**:
    *   `attemptsLeft = 5`: מאתחל את המשתנה `attemptsLeft` למעקב אחר מספר הניסיונות הנותרים, החל מ-5.
    *   `targetDistance = random.randint(100, 1000)`: יוצר מספר שלם אקראי בין 100 ל-1000, המייצג את המרחק אל המטרה, ושומר אותו ב-`targetDistance`.

3.  **לולאת המשחק הראשית `while attemptsLeft > 0:`**:
    *   הלולאה מתבצעת כל עוד לשחקן יש ניסיונות נותרים.

4.  **קלט נתונים**:
    *   `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך לא מספרי, תוצג הודעת שגיאה.
    *   `angle = float(input("Введите угол выстрела в градусах (0-90): "))`: מבקש מהמשתמש את זווית הירי וממיר אותה למספר עשרוני.
    *   `speed = float(input("Введите скорость выстрела в футах в секунду: "))`: מבקש מהמשתמש את מהירות הירי וממיר אותה למספר עשרוני.

5.  **בדיקת תקינות קלט הזווית**:
    *   `if not (0 <= angle <= 90):`: בודק האם הזווית שהוזנה נמצאת בטווח המותר (0 עד 90 מעלות).
    *   `print("Угол должен быть в диапазоне от 0 до 90 градусов.")`: מציג הודעת שגיאה אם הזווית הוזנה באופן שגוי.
    *   `continue`: עובר לאיטרציה הבאה של הלולאה, מבלי לבצע את שאר הקוד באיטרציה הנוכחית.

6.  **חישוב טווח המעוף**:
    *   `angle_radians = math.radians(angle)`: ממיר את הזווית ממעלות לרדיאנים, שכן פונקציית `math.sin()` מצפה לקלט ברדיאנים.
    *   `distance = (speed**2 * math.sin(2 * angle_radians)) / 32.2`: מחשב את טווח מעוף הפגז לפי הנוסחה הנתונה.

7.  **בדיקת פגיעה**:
    *   `if abs(distance - targetDistance) < 0.01:`: בודק האם הפגז פגע במטרה. משתמש ב-`abs()` לקבלת ההפרש המוחלט ובשגיאה קטנה (0.01) לצורך השוואת מספרים עשרוניים עקב אי-דיוקי ייצוג.
    *   `print("BINGO!")`: מציג הודעה על פגיעה.
    *   `break`: מסיים את הלולאה (ואת המשחק) עם הפגיעה.
    *   `elif distance < targetDistance:`: בודק אם הפגז לא הגיע למטרה.
    *   `print("TOO LOW")`: מציג הודעה שהפגז לא הגיע.
    *   `else:`: אם הפגז עבר מעבר למטרה.
    *   `print("TOO HIGH")`: מציג הודעה שהפגז עבר.
8.  **הקטנת מספר הניסיונות**:
    *   `attemptsLeft -= 1`: מקטין את מספר הניסיונות הנותרים ב-1.

9.  **הצגת הודעה על הפסד**:
    *   `if attemptsLeft == 0:`: בודק האם הניסיונות אזלו.
    *   `print("YOU LOSE")`: מציג הודעה על הפסד.
"""