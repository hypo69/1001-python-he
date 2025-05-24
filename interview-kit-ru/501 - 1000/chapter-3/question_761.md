### `question_761.md`

**שאלה 761.** נתון מצביע לראש רשימה מקושרת חד-כיוונית `head`. פתחו אלגוריתם ב-Python למיון צומתי הרשימה לפי ערך בסדר עולה, בסיבוכיות זמן `O(n log n)` ובסיבוכיות מקום `O(1)`.

**דוגמאות:**

```
קלט: head = [4,2,1,3]
פלט: [1,2,3,4]

קלט: head = [-1,5,3,4,0]
פלט: [-1,0,3,4,5]
```

- א. כדי לפתור את הבעיה יש להשתמש באלגוריתם מיון בועות (bubble sort) מכיוון שהוא פשוט ליישום.
- ב. כדי לפתור את הבעיה יש להשתמש במיון מהיר (quick sort).
- ג. כדי לפתור את הבעיה יש להשתמש במיון מיזוג (merge sort), תוך שימוש בגישה רקורסיבית ופיצול הרשימה לחלקים.
- ד. כדי לפתור את הבעיה מתאים רק אלגוריתם מיון בחירה (selection sort).

**תשובה נכונה: ג**

**הסבר:**

כדי לפתור את בעיית מיון רשימה מקושרת חד-כיוונית עם מגבלת סיבוכיות זמן `O(n log n)` וסיבוכיות מקום `O(1)`, השימוש באלגוריתם מיון מיזוג (Merge Sort) הוא המתאים ביותר. מיון מיזוג מתאים היטב לרשימות מקושרות, מכיוון שהוא אינו דורש גישה קבועה לאלמנטים, וניתן ליישם אותו באמצעות רקורסיה ב-`O(log n)`, שבמקרה זה לא ייצור זיכרון נוסף על המחסנית בשל מאפייני האלגוריתם (באמצעות פיצול לחלקים, להבדיל ממעבר ליניארי).

*   **האלגוריתם (מיון מיזוג):**
    1.  **חלוקה רקורסיבית:**
        *   מוצאים את אמצע הרשימה, ומפצלים את הרשימה לשני חלקים (לשם כך משתמשים בשני מצביעים: slow, fast).
        *   קוראים רקורסיבית לפונקציה למיון החלק השמאלי והימני של הרשימה.
        *   **מקרה בסיס:** אם הרשימה מורכבת מאפס או אלמנט אחד, מחזירים אותה ללא שינוי.
    2.  **מיזוג:** משתמשים בפונקציית עזר `merge` למיזוג שתי רשימות ממוינות:
        *   יוצרים רשימה חדשה `merged_list` ומשווים אלמנטים מתתי-הרשימה השמאלית והימנית ומוסיפים אותם בסדר עולה ל-`merged_list`.
        *   מוסיפים את האלמנטים שנותרו ברציפות, אם נותרו כאלה לאחר סיום הלולאה.
        *   מחזירים את התוצאה מ-`merged_list`.

*   **יתרונות האלגוריתם:**
    *   **סיבוכיות O(n log n):** בעל סיבוכיות זמן `O(n log n)`.
    *   **שימוש ברקורסיה:** פיצול לתת-בעיות באמצעות רקורסיה מאפשר ליישם את המיזוג בקלות.
    *   **יעילות:** מיון הרשימה מתבצע ללא שימוש בזיכרון נוסף (מלבד מצביעים).
*   **מדוע אפשרויות אחרות אינן מתאימות:**
    *   **Bubble sort, Insertion Sort, Selection Sort:** בעלות סיבוכיות ריבועית `O(n^2)`, ואינן מתאימות למשימה זו.
    *   **Quick sort:** Quick sort ברשימה מקושרת אינו תמיד יעיל, וכן היישום שלו אינו משימה פשוטה.

**דוגמאות (פסאודו קוד):**
```
function sort_linked_list(head):
   if head is null or head.next is null
     return head
     middle = find middle of list with pointers
    left = head;
   right  =  middle.next
   middle.next = null # split
   left =  sort_linked_list(left);
  right = sort_linked_list(right);
    return merge (left, right)

function merge(left, right):
   new_head = create empty list
  while left and right are not null:
      if left.val <= right.val
           append left to  new_head
           left=left.next
      else:
         append right to new_head
           right=right.next
    append to new_head all elements of  left or right if still not done.
  return new_head
```
**דוגמאות ליישום ב-Python:**
```python
class ListNode:
   def __init__(self, val=0, next=None):
     self.val = val
     self.next = next


def sort_linked_list(head):
    if not head or not head.next:
        return head

    # find middle node
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow
    right_part = mid.next
    mid.next = None # מפצלים לשתי רשימות


    left_part = sort_linked_list(head)
    right_part = sort_linked_list(right_part)
    return merge(left_part, right_part)

def merge(left, right):
   dummy = ListNode(0) # צומת דמה.
   curr = dummy
   while left and right:
        if left.val <= right.val:
           curr.next=left
           left = left.next
        else:
           curr.next=right
           right = right.next
        curr = curr.next

   if left:
       curr.next = left
   elif right:
        curr.next = right

   return dummy.next

# helper function to print list
def print_linked_list(head):
    res = []
    while head:
      res.append(head.val)
      head = head.next
    print(res)


head1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print(f"קלט: head = [4,2,1,3]")
head1_sorted = sort_linked_list(head1)
print("פלט: ", end = "")
print_linked_list(head1_sorted) # יוצג: [1, 2, 3, 4]

head2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
print(f"קלט: head = [-1,5,3,4,0]")
head2_sorted = sort_linked_list(head2)
print("פלט: ", end = "")
print_linked_list(head2_sorted) # יוצג: [-1, 0, 3, 4, 5]

```
**ניתוח האפשרויות:**

*   **א. כדי לפתור את הבעיה יש להשתמש באלגוריתם מיון בועות (bubble sort) מכיוון שהוא פשוט ליישום.:** לא נכון. מיון בועות בעל סיבוכיות `O(n^2)`.
*   **ב. כדי לפתור את הבעיה יש להשתמש במיון מהיר (quick sort).:** לא נכון. מיון מהיר ברשימות מקושרות אינו יעיל באותה מידה.
*   **ג. כדי לפתור את הבעיה יש להשתמש במיון מיזוג (merge sort), תוך שימוש בגישה רקורסיבית ופיצול הרשימה לחלקים.:** נכון.
*   **ד. כדי לפתור את הבעיה מתאים רק אלגוריתם מיון בחירה (selection sort).:** לא נכון. מיון בחירה בעל סיבוכיות `O(n^2)`.

**לסיכום:**
*   אלגוריתם מיון מיזוג מאפשר למיין רשימה מקושרת בסיבוכיות זמן `O(n log n)`.
*   רקורסיה משמשת לפיצול הרשימה לתת-רשימות, והפונקציה `merge()` - למיזוגן.
*   האלגוריתם אינו משתמש בזיכרון נוסף.

לפיכך, התשובה הנכונה היא **ג. כדי לפתור את הבעיה יש להשתמש במיון מיזוג (merge sort), תוך שימוש בגישה רקורסיבית ופיצול הרשימה לחלקים.**