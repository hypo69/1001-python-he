"""
STOCK:
=================
רמת קושי: 4
-----------------
המשחק "STOCK" מייצג סימולציה כלכלית פשוטה, שבה שחקן מנסה להרוויח כסף על ידי קנייה ומכירה של מניות במהלך מספר מוגדר של סבבים (ימים).
מחיר המניות משתנה באופן אקראי בכל סבב. מטרת המשחק היא למקסם את הרווח עד לסיום המשחק.

כללי המשחק:
1. השחקן מקבל סכום כסף התחלתי.
2. כל סבב מייצג יום, שבמהלכו מחיר המניה משתנה באופן אקראי.
3. השחקן יכול לקנות או למכור מניות בכל סבב, בתנאי שיש לו כסף או מניות.
4. השחקן צריך להזין את כמות המניות לקנייה או מכירה.
5. לאחר כל סבב, מוצגים מחיר המניה הנוכחי, מספר המניות הקיימות, כמות הכסף הקיימת והשווי הכולל.
6. המשחק נמשך במשך מספר מוגדר של סבבים.
7. מטרת המשחק היא לצבור כמה שיותר כסף עד לסיום המשחק.
-----------------
אלגוריתם:
1. לאתחל משתנים: מספר הימים, היום הנוכחי, כמות הכסף, מחיר המניה ומספר המניות.
2. להציג הודעת ברכה ומצב התחלתי.
3. להתחיל לולאה עבור כל יום:
   3.1 ליצור מחיר מניה אקראי חדש.
   3.2 להציג את היום הנוכחי, מחיר המניה, מספר המניות וסכום הכסף.
   3.3 לבקש מהשחקן לבצע פעולה (לקנות או למכור מניות).
   3.4 אם השחקן החליט לקנות מניות:
       3.4.1 לבקש את כמות המניות לקנייה.
       3.4.2 לבדוק אם יש מספיק כסף לקנייה. אם לא, להציג הודעת שגיאה.
       3.4.3 אם יש מספיק כסף, להקטין את כמות הכסף לפי עלות הקנייה, להגדיל את מספר המניות.
   3.5 אם השחקן החליט למכור מניות:
       3.5.1 לבקש את כמות המניות למכירה.
       3.5.2 לבדוק אם יש מספיק מניות למכירה. אם לא, להציג הודעת שגיאה.
       3.5.3 אם יש מספיק מניות, להגדיל את כמות הכסף לפי עלות המכירה, להקטין את מספר המניות.
   3.6 לעבור ליום הבא.
4. בתום כל הימים, להציג את המצב הסופי והודעה על סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfDays = 20<br>
    currentDay = 1<br>
    money = 1000<br>
    stockPrice = random(5, 50)<br>
    numberOfStocks = 0<br>
    </b></code></p>"]
    InitializeVariables --> GameLoopStart{"התחלת לולאה: כל עוד <code><b>currentDay <= numberOfDays</b></code>"}
    GameLoopStart -- כן --> UpdateStockPrice["<code><b>stockPrice = random(stockPrice * 0.9, stockPrice * 1.1)</b></code>"]
    UpdateStockPrice --> DisplayStatus["<p align='left'>הצג מצב:
    <code><b>
    currentDay, stockPrice,<br>
     numberOfStocks, money
    </b></code></p>"]
    DisplayStatus --> InputAction["קבלת פעולה: <code><b>action</b></code>"]
    InputAction --> CheckAction{"בדיקה: <code><b>action == 'buy'?</b></code>"}
    CheckAction -- כן --> InputBuyStocks["הכנס כמות לקנייה: <code><b>stocksToBuy</b></code>"]
    InputBuyStocks --> CheckMoney{"בדיקה: <code><b>money >= stocksToBuy * stockPrice?</b></code>"}
    CheckMoney -- כן --> BuyStocks["<code><b>money = money - stocksToBuy * stockPrice;<br>numberOfStocks = numberOfStocks + stocksToBuy</b></code>"]
    BuyStocks --> IncrementDay["<code><b>currentDay = currentDay + 1</b></code>"]
    IncrementDay --> GameLoopStart
    CheckMoney -- לא --> OutputNotEnoughMoney["הצג הודעה: <b>NOT ENOUGH MONEY</b>"]
    OutputNotEnoughMoney --> IncrementDay
    CheckAction -- לא --> CheckSell{"בדיקה: <code><b>action == 'sell'?</b></code>"}
    CheckSell -- כן --> InputSellStocks["הכנס כמות למכירה: <code><b>stocksToSell</b></code>"]
     InputSellStocks --> CheckStocks{"בדיקה: <code><b>numberOfStocks >= stocksToSell?</b></code>"}
    CheckStocks -- כן --> SellStocks["<code><b>money = money + stocksToSell * stockPrice;<br>numberOfStocks = numberOfStocks - stocksToSell</b></code>"]
    SellStocks --> IncrementDay
    CheckStocks -- לא --> OutputNotEnoughStocks["הצג הודעה: <b>NOT ENOUGH STOCKS</b>"]
    OutputNotEnoughStocks --> IncrementDay
   CheckSell -- לא -->  IncrementDay
   GameLoopStart -- לא --> End["סוף"]
```
**מקרא**:
    Start - תחילת התוכנית.
    InitializeVariables - אתחול משתנים: `numberOfDays` (מספר ימים) מוגדר ל-20, `currentDay` (יום נוכחי) מוגדר ל-1, `money` (כמות כסף) מוגדר ל-1000, `stockPrice` (מחיר מניה) נוצר באופן אקראי בטווח שבין 5 ל-50, ו-`numberOfStocks` (מספר מניות) מוגדר ל-0.
    GameLoopStart - תחילת לולאה, הנמשכת כל עוד היום הנוכחי `currentDay` קטן מ או שווה למספר הימים הכולל `numberOfDays`.
    UpdateStockPrice - עדכון מחיר המניה `stockPrice` באופן אקראי בטווח שבין 90% ל-110% מהמחיר הנוכחי.
    DisplayStatus - הצגת מצב המשחק הנוכחי: `currentDay`, `stockPrice`, `numberOfStocks`, ו-`money`.
    InputAction - בקשת פעולה מהמשתמש: קנייה ('buy') או מכירה ('sell') של מניות.
    CheckAction - בדיקה אם המשתמש בחר בפעולה "קנייה" ('buy').
    InputBuyStocks - בקשת כמות מניות לקנייה מהמשתמש `stocksToBuy`.
    CheckMoney - בדיקה אם למשתמש יש מספיק כסף `money` לקניית הכמות המבוקשת של מניות `stocksToBuy` לפי המחיר הנוכחי `stockPrice`.
    BuyStocks - קניית מניות: הפחתת כמות הכסף `money` לפי עלות הקנייה והגדלת מספר המניות `numberOfStocks`.
    IncrementDay - הגדלת היום הנוכחי `currentDay` ב-1.
    OutputNotEnoughMoney - הצגת הודעת שגיאה אם למשתמש אין מספיק כסף לקנייה.
    CheckSell - בדיקה אם המשתמש בחר בפעולה "מכירה" ('sell').
    InputSellStocks - בקשת כמות מניות למכירה מהמשתמש `stocksToSell`.
    CheckStocks - בדיקה אם למשתמש יש מספיק מניות `numberOfStocks` למכירת הכמות המבוקשת `stocksToSell`.
    SellStocks - מכירת מניות: הגדלת כמות הכסף `money` לפי עלות המכירה והפחתת מספר המניות `numberOfStocks`.
    OutputNotEnoughStocks - הצגת הודעת שגיאה אם למשתמש אין מספיק מניות למכירה.
    End - סוף התוכנית.
"""
import random

# אתחול פרמטרי המשחק
numberOfDays = 20 # מספר הימים הכולל
currentDay = 1 # היום הנוכחי
money = 1000 # סכום הכסף ההתחלתי
stockPrice = random.randint(5, 50) # מחיר מניה אקראי התחלתי
numberOfStocks = 0 # מספר המניות של השחקן

# הצגת הודעת ברכה ומצב התחלתי
print("ברוכים הבאים למשחק STOCK!")
print(f"מצב התחלתי: יום {currentDay}, מחיר מניה: {stockPrice}, מניות: {numberOfStocks}, כסף: {money}\n")

# לולאת המשחק הראשית
while currentDay <= numberOfDays:
    # משנים את מחיר המניה באופן אקראי
    stockPrice = round(random.uniform(stockPrice * 0.9, stockPrice * 1.1),2)

    # מציגים את המצב הנוכחי
    print(f"יום {currentDay}, מחיר מניה: {stockPrice}, מניות: {numberOfStocks}, כסף: {money}")

    # מבקשים פעולה מהמשתמש
    action = input("לקנות (buy) או למכור (sell) מניות? (או לחץ Enter למעבר ליום הבא): ").lower()

    # עיבוד פעולות המשתמש
    if action == 'buy':
        try:
            stocksToBuy = int(input("כמה מניות לקנות? "))
            if money >= stocksToBuy * stockPrice:
                money -= stocksToBuy * stockPrice
                numberOfStocks += stocksToBuy
                print("קנייה בוצעה")
            else:
                print("אין מספיק כסף לקנייה.")
        except ValueError:
             print("קלט לא תקין. אנא הזן מספר שלם.")
    elif action == 'sell':
        try:
             stocksToSell = int(input("כמה מניות למכור? "))
             if numberOfStocks >= stocksToSell:
                 money += stocksToSell * stockPrice
                 numberOfStocks -= stocksToSell
                 print("מכירה בוצעה")
             else:
                 print("אין מספיק מניות למכירה.")
        except ValueError:
            print("קלט לא תקין. אנא הזן מספר שלם.")
    else:
        print("עוברים ליום הבא.")

    currentDay += 1
    print("-----------------")
# הצגת מצב המשחק הסופי
print("המשחק הסתיים!")
print(f"מצב סופי: יום {currentDay - 1}, מחיר מניה: {stockPrice}, מניות: {numberOfStocks}, כסף: {money}")

"""
הסבר הקוד:

1. **אתחול משתנים**:
   - `numberOfDays`: מספר הימים הכולל של המשחק (20).
   - `currentDay`: היום הנוכחי (מתחיל מ-1).
   - `money`: סכום הכסף ההתחלתי של השחקן (1000).
   - `stockPrice`: מחיר המניה ההתחלתי, נוצר באופן אקראי בין 5 ל-50.
   - `numberOfStocks`: מספר המניות של השחקן (מתחיל מ-0).
2. **הצגת הודעת ברכה ומצב התחלתי**:
   - מוצגת הודעה על תחילת המשחק ומצב השחקן הנוכחי.
3. **לולאת המשחק הראשית `while currentDay <= numberOfDays:`**:
   - הלולאה נמשכת עד שיעברו כל הימים.
   - **שינוי מחיר המניה:**
     - `stockPrice = round(random.uniform(stockPrice * 0.9, stockPrice * 1.1),2)`: מחיר המניה משתנה באופן אקראי, בטווח שבין 90% ל-110% מהמחיר הנוכחי, ומעוגל ל-2 ספרות אחרי הנקודה העשרונית.
   - **הצגת המצב הנוכחי**:
     - הצגת היום הנוכחי, מחיר המניה, מספר המניות וכמות הכסף.
   - **קבלת פעולה מהשחקן**:
     - `action = input("לקנות (buy) או למכור (sell) מניות? (או לחץ Enter למעבר ליום הבא): ").lower()`: מתבקשת פעולה מהמשתמש (לקנות, למכור או לדלג יום), הפעולה מומרת לאותיות קטנות לנוחות.
    - **עיבוד פעולות השחקן**:
        - `if action == 'buy'`:
          -  מתבקשת כמות מניות לקנייה `stocksToBuy`.
          -  נבדק אם יש מספיק כסף לקנייה: `if money >= stocksToBuy * stockPrice:`.
          - אם יש מספיק, כמות הכסף פוחתת ומספר המניות גדל.
          - אחרת, מוצגת הודעה על מחסור בכסף.
        - `elif action == 'sell'`:
            -   מתבקשת כמות מניות למכירה `stocksToSell`.
            -   נבדק אם יש מספיק מניות למכירה: `if numberOfStocks >= stocksToSell:`.
            -   אם יש מספיק, כמות הכסף גדלה ומספר המניות פוחת.
            -   אחרת, מוצגת הודעה על מחסור במניות.
        - `else:`:
           - אם המשתמש הזין דבר אחר או לחץ enter, המשחק עובר ליום הבא.
     -  **הגדלת היום הנוכחי**:
        -  `currentDay += 1`: היום הנוכחי גדל ב-1.
        -   `print("-----------------")`: מוצג קו מפריד להפרדה ויזואלית בין הימים.

4. **הצגת מצב המשחק הסופי**:
   - לאחר סיום הלולאה, מוצגת הודעה על סיום המשחק ומצב השחקן הסופי.
"""