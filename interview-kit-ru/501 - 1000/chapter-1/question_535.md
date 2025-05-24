### `question_535.md`

**שאלה 535.** מה תהיה התוצאה שתתקבל בהרצת קוד ה-Python הבא, המיישם את אלגוריתם מיון המיזוג?

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# דוגמת שימוש
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
```

-   A. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [90, 64, 34, 25, 22, 12, 11]`
-   B. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [11, 12, 22, 25, 34, 64, 90]`
-   C. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [11, 90, 12, 64, 22, 34, 25]`
-   D. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [64, 34, 25, 22, 12, 11, 90]`

**תשובה נכונה: B**

**הסבר:**

הקוד המסופק מיישם את אלגוריתם מיון המיזוג (merge sort), אשר מבוסס על עיקרון "הפרד ומשול".

*   **אלגוריתם מיון המיזוג:**
    *   מפצל באופן רקורסיבי את המערך לשני חצאים.
    *   ממיין באופן רקורסיבי כל חצי.
    *   מבצע מיזוג של החצאים הממוינים למערך ממוין אחד.
*   **תיאור הקוד:**
    *   `merge_sort(arr)`: הפונקציה מפצלת באופן רקורסיבי את המערך `arr` לחצי, עד שנותרים איברים בודדים, ולאחר מכן קוראת לפונקציה `merge`.
        *   `if len(arr) <= 1`: מקרה הבסיס של הרקורסיה: אם אורך המערך קטן או שווה ל-1, הוא מוחזר כפי שהוא.
        *   `mid = len(arr) // 2`: מוצאת נקודת האמצע של המערך.
        *   `left = arr[:mid]`: החצי השמאלי של המערך.
        *   `right = arr[mid:]`: החצי הימני של המערך.
        *   `left = merge_sort(left)`: קריאה רקורסיבית עבור החצי השמאלי.
        *   `right = merge_sort(right)`: קריאה רקורסיבית עבור החצי הימני.
        *   `return merge(left, right)`: קורא לפונקציה `merge` לשילוב החצאים הממוינים.
    *   `merge(left, right)`: הפונקציה משלבת שני מערכים ממוינים `left` ו-`right` למערך ממוין אחד.
        *   `merged = []`: מאותחל רשימה חדשה לאלמנטים המאוחדים.
        *   `i = j = 0`: מאותחלים אינדקסים עבור המערכים השמאלי והימני.
        *   `while i < len(left) and j < len(right)`: לולאה המשווה אלמנטים מהמערך השמאלי והימני, ומוסיפה את הקטן יותר לרשימה `merged`.
        *   `merged.extend(left[i:])`: מוסיפה את האלמנטים הנותרים מהמערך השמאלי (אם קיימים).
        *   `merged.extend(right[j:])`: מוסיפה את האלמנטים הנותרים מהמערך הימני (אם קיימים).
        *   `return merged`: מחזירה את המערך המאוחד והממוין.

**ניתוח האפשרויות:**
*   **A. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [90, 64, 34, 25, 22, 12, 11]`:** שגוי, זהו סדר מיון יורד.
*   **B. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [11, 12, 22, 25, 34, 64, 90]`:** נכון. התוצאה היא מיון בסדר עולה.
*   **C. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [11, 90, 12, 64, 22, 34, 25]`:** שגוי.
*   **D. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [64, 34, 25, 22, 12, 11, 90]`:** שגוי.

**לסיכום:**
*   הקוד מיישם נכונה את אלגוריתם מיון המיזוג למיון מערך בסדר עולה.
*   מיון המיזוג הוא אלגוריתם מיון יעיל בעל סיבוכיות זמן מובטחת של O(n log n).

לפיכך, התשובה הנכונה היא **B. `Original array: [64, 34, 25, 12, 22, 11, 90] Sorted array: [11, 12, 22, 25, 34, 64, 90]`**.