<POKER>:
=================
רמת קושי: 5
-----------------
המשחק "פוקר" הינו גרסה מפושטת של פוקר קלפים לשחקן יחיד. השחקן מקבל חמישה קלפים, המיוצגים על ידי מספרים מ-1 עד 13 (כאשר 1 - אס, 11 - נסיך, 12 - מלכה, 13 - מלך). השחקן רשאי להשאיר או להחליף כל מספר של קלפים פעם אחת. לאחר מכן, מוצגת קומבינציית הקלפים והזכייה, אם קיימת.

כללי המשחק:
1.  השחקן מתחיל עם חמישה קלפים אקראיים מ-1 עד 13.
2.  השחקן יכול לבחור אילו קלפים להשאיר ואילו להחליף, על ידי הזנת מספרי הקלפים בהפרדה ברווח (לדוגמה "1 3 5"), או 0 כדי להשאיר הכל כפי שהוא.
3.  הקלפים שהוחלפו מוחלפים בקלפים אקראיים חדשים.
4.  לאחר החלפת הקלפים, נקבעת הקומבינציה:
    -   זוג (שני ערכים זהים)
    -   שני זוגות (פעמיים שני ערכים זהים)
    -   שלשה (שלושה ערכים זהים)
    -   פול האוס (שלושה ערכים זהים + זוג)
    -   רביעייה (ארבעה ערכים זהים)
    -   סטרייט (חמישה ערכים עוקבים)
    -   פלאש (חמישה קלפים מאותה סדרה; ביישום זה, הסדרה אינה נלקחת בחשבון, רק הרצף המספרי)
5.  השחקן מקבל הודעה עם הקומבינציה והזכייה (אם קיימת).
-----------------
אלגוריתם:
1. אתחול: יצירת רשימה של 5 מספרים אקראיים מ-1 עד 13, המייצגים קלפים.
2. הצגת הקלפים על המסך.
3. בקשה מהשחקן אילו קלפים ברצונו להחליף:
    3.1. קבלת קלט השחקן ושמירת רשימת מספרי הקלפים להחלפה.
    3.2. אם השחקן הזין 0, עבור לשלב 5.
4. החלפת קלפים:
    4.1. עבור כל קלף ברשימה להחלפה - החלף אותו במספר אקראי מ-1 עד 13.
    4.2. הצגת הקלפים המעודכנים על המסך.
5. ניתוח קומבינציה:
    5.1. ספירת כמות החזרות עבור כל ערך קלף.
    5.2. בדיקת קומבינציות בסדר הבא:
        -   סטרייט (חמישה ערכים עוקבים).
        -   רביעייה (ארבעה זהים).
        -   פול האוס (שלושה זהים וזוג).
        -   שלשה (שלושה זהים).
        -   שני זוגות (פעמיים שניים זהים).
        -   זוג (שניים זהים).
    5.3. אם נמצאה קומבינציה, הצג את שמה ואת הזכייה.
6. הצגת הודעה על היעדר זכייה אם לא נמצאה קומבינציה.
7. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeCards["אתחול 5 קלפים אקראיים (1-13)"]
    InitializeCards --> DisplayCards["הצגת קלפים"]
    DisplayCards --> InputReplaceCards["בקשת קלפים להחלפה"]
    InputReplaceCards --> CheckNoReplace{"השחקן הזין 0?"}
    CheckNoReplace -- Да --> AnalyzeHand["ניתוח קומבינציה"]
    CheckNoReplace -- Нет --> ReplaceCards["החלפת קלפים"]
    ReplaceCards --> DisplayNewCards["הצגת קלפים חדשים"]
    DisplayNewCards --> AnalyzeHand
    AnalyzeHand --> CheckFlush{"פלאש?"}
     CheckFlush -- Да --> OutputFlush["פלט: פלאש וזכייה"]
      OutputFlush --> End["סיום"]
     CheckFlush -- Нет --> CheckFourOfAKind{"רביעייה?"}
     CheckFourOfAKind -- Да --> OutputFourOfAKind["פלט: רביעייה וזכייה"]
     OutputFourOfAKind --> End
     CheckFourOfAKind -- Нет --> CheckFullHouse{"פול האוס?"}
     CheckFullHouse -- Да --> OutputFullHouse["פלט: פול האוס וזכייה"]
     OutputFullHouse --> End
     CheckFullHouse -- Нет --> CheckThreeOfAKind{"שלשה?"}
     CheckThreeOfAKind -- Да --> OutputThreeOfAKind["פלט: שלשה וזכייה"]
     OutputThreeOfAKind --> End
    CheckThreeOfAKind -- Нет --> CheckTwoPairs{"שני זוגות?"}
    CheckTwoPairs -- Да --> OutputTwoPairs["פלט: שני זוגות וזכייה"]
    OutputTwoPairs --> End
    CheckTwoPairs -- Нет --> CheckPair{"זוג?"}
    CheckPair -- Да --> OutputPair["פלט: זוג וזכייה"]
    OutputPair --> End
    CheckPair -- Нет --> OutputNoWin["פלט: אין זכייה"]
    OutputNoWin --> End
```

מקרא:
    Start - התחלת התוכנית.
    InitializeCards - אתחול 5 קלפים אקראיים (מספרים מ-1 עד 13).
    DisplayCards - הצגת הקלפים לשחקן על המסך.
    InputReplaceCards - בקשה מהשחקן אילו קלפים ברצונו להחליף (הזנת מספרי הקלפים בהפרדה ברווח).
    CheckNoReplace - בדיקה האם השחקן הזין 0, המציין היעדר החלפת קלפים.
    ReplaceCards - החלפת הקלפים שנבחרו על ידי השחקן בקלפים אקראיים חדשים.
    DisplayNewCards - הצגת הקלפים החדשים לאחר ההחלפה.
    AnalyzeHand - ניתוח הקומבינציה הנוכחית של הקלפים.
    CheckFlush - בדיקת קיום קומבינציית "פלאש".
    OutputFlush - הצגת הודעה על זכייה עם קומבינציית "פלאש".
    CheckFourOfAKind - בדיקת קיום קומבינציית "רביעייה".
    OutputFourOfAKind - הצגת הודעה על זכייה עם קומבינציית "רביעייה".
    CheckFullHouse - בדיקת קיום קומבינציית "פול האוס".
    OutputFullHouse - הצגת הודעה על זכייה עם קומבינציית "פול האוס".
    CheckThreeOfAKind - בדיקת קיום קומבינציית "שלשה".
    OutputThreeOfAKind - הצגת הודעה על זכייה עם קומבינציית "שלשה".
    CheckTwoPairs - בדיקת קיום קומבינציית "שני זוגות".
    OutputTwoPairs - הצגת הודעה על זכייה עם קומבינציית "שני זוגות".
    CheckPair - בדיקת קיום קומבינציית "זוג".
    OutputPair - הצגת הודעה על זכייה עם קומבינציית "זוג".
    OutputNoWin - הצגת הודעה על היעדר קומבינציה מזכה.
    End - סיום התוכנית.
"""
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
    """מבקש מהשחקן את מספרי הקלפים שיש להחליף."""
    while True:
        try:
            replace_str = input("הזן את מספרי הקלפים להחלפה בהפרדה ברווח (או 0 כדי להשאיר את כולם): ")
            replace_cards = list(map(int, replace_str.split()))

            if len(replace_cards) == 1 and replace_cards[0] == 0:
                return []

            if all(1 <= card <= 5 for card in replace_cards) and len(replace_cards) <=5:
                    return [card - 1 for card in replace_cards]
            else:
                print("קלט שגוי. הזן מספרי קלפים בין 1 ל-5 או 0.")

        except ValueError:
            print("קלט שגוי. אנא הזן את המספרים בהפרדה ברווח.")


def replace_cards(hand, replace_indices):
    """מחליף את הקלפים שנבחרו בקלפים אקראיים חדשים."""
    for index in replace_indices:
        hand[index] = random.randint(1, 13)
    return hand

def analyze_hand(hand):
    """מנתח את היד וקובע את הקומבינציה המזכה."""
    counts = {}  # מילון לספירת חזרות של קלפים
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    values = list(counts.values())  # רשימת כמות החזרות

    # בדיקה עבור פלאש (סטרייט לפי הגדרת המסמך - חמישה ערכים עוקבים)
    sorted_hand = sorted(hand)
    if len(set(sorted_hand)) == 5 and all(sorted_hand[i+1] - sorted_hand[i] == 1 for i in range(4)):
        print("פלאש! זכייה ב-20 נקודות") # הפלט משתמש במונח "פלאש"
        return

    # בדיקה עבור רביעייה
    if 4 in values:
        print("רביעייה! זכייה ב-25 נקודות")
        return

    # בדיקה עבור פול האוס
    if 3 in values and 2 in values:
      print("פול האוס! זכייה ב-15 נקודות")
      return

    # בדיקה עבור שלשה
    if 3 in values:
        print("שלשה! זכייה ב-10 נקודות")
        return

    # בדיקה עבור שני זוגות
    if values.count(2) == 2:
        print("שני זוגות! זכייה ב-5 נקודות")
        return

    # בדיקה עבור זוג
    if 2 in values:
        print("זוג! זכייה ב-2 נקודות")
        return

    print("אין זכייה.")


# לוגיקת המשחק העיקרית
def play_poker():
    """מפעיל את משחק הפוקר."""
    hand = create_hand() # יוצרים יד של 5 קלפים
    display_hand(hand)  # מציגים את הקלפים על המסך

    replace_indices = get_cards_to_replace() # מבקשים קלפים להחלפה
    if replace_indices:
        hand = replace_cards(hand, replace_indices) # מחליפים קלפים
        display_hand(hand) # מציגים את הקלפים המעודכנים

    analyze_hand(hand) # מנתחים את היד עבור קומבינציה ומציגים את התוצאה


if __name__ == "__main__":
    play_poker()

"""
הסבר הקוד:
1. **ייבוא מודול `random`**:
   - `import random`: מייבא את מודול random, המשמש ליצירת מספרים אקראיים.
2. **פונקציה `create_hand()`**:
    - `def create_hand():`: מגדירה פונקציה שיוצרת יד של 5 קלפים.
    - `hand = [random.randint(1, 13) for _ in range(5)]`: יוצרת רשימה של 5 מספרים שלמים אקראיים בטווח מ-1 עד 13 (המייצגים קלפים) ושומרת במשתנה `hand`.
    - `return hand`: מחזירה את היד שנוצרה.
3. **פונקציה `display_hand(hand)`**:
   - `def display_hand(hand):`: מגדירה פונקציה להצגת הקלפים על המסך.
   - `print("הקלפים שלך:")`: מציגה את הכותרת "הקלפים שלך:".
   - `for i, card in enumerate(hand):`: לולאה שעוברת על הקלפים, וממספרת אותם.
   - `print(f"{i+1}: {card}", end="  ")`: מציגה את מספר הקלף ואת ערכו עם רווחים לנוחות.
   - `print()`: מציגה שורה ריקה למעבר שורה.
4.  **פונקציה `get_cards_to_replace()`**:
    -   `def get_cards_to_replace():`: מגדירה פונקציה לקבלת קלט המשתמש לגבי הקלפים להחלפה.
    -   `while True:`: לולאה אינסופית עד לקבלת קלט תקין.
    -  `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין ערכים שאינם מספרים, תוצג הודעת שגיאה.
    -   `replace_str = input("הזן את מספרי הקלפים להחלפה בהפרדה ברווח (או 0 כדי להשאיר את כולם): ")`: מבקשת מהמשתמש מחרוזת עם מספרי הקלפים להחלפה.
    -   `replace_cards = list(map(int, replace_str.split()))`: ממירה את המחרוזת שהוזנה לרשימה של מספרים שלמים.
    -   `if len(replace_cards) == 1 and replace_cards[0] == 0:`: בודקת אם המשתמש הזין 0, במקרה זה מחזירה רשימה ריקה (להשאיר את כל הקלפים).
    -   `if all(1 <= card <= 5 for card in replace_cards) and len(replace_cards) <=5:`: בודקת שכל מספרי הקלפים שהוזנו בטווח 1 עד 5.
    -  `return [card - 1 for card in replace_cards]`: מחזירה רשימה של אינדקסים (מבוססי 0) של הקלפים להחלפה.
   -  `else:`: אם הקלט שגוי, מוצגת הודעת שגיאה.
5. **פונקציה `replace_cards(hand, replace_indices)`**:
   -  `def replace_cards(hand, replace_indices):`: מגדירה פונקציה להחלפת הקלפים שנבחרו.
   -  `for index in replace_indices:`: לולאה שעוברת על האינדקסים של הקלפים להחלפה.
   -   `hand[index] = random.randint(1, 13)`: מחליפה את הקלף ביד במספר אקראי.
   -  `return hand`: מחזירה את היד המעודכנת.
6. **פונקציה `analyze_hand(hand)`**:
    -  `def analyze_hand(hand):`: מגדירה פונקציה לניתוח קומבינציות הקלפים.
    - `counts = {}`: מילון לספירת חזרות של קלפים.
    -  `for card in hand: counts[card] = counts.get(card, 0) + 1`: סופרת את כמות כל קלף ביד.
    - `values = list(counts.values())`: רשימה המכילה את כמות החזרות של הקלפים.
    -   **בדיקה עבור פלאש (סטרייט):**
        -   `sorted_hand = sorted(hand)`: ממיין את היד.
        -   `if len(set(sorted_hand)) == 5 and all(sorted_hand[i+1] - sorted_hand[i] == 1 for i in range(4))`: בודקת שכל הקלפים ביד ייחודיים ועוקבים בסדר.
        -   `print("פלאש! זכייה ב-20 נקודות")`: הצגת הודעה על פלאש.
        -   `return`: מסיימת את ביצוע הפונקציה.
    -   **בדיקה עבור רביעייה:**
        -   `if 4 in values:`: בודקת אם קיימים 4 קלפים זהים.
        -   `print("רביעייה! זכייה ב-25 נקודות")`: הצגת הודעה על רביעייה.
        -   `return`: מסיימת את ביצוע הפונקציה.
    -   **בדיקה עבור פול האוס:**
        -   `if 3 in values and 2 in values:`: בודקת אם קיימים שלושה קלפים זהים וזוג.
        -   `print("פול האוס! זכייה ב-15 נקודות")`: הצגת הודעה על פול האוס.
        -   `return`: מסיימת את ביצוע הפונקציה.
    -   **בדיקה עבור שלשה:**
        -  `if 3 in values:`: בודקת אם קיימים שלושה קלפים זהים.
        -  `print("שלשה! זכייה ב-10 נקודות")`: הצגת הודעה על שלשה.
        -   `return`: מסיימת את ביצוע הפונקציה.
    -   **בדיקה עבור שני זוגות:**
         - `if values.count(2) == 2:`: בודקת אם קיימים שני זוגות.
         - `print("שני זוגות! זכייה ב-5 נקודות")`: הצגת הודעה על שני זוגות.
         - `return`: מסיימת את ביצוע הפונקציה.
    -   **בדיקה עבור זוג:**
        -   `if 2 in values:`: בודקת אם קיים זוג.
        -   `print("זוג! זכייה ב-2 נקודות")`: הצגת הודעה על זוג.
        -   `return`: מסיימת את ביצוע הפונקציה.
    -   `print("אין זכייה.")`: הצגת הודעה על היעדר זכייה.
7.  **פונקציה `play_poker()`**:
    - `def play_poker():`: מגדירה פונקציה להפעלת המשחק.
    -   `hand = create_hand()`: יוצרת יד.
    -   `display_hand(hand)`: מציגה את הקלפים על המסך.
    -   `replace_indices = get_cards_to_replace()`: מקבלת את מספרי הקלפים להחלפה.
    -  `if replace_indices:`: בודקת שהרשימה עם הקלפים להחלפה אינה ריקה.
    -   `hand = replace_cards(hand, replace_indices)`: מחליפה את הקלפים.
    -   `display_hand(hand)`: מציגה את הקלפים המעודכנים.
    -   `analyze_hand(hand)`: מנתחת את היד ומציגה את התוצאה.
8. **הפעלת המשחק**:
   -   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_poker()` תופעל רק אם הקובץ מבוצע ישירות, ולא מיובא כמודול.
   -   `play_poker()`: קורא לפונקציה כדי להתחיל את המשחק.
"""