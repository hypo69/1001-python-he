### `question_281_interview.md`

**שאלה 281.** מה עושה הפונקציה `itertools.filterfalse` בפייתון, וכיצד היא שונה מהפונקציה המובנית `filter`?

A.  `itertools.filterfalse` מסננת אלמנטים מתוך אובייקט בר-מעבר (iterable), ומחזירה רק את אלה שעבורם פונקציית הפרדיקט מחזירה `True`, ואילו `filter` מחזירה את אלה שעבורם פונקציית הפרדיקט מחזירה `False`.
B.  `itertools.filterfalse` מסננת אלמנטים מתוך אובייקט בר-מעבר, ומחזירה רק את אלה שעבורם פונקציית הפרדיקט מחזירה `False`, ואילו `filter` מחזירה את אלה שעבורם פונקציית הפרדיקט מחזירה `True`.
C.  `itertools.filterfalse` מיישמת פונקציה על כל אלמנט באובייקט בר-מעבר, ואילו `filter` מסננת אלמנטים על בסיס פרדיקט.
D.  `itertools.filterfalse` ו-`filter` מבצעות את אותה פעולה, ההבדל הוא רק בתחביר.

**תשובה נכונה: B**

**הסבר:**

הפונקציות `itertools.filterfalse` ו-`filter` מיועדות לסינון אלמנטים של אובייקטים ברי-מעבר, אך הן פועלות באופן שונה ביחס לאילו אלמנטים הן מחזירות.

*   **`filter(function, iterable)`**:
    *   מקבלת פונקציה `function` (פרדיקט) ואובייקט בר-מעבר `iterable`.
    *   מחזירה *איטרטור* המכיל *רק את האלמנטים* מתוך `iterable` שעבורם `function` מחזירה `True`.
    *   משמשת ל*סינון* אלמנטים המקיימים תנאי (פרדיקט).

*   **`itertools.filterfalse(function, iterable)`**:
    *   מקבלת גם כן פונקציה `function` (פרדיקט) ואובייקט בר-מעבר `iterable`.
    *   מחזירה *איטרטור* המכיל *רק את האלמנטים* מתוך `iterable` שעבורם `function` מחזירה `False`.
    *   משמשת ל*סינון* אלמנטים ש*אינם* מקיימים תנאי (פרדיקט).

לפיכך, `itertools.filterfalse` היא גרסה "הפוכה" של הפונקציה המובנית `filter`.

*   **אפשרות A אינה נכונה:** `itertools.filterfalse` מחזירה אלמנטים שעבורם פונקציית הפרדיקט מחזירה `False`.
*   **אפשרות B נכונה:** זהו התיאור המדויק של ההבדל בין `itertools.filterfalse` לבין `filter`.
*   **אפשרות C אינה נכונה:** `itertools.filterfalse` ו-`filter` מבצעות סינון, לא טרנספורמציה.
*   **אפשרות D אינה נכונה:** הפונקציות מבצעות סינונים *הפוכים*.

**דוגמאות:**

```python
import itertools

numbers = [1, 2, 3, 4, 5, 6]

# Using filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even Numbers (filter): {even_numbers}") # Output: [2, 4, 6]

# Using itertools.filterfalse to get odd numbers
odd_numbers = list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))
print(f"Odd Numbers (filterfalse): {odd_numbers}") # Output: [1, 3, 5]
```

**הבדלים מרכזיים:**

*   **`filter`**: מחזירה אלמנטים שעבורם פונקציית הפרדיקט מחזירה `True`.
*   **`itertools.filterfalse`**: מחזירה אלמנטים שעבורם פונקציית הפרדיקט מחזירה `False`.

**לסיכום:**

הפונקציה `itertools.filterfalse` מחזירה אלמנטים מאובייקט בר-מעבר שעבורם פונקציית הפרדיקט מחזירה `False`, בעוד ש-`filter` מחזירה אלמנטים שעבורם פונקציית הפרדיקט מחזירה `True`.

לפיכך, אפשרות B היא הנכונה.