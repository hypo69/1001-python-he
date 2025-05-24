<POKER>:
=================
רמת קושי: 5
-----------------
המשחק "פוקר" הוא גרסה פשוטה של פוקר קלפים לשחקן יחיד. השחקן מקבל חמישה קלפים, המיוצגים על ידי מספרים מ-1 עד 13 (כאשר 1 - אס, 11 - נסיך (ג'ק), 12 - מלכה (קווין), 13 - מלך (קינג)). השחקן יכול להשאיר או להחליף כל מספר של קלפים פעם אחת. לאחר מכן, מוצגת קומבינציית הקלפים והזכייה, אם קיימת.

כללי המשחק:
1.  השחקן מתחיל עם חמישה קלפים אקראיים מ-1 עד 13.
2.  השחקן יכול לבחור אילו קלפים להשאיר ואילו להחליף, על ידי הזנת מספרי הקלפים מופרדים ברווח (לדוגמה "1 3 5"), או 0 כדי להשאיר הכל כפי שהוא.
3.  קלפים שהוחלפו מוחלפים בקלפים אקראיים חדשים.
4.  לאחר החלפת הקלפים, נקבעת הקומבינציה:
    -   זוג (שני ערכים זהים)
    -   שני זוגות (פעמיים שני ערכים זהים)
    -   שלישייה (שלושה ערכים זהים)
    -   פול האוס (שלושה ערכים זהים + זוג)
    -   רביעייה (ארבעה ערכים זהים)
    -   סטרייט (חמישה ערכים עוקבים)
    -   פלאש (חמישה קלפים מאותה סדרה; ביישום זה, הסדרה אינה נלקחת בחשבון, רק הרצף המספרי)
5.  השחקן מקבל הודעה עם הקומבינציה והזכייה (אם קיימת).
-----------------
אלגוריתם:
1. אתחול: יצירת רשימה של 5 מספרים אקראיים מ-1 עד 13, המייצגים קלפים.
2. הצגת הקלפים על המסך.
3. בקשה מהשחקן אילו קלפים הוא רוצה להחליף:
    3.1. קבלת קלט מהשחקן ושמירת רשימת מספרי הקלפים להחלפה.
    3.2 אם השחקן הזין 0, עבור לשלב 5.
4. החלפת קלפים:
    4.1. עבור כל קלף ברשימה להחלפה - החלפתו במספר אקראי מ-1 עד 13.
    4.2. הצגת הקלפים המעודכנים על המסך.
5. ניתוח קומבינציה:
    5.1. ספירת מספר החזרות עבור כל ערך קלף.
    5.2. בדיקת הקומבינציות בסדר הבא:
        -   סטרייט (חמישה ערכים עוקבים).
        -   רביעייה (ארבעה זהים).
        -   פול האוס (שלושה זהים וזוג).
        -   שלישייה (שלושה זהים).
        -   שני זוגות (פעמיים שני זהים).
        -   זוג (שני זהים).
    5.3. אם נמצאה קומבינציה, הצגת שמה והזכייה.
6. הצגת הודעה על היעדר זכייה, אם קומבינציה לא נמצאה.
7. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeCards["אתחול 5 קלפים אקראיים (1-13)"]
    InitializeCards --> DisplayCards["הצגת קלפים"]
    DisplayCards --> InputReplaceCards["בקשת קלפים להחלפה"]
    InputReplaceCards --> CheckNoReplace{"השחקן הזין 0?"}
    CheckNoReplace -- כן --> AnalyzeHand["ניתוח קומבינציה"]
    CheckNoReplace -- לא --> ReplaceCards["החלפת קלפים"]
    ReplaceCards --> DisplayNewCards["הצגת קלפים חדשים"]
    DisplayNewCards --> AnalyzeHand
    AnalyzeHand --> CheckFlush{"סטרייט?"}
     CheckFlush -- כן --> OutputFlush["פלט: סטרייט וזכייה"]
      OutputFlush --> End["סיום"]
     CheckFlush -- לא --> CheckFourOfAKind{"רביעייה?"}
     CheckFourOfAKind -- כן --> OutputFourOfAKind["פלט: רביעייה וזכייה"]
     OutputFourOfAKind --> End
     CheckFourOfAKind -- לא --> CheckFullHouse{"פול האוס?"}
     CheckFullHouse -- כן --> OutputFullHouse["פלט: פול האוס וזכייה"]
     OutputFullHouse --> End
     CheckFullHouse -- לא --> CheckThreeOfAKind{"שלישייה?"}
     CheckThreeOfAKind -- כן --> OutputThreeOfAKind["פלט: שלישייה וזכייה"]
     OutputThreeOfAKind --> End
    CheckThreeOfAKind -- לא --> CheckTwoPairs{"שני זוגות?"}
    CheckTwoPairs -- כן --> OutputTwoPairs["פלט: שני זוגות וזכייה"]
    OutputTwoPairs --> End
    CheckTwoPairs -- לא --> CheckPair{"זוג?"}
    CheckPair -- כן --> OutputPair["פלט: זוג וזכייה"]
    OutputPair --> End
    CheckPair -- לא --> OutputNoWin["פלט: אין זכייה"]
    OutputNoWin --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeCards - אתחול 5 קלפים אקראיים (מספרים מ-1 עד 13).
    DisplayCards - הצגת הקלפים לשחקן על המסך.
    InputReplaceCards - בקשה מהשחקן אילו קלפים הוא רוצה להחליף (הזנת מספרי קלפים מופרדים ברווח).
    CheckNoReplace - בדיקה האם השחקן הזין 0, שמשמעותו היעדר החלפת קלפים.
    ReplaceCards - החלפת הקלפים שנבחרו על ידי השחקן בקלפים אקראיים חדשים.
    DisplayNewCards - הצגת הקלפים החדשים לאחר ההחלפה.
    AnalyzeHand - ניתוח קומבינציית הקלפים הנוכחית.
    CheckFlush - בדיקת קיום קומבינציית "סטרייט".
    OutputFlush - הצגת הודעה על זכייה עם קומבינציית "סטרייט".
    CheckFourOfAKind - בדיקת קיום קומבינציית "רביעייה".
    OutputFourOfAKind - הצגת הודעה על זכייה עם קומבינציית "רביעייה".
    CheckFullHouse - בדיקת קיום קומבינציית "פול האוס".
    OutputFullHouse - הצגת הודעה על זכייה עם קומבינציית "פול האוס".
    CheckThreeOfAKind - בדיקת קיום קומבינציית "שלישייה".
    OutputThreeOfAKind - הצגת הודעה על זכייה עם קומבינציית "שלישייה".
     CheckTwoPairs - בדיקת קיום קומבינציית "שני זוגות".
    OutputTwoPairs - הצגת הודעה על זכייה עם קומבינציית "שני זוגות".
    CheckPair - בדיקת קיום קומבינציית "זוג".
    OutputPair - הצגת הודעה על זכייה עם קומבינציית "זוג".
    OutputNoWin - הצגת הודעה על היעדר קומבינציה זוכה.
    End - סיום התוכנית.
```
import random

def create_hand():
    """יוצר יד של 5 קלפים אקראיים (מספרים מ-1 עד 13)."""
    hand = [random.randint(1, 13) for _ in range(5)]
    return hand

def display_hand(hand):
    """מציג את הקלפים על המסך, וממספר אותם לנוחות השחקן."""
    print("הקלפים שלך:")
    for i, card in enumerate(hand):
        print(f"{i+1}: {card}", end="  ")
    print()

def get_cards_to_replace():
    """מבקש מהשחקן את מספרי הקלפים להחלפה."""
    while True:
        try:
            replace_str = input("הזן את מספרי הקלפים להחלפה מופרדים ברווח (או 0 כדי להשאיר הכל): ")
            replace_cards = list(map(int, replace_str.split()))

            if len(replace_cards) == 1 and replace_cards[0] == 0:
                return []

            if all(1 <= card <= 5 for card in replace_cards) and len(replace_cards) <=5:
                    return [card - 1 for card in replace_cards]
            else:
                print("קלט לא חוקי. הזן מספרי קלפים מ-1 עד 5 או 0.")

        except ValueError:
            print("קלט לא חוקי. אנא הזן מספרים מופרדים ברווח.")


def replace_cards(hand, replace_indices):
    """מחליף את הקלפים שנבחרו בקלפים אקראיים חדשים."""
    for index in replace_indices:
        hand[index] = random.randint(1, 13)
    return hand

def analyze_hand(hand):
    """מנתח את היד וקובע את קומבינציית הזכייה."""
    counts = {}  # מילון לספירת חזרות קלפים
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    values = list(counts.values())  # רשימת מספר החזרות

    # בדיקה עבור סטרייט
    sorted_hand = sorted(hand)
    if len(set(sorted_hand)) == 5 and all(sorted_hand[i+1] - sorted_hand[i] == 1 for i in range(4)):
        print("סטרייט! זכייה של 20 נקודות")
        return

    # בדיקה עבור רביעייה
    if 4 in values:
        print("רביעייה! זכייה של 25 נקודות")
        return

    # בדיקה עבור פול האוס
    if 3 in values and 2 in values:
      print("פול האוס! זכייה של 15 נקודות")
      return

    # בדיקה עבור שלישייה
    if 3 in values:
        print("שלישייה! זכייה של 10 נקודות")
        return

    # בדיקה עבור שני זוגות
    if values.count(2) == 2:
        print("שני זוגות! זכייה של 5 נקודות")
        return

    # בדיקה עבור זוג
    if 2 in values:
        print("זוג! זכייה של 2 נקודות")
        return

    print("אין זכייה.")


# לוגיקת המשחק הראשית
def play_poker():
    """מפעיל את משחק הפוקר."""
    hand = create_hand() # יוצר יד של 5 קלפים
    display_hand(hand)  # מציג את הקלפים על המסך

    replace_indices = get_cards_to_replace() # מבקש קלפים להחלפה
    if replace_indices:
        hand = replace_cards(hand, replace_indices) # מחליף קלפים
        display_hand(hand) # מציג את הקלפים המעודכנים

    analyze_hand(hand) # מנתח את היד לנוכחות קומבינציה ומציג את התוצאה


if __name__ == "__main__":
    play_poker()

"""
הסבר קוד:
1. **ייבוא המודול `random`**:
   - `import random`: מייבא את המודול random, המשמש ליצירת מספרים אקראיים.
2. **פונקציה `create_hand()`**:
    - `def create_hand():`: מגדיר פונקציה שיוצרת יד של 5 קלפים.
    - `hand = [random.randint(1, 13) for _ in range(5)]`: יוצר רשימה של 5 מספרים שלמים אקראיים בטווח מ-1 עד 13 (המייצגים קלפים) ושומר במשתנה `hand`.
    - `return hand`: מחזיר את היד שנוצרה.
3. **פונקציה `display_hand(hand)`**:
   - `def display_hand(hand):`: מגדיר פונקציה להצגת הקלפים על המסך.
   - `print("הקלפים שלך:")`: מציג את הכותרת "הקלפים שלך:".
   - `for i, card in enumerate(hand):`:  לולאה עוברת על הקלפים, וממספרת אותם.
   - `print(f"{i+1}: {card}", end="  ")`: מציג את מספר הקלף ואת ערכו עם רווחים לנוחות.
   - `print()`: מציג שורה ריקה למעבר שורה.
4.  **פונקציה `get_cards_to_replace()`**:
    -   `def get_cards_to_replace():`:  מגדיר פונקציה לקבלת קלט מהמשתמש לגבי קלפים להחלפה.
    -   `while True:`: לולאה אינסופית עד שייקלט קלט תקין.
    -  `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערכים שאינם מספרים, תוצג הודעת שגיאה.
    -   `replace_str = input("הזן את מספרי הקלפים להחלפה מופרדים ברווח (או 0 כדי להשאיר הכל): ")`: מבקש מהמשתמש מחרוזת עם מספרי הקלפים להחלפה.
    -   `replace_cards = list(map(int, replace_str.split()))`: ממיר את המחרוזת שהוזנה לרשימת מספרים שלמים.
    -   `if len(replace_cards) == 1 and replace_cards[0] == 0:`: בודק אם המשתמש הזין 0, ואז מחזיר רשימה ריקה (להשאיר את כל הקלפים).
     -   `if all(1 <= card <= 5 for card in replace_cards) and len(replace_cards) <=5:`: בודק שכל מספרי הקלפים שהוזנו בטווח מ-1 עד 5.
    -  `return [card - 1 for card in replace_cards]`: מחזיר רשימת אינדקסים של קלפים להחלפה (אינדקסים מתחילים מ-0).
   -  `else:`: אם הקלט לא חוקי, מוצגת הודעת שגיאה.
5. **פונקציה `replace_cards(hand, replace_indices)`**:
   -  `def replace_cards(hand, replace_indices):`: מגדיר פונקציה להחלפת הקלפים שנבחרו.
   -  `for index in replace_indices:`: לולאה עוברת על אינדקסים של קלפים להחלפה.
   -   `hand[index] = random.randint(1, 13)`: מחליף את הקלף ביד במספר אקראי.
   -  `return hand`: מחזיר את היד המעודכנת.
6. **פונקציה `analyze_hand(hand)`**:
    -  `def analyze_hand(hand):`: מגדיר פונקציה לניתוח קומבינציות קלפים.
    - `counts = {}`: מילון לספירת חזרות קלפים.
    -  `for card in hand: counts[card] = counts.get(card, 0) + 1`: סופר את כמות כל קלף ביד.
    - `values = list(counts.values())`: רשימה עם כמות חזרות הקלפים.
    -   **בדיקה עבור סטרייט**:
        -   `sorted_hand = sorted(hand)`: ממיין את היד.
        -   `if len(set(sorted_hand)) == 5 and all(sorted_hand[i+1] - sorted_hand[i] == 1 for i in range(4))`: בדיקה שכל הקלפים ביד ייחודיים ובסדר עוקב.
        -   `print("סטרייט! זכייה של 20 נקודות")`: הצגת הודעה על סטרייט.
        -   `return`: מסיים את ביצוע הפונקציה.
    -   **בדיקה עבור רביעייה**:
        -   `if 4 in values:`: בודק האם קיימים 4 קלפים זהים.
        -   `print("רביעייה! זכייה של 25 נקודות")`: הצגת הודעה על רביעייה.
        -   `return`: מסיים את ביצוע הפונקציה.
    -   **בדיקה עבור פול האוס**:
        -   `if 3 in values and 2 in values:`: בודק האם קיימים שלושה קלפים זהים וזוג.
        -   `print("פול האוס! זכייה של 15 נקודות")`: הצגת הודעה על פול האוס.
        -   `return`: מסיים את ביצוע הפונקציה.
    -   **בדיקה עבור שלישייה**:
        -  `if 3 in values:`: בודק האם קיימים שלושה קלפים זהים.
        -  `print("שלישייה! זכייה של 10 נקודות")`: הצגת הודעה על שלישייה.
        -   `return`: מסיים את ביצוע הפונקציה.
    -   **בדיקה עבור שני זוגות**:
         - `if values.count(2) == 2:`: בודק האם קיימים שני זוגות.
         - `print("שני זוגות! זכייה של 5 נקודות")`: הצגת הודעה על שני זוגות.
         - `return`: מסיים את ביצוע הפונקציה.
    -   **בדיקה עבור זוג**:
        -   `if 2 in values:`: בודק האם קיים זוג.
        -   `print("זוג! זכייה של 2 נקודות")`: הצגת הודעה על זוג.
        -   `return`: מסיים את ביצוע הפונקציה.
    -   `print("אין זכייה.")`: הצגת הודעה על היעדר זכייה.
7.  **פונקציה `play_poker()`**:
    - `def play_poker():`: מגדיר פונקציה להפעלת המשחק.
    -   `hand = create_hand()`: יוצר יד.
    -   `display_hand(hand)`: מציג את הקלפים על המסך.
    -   `replace_indices = get_cards_to_replace()`: מקבל את מספרי הקלפים להחלפה.
    -  `if replace_indices:`: בודק שהרשימה עם הקלפים להחלפה אינה ריקה.
    -   `hand = replace_cards(hand, replace_indices)`: מחליף קלפים.
    -   `display_hand(hand)`: מציג את הקלפים המעודכנים.
    -   `analyze_hand(hand)`: מנתח את היד ומציג את התוצאה.
8. **הפעלת המשחק**:
   -   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_poker()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
   -   `play_poker()`: קורא לפונקציה כדי להתחיל את המשחק.
"""