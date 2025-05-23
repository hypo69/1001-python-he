BOUNCE:
=================
רמת קושי: 5
-----------------
המשחק "כדור קופץ" הוא אנימציה פשוטה המדמה תנועה של כדור המקפץ מהגבול העליון והתחתון של המסך. המשתמש יכול ללחוץ על כל מקש כדי לעצור את האנימציה. גובה הכדור משתנה על פי פונקציית הסינוס.

כללי המשחק:
1.  הכדור מתחיל תנועה ממיקום אנכי התחלתי מוגדר.
2.  הכדור נע מעלה ומטה, מדמה קפיצה מהגבול העליון והתחתון של המסך.
3.  גובה הכדור משתנה על פי פונקציית הסינוס.
4.  האנימציה נמשכת עד שהמשתמש לוחץ על מקש.
-----------------
אלגוריתם:
1.  אתחול משתנים:
    - `Y` - המיקום האנכי ההתחלתי של הכדור (אמצע המסך).
    - `T` - ערך התחלתי עבור פונקציית הסינוס (0).
    - `D` - מדרגת השינוי של פונקציית הסינוס (0.2).
2.  התחלת לולאה אינסופית:
    2.1. חישוב המיקום האנכי החדש `Y` באמצעות הנוסחה: `20 + 19 * SIN(T)`.
    2.2. הדפסת `Y` למסך, תוך שימוש בערך שלם.
    2.3. הגדלת `T` ב-`D`.
    2.4. בדיקה האם נלחץ מקש כלשהו.
    2.5. אם נלחץ מקש, יציאה מהלולאה.
3. סוף המשחק.
-----------------
בлок-схема:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    Y = 20
    T = 0
    D = 0.2
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה אינסופית"}
    LoopStart --> CalculateY["<code><b>Y = 20 + 19 * SIN(T)</b></code>"]
    CalculateY --> OutputY["הדפסת <code><b>INT(Y)</b></code> למסך"]
    OutputY --> IncreaseT["<code><b>T = T + D</b></code>"]
    IncreaseT --> CheckKeyPress{"בדיקה: האם נלחץ מקש?"}
    CheckKeyPress -- Нет --> LoopStart
    CheckKeyPress -- Да --> End["סוף"]

```
מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: Y (המיקום האנכי ההתחלתי), T (הערך ההתחלתי עבור פונקציית הסינוס), D (מדרגת השינוי של פונקציית הסינוס).
    LoopStart - התחלת לולאה אינסופית.
    CalculateY - חישוב המיקום האנכי החדש Y באמצעות הנוסחה 20 + 19 * SIN(T).
    OutputY - הדפסת הערך השלם של Y למסך.
    IncreaseT - הגדלת הערך של T בגודל D.
    CheckKeyPress - בדיקה האם נלחץ מקש כלשהו.
    End - סוף התוכנית.
"""
import math
import time
import os
import sys

def clear_screen():
    """מנקה את מסך הטרמינל."""
    if os.name == 'nt':  # עבור Windows
        os.system('cls')
    else:  # עבור Linux ו-macOS
        os.system('clear')

def get_keypress():
    """בודק לחיצת מקש, מבלי לחסום את ההרצה."""
    if os.name == 'nt':
        import msvcrt
        if msvcrt.kbhit():
            msvcrt.getch()
            return True
    else:
        import select
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            sys.stdin.read(1)
            return True
    return False

# אתחול משתנים
Y = 20  # המיקום האנכי ההתחלתי של הכדור
T = 0   # ערך התחלתי עבור פונקציית הסינוס
D = 0.2 # מדרגת השינוי של פונקציית הסינוס

# לולאה אינסופית של אנימציה
while True:
    # מחשבים את המיקום האנכי החדש של הכדור
    Y = 20 + 19 * math.sin(T)
    # מנקים את המסך לפני הדפסת המיקום החדש
    clear_screen()
    # מדפיסים את הכדור למסך
    print(" " * int(Y) + "O")
    # מגדילים את הערך של T עבור הפריימ (frame) הבא
    T += D
    # השהיה ליצירת אפקט אנימציה
    time.sleep(0.1)
    # בודקים לחיצת מקש
    if get_keypress():
        break  # מסיימים את הלולאה אם המקש נלחץ
"""
הסבר על הקוד:
1. **ייבוא מודולים:**
   - `import math`: מייבא את המודול `math` לצורך שימוש בפונקציה המתמטית `sin`.
   - `import time`: מייבא את המודול `time` לצורך שליטה על ההשהיה באנימציה.
   - `import os`: מייבא את המודול `os` לצורך עבודה עם מערכת ההפעלה.
   - `import sys`: מייבא את המודול `sys` לצורך עבודה עם פרמטרים מערכתיים.
2. **הפונקציה `clear_screen()`:**
   - הפונקציה `clear_screen()` משמשת לניקוי מסך הטרמינל.
   - בהתאם למערכת ההפעלה (Windows או דמויות יוניקס), נקראת פקודת ניקוי המסך המתאימה.
3. **הפונקציה `get_keypress()`:**
    - הפונקציה `get_keypress()` בודקת האם נלחץ מקש כלשהו.
    - עבור Windows משתמשים במודול `msvcrt`, הפונקציה `kbhit()` בודקת לחיצה, ו-`getch()` קוראת תו.
    - עבור מערכות דמויות יוניקס משתמשים ב-`select.select` לקריאה לא חוסמת של תו מ-`stdin`.
    - מחזירה `True` אם נלחץ מקש, ו-`False` אחרת.
4. **אתחול משתנים:**
   - `Y = 20`: המיקום האנכי ההתחלתי של הכדור.
   - `T = 0`: הערך ההתחלתי עבור פונקציית הסינוס.
   - `D = 0.2`: מדרגת השינוי של פונקציית הסינוס.
5. **הלולאה האינסופית `while True:`:**
   - הלולאה נמשכת עד שלחיצת מקש תתרחש.
   - `Y = 20 + 19 * math.sin(T)`: מחשבת את המיקום האנכי החדש של הכדור, תוך שימוש בפונקציית הסינוס.
   - `clear_screen()`: מנקה את המסך לפני ציור המיקום החדש.
   - `print(" " * int(Y) + "O")`: מדפיסה את הכדור (`O`) למסך.
   - `T += D`: מגדילה את הערך של `T` עבור שלב האנימציה הבא.
   - `time.sleep(0.1)`: יוצרת השהיה של 0.1 שניות כדי להאט את האנימציה.
   - `if get_keypress():`: בודקת האם נלחץ מקש.
      - `break`: מסיימת את הלולאה אם המקש נלחץ.
"""