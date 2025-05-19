"""
<BLKJAK>:
=================
רמת קושי: 7
-----------------
בלאקג'ק הוא משחק קלפים שבו השחקן מתחרה נגד הדילר. מטרת המשחק היא לצבור 21 נקודות או כמה שיותר קרוב ל-21, מבלי לחרוג מערך זה. קלפים עם מספרים מקנים נקודות לפי ערכם הנקוב, ג'ק, קווין וקינג - 10 נקודות, ואילו אס - 1 או 11 נקודות, בהתאם למצב. השחקן משחק נגד הדילר. השחקן יכול לבקש קלף נוסף או לעצור. לאחר שהשחקן עצר, הדילר לוקח קלפים עד שסכום הקלפים שלו עולה על 16. השחקן מנצח אם סכום הקלפים שלו גבוה מזה של הדילר, אך נמוך או שווה ל-21.

חוקי המשחק:
1.  השחקן והדילר מקבלים שני קלפים כל אחד. אחד מקלפי הדילר גלוי.
2.  השחקן מסתכל על קלפיו ומחליט אם ברצונו לקחת קלף נוסף (HIT) או לעצור (STAND).
3.  אם סכום קלפי השחקן גבוה מ-21, הוא מפסיד.
4.  כאשר השחקן עוצר, הדילר מתחיל לקחת קלפים עד שסכום קלפיו עולה על 16.
5.  אם סכום קלפי הדילר גבוה מ-21, הוא מפסיד, והשחקן מנצח.
6.  אם סכום קלפי הדילר אינו עולה על 21, מושווים סכומי קלפי השחקן והדילר. מנצח מי שסכומו קרוב יותר ל-21, אך אינו גבוה מ-21.
7.  במקרה של שוויון בנקודות, מוכרז תיקו (PUSH).
-----------------
אלגוריתם:
1. אתחול חבילה: יצירת חבילת קלפים של 52 קלפים. לכל קלף יש ערך מ-1 עד 10 (ג'ק, קווין, קינג = 10, אס = 1 או 11).
2. ערבוב החבילה.
3. חלוקת שני קלפים לכל אחד, לשחקן ולדילר. קלף אחד של הדילר גלוי, השני חבוי.
4. הצגת קלפי השחקן והקלף הגלוי של הדילר על המסך.
5. תור השחקן:
   5.1. שאילת השחקן אם ברצונו לקחת קלף נוסף (HIT) או לעצור (STAND).
   5.2. אם השחקן בוחר HIT, לתת לו קלף נוסף ולעבור לשלב 5.3.
   5.3. אם סכום קלפי השחקן גבוה מ-21, השחקן מפסיד. לעבור לשלב 7.
   5.4. אם השחקן בוחר STAND, לעבור לשלב 6.
6. תור הדילר:
   6.1. כל עוד סכום קלפי הדילר קטן או שווה ל-16, לתת לו קלף נוסף.
   6.2. אם סכום קלפי הדילר גבוה מ-21, הדילר מפסיד, השחקן מנצח. לעבור לשלב 7.
7. קביעת מנצח:
   7.1. השוואת סכומי קלפי השחקן והדילר.
   7.2. אם סכום קלפי השחקן גבוה מסכום קלפי הדילר ואינו גבוה מ-21, השחקן מנצח.
   7.3. אם סכום קלפי הדילר גבוה מסכום קלפי השחקן ואינו גבוה מ-21, הדילר מנצח.
   7.4. אם הסכומים שווים, תיקו.
8. הצגת תוצאת המשחק.
9. סוף המשחק
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeDeck["<p align='left'>אתחול חבילה: 
    <code><b>deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4</b></code></p>"]
    InitializeDeck --> ShuffleDeck["ערבוב חבילה: <code><b>random.shuffle(deck)</b></code>"]
    ShuffleDeck --> DealInitialCards["<p align='left'>חלוקת קלפים ראשונית:
    <code><b>
    playerHand = [deal_card(deck), deal_card(deck)]
    dealerHand = [deal_card(deck), deal_card(deck)]
    </b></code></p>"]
    DealInitialCards --> ShowHands["<p align='left'>הצגת קלפי השחקן וקלף גלוי אחד של הדילר</p>"]
    ShowHands --> PlayerTurnStart{"התחלת תור השחקן"}
    PlayerTurnStart --> PlayerActionChoice{"קלט פעולת שחקן: HIT או STAND"}
    PlayerActionChoice -- HIT --> PlayerHit["<p align='left'>שחקן לוקח קלף: <code><b>playerHand.append(deal_card(deck))</b></code></p>"]
    PlayerHit --> CalculatePlayerHandValue["<p align='left'>חישוב סכום קלפי השחקן: <code><b>player_value = calculate_hand_value(playerHand)</b></code></p>"]
    CalculatePlayerHandValue --> CheckPlayerBust{"<p align='left'>בדיקה: <code><b>player_value > 21?</b></code></p>"}
    CheckPlayerBust -- כן --> PlayerBust["<p align='left'>השחקן הפסיד: <code><b>print('Игрок проиграл!')</b></code></p>"]
    PlayerBust --> End["סיום"]
    CheckPlayerBust -- לא --> PlayerTurnStart
    PlayerActionChoice -- STAND --> DealerTurnStart{"התחלת תור הדילר"}
    DealerTurnStart --> DealerHit{"<p align='left'>דילר לוקח קלף כל עוד <code><b>dealer_value <= 16</b></code></p>"}
    DealerHit --> CalculateDealerHandValue["<p align='left'>חישוב סכום קלפי הדילר: <code><b>dealer_value = calculate_hand_value(dealerHand)</b></code></p>"]
    CalculateDealerHandValue --> CheckDealerBust{"<p align='left'>בדיקה: <code><b>dealer_value > 21?</b></code></p>"}
    CheckDealerBust -- כן --> DealerBust["<p align='left'>הדילר הפסיד: <code><b>print('Дилер проиграл!')</b></code></p>"]
    DealerBust --> End
    CheckDealerBust -- לא --> DetermineWinner["<p align='left'>קביעת מנצח והצגת תוצאה</p>"]
    DetermineWinner --> End
    

```
**מקרא**
    Start - התחלת המשחק.
    InitializeDeck - אתחול חבילה, יצירת רשימת קלפים (ערכים מספריים ואס, חוזרים 4 פעמים עבור כל סוג קלף).
    ShuffleDeck - ערבוב החבילה בסדר אקראי.
    DealInitialCards - חלוקת קלפים ראשוניים לשחקן ולדילר (שני קלפים לכל אחד).
    ShowHands - הצגת קלפי השחקן וקלף גלוי אחד של הדילר.
    PlayerTurnStart - התחלת תור השחקן.
    PlayerActionChoice - בקשת פעולת השחקן: HIT (לקחת קלף) או STAND (לעצור).
    PlayerHit - השחקן לוקח קלף נוסף מהחבילה.
    CalculatePlayerHandValue - חישוב הסכום הכולל של נקודות קלפי השחקן.
    CheckPlayerBust - בדיקה האם סכום נקודות השחקן עלה על 21.
    PlayerBust - הצגת הודעה על הפסד השחקן, אם סכום הנקודות גבוה מ-21.
    DealerTurnStart - התחלת תור הדילר.
    DealerHit - הדילר לוקח קלף כל עוד סכום נקודות קלפיו אינו עולה על 16.
    CalculateDealerHandValue - חישוב סכום נקודות קלפי הדילר.
    CheckDealerBust - בדיקה האם סכום נקודות הדילר עלה על 21.
    DealerBust - הצגת הודעה על הפסד הדילר, אם סכום הנקודות גבוה מ-21.
    DetermineWinner - קביעת מנצח על ידי השוואת נקודות השחקן והדילר, הצגת התוצאה.
    End - סיום המשחק.
"""

import random

def deal_card(deck):
    """מוציא קלף מהחבילה."""
    return deck.pop()

def calculate_hand_value(hand):
    """מחשב את ערך היד."""
    ace_count = hand.count(11) # סופר את כמות האסים (11)
    total = sum(hand) # סופר את הסכום הכולל של הנקודות

    # אם הסכום הכולל גבוה מ-21 ויש אס שניתן לספור כ-1
    while total > 21 and ace_count > 0:
        total -= 10 #  הופך אס מ-11 ל-1
        ace_count -= 1
    return total


def display_cards(player_hand, dealer_hand, show_dealer_full=False):
  """מציג את קלפי השחקן והדילר."""
  print("\nקלפי הדילר:")
  if show_dealer_full:
    print(" ".join(map(str, dealer_hand)), f"סכום: {calculate_hand_value(dealer_hand)}")
  else:
    print("<קלף חבוי> ", dealer_hand[1]) # מציג את הקלף הראשון של הדילר, השני מוסתר
  
  print("קלפי השחקן:", " ".join(map(str, player_hand)), f"סכום: {calculate_hand_value(player_hand)}")
 
def play_blackjack():
    """מפעיל את משחק הבלאקג'ק."""
    # יצירת חבילת קלפים של 52 קלפים: ערכים מספריים (2-10) ואס (11)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 
    random.shuffle(deck) # מערבב את החבילה

    # מחלק קלפים לשחקן ולדילר (2 קלפים לכל אחד)
    player_hand = [deal_card(deck), deal_card(deck)] 
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # מציג את הקלפים (קלף אחד של הדילר מוסתר)
    display_cards(player_hand, dealer_hand)
    
    # תור השחקן
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value == 21: # אם לשחקן יש מיד 21
          print("בלאקג'ק! ניצחת!")
          return
        
        if player_value > 21: # אם השחקן הפסיד
          print("ברסט (עברת את ה-21)! הפסדת!")
          return

        action = input("האם ברצונך לקחת קלף נוסף? (HIT/STAND): ").upper()
        if action == "HIT":
            player_hand.append(deal_card(deck)) # נותן קלף לשחקן
            display_cards(player_hand, dealer_hand)
        elif action == "STAND":
            break # עובר לתור הדילר
        else:
            print("קלט לא תקין. אנא הכנס HIT או STAND.")

    # תור הדילר
    print("\nתור הדילר:")
    while calculate_hand_value(dealer_hand) <= 16:
        dealer_hand.append(deal_card(deck)) # הדילר לוקח קלף
        
    display_cards(player_hand, dealer_hand, True) # מציג את כל קלפי הדילר

    player_value = calculate_hand_value(player_hand) # סכום השחקן
    dealer_value = calculate_hand_value(dealer_hand) # סכום הדילר

    # בדיקת תנאי הניצחון
    if dealer_value > 21: # אם לדילר יש ברסט (מעל 21)
      print("הדילר עבר את ה-21! ניצחת!")
    elif player_value > dealer_value or dealer_value > 21: # אם לשחקן יש יותר נקודות (והוא לא עבר)
      print("ניצחת!")
    elif dealer_value > player_value : # אם לדילר יש יותר נקודות (והוא לא עבר)
      print("הפסדת!")
    else:
        print("תיקו!") # תיקו


if __name__ == "__main__":
    play_blackjack() # הפעלת המשחק

"""
הסבר קוד:
1.  **ייבוא מודול `random`**:
   -  `import random`: מייבא את מודול `random`, המשמש ליצירת סדר קלפים אקראי.
2.  **פונקציה `deal_card(deck)`**:
    -  `def deal_card(deck):`: מגדירה פונקציה לשליפת קלף מהחבילה.
    -  `return deck.pop()`: מסירה ומחזירה את הקלף האחרון מהחבילה.
3.  **פונקציה `calculate_hand_value(hand)`**:
    -   `def calculate_hand_value(hand):`: מגדירה פונקציה לחישוב סכום נקודות הקלפים.
    -   `ace_count = hand.count(11)`: סופרת את כמות האסים ביד (אס = 11).
    -   `total = sum(hand)`: מחשבת את הסכום הכולל של נקודות הקלפים.
    -   `while total > 21 and ace_count > 0`: אם הסכום הכולל גבוה מ-21 ויש אסים.
    -   `total -= 10`:  משנה את ערך האס מ-11 ל-1.
    -   `ace_count -= 1`: מקטין את מספר האסים שניתן לשנות את ערכם.
    -   `return total`: מחזירה את הסכום הכולל של הנקודות.
4.  **פונקציה `display_cards(player_hand, dealer_hand, show_dealer_full=False)`**:
    -   `def display_cards(player_hand, dealer_hand, show_dealer_full=False):`: מגדירה פונקציה להצגת הקלפים.
    -  `show_dealer_full=False`: מציג רק קלף 1 של הדילר.
    -  אם `show_dealer_full=True`: מציג את כל קלפי הדילר.
5.  **פונקציה `play_blackjack()`**:
    -  `def play_blackjack():`: מגדירה פונקציה שמכילה את לוגיקת המשחק הראשית.
    -  `deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4`: יוצרת חבילה של 52 קלפים (ערכים מספריים ואס).
    -  `random.shuffle(deck)`: מערבבת את החבילה.
    -  `player_hand = [deal_card(deck), deal_card(deck)]`: מחלקת 2 קלפים לשחקן.
    -  `dealer_hand = [deal_card(deck), deal_card(deck)]`: מחלקת 2 קלפים לדילר.
    -  `display_cards(player_hand, dealer_hand)`: מציגה את הקלפים הראשוניים.
    -   **תור השחקן**:
         -   `while True:`: לולאה ראשית לתור השחקן.
        - `player_value = calculate_hand_value(player_hand)`: מחשב את סכום השחקן.
        - `if player_value == 21:`: בדיקה לבלאקג'ק.
        - `if player_value > 21:`: בדיקה להפסד השחקן (ברסט).
         -   `action = input("האם ברצונך לקחת קלף נוסף? (HIT/STAND): ").upper()`: מבקשת פעולת שחקן (HIT או STAND).
         -   `if action == "HIT":`: אם השחקן בוחר HIT:
            -   `player_hand.append(deal_card(deck))`: מוסיף קלף ליד השחקן.
            -    `display_cards(player_hand, dealer_hand)`: מציג את הקלפים.
         -   `elif action == "STAND":`: אם השחקן בוחר STAND, עובר לתור הדילר.
    -   **תור הדילר**:
        -  `while calculate_hand_value(dealer_hand) <= 16:`: הדילר לוקח קלף כל עוד הסכום קטן מ-16.
         -    `dealer_hand.append(deal_card(deck))`: נותן קלף לדילר.
        -  `display_cards(player_hand, dealer_hand, True)`: מציג את קלפי הדילר.
     -    **קביעת מנצח**:
         - `player_value = calculate_hand_value(player_hand)`: מחשב את סכום השחקן.
         -`dealer_value = calculate_hand_value(dealer_hand)`: מחשב את סכום הדילר.
        - `if dealer_value > 21: `: בדיקה לברסט אצל הדילר.
        - `elif player_value > dealer_value or dealer_value > 21`: בדיקת ניצחון השחקן.
        -`elif dealer_value > player_value`: בדיקת ניצחון הדילר.
    -`if __name__ == "__main__":`: הפעלת הקוד הראשי.
    -`play_blackjack()`: קריאה לפונקציית המשחק.
"""