"""
<BINGO>:
=================
דרגת קושי: 4
-----------------
המשחק "בינגו" מהווה גרסה פשוטה של המשחק הקלאסי, שבה נוצר כרטיס אקראי בגודל 5x5 עם מספרים מ-1 עד 75 (לא כולל מספרים המתחלקים ב-10, כגון 10, 20, 30 וכו').
הכרטיס מוצג למשתמש, ולאחר מכן נקראים מספרים אקראיים מ-1 עד 75.
אם המספר שנקרא קיים על הכרטיס, הוא מסומן.
המשחק מסתיים כאשר כל המספרים על הכרטיס מסומנים.

כללי המשחק:
1. נוצר כרטיס משחק 5x5 עם מספרים אקראיים ייחודיים מ-1 עד 75, למעט מספרים המתחלקים ב-10.
2. השחקן מקבל ברצף קריאה של מספרים אקראיים מ-1 עד 75.
3. אם המספר שנקרא קיים על הכרטיס, הוא מסומן (מוחלף ב-0).
4. המשחק נמשך עד שכל המספרים על הכרטיס מסומנים.
5. לאחר סיום המשחק, מוצגת הודעת ניצחון.
-----------------
אלגוריתם:
1. אתחול כרטיס BINGO:
    1.1 יצירת מטריצה ריקה 5x5.
    1.2 מילוי המטריצה במספרים אקראיים ייחודיים מ-1 עד 75, למעט מספרים המתחלקים ב-10.
2. התחלת לולאה "כל עוד ישנם מספרים לא מסומנים על הכרטיס":
    2.1 יצירת מספר אקראי מ-1 עד 75.
    2.2 הצגת המספר האקראי למשתמש.
    2.3 בדיקה האם המספר קיים על הכרטיס:
        2.3.1 אם המספר קיים, החלפתו במטריצה ב-0.
        2.3.2 אם המספר אינו קיים, דילוג על התור.
    2.4 הצגת הכרטיס בקונסול.
3. הצגת ההודעה "BINGO!".
4. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBingoCard["<p align='left'>אתחול כרטיס BINGO:
    <code><b>
    bingoCard = 5x5 matrix
    Fill bingoCard with random unique numbers from 1 to 75 (not divisible by 10)
    </b></code></p>"]
    InitializeBingoCard --> LoopStart{"תחילת לולאה: כל עוד לא כל המספרים סומנו"}
    LoopStart -- Да --> GenerateRandomNumber["<code><b>randomNumber = random(1, 75)</b></code>"]
    GenerateRandomNumber --> OutputRandomNumber["הצגת מספר: <code><b>randomNumber</b></code>"]
    OutputRandomNumber --> CheckNumberInCard{"בדיקה: <code><b>randomNumber</b></code> נמצא ב-<code><b>bingoCard</b></code>?"}
    CheckNumberInCard -- Да --> MarkNumberOnCard["החלפת <code><b>randomNumber</b></code> ב-0 ב-<code><b>bingoCard</b></code>"]
    MarkNumberOnCard --> OutputBingoCard["הצגת כרטיס <code><b>bingoCard</b></code>"]
    OutputBingoCard --> LoopStart
    CheckNumberInCard -- Нет --> OutputBingoCard
    LoopStart -- Нет --> OutputWin["הצגת הודעה: <b>BINGO!</b>"]
    OutputWin --> End["סיום"]
```

מקרא:
    Start - תחילת המשחק.
    InitializeBingoCard - אתחול כרטיס המשחק BINGO: נוצרת מטריצה 5x5, הממולאת במספרים אקראיים ייחודיים מ-1 עד 75 (לא המתחלקים ב-10).
    LoopStart - תחילת לולאה שנמשכת כל עוד לא כל המספרים על הכרטיס מסומנים.
    GenerateRandomNumber - יצירת מספר אקראי מ-1 עד 75.
    OutputRandomNumber - הצגת המספר האקראי שנוצר על המסך למשתמש.
    CheckNumberInCard - בדיקה האם המספר שנוצר קיים על כרטיס המשחק.
    MarkNumberOnCard - אם המספר קיים על הכרטיס, הוא מוחלף ב-0 (מסומן).
    OutputBingoCard - הצגת המצב הנוכחי של כרטיס המשחק על המסך.
    OutputWin - הצגת הודעת הניצחון "BINGO!", כאשר כל המספרים על הכרטיס מסומנים.
    End - סיום המשחק.
"""
import random

def create_bingo_card():
    """
    יוצר ומחזיר כרטיס בינגו בגודל 5x5.
    
    הכרטיס מכיל מספרים אקראיים ייחודיים מ-1 עד 75, למעט מספרים המתחלקים ב-10.
    
    Returns:
      list of lists: כרטיס הבינגו.
    """
    card = []
    numbers = [i for i in range(1, 76) if i % 10 != 0] # יצירת רשימת מספרים מ-1 עד 75, לא המתחלקים ב-10
    random.shuffle(numbers) # ערבוב הרשימה

    # מילוי הכרטיס במספרים מהרשימה המעורבבת
    for i in range(5):
        row = []
        for j in range(5):
            row.append(numbers.pop())
        card.append(row)
    return card

def print_bingo_card(card):
    """
    מציג את כרטיס הבינגו בקונסול.
    
    Args:
        card (list of lists): כרטיס הבינגו להצגה.
    """
    for row in card:
      print(" ".join(str(x).rjust(2) for x in row))
    print()
    
def mark_number(card, number):
  """
    מסמן מספר על כרטיס הבינגו על ידי החלפתו ב-0.

    Args:
      card (list of lists): כרטיס הבינגו.
      number (int): המספר לסימון.
  """
  for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == number:
                card[i][j] = 0
                return

def is_bingo(card):
    """
    בדיקה האם כל המספרים על כרטיס הבינגו סומנו (הוחלפו ב-0).
    
    Args:
        card (list of lists): כרטיס הבינגו לבדיקה.
    
    Returns:
        bool: True אם כל המספרים סומנו, אחרת False.
    """
    for row in card:
        for num in row:
            if num != 0:
                return False
    return True
  
def play_bingo():
    """
    מפעיל את המשחק "בינגו".
    
    יוצר כרטיס בינגו, מציג אותו על המסך, ומבקש מהמשתמש להזין מספרים.
    המשחק מסתיים כאשר כל המספרים על הכרטיס מסומנים.
    """
    bingo_card = create_bingo_card() # יצירת כרטיס המשחק
    print("הכרטיס BINGO שלך:")
    print_bingo_card(bingo_card) # הצגת הכרטיס על המסך

    called_numbers = set() # קבוצה למעקב אחר מספרים שכבר נקראו

    while not is_bingo(bingo_card): # לולאת המשחק
       number = random.randint(1, 75) # יצירת מספר אקראי חדש
       
       while number in called_numbers:
        number = random.randint(1, 75) # יצירת מספר אקראי חדש, אם מספר זה כבר נקרא
       
       called_numbers.add(number) # רישום המספר כאחד שכבר נקרא
       print(f"המספר שהוגרל: {number}")
       mark_number(bingo_card,number)
       print_bingo_card(bingo_card) # הצגת הכרטיס על המסך
    print("BINGO!")

if __name__ == "__main__":
    play_bingo()
    
"""
הסבר קוד:

1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים ולערבוב רשימות.

2.  **פונקציה `create_bingo_card()`**:
    -   `def create_bingo_card():`: מגדירה פונקציה שיוצרת ומחזירה כרטיס בינגו.
    -   `card = []`: מאתחל רשימה ריקה `card`, שתייצג מטריצה 5x5 (כרטיס בינגו).
    -   `numbers = [i for i in range(1, 76) if i % 10 != 0]`: יוצר רשימת מספרים מ-1 עד 75, למעט מספרים המתחלקים ב-10.
    -   `random.shuffle(numbers)`: מערבב את רשימת המספרים באופן אקראי.
    -   **מילוי הכרטיס**:
        -   לולאות מקוננות `for i in range(5)` ו-`for j in range(5)`: עוברות על כל התאים במטריצה 5x5.
        -   `row.append(numbers.pop())`: שולף את המספר האחרון מרשימת `numbers` ומוסיף אותו לשורה הנוכחית של הכרטיס.
        -   `card.append(row)`: מוסיף את השורה שנוצרה לכרטיס.
    -   `return card`: מחזיר את כרטיס הבינגו המוכן.

3.  **פונקציה `print_bingo_card(card)`**:
    -   `def print_bingo_card(card):`: מגדירה פונקציה שמציגה את כרטיס הבינגו על המסך.
    -   לולאה `for row in card`: עוברת על כל השורות בכרטיס.
    -   `print(" ".join(str(x).rjust(2) for x in row))`: מציג את השורה הנוכחית. `str(x).rjust(2)` ממיר כל מספר למחרוזת, מיישר אותו לימין עד ל-2 תווים, ו-" ".join() מכניס רווחים בין המספרים.
    -   `print()`: מוסיף שורה ריקה לאחר הצגת הכרטיס לצורך עיצוב טוב יותר.

4.  **פונקציה `mark_number(card, number)`**:
    -   `def mark_number(card, number):`: מגדירה פונקציה שמסמנת מספר על כרטיס הבינגו.
    -   **חיפוש והחלפת המספר**:
        -   לולאות מקוננות `for i in range(len(card))` ו-`for j in range(len(card[i]))`: עוברות על כל התאים בכרטיס.
        -   `if card[i][j] == number:`: בודק האם המספר הנוכחי שווה למספר המבוקש.
        -   `card[i][j] = 0`: אם המספר נמצא, הוא מוחלף ב-0.
        -   `return`: מסיים את הפונקציה לאחר ההחלפה הראשונה.

5.  **פונקציה `is_bingo(card)`**:
    -   `def is_bingo(card):`: מגדירה פונקציה שבודקת האם כל המספרים על הכרטיס סומנו.
    -   **בדיקת כל המספרים**:
        -   לולאה `for row in card`: עוברת על כל השורות בכרטיס.
        -   לולאה `for num in row`: עוברת על כל המספרים בשורה הנוכחית.
        -   `if num != 0:`: אם נמצא מספר לא מסומן (שאינו שווה ל-0), מחזיר `False`.
    -   `return True`: אם כל המספרים סומנו, מחזיר `True`.

6.  **פונקציה `play_bingo()`**:
    -   `def play_bingo():`: מגדירה פונקציה שמפעילה את המשחק "בינגו".
    -   `bingo_card = create_bingo_card()`: יוצר כרטיס בינגו.
    -   `print("הכרטיס BINGO שלך:")`: מציג הודעה על תחילת המשחק.
    -   `print_bingo_card(bingo_card)`: מציג את הכרטיס על המסך.
    -   `called_numbers = set()`: יוצר קבוצה לאחסון מספרים שכבר נקראו, כדי למנוע חזרות.
    -   **לולאת המשחק**:
        -   `while not is_bingo(bingo_card)`: מתבצעת כל עוד ישנם מספרים לא מסומנים על הכרטיס.
        -   `number = random.randint(1, 75)`: יוצר מספר אקראי.
        -   `while number in called_numbers`: יוצר מספר חדש עד שהוא אינו נמצא ברשימת המספרים שכבר נקראו.
        -   `called_numbers.add(number)`: מוסיף את המספר לרשימת המספרים שנקראו.
        -   `print(f"המספר שהוגרל: {number}")`: מציג את המספר שהוגרל.
        -   `mark_number(bingo_card, number)`: מסמן את המספר על הכרטיס.
        -   `print_bingo_card(bingo_card)`: מציג את הכרטיס המעודכן על המסך.
    -   `print("BINGO!")`: מציג הודעת ניצחון כאשר כל המספרים סומנו.

7.  **הפעלה מותנית של המשחק**:
    -   `if __name__ == "__main__":`: בודק שהקובץ מופעל כראשי, ולא יובא כמודול.
    -   `play_bingo()`: קורא לפונקציה `play_bingo()` כדי להפעיל את המשחק.
"""