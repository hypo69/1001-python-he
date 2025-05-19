import random

# פונקציה לחישוב מספר פיבונאצ'י
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# אתחול מונה הניסיונות
numberOfGuesses = 0
# יצירת מספר אקראי בין 1 ל-100
targetNumber = random.randint(1, 100)

# לולאת המשחק הראשית
while True:
    # הגדלת מספר הניסיונות
    numberOfGuesses += 1
    # חישוב מספר פיבונאצ'י עבור הניסיון הנוכחי
    fibonacciNumber = fibonacci(numberOfGuesses)
    # העלאת המספר המטרה בחזקת מספר פיבונאצ'י
    poweredNumber = targetNumber ** fibonacciNumber

    # בקשת קלט מספר מהמשתמש
    try:
        userGuess = int(input(f"ניסיון {numberOfGuesses}: אנא הכנס מספר: "))
    except ValueError:
         print("אנא הזן מספר שלם.")
         continue

    # בדיקה האם המספר נחזה נכונה
    if userGuess == poweredNumber:
        print(f"מזל טוב! ניחשת את המספר ב-{numberOfGuesses} ניסיונות!")
        break  # סיום הלולאה אם המספר נחזה
    else:
         print("אנא נסה שוב!") # הודעה למשתמש לנסות שוב