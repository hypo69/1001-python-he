SLOTS:
=================
דרגת קושי: 5
-----------------
המשחק "סלוֹטְס" (Slots) הוא משחק מזל פשוט המדמה מכונת הימורים עם שלושה גלילים. בכל גליל נוחת באופן אקראי אחד מכמה ערכים (דובדבן, שזיף, פעמון או כוכבית). אם בכל שלושת הגלילים נוחתים ערכים זהים, השחקן זוכה; אחרת, הוא מפסיד.

כללי המשחק:
1.  השחקן מפעיל את "מכונת ההימורים".
2.  על שלושת הגלילים נוחתים סמלים באופן אקראי: דובדבן (C), שזיף (P), פעמון (B) או כוכבית (*).
3.  אם כל שלושת הסמלים זהים, השחקן זוכה.
4.  אם הסמלים אינם זהים, השחקן מפסיד.
-----------------
אלגוריתם:
1.  הפק שלושה מספרים אקראיים, כל אחד בין 1 ל-4.
2.  המר כל מספר לסמל המתאים:
    -   1 -> "C" (דובדבן)
    -   2 -> "P" (שזיף)
    -   3 -> "B" (פעמון)
    -   4 -> "*" (כוכבית)
3.  הצג על המסך את שילוב הסמלים שהתקבלו על הגלילים.
4.  בדוק אם כל שלושת הסמלים זהים:
    -   אם הם זהים, הצג את ההודעה "YOU WIN".
    -   אם הם אינם זהים, הצג את ההודעה "YOU LOSE".
5.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> GenerateReels["<p align='left'>Генерация случайных чисел для барабанов:
    <code><b>
    reel1 = random(1, 4)
    reel2 = random(1, 4)
    reel3 = random(1, 4)
    </b></code></p>"]
    GenerateReels --> ConvertToSymbols["<p align='left'>Преобразование чисел в символы:
    <code><b>
    symbol1 = getSymbol(reel1)
    symbol2 = getSymbol(reel2)
    symbol3 = getSymbol(reel3)
    </b></code></p>"]
    ConvertToSymbols --> DisplaySymbols["Вывод символов: <code><b>symbol1, symbol2, symbol3</b></code>"]
    DisplaySymbols --> CheckWin{"Проверка: <code><b>symbol1 == symbol2 and symbol2 == symbol3?</b></code>"}
    CheckWin -- Да --> OutputWin["Вывод сообщения: <b>YOU WIN</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> OutputLose["Вывод сообщения: <b>YOU LOSE</b>"]
    OutputLose --> End
```
מקרא:
    Start - התחלת התוכנית.
    GenerateReels - הפקת שלושה מספרים אקראיים בין 1 ל-4 עבור גלילי מכונת ההימורים.
    ConvertToSymbols - המרת כל מספר לסמל המתאים: 1 -> "C", 2 -> "P", 3 -> "B", 4 -> "*".
    DisplaySymbols - הצגת הסמלים שהופקו על המסך.
    CheckWin - בדיקה האם כל שלושת הסמלים זהים.
    OutputWin - הצגת הודעת זכייה אם הסמלים זהים.
    OutputLose - הצגת הודעת הפסד אם הסמלים אינם זהים.
    End - סיום התוכנית.
"""
import random

# פונקציה להמרת מספר לסמל
def get_symbol(number):
    """
    ממירה מספר לסמל המתאים עבור מכונת ההימורים.
    
    Args:
        number (int): מספר בין 1 ל-4, המייצג גליל.
    
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
        return "*"  # כוכבית
    else:
        return "?" # לא ידוע

# פונקציה ראשית למשחק הסלוטים
def play_slots():
    """
    מדמה מכונת הימורים.
    מפיק סמלים אקראיים על שלושה גלילים וקובע אם השחקן זכה.
    """
    # מפיקים מספרים אקראיים עבור כל אחד משלושת הגלילים
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
        print("YOU WIN")  # הצגת הודעת זכייה
    else:
        print("YOU LOSE") # הצגת הודעת הפסד


# מריצים את המשחק
if __name__ == "__main__":
    play_slots()

"""
הסבר קוד:

1.  **ייבוא מודול `random`:**
    -   `import random`: מייבאת את מודול `random`, המשמש להפקת מספרים אקראיים.

2.  **פונקציה `get_symbol(number)`:**
    -   `def get_symbol(number):`: מגדירה פונקציה שמקבלת מספר בין 1 ל-4 ומחזירה את הסמל המתאים לסלוטים.
    -   `if number == 1: return "C"`: אם המספר שווה ל-1, מוחזר "C" (דובדבן).
    -   `elif number == 2: return "P"`: אם המספר שווה ל-2, מוחזר "P" (שזיף).
    -   `elif number == 3: return "B"`: אם המספר שווה ל-3, מוחזר "B" (פעמון).
    -   `elif number == 4: return "*"`: אם המספר שווה ל-4, מוחזר "*" (כוכבית).
    -   `else: return "?"`: במקרה של מספר לא תקין, מוחזר "?" (לא ידוע).

3.  **פונקציה `play_slots()`:**
    -   `def play_slots():`: מגדירה את הפונקציה הראשית של המשחק "סלוטים".
    -   `reel1 = random.randint(1, 4)`: מפיק מספר שלם אקראי בין 1 ל-4 עבור הגליל הראשון.
    -   `reel2 = random.randint(1, 4)`: מפיק מספר שלם אקראי בין 1 ל-4 עבור הגליל השני.
    -   `reel3 = random.randint(1, 4)`: מפיק מספר שלם אקראי בין 1 ל-4 עבור הגליל השלישי.
    -   `symbol1 = get_symbol(reel1)`: ממיר את מספר הגליל הראשון לסמל, באמצעות הפונקציה `get_symbol`.
    -   `symbol2 = get_symbol(reel2)`: ממיר את מספר הגליל השני לסמל, באמצעות הפונקציה `get_symbol`.
    -   `symbol3 = get_symbol(reel3)`: ממיר את מספר הגליל השלישי לסמל, באמצעות הפונקציה `get_symbol`.
    -   `print(f"סלוטים: {symbol1} {symbol2} {symbol3}")`: מציג את שילוב הסמלים על המסך.
    -   `if symbol1 == symbol2 and symbol2 == symbol3:`: בודק אם כל שלושת הסמלים זהים.
        -   `print("YOU WIN")`: אם כל הסמלים זהים, מציג את ההודעה "YOU WIN".
    -   `else:`: אם הסמלים אינם זהים, מבוצע בלוק ה-`else`.
        -   `print("YOU LOSE")`: מציג את ההודעה "YOU LOSE".

4.  **הפעלת המשחק:**
    -   `if __name__ == "__main__":`: בודק אם הסקריפט מורץ ישירות (ולא מיובא כמודול).
    -   `play_slots()`: קורא לפונקציה `play_slots()` כדי להתחיל את המשחק, אם הסקריפט הוא הראשי.
"""