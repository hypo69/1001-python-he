<YAHTZE>:
=================
**רמת קושי:** 6
-----------------
משחק "Yahtzee" הוא משחק קוביות שבו השחקן מטיל חמש קוביות ומנסה לצבור נקודות על ידי יצירת קומבינציות, כגון זוגות, שלשות, פול האוס, סטרייטים וכו'.
לשחקן יש שלושה ניסיונות הטלה עבור כל קומבינציה, עם אפשרות להשאיר חלק מהקוביות ולהטיל מחדש את הנותרות.
המשחק מורכב מ-13 סבבים, כשכל סבב מוערך לפי אחת הקומבינציות. בסיום המשחק, הנקודות מסוכמות.
**חוקי המשחק:**
1.  בכל סבב, השחקן מטיל 5 קוביות.
2.  לאחר ההטלה הראשונה, השחקן יכול להשאיר קוביות כרצונו ולהטיל מחדש את הנותרות.
3.  לאחר ההטלה השנייה, השחקן יכול שוב להשאיר קוביות כרצונו ולהטיל מחדש את הנותרות.
4.  לאחר ההטלה השלישית, על השחקן לבחור אחת מהקטגוריות הזמינות לרישום התוצאה.
5.  הקטגוריות כוללות:
    -   סכום כל האחדות, הדובלים, השלשות, הרביעיות, החמישיות והשישיות.
    -   קומבינציות: 3 זהים, 4 זהים, פול האוס, סטרייט קטן, סטרייט גדול, יאצ'י (כל ה-5 זהים), צ'אנס.
6.  כל קטגוריה יכולה לשמש פעם אחת בלבד במשחק.
7.  המשחק מורכב מ-13 סבבים, אחד לכל קטגוריה.
8.  לאחר 13 סבבים, הנקודות מסוכמות.
-----------------
**אלגוריתם:**
1.  לאתחל מערך קטגוריות, המייצגות את הקומבינציות לרישום ניקוד, ומערך לאחסון הניקוד.
2.  להתחיל לולאה של 13 סבבים:
    2.1. לאתחל מערך הטלות, המייצג 5 קוביות משחק.
    2.2. להתחיל לולאה של 3 ניסיונות הטלה:
         2.2.1. ליצור 5 מספרים אקראיים (מ-1 עד 6) עבור מערך ההטלות.
         2.2.2. להציג את תוצאות ההטלה על המסך.
         2.2.3. אם זה לא הניסיון השלישי, לבקש קלט מהשחקן אילו קוביות הוא רוצה להטיל מחדש.
         2.2.4. להטיל מחדש את הקוביות שנבחרו (תוך שמירה על אלו שלא הוטלו מחדש).
    2.3. להציג רשימה של הקטגוריות הזמינות שטרם נוצלו.
    2.4. לבקש קלט מהשחקן לבחירת קטגוריה.
    2.5. לחשב את מספר הנקודות עבור הקטגוריה שנבחרה, בהתאם להטלת הקוביות.
    2.6. לרשום את מספר הנקודות במערך הניקוד עבור הקטגוריה המתאימה.
3.  לחשב את סך כל הנקודות.
4.  להציג את טבלת הניקוד לפי קטגוריות ואת הסכום הכולל.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["Начало"] --> InitializeGame["Инициализация игры: <br><code><b>categories = [...]<br>scores = [...]<br>used_categories = []</b></code>"]
    InitializeGame --> RoundLoopStart{"Начало цикла: 13 раундов"}
    RoundLoopStart -- Да --> InitializeDice["Инициализация бросков: <code><b>dice = []</b></code>"]
    InitializeDice --> RollLoopStart{"Начало цикла: 3 попытки броска"}
    RollLoopStart -- Да --> RollDice["Бросок костей: <code><b>dice = random(1-6, 5)</b></code>"]
    RollDice --> OutputDice["Вывод результата броска: <code><b>dice</b></code>"]
    OutputDice --> CheckRollAttempt{"Проверка: <code><b>rollAttempt < 3?</b></code>"}
    CheckRollAttempt -- Да --> InputKeepDice["Запрос какие кубики оставить: <code><b>keep_indices</b></code>"]
    InputKeepDice --> ReRollDice["Перебросить выбранные кубики"]
    ReRollDice --> RollLoopStart
    CheckRollAttempt -- Нет --> OutputAvailableCategories["Вывод доступных категорий"]
     OutputAvailableCategories--> InputCategoryChoice["Выбор категории: <code><b>category</b></code>"]
     InputCategoryChoice --> CalculateScore["Подсчет очков для категории: <code><b>score = calculateScore(dice, category)</b></code>"]
    CalculateScore --> UpdateScorecard["Записать очки в таблицу: <code><b>scores[category] = score<br>used_categories.add(category)</b></code>"]
     UpdateScorecard --> RoundLoopStart
      RoundLoopStart -- Нет --> CalculateTotalScore["Суммировать очки: <code><b>totalScore = sum(scores)</b></code>"]
      CalculateTotalScore --> OutputScorecard["Вывод таблицы очков: <code><b>scores, totalScore</b></code>"]
       OutputScorecard--> End["Конец"]
```
**מקרא:**
    Start - התחלת התוכנית.
    InitializeGame - אתחול משתנים: מערכי קטגוריות, ניקוד, קטגוריות שנוצלו.
    RoundLoopStart - תחילת לולאה, אשר מבוצעת 13 פעמים (מספר הסבבים במשחק).
    InitializeDice - אתחול מערך עבור הטלות קוביות.
    RollLoopStart - תחילת לולאה, אשר מבוצעת 3 פעמים (מספר מרבי של הטלות בסבב).
    RollDice - נוצרת הטלה אקראית של 5 קוביות עם ערכים מ-1 עד 6.
    OutputDice - מציג את התוצאות הנוכחיות של ההטלה.
    CheckRollAttempt - בדיקה האם מספר ההטלות הגיע ל-3, מספר ההטלות המרבי בסבב.
    InputKeepDice - בקשת קלט מהמשתמש, אילו קוביות להשאיר.
    ReRollDice - הטלה מחדש של קוביות שלא נבחרו.
    OutputAvailableCategories - הצגת רשימת הקטגוריות הזמינות.
    InputCategoryChoice - בקשת קלט מהמשתמש לבחירת קטגוריה.
    CalculateScore - חישוב ניקוד עבור הקטגוריה שנבחרה בהתאם להטלה.
    UpdateScorecard - רישום הניקוד בטבלה והוספת הקטגוריה שנבחרה לרשימת הקטגוריות שנוצלו.
    CalculateTotalScore - סיכום הניקוד מכל הקטגוריות.
    OutputScorecard - הצגת טבלת הניקוד לפי קטגוריות והסכום הכולל.
    End - סיום התוכנית.
```python
import random

def roll_dice():
    """מטילה 5 קוביות ומחזירה את התוצאות."""
    return [random.randint(1, 6) for _ in range(5)]

def calculate_score(dice, category):
    """מחשבת את הניקוד עבור הקטגוריה שנבחרה."""
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1

    if category in ['1', '2', '3', '4', '5', '6']:
        value = int(category)
        return sum(die for die in dice if die == value)
    elif category == '3 of a kind':
        for count in counts.values():
            if count >= 3:
                return sum(dice)
        return 0
    elif category == '4 of a kind':
        for count in counts.values():
            if count >= 4:
                return sum(dice)
        return 0
    elif category == 'full house':
        if 2 in counts.values() and 3 in counts.values():
            return 25
        return 0
    elif category == 'small straight':
        dice.sort()
        unique_dice = sorted(list(set(dice)))
        for i in range(len(unique_dice) - 3):
            if unique_dice[i+1] == unique_dice[i] + 1 and \
               unique_dice[i+2] == unique_dice[i] + 2 and \
               unique_dice[i+3] == unique_dice[i] + 3:
                return 30
        return 0
    elif category == 'large straight':
          dice.sort()
          unique_dice = sorted(list(set(dice)))
          if len(unique_dice) == 5:
              for i in range(len(unique_dice)-1):
                if unique_dice[i+1] != unique_dice[i]+1:
                  return 0
              return 40
          return 0
    elif category == 'yahtzee':
        if len(set(dice)) == 1:
            return 50
        return 0
    elif category == 'chance':
        return sum(dice)
    return 0

def play_yahtzee():
    """הפונקציה הראשית למשחק Yahtzee."""
    categories = [
      '1', '2', '3', '4', '5', '6',
      '3 of a kind', '4 of a kind',
      'full house', 'small straight', 'large straight',
      'yahtzee', 'chance'
    ]
    scores = {category: None for category in categories}  # מילון לאחסון הניקוד
    used_categories = set()  # קבוצה של קטגוריות שנוצלו

    for round_num in range(1, 14):
        print(f"\n----- סבב {round_num} -----")
        dice = roll_dice()  # מטילים קוביות
        print(f"הטלה ראשונה: {dice}")

        for roll_attempt in range(1, 3): # נותנים 3 ניסיונות
            keep_dice_str = input(f"ניסיון {roll_attempt}, אילו קוביות להשאיר (הזן מספרים ברווח, מ-1 עד 5, 0 = הטל מחדש הכל, n = אל תטיל מחדש כלום)? ")

            if keep_dice_str.lower() == 'n':
              break
            if keep_dice_str == '0':
              dice = roll_dice()
              print(f"הטלה חדשה: {dice}")
              continue
            try:
                keep_indices = [int(i) - 1 for i in keep_dice_str.split()] # מקבלים רשימת אינדקסים של קוביות שיש להשאיר
                if not all(0 <= index < 5 for index in keep_indices):
                  print("אינדקסים שגויים, נסה שוב.")
                  continue
                new_dice = [] # רשימה חדשה של קוביות
                for i in range(5): # עוברים על כל הקוביות
                  if i not in keep_indices: # אם אין צורך להשאיר קובייה, אז מטילים אותה מחדש
                    new_dice.append(random.randint(1, 6))
                  else: # אחרת, מוסיפים את הקובייה לרשימה החדשה מהרשימה הישנה
                    new_dice.append(dice[i])
                dice = new_dice
                print(f"הטלה חדשה: {dice}")
            except ValueError:
                print("קלט שגוי, נסה שוב.")

        available_categories = [cat for cat in categories if cat not in used_categories] # רשימת קטגוריות זמינות
        print("קטגוריות זמינות:")
        for i, cat in enumerate(available_categories, start=1):
            print(f"{i}. {cat}")

        while True:
            try:
                choice_index = int(input("בחר מספר קטגוריה לרישום הניקוד: "))-1 # מבקשים קלט לבחירה
                if  0 <= choice_index < len(available_categories) :
                    category_choice = available_categories[choice_index]
                    break
                else:
                    print('מספר קטגוריה שגוי, נסה שוב.')
            except ValueError:
                print('קלט שגוי, נסה שוב.')

        score = calculate_score(dice, category_choice) # מחשבים ניקוד
        scores[category_choice] = score # רושמים ניקוד
        used_categories.add(category_choice) # מוסיפים את הקטגוריה לרשימת הקטגוריות שנוצלו
        print(f"ניקוד עבור קטגוריה {category_choice}: {score}")

    # מציגים את טבלת הניקוד
    print("\n----- טבלת ניקוד סופית -----")
    for category, score in scores.items():
      print(f"{category}: {score if score is not None else 0}")

    total_score = sum(score if score is not None else 0 for score in scores.values())
    print(f"ציון כולל: {total_score}")

if __name__ == "__main__":
    play_yahtzee()
"""
**הסבר קוד:**
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבאת את מודול `random`, המשמש ליצירת מספרים אקראיים.

2.  **פונקציה `roll_dice()`**:
     -   `def roll_dice():`: מגדירה פונקציה המדמה הטלה של חמש קוביות משחק.
     -   `return [random.randint(1, 6) for _ in range(5)]`: יוצרת רשימה של 5 מספרים אקראיים בטווח 1 עד 6, המייצגים את תוצאות הטלת הקוביות.

3.  **פונקציה `calculate_score(dice, category)`**:
     -   `def calculate_score(dice, category):`: מגדירה פונקציה לחישוב הניקוד עבור הקטגוריה שנבחרה.
     -   `counts = {}`: מאתחלת מילון ריק לספירת כמות כל ערך על הקוביות.
     -   `for die in dice: counts[die] = counts.get(die, 0) + 1`: סופרת את כמות כל ערך על הקוביות
     -   בלוקים מותנים `if category in [...]`: בודקת איזו קטגוריה נבחרה על ידי השחקן ומחשבת את הניקוד.
         -   עבור קטגוריות 1 עד 6 מסכמת רק את אותן קוביות אשר תואמות לקטגוריה שנבחרה.
         -   עבור "3 of a kind" ו-"4 of a kind" בודקת קיום 3 או 4 ערכים זהים ומחזירה את סכום כל הקוביות או 0.
         -   עבור "full house" בודקת קיום זוג ושלישייה ומחזירה 25 נקודות, אחרת 0.
         -   עבור "small straight" בודקת קיום 4 מספרים עוקבים ומחזירה 30 נקודות, אחרת 0.
         -   עבור "large straight" בודקת קיום 5 מספרים עוקבים ומחזירה 40 נקודות, אחרת 0.
         -   עבור "yahtzee" בודקת קיום 5 ערכים זהים ומחזירה 50 נקודות, אחרת 0.
         -   עבור "chance" מחזירה את סכום כל הקוביות.

4.  **פונקציה `play_yahtzee()`**:
     -   `def play_yahtzee():`: מגדירה את פונקציית המשחק הראשית של Yahtzee.
     -   `categories = [...]`: מגדירה רשימה של כל הקטגוריות האפשריות.
     -   `scores = {category: None for category in categories}`: יוצרת מילון לאחסון הניקוד שנצבר עבור כל קטגוריה, ערך התחלתי None.
     -   `used_categories = set()`: יוצרת קבוצה לאחסון קטגוריות שנוצלו.
     -   `for round_num in range(1, 14):`: לולאת המשחק הראשית. סך הכל 13 סבבים.
         -   `dice = roll_dice()`: מטילה 5 קוביות, התוצאה נשמרת במשתנה `dice`.
         -   `print(f"הטלה ראשונה: {dice}")`: מציגה את תוצאת ההטלה הראשונה על המסך.
         -   `for roll_attempt in range(1, 3):`: לולאה להטלות נוספות (עד פעמיים).
             -   `keep_dice_str = input(...)`: מבקשת קלט מהשחקן, אילו קוביות יש להשאיר, מוזנים אינדקסים (1-5) ברווח, 0 - הטל מחדש הכל, n - אל תטיל מחדש.
             -   `if keep_dice_str.lower() == 'n': break`: אם השחקן מזין `n`, לולאת ההטלות מסתיימת.
             -   `if keep_dice_str == '0':`: אם השחקן מזין `0`, כל הקוביות מוטלות מחדש.
             -   `try... except ValueError`: בלוק try-except לטיפול בשגיאות קלט.
             -   `keep_indices = [int(i) - 1 for i in keep_dice_str.split()]`: ממירה את האינדקסים שהוזנו לרשימת אינדקסים להשארת קוביות.
             -   `new_dice = []` נוצר מערך ריק עבור קוביות חדשות.
             -   `for i in range(5):`: לולאה על כל הקוביות.
             -   `if i not in keep_indices:`: אם אין צורך להשאיר את הקובייה, אז היא מוטלת מחדש.
             -   `else:`: אם יש צורך להשאיר את הקובייה, אז היא מתווספת לרשימה החדשה מהרשימה הישנה.
             -   `dice = new_dice`: מעדכנת את מערך הקוביות.
             -   `print(f"הטלה חדשה: {dice}")`: מציגה את תוצאות ההטלה החדשה על המסך.
         -   `available_categories = [cat for cat in categories if cat not in used_categories]`: נוצרת רשימה של קטגוריות זמינות.
         -   `print("קטגוריות זמינות:")` ו-`for ...`: מוצגת רשימת הקטגוריות הזמינות על המסך.
         -   `while True:`: לולאה לבחירת קטגוריה על ידי השחקן.
              -   `try... except ValueError:`: בלוק try-except לטיפול בשגיאות קלט.
              -   `choice_index = int(input(...))-1`: מבקשת קלט של מספר הקטגוריה שנבחרה.
              -   `if  0 <= choice_index < len(available_categories) :`: בדיקה שהאינדקס שנבחר קיים במערך הקטגוריות הזמינות.
              -   `category_choice = available_categories[choice_index]`: שומרים את הקטגוריה שנבחרה.
              -   `break`: מסיימים את הלולאה אם הקלט תקין.
         -   `score = calculate_score(dice, category_choice)`: מחשבת ניקוד עבור הקטגוריה שנבחרה.
         -   `scores[category_choice] = score`: שומרת את הניקוד במילון `scores`.
         -   `used_categories.add(category_choice)`: מוסיפה את הקטגוריה שנבחרה לקבוצה `used_categories`.
         -   `print(f"ניקוד עבור קטגוריה {category_choice}: {score}")`: מציגה את הניקוד שנצבר עבור הקטגוריה שנבחרה.
     -   `print("\n----- טבלת ניקוד סופית -----")` ו-`for ...`: הצגת טבלת הניקוד הסופית.
     -   `total_score = sum(score if score is not None else 0 for score in scores.values())`: חישוב סך כל הנקודות.
     -   `print(f"ציון כולל: {total_score}")`: הצגת סך כל הנקודות.

5.  **הפעלת המשחק**:
     -   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_yahtzee()` תופעל רק אם הקובץ מופעל ישירות, ולא מיובא כמודול.
     -   `play_yahtzee()`: קוראת לפונקציה להתחלת המשחק.
"""