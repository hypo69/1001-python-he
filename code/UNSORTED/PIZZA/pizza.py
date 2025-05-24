PIZZA:
=================
רמת קושי: 5
-----------------
המשחק "פיצה" מדמה את התהליך של הזמנה ואספקת פיצה. על השחקן לענות על סדרת שאלות בנוגע לכמות הפיצות, עלותן, שיעור דמי השירות וכדומה. בסיום, התוכנית מציגה את העלות הכוללת של ההזמנה, לרבות מס ודמי שירות.

כללי המשחק:
1. התוכנית מבקשת את כמות הפיצות.
2. לאחר מכן מבקשת את עלות כל פיצה.
3. בהמשך מבקשת את שיעור דמי השירות באחוזים.
4. מחושבת העלות הכוללת של הפיצות.
5. מחושב המס (5% מהעלות הכוללת).
6. מחושב סכום דמי השירות.
7. מוצגת העלות הכוללת של ההזמנה, לרבות מס ודמי שירות.
-----------------
אלגוריתם:
1. קלט את כמות הפיצות (QUANTITY).
2. בלולאה מ-1 עד QUANTITY:
   2.1. קלט את עלות הפיצה (COST).
   2.2. הגדל את העלות הכוללת של הפיצות (TOTAL) ב-COST.
3. קלט את אחוז דמי השירות (TIP).
4. חשב את המס (TAX) כ-5% מ-TOTAL.
5. חשב את סכום דמי השירות (TIP) כ-TIP% מ-TOTAL.
6. חשב את העלות המלאה של ההזמנה (GRAND) כ-TOTAL + TAX + TIP.
7. הצג:
   7.1. את העלות הכוללת של הפיצות (TOTAL).
   7.2. את המס (TAX).
   7.3. את סכום דמי השירות (TIP).
   7.4. את העלות המלאה של ההזמנה (GRAND).
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InputQuantity["קלט כמות פיצות: <code><b>quantity</b></code>"]
    InputQuantity --> InitializeTotal["<code><b>totalCost = 0</b></code>"]
    InitializeTotal --> LoopStart{"תחילת לולאה: עבור כל פיצה"}
    LoopStart -- כן --> InputCost["קלט עלות פיצה: <code><b>pizzaCost</b></code>"]
    InputCost --> UpdateTotal["<code><b>totalCost = totalCost + pizzaCost</b></code>"]
    UpdateTotal --> LoopEnd{"סוף לולאה: כל הפיצות עובדו"}
    LoopEnd -- כן --> InputTipPercent["קלט אחוז דמי שירות: <code><b>tipPercent</b></code>"]
    LoopEnd -- לא --> InputTipPercent
    InputTipPercent --> CalculateTax["<code><b>tax = totalCost * 0.05</b></code>"]
    CalculateTax --> CalculateTip["<code><b>tipAmount = totalCost * tipPercent / 100</b></code>"]
    CalculateTip --> CalculateGrandTotal["<code><b>grandTotal = totalCost + tax + tipAmount</b></code>"]
    CalculateGrandTotal --> OutputTotal["הצגה: <b>עלות פיצות כוללת: <code>totalCost</code></b>"]
    OutputTotal --> OutputTax["הצגה: <b>מס: <code>tax</code></b>"]
    OutputTax --> OutputTip["הצגה: <b>דמי שירות: <code>tipAmount</code></b>"]
    OutputTip --> OutputGrandTotal["הצגה: <b>עלות הזמנה מלאה: <code>grandTotal</code></b>"]
    OutputGrandTotal --> End["סיום"]

```

מקרא:
    Start - התחלת התוכנית.
    InputQuantity - בקשת כמות הפיצות מהמשתמש ושמירת הערך במשתנה quantity.
    InitializeTotal - הגדרת הערך ההתחלתי של העלות הכוללת (totalCost) ל-0.
    LoopStart - תחילת לולאה לקלט עלות כל פיצה.
    InputCost - בקשת עלות הפיצה הנוכחית מהמשתמש ושמירת הערך במשתנה pizzaCost.
    UpdateTotal - הוספת עלות הפיצה הנוכחית לעלות הכוללת (totalCost).
    LoopEnd - סוף הלולאה, בודק האם כל הפיצות עובדו.
    InputTipPercent - בקשת אחוז דמי השירות מהמשתמש ושמירת הערך במשתנה tipPercent.
    CalculateTax - חישוב המס כ-5% מהעלות הכוללת (totalCost).
    CalculateTip - חישוב סכום דמי השירות על בסיס האחוז שהוזן מהעלות הכוללת (totalCost).
    CalculateGrandTotal - חישוב עלות ההזמנה המלאה על ידי סיכום העלות הכוללת, המס ודמי השירות.
    OutputTotal - הצגת עלות הפיצות הכוללת (totalCost).
    OutputTax - הצגת סכום המס (tax).
    OutputTip - הצגת סכום דמי השירות (tipAmount).
    OutputGrandTotal - הצגת עלות ההזמנה המלאה (grandTotal).
    End - סיום התוכנית.
"""


# מבקש מהמשתמש את כמות הפיצות
while True:
    try:
        quantity = int(input("כמה פיצות תרצה להזמין? "))
        if quantity > 0:
            break  # יוצא מהלולאה אם הוזן ערך תקין
        else:
            print("אנא הזן מספר חיובי.")
    except ValueError:
        print("אנא הזן מספר שלם.")

# מאתחל את העלות הכוללת
totalCost = 0

# לולאה לקלט עלות כל פיצה
for i in range(quantity):
    while True:
        try:
           pizzaCost = float(input(f"הזן את עלות פיצה {i + 1}: "))
           if pizzaCost > 0:
                totalCost += pizzaCost # מוסיף את עלות הפיצה לסכום הכולל
                break  # יוצא מהלולאה אם הוזן ערך תקין
           else:
              print("אנא הזן עלות חיובית.")
        except ValueError:
           print("אנא הזן ערך מספרי.")


# מבקש את אחוז דמי השירות
while True:
    try:
        tipPercent = float(input("איזה אחוז דמי שירות תרצה להשאיר? "))
        if 0 <= tipPercent <= 100:
            break  # יוצא מהלולאה אם האחוז בטווח 0 עד 100
        else:
            print("אנא הזן אחוז בין 0 ל-100.")
    except ValueError:
        print("אנא הזן ערך מספרי.")

# מחשב את המס (5%)
tax = totalCost * 0.05
# מחשב את סכום דמי השירות
tipAmount = totalCost * tipPercent / 100
# מחשב את העלות המלאה של ההזמנה
grandTotal = totalCost + tax + tipAmount

# מציג את התוצאות
print(f"עלות פיצות כוללת: {totalCost:.2f}")
print(f"מס: {tax:.2f}")
print(f"דמי שירות: {tipAmount:.2f}")
print(f"עלות הזמנה מלאה: {grandTotal:.2f}")

"""
הסבר קוד:
1.  **אתחול**:
    -   `totalCost = 0`: מאתחל את המשתנה `totalCost` לאחסון העלות הכוללת של כל הפיצות.
    -   הלולאה `while True:`: משמשת לווידוא קלט תקין מהמשתמש.
2.  **קלט כמות פיצות**:
    -   `quantity = int(input("כמה פיצות תרצה להזמין? "))`: מבקש מהמשתמש את כמות הפיצות ושומר אותה במשתנה `quantity`.
    -   בדיקה למספר חיובי: בודק שכמות הפיצות גדולה מאפס, אחרת מבקש להזין את הערך מחדש.
3.  **לולאה לקלט עלות כל פיצה**:
    -   `for i in range(quantity):`: הלולאה מתבצעת `quantity` פעמים עבור כל פיצה.
    -   `pizzaCost = float(input(f"הזן את עלות פיצה {i + 1}: "))`: מבקש את עלות כל פיצה ושומר אותה במשתנה `pizzaCost`.
    -   `totalCost += pizzaCost`: מוסיף את עלות הפיצה הנוכחית לעלות הכוללת `totalCost`.
4. **קלט אחוז דמי שירות**:
    -   `tipPercent = float(input("איזה אחוז דמי שירות תרצה להשאיר? "))`: מבקש מהמשתמש את אחוז דמי השירות.
    - בודק שאחוז דמי השירות בטווח 0 עד 100, אחרת מבקש להזין את הערך מחדש.
5.  **חישובים**:
    -   `tax = totalCost * 0.05`: מחשב את המס כ-5% מהעלות הכוללת.
    -   `tipAmount = totalCost * tipPercent / 100`: מחשב את סכום דמי השירות.
    -   `grandTotal = totalCost + tax + tipAmount`: מחשב את העלות המלאה של ההזמנה, כולל עלות הפיצות, המס ודמי השירות.
6.  **הצגת תוצאות**:
    -   `print(f"עלות פיצות כוללת: {totalCost:.2f}")`: מציג את העלות הכוללת של הפיצות, מפורמטת לשתי ספרות אחרי הנקודה העשרונית.
    -   `print(f"מס: {tax:.2f}")`: מציג את סכום המס.
    -   `print(f"דמי שירות: {tipAmount:.2f}")`: מציג את סכום דמי השירות.
    -   `print(f"עלות הזמנה מלאה: {grandTotal:.2f}")`: מציג את העלות המלאה של ההזמנה.
"""