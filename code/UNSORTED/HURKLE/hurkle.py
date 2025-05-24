HURKLE:
=================
רמת מורכבות: 5
-----------------
המשחק "HURKLE" הוא משחק ניחוש מיקום של ה-"HURKLE", המוסתר על גבי מפה בגודל 10x10. השחקן מבצע מהלכים על ידי הזנת קואורדינטות, ומקבל רמזים לגבי מיקומו של ה-HURKLE ביחס לניחושיו. מטרת המשחק היא למצוא את ה-HURKLE במספר מהלכים מינימלי.
כללי המשחק:
1. ה-HURKLE מוסתר על גבי מפה בגודל 10x10. קואורדינטות ה-HURKLE נבחרות באופן אקראי.
2. השחקן מבצע מהלכים על ידי הזנת קואורדינטות x ו-y.
3. לאחר כל מהלך, השחקן מקבל רמז המציין את הכיוון (צפון, דרום, מזרח, מערב, צפון-מזרח, דרום-מזרח, צפון-מערב, דרום-מערב) מהקואורדינטה שהוזנה על ידי השחקן ועד למיקום ה-HURKLE.
4. המשחק ממשיך עד שהשחקן מנחש את מיקום ה-HURKLE.
-----------------
אלגוריתם:
1. לייצר קואורדינטות אקראיות עבור ה-HURKLE (X ו-Y) בטווח שבין 1 ל-10.
2. לאפס את מונה המהלכים.
3. להתחיל את לולאת המשחק:
    3.1. להגדיל את מונה המהלכים ב-1.
    3.2. לבקש מהשחקן להזין קואורדינטות X ו-Y.
    3.3. אם הקואורדינטות שהוזנו שוות לקואורדינטות ה-HURKLE, להדפיס הודעת ניצחון ואת מספר המהלכים. לסיים את המשחק.
    3.4. אחרת, לקבוע את הכיוון מהקואורדינטות שהוזנו ועד לקואורדינטות ה-HURKLE ולהדפיס את הרמז (הכיוון).
4. לחזור על לולאת המשחק עד שה-HURKLE יימצא.
-----------------

```python
import random

# פונקציה לקביעת כיוון ה-HURKLE
def get_direction(user_x, user_y, hurkle_x, hurkle_y):
    """
    קובעת את הכיוון מהקואורדינטות של המשתמש לקואורדינטות של ה-HURKLE.
    ארגומנטים:
        user_x (int): קואורדינטת X שהוזנה על ידי המשתמש.
        user_y (int): קואורדינטת Y שהוזנה על ידי המשתמש.
        hurkle_x (int): קואורדינטת X של ה-HURKLE.
        hurkle_y (int): קואורדינטת Y של ה-HURKLE.
    החזרות:
        str: מחרוזת המייצגת את הכיוון.
    """
    if user_x < hurkle_x and user_y < hurkle_y:
        return "צפון-מזרח"
    elif user_x < hurkle_x and user_y > hurkle_y:
        return "דרום-מזרח"
    elif user_x > hurkle_x and user_y < hurkle_y:
        return "צפון-מערב"
    elif user_x > hurkle_x and user_y > hurkle_y:
        return "דרום-מערב"
    elif user_x < hurkle_x:
        return "מזרח"
    elif user_x > hurkle_x:
        return "מערב"
    elif user_y < hurkle_y:
        return "צפון"
    else:
        return "דרום"

# מייצרים קואורדינטות אקראיות עבור ה-HURKLE
hurkle_x = random.randint(1, 10)
hurkle_y = random.randint(1, 10)

# מאתחלים את מונה המהלכים
numberOfGuesses = 0

# לולאת המשחק הראשית
while True:
    # מגדילים את מונה המהלכים
    numberOfGuesses += 1

    # מבקשים קלט קואורדינטות מהמשתמש
    try:
        user_x = int(input("הזן קואורדינטת X (1-10): "))
        user_y = int(input("הזן קואורדינטת Y (1-10): "))
    except ValueError:
        print("אנא הזן מספרים שלמים.")
        continue

    # בודקים אם המשתמש ניחש את מיקום ה-HURKLE
    if user_x == hurkle_x and user_y == hurkle_y:
        print(f"מזל טוב! מצאת את ה-HURKLE ב-{numberOfGuesses} מהלכים!")
        break

    # מחשבים ומדפיסים את הכיוון
    direction = get_direction(user_x, user_y, hurkle_x, hurkle_y)
    print(direction)