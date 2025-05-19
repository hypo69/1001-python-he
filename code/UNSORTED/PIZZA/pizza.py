פִיצָה:
=================
דרגת מורכבות: 5
-----------------
המשחק 'פיצה' מדמה את תהליך הזמנת ומשלוח פיצה. השחקן נדרש לענות על סדרה של שאלות אודות כמות הפיצות, עלותן, גודל הטיפ וכדומה. בסיום, התוכנית מציגה את העלות הכוללת של ההזמנה, לרבות מס וטיפים.

כללי המשחק:
1. התוכנית מבקשת את כמות הפיצות.
2. לאחר מכן, מבקשת את עלותה של כל פיצה בנפרד.
3. בהמשך, מבקשת את שיעור הטיפ באחוזים.
4. מחושבת העלות הכוללת של הפיצות.
5. מחושב המס (5% מהעלות הכוללת).
6. מחושבת סכום הטיפים.
7. מוצגת העלות הכוללת של ההזמנה, לרבות מס וטיפים.
-----------------
אלגוריתם:
1. קלט את כמות הפיצות (QUANTITY).
2. בלולאה מ-1 עד QUANTITY:
   2.1. קלט את עלות הפיצה (COST).
   2.2. הגדל את העלות הכוללת של הפיצות (TOTAL) ב- COST.
3. קלט את אחוז הטיפים (TIP).
4. חשב את המס (TAX) כ-5% מ- TOTAL.
5. חשב את סכום הטיפים (TIP) כ- TIP% מ- TOTAL.
6. חשב את העלות הכוללת המלאה של ההזמנה (GRAND) כ- TOTAL + TAX + TIP.
7. פלט:
   7.1. העלות הכוללת של הפיצות (TOTAL).
   7.2. המס (TAX).
   7.3. סכום הטיפים (TIP).
   7.4. העלות הכוללת המלאה של ההזמנה (GRAND).
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InputQuantity["Ввод количества пицц: <code><b>quantity</b></code>"]
    InputQuantity --> InitializeTotal["<code><b>totalCost = 0</b></code>"]
    InitializeTotal --> LoopStart{"Начало цикла: для каждой пиццы"}
    LoopStart -- Да --> InputCost["Ввод стоимости пиццы: <code><b>pizzaCost</b></code>"]
    InputCost --> UpdateTotal["<code><b>totalCost = totalCost + pizzaCost</b></code>"]
    UpdateTotal --> LoopEnd{"Конец цикла: все пиццы обработаны"}
    LoopEnd -- Да --> InputTipPercent["Ввод процента чаевых: <code><b>tipPercent</b></code>"]
    LoopEnd -- Нет --> InputTipPercent
    InputTipPercent --> CalculateTax["<code><b>tax = totalCost * 0.05</b></code>"]
    CalculateTax --> CalculateTip["<code><b>tipAmount = totalCost * tipPercent / 100</b></code>"]
    CalculateTip --> CalculateGrandTotal["<code><b>grandTotal = totalCost + tax + tipAmount</b></code>"]
    CalculateGrandTotal --> OutputTotal["Вывод: <b>Общая стоимость пицц: <code>totalCost</code></b>"]
    OutputTotal --> OutputTax["Вывод: <b>Налог: <code>tax</code></b>"]
    OutputTax --> OutputTip["Вывод: <b>Чаевые: <code>tipAmount</code></b>"]
    OutputTip --> OutputGrandTotal["Вывод: <b>Полная стоимость заказа: <code>grandTotal</code></b>"]
    OutputGrandTotal --> End["Конец"]

```

מקרא:
    Start - תחילת התוכנית.
    InputQuantity - בקשה מהמשתמש לקלוט את כמות הפיצות ושמירת הערך במשתנה quantity.
    InitializeTotal - הגדרת ערך התחלתי של העלות הכוללת (totalCost) ל-0.
    LoopStart - תחילת לולאה לקליטת עלותה של כל פיצה בנפרד.
    InputCost - בקשה מהמשתמש לקלוט את עלות הפיצה הנוכחית ושמירת הערך במשתנה pizzaCost.
    UpdateTotal - הוספת עלות הפיצה הנוכחית לעלות הכוללת (totalCost).
    LoopEnd - סיום הלולאה, בודק האם כל הפיצות עובדו.
    InputTipPercent - בקשה מהמשתמש לקלוט את אחוז הטיפים ושמירת הערך במשתנה tipPercent.
    CalculateTax - חישוב המס כ-5% מהעלות הכוללת (totalCost).
    CalculateTip - חישוב סכום הטיפים על בסיס האחוז שהוזן מהעלות הכוללת (totalCost).
    CalculateGrandTotal - חישוב העלות הכוללת המלאה של ההזמנה על ידי סכימת העלות הכוללת, המס והטיפים.
    OutputTotal - פלט העלות הכוללת של הפיצות (totalCost).
    OutputTax - פלט סכום המס (tax).
    OutputTip - פלט סכום הטיפים (tipAmount).
    OutputGrandTotal - פלט העלות הכוללת המלאה של ההזמנה (grandTotal).
    End - סיום התוכנית.
"""


# בקשה מהמשתמש לקלוט את כמות הפיצות
while True:
    try:
        quantity = int(input("Сколько пицц вы хотите заказать? "))
        if quantity > 0:
            break  # יציאה מהלולאה אם הוזן ערך תקין
        else:
            print("Пожалуйста, введите положительное число.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

# אתחול העלות הכוללת
totalCost = 0

# לולאה לקליטת עלותה של כל פיצה
for i in range(quantity):
    while True:
        try:
           pizzaCost = float(input(f"Введите стоимость пиццы {i + 1}: "))
           if pizzaCost > 0:
                totalCost += pizzaCost # הוספת עלות הפיצה לסכום הכולל
                break  # יציאה מהלולאה אם הוזן ערך תקין
           else:
              print("Пожалуйста, введите положительную стоимость.")
        except ValueError:
           print("Пожалуйста, введите числовое значение.")


# בקשה לקלוט את אחוז הטיפים
while True:
    try:
        tipPercent = float(input("Какой процент чаевых вы хотите оставить? "))
        if 0 <= tipPercent <= 100:
            break  # יציאה מהלולאה אם האחוז בטווח שבין 0 ל-100
        else:
            print("Пожалуйста, введите процент от 0 до 100.")
    except ValueError:
        print("Пожалуйста, введите числовое значение.")

# חישוב המס (5%)
tax = totalCost * 0.05
# חישוב סכום הטיפים
tipAmount = totalCost * tipPercent / 100
# חישוב העלות הכוללת המלאה של ההזמנה
grandTotal = totalCost + tax + tipAmount

# הצגת התוצאות
print(f"Общая стоимость пицц: {totalCost:.2f}")
print(f"Налог: {tax:.2f}")
print(f"Чаевые: {tipAmount:.2f}")
print(f"Полная стоимость заказа: {grandTotal:.2f}")

"""
הסבר הקוד:
1.  **אתחול**:
    -   `totalCost = 0`: מאתחל את המשתנה `totalCost` לאחסון העלות הכוללת של כל הפיצות.
    -   לולאת `while True:`: משמשת לבדיקת קלט תקין מהמשתמש.
2.  **קליטת כמות הפיצות**:
    -   `quantity = int(input("Сколько пицц вы хотите заказать? "))`: מבקש מהמשתמש את כמות הפיצות ושומר אותה במשתנה `quantity`.
    -   בדיקה למספר חיובי: בודקים שכמות הפיצות גדולה מאפס, אחרת מבקשים להזין את הערך מחדש.
3.  **לולאה לקליטת עלותה של כל פיצה**:
    -   `for i in range(quantity):`: הלולאה מתבצעת `quantity` פעמים עבור כל פיצה.
    -   `pizzaCost = float(input(f"Введите стоимость пиццы {i + 1}: "))`: מבקש את עלות כל פיצה ושומר אותה במשתנה `pizzaCost`.
    -   `totalCost += pizzaCost`: מוסיף את עלות הפיצה הנוכחית לעלות הכוללת `totalCost`.
4. **קליטת אחוז הטיפים**:
    -   `tipPercent = float(input("Какой процент чаевых вы хотите оставить? "))`: מבקש מהמשתמש את אחוז הטיפים.
    - בודקים שאחוז הטיפים נמצא בטווח שבין 0 ל-100, אחרת מבקשים להזין את הערך מחדש.
5.  **חישובים**:
    -   `tax = totalCost * 0.05`: מחשב את המס כ-5% מהעלות הכוללת.
    -   `tipAmount = totalCost * tipPercent / 100`: מחשב את סכום הטיפים.
    -   `grandTotal = totalCost + tax + tipAmount`: מחשב את העלות הכוללת המלאה של ההזמנה, לרבות עלות הפיצות, המס והטיפים.
6.  **הצגת תוצאות**:
    -   `print(f"Общая стоимость пицц: {totalCost:.2f}")`: מציג את העלות הכוללת של הפיצות, מעוצבת לשני מקומות עשרוניים.
    -   `print(f"Налог: {tax:.2f}")`: מציג את סכום המס.
    -   `print(f"Чаевые: {tipAmount:.2f}")`: מציג את סכום הטיפים.
    -   `print(f"Полная стоимость заказа: {grandTotal:.2f}")`: מציג את העלות הכוללת המלאה של ההזמנה.
"""