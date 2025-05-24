<BINGO>:
=================
מורכבות: 4
-----------------
המשחק "בינגו" מהווה גרסה מפושטת של המשחק הקלאסי, בה נוצר כרטיס אקראי בגודל 5x5 עם מספרים מ-1 עד 75 (לא כולל מספרים המתחלקים ב-10, כגון 10, 20, 30 וכו').
הכרטיס מוצג למשתמש, ולאחר מכן מוכרזים מספרים אקראיים מ-1 עד 75.
אם המספר שהוכרז נמצא על הכרטיס, הוא מסומן.
המשחק מסתיים כאשר כל המספרים על הכרטיס סומנו.

חוקי המשחק:
1. נוצר כרטיס משחק בגודל 5x5 עם מספרים אקראיים מ-1 עד 75, למעט מספרים המתחלקים ב-10.
2. לשחקן מוכרזים מספרים אקראיים מ-1 עד 75 בזה אחר זה.
3. אם המספר שהוכרז נמצא על הכרטיס, הוא מסומן (מוחלף ב-0).
4. המשחק נמשך עד שכל המספרים על הכרטיס מסומנים.
5. בסיום המשחק מוצגת הודעת ניצחון.
-----------------
אלגוריתם:
1. אתחול כרטיס BINGO:
    1.1 יצירת מטריצה ריקה בגודל 5x5.
    1.2 מילוי המטריצה במספרים אקראיים ייחודיים מ-1 עד 75, למעט מספרים המתחלקים ב-10.
2. תחילת לולאה "כל עוד יש מספרים שלא סומנו על הכרטיס":
    2.1 ייצור מספר אקראי מ-1 עד 75.
    2.2 הצגת המספר האקראי למשתמש.
    2.3 בדיקה האם המספר נמצא על הכרטיס:
        2.3.1 אם המספר נמצא, החלפתו במטריצה ב-0.
        2.3.2 אם המספר אינו נמצא, דילוג על מהלך.
    2.4 הצגת הכרטיס בקונסול.
3. הצגת הודעת "BINGO!".
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
    LoopStart -- כן --> GenerateRandomNumber["<code><b>randomNumber = random(1, 75)</b></code>"]
    GenerateRandomNumber --> OutputRandomNumber["הצגת המספר: <code><b>randomNumber</b></code>"]
    OutputRandomNumber --> CheckNumberInCard{"בדיקה: <code><b>randomNumber</b></code> נמצא ב- <code><b>bingoCard</b></code>?"}
    CheckNumberInCard -- כן --> MarkNumberOnCard["החלף את <code><b>randomNumber</b></code> ב-0 ב- <code><b>bingoCard</b></code>"]
    MarkNumberOnCard --> OutputBingoCard["הצגת הכרטיס <code><b>bingoCard</b></code>"]
    OutputBingoCard --> LoopStart
    CheckNumberInCard -- לא --> OutputBingoCard
    LoopStart -- לא --> OutputWin["הצגת הודעה: <b>BINGO!</b>"]
    OutputWin --> End["סיום"]
```

מקרא:
    Start - התחלת המשחק.
    InitializeBingoCard - אתחול כרטיס המשחק BINGO: נוצרת מטריצה בגודל 5x5, המלאה במספרים אקראיים ייחודיים מ-1 עד 75 (שאינם מתחלקים ב-10).
    LoopStart - תחילת הלולאה, הנמשכת כל עוד לא כל המספרים על הכרטיס סומנו.
    GenerateRandomNumber - ייצור מספר אקראי מ-1 עד 75.
    OutputRandomNumber - הצגת המספר האקראי שנוצר על המסך למשתמש.
    CheckNumberInCard - בדיקה האם המספר שנוצר נמצא על כרטיס המשחק.
    MarkNumberOnCard - אם המספר נמצא על הכרטיס, הוא מוחלף ב-0 (מסומן).
    OutputBingoCard - הצגת המצב הנוכחי של כרטיס המשחק על המסך.
    OutputWin - הצגת הודעת ניצחון "BINGO!", כאשר כל המספרים על הכרטיס סומנו.
    End - סיום המשחק.
```
import random

def create_bingo_card():
    """
    יוצר ומחזיר כרטיס בינגו בגודל 5x5.

    הכרטיס מכיל מספרים אקראיים ייחודיים מ-1 עד 75, למעט מספרים המתחלקים ב-10.

    Returns:
      list of lists: כרטיס הבינגו.
    """
    card = []
    numbers = [i for i in range(1, 76) if i % 10 != 0] # יוצר רשימה של מספרים מ-1 עד 75, לא כולל כפילויות של 10
    random.shuffle(numbers) # מערבב את הרשימה

    # ממלא את הכרטיס במספרים מהרשימה המעורבבת
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
    מסמן מספר על כרטיס הבינגו, על ידי החלפתו ב-0.

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
    בודק האם כל המספרים על כרטיס הבינגו סומנו (הוחלפו ב-0).

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
    מריץ את המשחק "בינגו".

    יוצר כרטיס בינגו, מציג אותו על המסך, ומבקש מהמשתמש להכריז על מספרים.
    המשחק מסתיים כאשר כל המספרים על הכרטיס סומנו.
    """
    bingo_card = create_bingo_card() # יוצר כרטיס משחק
    print("Your BINGO card:")
    print_bingo_card(bingo_card) # מציג את הכרטיס על המסך

    called_numbers = set() # סט למעקב אחר מספרים שכבר נקראו

    while not is_bingo(bingo_card): # לולאת המשחק
       number = random.randint(1, 75) # מייצר מספר אקראי חדש

       while number in called_numbers:
        number = random.randint(1, 75) # מייצר מספר אקראי חדש אם הוא כבר נקרא

       called_numbers.add(number) # מוסיף את המספר לסט המספרים שנקראו
       print(f"Called number: {number}")
       mark_number(bingo_card,number) # מסמן את המספר על הכרטיס.
       print_bingo_card(bingo_card) # מציג את הכרטיס על המסך
    print("BINGO!")

if __name__ == "__main__":
    play_bingo()

"""
הסבר קוד:

1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש לייצור מספרים אקראיים וערבוב רשימות.

2.  **פונקציה `create_bingo_card()`**:
    -   `def create_bingo_card():`: מגדיר פונקציה שיוצרת ומחזירה כרטיס בינגו.
    -   `card = []`: מאתחל רשימה ריקה בשם `card`, שתייצג את מטריצת ה-5x5 (כרטיס הבינגו).
    -   `numbers = [i for i in range(1, 76) if i % 10 != 0]`: יוצר רשימה של מספרים מ-1 עד 75, למעט מספרים המתחלקים ב-10.
    -   `random.shuffle(numbers)`: מערבב את רשימת המספרים באופן אקראי.
    -   **מילוי הכרטיס**:
        -   לולאות מקוננות `for i in range(5)` ו-`for j in range(5)`: עוברות על כל התאים במטריצת ה-5x5.
        -   `row.append(numbers.pop())`: שולף את המספר האחרון מהרשימה `numbers` ומוסיף אותו לשורה הנוכחית של הכרטיס.
        -   `card.append(row)`: מוסיף את השורה שנוצרה לכרטיס.
    -   `return card`: מחזיר את כרטיס הבינגו המוכן.

3.  **פונקציה `print_bingo_card(card)`**:
    -   `def print_bingo_card(card):`: מגדיר פונקציה שמציגה את כרטיס הבינגו על המסך.
    -   לולאה `for row in card`: עוברת על כל שורות הכרטיס.
    -   `print(" ".join(str(x).rjust(2) for x in row))`: מציגה את השורה הנוכחית. `str(x).rjust(2)` ממיר כל מספר למחרוזת, מיישר אותו לימין לרוחב של 2 תווים, ו-`" ".join()` מוסיף רווחים בין המספרים.
    -   `print()`: מוסיף שורה ריקה לאחר הצגת הכרטיס לעיצוב טוב יותר.

4.  **פונקציה `mark_number(card, number)`**:
    -   `def mark_number(card, number):`: מגדיר פונקציה שמסמנת מספר על כרטיס הבינגו.
    -   **חיפוש והחלפת מספר**:
        -   לולאות מקוננות `for i in range(len(card))` ו-`for j in range(len(card[i]))`: עוברות על כל תאי הכרטיס.
        -   `if card[i][j] == number:`: בודק האם המספר הנוכחי שווה למספר המבוקש.
        -   `card[i][j] = 0`: אם המספר נמצא, הוא מוחלף ב-0.
        -   `return`: מסיים את הפונקציה לאחר ההחלפה הראשונה.

5.  **פונקציה `is_bingo(card)`**:
    -   `def is_bingo(card):`: מגדיר פונקציה שבודקת האם כל המספרים על הכרטיס סומנו.
    -   **בדיקת כל המספרים**:
        -   לולאה `for row in card`: עוברת על כל שורות הכרטיס.
        -   לולאה `for num in row`: עוברת על כל המספרים בשורה הנוכחית.
        -   `if num != 0:`: אם נמצא מספר שאינו מסומן (שאינו שווה ל-0), הפונקציה מחזירה `False`.
    -   `return True`: אם כל המספרים סומנו, הפונקציה מחזירה `True`.

6.  **פונקציה `play_bingo()`**:
    -   `def play_bingo():`: מגדיר פונקציה שמריצה את המשחק "בינגו".
    -   `bingo_card = create_bingo_card()`: יוצר כרטיס בינגו.
    -   `print("Your BINGO card:")`: מציג הודעה על תחילת המשחק. (השארתי את הטקסט הזה באנגלית כפי שהיה בקוד הרוסי המקורי בהקשר זה)
    -   `print_bingo_card(bingo_card)`: מציג את הכרטיס על המסך.
    -   `called_numbers = set()`: יוצר סט (קבוצה) לאחסון מספרים שכבר הוכרזו, כדי למנוע חזרות.
    -   **לולאת המשחק**:
        -   `while not is_bingo(bingo_card)`: מתבצעת כל עוד ישנם מספרים שלא סומנו על הכרטיס.
        -   `number = random.randint(1, 75)`: מייצר מספר אקראי.
        -   `while number in called_numbers`: ממשיך לייצר מספר חדש כל עוד המספר הנוכחי כבר הוכרז בעבר.
        -   `called_numbers.add(number)`: מוסיף את המספר לסט המספרים שהוכרזו.
        -   `print(f"Called number: {number}")`: מציג את המספר שהוגרל. (השארתי את הטקסט הזה באנגלית כפי שהיה בקוד הרוסי המקורי בהקשר זה)
        -   `mark_number(bingo_card, number)`: מסמן את המספר על הכרטיס.
        -   `print_bingo_card(bingo_card)`: מציג את הכרטיס המעודכן על המסך.
    -   `print("BINGO!")`: מציג הודעת ניצחון, כאשר כל המספרים סומנו.

7.  **הרצת המשחק מותנית**:
    -   `if __name__ == "__main__":`: בודק שהקובץ מורץ כתוכנית ראשית, ולא מיובא כמודול.
    -   `play_bingo()`: קורא לפונקציה `play_bingo()` כדי להריץ את המשחק.