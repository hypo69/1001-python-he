WAR:
=================
מורכבות: 3
-----------------
המשחק "מלחמה" הוא משחק קלפים לשני שחקנים, המשתמש בחבילת קלפים סטנדרטית בת 52 קלפים. השחקנים מחלקים את החבילה לשניים ומניחים בתורם קלף אחד בכל פעם. השחקן שקלפו בעל ערך גבוה יותר מנצח בסיבוב ולוקח את שני הקלפים. אם הקלפים בעלי ערך זהה, מוכרזת "מלחמה" - השחקנים מניחים עוד שלושה קלפים עם הפנים כלפי מטה, ולאחר מכן חושפים את הקלף הרביעי, אשר קובע את המנצח.

כללי המשחק:
1.  נעשה שימוש בחבילת קלפים סטנדרטית בת 52 קלפים.
2.  החבילה מחולקת שווה בשווה בין שני השחקנים.
3.  כל שחקן בתורו מניח את הקלף העליון מחבילתו.
4.  השחקן עם קלף בעל ערך גדול יותר לוקח את שני הקלפים ומניח אותם בתחתית החבילה שלו.
5.  אם הקלפים בעלי ערך זהה, מוכרזת "מלחמה":
    -   כל שחקן מניח 3 קלפים עם הפנים כלפי מטה.
    -   לאחר מכן כל שחקן חושף את הקלף הרביעי.
    -   השחקן עם הקלף הרביעי בעל הערך הגדול יותר מנצח ב"מלחמה" ולוקח את כל הקלפים (10) מסיבוב זה.
6.  המשחק נמשך עד אשר אחד השחקנים נשאר ללא קלפים.
7.  השחקן שנותרים לו קלפים מוכרז כמנצח.

-----------------
אלגוריתם:
1.  יצירת חבילת קלפים של 52 קלפים.
2.  ערבוב החבילה.
3.  חלוקת החבילה שווה בשווה בין שני השחקנים.
4.  התחלת לולאת המשחק: כל עוד לשני השחקנים יש קלפים:
    4.1 כל שחקן מניח את הקלף העליון מחבילתו.
    4.2 אם הקלף של השחקן הראשון גדול מהקלף של השחקן השני, השחקן הראשון לוקח את שני הקלפים ומניח אותם בתחתית החבילה שלו.
    4.3 אם הקלף של השחקן השני גדול מהקלף של השחקן הראשון, השחקן השני לוקח את שני הקלפים ומניח אותם בתחתית החבילה שלו.
    4.4 אם הקלפים שווים, הכרזת "מלחמה":
        4.4.1 אם לאחד מהשחקנים אין מספיק קלפים ל"מלחמה" (פחות מ-4), הוא מפסיד.
        4.4.2 כל שחקן מניח שלושה קלפים עם הפנים כלפי מטה.
        4.4.3 כל שחקן מניח את הקלף הרביעי עם הפנים כלפי מעלה.
        4.4.4 השחקן עם הקלף הרביעי בעל הערך הגדול יותר לוקח את כל הקלפים (10) ומוסיף אותם לתחתית החבילה שלו. אם הקלפים שוב שווים, "מלחמה" חוזרת על עצמה.
5.  הצגת הודעה על המנצח (השחקן שנותרו לו קלפים).
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> CreateDeck["Создание колоды из 52 карт"]
    CreateDeck --> ShuffleDeck["Перемешивание колоды"]
    ShuffleDeck --> DivideDeck["Разделение колоды поровну между двумя игроками"]
    DivideDeck --> GameLoopStart{"Начало игрового цикла: пока у обоих игроков есть карты"}
    GameLoopStart -- Да --> Player1Card["Игрок 1 выкладывает карту"]
    GameLoopStart -- Да --> Player2Card["Игрок 2 выкладывает карту"]
    Player1Card --> CompareCards{"Сравнение карт: <code>card1 > card2</code>?"}
    CompareCards -- Да --> Player1WinsRound["Игрок 1 выигрывает раунд"]
     Player1WinsRound --> AddCardsToPlayer1Deck["Игрок 1 забирает обе карты и добавляет их в конец своей колоды"]
      AddCardsToPlayer1Deck --> GameLoopStart
    CompareCards -- Нет --> CompareCards2{"Сравнение карт: <code>card1 < card2</code>?"}
    CompareCards2 -- Да --> Player2WinsRound["Игрок 2 выигрывает раунд"]
     Player2WinsRound --> AddCardsToPlayer2Deck["Игрок 2 забирает обе карты и добавляет их в конец своей колоды"]
     AddCardsToPlayer2Deck --> GameLoopStart
    CompareCards2 -- Нет --> WarStart{"Объявление войны: <code>card1 == card2</code>"}
    WarStart --> CheckWarCards{"Проверка: есть ли у игроков 4 карты для войны?"}
    CheckWarCards -- Нет --> DetermineWinner["Определение победителя (у кого остались карты)"]
    DetermineWinner --> End["Конец игры"]
    CheckWarCards -- Да --> Player1WarCards["Игрок 1 выкладывает 3 карты в закрытую и 1 открытую"]
    Player1WarCards --> Player2WarCards["Игрок 2 выкладывает 3 карты в закрытую и 1 открытую"]
    Player2WarCards --> CompareWarCards{"Сравнение открытых карт войны: <code>warCard1 > warCard2</code>?"}
    CompareWarCards -- Да --> Player1WinsWar["Игrok 1 выигрывает войну"]
    Player1WinsWar --> AddWarCardsToPlayer1Deck["Игрок 1 забирает все карты войны"]
    AddWarCardsToPlayer1Deck --> GameLoopStart
     CompareWarCards -- Нет --> CompareWarCards2{"Сравнение открытых карт войны: <code>warCard1 < warCard2</code>?"}
     CompareWarCards2 -- Да --> Player2WinsWar["Игрок 2 выигрывает войну"]
    Player2WinsWar --> AddWarCardsToPlayer2Deck["Игрок 2 забирает все карты войны"]
    AddWarCardsToPlayer2Deck --> GameLoopStart
     CompareWarCards2 -- Нет --> WarStart
        
    GameLoopStart -- Нет --> DetermineWinner
```
מקרא:
    Start - התחלת התוכנית.
    CreateDeck - יצירת חבילת קלפים סטנדרטית בת 52 קלפים.
    ShuffleDeck - ערבוב החבילה שנוצרה.
    DivideDeck - חלוקת החבילה שווה בשווה בין שני השחקנים.
    GameLoopStart - התחלת לולאת המשחק הראשית, הנמשכת כל עוד לשני השחקנים יש קלפים.
    Player1Card - שחקן 1 מניח את הקלף העליון מחבילתו.
    Player2Card - שחקן 2 מניח את הקלף העליון מחבילתו.
    CompareCards - השוואת הקלפים שהונחו על ידי השחקנים, קובעת למי יש קלף גדול יותר.
    Player1WinsRound - שחקן 1 מנצח בסיבוב, אם קלפו גדול יותר.
    AddCardsToPlayer1Deck - שחקן 1 לוקח את שני הקלפים ומוסיף אותם לתחתית החבילה שלו.
    Player2WinsRound - שחקן 2 מנצח בסיבוב, אם קלפו גדול יותר.
    AddCardsToPlayer2Deck - שחקן 2 לוקח את שני הקלפים ומוסיף אותם לתחתית החבילה שלו.
     WarStart - התחלת "מלחמה" אם הקלפים בעלי ערכים זהים.
    CheckWarCards - בדיקה האם לשחקנים יש מספיק קלפים ל"מלחמה" (לא פחות מ-4).
     DetermineWinner - קביעת המנצח, אם לאחד השחקנים נגמרו הקלפים.
    End - סוף התוכנית.
    Player1WarCards - שחקן 1 מניח 3 קלפים עם הפנים כלפי מטה וקלף אחד עם הפנים כלפי מעלה עבור "מלחמה".
    Player2WarCards - שחקן 2 מניח 3 קלפים עם הפנים כלפי מטה וקלף אחד עם הפנים כלפי מעלה עבור "מלחמה".
    CompareWarCards - השוואת הקלפים הפתוחים ב"מלחמה" לקביעת המנצח.
    Player1WinsWar - שחקן 1 מנצח ב"מלחמה".
     AddWarCardsToPlayer1Deck - שחקן 1 לוקח את כל הקלפים מסיבוב ה"מלחמה" ומוסיף אותם לתחתית החבילה שלו.
    Player2WinsWar - שחקן 2 מנצח ב"מלחמה".
    AddWarCardsToPlayer2Deck - שחקן 2 לוקח את כל הקלפים מסיבוב ה"מלחמה" ומוסיף אותם לתחתית החבילה שלו.
```
```python
import random

# פונקציה ליצירת חבילת קלפים
def create_deck():
    suits = ["C", "D", "H", "S"] # סדרות (לבבות, יהלומים, עלים, פיקים)
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]  # ערכי קלפים (2-10, נסיך, מלכה, מלך, אס)
    deck = [rank + suit for suit in suits for rank in ranks] # יוצרת חבילה כרשימה של מחרוזות (לדוגמה, '2C' - שתיים עלים)
    return deck

# פונקציה לחלוקת החבילה בין השחקנים
def deal_cards(deck):
    random.shuffle(deck)  # מערבבת את החבילה
    middle = len(deck) // 2  # מוצאת את אמצע החבילה
    player1_deck = deck[:middle] # מחלקת את החצי הראשון לשחקן 1
    player2_deck = deck[middle:] # מחלקת את החצי השני לשחקן 2
    return player1_deck, player2_deck

# פונקציה לקביעת ערך הקלף
def card_value(card):
    rank = card[0]  # לוקחת את התו הראשון של הקלף, למשל '2' או 'T'
    if rank.isdigit():  # אם זה תו ספרתי, מחזירה אותו כ-int
        return int(rank)
    elif rank == 'T':
        return 10   # 'T' - 10
    elif rank == 'J':
        return 11   # 'J' - נסיך
    elif rank == 'Q':
        return 12   # 'Q' - מלכה
    elif rank == 'K':
        return 13   # 'K' - מלך
    elif rank == 'A':
        return 14   # 'A' - אס
    
# פונקציה למשחק "מלחמה"
def war(player1_deck, player2_deck):
    print("ВОЙНА!!!") # Keep as is, potentially a sound effect or standard print
    # בדיקה שלמספר הקלפים אצל כל שחקן מספיק למלחמה (מינימום 4 קלפים אצל כל אחד)
    if len(player1_deck) < 4 or len(player2_deck) < 4:
        if len(player1_deck) < 4:
            print("У игрока 1 недостаточно карт для войны. Игрок 2 побеждает!") # Keep as is, user printout
            return 2, [], [] # מחזירה ששחקן 2 ניצח ורשימות קלפים ריקות
        else:
            print("У игрока 2 недостаточно карт для войны. Игрок 1 побеждает!") # Keep as is, user printout
            return 1, [], [] # מחזירה ששחקן 1 ניצח ורשימות קלפים ריקות

    # לוקחת 3 קלפים "עם הפנים כלפי מטה" + 1 "עם הפנים כלפי מעלה"
    player1_war_cards = []
    player2_war_cards = []
    for _ in range(3):
        player1_war_cards.append(player1_deck.pop(0)) # לוקחת קלפים מתחילת החבילה
        player2_war_cards.append(player2_deck.pop(0))

    player1_war_card = player1_deck.pop(0)
    player2_war_card = player2_deck.pop(0)
    print(f"Игрок 1 открывает: {player1_war_card}, Игрок 2 открывает: {player2_war_card}") # Keep as is, user printout
    war_cards = player1_war_cards + player2_war_cards + [player1_war_card, player2_war_card] # אוספת את כל הקלפים מה"מלחמה" לרשימה אחת
    
    # משווה את קלפי ה"מלחמה"
    if card_value(player1_war_card) > card_value(player2_war_card):
         print("Игрок 1 выигрывает войну!") # Keep as is, user printout
         return 1, war_cards, []   # מחזירה ששחקן 1 ניצח ואת רשימת קלפי ה"מלחמה"
    elif card_value(player2_war_card) > card_value(player1_war_card):
        print("Игрок 2 выигрывает войну!") # Keep as is, user printout
        return 2, [], war_cards  # מחזירה ששחקן 2 ניצח ואת רשימת קלפי ה"מלחמה"
    else:
        print("Ещё одна война!") # Keep as is, user printout
        winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck) # קוראת לפונקציה באופן רקורסיבי עבור "מלחמה" נוספת
        # The logic here was a bit off in the original comment/code - fixed translation of the comment
        # If winner is 1, player1 gets cards. If winner is 2, player2 gets cards. If still tied (shouldn't happen with recursive return 1 or 2), nobody gets these cards?
        # The code logic is: if winner is 1, add war_cards to player1_add_cards; otherwise add empty list. Similarly for player2. This seems correct for recursive calls.
        return winner, player1_add_cards + war_cards if winner == 1 else [], player2_add_cards + war_cards if winner == 2 else []
    


# פונקציה ראשית של המשחק
def play_war():
    deck = create_deck()    # יוצרת חבילה
    player1_deck, player2_deck = deal_cards(deck) # מחלקת קלפים לשחקנים
    round_number = 0    # מונה סיבובים
    
    # לולאת המשחק הראשית
    while player1_deck and player2_deck:
        round_number += 1 # מגדילה את מונה הסיבובים
        print(f"\n--- Раунд {round_number} ---") # Keep as is, user printout
        
        player1_card = player1_deck.pop(0)  # שחקן 1 מניח קלף
        player2_card = player2_deck.pop(0)  # שחקן 2 מניח קלף
        print(f"Игрок 1 выкладывает: {player1_card}, Игрок 2 выкладывает: {player2_card}") # Keep as is, user printout

        # משווה את הקלפים
        if card_value(player1_card) > card_value(player2_card):
            print("Игрок 1 выигрывает раунд!") # Keep as is, user printout
            player1_deck.append(player1_card) # השחקן המנצח לוקח את הקלפים לתחתית החבילה שלו
            player1_deck.append(player2_card)
        elif card_value(player2_card) > card_value(player1_card):
            print("Игрок 2 выигрывает раунд!") # Keep as is, user printout
            player2_deck.append(player2_card) # השחקן המנצח לוקח את הקלפים לתחתית החבילה שלו
            player2_deck.append(player1_card)
        else:
           winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck) # אם הקלפים שווים, קוראת לפונקציית ה"מלחמה"
           if winner == 1:
                player1_deck.extend(player1_add_cards)  # מוסיפה קלפים לחבילה של שחקן 1
           elif winner == 2:
                player2_deck.extend(player2_add_cards)  # מוסיפה קלפים לחבילה של שחקן 2
        print(f"У Игрока 1 {len(player1_deck)} карт, у Игрока 2 {len(player2_deck)} карт.") # Keep as is, user printout
    # קובעת את המנצח
    if player1_deck:
        print("\nИгрок 1 победил!") # Keep as is, user printout
    else:
        print("\nИгрок 2 победил!") # Keep as is, user printout

if __name__ == "__main__":
    play_war() # קוראת לפונקציה להתחלת המשחק
```
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש לערבוב החבילה.

2.  **פונקציה `create_deck()`**:
    -   `suits = ["C", "D", "H", "S"]`: רשימת סדרות קלפי המשחק (עלים, יהלומים, לבבות, פיקים).
    -   `ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]`: רשימת ערכי קלפי המשחק (מ-2 ועד אס).
    -   `deck = [rank + suit for suit in suits for rank in ranks]`: יוצרת את החבילה, כרשימה של 52 קלפים (לדוגמה, "2C" - שתיים עלים).

3.  **פונקציה `deal_cards(deck)`**:
    -   `random.shuffle(deck)`: מערבבת את החבילה באופן אקראי.
    -   `middle = len(deck) // 2`: מוצאת את אמצע החבילה.
    -   `player1_deck = deck[:middle]`: יוצרת את חבילת השחקן הראשון מהחצי הראשון של החבילה.
    -   `player2_deck = deck[middle:]`: יוצרת את חבילת השחקן השני מהחצי השני של החבילה.
    -   מחזירה את חבילות השחקן הראשון והשני.

4.  **פונקציה `card_value(card)`**:
    -   `rank = card[0]`: מקבלת את ערך הקלף מהמחרוזת שלו (לדוגמה, '2', 'T', 'J', 'Q', 'K', 'A').
    -   `if rank.isdigit(): ... elif rank == 'T': ... elif rank == 'J': ... elif rank == 'Q': ... elif rank == 'K': ... elif rank == 'A':`: קובעת את הערך המספרי של הקלף (מ-2 ועד 14 עבור אס).

5.  **פונקציה `war(player1_deck, player2_deck)`**:
    -   מממשת את לוגיקת ה"מלחמה", כאשר הקלפים של השחקנים שווים.
    -   בדיקה האם לשחקנים יש מספיק קלפים (לא פחות מ-4) להכרזת מלחמה.
    -   אם לאחד השחקנים חסרים קלפים למלחמה, השחקן השני מוכרז כמנצח.
    -   אחרת, לוקחת 3 קלפים "עם הפנים כלפי מטה" ו-1 "עם הפנים כלפי מעלה" מכל שחקן.
    -   משווה את הקלפים הפתוחים.
    -   אם הקלפים שווים, קוראת לפונקציה `war` באופן רקורסיבי (מלחמה חוזרת).
    -   מחזירה את המנצח ואת כל הקלפים מסיבוב ה"מלחמה" (עבור המנצח).

6.  **פונקציה `play_war()`**:
    -   `deck = create_deck()`: יוצרת חבילה.
    -   `player1_deck, player2_deck = deal_cards(deck)`: מחלקת קלפים לשחקנים.
    -   `round_number = 0`: מאתחלת את מונה הסיבובים.
    -   **לולאת המשחק הראשית `while player1_deck and player2_deck:`**:
        -   מציגה את מספר הסיבוב הנוכחי.
        -   כל שחקן מניח את הקלף העליון.
        -   משווה את ערכי הקלפים.
        -   אם ערכי הקלפים שווים, נקראת פונקציית `war` לקביעת מנצח ה"מלחמה".
        -   אחרת, מוסיפה את הקלפים לתחתית חבילת השחקן המנצח.
        -   מציגה את כמות הקלפים אצל כל שחקן.
        -   הלולאה ממשיכה עד אשר לאחד השחקנים נגמרים הקלפים.
    -   מציגה את מנצח המשחק.
7.  **תנאי `if __name__ == "__main__":`**:
    -   `play_war()`: קוראת לפונקציה להתחלת המשחק.