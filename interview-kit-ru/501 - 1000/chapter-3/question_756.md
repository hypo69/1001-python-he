### `question_756.md`

**שאלה 756.** פתח/י מחלקה בשם `MyStack` ב-Python, אשר מיישמת את מבנה הנתונים "מחסנית" תוך שימוש בשני תורים (queues) בלבד. המחלקה `MyStack` צריכה לתמוך בשיטות הבאות:

*   `__init__()`: מאתחל מחסנית ריקה.
*   `push(x)`: מוסיף את האלמנט `x` לראש המחסנית.
*   `pop()`: מסיר את האלמנט מראש המחסנית ומחזיר אותו.
*   `top()`: מחזיר את האלמנט בראש המחסנית, מבלי להסיר אותו.
*   `empty()`: מחזיר `True` אם המחסנית ריקה, ו-`False` אחרת.

**דוגמאות:**

```
Ввод:
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Вывод: [null, null, null, 2, 2, False]
Объяснение:
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

-   A. ליישום מחסנית ניתן להשתמש במערך אחד בלבד, והוספת אלמנט מתבצעת בסוף המערך, והסרה מההתחלה.
-   B. ליישום מחסנית ניתן להשתמש בשתי רשימות, כאשר כל הפעולות מתבצעות רק על הרשימה השנייה.
-   C. ליישום מחסנית ניתן להשתמש בשני תורים, כאשר אלמנטים חדשים מוספים לאחד מהתורים, והסרה, הצגה ובדיקה לריקות מתבצעות דרך התור השני (כשהוא אינו ריק).
-   D. ליישום מחסנית יש להשתמש רק באלגוריתם רקורסיבי.

**תשובה נכונה: C**

**הסבר:**

לצורך יישום מחסנית תוך שימוש בשני תורים, יש לפזר את האלמנטים בין התורים באופן כזה שבעת ביצוע פעולות `pop`, `top` ו-`empty`, ישמש התור בו נמצא ראש המחסנית.

*   **אלגוריתם (עם שני תורים):**
    1.  **אתחול:**
        *   יוצרים שני תורים ריקים `q1` ו-`q2`.
        *   `top` - לשמירת הערך האחרון שנוסף (הנמצא בראש המחסנית).
    2.  **שיטה `push(x)`:**
        *   רושמים את הערך בתור `q1`.
        *   מעדכנים את המשתנה `top`.
    3.  **שיטה `pop()`:**
        *   משתמשים בתור `q1`, אם הוא אינו ריק:
            *   מעבירים את כל האלמנטים מ-`q1`, למעט האחרון, לתור `q2`, ואת האלמנט האחרון שומרים כ-`last` ומחזירים אותו.
            *   מחליפים את `q1` ו-`q2`, כך ש-`q1` תמיד תכיל את כל הערכים ותהיה התור הפעיל.
        *   אם `q1` ריק, מחזירים None.
    4.  **שיטה `top()`:** מחזירה את הערך השמור במשתנה `top`.
    5.  **שיטה `empty()`:** בודקים האם התור `q1` ריק (ומחזירים `True` או `False`).

*   **יתרונות האלגוריתם:**
    *   **יישום מחסנית:** מאפשר ליישם מחסנית תוך שימוש בתורים בלבד.
    *   **פשטות:** קל ליישום ולהבנה.
    *   **ניהול תורים:** כל פעולה דורשת בחירה של התור הפעיל.
    *   **החזרת ערך:** עבור pop מוחזר הערך מהתור, עבור top מוחזר המשתנה השמור.
    *   **אורך זוגי ואי-זוגי:** השיטה פועלת גם עבור אורך רשימה אי-זוגי.

**דוגמאות (פסאודו-קוד):**
```
class MyStack:
    function __init__():
       q1 = empty queue # תור ריק
       q2 = empty queue # תור ריק
        top = None # ראש המחסנית
     function push(val):
      add val to q1 # הוספת ערך ל-q1
       top = val # עדכון ראש המחסנית

    function pop():
       if queue q1 is empty: # אם תור q1 ריק
         return None # החזרת None
       while queue q1 size more than 1 # כל עוד גודל תור q1 גדול מ-1
          move head from q1 to q2 # העברת ראש מ-q1 ל-q2
       last = head from queue q1 # האלמנט האחרון הוא ראש q1
        swap q1 and q2 # החלפת q1 ו-q2
        return last # החזרת האלמנט האחרון
    function top()
        return top

    function empty()
        return q1 is empty;
```

**דוגמאות ליישום ב-Python:**
```python
from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.top = None
    def push(self, x: int) -> None:
        self.q1.append(x)
        self.top = x

    def pop(self) -> int | None:
        if not self.q1:
            return None
        while len(self.q1) > 1:
          self.q2.append(self.q1.popleft())
        last = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return last

    def top(self) -> int | None:
        return self.top

    def empty() -> bool: # Changed from empty(self) -> bool
        return not self.q1

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(f"top: {myStack.top()}") # Выведет: top: 2 # ידפיס: top: 2
print(f"pop: {myStack.pop()}") # Выведет: pop: 2 # ידפיס: pop: 2
print(f"empty: {myStack.empty()}") # Выведет: empty: False # ידפיס: empty: False
print(f"pop: {myStack.pop()}")
print(f"empty: {myStack.empty()}")
```
*Self-correction during translation*: The Python code had a small error in the `empty()` definition (`empty()` instead of `empty(self)`). I will keep the original user code exactly as provided, including the error, as per instruction 2. I will only translate the comments. However, the Python code block itself has no comments. The comments are in the example usage and were originally in Russian, indicating what the output should be. I will translate these Russian comments to Hebrew.

**ניתוח האפשרויות:**
*   **A. ליישום מחסנית ניתן להשתמש במערך אחד בלבד, והוספת אלמנט מתבצעת בסוף המערך, והסרה מההתחלה.:** לא נכון. זהו יישום של תור, לא של מחסנית.
*   **B. ליישום מחסנית ניתן להשתמש בשתי רשימות, כאשר כל הפעולות מתבצעות רק על הרשימה השנייה.:** לא נכון, זה לא יענה על הדרישה לשימוש בתורים.
*   **C. ליישום מחסנית ניתן להשתמש בשני תורים, כאשר אלמנטים חדשים מוספים לאחד מהתורים, והסרה, הצגה ובדיקה לריקות מתבצעות דרך התור השני (כשהוא אינו ריק).:** נכון.
*   **D. ליישום מחסנית יש להשתמש רק באלגוריתם רקורסיבי.:** לא נכון.

**כתוצאה מכך:**
*   שימוש בשני תורים מאפשר ליישם את הלוגיקה של מחסנית.
*   יישום נכון של push/pop ו-top מאפשר ליצור מבנה LIFO (Last-In, First-Out) פועל.

לפיכך, התשובה הנכונה היא **C. ליישום מחסנית ניתן להשתמש בשני תורים, כאשר אלמנטים חדשים מוספים לאחד מהתורים, והסרה, הצגה ובדיקה לריקות מתבצעות דרך התור השני (כשהוא אינו ריק).**