CIVILW:
=================
דרגת מורכבות: 7
-----------------
המשחק "מלחמת אזרחים" מהווה סימולציית קרב בין שני צבאות: הקונפדרציה והאיחוד. השחקן מנהל את הקונפדרציה ומקבל החלטות הנוגעות למספר החיילים בכוחותיו ולסוגי התקפות (התקפה ישירה או תמרון עקיף). מטרת המשחק היא להכריע את צבא האיחוד, תוך צמצום אבדות השחקן. המשחק מביא בחשבון גורמים אקראיים המשפיעים על תוצאת הקרב, מה שהופך כל קרב לייחודי.

כללי המשחק:
1.  השחקן מנהל את צבא הקונפדרציה וחייב להכריע את צבא האיחוד.
2.  השחקן מזין את מספר החיילים להתקפה.
3.  השחקן בוחר את סוג ההתקפה: ישירה (1) או עקיפה (2).
4.  בהתאם לבחירת השחקן וגורמים אקראיים, מחושבת כמות האבדות עבור שני הצדדים.
5.  לאחר כל קרב, המשחק מציג את סדר הכוחות הנוכחי של שני הצבאות.
6.  המשחק מסתיים בניצחון אחד הצדדים כאשר סדר הכוחות של האויב הופך לשווה או קטן מ-0.
-----------------
אלגוריתם:
1.  להגדיר את סדר הכוחות ההתחלתי של צבא האיחוד (UnionForce) כשווה ל-1000 ושל צבא הקונפדרציה (ConfederateForce) כשווה ל-800.
2.  להתחיל לולאה "כל עוד סדר הכוחות של שני הצבאות גדול מ-0":
    2.1. לבקש מהשחקן את מספר החיילים שברצונו לשלוח להתקפה (AttackForce).
        2.1.1. אם AttackForce גדול מהכוחות הזמינים של הקונפדרציה (ConfederateForce), להציג הודעה "אין מספיק כוחות" ולחזור לתחילת שלב 2.1.
    2.2. לבקש מהשחקן את סוג ההתקפה: ישירה (1) או עקיפה (2) (AttackType).
    2.3. לחשב את אבדות הקונפדרציה (ConfederateLosses) באופן אקראי, על ידי הכפלת AttackForce במספר אקראי בין 0 ל-0.4 (עבור התקפה ישירה) או במספר אקראי בין 0 ל-0.2 (עבור תמרון עקיף).
        2.3.1. אם ConfederateLosses גדול מ-AttackForce, להגדיר את ConfederateLosses כשווה ל-AttackForce.
    2.4. לחשב את אבדות האיחוד (UnionLosses) באופן אקראי, על ידי הכפלת AttackForce במספר אקראי בין 0 ל-0.3.
        2.4.1. אם AttackType שווה ל-2, להגדיל את UnionLosses במספר אקראי בין 0 ל-100.
    2.5. לעדכן את סדר הכוחות של הצבאות:
        ConfederateForce = ConfederateForce - ConfederateLosses
        UnionForce = UnionForce - UnionLosses
    2.6. להציג את סדר הכוחות הנוכחי של שני הצבאות.
    2.7. לבחון את תנאי הניצחון:
        2.7.1. אם UnionForce קטן או שווה ל-0, להציג הודעה "הקונפדרציה ניצחה!" ולסיים את המשחק.
        2.7.2. אם ConfederateForce קטן או שווה ל-0, להציג הודעה "האיחוד ניצח!" ולסיים את המשחק.
3. סיום המשחק.
-----------------

"""
import random

# Начальная численность армий
# Initial army strength
unionForce = 1000  # Армия Союза # Union Army
confederateForce = 800  # Армия Конфедерации # Confederate Army

# Основной игровой цикл
# Main game loop
while unionForce > 0 and confederateForce > 0:
    # Запрос количества солдат для атаки
    # Request number of soldiers for attack
    while True:
         try:
            attackForce = int(input("Введите количество солдат для атаки (Конфедерация): "))
            if attackForce > confederateForce:
                print("Недостаточно сил! Попробуйте еще раз.")
            else:
                break
         except ValueError:
                print("Пожалуйста, введите целое число.")

    # Запрос типа атаки
    # Request attack type
    while True:
        try:
             attackType = int(input("Выберите тип атаки (1 - прямая, 2 - обходная): "))
             if attackType in [1, 2]:
                break
             else:
                 print("Неверный тип атаки, попробуйте еще раз")
        except ValueError:
            print("Пожалуйста, введите целое число 1 או 2.")

    # Расчет потерь Конфедерации
    # Calculate Confederate losses
    if attackType == 1:  # Прямая атака # Direct attack
        confederateLosses = int(attackForce * random.random() * 0.4)
    else:  # Обходной маневр # Flanking maneuver
        confederateLosses = int(attackForce * random.random() * 0.2)

    if confederateLosses > attackForce:
        confederateLosses = attackForce

    # Расчет потерь Союза
    # Calculate Union losses
    unionLosses = int(attackForce * random.random() * 0.3)
    if attackType == 2:
        unionLosses += random.randint(0, 100)

    # Обновление численности армий
    # Update army strength
    confederateForce -= confederateLosses
    unionForce -= unionLosses

    # Вывод текущей численности армий
    # Display current army strength
    print(f"Конфедерация: {confederateForce} солдат")
    print(f"Союз: {unionForce} солдат")

    # Проверка условий победы
    # Check victory conditions
    if unionForce <= 0:
        print("Конфедерация победила!")
    elif confederateForce <= 0:
        print("Союз победил!")

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים בעת חישוב האבדות.
2.  **אתחול סדר הכוחות של הצבאות**:
    -   `unionForce = 1000`: מגדיר את סדר הכוחות ההתחלתי של צבא האיחוד ל-1000.
    -   `confederateForce = 800`: מגדיר את סדר הכוחות ההתחלתי של צבא הקונפדרציה ל-800.
3.  **הלולאה הראשית `while unionForce > 0 and confederateForce > 0:`**:
    -   הלולאה נמשכת כל עוד סדר הכוחות של שני הצבאות גדול מ-0, כלומר, עד אשר יושג ניצחון של אחד הצדדים.
    -   **קלט נתונים**:
        -   הלולאה `while True: try: ... except ValueError:` מבטיחה קלט נתונים תקין. אם המשתמש מזין ערך שאינו מספר, התוכנית תציג שגיאה ותבקש לחזור על הקלט.
        -   `attackForce = int(input("Введите количество солдат для атаки (Конфедерация): "))`: מבקש מהשחקן את מספר החיילים להתקפה וממיר את הקלט למספר שלם.
        -   בדיקת מספר החיילים שהוזן
        -   `if attackForce > confederateForce: print("Недостаточно сил! Попробуйте еще раз.")`: בודק שמספר החיילים התוקפים אינו גדול מסדר הכוחות של צבא הקונפדרציה. אם אכן כך, מוצגת שגיאה והלולאה ממשיכה.
        -   `attackType = int(input("Выберите тип атаки (1 - прямая, 2 - обходная): "))`: מבקש מהשחקן את סוג ההתקפה וממיר את הקלט למספר שלם.
        -   בדיקת סוג ההתקפה שהוזן
        -   `if attackType in [1, 2]: break`: בודק שסוג ההתקפה הוא 1 או 2. אם אכן כך, יציאה מהלולאה. אחרת, מציג שגיאה ומבקש לחזור על הקלט.
    -   **חישוב אבדות הקונפדרציה**:
        -   `if attackType == 1: ... else:`: בהתאם לסוג ההתקפה, מחושבת כמות האבדות.
        -   `confederateLosses = int(attackForce * random.random() * 0.4)`: עבור התקפה ישירה, אבדות הקונפדרציה הן מספר אקראי בין 0 ל-40% מהכוח התוקף.
        -   `confederateLosses = int(attackForce * random.random() * 0.2)`: עבור תמרון עקיף, אבדות הקונפדרציה הן מספר אקראי בין 0 ל-20% מהכוח התוקף.
        -   `if confederateLosses > attackForce: confederateLosses = attackForce`: מבטיח שהאבדות לא יהיו גדולות ממספר התוקפים.
    -   **חישוב אבדות האיחוד**:
        -   `unionLosses = int(attackForce * random.random() * 0.3)`: אבדות האיחוד הן מספר אקראי בין 0 ל-30% מהכוח התוקף.
        -   `if attackType == 2: unionLosses += random.randint(0, 100)`: במהלך תמרון עקיף, מספר אקראי בין 0 ל-100 מתווסף לאבדות האיחוד.
    -   **עדכון סדר הכוחות של הצבאות**:
        -   `confederateForce -= confederateLosses`: מקטין את סדר הכוחות של צבא הקונפדרציה בכמות האבדות.
        -   `unionForce -= unionLosses`: מקטין את סדר הכוחות של צבא האיחוד בכמות האבדות.
    -   **הצגת סדר הכוחות הנוכחי של הצבאות**:
        -   `print(f"Конфедерация: {confederateForce} солдат")`: מציג את סדר הכוחות הנוכחי של צבא הקונפדרציה.
        -   `print(f"Союз: {unionForce} солдат")`: מציג את סדר הכוחות הנוכחי של צבא האיחוד.
    -   **בחינת תנאי הניצחון**:
        -   `if unionForce <= 0: print("Конфедерация победила!")`: אם סדר הכוחות של צבא האיחוד הפך לקטן או שווה ל-0, הקונפדרציה מוכרזת כמנצחת.
        -   `elif confederateForce <= 0: print("Союз победил!")`: אם סדר הכוחות של צבא הקונפדרציה הפך לקטן או שווה ל-0, האיחוד מוכרז כמנצח.
"""