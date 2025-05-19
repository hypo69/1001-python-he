<YAHTZE>:
=================
רמת קושי: 6
-----------------
המשחק "יאצ'י" הוא משחק קוביות שבו שחקן מטיל חמש קוביות ומנסה לצבור נקודות על ידי יצירת צירופים כגון זוגות, שלישיות, פול האוס, סטרייטים וכדומה.
לשחקן יש שלוש ניסיונות הטלה עבור כל צירוף, עם אפשרות להשאיר קוביות מסוימות ולהטיל מחדש את הנותרות.
המשחק מורכב מ-13 סבבים, כל סבב מוערך לפי אחד הצירופים. בסוף המשחק הנקודות מסוכמות.
כללי המשחק:
1. בכל סבב השחקן מטיל 5 קוביות.
2. לאחר ההטלה הראשונה, השחקן רשאי להשאיר אילו קוביות שירצה ולהטיל מחדש את הנותרות.
3. לאחר ההטלה השנייה, השחקן רשאי שוב להשאיר אילו קוביות שירצה ולהטיל מחדש את הנותרות.
4. לאחר ההטלה השלישית, השחקן חייב לבחור אחת מהקטגוריות הזמינות לרישום התוצאה.
5. הקטגוריות כוללות:
   - סכום כל האחדות, השתיים, השלוש, הארבע, החמש והשש.
   - צירופים: 3 זהים (שלישייה), 4 זהים (רביעייה), פול האוס, סטרייט קטן, סטרייט גדול, יאצ'י (כל 5 זהים), צ'אנס.
6. כל קטגוריה יכולה לשמש רק פעם אחת במהלך המשחק.
7. המשחק מורכב מ-13 סבבים, אחד עבור כל קטגוריה.
8. לאחר 13 סבבים הנקודות מסוכמות.
-----------------
אלגוריתם:
1. לאתחל מערך קטגוריות, המייצגות את הצירופים לרישום נקודות, ומערך לאחסון נקודות.
2. התחלת לולאה של 13 סבבים:
   2.1. לאתחל מערך הטלות, המייצג 5 קוביות משחק.
   2.2. התחלת לולאה של 3 ניסיונות הטלה:
        2.2.1. ליצור 5 מספרים אקראיים (מ-1 עד 6) עבור מערך ההטלות.
        2.2.2. להציג את תוצאות ההטלה על המסך.
        2.2.3. אם זה לא הניסיון השלישי, לבקש מהשחקן אילו קוביות הוא רוצה להטיל מחדש.
        2.2.4. להטיל מחדש את הקוביות שנבחרו (תוך שמירה על אלו שלא הוטלו מחדש).
   2.3. להציג רשימת קטגוריות זמינות שעדיין לא נעשה בהן שימוש.
   2.4. לבקש מהשחקן בחירת קטגוריה.
   2.5. לחשב את כמות הנקודות עבור הקטגוריה שנבחרה, בהתאם להטלת הקוביות.
   2.6. לרשום את כמות הנקודות במערך הנקודות עבור הקטגוריה המתאימה.
3. לחשב את סך כל הנקודות.
4. להציג טבלת נקודות לפי קטגוריות ואת הסכום הכולל.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["אתחול המשחק: <br><code><b>categories = [...]<br>scores = [...]<br>used_categories = []</b></code>"]
    InitializeGame --> RoundLoopStart{"התחלת לולאה: 13 סבבים"}
    RoundLoopStart -- כן --> InitializeDice["אתחול הטלות: <code><b>dice = []</b></code>"]
    InitializeDice --> RollLoopStart{"התחלת לולאה: 3 ניסיונות הטלה"}
    RollLoopStart -- כן --> RollDice["הטלת קוביות: <code><b>dice = random(1-6, 5)</b></code>"]
    RollDice --> OutputDice["הצגת תוצאת הטלה: <code><b>dice</b></code>"]
    OutputDice --> CheckRollAttempt{"בדיקה: <code><b>rollAttempt < 3?</b></code>"}
    CheckRollAttempt -- כן --> InputKeepDice["בקשת אילו קוביות להשאיר: <code><b>keep_indices</b></code>"]
    InputKeepDice --> ReRollDice["להטיל מחדש את הקוביות שנבחרו"]
    ReRollDice --> RollLoopStart
    CheckRollAttempt -- לא --> OutputAvailableCategories["הצגת קטגוריות זמינות"]
     OutputAvailableCategories--> InputCategoryChoice["בחירת קטגוריה: <code><b>category</b></code>"]
     InputCategoryChoice --> CalculateScore["ספירת נקודות עבור קטגוריה: <code><b>score = calculateScore(dice, category)</b></code>"]
    CalculateScore --> UpdateScorecard["לרשום נקודות בטבלה: <code><b>scores[category] = score<br>used_categories.add(category)</b></code>"]
     UpdateScorecard --> RoundLoopStart
      RoundLoopStart -- לא --> CalculateTotalScore["סיכום נקודות: <code><b>totalScore = sum(scores)</b></code>"]
      CalculateTotalScore --> OutputScorecard["הצגת טבלת נקודות: <code><b>scores, totalScore</b></code>"]
       OutputScorecard--> End["סוף"]
```
מקרא:
    Start - התחלת התוכנית.
    InitializeGame - אתחול משתנים: מערכי קטגוריות, נקודות, קטגוריות בשימוש.
    RoundLoopStart - התחלת לולאה המבוצעת 13 פעמים (מספר הסבבים במשחק).
    InitializeDice - אתחול מערך להטלות קוביות.
    RollLoopStart - התחלת לולאה המבוצעת 3 פעמים (המספר המקסימלי של הטלות בסבב).
    RollDice - נוצרת הטלה אקראית של 5 קוביות עם ערכים מ-1 עד 6.
    OutputDice - מציג את תוצאות ההטלה הנוכחיות.
    CheckRollAttempt - בדיקה האם מספר ההטלות הגיע ל-3, המספר המקסימלי של הטלות בסבב.
    InputKeepDice - בקשת המשתמש אילו קוביות להשאיר.
    ReRollDice - הטלה מחדש של הקוביות שלא נבחרו.
    OutputAvailableCategories - הצגת רשימת הקטגוריות הזמינות.
    InputCategoryChoice - בקשת המשתמש לבחירת קטגוריה.
    CalculateScore - ספירת נקודות עבור הקטגוריה שנבחרה בהתאם להטלה.
    UpdateScorecard - רישום הנקודות בטבלה והוספת הקטגוריה שנבחרה לרשימת הקטגוריות בשימוש.
    CalculateTotalScore - סיכום נקודות מכל הקטגוריות.
    OutputScorecard - הצגת טבלת נקודות לפי קטגוריות והסכום הכולל.
    End - סיום התוכנית.
```
import random

def roll_dice():
    """מטיל 5 קוביות ומחזיר את התוצאות."""
    return [random.randint(1, 6) for _ in range(5)]

def calculate_score(dice, category):
    """מחשב את הנקודות עבור הקטגוריה שנבחרה."""
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
    """פונקציה ראשית למשחק יאצ'י."""
    categories = [
      '1', '2', '3', '4', '5', '6',
      '3 of a kind', '4 of a kind',
      'full house', 'small straight', 'large straight',
      'yahtzee', 'chance'
    ]
    scores = {category: None for category in categories}  # מילון לאחסון נקודות
    used_categories = set()  # קבוצה של קטגוריות בשימוש

    for round_num in range(1, 14):
        print(f"\n----- סבב {round_num} -----")
        dice = roll_dice()  # הטלת קוביות
        print(f"הטלה ראשונה: {dice}")

        for roll_attempt in range(1, 3): # מתן 3 ניסיונות
            keep_dice_str = input(f"ניסיון {roll_attempt}, אילו קוביות להשאיר (הזן מספרים ברווחים, מ-1 עד 5, 0 = להטיל מחדש את כולם, n = לא להטיל מחדש כלום)? ")
            
            if keep_dice_str.lower() == 'n':
              break
            if keep_dice_str == '0':
              dice = roll_dice()
              print(f"הטלה חדשה: {dice}")
              continue
            try:
                keep_indices = [int(i) - 1 for i in keep_dice_str.split()] # קבלת רשימת האינדקסים של הקוביות שיש להשאיר
                if not all(0 <= index < 5 for index in keep_indices):
                  print("אינדקסים לא תקינים, נסה שוב.") # הודעה למשתמש
                  continue
                new_dice = [] # רשימה חדשה של קוביות
                for i in range(5): # מעבר על כל הקוביות
                  if i not in keep_indices: # אם את הקוביה אין צורך להשאיר, אז מטילים אותה מחדש
                    new_dice.append(random.randint(1, 6))
                  else: # אחרת, מוסיפים את הקוביה לרשימה החדשה מהרשימה הישנה
                    new_dice.append(dice[i])
                dice = new_dice
                print(f"הטלה חדשה: {dice}") # הצגת תוצאות ההטלה החדשה
            except ValueError:
                print("קלט לא תקין, נסה שוב.") # הודעה למשתמש
        
        available_categories = [cat for cat in categories if cat not in used_categories] # רשימת קטגוריות זמינות
        print("קטגוריות זמינות:")
        for i, cat in enumerate(available_categories, start=1):
            print(f"{i}. {cat}")
        
        while True:
            try:
                choice_index = int(input("בחר מספר קטגוריה לרישום נקודות: "))-1 # בקשת בחירה
                if  0 <= choice_index < len(available_categories) :
                    category_choice = available_categories[choice_index]
                    break
                else:
                    print('מספר קטגוריה לא תקין, נסה שוב.') # הודעה למשתמש
            except ValueError:
                print('קלט לא תקין, נסה שוב.') # הודעה למשתמש
        
        score = calculate_score(dice, category_choice) # חישוב נקודות
        scores[category_choice] = score # רישום נקודות
        used_categories.add(category_choice) # הוספת הקטגוריה לרשימת הקטגוריות בשימוש
        print(f"נקודות עבור קטגוריה {category_choice}: {score}")

    # הצגת טבלת נקודות
    print("\n----- טבלת נקודות סופית -----")
    for category, score in scores.items():
      print(f"{category}: {score if score is not None else 0}")

    total_score = sum(score if score is not None else 0 for score in scores.values())
    print(f"סה\"כ נקודות: {total_score}") # הצגת סך כל הנקודות

if __name__ == "__main__":
    play_yahtzee()
```
"""
הסבר הקוד:
1. **ייבוא מודול `random`**:
   -  `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים.

2. **פונקציה `roll_dice()`**:
    -   `def roll_dice():`: מגדיר פונקציה המדמה הטלה של חמש קוביות משחק.
    -  `return [random.randint(1, 6) for _ in range(5)]`: יוצר רשימה של 5 מספרים אקראיים בטווח מ-1 עד 6, המייצגים את תוצאות הטלת הקוביות.

3. **פונקציה `calculate_score(dice, category)`**:
    - `def calculate_score(dice, category):`: מגדיר פונקציה לחישוב נקודות עבור הקטגוריה שנבחרה.
    -  `counts = {}`: מאתחל מילון ריק לספירת כמות כל ערך על הקוביות.
    -  `for die in dice: counts[die] = counts.get(die, 0) + 1`: סופר את כמות כל ערך על הקוביות.
    -  בלוקים מותנים `if category in [...]`: בודק איזו קטגוריה נבחרה על ידי השחקן ומחשב את הנקודות.
        -  עבור קטגוריות מ-1 עד 6 מסכם רק את הקוביות התואמות את הקטגוריה שנבחרה.
        -  עבור "3 of a kind" ו-"4 of a kind" בודק נוכחות של 3 או 4 ערכים זהים ומחזיר את סכום כל הקוביות או 0.
        -  עבור "full house" בודק נוכחות של זוג ושלישייה ומחזיר 25 נקודות, אחרת 0.
        -  עבור "small straight" בודק נוכחות של 4 מספרים עוקבים ומחזיר 30 נקודות, אחרת 0.
        -   עבור "large straight" בודק נוכחות של 5 מספרים עוקבים ומחזיר 40 נקודות, אחרת 0.
        -   עבור "yahtzee" בודק נוכחות של 5 ערכים זהים ומחזיר 50 נקודות, אחרת 0.
        -   עבור "chance" מחזיר את סכום כל הקוביות.

4. **פונקציה `play_yahtzee()`**:
    -  `def play_yahtzee():`: מגדיר את פונקציית המשחק הראשית יאצ'י.
    - `categories = [...]`: מגדיר רשימה של כל הקטגוריות האפשריות.
    - `scores = {category: None for category in categories}`: יוצר מילון לאחסון הנקודות שנצברו עבור כל קטגוריה, ערך התחלתי None.
    - `used_categories = set()`: יוצר קבוצה לאחסון הקטגוריות ששימשו.
    - `for round_num in range(1, 14):`: לולאת המשחק הראשית. בסך הכל 13 סבבים.
        -  `dice = roll_dice()`: מטיל 5 קוביות, התוצאה נשמרת במשתנה `dice`.
        -  `print(f"הטלה ראשונה: {dice}")`: מציג את תוצאת ההטלה הראשונה על המסך.
        -  `for roll_attempt in range(1, 3):`: לולאה להטלות נוספות (עד פעמיים).
            -  `keep_dice_str = input(...)`: מבקש מהשחקן אילו קוביות צריך להשאיר, מוזנים אינדקסים (1-5) ברווחים, 0 - להטיל מחדש את כולם, n - לא להטיל מחדש.
            - `if keep_dice_str.lower() == 'n': break`: אם השחקן מזין `n`, אז לולאת ההטלות מסתיימת.
            - `if keep_dice_str == '0':`: אם השחקן מזין `0`, אז כל הקוביות מוטלות מחדש.
            - `try... except ValueError`: בלוק try-except לטיפול בשגיאות קלט.
            - `keep_indices = [int(i) - 1 for i in keep_dice_str.split()]`: ממיר את האינדקסים המוזנים לרשימת אינדקסים להשארת קוביות.
            -  `new_dice = []` נוצר מערך ריק לקוביות חדשות.
            -   `for i in range(5):`: לולאה על כל הקוביות.
            -   `if i not in keep_indices:`: אם את הקוביה אין צורך להשאיר, אז היא מוטלת מחדש.
            -  `else:`: אם את הקוביה צריך להשאיר, אז היא מוספת לרשימה החדשה מהרשימה הישנה.
            - `dice = new_dice`: מעדכן את מערך הקוביות.
            - `print(f"הטלה חדשה: {dice}")`: מציג את תוצאות ההטלה החדשה על המסך.
        - `available_categories = [cat for cat in categories if cat not in used_categories]`: נוצרת רשימה של קטגוריות זמינות.
        - `print("קטגוריות זמינות:")` ו- `for ...`: רשימת הקטגוריות הזמינות מוצגת על המסך.
        - `while True:`: לולאה לבחירת קטגוריה על ידי השחקן.
             - `try... except ValueError:`: בלוק try-except לטיפול בשגיאות קלט.
             - `choice_index = int(input(...))-1`: מבקש הזנת מספר הקטגוריה שנבחרה.
             -  `if  0 <= choice_index < len(available_categories) :`: בדיקה שהאינדקס שנבחר קיים במערך הקטגוריות הזמינות.
             - `category_choice = available_categories[choice_index]`: שומרים את הקטגוריה שנבחרה.
             - `break`: מסיימים את הלולאה אם הקלט תקין.
        - `score = calculate_score(dice, category_choice)`: מחשב את הנקודות עבור הקטגוריה שנבחרה.
        - `scores[category_choice] = score`: שומר את הנקודות במילון `scores`.
        - `used_categories.add(category_choice)`: מוסיף את הקטגוריה שנבחרה לקבוצה `used_categories`.
        - `print(f"נקודות עבור קטגוריה {category_choice}: {score}")`: מציג את הנקודות שנצברו עבור הקטגוריה שנבחרה.
    -  `print("\n----- טבלת נקודות סופית -----")` ו- `for ...`: הצגת טבלת הנקודות הסופית.
    -  `total_score = sum(score if score is not None else 0 for score in scores.values())`: ספירת סך כל הנקודות.
    - `print(f"סה\"כ נקודות: {total_score}")`: הצגת סך כל הנקודות.

5. **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_yahtzee()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    - `play_yahtzee()`: קורא לפונקציה כדי להתחיל את המשחק.
"""