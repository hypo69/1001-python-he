STOCK:
=================
רמת קושי: 4
-----------------
המשחק "STOCK" מהווה סימולציה כלכלית פשוטה, בה השחקן מנסה להרוויח כסף על ידי קנייה ומכירה של מניות במהלך מספר מוגדר של סבבים (ימים).
מחיר המניה משתנה באופן אקראי בכל סבב. מטרת המשחק היא למקסם את הרווח עד סוף המשחק.

כללי המשחק:
1. לשחקן מוענק סכום כסף התחלתי.
2. כל סבב מייצג יום, שבמהלכו מחיר המניה מתנודד אקראית.
3. השחקן יכול לקנות או למכור מניות בכל סבב, בתנאי שיש לו כסף או מניות בהתאמה.
4. השחקן נדרש להזין את כמות המניות לקנייה או למכירה.
5. לאחר כל סבב, מוצגים מחיר המניה הנוכחי, כמות המניות שברשות השחקן, הכסף שברשותו, והשווי הכולל.
6. המשחק ממשיך למשך מספר מוגדר מראש של סבבים.
7. מטרת המשחק היא לצבור כמה שיותר כסף עד סוף המשחק.
-----------------
אלגוריתם:
1. אתחול משתנים: מספר הימים, היום הנוכחי, סכום הכסף, מחיר המניה, וכמות המניות.
2. הצגת הודעת פתיחה ומצב התחלתי.
3. הפעלת לולאה עבור כל יום:
    3.1 יצירת מחיר מניה אקראי חדש.
    3.2 הצגת היום הנוכחי, מחיר המניה, כמות המניות, וסכום הכסף.
    3.3 בקשת פעולה מהשחקן (קנייה או מכירה של מניות).
    3.4 אם השחקן בחר לקנות מניות:
        3.4.1 בקשת כמות מניות לקנייה.
        3.4.2 בדיקה האם יש מספיק כסף לקנייה. אם לא, הצגת הודעת שגיאה.
        3.4.3 אם יש מספיק כסף, הקטנת סכום הכסף בעלות הקנייה, והגדלת כמות המניות.
    3.5 אם השחקן בחר למכור מניות:
        3.5.1 בקשת כמות מניות למכירה.
        3.5.2 בדיקה האם יש מספיק מניות למכירה. אם לא, הצגת הודעת שגיאה.
        3.5.3 אם יש מספיק מניות, הגדלת סכום הכסף בעלות המכירה, והקטנת כמות המניות.
    3.6 מעבר ליום הבא.
4. בתום כל הימים, הצגת המצב הסופי והודעה על סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br>
    <code><b>
    numberOfDays = 20<br>
    currentDay = 1<br>
    money = 1000<br>
    stockPrice = random(5, 50)<br>
    numberOfStocks = 0<br>
    </b></code></p>"]
    InitializeVariables --> GameLoopStart{"תחילת הלולאה: כל עוד <code><b>currentDay <= numberOfDays</b></code>"}
    GameLoopStart -- כן --> UpdateStockPrice["<code><b>stockPrice = random(stockPrice * 0.9, stockPrice * 1.1)</b></code>"]
    UpdateStockPrice --> DisplayStatus["<p align='left'>הצגת מצב: <br>
    <code><b>
    currentDay, stockPrice,<br>
     numberOfStocks, money
    </b></code></p>"]
    DisplayStatus --> InputAction["קלט פעולה: <code><b>action</b></code>"]
    InputAction --> CheckAction{"בדיקה: <code><b>action == 'buy'?</b></code>"}
    CheckAction -- כן --> InputBuyStocks["קלט כמות לקנייה: <code><b>stocksToBuy</b></code>"]
    InputBuyStocks --> CheckMoney{"בדיקה: <code><b>money >= stocksToBuy * stockPrice?</b></code>"}
    CheckMoney -- כן --> BuyStocks["<code><b>money = money - stocksToBuy * stockPrice;<br>numberOfStocks = numberOfStocks + stocksToBuy</b></code>"]
    BuyStocks --> IncrementDay["<code><b>currentDay = currentDay + 1</b></code>"]
    IncrementDay --> GameLoopStart
    CheckMoney -- לא --> OutputNotEnoughMoney["הצגת הודעה: <b>NOT ENOUGH MONEY</b>"]
    OutputNotEnoughMoney --> IncrementDay
    CheckAction -- לא --> CheckSell{"בדיקה: <code><b>action == 'sell'?</b></code>"}
    CheckSell -- כן --> InputSellStocks["קלט כמות למכירה: <code><b>stocksToSell</b></code>"]
     InputSellStocks --> CheckStocks{"בדיקה: <code><b>numberOfStocks >= stocksToSell?</b></code>"}
    CheckStocks -- כן --> SellStocks["<code><b>money = money + stocksToSell * stockPrice;<br>numberOfStocks = numberOfStocks - stocksToSell</b></code>"]
    SellStocks --> IncrementDay
    CheckStocks -- לא --> OutputNotEnoughStocks["הצגת הודעה: <b>NOT ENOUGH STOCKS</b>"]
    OutputNotEnoughStocks --> IncrementDay
   CheckSell -- לא -->  IncrementDay
   GameLoopStart -- לא --> End["סוף"]
```
**מקרא**:
    התחלה - תחילת התוכנית.
    InitializeVariables - אתחול משתנים: `numberOfDays` (מספר הימים) מוגדר ל-20, `currentDay` (היום הנוכחי) מוגדר ל-1, `money` (סכום הכסף) מוגדר ל-1000, `stockPrice` (מחיר המניה) נוצר באופן אקראי בטווח שבין 5 ל-50, ו-`numberOfStocks` (כמות המניות) מוגדר ל-0.
    GameLoopStart - תחילת הלולאה, הנמשכת כל עוד היום הנוכחי `currentDay` קטן או שווה למספר הימים הכולל `numberOfDays`.
    UpdateStockPrice - עדכון מחיר המניה `stockPrice` באופן אקראי בטווח שבין 90% ל-110% מהמחיר הנוכחי.
    DisplayStatus - הצגת המצב הנוכחי של המשחק: `currentDay`, `stockPrice`, `numberOfStocks`, ו-`money`.
    InputAction - בקשת פעולה מהמשתמש: קנייה ('buy') או מכירה ('sell') של מניות.
    CheckAction - בדיקה האם המשתמש בחר בפעולת "קנייה" ('buy').
    InputBuyStocks - בקשת כמות מניות לקנייה `stocksToBuy` מהמשתמש.
    CheckMoney - בדיקה האם למשתמש יש מספיק כסף `money` לקניית הכמות המבוקשת של מניות `stocksToBuy` במחיר הנוכחי `stockPrice`.
    BuyStocks - קניית מניות: הקטנת סכום הכסף `money` בעלות הקנייה והגדלת כמות המניות `numberOfStocks`.
     IncrementDay - הגדלת היום הנוכחי `currentDay` ב-1.
    OutputNotEnoughMoney - הצגת הודעת שגיאה, אם למשתמש אין מספיק כסף לקנייה.
    CheckSell - בדיקה האם המשתמש בחר בפעולת "מכירה" ('sell').
    InputSellStocks - בקשת כמות מניות למכירה `stocksToSell` מהמשתמש.
    CheckStocks - בדיקה האם למשתמש יש מספיק מניות `numberOfStocks` למכירת הכמות המבוקשת `stocksToSell`.
    SellStocks - מכירת מניות: הגדלת סכום הכסף `money` בעלות המכירה והקטנת כמות המניות `numberOfStocks`.
    OutputNotEnoughStocks - הצגת הודעת שגיאה, אם למשתמש אין מספיק מניות למכירה.
    סוף - סיום התוכנית.
```
import random

# אתחול פרמטרי המשחק
numberOfDays = 20 # מספר הימים
currentDay = 1 # היום הנוכחי
money = 1000 # סכום הכסף
stockPrice = random.randint(5, 50) # מחיר מניה אקראי
numberOfStocks = 0 # כמות המניות

# הצגת הודעת פתיחה ומצב התחלתי
print("ברוכים הבאים למשחק STOCK!")
print(f"מצב התחלתי: יום {currentDay}, מחיר מניה: {stockPrice}, מניות: {numberOfStocks}, כסף: {money}\n")

# לולאת המשחק הראשית
while currentDay <= numberOfDays:
    # משנים את מחיר המניה באופן אקראי
    stockPrice = round(random.uniform(stockPrice * 0.9, stockPrice * 1.1),2)

    # מציגים את המצב הנוכחי
    print(f"יום {currentDay}, מחיר מניה: {stockPrice}, מניות: {numberOfStocks}, כסף: {money}")

    # מבקשים פעולה מהמשתמש
    action = input("קנות (buy) או למכור (sell) מניות? (או לחצו Enter למעבר ליום הבא): ").lower()
    
    # טיפול בפעולות המשתמש
    if action == 'buy':
        try:
            stocksToBuy = int(input("כמה מניות לקנות? "))
            if money >= stocksToBuy * stockPrice:
                money -= stocksToBuy * stockPrice
                numberOfStocks += stocksToBuy
                print("הקנייה בוצעה בהצלחה")
            else:
                print("אין מספיק כסף לקנייה.")
        except ValueError:
             print("קלט לא תקין. אנא הזינו מספר שלם.")
    elif action == 'sell':
        try:
             stocksToSell = int(input("כמה מניות למכור? "))
             if numberOfStocks >= stocksToSell:
                 money += stocksToSell * stockPrice
                 numberOfStocks -= stocksToSell
                 print("המכירה בוצעה בהצלחה")
             else:
                 print("אין מספיק מניות למכירה.")
        except ValueError:
            print("קלט לא תקין. אנא הזינו מספר שלם.")
    else:
        print("עוברים ליום הבא.")

    currentDay += 1
    print("-----------------")
# הצגת המצב הסופי של המשחק
print("המשחק הסתיים!")
print(f"מצב סופי: יום {currentDay - 1}, מחיר מניה: {stockPrice}, מניות: {numberOfStocks}, כסף: {money}")

"""
הסבר הקוד:

1. **אתחול משתנים**:
   - `numberOfDays`: מספר הימים הכולל של המשחק (20).
   - `currentDay`: היום הנוכחי (מתחיל מ-1).
   - `money`: סכום הכסף ההתחלתי שברשות השחקן (1000).
   - `stockPrice`: מחיר המניה ההתחלתי, נוצר באופן אקראי מ-5 עד 50.
   - `numberOfStocks`: כמות המניות שברשות השחקן (מתחילה מ-0).
2. **הצגת הודעת פתיחה ומצב התחלתי**:
   - מוצגת הודעה על תחילת המשחק והמצב הנוכחי של השחקן.
3. **לולאת המשחק הראשית `while currentDay <= numberOfDays:`**:
   - הלולאה נמשכת כל עוד לא עברו כל הימים.
   - **שינוי מחיר המניה:**
     - `stockPrice = round(random.uniform(stockPrice * 0.9, stockPrice * 1.1),2)`: מחיר המניה משתנה באופן אקראי, בטווח שבין 90% ל-110% מהמחיר הנוכחי, ומעוגל לשתי ספרות לאחר הנקודה העשרונית.
   - **הצגת המצב הנוכחי**:
     - הצגת היום הנוכחי, מחיר המניה, כמות המניות והכסף.
   - **קלט פעולת השחקן**:
     - `action = input("Купить (buy) или продать (sell) акции? (или нажмите Enter для перехода к следующему дню): ").lower()`: נבקשת פעולה מהמשתמש (קנייה, מכירה או דילוג על היום), הפעולה מומרת לאותיות קטנות לנוחות.
    - **טיפול בפעולות השחקן**:
        - `if action == 'buy'`:
          -  נבקשת כמות מניות לקנייה `stocksToBuy`.
          -  נבדק האם יש מספיק כסף לקנייה: `if money >= stocksToBuy * stockPrice:`.
          - אם יש מספיק, הכסף מופחת, והמניות גדלות.
          - אחרת, מוצגת הודעה על מחסור בכסף.
        - `elif action == 'sell'`:
            -   נבקשת כמות מניות למכירה `stocksToSell`.
            -   נבדק האם יש מספיק מניות למכירה: `if numberOfStocks >= stocksToSell:`.
            -   אם יש מספיק, הכסף גדל, והמניות מופחתות.
            -   אחרת, מוצגת הודעה על מחסור במניות.
        - `else:`:
           - אם המשתמש הזין דבר אחר או לחץ על Enter, המשחק ממשיך ליום הבא.
     -  **הגדלת היום הנוכחי**:
        -  `currentDay += 1`: היום הנוכחי מוגדל ב-1.
        -   `print("-----------------")`: מוצג קו הפרדה להפרדה חזותית בין הימים.

4. **הצגת המצב הסופי של המשחק**:
   - לאחר סיום הלולאה מוצגת הודעה על סיום המשחק והמצב הסופי של השחקן.
"""