<WAR 2>:
=================
**מורכבות**: 4
-----------------
המשחק "WAR 2" הוא משחק קלפים לשני שחקנים, בו כל שחקן מקבל מחצית מחבילת קלפים סטנדרטית. שחקנים מניחים קלף אחד בו זמנית, והשחקן שקלפו בכיר יותר לוקח את שני הקלפים. אם הקלפים שווים, מוכרזת "מלחמה", ושחקנים מניחים שלושה קלפים עם הפנים כלפי מטה, ולאחר מכן קלף אחד נוסף עם הפנים כלפי מעלה. מנצח ה"מלחמה" לוקח את כל הקלפים. מטרת המשחק היא לאסוף את כל קלפי החבילה.

**חוקי המשחק:**
1.  חבילת קלפים סטנדרטית בת 52 קלפים מחולקת שווה בשווה בין שני שחקנים.
2.  כל שחקן מניח בו זמנית את הקלף העליון מחבילת הקלפים שלו.
3.  השחקן עם הקלף הבכיר יותר לוקח את שני הקלפים ומוסיף אותם לסוף חבילת הקלפים שלו.
4.  אם הקלפים שווים, מוכרזת "מלחמה":
    4.1. כל שחקן מניח שלושה קלפים עם הפנים כלפי מטה.
    4.2. כל שחקן מניח קלף אחד נוסף עם הפנים כלפי מעלה.
    4.3. השחקן עם הקלף הפתוח הבכיר יותר לוקח את כל הקלפים (כולל קלפי המלחמה).
    4.4. אם הקלפים הפתוחים שווים שוב, המלחמה חוזרת על עצמה.
5.  המשחק נמשך עד שאחד מהשחקנים אוסף את כל הקלפים.
6.  סמלי הקלפים (suits) אינם נלקחים בחשבון במשחק, רק דרגת הקלף (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A).
-----------------
**אלגוריתם:**
1.  יצירת חבילת קלפים בת 52 קלפים.
2.  ערבוב חבילת הקלפים.
3.  חלוקת חבילת הקלפים לשניים בין שני שחקנים (שחקן A ושחקן B).
4.  התחלת לולאה "כל עוד לשני השחקנים יש קלפים":
    4.1. שחקן A מניח את הקלף העליון.
    4.2. שחקן B מניח את הקלף העליון.
    4.3. אם קלף שחקן A בכיר יותר מקלף שחקן B:
        4.3.1. שחקן A לוקח את שני הקלפים.
    4.4. אם קלף שחקן B בכיר יותר מקלף שחקן A:
        4.4.1. שחקן B לוקח את שני הקלפים.
    4.5. אם הקלפים שווים:
        4.5.1. התחלת מלחמה:
           4.5.1.1. אם לשחקן יש פחות מ-4 קלפים:
              4.5.1.1.1. השחקן עם מספר הקלפים הגדול יותר מנצח.
           4.5.1.2. שחקן A מניח 3 קלפים עם הפנים כלפי מטה וקלף אחד פתוח.
           4.5.1.3. שחקן B מניח 3 קלפים עם הפנים כלפי מטה וקלף אחד פתוח.
           4.5.1.4. אם הקלף הפתוח של שחקן A בכיר יותר מהקלף הפתוח של שחקן B:
              4.5.1.4.1. שחקן A לוקח את כל הקלפים.
           4.5.1.5. אם הקלף הפתוח של שחקן B בכיר יותר מהקלף הפתוח של שחקן A:
              4.5.1.5.1. שחקן B לוקח את כל הקלפים.
           4.5.1.6. אם הקלפים הפתוחים שווים, חזרה על המלחמה.
5.  קביעת המנצח: השחקן שלו נשארו קלפים.
6.  הצגת הודעה על המנצח.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["Начало"] --> InitializeDeck["<p align='left'>Инициализация колоды:
    <code><b>
    deck = createDeck()
    shuffle(deck)
    playerA, playerB = dealCards(deck)
    </b></code></p>"]
    InitializeDeck --> GameLoopStart{"Начало игрового цикла: пока у обоих игроков есть карты"}
    GameLoopStart -- Да --> PlayerA_Draws["Игрок A выкладывает карту"]
    PlayerA_Draws --> PlayerB_Draws["Игрок B выкладывает карту"]
    PlayerB_Draws --> CompareCards{"Проверка: Карта A > Карта B ?"}
    CompareCards -- Да --> PlayerA_WinsRound["Игрок A забирает карты"]
    PlayerA_WinsRound --> GameLoopStart
    CompareCards -- Нет --> CompareCards2{"Проверка: Карта B > Карта A ?"}
     CompareCards2 -- Да --> PlayerB_WinsRound["Игрок B забирает карты"]
    PlayerB_WinsRound --> GameLoopStart
     CompareCards2 -- Нет --> WarStart{"Начало Войны"}
     WarStart --> CheckCardsForWarA{"Проверка: У игрока A < 4 карт ?"}
     CheckCardsForWarA -- Да --> PlayerBWinsWar["Победа Игрока B в войне"]
     PlayerBWinsWar --> GameLoopStart
     CheckCardsForWarA -- Нет --> CheckCardsForWarB{"Проверка: У игрока B < 4 карт ?"}
     CheckCardsForWarB -- Да --> PlayerAWinsWar["Победа Игрока A в войне"]
     PlayerAWinsWar --> GameLoopStart
     CheckCardsForWarB -- Нет --> PlayerA_DrawsWar["Игрок A выкладывает 3 карты + 1 открытую карту"]
     PlayerA_DrawsWar --> PlayerB_DrawsWar["Игрок B выкладывает 3 карты + 1 открытую карту"]
     PlayerB_DrawsWar --> CompareWarCards{"Проверка: Открытая карта A > Открытая карта B ?"}
     CompareWarCards -- Да --> PlayerA_WinsWarRound["Игрок A забирает все карты войны"]
     PlayerA_WinsWarRound --> WarStart
     CompareWarCards -- Нет --> CompareWarCards2{"Проверка: Открытая карта B > Открытая карта A ?"}
      CompareWarCards2 -- Да --> PlayerB_WinsWarRound["Игрок B забирает все карты войны"]
     PlayerB_WinsWarRound --> WarStart
     CompareWarCards2 -- Нет --> WarStart
    GameLoopStart -- Нет --> DetermineWinner["Определение победителя"]
    DetermineWinner --> OutputWinner["Вывод сообщения о победителе"]
    OutputWinner --> End["Конец"]
```
**מקרא:**
    Start - התחלת התוכנית.
    InitializeDeck - יצירה וערבוב של חבילת הקלפים, חלוקתה בין שחקנים A ו-B.
    GameLoopStart - התחלת הלולאה הנמשכת כל עוד לשני השחקנים יש קלפים.
    PlayerA_Draws - שחקן A מניח את הקלף העליון מחבילת הקלפים שלו.
    PlayerB_Draws - שחקן B מניח את הקלף העליון מחבילת הקלפים שלו.
    CompareCards - השוואת הקלפים שהונחו על ידי שחקנים A ו-B.
    PlayerA_WinsRound - שחקן A לוקח את הקלפים מהשולחן ומוסיף אותם לסוף חבילת הקלפים שלו.
     PlayerB_WinsRound - שחקן B לוקח את הקלפים מהשולחן ומוסיף אותם לסוף חבילת הקלפים שלו.
    WarStart - התחלת "מלחמה" במקרה של קלפים שווים.
     CheckCardsForWarA - בדיקה: האם לשחקן A יש פחות מ-4 קלפים?
     PlayerAWinsWar - ניצחון שחקן A במלחמה (לשחקן B פחות מ-4 קלפים).
     CheckCardsForWarB - בדיקה: האם לשחקן B יש פחות מ-4 קלפים?
     PlayerBWinsWar - ניצחון שחקן B במלחמה (לשחקן A פחות מ-4 קלפים).
     PlayerA_DrawsWar - שחקן A מניח 3 קלפים עם הפנים כלפי מטה ו-1 פתוח.
     PlayerB_DrawsWar - שחקן B מניח 3 קלפים עם הפנים כלפי מטה ו-1 פתוח.
     CompareWarCards - השוואת הקלפים הפתוחים במהלך המלחמה.
    PlayerA_WinsWarRound - שחקן A מנצח ב"מלחמה" ולוקח את כל הקלפים.
     PlayerB_WinsWarRound - שחקן B מנצח ב"מלחמה" ולוקח את כל הקלפים.
    DetermineWinner - קביעת מנצח המשחק.
    OutputWinner - הצגת הודעה על המנצח.
    End - סיום התוכנית.
```
```python
import random

def create_deck():
    """יוצר חבילת קלפים סטנדרטית בת 52 קלפים."""
    suits = ["C", "D", "H", "S"]  # סמלי הקלפים: Clubs, Diamonds, Hearts, Spades
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [rank + suit for suit in suits for rank in ranks] # מייצרים את החבילה
    return deck


def deal_cards(deck):
    """מחלק קלפים לשני שחקנים."""
    random.shuffle(deck) # מערבבים את החבילה
    player_a = deck[:len(deck) // 2] # מחלקים חצי מהקלפים לשחקן הראשון
    player_b = deck[len(deck) // 2:] # מחלקים את החצי השני לשחקן השני
    return player_a, player_b


def get_card_value(card):
    """מחזיר את הערך המספרי של הקלף (ללא התחשבות בסמל)."""
    rank = card[:-1]  # מקבלים את דרגת הקלף, תוך התעלמות מהסמל
    if rank.isdigit():  # אם הדרגה היא מספר
        return int(rank)  # מחזירים את הערך המספרי של הדרגה
    elif rank == "J":    # אם הדרגה היא נסיך (J)
        return 11        # מחזירים 11
    elif rank == "Q":    # אם הדרגה היא מלכה (Q)
        return 12        # מחזירים 12
    elif rank == "K":    # אם הדרגה היא מלך (K)
        return 13        # מחזירים 13
    elif rank == "A":    # אם הדרגה היא אס (A)
        return 14        # מחזירים 14
    return 0


def war(player_a, player_b, cards_on_table):
    """תהליך המלחמה."""
    while True:
        # בודקים האם לשחקנים יש מספיק קלפים למלחמה
        if len(player_a) < 4: # אם לשחקן A פחות מ-4 קלפים
            return True,False,cards_on_table,player_a, player_b # מחזירים ששחקן B ניצח, ואת הקלפים
        if len(player_b) < 4: # אם לשחקן B פחות מ-4 קלפים
           return False,True, cards_on_table,player_a, player_b # מחזירים ששחקן A ניצח, ואת הקלפים

        # לוקחים קלפים למלחמה
        war_cards_a = player_a[:4] # 4 הקלפים הראשונים של שחקן A
        war_cards_b = player_b[:4] # 4 הקלפים הראשונים של שחקן B
        player_a = player_a[4:]    # מסירים את 4 הקלפים הראשונים מחבילת שחקן A
        player_b = player_b[4:]    # מסירים את 4 הקלפים הראשונים מחבילת שחקן B
        cards_on_table.extend(war_cards_a) # מוסיפים את קלפי שחקן A לשולחן
        cards_on_table.extend(war_cards_b) # מוסיפים את קלפי שחקן B לשולחן

        # משווים את הקלפים הפתוחים
        card_a_value = get_card_value(war_cards_a[-1]) # מקבלים את הערך של הקלף האחרון של שחקן A
        card_b_value = get_card_value(war_cards_b[-1]) # מקבלים את הערך של הקלף האחרון של שחקן B

        if card_a_value > card_b_value: # אם קלף שחקן A בכיר יותר
            player_a.extend(cards_on_table) # שחקן A לוקח את כל הקלפים מהשולחן
            return False,False,[],player_a, player_b  # מחזירים שהמלחמה הסתיימה, שחקן A ניצח
        elif card_b_value > card_a_value: # אם קלף שחקן B בכיר יותר
            player_b.extend(cards_on_table) # שחקן B לוקח את כל הקלפים מהשולחן
            return False,False,[],player_a, player_b  # מחזירים שהמלחמה הסתיימה, שחקן B ניצח
        # אם הקלפים שווים - חוזרים על המלחמה


def play_war():
    """הלוגיקה הראשית של משחק המלחמה."""
    deck = create_deck()  # יוצרים חבילת קלפים
    player_a, player_b = deal_cards(deck) # מחלקים קלפים

    round_number = 0 # מונה סיבובים
    while player_a and player_b: # כל עוד לשני השחקנים יש קלפים
        round_number += 1 # מגדילים את מונה הסיבובים
        print(f"Раунд {round_number}. Карты игрока A: {len(player_a)}, Карты игрока B: {len(player_b)}")
        card_a = player_a.pop(0) # לוקחים קלף מחבילת שחקן A
        card_b = player_b.pop(0) # לוקחים קלף מחבילת שחקן B
        cards_on_table = [card_a, card_b] # קלפים על השולחן

        card_a_value = get_card_value(card_a) # מקבלים את הערך של קלף שחקן A
        card_b_value = get_card_value(card_b) # מקבלים את הערך של קלף שחקן B

        if card_a_value > card_b_value: # אם קלף שחקן A בכיר יותר
            player_a.extend(cards_on_table) # שחקן A לוקח את הקלפים
        elif card_b_value > card_a_value:  # אם קלף שחקן B בכיר יותר
            player_b.extend(cards_on_table) # שחקן B לוקח את הקלפים
        else:  # אם הקלפים שווים, מתחילים מלחמה
            a_win_war, b_win_war ,cards_on_table,player_a, player_b = war(player_a, player_b, cards_on_table) # מריצים מלחמה
            if a_win_war == True: # אם לשחקן A לא הספיקו הקלפים
                print ("Игрок B победил в войне")
                break # יוצאים מהלולאה
            elif b_win_war == True: # אם לשחקן B לא הספיקו הקלפים
                print ("Игрок A победил в войне")
                break # יוצאים מהלולאה
        
        # למטרת אקראיות, מערבבים את הקלפים בסוף כל יד
        random.shuffle(player_a) 
        random.shuffle(player_b)


    if not player_a:  # אם לשחקן A אין קלפים
        print("Игрок B выиграл игру!")  # מציגים הודעה על ניצחון שחקן B
    elif not player_b: # אם לשחקן B אין קלפים
        print("Игрок A выиграл игру!") # מציגים הודעה על ניצחון שחקן A


if __name__ == "__main__":
    play_war()

```
**הסבר קוד:**
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, הדרוש לערבוב חבילת הקלפים.
2.  **פונקציה `create_deck()`**:
    -   יוצרת חבילת קלפים סטנדרטית בת 52 קלפים.
    -   `suits = ["C", "D", "H", "S"]`: מגדיר רשימה של סמלי קלפים (Clubs, Diamonds, Hearts, Spades).
    -   `ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]`: מגדיר רשימה של דרגות קלפים.
    -   `deck = [rank + suit for suit in suits for rank in ranks]`: מייצר את חבילת הקלפים על ידי שילוב דרגות וסמלים.
    -   `return deck`: מחזירה את חבילת הקלפים שנוצרה.
3.  **פונקציה `deal_cards(deck)`**:
    -   מחלקת קלפים לשני שחקנים.
    -   `random.shuffle(deck)`: מערבבת את חבילת הקלפים.
    -   `player_a = deck[:len(deck) // 2]`: מחלקת את החצי הראשון של החבילה לשחקן A.
    -   `player_b = deck[len(deck) // 2:]`: מחלקת את החצי השני של החבילה לשחקן B.
    -   `return player_a, player_b`: מחזירה את קלפי השחקנים.
4.  **פונקציה `get_card_value(card)`**:
    -   קובעת את הערך המספרי של הקלף להשוואה.
    -   `rank = card[:-1]`: מחלצת את דרגת הקלף.
    -   בודקת האם הדרגה היא מספר ומחזירה את ערכה המספרי.
    -   קובעת ערך מספרי לקלפים עם אותיות (J=11, Q=12, K=13, A=14).
    -   `return 0`: אם הדרגה לא מוגדרת (לכל מקרה) מחזירה 0.
5.  **פונקציה `war(player_a, player_b, cards_on_table)`**:
    -   מממשת את לוגיקת ה"מלחמה" במשחק.
    -   `while True:`: לולאה אינסופית, נמשכת עד סיום המלחמה.
        -   בדיקה האם לשחקנים יש מספיק קלפים למלחמה.
        -   אם למישהו פחות מ-4 קלפים, מוכרז ניצחון לשחקן השני.
        -   לוקחים 4 קלפים מכל שחקן ומניחים על השולחן.
        -   משווים את הקלפים הפתוחים (הקלפים האחרונים ברשימות).
        -   אם קלף שחקן A בכיר יותר, שחקן A לוקח את הקלפים, יוצאים מהלולאה.
        -   אם קלף שחקן B בכיר יותר, שחקן B לוקח את הקלפים, יוצאים מהלולאה.
        -   אם הקלפים שווים, חוזרים על המלחמה.
    -   `return` מחזיר ערכים:
        - a_win_war - ניצחון שחקן A במלחמה (לשחקן B פחות מ-4 קלפים)
        - b_win_war - ניצחון שחקן B במלחמה (לשחקן A פחות מ-4 קלפים)
        - cards_on_table - הקלפים שנותרו על השולחן
        - player_a - חבילת שחקן A אחרי המלחמה
        - player_b - חבילת שחקן B אחרי המלחמה
6. **פונקציה `play_war()`**:
    -   הלוגיקה הראשית של המשחק.
    -   יוצרת חבילת קלפים ומחלקת קלפים לשחקנים.
    -   `while player_a and player_b:`: מריצה את הלולאה הראשית כל עוד לשני השחקנים יש קלפים.
        -   מונה סיבובים.
        -   לוקחים קלף אחד מחבילות השחקנים.
        -   משווים את ערכי הקלפים.
        -   אם קלף A > קלף B, אז A לוקח את כל הקלפים.
        -   אם קלף B > קלף A, אז B לוקח את כל הקלפים.
        -   אם הקלפים שווים, קוראים לפונקציה `war()`.
        -   מערבבים את חבילות השחקנים בסוף כל סיבוב.
    -   קובעת את המנצח לפי הימצאות קלפים אצל השחקנים.
    -   מציגה הודעה על המנצח.
7.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: מפעיל את המשחק אם הקובץ מורץ ישירות.
    -   `play_war()`: קורא לפונקציה כדי להתחיל את המשחק.