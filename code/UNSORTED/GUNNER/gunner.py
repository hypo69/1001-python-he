GUNNER:
=================
דרגת קושי: 4
-----------------
המשחק "GUNNER" הוא סימולציה של ירי למטרה. השחקן מזין את זווית הירי ואת מהירותו, והמחשב מחשב האם הפגז יפגע במטרה.
לשחקן יש 5 ניסיונות ולאחר כל ניסיון הוא מקבל משוב:
 - "TOO LOW" - אם הפגז לא הגיע למטרה.
 - "TOO HIGH" - אם הפגז עבר מעל המטרה.
 - "BINGO" - אם הפגז פגע במטרה.

חוקי המשחק:
1. המחשב מגדיר מרחק אקראי למטרה בטווח שבין 100 ל-1000 רגל.
2. השחקן מזין את זווית הירי במעלות (מ-0 עד 90) ואת מהירות הירי ברגל לשנייה.
3. המחשב מחשב את טווח מעוף הפגז לפי הנוסחה: טווח = (מהירות^2 * sin(2 * זווית)) / 32.2
4. המחשב משווה את טווח המעוף למרחק עד למטרה ומדווח על התוצאה: "TOO LOW", "TOO HIGH" או "BINGO".
5. לשחקן יש 5 ניסיונות.
6. המשחק מסתיים לאחר 5 ניסיונות או אם השחקן פגע במטרה.
-----------------
אלגוריתם:
1. הגדר את מספר הניסיונות ל-5.
2. צור מרחק אקראי עד למטרה בטווח שבין 100 ל-1000.
3. התחל לולאה, עד שיסתיימו הניסיונות:
    3.1. בקש מהשחקן את זווית הירי ואת מהירות הירי.
    3.2. חשב את טווח מעוף הפגז לפי הנוסחה: טווח = (מהירות^2 * sin(2 * זווית ברדיאנים)) / 32.2.
    3.3. אם טווח המעוף שווה למרחק עד למטרה, פלט "BINGO" וסיים את המשחק.
    3.4. אם טווח המעוף קטן מהמרחק עד למטרה, פלט "TOO LOW".
    3.5. אם טווח המעוף גדול מהמרחק עד למטרה, פלט "TOO HIGH".
    3.6. הקטן את מספר הניסיונות הנותרים.
4. אם לאחר 5 ניסיונות המטרה לא נפגעה, פלט הודעה על הפסד.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    attemptsLeft = 5
    targetDistance = random(100, 1000)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока <code><b>attemptsLeft > 0</b></code>"}
    LoopStart -- Да --> InputAngleSpeed["Ввод угла (<code><b>angle</b></code>) и скорости (<code><b>speed</b></code>)"]
    InputAngleSpeed --> CalculateDistance["<p align='left'>Расчет дальности:
        <code><b>
        distance = (speed<sup>2</sup> * sin(2 * angle * pi / 180)) / 32.2
        </b></code></p>"]
    CalculateDistance --> CheckHit{"Проверка: <code><b>distance == targetDistance</b></code>?"}
    CheckHit -- Да --> OutputBingo["Вывод сообщения: <b>BINGO</b>"]
    OutputBingo --> End["Конец"]
    CheckHit -- Нет --> CheckLow{"Проверка: <code><b>distance < targetDistance</b></code>?"}
    CheckLow -- Да --> OutputLow["Вывод сообщения: <b>TOO LOW</b>"]
    OutputLow --> DecreaseAttempts["<code><b>attemptsLeft = attemptsLeft - 1</b></code>"]
    DecreaseAttempts --> LoopStart
    CheckLow -- Нет --> OutputHigh["Вывод сообщения: <b>TOO HIGH</b>"]
    OutputHigh --> DecreaseAttempts
    LoopStart -- Нет --> OutputLose["Вывод сообщения: <b>YOU LOSE</b>"]
    OutputLose --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: attemptsLeft (מספר הניסיונות) מוגדר ל-5, ו-targetDistance (מרחק עד למטרה) נוצר באופן אקראי מ-100 עד 1000.
    LoopStart - תחילת לולאה, שנמשכת כל עוד מספר הניסיונות הנותרים (attemptsLeft) גדול מ-0.
    InputAngleSpeed - בקשת קלט מהמשתמש עבור זווית הירי (angle) ומהירות (speed).
    CalculateDistance - חישוב טווח מעוף הפגז (distance) לפי הנוסחה.
    CheckHit - בדיקה האם המרחק המחושב (distance) שווה למרחק שהוגדר עד למטרה (targetDistance).
    OutputBingo - פלט הודעה "BINGO" אם הטווח שווה למרחק עד למטרה.
    End - סוף התוכנית.
    CheckLow - בדיקה האם טווח המעוף (distance) קטן מהמרחק עד למטרה (targetDistance).
    OutputLow - פלט הודעה "TOO LOW" אם הטווח קטן מהמטרה.
    OutputHigh - פלט הודעה "TOO HIGH" אם הטווח גדול מהמטרה.
    DecreaseAttempts - הקטנת מספר הניסיונות הנותרים ב-1.
    OutputLose - פלט הודעה "YOU LOSE" אם לאחר 5 ניסיונות המטרה לא נפגעה.
"""
import random
import math

# אתחול מספר הניסיונות
attemptsLeft = 5
# יצירת מרחק אקראי עד למטרה מ-100 עד 1000 רגל
targetDistance = random.randint(100, 1000)

# לולאת המשחק הראשית
while attemptsLeft > 0:
    # מבקשים קלט של זווית ומהירות הירי
    try:
        angle = float(input("Введите угол выстрела в градусах (0-90): "))
        speed = float(input("Введите скорость выстрела в футах в секунду: "))
    except ValueError:
        print("Пожалуйста, введите числовые значения.")
        continue

    # בדיקת קלט הזווית
    if not (0 <= angle <= 90):
        print("Угол должен быть в диапазоне от 0 до 90 градусов.")
        continue

    # חישוב טווח מעוף הפגז
    # המרת הזווית לרדיאנים
    angle_radians = math.radians(angle)
    distance = (speed**2 * math.sin(2 * angle_radians)) / 32.2

    # בדיקת פגיעה
    if abs(distance - targetDistance) < 0.01: # משתמשים בסטייה קטנה להשוואה
        print("BINGO!")
        break  # מסיימים את המשחק במקרה של פגיעה במטרה
    elif distance < targetDistance:
        print("TOO LOW") # מודיעים שהפגז לא הגיע
    else:
        print("TOO HIGH") # מודיעים שהפגז עבר מעל

    # מקטינים את מספר הניסיונות הנותרים
    attemptsLeft -= 1

# פלט הודעה על הפסד, אם הניסיונות אזלו
if attemptsLeft == 0:
    print("YOU LOSE")

"""
הסבר קוד:
1. **ייבוא מודולים**:
   - `import random`: מייבא את המודול `random`, שמשמש ליצירת מרחק אקראי עד למטרה.
   - `import math`: מייבא את המודול `math`, שמשמש לחישובים מתמטיים (סינוס והמרת מעלות לרדיאנים).

2. **אתחול משתנים**:
   - `attemptsLeft = 5`: מאתחל את המשתנה `attemptsLeft` למעקב אחר מספר הניסיונות הנותרים, החל מ-5.
   - `targetDistance = random.randint(100, 1000)`: יוצר מספר שלם אקראי בין 100 ל-1000, המייצג את המרחק עד למטרה, ושומר אותו ב-`targetDistance`.

3. **לולאת המשחק הראשית `while attemptsLeft > 0:`**:
   - הלולאה מתבצעת כל עוד לשחקן יש ניסיונות נותרים.

4. **קלט נתונים**:
   - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערך שאינו מספרי, תוצג הודעת שגיאה.
   - `angle = float(input("Введите угол выстрела в градусах (0-90): "))`: מבקש מהמשתמש את זווית הירי וממיר אותה למספר נקודה צפה.
   - `speed = float(input("Введите скорость выстрела в футах в секунду: "))`: מבקש מהמשתמש את מהירות הירי וממיר אותה למספר נקודה צפה.

5. **בדיקת קלט הזווית**:
   - `if not (0 <= angle <= 90):`: בודק האם הזווית שהוזנה נמצאת בטווח המותר (מ-0 עד 90 מעלות).
   - `print("Угол должен быть в диапазоне от 0 до 90 градусов.")`: פולט הודעת שגיאה אם הזווית הוזנה באופן שגוי.
   - `continue`: עובר לאיטרציה הבאה של הלולאה, מבלי לבצע את יתר הקוד באיטרציה הנוכחית.

6. **חישוב טווח מעוף**:
   - `angle_radians = math.radians(angle)`: ממיר את הזווית ממעלות לרדיאנים, מכיוון שהפונקציה `math.sin()` מצפה לקבל רדיאנים.
   - `distance = (speed**2 * math.sin(2 * angle_radians)) / 32.2`: מחשב את טווח מעוף הפגז לפי הנוסחה הנתונה.

7. **בדיקת פגיעה**:
    -   `if abs(distance - targetDistance) < 0.01:`: בודק האם הפגז פגע במטרה. נעשה שימוש ב-`abs()` לקבלת הערך המוחלט של ההפרש ובסטייה קטנה (0.01) להשוואת מספרי נקודה צפה עקב אי-דיוקים בייצוג.
    -   `print("BINGO!")`: פולט הודעה על הפגיעה.
    -   `break`: מסיים את הלולאה (המשחק) במקרה של פגיעה.
    -   `elif distance < targetDistance:`: בודק אם הפגז לא הגיע.
    -   `print("TOO LOW")`: פולט הודעה שהפגז לא הגיע.
    -   `else:`: אם הפגז עבר מעל.
    -   `print("TOO HIGH")`: פולט הודעה שהפגז עבר מעל.
8. **הקטנת מספר הניסיונות**:
    - `attemptsLeft -= 1`: מקטין את מספר הניסיונות הנותרים ב-1.

9. **פלט הודעה על הפסד**:
    -   `if attemptsLeft == 0:`: בודק האם הניסיונות אזלו.
    -   `print("YOU LOSE")`: פולט הודעה על הפסד.
"""