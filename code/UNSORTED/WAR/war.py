מלחמה (WAR):
=================
דרגת קושי: 3
-----------------
המשחק "מלחמה" הוא משחק קלפים המיועד לשני שחקנים, העושה שימוש בחבילת קלפים סטנדרטית בת 52 קלפים. השחקנים מחלקים את החבילה לשניים ומניחים בתורם קלף אחד. השחקן שקלפו בעל ערך גבוה יותר זוכה בסיבוב ולוקח את שני הקלפים. אם ערכי הקלפים זהים, מוכרזת "מלחמה" - השחקנים מניחים שלושה קלפים נוספים פנים כלפי מטה, ולאחר מכן חושפים את הקלף הרביעי, אשר קובע את המנצח.

כללי המשחק:
1.  נעשה שימוש בחבילת קלפים סטנדרטית בת 52 קלפים.
2.  החבילה מחולקת לשניים בין שני השחקנים.
3.  כל שחקן בתורו מניח את הקלף העליון מחבילתו.
4.  השחקן עם הקלף בעל הערך הגבוה יותר לוקח את שני הקלפים ומניח אותם בסוף חבילתו.
5.  אם ערכי הקלפים זהים, מוכרזת "מלחמה":
    -   כל שחקן מניח 3 קלפים פנים כלפי מטה (סמויים).
    -   לאחר מכן, כל שחקן מניח קלף רביעי פנים כלפי מעלה (גלוי).
    -   השחקן עם הקלף הרביעי הגדול יותר זוכה ב"מלחמה" ולוקח את כל הקלפים (10) מסיבוב זה.
6.  המשחק נמשך עד אשר אחד מהשחקנים נשאר ללא קלפים.
7.  השחקן שנשארו לו קלפים מוכרז כמנצח.

-----------------
אלגוריתם:
1.  יצירת חבילה בת 52 קלפים.
2.  ערבוב החבילה.
3.  חלוקת החבילה שווה בשווה בין שני השחקנים.
4.  התחלת לולאה "כל עוד לשני השחקנים יש קלפים":
    4.1 כל שחקן מניח את הקלף העליון מחבילתו.
    4.2 אם קלף שחקן 1 גדול יותר מקלף שחקן 2, שחקן 1 לוקח את שני הקלפים ומניח אותם בסוף חבילתו.
    4.3 אם קלף שחקן 2 גדול יותר מקלף שחקן 1, שחקן 2 לוקח את שני הקלפים ומניח אותם בסוף חבילתו.
    4.4 אם הקלפים שווים, הכרזת "מלחמה":
        4.4.1 אם לאחד מהשחקנים אין מספיק קלפים ל"מלחמה" (פחות מ-4), אז הוא מפסיד.
        4.4.2 כל שחקן מניח שלושה קלפים פנים כלפי מטה (סמויים).
        4.4.3 כל שחקן מניח קלף רביעי פנים כלפי מעלה (גלוי).
        4.4.4 השחקן עם הקלף הרביעי הגדול יותר לוקח את כל הקלפים (10) ומוסיף אותם לסוף חבילתו. אם הקלפים שווים שוב, ה"מלחמה" חוזרת על עצמה.
5.  הצגת הודעה על המנצח (השחקן שנשארו לו קלפים).
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> CreateDeck["יצירת חבילה בת 52 קלפים"]
    CreateDeck --> ShuffleDeck["ערבוב החבילה"]
    ShuffleDeck --> DivideDeck["חלוקת החבילה שווה בשווה בין שני שחקנים"]
    DivideDeck --> GameLoopStart{"התחלת לולאת המשחק: כל עוד לשני השחקנים יש קלפים"}
    GameLoopStart -- כן --> Player1Card["שחקן 1 מניח קלף"]
    GameLoopStart -- כן --> Player2Card["שחקן 2 מניח קלף"]
    Player1Card --> CompareCards{"השוואת קלפים: <code>card1 > card2</code>?"}
    CompareCards -- כן --> Player1WinsRound["שחקן 1 זוכה בסיבוב"]
     Player1WinsRound --> AddCardsToPlayer1Deck["שחקן 1 לוקח את שני הקלפים ומוסיף לחבילתו"]
      AddCardsToPlayer1Deck --> GameLoopStart
    CompareCards -- לא --> CompareCards2{"השוואת קלפים: <code>card1 < card2</code>?"}
    CompareCards2 -- כן --> Player2WinsRound["שחקן 2 זוכה בסיבוב"]
     Player2WinsRound --> AddCardsToPlayer2Deck["שחקן 2 לוקח את שני הקלפים ומוסיף לחבילתו"]
     AddCardsToPlayer2Deck --> GameLoopStart
    CompareCards2 -- לא --> WarStart{"הכרזת מלחמה: <code>card1 == card2</code>"}
    WarStart --> CheckWarCards{"בדיקה: האם לשחקנים יש 4 קלפים למלחמה?"}
    CheckWarCards -- לא --> DetermineWinner["קביעת המנצח (למי שנשארו קלפים)"]
    DetermineWinner --> End["סוף משחק"]
    CheckWarCards -- כן --> Player1WarCards["שחקן 1 מניח 3 קלפים סמויים ו-1 גלוי"]
    Player1WarCards --> Player2WarCards["שחקן 2 מניח 3 קלפים סמויים ו-1 גלוי"]
    Player2WarCards --> CompareWarCards{"השוואת קלפי מלחמה גלויים: <code>warCard1 > warCard2</code>?"}
    CompareWarCards -- כן --> Player1WinsWar["שחקן 1 זוכה במלחמה"]
    Player1WinsWar --> AddWarCardsToPlayer1Deck["שחקן 1 לוקח את כל קלפי המלחמה"]
    AddWarCardsToPlayer1Deck --> GameLoopStart
     CompareWarCards -- לא --> CompareWarCards2{"השוואת קלפי מלחמה גלויים: <code>warCard1 < warCard2</code>?"}
     CompareWarCards2 -- כן --> Player2WinsWar["שחקן 2 זוכה במלחמה"]
    Player2WinsWar --> AddWarCardsToPlayer2Deck["שחקן 2 לוקח את כל קלפי המלחמה"]
    AddWarCardsToPlayer2Deck --> GameLoopStart
     CompareWarCards2 -- לא --> WarStart
        
    GameLoopStart -- לא --> DetermineWinner
```
מקרא:
    Start - התחלת התוכנית.
    CreateDeck - יצירת חבילת קלפים סטנדרטית בת 52 קלפים.
    ShuffleDeck - ערבוב החבילה שנוצרה.
    DivideDeck - חלוקת החבילה שווה בשווה בין שני שחקנים.
    GameLoopStart - התחלת לולאת המשחק הראשית, הנמשכת כל עוד לשני השחקנים יש קלפים.
    Player1Card - שחקן 1 מניח את הקלף העליון מהחבילה שלו.
    Player2Card - שחקן 2 מניח את הקלף העליון מהחבילה שלו.
    CompareCards - השוואת הקלפים שהונחו על ידי השחקנים, קובעת למי הקלף גדול יותר.
    Player1WinsRound - שחקן 1 זוכה בסיבוב, אם הקלף שלו גדול יותר.
    AddCardsToPlayer1Deck - שחקן 1 לוקח את שני הקלפים ומוסיף אותם לסוף חבילתו.
    Player2WinsRound - שחקן 2 זוכה בסיבוב, אם הקלף שלו גדול יותר.
    AddCardsToPlayer2Deck - שחקן 2 לוקח את שני הקלפים ומוסיף אותם לסוף חבילתו.
     WarStart - התחלת "מלחמה" אם הקלפים בעלי ערכים זהים.
    CheckWarCards - בדיקה, האם לשחקנים יש מספיק קלפים ל"מלחמה" (לא פחות מ-4).
     DetermineWinner - קביעת המנצח, אם לאחד מהשחקנים נגמרו הקלפים.
    End - סיום התוכנית.
    Player1WarCards - שחקן 1 מניח 3 קלפים סמויים וקלף 1 גלוי עבור ה"מלחמה".
    Player2WarCards - שחקן 2 מניח 3 קלפים סמויים וקלף 1 גלוי עבור ה"מלחמה".
    CompareWarCards - השוואת הקלפים הגלויים ב"מלחמה" לקביעת המנצח.
    Player1WinsWar - שחקן 1 זוכה ב"מלחמה".
     AddWarCardsToPlayer1Deck - שחקן 1 לוקח את כל הקלפים מסיבוב המלחמה ומוסיף אותם לסוף חבילתו.
    Player2WinsWar - שחקן 2 זוכה ב"מלחמה".
    AddWarCardsToPlayer2Deck - שחקן 2 לוקח את כל הקלפים מסיבוב המלחמה ומוסיף אותם לסוף חבילתו.
```
```python
import random

# פונקציה ליצירת חבילת קלפים
def create_deck():
    suits = ["C", "D", "H", "S"] # סוגי קלפים (תלתנים, יהלומים, לבבות, עלים)
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]  # ערכי קלפים (2-10, נסיך, מלכה, מלך, אס)
    deck = [rank + suit for suit in suits for rank in ranks] # יוצר את החבילה כרשימת מחרוזות (לדוגמה, '2C' - שתיים תלתן)
    return deck

# פונקציה לחלוקת החבילה בין השחקנים
def deal_cards(deck):
    random.shuffle(deck)  # מערבב את החבילה
    middle = len(deck) // 2  # מוצא את אמצע החבילה
    player1_deck = deck[:middle] # מחלק את החצי הראשון לשחקן 1
    player2_deck = deck[middle:] # מחלק את החצי השני לשחקן 2
    return player1_deck, player2_deck

# פונקציה לקביעת ערך הקלף
def card_value(card):
    rank = card[0]  # לוקח את התו הראשון של הקלף, לדוגמה '2' או 'T'
    if rank.isdigit():  # אם זה ספרה, מחזיר אותה כמספר שלם
        return int(rank)
    elif rank == 'T':
        return 10   # 'T' - עשר
    elif rank == 'J':
        return 11   # 'J' - נסיך
    elif rank == 'Q':
        return 12   # 'Q' - מלכה
    elif rank == 'K':
        return 13   # 'K' - מלך
    elif rank == 'A':
        return 14   # 'A' - אס
    
# פונקציה לניהול מצב "מלחמה"
def war(player1_deck, player2_deck):
    print("ВОЙНА!!!") # Keep Russian print output as per instructions implicitly
    # בדיקה האם לשחקנים יש מספיק קלפים למלחמה (מינימום 4 קלפים לכל אחד)
    if len(player1_deck) < 4 or len(player2_deck) < 4:
        if len(player1_deck) < 4:
            print("У игрока 1 недостаточно карт для войны. Игрок 2 побеждает!") # Keep Russian print output
            return 2, [], [] # מחזיר ששחקן 2 ניצח ורשימות קלפים ריקות
        else:
            print("У игрока 2 недостаточно карт для войны. Игрок 1 побеждает!") # Keep Russian print output
            return 1, [], [] # מחזיר ששחקן 1 ניצח ורשימות קלפים ריקות

    # לוקח 3 קלפים סמויים + 1 קלף גלוי
    player1_war_cards = []
    player2_war_cards = []
    for _ in range(3):
        player1_war_cards.append(player1_deck.pop(0)) # לוקח קלפים מתחילת החבילה
        player2_war_cards.append(player2_deck.pop(0))

    player1_war_card = player1_deck.pop(0)
    player2_war_card = player2_deck.pop(0)
    print(f"Игрок 1 открывает: {player1_war_card}, Игрок 2 открывает: {player2_war_card}") # Keep Russian print output
    war_cards = player1_war_cards + player2_war_cards + [player1_war_card, player2_war_card] #אוסף את כל קלפי המלחמה לרשימה אחת
    
    # משווה את קלפי המלחמה
    if card_value(player1_war_card) > card_value(player2_war_card):
         print("Игрок 1 выигрывает войну!") # Keep Russian print output
         return 1, war_cards, []   # מחזיר ששחקן 1 ניצח ורשימת קלפי המלחמה
    elif card_value(player2_war_card) > card_value(player1_war_card):
        print("Игрок 2 выигрывает войну!") # Keep Russian print output
        return 2, [], war_cards  # מחזיר ששחקן 2 ניצח ורשימת קלפי המלחמה
    else:
        print("Ещё одна война!") # Keep Russian print output
        winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck) #קורא לפונקציה באופן רקורסיבי עבור מלחמה נוספת
        return winner, player1_add_cards + war_cards if winner == 1 else [], player2_add_cards + war_cards if winner == 2 else []
    


# פונקציית המשחק הראשית
def play_war():
    deck = create_deck()    # יוצר חבילה
    player1_deck, player2_deck = deal_cards(deck) # מחלק קלפים לשחקנים
    round_number = 0    # מונה סיבובים
    
    # לולאת המשחק הראשית
    while player1_deck and player2_deck:
        round_number += 1 # מגדיל את מונה הסיבובים
        print(f"\n--- Раунд {round_number} ---") # Keep Russian print output
        
        player1_card = player1_deck.pop(0)  # שחקן 1 מניח קלף
        player2_card = player2_deck.pop(0)  # שחקן 2 מניח קלף
        print(f"Игрок 1 выкладывает: {player1_card}, Игрок 2 выкладывает: {player2_card}") # Keep Russian print output

        # משווה את הקלפים
        if card_value(player1_card) > card_value(player2_card):
            print("Игрок 1 выигрывает раунд!") # Keep Russian print output
            player1_deck.append(player1_card) # השחקן המנצח בסיבוב לוקח את הקלפים לסוף החבילה שלו
            player1_deck.append(player2_card)
        elif card_value(player2_card) > card_value(player1_card):
            print("Игрок 2 выигрывает раунд!") # Keep Russian print output
            player2_deck.append(player2_card) # השחקן המנצח בסיבוב לוקח את הקלפים לסוף החבילה שלו
            player2_deck.append(player1_card)
        else:
           winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck) # אם הקלפים שווים, קורא לפונקציית המלחמה
           if winner == 1:
                player1_deck.extend(player1_add_cards)  # מוסיף את הקלפים לחבילה של שחקן 1
           elif winner == 2:
                player2_deck.extend(player2_add_cards)  # מוסיף את הקלפים לחבילה של שחקן 2
        print(f"У Игрока 1 {len(player1_deck)} карт, у Игрока 2 {len(player2_deck)} карт.") # Keep Russian print output
    # קובע את המנצח
    if player1_deck:
        print("\nИгрок 1 победил!") # Keep Russian print output
    else:
        print("\nИгрок 2 победил!") # Keep Russian print output

if __name__ == "__main__":
    play_war() # קורא לפונקציה להתחלת המשחק
```
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש לערבוב החבילה.

2.  **הפונקציה `create_deck()`**:
    -   `suits = ["C", "D", "H", "S"]`: רשימת סוגי קלפים במשחק (תלתנים, יהלומים, לבבות, עלים).
    -   `ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]`: רשימת ערכי קלפים במשחק (מ-2 ועד אס).
    -   `deck = [rank + suit for suit in suits for rank in ranks]`: יוצר את החבילה, כרשימה של 52 קלפים (לדוגמה, "2C" - שתיים תלתן).

3.  **הפונקציה `deal_cards(deck)`**:
    -   `random.shuffle(deck)`: מערבב את החבילה באופן אקראי.
    -   `middle = len(deck) // 2`: מוצא את אמצע החבילה.
    -   `player1_deck = deck[:middle]`: יוצר את חבילת שחקן 1 מהחצי הראשון של החבילה.
    -   `player2_deck = deck[middle:]`: יוצר את חבילת שחקן 2 מהחצי השני של החבילה.
    -   מחזיר את החבילות של שחקן 1 ושחקן 2.

4.  **הפונקציה `card_value(card)`**:
    -   `rank = card[0]`: מקבל את ערך הקלף ממחרוזתו (לדוגמה, '2', 'T', 'J', 'Q', 'K', 'A').
    -   `if rank.isdigit(): ... elif rank == 'T': ... elif rank == 'J': ... elif rank == 'Q': ... elif rank == 'K': ... elif rank == 'A':`: קובע את הערך המספרי של הקלף (מ-2 ועד 14 עבור אס).

5.  **הפונקציה `war(player1_deck, player2_deck)`**:
    -   מממש את לוגיקת ה"מלחמה", כאשר קלפי השחקנים שווים.
    -   בודק האם לשחקנים יש מספיק קלפים (לא פחות מ-4) להכרזת מלחמה.
    -   אם לאחד מהשחקנים אין מספיק קלפים למלחמה, השחקן השני מוכרז כמנצח.
    -   אחרת, לוקח 3 קלפים "סמויים" וקלף 1 "גלוי" מכל שחקן.
    -   משווה את הקלפים הגלויים.
    -   אם הקלפים שווים, קורא לפונקציה `war` באופן רקורסיבי (מלחמה חוזרת).
    -   מחזיר את המנצח ואת כל הקלפים מסיבוב המלחמה (עבור המנצח).

6.  **הפונקציה `play_war()`**:
    -   `deck = create_deck()`: יוצר חבילה.
    -   `player1_deck, player2_deck = deal_cards(deck)`: מחלק קלפים לשחקנים.
    -   `round_number = 0`: מאתחל את מונה הסיבובים.
    -   **לולאת המשחק הראשית `while player1_deck and player2_deck:`**:
        -   מציג את מספר הסיבוב הנוכחי.
        -   כל שחקן מניח את הקלף העליון.
        -   משווה את ערכי הקלפים.
        -   אם ערכי הקלפים שווים, נקראת פונקציית `war` לקביעת המנצח ב"מלחמה".
        -   במצב אחר, מוסיף את הקלפים לסוף החבילה של השחקן המנצח בסיבוב.
        -   מציג את כמות הקלפים אצל כל שחקן.
        -   הלולאה נמשכת עד אשר לאחד מהשחקנים לא יישארו קלפים.
    -   מציג את מנצח המשחק.
7.  **התנאי `if __name__ == "__main__":`**:
    -   `play_war()`: קורא לפונקציה להתחלת המשחק.