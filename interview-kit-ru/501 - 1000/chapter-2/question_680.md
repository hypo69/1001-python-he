### `question_680.md`

**שאלה 680.** פתח/י אלגוריתם למיון מערך של מספרים שלמים `nums` בסדר עולה עם מורכבות זמן O(n log n) ועם מורכבות המקום הנמוכה ביותר האפשרית, מבלי להשתמש בפונקציות מובנות למיון.

**דוגמאות:**
```
קלט: nums = [5,2,3,1]
פלט: [1,2,3,5]

קלט: nums = [5,1,1,2,0,0]
פלט: [0,0,1,1,2,5]
```

- A. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון בועות (Bubble Sort).
- B. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון הכנסה (Insertion Sort).
- C. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון בחירה (Selection Sort).
- D. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון מיזוג (Merge Sort), שלו מורכבות זמן O(n log n) ואינו משתמש בזיכרון עזר רב.

**תשובה נכונה: D**

**הסבר:**

כדי לפתור את בעיית מיון מערך של מספרים שלמים בסדר עולה עם מורכבות זמן O(n log n) ללא שימוש בפונקציות מיון מובנות, האלגוריתם המתאים הוא מיון מיזוג (Merge Sort).

*   **מיון מיזוג (Merge Sort):**
    *   **עקרון 'הפרד ומשול':** מחלק את הרשימה לשני חצאים עד שנותרות רשימות בנות איבר אחד, ואז ממזג באופן רקורסיבי את הרשימות הממוינות.
    *   **מורכבות זמן:** בעל מורכבות זמן O(n log n) במקרים הגרוע, הממוצע והטוב ביותר.
    *   **יציבות:** שומר על סדר של איברים זהים.
    *   **רק ורסיה:** מבוסס על קריאה רקורסיבית של עצמו.

*   **מדוע אפשרויות אחרות אינן מתאימות:**
    *   **מיון בועות (Bubble Sort), מיון הכנסה (Insertion Sort), ומיון בחירה (Selection Sort):** בעלי מורכבות זמן O(n^2) במקרים הגרוע והממוצע, מה שהופך אותם ללא יעילים עבור קבוצות נתונים גדולות.

**דוגמאות (פסאודו-קוד):**

```
function merge_sort(arr):
    if length(arr) <= 1:
        return arr
    mid = length(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
function merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < length(left) and j < length(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
```

**דוגמאות ליישום ב-Python:**
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

print(merge_sort([5,2,3,1])) # פלט: [1, 2, 3, 5]
print(merge_sort([5,1,1,2,0,0])) # פלט: [0, 0, 1, 1, 2, 5]
```

**ניתוח אפשרויות:**
*   **A. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון בועות.:** לא נכון.
*   **B. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון הכנסה.:** לא נכון.
*   **C. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון בחירה.:** לא נכון.
*   **D. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון מיזוג (Merge Sort), שלו מורכבות זמן O(n log n) ואינו משתמש בזיכרון עזר רב.:** נכון.

**לסיכום:**
*   אלגוריתם מיון מיזוג (Merge Sort) יעיל למיון מערך עם מורכבות זמן O(n log n).
*   האלגוריתם ממומש באופן רקורסיבי ומשתמש בעקרון 'הפרד ומשול'.

לפיכך, התשובה הנכונה היא **D. כדי לפתור בעיה זו ניתן להשתמש באלגוריתם מיון מיזוג (Merge Sort), שלו מורכבות זמן O(n log n) ואינו משתמש בזיכרון עזר רב.**