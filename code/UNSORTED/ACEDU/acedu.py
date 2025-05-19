import random

# אתחול חפיסת קלפים
def create_deck():
    ranks = list(range(2, 15))  # קלפים מ-2 עד 14 (אס = 14)
    deck = ranks * 4  # 4 צבעים
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
    print("חוקים: הניחו הימור, בהתאם לניחוש האם הקלף הבא יהיה בין שני הקלפים שהוצגו.")
    print("אם הקלף שווה לאחד הקלפים שהוצגו, או אם הוא אס, אתם מפסידים.")
    print("הזינו '0' על מנת לדלג על התור.\n")

    money = 100  # הון התחלתי של השחקן
    deck = create_deck()

    while money > 0 and len(deck) >= 3:
        print(f"יתרתכם הנוכחית: ${money}")

        # חשיפת שני קלפים
        card1 = deck.pop()
        card2 = deck.pop()
        while card1 == card2:  # אם הקלפים זהים, לוקחים חדשים
            deck.insert(0, card1)
            deck.insert(0, card2)
            card1 = deck.pop()
            card2 = deck.pop()

        print(f"קלף ראשון: {card_name(card1)}")
        print(f"קלף שני: {card_name(card2)}")

        # הגדרת הטווח
        low_card = min(card1, card2)
        high_card = max(card1, card2)

        # הנחת הימור או דילוג על התור
        try:
            bet = int(input(f"הניחו הימור (מ-0 עד {money}) או הזינו '0' על מנת לדלג על התור: "))
            if bet < 0 or bet > money:
                print("הימור שגוי. אנא נסו שנית.")
                continue
            if bet == 0:
                print("דילגתם על התור.\n")
                continue  # דילוג על התור
        except ValueError:
            print("אנא הזינו מספר.")
            continue

        # משיכת הקלף הבא
        next_card = deck.pop()
        print(f"קלף הבא: {card_name(next_card)}")

        # בדיקת התוצאה
        if next_card == card1 or next_card == card2 or next_card == 14:
            print("הפסדתם!")
            money -= bet
        elif low_card < next_card < high_card:
            print("ניצחתם!")
            money += bet
        else:
            print("הפסדתם!")
            money -= bet

        print()

    # סיום המשחק
    if money <= 0:
        print("נגמר לכם הכסף. המשחק הסתיים.")
    else:
        print(f"המשחק הסתיים. יתרתכם הסופית: ${money}")

# הפעלת המשחק
if __name__ == "__main__":
    play_acey_ducey()