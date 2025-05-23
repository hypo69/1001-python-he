"""
NUMBER RANDOM NUMBER GAME:
=================
רמת קושי: 6
-----------------
המשחק "NUMBER RANDOM NUMBER GAME" הוא משחק שבו השחקן מנסה לנחש מספר אקראי שנוצר על ידי המחשב. בניגוד למשחקים אחרים שבהם ניתנים מספר ניסיונות, כאן לשחקן יש רק ניסיון אחד לכל משחק. נקודות מוענקות או מופחתות בהתאם למידת הקרבה של ניחוש השחקן למספר שנבחר. כמו כן, קיים סיכוי לקבל ג'קפוט, שמכפיל את כמות הנקודות. מטרת המשחק היא לצבור 500 נקודות.

חוקי המשחק:
1. המחשב מייצר מספר אקראי בטווח שבין 1 ל-100.
2. השחקן מנחש ניחוש אחד.
3. נקודות מוענקות או מופחתות בהתאם למידת הקרבה של ניחוש השחקן למספר שנבחר:
    - הפרש 0: +100 נקודות (ג'קפוט, הנקודות מוכפלות)
    - הפרש מ-1 עד 5: +50 נקודות
    - הפרש מ-6 עד 10: +25 נקודות
    - הפרש מ-11 עד 20: -25 נקודות
    - הפרש גדול מ-20: -50 נקודות
4. השחקן זוכה אם הוא צובר 500 נקודות.

-----------------
אלגוריתם:
1. להגדיר את כמות הנקודות ההתחלתית ל-0.
2. להתחיל את לולאת המשחק:
    2.1 לייצר מספר אקראי מ-1 עד 100.
    2.2 לבקש מהשחקן ניחוש למספר.
    2.3 לחשב את ההפרש בין המספר שנבחר לניחוש של השחקן.
    2.4 לקבוע את כמות הנקודות שהשחקן יקבל בהתאם להפרש.
    2.5 אם השחקן ניחש את המספר, להכפיל את כמות הנקודות.
    2.6 להוסיף/להפחית נקודות מסך הנקודות הכולל.
    2.7 אם כמות הנקודות הכוללת היא 500 או יותר, להדפיס הודעת ניצחון ולסיים את המשחק.
    2.8 להדפיס את כמות הנקודות הנוכחית.
3. לעבור לשלב 2.
4. אם המשחק הסתיים, לצאת מהלולאה.
-----------------
"""

import random

# אתחול הסך הכולל של הנקודות
totalScore = 0

# לולאת המשחק
while True:
    # מייצרים מספר אקראי מ-1 עד 100
    randomNumber = random.randint(1, 100)
    
    # מבקשים מהשחקן לנחש את המספר
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue
    
    # מחשבים את ההפרש בין המספר שנבחר לניחוש של השחקן
    difference = abs(randomNumber - guess)
    
    # קובעים את כמות הנקודות בהתאם להפרש
    if difference == 0:
        points = 100 # השחקן ניחש את המספר
    elif difference <= 5:
        points = 50 # הפרש מ-1 עד 5
    elif difference <= 10:
        points = 25 # הפרש מ-6 עד 10
    elif difference <= 20:
        points = -25 # הפרש מ-11 עד 20
    else:
        points = -50 # הפרש גדול מ-20
    
    # אם השחקן ניחש את המספר, מכפילים את כמות הנקודות
    if difference == 0:
        points *= 2
    
    # מוסיפים/מפחיתים נקודות מסך הנקודות הכולל
    totalScore += points
    
    # בודקים אם השחקן ניצח
    if totalScore >= 500:
        print(f"You Win! Total Score: {totalScore}")
        break
    
    # מדפיסים את כמות הנקודות הנוכחית
    print(f"Current Score: {totalScore}")
```