"""
<מלחמה 2>:
=================
מורכבות: 4
-----------------
המשחק "מלחמה 2" הינו משחק קלפים לשני שחקנים, שבו כל שחקן מקבל חצי מחפיסת קלפים סטנדרטית. השחקנים שולפים בו-זמנית קלף אחד כל אחד, וזה שקלפו גבוה יותר זוכה בשני הקלפים. אם הקלפים שווים, מוכרזת "מלחמה", והשחקנים מניחים שלושה קלפים עם הפנים כלפי מטה, ואז קלף נוסף פתוח. המנצח ב"מלחמה" לוקח את כל הקלפים. מטרת המשחק היא לאסוף את כל קלפי החפיסה.
חוקי המשחק:
1. חפיסה סטנדרטית של 52 קלפים מחולקת באופן שווה בין שני שחקנים.
2. כל שחקן שולף בו-זמנית את הקלף העליון מחפיסתו.
3. השחקן עם הקלף הגבוה יותר זוכה בשני הקלפים ומוסיף אותם לסוף חפיסתו.
4. אם הקלפים שווים, מוכרזת "מלחמה":
    4.1. כל שחקן מניח שלושה קלפים עם הפנים כלפי מטה.
    4.2. כל שחקן מניח קלף נוסף פתוח.
    4.3. השחקן עם הקלף הפתוח הגבוה יותר זוכה בכל הקלפים (כולל קלפי המלחמה).
    4.4. אם הקלפים הפתוחים שוב שווים, המלחמה חוזרת על עצמה.
5. המשחק ממשיך עד שאחד השחקנים אוסף את כל הקלפים.
6. סמלי הסדרות (מאסטי) אינם נחשבים במשחק, רק דרגת הקלף (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A).
-----------------
אלגוריתם:
1. יצירת חפיסה של 52 קלפים.
2. ערבוב החפיסה.
3. חלוקת החפיסה לשניים באופן שווה בין שני שחקנים (שחקן א' ושחקן ב').
4. התחלת לולאה "כל עוד לשני השחקנים יש קלפים":
    4.1 שחקן א' שולף את הקלף העליון.
    4.2 שחקן ב' שולף את הקלף העליון.
    4.3 אם קלף שחקן א' גבוה מקלף שחקן ב':
        4.3.1 שחקן א' לוקח את שני הקלפים.
    4.4 אם קלף שחקן ב' גבוה מקלף שחקן א':
        4.4.1 שחקן ב' לוקח את שני הקלפים.
    4.5 אם הקלפים שווים:
        4.5.1 התחלת מלחמה:
           4.5.1.1 אם לשחקן פחות מ-4 קלפים:
              4.5.1.1.1 השחקן עם כמות הקלפים הגדולה יותר מנצח.
           4.5.1.2 שחקן א' מניח 3 קלפים עם הפנים כלפי מטה ואחד פתוח.
           4.5.1.3 שחקן ב' מניח 3 קלפים עם הפנים כלפי מטה ואחד פתוח.
           4.5.1.4 אם הקלף הפתוח של שחקן א' גבוה מהקלף הפתוח של שחקן ב':
              4.5.1.4.1 שחקן א' לוקח את כל הקלפים.
           4.5.1.5 אם הקלף הפתוח של שחקן ב' גבוה מהקלף הפתוח של שחקן א':
              4.5.1.5.1 שחקן ב' לוקח את כל הקלפים.
           4.5.1.6 אם הקלפים הפתוחים שווים, חזרה על המלחמה.
5. קביעת המנצח: השחקן שנשארו לו קלפים.
6. הצגת הודעה על המנצח.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeDeck["<p align='left'>אתחול חפיסה:
    <code><b>
    deck = createDeck()
    shuffle(deck)
    playerA, playerB = dealCards(deck)
    </b></code></p>"]
    InitializeDeck --> GameLoopStart{"התחלת לולאת משחק: כל עוד לשני השחקנים יש קלפים"}
    GameLoopStart -- כן --> PlayerA_Draws["שחקן א' שולף קלף"]
    PlayerA_Draws --> PlayerB_Draws["שחקן ב' שולף קלף"]
    PlayerB_Draws --> CompareCards{"בדיקה: קלף A > קלף B ?"}
    CompareCards -- כן --> PlayerA_WinsRound["שחקן א' לוקח קלפים"]
    PlayerA_WinsRound --> GameLoopStart
    CompareCards -- לא --> CompareCards2{"בדיקה: קלף B > קלף A ?"}
     CompareCards2 -- כן --> PlayerB_WinsRound["שחקן ב' לוקח קלפים"]
    PlayerB_WinsRound --> GameLoopStart
     CompareCards2 -- לא --> WarStart{"התחלת מלחמה"}
     WarStart --> CheckCardsForWarA{"בדיקה: לשחקן א' פחות מ-4 קלפים ?"}
     CheckCardsForWarA -- כן --> PlayerBWinsWar["שחקן ב' מנצח במלחמה"]
     PlayerBWinsWar --> GameLoopStart
     CheckCardsForWarA -- לא --> CheckCardsForWarB{"בדיקה: לשחקן ב' פחות מ-4 קלפים ?"}
     CheckCardsForWarB -- כן --> PlayerAWinsWar["שחקן א' מנצח במלחמה"]
     PlayerAWinsWar --> GameLoopStart
     CheckCardsForWarB -- לא --> PlayerA_DrawsWar["שחקן א' מניח 3 קלפים + 1 קלף פתוח"]
     PlayerA_DrawsWar --> PlayerB_DrawsWar["שחקן ב' מניח 3 קלפים + 1 קלף פתוח"]
     PlayerB_DrawsWar --> CompareWarCards{"בדיקה: קלף פתוח A > קלף פתוח B ?"}
     CompareWarCards -- כן --> PlayerA_WinsWarRound["שחקן א' לוקח את כל קלפי המלחמה"]
     PlayerA_WinsWarRound --> WarStart
     CompareWarCards -- לא --> CompareWarCards2{"בדיקה: קלף פתוח B > קלף פתוח A ?"}
      CompareWarCards2 -- כן --> PlayerB_WinsWarRound["שחקן ב' לוקח את כל קלפי המלחמה"]
     PlayerB_WinsWarRound --> WarStart
     CompareWarCards2 -- לא --> WarStart
    GameLoopStart -- לא --> DetermineWinner["קביעת מנצח"]
    DetermineWinner --> OutputWinner["הצגת הודעה על המנצח"]
    OutputWinner --> End["סיום"]
```
**מקרא:**
    Start - התחלת התוכנית.
    InitializeDeck - יצירה וערבוב חפיסה, חלוקתה בין שחקנים A ו-B.
    GameLoopStart - התחלת לולאה הנמשכת כל עוד לשני השחקנים יש קלפים.
    PlayerA_Draws - שחקן A שולף את הקלף העליון מחפיסתו.
    PlayerB_Draws - שחקן B שולף את הקלף העליון מחפיסתו.
    CompareCards - השוואת הקלפים ששלפו שחקנים A ו-B.
    PlayerA_WinsRound - שחקן A לוקח את הקלפים מהשולחן ומוסיף אותם לסוף חפיסתו.
     PlayerB_WinsRound - שחקן B לוקח את הקלפים מהשולחן ומוסיף אותם לסוף חפיסתו.
    WarStart - התחלת "מלחמה" במקרה של שוויון קלפים.
     CheckCardsForWarA - בדיקה: האם לשחקן A פחות מ-4 קלפים?
     PlayerAWinsWar - ניצחון שחקן A במלחמה (לשחקן B פחות מ-4 קלפים).
     CheckCardsForWarB - בדיקה: האם לשחקן B פחות מ-4 קלפים?
     PlayerBWinsWar - ניצחון שחקן B במלחמה (לשחקן A פחות מ-4 קלפים).
     PlayerA_DrawsWar - שחקן A מניח 3 קלפים עם הפנים כלפי מטה וקלף אחד פתוח.
     PlayerB_DrawsWar - שחקן B מניח 3 קלפים עם הפנים כלפי מטה וקלף אחד פתוח.
     CompareWarCards - השוואת הקלפים הפתוחים במהלך המלחמה.
    PlayerA_WinsWarRound - שחקן A מנצח ב"מלחמה" ולוקח את כל הקלפים.
     PlayerB_WinsWarRound - שחקן B מנצח ב"מלחמה" ולוקח את כל הקלפים.
    DetermineWinner - קביעת מנצח המשחק.
    OutputWinner - הצגת הודעה על המנצח.
    End - סיום התוכנית.
"""
import random

def create_deck():
    """יוצר חפיסה סטנדרטית של 52 קלפים."""
    suits = ["C", "D", "H", "S"]  # סדרות: Clubs, Diamonds, Hearts, Spades
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [rank + suit for suit in suits for rank in ranks] # יוצרים חפיסה
    return deck


def deal_cards(deck):
    """מחלק קלפים לשני שחקנים."""
    random.shuffle(deck) # מערבבים את החפיסה
    player_a = deck[:len(deck) // 2] # מחלקים חצי מהקלפים לשחקן הראשון
    player_b = deck[len(deck) // 2:] # מחלקים את החצי השני לשחקן השני
    return player_a, player_b


def get_card_value(card):
    """מחזיר את הערך המספרי של קלף (ללא התחשבות בסדרה)."""
    rank = card[:-1]  # מקבלים את דרגת הקלף, תוך השמטת הסדרה
    if rank.isdigit():  # אם הדרגה היא מספר
        return int(rank)  # מחזירים את הערך המספרי של הדרגה
    elif rank == "J":    # אם הדרגה היא נסיך (ג'ק)
        return 11        # מחזירים 11
    elif rank == "Q":    # אם הדרגה היא מלכה (קווין)
        return 12        # מחזירים 12
    elif rank == "K":    # אם הדרגה היא מלך (קינג)
        return 13        # מחזירים 13
    elif rank == "A":    # אם הדרגה היא אס
        return 14        # מחזירים 14
    return 0


def war(player_a, player_b, cards_on_table):
    """תהליך מלחמה."""
    while True:
        # בודקים האם לשחקנים יש מספיק קלפים למלחמה
        if len(player_a) < 4: # אם לשחקן A יש פחות מ-4 קלפים
            return True,False,cards_on_table,player_a, player_b # מחזירים ששחקן B ניצח, ואת הקלפים
        if len(player_b) < 4: # אם לשחקן B יש פחות מ-4 קלפים
           return False,True, cards_on_table,player_a, player_b # מחזירים ששחקן A ניצח, ואת הקלפים

        # לוקחים קלפים למלחמה
        war_cards_a = player_a[:4] # 4 הקלפים הראשונים של שחקן A
        war_cards_b = player_b[:4] # 4 הקלפים הראשונים של שחקן B
        player_a = player_a[4:]    # מסירים את 4 הקלפים הראשונים מחפיסת שחקן A
        player_b = player_b[4:]    # מסירים את 4 הקלפים הראשונים מחפיסת שחקן B
        cards_on_table.extend(war_cards_a) # מוסיפים את קלפי שחקן A לשולחן
        cards_on_table.extend(war_cards_b) # מוסיפים את קלפי שחקן B לשולחן

        # משווים קלפים פתוחים
        card_a_value = get_card_value(war_cards_a[-1]) # מקבלים את הערך של הקלף האחרון של שחקן A
        card_b_value = get_card_value(war_cards_b[-1]) # מקבלים את הערך של הקלף האחרון של שחקן B

        if card_a_value > card_b_value: # אם קלף שחקן A גבוה יותר
            player_a.extend(cards_on_table) # שחקן A לוקח את כל הקלפים מהשולחן
            return False,False,[],player_a, player_b  # מחזירים שהמלחמה הסתיימה, שחקן A ניצח
        elif card_b_value > card_a_value: # אם קלף שחקן B גבוה יותר
            player_b.extend(cards_on_table) # שחקן B לוקח את כל הקלפים מהשולחן
            return False,False,[],player_a, player_b  # מחזירים שהמלחמה הסתיימה, שחקן B ניצח
        # אם הקלפים שווים - חוזרים על המלחמה


def play_war():
    """הלוגיקה העיקרית של משחק המלחמה."""
    deck = create_deck()  # יוצרים חפיסה
    player_a, player_b = deal_cards(deck) # מחלקים קלפים

    round_number = 0 # מונה סיבובים
    while player_a and player_b: # כל עוד לשני השחקנים יש קלפים
        round_number += 1 # מגדילים את מונה הסיבובים
        print(f"סיבוב {round_number}. קלפים של שחקן A: {len(player_a)}, קלפים של שחקן B: {len(player_b)}")
        card_a = player_a.pop(0) # לוקחים קלף מחפיסת שחקן A
        card_b = player_b.pop(0) # לוקחים קלף מחפיסת שחקן B
        cards_on_table = [card_a, card_b] # קלפים על השולחן

        card_a_value = get_card_value(card_a) # מקבלים את ערך קלף שחקן A
        card_b_value = get_card_value(card_b) # מקבלים את ערך קלף שחקן B

        if card_a_value > card_b_value: # אם קלף שחקן A גבוה יותר
            player_a.extend(cards_on_table) # שחקן A לוקח את הקלפים
        elif card_b_value > card_a_value:  # אם קלף שחקן B גבוה יותר
            player_b.extend(cards_on_table) # שחקן B לוקח את הקלפים
        else:  # אם הקלפים שווים, מתחילים מלחמה
            a_win_war, b_win_war ,cards_on_table,player_a, player_b = war(player_a, player_b, cards_on_table) # מפעילים מלחמה
            if a_win_war == True: # אם לשחקן A לא הספיקו קלפים
                print ("שחקן B ניצח במלחמה")
                break # יוצאים מהלולאה
            elif b_win_war == True: # אם לשחקן B לא הספיקו קלפים
                print ("שחקן A ניצח במלחמה")
                break # יוצאים מהלולאה
        
        # לשם נוחות, מערבבים את הקלפים בסוף כל יד
        random.shuffle(player_a) 
        random.shuffle(player_b)


    if not player_a:  # אם לשחקן A אין קלפים
        print("שחקן B ניצח במשחק!")  # מציגים הודעה על ניצחון שחקן B
    elif not player_b: # אם לשחקן B אין קלפים
        print("שחקן A ניצח במשחק!") # מציגים הודעה על ניצחון שחקן A


if __name__ == "__main__":
    play_war()

"""
הסבר קוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את המודול `random`, הנחוץ לערבוב חפיסת הקלפים.
2.  **פונקציה `create_deck()`**:
    -   יוצרת חפיסה סטנדרטית של 52 קלפים.
    -   `suits = ["C", "D", "H", "S"]`: מגדירה רשימת סדרות (Clubs, Diamonds, Hearts, Spades).
    -   `ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]`: מגדירה רשימת דרגות קלפים.
    -   `deck = [rank + suit for suit in suits for rank in ranks]`: מייצרת חפיסת קלפים על ידי שילוב דרגות וסדרות.
    -   `return deck`: מחזירה את החפיסה שנוצרה.
3.  **פונקציה `deal_cards(deck)`**:
    -   מחלקת קלפים לשני שחקנים.
    -   `random.shuffle(deck)`: מערבבת את החפיסה.
    -   `player_a = deck[:len(deck) // 2]`: מחלקת את החצי הראשון של החפיסה לשחקן A.
    -   `player_b = deck[len(deck) // 2:]`: מחלקת את החצי השני של החפיסה לשחקן B.
    -   `return player_a, player_b`: מחזירה את קלפי השחקנים.
4.  **פונקציה `get_card_value(card)`**:
    -   קובעת את הערך המספרי של הקלף לצורך השוואה.
    -   `rank = card[:-1]`: מחלצת את דרגת הקלף.
    -   בודקת אם הדרגה היא מספר, ומחזירה את ערכה המספרי.
    -   קובעת ערך מספרי לקלפים עם אותיות (J=11, Q=12, K=13, A=14).
    -   `return 0`: אם הדרגה לא מוגדרת (לשם הזהירות) מחזירה 0.
5.  **פונקציה `war(player_a, player_b, cards_on_table)`**:
    -   מממשת את לוגיקת ה"מלחמה" במשחק.
    -   `while True:`: לולאה אינסופית, ממשיכה עד סיום המלחמה.
        -   בודקים האם לשחקנים יש מספיק קלפים למלחמה.
        -   אם למישהו יש פחות מ-4 קלפים, מוכרז שהשחקן השני ניצח
        -   לוקחים 4 קלפים מכל שחקן ומניחים על השולחן
        -   משווים קלפים פתוחים (הקלפים האחרונים ברשימות)
        -   אם קלף שחקן A גבוה יותר, שחקן A לוקח את הקלפים, יוצאים מהלולאה
        -   אם קלף שחקן B גבוה יותר, שחקן B לוקח את הקלפים, יוצאים מהלולאה
        -   אם הקלפים שווים, חוזרים על המלחמה.
    -   `return` מחזיר ערכים:
        - a_win_war - ניצחון שחקן A במלחמה (לשחקן B פחות מ-4 קלפים)
        - b_win_war - ניצחון שחקן B במלחמה (לשחקן A פחות מ-4 קלפים)
        - cards_on_table - הקלפים שנותרו על השולחן
        - player_a - חפיסת שחקן A לאחר המלחמה
        - player_b - חפיסת שחקן B לאחר המלחמה
6. **פונקציה `play_war()`**:
    -   הלוגיקה העיקרית של המשחק.
    -   יוצרת חפיסה ומחלקת קלפים לשחקנים.
    -   `while player_a and player_b:`: מפעילה את הלולאה הראשית, כל עוד לשני השחקנים יש קלפים.
        -   מונה סיבובים.
        -   לוקחים קלף אחד מחפיסות השחקנים.
        -   משווים את ערכי הקלפים.
        -   אם קלף A > קלף B, אז A לוקח את כל הקלפים.
        -   אם קלף B > קלף A, אז B לוקח את כל הקלפים.
        -   אם הקלפים שווים, קוראים לפונקציה `war()`.
        -   מערבבים את חפיסות השחקנים בסוף הסיבוב.
    -   קובעת את המנצח לפי הימצאות קלפים אצל השחקנים.
    -   מציגה הודעה על המנצח.
7.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: מפעיל את המשחק אם הקובץ מורץ ישירות.
    -   `play_war()`: קורא לפונקציה להתחלת המשחק.
"""