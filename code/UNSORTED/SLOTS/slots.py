SLOTS:
=================
דרגת קושי: 5
-----------------
המשחק "סלוטים" הוא משחק מזל פשוט המדמה מכונת מזל עם שלושה סלילים. בכל סליל נופל באופן אקראי אחד מכמה ערכים (דובדבן, שזיף, פעמון או כוכב). אם בשלושת הסלילים נופלים אותם ערכים, השחקן זוכה, אחרת הוא מפסיד.

כללי המשחק:
1.  השחקן מפעיל את "מכונת המזל".
2.  בשלושת הסלילים נופלים באופן אקראי סמלים: דובדבן (C), שזיף (P), פעמון (B) או כוכב (*).
3.  אם כל שלושת הסמלים זהים, השחקן זוכה.
4.  אם הסמלים אינם זהים, השחקן מפסיד.
-----------------
אלגוריתם:
1.  ליצור שלושה מספרים אקראיים, כל אחד בין 1 ל-4.
2.  להמיר כל מספר לסמל המתאים:
    -   1 -> "C" (דובדבן)
    -   2 -> "P" (שזיף)
    -   3 -> "B" (פעמון)
    -   4 -> "*" (כוכב)
3.  להציג על המסך את שילוב הסמלים שהתקבל על הסלילים.
4.  לבדוק אם כל שלושת הסמלים זהים:
    -   אם הם זהים, להציג הודעה "YOU WIN".
    -   אם הם אינם זהים, להציג הודעה "YOU LOSE".
5.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateReels["<p align='left'>יצירת מספרים אקראיים לסלילים:
    <code><b>
    reel1 = random(1, 4)
    reel2 = random(1, 4)
    reel3 = random(1, 4)
    </b></code></p>"]
    GenerateReels --> ConvertToSymbols["<p align='left'>המרת מספרים לסמלים:
    <code><b>
    symbol1 = getSymbol(reel1)
    symbol2 = getSymbol(reel2)
    symbol3 = getSymbol(reel3)
    </b></code></p>"]
    ConvertToSymbols --> DisplaySymbols["הצגת סמלים: <code><b>symbol1, symbol2, symbol3</b></code>"]
    DisplaySymbols --> CheckWin{"בדיקה: <code><b>symbol1 == symbol2 and symbol2 == symbol3?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU WIN</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> OutputLose["הצגת הודעה: <b>YOU LOSE</b>"]
    OutputLose --> End
```
מקרא:
    Start - התחלת התוכנית.
    GenerateReels - יצירת שלושה מספרים אקראיים בין 1 ל-4 עבור סלילי מכונת המזל.
    ConvertToSymbols - המרת כל מספר לסמל המתאים: 1 -> "C", 2 -> "P", 3 -> "B", 4 -> "*".
    DisplaySymbols - הצגת הסמלים שנוצרו על המסך.
    CheckWin - בדיקה האם כל שלושת הסמלים זהים.
    OutputWin - הצגת הודעת זכייה אם הסמלים זהים.
    OutputLose - הצגת הודעת הפסד אם הסמלים אינם זהים.
    End - סוף התוכנית.
```
import random

# פונקציה להמרת מספר לסמל
def get_symbol(number):
    """
    ממירה מספר לסמל המתאים עבור מכונת המזל.
    
    Args:
        number (int): מספר בין 1 ל-4, המייצג סליל.
    
    Returns:
        str: הסמל המתאים למספר ("C", "P", "B", "*").
    """
    if number == 1:
        return "C"  # דובדבן
    elif number == 2:
        return "P"  # שזיף
    elif number == 3:
        return "B"  # פעמון
    elif number == 4:
        return "*"  # כוכב
    else:
        return "?" # לא ידוע

# פונקציה ראשית למשחק סלוטים
def play_slots():
    """
    מדמה מכונת מזל.
    יוצרת סמלים אקראיים על שלושה סלילים וקובעת אם השחקן זכה.
    """
    # יוצרים מספרים אקראיים עבור כל אחד משלושת הסלילים
    reel1 = random.randint(1, 4)
    reel2 = random.randint(1, 4)
    reel3 = random.randint(1, 4)

    # ממירים את המספרים לסמלים המתאימים
    symbol1 = get_symbol(reel1)
    symbol2 = get_symbol(reel2)
    symbol3 = get_symbol(reel3)

    # מציגים את התוצאה על המסך
    print(f"סלוטים: {symbol1} {symbol2} {symbol3}")

    # בודקים אם השחקן זכה
    if symbol1 == symbol2 and symbol2 == symbol3:
        print("YOU WIN")  # הדפסת הודעת זכייה
    else:
        print("YOU LOSE") # הדפסת הודעת הפסד


# מריצים את המשחק
if __name__ == "__main__":
    play_slots()

```
הסבר קוד:

1.  **ייבוא מודול `random`:**
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים.

2.  **פונקציה `get_symbol(number)`:**
    -   `def get_symbol(number):`: מגדירה פונקציה שמקבלת מספר בין 1 ל-4 ומחזירה את הסמל המתאים לסלוטים.
    -   `if number == 1: return "C"`: אם המספר שווה ל-1, מוחזר "C" (דובדבן).
    -   `elif number == 2: return "P"`: אם המספר שווה ל-2, מוחזר "P" (שזיף).
    -   `elif number == 3: return "B"`: אם המספר שווה ל-3, מוחזר "B" (פעמון).
    -   `elif number == 4: return "*"`: אם המספר שווה ל-4, מוחזר "*" (כוכב).
    -   `else: return "?"`: במקרה של מספר לא תקין מוחזר "?" (לא ידוע).

3.  **פונקציה `play_slots()`:**
    -   `def play_slots():`: מגדירה את הפונקציה הראשית של משחק "סלוטים".
    -   `reel1 = random.randint(1, 4)`: יוצרת מספר שלם אקראי בין 1 ל-4 עבור הסליל הראשון.
    -   `reel2 = random.randint(1, 4)`: יוצרת מספר שלם אקראי בין 1 ל-4 עבור הסליל השני.
    -   `reel3 = random.randint(1, 4)`: יוצרת מספר שלם אקראי בין 1 ל-4 עבור הסליל השלישי.
    -   `symbol1 = get_symbol(reel1)`: ממירה את מספר הסליל הראשון לסמל, באמצעות הפונקציה `get_symbol`.
    -   `symbol2 = get_symbol(reel2)`: ממירה את מספר הסליל השני לסמל, באמצעות הפונקציה `get_symbol`.
    -   `symbol3 = get_symbol(reel3)`: ממירה את מספר הסליל השלישי לסמל, באמצעות הפונקציה `get_symbol`.
    -   `print(f"סלוטים: {symbol1} {symbol2} {symbol3}")`: מציגה את שילוב הסמלים על המסך.
    -   `if symbol1 == symbol2 and symbol2 == symbol3:`: בודקת אם כל שלושת הסמלים זהים.
        -   `print("YOU WIN")`: אם כל הסמלים זהים, מציגה הודעה "YOU WIN".
    -   `else:`: אם הסמלים אינם זהים, מבוצע בלוק ה-`else`.
        -   `print("YOU LOSE")`: מציגה הודעה "YOU LOSE".

4.  **הפעלת המשחק:**
    -   `if __name__ == "__main__":`: בודקת אם הסקריפט הוא הראשי.
    -   `play_slots()`: קוראת לפונקציה `play_slots()` כדי להתחיל את המשחק, אם הסקריפט הוא הראשי.