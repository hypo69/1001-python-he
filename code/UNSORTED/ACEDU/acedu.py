import random

# אתחול חפיסת קלפים
def create_deck():
    ranks = list(range(2, 15))  # קלפים מ-2 עד 14 (אס = 14)
    deck = ranks * 4  # 4 סדרות
    random.shuffle(deck)
    return deck

# הצגת קלף בפורמט קריא
def card_name(value):
    if value == 11:
        return "נסיך"
    elif value == 12:
        return "מלכה"
    elif value == 13:
        return "מלך"
    elif value == 14:
        return "אס"
    else:
        return str(value)

# לולאת המשחק הראשית
def play_acey_ducey():
    print("ברוכים הבאים למשחק Acey Ducey!")
    print("חוקים: עליך להמר האם הקלף הבא יהיה בין שני הקלפים החשופים.")
    print("אם הקלף שווה לאחד הקלפים החשופים, או שהוא אס, אתה מפסיד.")
    print("הקלד '0' כדי לדלג על התור.\n")

    money = 100  # הון התחלתי של השחקן
    deck = create_deck()

    while money > 0 and len(deck) >= 3:
        print(f"יתרתך הנוכחית: ${money}")

        # חשיפת שני קלפים
        card1 = deck.pop()
        card2 = deck.pop()
        while card1 == card2:  # אם הקלפים זהים, שולפים חדשים
            deck.insert(0, card1)
            deck.insert(0, card2)
            card1 = deck.pop()
            card2 = deck.pop()

        print(f"קלף ראשון: {card_name(card1)}")
        print(f"קלף שני: {card_name(card2)}")

        # הגדרת הטווח
        low_card = min(card1, card2)
        high_card = max(card1, card2)

        # ביצוע הימור או דילוג על התור
        try:
            bet = int(input(f"בצע הימור (מ-0 עד {money}) או הקלד '0' לדילוג על התור: "))
            if bet < 0 or bet > money:
                print("הימור שגוי. אנא נסה שנית.")
                continue
            if bet == 0:
                print("דילגת על התור.\n")
                continue  # דילוג על התור
        except ValueError:
            print("אנא הזן מספר.")
            continue

        # שליפת הקלף הבא
        next_card = deck.pop()
        print(f"קלף הבא: {card_name(next_card)}")

        # בדיקת התוצאה
        if next_card == card1 or next_card == card2 or next_card == 14:
            print("הפסדת!")
            money -= bet
        elif low_card < next_card < high_card:
            print("ניצחת!")
            money += bet
        else:
            print("הפסדת!")
            money -= bet

        print()

    # סיום המשחק
    if money <= 0:
        print("נגמר לך הכסף. המשחק הסתיים.")
    else:
        print(f"המשחק הסתיים. יתרתך הסופית: ${money}")

# הפעלת המשחק
if __name__ == "__main__":
    play_acey_ducey()