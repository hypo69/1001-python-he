ACE:
=================
רמת קושי: 7
-----------------
המשחק "אייס" הוא משחק שבו שני שחקנים שולפים בתורם קלפים מחבילה ומנסים לצבור יותר נקודות. אס נחשב לנקודה אחת, וקלפים עם מספרים מ-2 עד 10 נחשבים לפי ערכם הנקוב, וכן נסיך, מלכה ומלך נחשבים ל-10. השחקן שצבר יותר נקודות מנצח. המשחק נמשך עד שמשחקים מספר מוגדר של סבבים.

כללי המשחק:
1. משחקים שני שחקנים.
2. השחקנים שולפים בתורם קלפים מהחבילה.
3. לכל קלף יש מספר נקודות מסוים: אס - 1, קלפים מ-2 עד 10 - לפי ערכם הנקוב, נסיך, מלכה ומלך - 10.
4. כל שחקן שואף לצבור כמה שיותר נקודות בסבב.
5. בסוף הסבב, נקודות השחקנים מושוות.
6. המשחק מורכב ממספר מוגדר של סבבים.
7. המנצח במשחק הוא השחקן שצבר את מירב הנקודות בכל הסבבים.
-----------------
אלגוריתם:
1. אתחול הנקודות של שחקנים 1 ו-2 לאפס.
2. בקשת מספר הסבבים.
3. התחלת לולאה עבור מספר הסבבים:
    3.1. שחקן 1 שולף קלף.
    3.2. הדפסת הקלף של שחקן 1 ומספר הנקודות עבור הקלף.
    3.3. הוספת הנקודות עבור הקלף לסך הנקודות של שחקן 1.
    3.4. שחקן 2 שולף קלף.
    3.5. הדפסת הקלף של שחקן 2 ומספר הנקודות עבור הקלף.
    3.6. הוספת הנקודות עבור הקלף לסך הנקודות של שחקן 2.
    3.7. אם הנקודות של שחקן 1 גדולות מהנקודות של שחקן 2, הדפסת ההודעה "שחקן 1 ניצח את הסבב".
    3.8. אם הנקודות של שחקן 2 גדולות מהנקודות של שחקן 1, הדפסת ההודעה "שחקן 2 ניצח את הסבב".
    3.9. אם הנקודות של שחקן 1 שוות לנקודות של שחקן 2, הדפסת ההודעה "תיקו בסבב זה".
4. הדפסת סך הנקודות של שחקן 1.
5. הדפסת סך הנקודות של שחקן 2.
6. אם סך הנקודות של שחקן 1 גדול מסך הנקודות של שחקן 2, הדפסת ההודעה "שחקן 1 ניצח במשחק".
7. אם סך הנקודות של שחקן 2 גדול מסך הנקודות של שחקן 1, הדפסת ההודעה "שחקן 2 ניצח במשחק".
8. אם סך הנקודות של שחקן 1 שווה לסך הנקודות של שחקן 2, הדפסת ההודעה "תיקו במשחק".
9. סיום המשחק.
-----------------

"""
import random

def calculate_card_value(card):
    """
    מחשבת את ערך הקלף. אס - 1, נסיך, מלכה, מלך - 10, השאר לפי הערך הנקוב.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        try:
            return int(card)
        except ValueError:
            return 0

def draw_card(deck):
    """
    שולפת קלף אקראי מחבילת הקלפים.
    """
    card = random.choice(deck)
    return card, calculate_card_value(card)

def play_ace_game():
    """
    הפונקציה הראשית של המשחק אייס.
    """
    player1Score = 0  # אתחול הניקוד עבור שחקן 1
    player2Score = 0  # אתחול הניקוד עבור שחקן 2
    
    # יצירת חבילת קלפים
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    
    try:
        numberOfRounds = int(input("כמה סבבים ברצונך לשחק? ")) # בקשת מספר הסבבים מהמשתמש
        if numberOfRounds <= 0:
            print("מספר הסבבים חייב להיות מספר חיובי.")
            return
    except ValueError:
        print("אנא הכנס מספר שלם עבור מספר הסבבים.")
        return

    for roundNumber in range(1, numberOfRounds + 1):
      print(f"\nסבב {roundNumber}:")

      # שחקן 1 שולף קלף
      card1, card1Value = draw_card(deck)
      print(f"שחקן 1 שלף {card1} ({card1Value} נקודות)")
      player1Score += card1Value  # עדכון הניקוד של שחקן 1

      # שחקן 2 שולף קלף
      card2, card2Value = draw_card(deck)
      print(f"שחקן 2 שלף {card2} ({card2Value} נקודות)")
      player2Score += card2Value  # עדכון הניקוד של שחקן 2

      # השוואת נקודות עבור הסבב
      if card1Value > card2Value:
          print("שחקן 1 ניצח בסבב זה")
      elif card2Value > card1Value:
          print("שחקן 2 ניצח בסבב זה")
      else:
          print("תיקו בסבב זה")
    
    # הדפסת הניקוד הסופי
    print(f"\nניקוד סופי:")
    print(f"שחקן 1: {player1Score} נקודות")
    print(f"שחקן 2: {player2Score} נקודות")

    # קביעת מנצח המשחק
    if player1Score > player2Score:
        print("שחקן 1 ניצח במשחק!")
    elif player2Score > player1Score:
        print("שחקן 2 ניצח במשחק!")
    else:
        print("תיקו במשחק!")


if __name__ == "__main__":
    # הפעלת המשחק
    # בלוק זה מבטיח שהפונקציה `play_ace_game()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    play_ace_game()
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת קלפים אקראיים.
2.  **הפונקציה `calculate_card_value(card)`**:
    -   מקבלת קלף כארגומנט.
    -   מחזירה את הערך המספרי של הקלף.
        -   עבור הקלפים 'J', 'Q', 'K' מחזירה 10.
        -   עבור הקלף 'A' מחזירה 1.
        -   עבור שאר הקלפים מחזירה את ערכם הנקוב (ממירה את המחרוזת למספר שלם).
        -   מטפלת בשגיאת ValueError אם הקלף אינו מזוהה, ומחזירה 0.
3.  **הפונקציה `draw_card(deck)`**:
    -   מקבלת חבילת קלפים כארגומנט.
    -   בוחרת קלף אקראי מהחבילה באמצעות `random.choice()`.
    -   מחזירה את הקלף ואת ערכו המספרי.
4.  **הפונקציה `play_ace_game()`**:
    -   `player1Score = 0` ו- `player2Score = 0`: מאתחלת את מונים הנקודות עבור השחקנים.
    -   `deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4`: יוצרת חבילה סטנדרטית של 52 קלפים.
    -   מבקשת מהמשתמש את מספר הסבבים ובודקת את תקינות הקלט (שיהיה מספר שלם חיובי).
    -   **הלולאה הראשית `for roundNumber in range(1, numberOfRounds + 1):`**:
        -   הלולאה רצה עבור כל סבב משחק.
        -   **קלף שחקן 1**:
            -   `card1, card1Value = draw_card(deck)`: שחקן 1 שולף קלף, וערכו נקבע.
            -   מודפסת אינפורמציה על הקלף וערכו.
            -   `player1Score += card1Value`: ערך הקלף מתווסף לסך הניקוד של שחקן 1.
        -   **קלף שחקן 2**:
            -   `card2, card2Value = draw_card(deck)`: שחקן 2 שולף קלף, וערכו נקבע.
            -   מודפסת אינפורמציה על הקלף וערכו.
            -   `player2Score += card2Value`: ערך הקלף מתווסף לסך הניקוד של שחקן 2.
        -   **השוואת נקודות**:
            -   מושווים ערכי הקלפים של השחקנים בסבב הנוכחי.
            -   מודפסת הודעה על ניצחון של אחד השחקנים או על תיקו בסבב.
    -   **הדפסת הניקוד הסופי**:
        -   מדפיסה את הניקוד הסופי של כל שחקן.
    -   **קביעת מנצח המשחק**:
        -   מושווים סך הנקודות של השחקנים.
        -   מודפסת הודעה על ניצחון של אחד השחקנים או על תיקו במשחק.
5.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_ace_game()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    -   `play_ace_game()`: קוראת לפונקציה כדי להתחיל את המשחק.
"""