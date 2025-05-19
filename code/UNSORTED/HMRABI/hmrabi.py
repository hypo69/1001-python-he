<HMRABI>:
=================
קושי: 4
-----------------
המשחק "חמורבי" הוא משחק כלכלי מבוסס טקסט, שבו השחקן מנהל עיר עתיקה, ומנסה לשרוד ולשגשג בתנאים של משאבים מוגבלים. השחקן מקבל החלטות לגבי קנייה ומכירה של קרקע, חלוקת היבול, זריעה, ועוקב אחר רמת הרעב וגודל האוכלוסייה. המשחק מסתיים אם אוכלוסיית העיר מתה מרעב, או לאחר 10 שנות משחק.

כללי המשחק:
1.  השחקן מתחיל את המשחק עם 100 תושבים, 2800 בושלים של תבואה ו-1000 אקרים של קרקע.
2.  בכל שנה השחקן מקבל החלטות לגבי קנייה או מכירה של קרקע, כמות התבואה המשמשת לזריעה, והאכלת האוכלוסייה.
3.  שטח הקרקע נמדד באקרים, תבואה בבושלים.
4.  אירועים אקראיים, כגון מכת עכברים, יכולים להשפיע על מלאי התבואה.
5.  העיר שורדת אם יש מספיק תבואה כדי להאכיל את האוכלוסייה, אחרת האוכלוסייה מתה מרעב.
6.  המשחק מסתיים או לאחר 10 שנים, או כשהעיר חרבה לחלוטין (כל האוכלוסייה נספתה).
7.  תפוקת הקרקע משתנה בכל שנה (מספר אקראי מ-1 עד 8).
8.  מחיר הקרקע משתנה בכל שנה מ-15 עד 25 בושלים לאקר.

-----------------
אלגוריתם:
1.  אתחול משתנים: שנה = 0, אוכלוסייה = 100, תבואה = 2800, קרקע = 1000.
2.  התחלת מחזור משחק ל-10 שנים או עד שהאוכלוסייה הופכת ל-0.
3.  הצגת השנה הנוכחית, כמות האוכלוסייה, כמות התבואה וכמות הקרקע.
4.  חישוב והצגת מחיר הקרקע לאקר (מספר אקראי מ-15 עד 25).
5.  בקשה מהשחקן את כמות האקרים של קרקע לקנייה או מכירה (מספר חיובי לקנייה, מספר שלילי למכירה).
6.  בדיקה האם יש לשחקן מספיק תבואה לקניית קרקע, והאם יש מספיק קרקע למכירה.
7.  עדכון כמות הקרקע והתבואה.
8.  בקשה מהשחקן את כמות בושלים של תבואה לזריעה.
9.  בדיקה האם יש מספיק תבואה לזריעה.
10. חישוב התפוקה (מספר אקראי מ-1 עד 8 בושלים לאקר).
11. חישוב והוספת יבול חדש של תבואה למלאי הכולל.
12. חישוב כמות התבואה שנאכלה על ידי עכברים (מספר אקראי מ-0 עד 10%).
13. הפחתת כמות התבואה בכמות שנאכלה על ידי עכברים.
14. בקשה מהשחקן את כמות התבואה להאכלת האוכלוסייה.
15. אם אין מספיק תבואה להאכלה, האוכלוסייה מתה מרעב באופן יחסי למחסור (מחצית מהאוכלוסייה מתה אם חסרים 50% מהמלאי).
16. אם כל האוכלוסייה מתה, הצגת הודעת הפסד וסיום המשחק.
17. אם התבואה מספיקה להאכלה, הגדלת האוכלוסייה ב-10% או עד 1000, תלוי מה קטן יותר.
18. הגדלת השנה ב-1.
19. אם עברו 10 שנים, הצגת הודעה על סיום המשחק.
20. סיום המשחק.

-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    year = 0<br>
    population = 100<br>
    grain = 2800<br>
    land = 1000
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока <code><b>year < 10</b></code> и <code><b>population > 0</b></code>"}
    LoopStart -- Да --> DisplayStatus["<p align='left'>Вывод текущего статуса:
    <code><b>year</b>, <b>population</b>, <b>grain</b>, <b>land</b></code></p>"]
    DisplayStatus --> CalculateLandPrice["Вычисление цены земли: <code><b>landPrice = random(15, 25)</b></code>"]
    CalculateLandPrice --> DisplayLandPrice["Вывод цены земли: <code><b>landPrice</b></code>"]
    DisplayLandPrice --> InputLandTrade["Ввод: <code><b>landToBuyOrSell</b></code> (положительное - купить, отрицательное - продать)"]
    InputLandTrade --> CheckLandTrade["Проверка: хватает ли зерна для покупки или земли для продажи?"]
    CheckLandTrade -- Да --> UpdateLandAndGrain["<p align='left'>Обновление запасов:
    <code><b>land += landToBuyOrSell</b><br>
    <b>grain -= landToBuyOrSell * landPrice</b></code></p>"]
    UpdateLandAndGrain --> InputGrainToPlant["Ввод: <code><b>grainToPlant</b></code> (количество зерна для посева)"]
    InputGrainToPlant --> CheckGrainToPlant["Проверка: хватает ли зерна для посева?"]
    CheckGrainToPlant -- Да --> CalculateHarvest["Вычисление урожая: <code><b>yield = random(1, 8)</b></code><br><code><b>harvest = grainToPlant * yield</b></code>"]
    CalculateHarvest --> UpdateGrainWithHarvest["<code><b>grain += harvest</b></code>"]
    UpdateGrainWithHarvest --> CalculateRatsDamage["<p align='left'>Вычисление урона от крыс:
    <code><b>ratsDamage = random(0, 0.1) * grain</b></code></p>"]
    CalculateRatsDamage --> UpdateGrainWithRats["<code><b>grain -= ratsDamage</b></code>"]
    UpdateGrainWithRats --> InputGrainToFeed["Ввод: <code><b>grainToFeed</b></code> (количество зерна для пропитания)"]
    InputGrainToFeed --> CheckGrainToFeed["Проверка: хватает ли зерна для пропитания?"]
    CheckGrainToFeed -- Да --> UpdatePopulation["<code><b>population = min(1000, population * 1.1)</b></code>"]
    UpdatePopulation --> IncreaseYear["<code><b>year += 1</b></code>"]
    IncreaseYear --> LoopStart
    CheckGrainToFeed -- Нет --> CalculateStarvation["<p align='left'>Вычисление голода:
    <code><b>starved = population * (1 - grainToFeed/requiredGrain)</b></code></p>"]
    CalculateStarvation --> UpdatePopulationWithStarvation["<code><b>population -= starved</b></code>"]
    UpdatePopulationWithStarvation --> CheckPopulation["Проверка: <code><b>population <= 0</b></code>?"]
        CheckPopulation -- Да --> OutputGameOver["Вывод сообщения: <b>GAME OVER! You starved your population!</b>"]
        OutputGameOver --> End["Конец"]
    CheckPopulation -- Нет --> IncreaseYear
    CheckLandTrade -- Нет --> OutputErrorLand["Вывод сообщения: <b>Not enough resource for trade!</b>"]
    OutputErrorLand --> InputLandTrade
    CheckGrainToPlant -- Нет --> OutputErrorPlant["Вывод сообщения: <b>Not enough grain for planting!</b>"]
    OutputErrorPlant --> InputGrainToPlant
    LoopStart -- Нет --> OutputGameEnd["Вывод сообщения: <b>Game finished after 10 years</b>"]
    OutputGameEnd --> End
```

מקרא:
    Start - תחילת המשחק.
    InitializeVariables - אתחול ערכים התחלתיים למשתנים: שנה (year) מוגדרת ל-0, אוכלוסייה (population) ל-100, מלאי תבואה (grain) ל-2800, שטח קרקע (land) ל-1000 אקרים.
    LoopStart - תחילת מחזור המשחק, שנמשך כל עוד לא יעברו 10 שנים או כל עוד האוכלוסייה לא תהפוך ל-0.
    DisplayStatus - הצגת הסטטוס הנוכחי של המשחק: שנה, כמות האוכלוסייה, מלאי תבואה ושטח קרקע.
    CalculateLandPrice - חישוב מחיר אקראי לאקר קרקע בטווח שבין 15 ל-25 בושלים.
    DisplayLandPrice - הצגת המחיר לאקר קרקע.
    InputLandTrade - בקשה מהמשתמש את כמות הקרקע לקנייה (ערך חיובי) או למכירה (ערך שלילי).
    CheckLandTrade - בדיקה האם יש מספיק משאבים לביצוע העסקה של קנייה/מכירה של קרקע.
    UpdateLandAndGrain - עדכון מלאי הקרקע והתבואה בהתאם לעסקה שבוצעה.
    InputGrainToPlant - בקשה מהמשתמש את כמות התבואה שיש להשתמש בה לזריעה.
    CheckGrainToPlant - בדיקה האם יש מספיק תבואה לזריעה.
    CalculateHarvest - חישוב היבול על בסיס כמות התבואה שנזרעה ויבול אקראי לאקר (מ-1 עד 8 בושלים).
    UpdateGrainWithHarvest - עדכון מלאי התבואה תוך התחשבות ביבול שנקצר.
    CalculateRatsDamage - חישוב נזק מעכברים (ערך אקראי מ-0 עד 10% ממלאי התבואה).
    UpdateGrainWithRats - הפחתת מלאי התבואה בשיעור הנזק מהעכברים.
    InputGrainToFeed - בקשה מהמשתמש את כמות התבואה שיש להשתמש בה להאכלת האוכלוסייה.
    CheckGrainToFeed - בדיקה האם יש מספיק תבואה למחיית כל האוכלוסייה.
    UpdatePopulation - הגדלת האוכלוסייה ב-10% (אך לא יותר מ-1000 איש), אם התבואה מספיקה.
    IncreaseYear - הגדלת השנה הנוכחית ב-1.
    CalculateStarvation - חישוב כמות האוכלוסייה שנספה מרעב, אם התבואה אינה מספיקה.
    UpdatePopulationWithStarvation - עדכון האוכלוסייה תוך התחשבות באלו שנספו מרעב.
    CheckPopulation - בדיקה האם כל האוכלוסייה מתה מרעב.
    OutputGameOver - הצגת הודעת הפסד, אם כל האוכלוסייה מתה מרעב.
    OutputErrorLand - הצגת הודעת שגיאה, אם אין מספיק משאבים למסחר בקרקע.
    OutputErrorPlant - הצגת הודעת שגיאה, אם אין מספיק תבואה לזריעה.
    OutputGameEnd - הצגת הודעה על סיום המשחק לאחר 10 שנים.
    End - סיום המשחק.
```
```python
import random

# Инициализация переменных
year = 0          # השנה הנוכחית
population = 100  # אוכלוסייה התחלתית
grain = 2800      # כמות תבואה התחלתית
land = 1000       # שטח קרקע התחלתי

print("Добро пожаловать в игру Хаммурапи!")

# לולאת המשחק הראשית, מתבצעת כל עוד לא עברו 10 שנים או כל עוד כל האוכלוסייה לא נספתה.
while year < 10 and population > 0:
    print(f"\nГод {year + 1}")
    print(f"Население: {population}")
    print(f"Зерно: {grain} бушелей")
    print(f"Земля: {land} акров")

    # חישוב מחיר קרקע אקראי בין 15 ל-25 בושלים לאקר
    land_price = random.randint(15, 25)
    print(f"Цена земли: {land_price} бушелей за акр")

    # שאלת השחקן כמה קרקע לקנות או למכור.
    while True:
        try:
            land_trade = int(input("Сколько земли купить (+) или продать (-)? "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    # בדיקה האם יש מספיק תבואה לקנייה או קרקע למכירה. אם לא, מבקשים להזין שוב.
    while True:
        if land_trade > 0 and grain < land_trade * land_price:
            print("Недостаточно зерна для покупки земли.")
            try:
                land_trade = int(input("Сколько земли купить (+) или продать (-)? "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue
            
        elif land_trade < 0 and land < abs(land_trade):
            print("Недостаточно земли для продажи.")
            try:
                land_trade = int(input("Сколько земли купить (+) или продать (-)? "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue
        else:
            break

    # עדכון כמות הקרקע והתבואה
    land += land_trade
    grain -= land_trade * land_price
    
    # שאלת כמה תבואה לזרוע
    while True:
        try:
            grain_to_plant = int(input("Сколько зерна использовать для посева? "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    # בדיקה האם יש מספיק תבואה לזריעה. אם לא, מבקשים להזין שוב.
    while True:
        if grain < grain_to_plant:
            print("Недостаточно зерна для посева.")
            try:
                grain_to_plant = int(input("Сколько зерна использовать для посева? "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue
        else:
            break
    
    # חישוב יבול אקראי בין 1 ל-8 בושלים לאקר
    yield_per_acre = random.randint(1, 8)
    harvest = grain_to_plant * yield_per_acre
    grain += harvest
    
    # חישוב כמות התבואה שנאכלה על ידי עכברים, בין 0 ל-10% מכלל התבואה.
    rats_damage = int(random.random() * 0.1 * grain)
    grain -= rats_damage
    print(f"Крысы съели {rats_damage} бушелей зерна.")

    # שאלת כמה תבואה להקצות למחייה.
    while True:
        try:
            grain_to_feed = int(input("Сколько зерна отдать на пропитание? "))
            break
        except ValueError:
           print("Пожалуйста, введите целое число.")

    # בדיקה האם התבואה מספיקה למחייה.
    if grain_to_feed >= population:
        population = min(1000, int(population * 1.1))  # הגדלת האוכלוסייה ב-10%, אך לא יותר מ-1000.
        grain -= grain_to_feed
        print("Все сыты, население растёт!")
    else:
        starved = int(population * (1 - grain_to_feed / population )) # חישוב מספר המתים מרעב, באופן יחסי למחסור בתבואה.
        population -= starved
        grain -= grain_to_feed
        print(f"{starved} человек умерло от голода.")
        if population <= 0:
            print("Вы проиграли, все население вымерло от голода!")

    year += 1 # הגדלת השנה ב-1

if year == 10:
    print("Игра окончена. Прошло 10 лет.")

"""
הסבר קוד:
1. **ייבוא מודול `random`**:
    - `import random`: מייבא את המודול ליצירת מספרים אקראיים.

2. **אתחול משתנים**:
    - `year = 0`: מאתחל את המשתנה `year` למעקב אחר השנה הנוכחית (מתחילה ב-0).
    - `population = 100`: מאתחל את המשתנה `population` למעקב אחר כמות האוכלוסייה (מתחילה ב-100).
    - `grain = 2800`: מאתחל את המשתנה `grain` למעקב אחר כמות התבואה (מתחילה ב-2800).
    - `land = 1000`: מאתחל את המשתנה `land` למעקב אחר כמות הקרקע (מתחילה ב-1000).
    - `print("Добро пожаловать в игру Хаммурапи!")`: מציג הודעת קבלת פנים לשחקן.

3. **לולאת המשחק הראשית `while year < 10 and population > 0:`**:
    - הלולאה נמשכת כל עוד לא עברו 10 שנים או שהאוכלוסייה לא הפכה לקטנה או שווה ל-0.
    - `print(f"\nГод {year + 1}")`: מציגה את השנה הנוכחית.
    - `print(f"Население: {population}")`: מציגה את כמות האוכלוסייה הנוכחית.
    - `print(f"Зерно: {grain} бушелей")`: מציגה את כמות התבואה הנוכחית.
    - `print(f"Земля: {land} акров")`: מציגה את כמות הקרקע הנוכחית.

4. **קביעת מחיר הקרקע**:
    - `land_price = random.randint(15, 25)`: מייצרת מחיר אקראי לאקר קרקע בטווח שבין 15 ל-25 בושלים.
    - `print(f"Цена земли: {land_price} бушелей за акр")`: מציגה את מחיר הקרקע הנוכחי.

5. **קלט כמות קרקע למסחר**:
   - `while True: try...except ValueError`: לולאה לקלט כמות קרקע, מטפלת בשגיאת קלט של מספר לא שלם.
   - `land_trade = int(input("Сколько земли купить (+) или продать (-)? "))`: מבקשת מהמשתמש את כמות הקרקע לקנייה (ערך חיובי) או למכירה (ערך שלילי).

6. **בדיקת מספיקות המשאבים למסחר**:
   - `while True: if land_trade > 0 and grain < land_trade * land_price:`: לולאה לבדיקה האם יש מספיק תבואה לקניית קרקע
   - `elif land_trade < 0 and land < abs(land_trade):`: לולאה לבדיקה האם יש מספיק קרקע למכירה
   - אם אין מספיק משאבים, מוצגת הודעה מתאימה ומבוקש קלט חדש.

7. **עדכון כמות הקרקע והתבואה**:
   - `land += land_trade`: מעדכנת את כמות הקרקע.
   - `grain -= land_trade * land_price`: מעדכנת את כמות התבואה.

8. **קלט כמות תבואה לזריעה**:
   - `while True: try...except ValueError`: לולאה לקלט כמות תבואה לזריעה עם טיפול בשגיאת קלט של מספר לא שלם
   - `grain_to_plant = int(input("Сколько зерна использовать для посева? "))`: מבקשת מהמשתמש את כמות התבואה לזריעה.

9. **בדיקת מספיקות תבואה לזריעה**:
    -  `while True: if grain < grain_to_plant:`: לולאה לבדיקה האם יש מספיק תבואה לזריעה.
    - אם אין מספיק תבואה, מוצגת הודעה ומבוקש קלט חדש.

10. **חישוב יבול**:
    - `yield_per_acre = random.randint(1, 8)`: מייצרת כמות יבול אקראית בין 1 ל-8 בושלים לאקר.
    - `harvest = grain_to_plant * yield_per_acre`: מחשבת את היבול הכולל.
    - `grain += harvest`: מוסיפה את היבול למלאי התבואה הכולל.

11. **חישוב נזק מעכברים**:
    - `rats_damage = int(random.random() * 0.1 * grain)`: מחשבת נזק אקראי מעכברים (מ-0 עד 10% ממלאי התבואה).
    - `grain -= rats_damage`: מפחיתה את כמות התבואה בשיעור הנזק מהעכברים.
    - `print(f"Крысы съели {rats_damage} бушелей зерна.")`: מציגה הודעה על כמות התבואה שנאכלה על ידי עכברים.

12. **קלט כמות תבואה למחייה**:
     - `while True: try...except ValueError`: לולאה לקלט כמות תבואה למחייה, מטפלת בשגיאת קלט של מספר לא שלם.
    - `grain_to_feed = int(input("Сколько зерна отдать на пропитание? "))`: מבקשת מהמשתמש את כמות התבואה למחיית האוכלוסייה.

13. **בדיקת מספיקות תבואה למחייה**:
     - `if grain_to_feed >= population:`: בודקת האם התבואה מספיקה למחיית כל האוכלוסייה
     - `population = min(1000, int(population * 1.1))`: אם התבואה מספיקה, מגדילה את האוכלוסייה ב-10%, אך לא יותר מ-1000.
     - `grain -= grain_to_feed`: מפחיתה את מלאי התבואה בכמות שהוקצתה למחייה.
     - `else:`: מבוצע אם אין מספיק תבואה.
     - `starved = int(population * (1 - grain_to_feed / population ))`: מחשבת את כמות המתים מרעב באופן יחסי למחסור בתבואה.
     - `population -= starved`: מפחיתה את האוכלוסייה בכמות המתים.
     - `print(f"{starved} человек умерло от голода.")`: מציגה הודעה על כמות המתים מרעב.
     - `if population <= 0:`: בודקת האם כל האוכלוסייה מתה.
     - `print("Вы проиграли, все население вымерло от голода!")`: מציגה הודעת הפסד במקרה שכל האוכלוסייה מתה.
     
14. **הגדלת השנה**:
    - `year += 1`: מגדילה את ערך השנה ב-1.

15. **סיום המשחק**:
    - `if year == 10:`: בודקת האם עברו 10 שנים.
    - `print("Игра окончена. Прошло 10 лет.")`: מציגה הודעה על סיום המשחק אם עברו 10 שנים.
"""
```
```python
import random

# ייבוא מודול random:
# import random: מייבא את המודול ליצירת מספרים אקראיים.

# אתחול משתנים:
# year = 0: מאתחל את המשתנה year למעקב אחר השנה הנוכחית (מתחילה ב-0).
year = 0          # השנה הנוכחית
# population = 100: מאתחל את המשתנה population למעקב אחר כמות האוכלוסייה (מתחילה ב-100).
population = 100  # אוכלוסייה התחלתית
# grain = 2800: מאתחל את המשתנה grain למעקב אחר כמות התבואה (מתחילה ב-2800).
grain = 2800      # כמות תבואה התחלתית
# land = 1000: מאתחל את המשתנה land למעקב אחר כמות הקרקע (מתחילה ב-1000).
land = 1000       # שטח קרקע התחלתי

# print("Добро пожаловать в игру Хаммурапи!"): מציג הודעת קבלת פנים לשחקן.
print("Добро пожаловать в игру Хаммурапи!")

# לולאת המשחק הראשית, מתבצעת כל עוד לא עברו 10 שנים או כל עוד כל האוכלוסייה לא נספתה.
# לולאת המשחק הראשית while year < 10 and population > 0::
# הלולאה נמשכת כל עוד לא עברו 10 שנים או שהאוכלוסייה לא הפכה לקטנה או שווה ל-0.
while year < 10 and population > 0:
    # print(f"\nГод {year + 1}"): מציגה את השנה הנוכחית.
    print(f"\nГод {year + 1}")
    # print(f"Население: {population}"): מציגה את כמות האוכלוסייה הנוכחית.
    print(f"Население: {population}")
    # print(f"Зерно: {grain} бушелей"): מציגה את כמות התבואה הנוכחית.
    print(f"Зерно: {grain} бушелей")
    # print(f"Земля: {land} акров"): מציגה את כמות הקרקע הנוכחית.
    print(f"Земля: {land} акров")

    # קביעת מחיר הקרקע:
    # land_price = random.randint(15, 25): מייצרת מחיר אקראי לאקר קרקע בטווח שבין 15 ל-25 בושלים.
    land_price = random.randint(15, 25)
    # print(f"Цена земли: {land_price} бушелей за акр") הנקודה הרביעית באלגוריתם ונקודה 4 בקוד
    print(f"Цена земли: {land_price} бушелей за акр")

    # קלט כמות קרקע למסחר:
    # בלוק while True: try...except ValueError: לולאה לקלט כמות קרקע, מטפלת בשגיאת קלט של מספר לא שלם.
    # land_trade = int(input("Сколько земли купить (+) или продать (-)? ")) מבקשת מהמשתמש את כמות הקרקע לקנייה (ערך חיובי) או למכירה (ערך שלילי).
    while True:
        try:
            land_trade = int(input("Сколько земли купить (+) или продать (-)? "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    # בדיקת מספיקות המשאבים למסחר:
    # בלוק while True: if land_trade > 0 and grain < land_trade * land_price:: לולאה לבדיקה האם יש מספיק תבואה לקניית קרקע
    # elif land_trade < 0 and land < abs(land_trade):: לולאה לבדיקה האם יש מספיק קרקע למכירה
    # אם אין מספיק משאבים, מוצגת הודעה מתאימה ומבוקש קלט חדש.
    while True:
        if land_trade > 0 and grain < land_trade * land_price:
            print("Недостаточно зерна для покупки земли.")
            try:
                land_trade = int(input("Сколько земли купить (+) или продать (-)? "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue
            
        elif land_trade < 0 and land < abs(land_trade):
            print("Недостаточно земли для продажи.")
            try:
                land_trade = int(input("Сколько земли купить (+) или продать (-)? "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue
        else:
            break

    # עדכון כמות הקרקע והתבואה:
    # land += land_trade: מעדכנת את כמות הקרקע.
    land += land_trade
    # grain -= land_trade * land_price: מעדכנת את כמות התבואה.
    grain -= land_trade * land_price
    
    # קלט כמות תבואה לזריעה:
    # בלוק while True: try...except ValueError: לולאה לקלט כמות תבואה לזריעה עם טיפול בשגיאת קלט של מספר לא שלם
    # grain_to_plant = int(input("Сколько зерна использовать для посева? ")) מבקשת מהמשתמש את כמות התבואה לזריעה.
    while True:
        try:
            grain_to_plant = int(input("Сколько зерна использовать для посева? "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    # בדיקת מספיקות תבואה לזריעה:
    # בלוק while True: if grain < grain_to_plant:: לולאה לבדיקה האם יש מספיק תבואה לזריעה.
    # אם אין מספיק תבואה, מוצגת הודעה ומבוקש קלט חדש.
    while True:
        if grain < grain_to_plant:
            print("Недостаточно зерна для посева.")
            try:
                grain_to_plant = int(input("Сколько зерна использовать для посева? "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue
        else:
            break
    
    # חישוב יבול:
    # yield_per_acre = random.randint(1, 8): מייצרת כמות יבול אקראית בין 1 ל-8 בושלים לאקר.
    yield_per_acre = random.randint(1, 8)
    # harvest = grain_to_plant * yield_per_acre: מחשבת את היבול הכולל.
    harvest = grain_to_plant * yield_per_acre
    # grain += harvest: מוסיפה את היבול למלאי התבואה הכולל.
    grain += harvest
    
    # חישוב נזק מעכברים:
    # rats_damage = int(random.random() * 0.1 * grain): מחשבת נזק אקראי מעכברים (מ-0 עד 10% ממלאי התבואה).
    rats_damage = int(random.random() * 0.1 * grain)
    # grain -= rats_damage: מפחיתה את כמות התבואה בשיעור הנזק מהעכברים.
    grain -= rats_damage
    # print(f"Крысы съели {rats_damage} бушелей зерна."): מציגה הודעה על כמות התבואה שנאכלה על ידי עכברים.
    print(f"Крысы съели {rats_damage} бушелей зерна.")

    # קלט כמות תבואה למחייה:
    # בלוק while True: try...except ValueError: לולאה לקלט כמות תבואה למחייה, מטפלת בשגיאת קלט של מספר לא שלם.
    # grain_to_feed = int(input("Сколько зерна отдать на пропитание? ")) מבקשת מהמשתמש את כמות התבואה למחיית האוכלוסייה.
    while True:
        try:
            grain_to_feed = int(input("Сколько зерна отдать на пропитание? "))
            break
        except ValueError:
           print("Пожалуйста, введите целое число.")

    # בדיקת מספיקות תבואה למחייה:
    # if grain_to_feed >= population:: בודקת האם התבואה מספיקה למחיית כל האוכלוסייה
    if grain_to_feed >= population:
        # population = min(1000, int(population * 1.1)): אם התבואה מספיקה, מגדילה את האוכלוסייה ב-10%, אך לא יותר מ-1000.
        population = min(1000, int(population * 1.1))  # הגדלת האוכלוסייה ב-10%, אך לא יותר מ-1000.
        # grain -= grain_to_feed: מפחיתה את מלאי התבואה בכמות שהוקצתה למחייה.
        grain -= grain_to_feed
        # print("Все сыты, население растёт!"): מציגה הודעה.
        print("Все сыты, население растёт!")
    # else:: מבוצע אם אין מספיק תבואה.
    else:
        # starved = int(population * (1 - grain_to_feed / population )): מחשבת את כמות המתים מרעב באופן יחסי למחסור בתבואה.
        starved = int(population * (1 - grain_to_feed / population )) # חישוב מספר המתים מרעב, באופן יחסי למחסור בתבואה.
        # population -= starved: מפחיתה את האוכלוסייה בכמות המתים.
        population -= starved
        # print(f"{starved} человек умерло от голода."): מציגה הודעה על כמות המתים מרעב.
        print(f"{starved} человек умерло от голода.")
        # if population <= 0:: בודקת האם כל האוכלוסייה מתה.
        if population <= 0:
            # print("Вы проиграли, все население вымерло от голода!"): מציגה הודעת הפסד במקרה שכל האוכלוסייה מתה.
            print("Вы проиграли, все население вымерло от голода!")

    # year += 1: מגדילה את ערך השנה ב-1.
    year += 1 # הגדלת השנה ב-1

# if year == 10:: בודקת האם עברו 10 שנים.
if year == 10:
    # print("Игра окончена. Прошло 10 лет."): מציגה הודעה על סיום המשחק אם עברו 10 שנים.
    print("Игра окончена. Прошло 10 лет.")

"""
הסבר קוד:
1. **ייבוא מודול `random`**:
    - `import random`: מייבא את המודול ליצירת מספרים אקראיים.

2. **אתחול משתנים**:
    - `year = 0`: מאתחל את המשתנה `year` למעקב אחר השנה הנוכחית (מתחילה ב-0).
    - `population = 100`: מאתחל את המשתנה `population` למעקב אחר כמות האוכלוסייה (מתחילה ב-100).
    - `grain = 2800`: מאתחל את המשתנה `grain` למעקב אחר כמות התבואה (מתחילה ב-2800).
    - `land = 1000`: מאתחל את המשתנה `land` למעקב אחר כמות הקרקע (מתחילה ב-1000).
    - `print("Добро пожаловать в игру Хаммурапи!")`: מציג הודעת קבלת פנים לשחקן.

3. **לולאת המשחק הראשית `while year < 10 and population > 0:`**:
    - הלולאה נמשכת כל עוד לא עברו 10 שנים או שהאוכלוסייה לא הפכה לקטנה או שווה ל-0.
    - `print(f"\nГод {year + 1}")`: מציגה את השנה הנוכחית.
    - `print(f"Население: {population}")`: מציגה את כמות האוכלוסייה הנוכחית.
    - `print(f"Зерно: {grain} бушелей")`: מציגה את כמות התבואה הנוכחית.
    - `print(f"Земля: {land} акров")`: מציגה את כמות הקרקע הנוכחית.

4. **קביעת מחיר הקרקע**:
    - `land_price = random.randint(15, 25)`: מייצרת מחיר אקראי לאקר קרקע בטווח שבין 15 ל-25 בושלים.
    - `print(f"Цена земли: {land_price} бушелей за акр")`: מציגה את מחיר הקרקע הנוכחי.

5. **קלט כמות קרקע למסחר**:
   - `while True: try...except ValueError`: לולאה לקלט כמות קרקע, מטפלת בשגיאת קלט של מספר לא שלם.
   - `land_trade = int(input("Сколько земли купить (+) или продать (-)? "))`: מבקשת מהמשתמש את כמות הקרקע לקנייה (ערך חיובי) או למכירה (ערך שלילי).

6. **בדיקת מספיקות המשאבים למסחר**:
   - `while True: if land_trade > 0 and grain < land_trade * land_price:`: לולאה לבדיקה האם יש מספיק תבואה לקניית קרקע
   - `elif land_trade < 0 and land < abs(land_trade):`: לולאה לבדיקה האם יש מספיק קרקע למכירה
   - אם אין מספיק משאבים, מוצגת הודעה מתאימה ומבוקש קלט חדש.

7. **עדכון כמות הקרקע והתבואה**:
   - `land += land_trade`: מעדכנת את כמות הקרקע. אם ערך `land_trade` חיובי, אז הקרקע נקנית, וכמות הקרקע גדלה. אם `land_trade` שלילי, אז הקרקע נמכרת, וכמות הקרקע קטנה.
   - `grain -= land_trade * land_price`: מעדכנת את כמות התבואה בהתאם לקנייה או מכירה של קרקע.

8. **קלט כמות תבואה לזריעה**:
    - בלוק `while True:` משמש לבקשת קלט מהמשתמש עד שיזין נתונים תקינים.
    - `try...except ValueError`: בלוק זה מטפל בשגיאה אם המשתמש יזין מספר לא שלם.
   - `grain_to_plant = int(input("Сколько зерна использовать для посева? "))`: מבקשת מהמשתמש את כמות התבואה לזריעה.

9. **בדיקת מספיקות תבואה לזריעה**:
   -  בלוק `while True:` משמש לבקשת קלט מהמשתמש עד שיתקיימו תנאי תקינות הנתונים המוזנים.
   - `if grain < grain_to_plant:`: בודקת האם יש מספיק תבואה לזריעה. אם לא, מציגה הודעה ומבקשת קלט חדש.

10. **חישוב יבול**:
    - `yield_per_acre = random.randint(1, 8)`: מייצרת יבול אקראי (בין 1 ל-8 בושלים לאקר).
    - `harvest = grain_to_plant * yield_per_acre`: מחשבת את היבול הכולל של התבואה.
    - `grain += harvest`: מגדילה את כמות התבואה בשיעור היבול.

11. **חישוב נזק מעכברים**:
    - `rats_damage = int(random.random() * 0.1 * grain)`: מחשבת נזק אקראי מעכברים (מ-0 עד 10% מכמות התבואה הנוכחית).
    - `grain -= rats_damage`: מפחיתה את כמות התבואה בשיעור הנזק מהעכברים.
    - `print(f"Крысы съели {rats_damage} бушелей зерна.")`: מציגה הודעה על כמות התבואה שנאכלה על ידי עכברים.

12. **קלט כמות תבואה למחייה**:
    - בלוק `while True:` משמש לבקשת קלט מהמשתמש עד שיזין נתונים תקינים.
    - `try...except ValueError`: בלוק זה מטפל בשגיאה אם המשתמש יזין מספר לא שלם.
    -`grain_to_feed = int(input("Сколько зерна отдать на пропитание? "))`: מבקשת מהמשתמש את כמות התבואה למחיית האוכלוסייה.

13. **בדיקת מספיקות תבואה למחייה**:
    - `if grain_to_feed >= population:`: בודקת האם התבואה מספיקה למחיית כל האוכלוסייה.
    - `population = min(1000, int(population * 1.1))`: אם התבואה מספיקה, מגדילה את האוכלוסייה ב-10%, אך לא יותר מ-1000.
    - `grain -= grain_to_feed`: מפחיתה את כמות התבואה בכמות שהוקצתה למחיית האוכלוסייה.
    - `else:`: מבוצע, אם אין מספיק תבואה.
    - `starved = int(population * (1 - grain_to_feed / population ))`: מחשבת את כמות המתים מרעב באופן יחסי למחסור בתבואה.
    - `population -= starved`: מפחיתה את כמות האוכלוסייה במספר המתים.
    - `print(f"{starved} человек умерло от голода.")`: מציגה הודעה על כמות המתים מרעב.
    - `if population <= 0:`: בודקת האם כל האוכלוסייה מתה.
    - `print("Вы проиграли, все население вымерло от голода!")`: מציגה הודעת הפסד במקרה שכל האוכלוסייה מתה.

14. **הגדלת השנה**:
    - `year += 1`: מגדילה את ערך השנה ב-1.

15. **סיום המשחק**:
    - `if year == 10:`: בודקת האם עברו 10 שנים.
    - `print("Игра окончена. Прошло 10 лет.")`: מציגה הודעה על סיום המשחק, אם עברו 10 שנים.
"""
```