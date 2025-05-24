<BLKJAK>:
=================
רמת מורכבות: 7
-----------------
בלק ג'ק הוא משחק קלפים שבו השחקן מתחרה בדילר. מטרת המשחק היא לצבור 21 נקודות או להיות קרוב ככל האפשר ל-21, מבלי לעבור ערך זה. קלפים עם מספרים מקנים נקודות בהתאם לערכם הנקוב, נסיך, מלכה ומלך מקנים 10 נקודות, ואס מקנה נקודה אחת או 11 נקודות, בהתאם לסיטואציה. השחקן משחק נגד הדילר. השחקן רשאי לקחת קלף נוסף או לעצור. לאחר שהשחקן עצר, הדילר לוקח קלפים עד שסכומו יהיה גדול מ-16. השחקן מנצח אם סכום קלפיו גדול מזה של הדילר, אך קטן או שווה ל-21.

כללי המשחק:
1.  השחקן והדילר מקבלים שני קלפים כל אחד. אחד מקלפי הדילר גלוי.
2.  השחקן בוחן את קלפיו ומחליט אם ברצונו לקחת קלף נוסף (HIT) או לעצור (STAND).
3.  אם סכום קלפי השחקן גדול מ-21, הוא מפסיד.
4.  כאשר השחקן עוצר, הדילר מתחיל לקחת קלפים עד שסכומו יעלה על 16.
5.  אם סכום קלפי הדילר גדול מ-21, הוא מפסיד, והשחקן מנצח.
6.  אם סכום קלפי הדילר אינו עולה על 21, סכומי הקלפים של השחקן ושל הדילר מושווים. המנצח הוא זה שסכומו קרוב יותר ל-21, אך אינו גדול מ-21.
7.  במקרה של שוויון בנקודות מוכרז תיקו (PUSH).
-----------------
אלגוריתם:
1. אתחול חפיסת הקלפים: יצירת חפיסה הכוללת 52 קלפים. לכל קלף ערך מ-1 עד 10 (נסיך, מלכה, מלך = 10, אס = 1 או 11).
2. ערבוב חפיסת הקלפים.
3. חלוקת שני קלפים לשחקן ושני קלפים לדילר. קלף אחד של הדילר גלוי, והשני סמוי.
4. הצגת קלפי השחקן והקלף הגלוי של הדילר על המסך.
5. תור השחקן:
   5.1. שאל את השחקן אם ברצונו לקחת קלף נוסף (HIT) או לעצור (STAND).
   5.2. אם השחקן בוחר ב-HIT, תן לו קלף נוסף ועבור לשלב 5.3.
   5.3. אם סכום קלפי השחקן גדול מ-21, השחקן מפסיד. עבור לשלב 7.
   5.4. אם השחקן בוחר ב-STAND, עבור לשלב 6.
6. תור הדילר:
   6.1. כל עוד סכום קלפי הדילר קטן או שווה ל-16, תן לו קלף נוסף.
   6.2. אם סכום קלפי הדילר גדול מ-21, הדילר מפסיד, השחקן מנצח. עבור לשלב 7.
7. קביעת המנצח:
   7.1. השווה את סכומי קלפי השחקן והדילר.
   7.2. אם סכום קלפי השחקן גדול מסכום קלפי הדילר ואינו גדול מ-21, השחקן מנצח.
   7.3. אם סכום קלפי הדילר גדול מסכום קלפי השחקן ואינו גדול מ-21, הדילר מנצח.
   7.4. אם הסכומים שווים, תיקו.
8. הצגת תוצאת המשחק.
9. סוף המשחק
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeDeck["<p align='left'>אתחול חפיסת הקלפים: 
    <code><b>deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4</b></code></p>"]
    InitializeDeck --> ShuffleDeck["ערבוב חפיסת הקלפים: <code><b>random.shuffle(deck)</b></code>"]
    ShuffleDeck --> DealInitialCards["<p align='left'>חלוקת קלפים ראשונית:
    <code><b>
    playerHand = [deal_card(deck), deal_card(deck)]
    dealerHand = [deal_card(deck), deal_card(deck)]
    </b></code></p>"]
    DealInitialCards --> ShowHands["<p align='left'>הצגת קלפי השחקן וקלף אחד של הדילר</p>"]
    ShowHands --> PlayerTurnStart{"התחלת תור השחקן"}
    PlayerTurnStart --> PlayerActionChoice{"הכנסת פעולת השחקן: HIT או STAND"}
    PlayerActionChoice -- HIT --> PlayerHit["<p align='left'>השחקן לוקח קלף: <code><b>playerHand.append(deal_card(deck))</b></code></p>"]
    PlayerHit --> CalculatePlayerHandValue["<p align='left'>חישוב סכום קלפי השחקן: <code><b>player_value = calculate_hand_value(playerHand)</b></code></p>"]
    CalculatePlayerHandValue --> CheckPlayerBust{"<p align='left'>בדיקה: <code><b>player_value > 21?</b></code></p>"}
    CheckPlayerBust -- Да --> PlayerBust["<p align='left'>השחקן הפסיד: <code><b>print('Игрок проиграл!')</b></code></p>"]
    PlayerBust --> End["סוף"]
    CheckPlayerBust -- Нет --> PlayerTurnStart
    PlayerActionChoice -- STAND --> DealerTurnStart{"התחלת תור הדילר"}
    DealerTurnStart --> DealerHit{"<p align='left'>הדילר לוקח קלף, כל עוד <code><b>dealer_value <= 16</b></code></p>"}
    DealerHit --> CalculateDealerHandValue["<p align='left'>חישוב סכום קלפי הדילר: <code><b>dealer_value = calculate_hand_value(dealerHand)</b></code></p>"]
    CalculateDealerHandValue --> CheckDealerBust{"<p align='left'>בדיקה: <code><b>dealer_value > 21?</b></code></p>"}
    CheckDealerBust -- Да --> DealerBust["<p align='left'>הדילר הפסיד: <code><b>print('Дилер проиграл!')</b></code></p>"]
    DealerBust --> End
    CheckDealerBust -- Нет --> DetermineWinner["<p align='left'>קביעת המנצח והצגת התוצאה</p>"]
    DetermineWinner --> End
    

```
**Legenda** (מקרא)
    Start - התחלת המשחק.
    InitializeDeck - אתחול חפיסת הקלפים, יצירת רשימת קלפים (ערכים מספריים ואס, שחוזרים על עצמם 4 פעמים לכל סוג).
    ShuffleDeck - ערבוב חפיסת הקלפים בסדר אקראי.
    DealInitialCards - חלוקת הקלפים הראשונית לשחקן ולדילר (שני קלפים לכל אחד).
    ShowHands - הצגת קלפי השחקן וקלף אחד גלוי של הדילר.
    PlayerTurnStart - התחלת תור השחקן.
    PlayerActionChoice - בקשת פעולת השחקן: HIT (לקחת קלף) או STAND (לעצור).
    PlayerHit - השחקן לוקח קלף נוסף מהחפיסה.
    CalculatePlayerHandValue - חישוב סכום הנקודות הכולל של קלפי השחקן.
    CheckPlayerBust - בדיקה האם סכום נקודות השחקן עבר את 21.
    PlayerBust - הצגת הודעה על הפסד השחקן, אם סכום הנקודות גדול מ-21.
    DealerTurnStart - התחלת תור הדילר.
    DealerHit - הדילר לוקח קלף, כל עוד סכום נקודות קלפיו אינו עולה על 16.
    CalculateDealerHandValue - חישוב סכום נקודות קלפי הדילר.
    CheckDealerBust - בדיקה האם סכום נקודות הדילר עבר את 21.
    DealerBust - הצגת הודעה על הפסד הדילר, אם סכום הנקודות גדול מ-21.
    DetermineWinner - קביעת המנצח על ידי השוואת נקודות השחקן והדילר, והצגת התוצאה.
    End - סוף המשחק.
"""

import random

def deal_card(deck):
    """מוציאה קלף מחפיסת הקלפים."""
    return deck.pop()

def calculate_hand_value(hand):
    """מחשבת את ערך היד."""
    ace_count = hand.count(11) # מונה את מספר האסים (11)
    total = sum(hand) # מחשבת את הסכום הכולל של הנקודות

    # אם הסכום הכולל גדול מ-21 ויש אס שניתן לספור כ-1
    while total > 21 and ace_count > 0:
        total -= 10 #  הופך אס מ-11 ל-1
        ace_count -= 1
    return total


def display_cards(player_hand, dealer_hand, show_dealer_full=False):
  """מציגה את קלפי השחקן והדילר."""
  print("\nקלפי הדילר:")
  if show_dealer_full:
    print(" ".join(map(str, dealer_hand)), f"סכום: {calculate_hand_value(dealer_hand)}")
  else:
    print("<קלף סמוי> ", dealer_hand[1]) # מציגה את הקלף הראשון של הדילר, השני סמוי
  
  print("קלפי השחקן:", " ".join(map(str, player_hand)), f"סכום: {calculate_hand_value(player_hand)}")
 
def play_blackjack():
    """מפעילה את משחק הבלאק ג'ק."""
    # יצירת חפיסה של 52 קלפים: ערכים מספריים (2-10) ואס (11)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 
    random.shuffle(deck) # מערבבת את חפיסת הקלפים

    # חלוקת קלפים לשחקן ולדילר (2 קלפים לכל אחד)
    player_hand = [deal_card(deck), deal_card(deck)] 
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # הצגת קלפים (קלף אחד של הדילר סמוי)
    display_cards(player_hand, dealer_hand)
    
    # תור השחקן
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value == 21: # אם לשחקן יש מיד 21
          print("בלק ג'ק! ניצחת!")
          return
        
        if player_value > 21: # אם השחקן הפסיד
          print("עברת את 21! הפסדת!")
          return

        action = input("רוצה לקחת עוד קלף? (HIT/STAND): ").upper()
        if action == "HIT":
            player_hand.append(deal_card(deck)) # נותנת קלף לשחקן
            display_cards(player_hand, dealer_hand)
        elif action == "STAND":
            break # עוברת לתור הדילר
        else:
            print("קלט לא תקין. אנא הכנס HIT או STAND.")

    # תור הדילר
    print("\nתור הדילר:")
    while calculate_hand_value(dealer_hand) <= 16:
        dealer_hand.append(deal_card(deck)) # הדילר לוקח קלף
        
    display_cards(player_hand, dealer_hand, True) # מציגה את כל קלפי הדילר

    player_value = calculate_hand_value(player_hand) # סכום השחקן
    dealer_value = calculate_hand_value(dealer_hand) # סכום הדילר

    # בדיקת תנאי ניצחון
    if dealer_value > 21: # אם לדילר יש יותר מ-21
      print("הדילר עבר את 21! ניצחת!")
    elif player_value > dealer_value or dealer_value > 21: # אם לשחקן יש יותר נקודות
      print("ניצחת!")
    elif dealer_value > player_value : # אם לדילר יש יותר נקודות
      print("הפסדת!")
    else:
        print("תיקו!") # תיקו


if __name__ == "__main__":
    play_blackjack() # הפעלת המשחק

"""
הסבר על הקוד:
1.  **ייבוא המודול `random`**:
   -  `import random`: מייבאת את המודול `random`, המשמש ליצירת סדר קלפים אקראי.
2.  **הפונקציה `deal_card(deck)`**:
    -  `def deal_card(deck):`: מגדירה פונקציה לשליפת קלף מחפיסת הקלפים.
    -  `return deck.pop()`: מסירה ומחזירה את הקלף האחרון מחפיסת הקלפים.
3.  **הפונקציה `calculate_hand_value(hand)`**:
    -   `def calculate_hand_value(hand):`: מגדירה פונקציה לחישוב סכום נקודות הקלפים ביד.
    -   `ace_count = hand.count(11)`: סופרת את מספר האסים ביד (אס = 11).
    -   `total = sum(hand)`: מחשבת את הסכום הכולל של נקודות הקלפים.
    -   `while total > 21 and ace_count > 0`: אם הסכום גדול מ-21 ויש אסים.
    -   `total -= 10`:  מחליפה אס מ-11 ל-1.
    -   `ace_count -= 1`: מקטינה את מונה האסים.
    -   `return total`: מחזירה את הסכום הכולל של הנקודות.
4.  **הפונקציה `display_cards(player_hand, dealer_hand, show_dealer_full=False)`**:
    -   `def display_cards(player_hand, dealer_hand, show_dealer_full=False):`: מגדירה פונקציה להצגת הקלפים.
    -  `show_dealer_full=False`: מציגה רק קלף אחד של הדילר.
    -  אם `show_dealer_full=True`: מציגה את כל קלפי הדילר.
5.  **הפונקציה `play_blackjack()`**:
    -  `def play_blackjack():`: מגדירה פונקציה המכילה את לוגיקת המשחק העיקרית.
    -  `deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4`: יוצרת חפיסה של 52 קלפים (ערכים מספריים ואס).
    -  `random.shuffle(deck)`: מערבבת את חפיסת הקלפים.
    -  `player_hand = [deal_card(deck), deal_card(deck)]`: מחלקת 2 קלפים לשחקן.
    -  `dealer_hand = [deal_card(deck), deal_card(deck)]`: מחלקת 2 קלפים לדילר.
    -  `display_cards(player_hand, dealer_hand)`: מציגה את הקלפים הראשוניים.
    -   **תור השחקן**:
         -   `while True:`: לולאה ראשית עבור תור השחקן.
        - `player_value = calculate_hand_value(player_hand)`: מחשבת את סכום השחקן.
        - `if player_value == 21:`: בדיקה לבלאק ג'ק.
        - `if player_value > 21:`: בדיקה להפסד השחקן (עבר את 21).
         -   `action = input("Хотите взять еще карту? (HIT/STAND): ").upper()`: מבקשת את פעולת השחקן (HIT או STAND).
         -   `if action == "HIT":`: אם השחקן בוחר ב-HIT:
            -   `player_hand.append(deal_card(deck))`: מוסיפה קלף ליד השחקן.
            -    `display_cards(player_hand, dealer_hand)`: מציגה את הקלפים.
         -   `elif action == "STAND":`: אם השחקן בוחר ב-STAND, עוברת לתור הדילר.
    -   **תור הדילר**:
        -  `while calculate_hand_value(dealer_hand) <= 16:`: הדילר לוקח קלף כל עוד הסכום קטן מ-16.
         -    `dealer_hand.append(deal_card(deck))`: נותנת קלף לדילר.
        -  `display_cards(player_hand, dealer_hand, True)`: מציגה את קלפי הדילר.
     -    **קביעת המנצח**:
         - `player_value = calculate_hand_value(player_hand)`: מחשבת את סכום השחקן.
         -`dealer_value = calculate_hand_value(dealer_hand)`: מחשבת את סכום הדילר.
        - `if dealer_value > 21: `: בדיקה לעבור את 21 אצל הדילר.
        - `elif player_value > dealer_value or dealer_value > 21`: בדיקת ניצחון השחקן.
        -`elif dealer_value > player_value`: בדיקת ניצחון הדילר.
    -`if __name__ == "__main__":`: הפעלת המשחק.
    -`play_blackjack()`: קריאה לפונקציית המשחק.
"""