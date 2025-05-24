### `question_773.md`

**שאלה 773.** נתונים שני עצים בינאריים, המיוצגים על ידי שורשיהם `root1` ו-`root2`. פתח/י אלגוריתם בפייתון למיזוג עצים אלה, כאשר ערכי הצמתים המקבילים מסוכמים, ומוחזר שורש העץ התוצאתי. במקרה שלעץ אחד אין צומת צאצא, אזי בעץ התוצאתי, יתווספו צמתים צאצאים מהעץ השני.

**עץ 1:**
```
    1
   / \
  3   2
 /
5
```

**עץ 2:**

```
    2
   / \
  1  3
   \ /
    4  7

```
**עץ תוצאתי:**
```
    4
   /  \
  4   5
 /  \  \
5  4  7
```

**דוגמאות:**

```
Ввод: root1 = [1, 3, 2, 5], root2 = [2, 1, 3, null, 4, null, 7]
Вывод: [3, 4, 5, 5, 4, null, 7]

Ввод: root1 = [1], root2 = [1, 2]
Вывод: [2, 2]
```
- א. כדי לפתור את הבעיה, יש לבחור את הצמתים המתאימים באמצעות חיפוש בינארי, ולאחר מכן לסכם אותם.
- ב. כדי לפתור את הבעיה, יש להשתמש רק ברקורסיה, ולעבור רק על ערכי העלים.
- ג. כדי לפתור את הבעיה, יש להשתמש באלגוריתם רקורסיבי, כאשר במקרה ששני הצמתים אינם `None`, מסכמים את ערכיהם ובונים עץ חדש, ואם יש רק אחד שאינו `None`, מחזירים אותו.
- ד. כדי לפתור את הבעיה, יש למיין תחילה את שני העצים, ולאחר מכן לבצע סכימה.

**תשובה נכונה: ג**

**הסבר:**

לפתרון בעיית מיזוג עצים בינאריים וסכימת הצמתים המקבילים שלהם, האופטימלי הוא שימוש באלגוריתם רקורסיבי, מכיוון שמבנה העץ הבינארי עצמו הוא רקורסיבי.

*   **אלגוריתם (רקורסיבי):**
    1. **פונקציה רקורסיבית:**
         *   נוצרת פונקציה רקורסיבית שמקבלת שני צמתים `root1` ו-`root2`.
         *   **מקרה בסיס:**
              *  אם גם `root1` וגם `root2` הם `None` אזי מחזירים `None`.
              *   אם רק `root1` הוא `None`, אזי מחזירים את `root2` (את תת-העץ `root2`).
             *   אם רק `root2` הוא `None`, אזי מחזירים את `root1` (את תת-העץ `root1`).
        *   **סכימה:** יוצרים צומת חדש `head`, שערכו שווה לסכום הערכים של `root1.val` + `root2.val`.
        *  **קריאה רקורסיבית:** קוראים רקורסיבית לפונקציה עבור תת-העצים השמאלי והימני: `head.left = constructTree(root1.left, root2.left)` ו-`head.right = constructTree(root1.right, root2.right)`.
       *  **החזרת צומת:** הפונקציה מחזירה את הצומת שנוצר `head` (תת-העץ הנוכחי).
     2.  **קריאה התחלתית:**  קוראים רקורסיבית עבור שני השורשים `root1` ו-`root2`.
     3.  **תוצאה:** מוחזר שורש העץ התוצאתי.

*   **יתרונות האלגוריתם:**
    *   **מעבר רקורסיבי:** רקורסיה מאפשרת לעבור בקלות על עץ בינארי.
    *  **שומר על מבנה העץ:** יוצר מבנה עץ חדש, בהתחשב במבנים של העצים המקוריים.
     *  **סוכם ערכים:** מבטיח סכימה נכונה של ערכים במיקומים המתאימים.
    *  **יעילות:** לאלגוריתם סיבוכיות זמן O(n), כאשר n הוא מספר הצמתים בעץ.

**דוגמאות (פסאודו קוד):**
```
function constructTree(root1, root2):
    if root1 is null and root2 is null:
        return null
    if root2 is null:
       return root1
     if root1 is null:
          return root2
    root =  new Node with value as sum of current roots
    root.left = constructTree(root1.left, root2.left)
    root.right = constructTree(root1.right, root2.right)
   return root
```
**דוגמאות מימוש בפייתון:**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees(root1, root2):
        def constructTree(root1, root2):
            if not root1 and not root2:
                return None
            if not root2:
                return root1
            if not root1:
                return root2
            head = TreeNode(root1.val + root2.val)
            head.left = constructTree(root1.left, root2.left)
            head.right = constructTree(root1.right, root2.right)
            return head

        return constructTree(root1, root2)

# helper function for printing results.
def print_tree(root):
    if not root:
      return [None]
    else:
      return [root.val] + print_tree(root.left) + print_tree(root.right)

root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
print(f"Ввод: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]")
print(f"Вывод: {print_tree(merge_trees(root1, root2))}")
# Выведет: Вывод: [3, 4, 5, None, None, 5, 4, None, None, None, 7, None, None]

root3 = TreeNode(1)
root4 = TreeNode(1, None, TreeNode(2))
print(f"Ввод: root1 = [1], root2 = [1,2]")
print(f"Вывод: {print_tree(merge_trees(root3, root4))}") # Выведет: [2, None, 2, None, None]
```

**ניתוח אפשרויות:**
*  **א. כדי לפתור את הבעיה, יש להשתמש בשיטת הוספת אלמנטים לעץ על בסיס ערכם, כאשר ילד שמאל קטן מהשורש, וימין גדול:** לא נכון. שיטה זו אינה מתאימה.
*   **ב. כדי לפתור את הבעיה, יש להשתמש רק באלגוריתם רקורסיבי, ולעבור רק על ערכי העלים.:** לא נכון. יש לסכם את העלים, אך יש לעבד את כל הרמות.
*  **ג. כדי לפתור את הבעיה, יש להשתמש באלגוריתם רקורסיבי, שיסכם את ערכי הצמתים המקבילים בשני העצים.:** נכון.
*  **ד. לפתרון הבעיה יתאים רק אלגוריתם איטרטיבי עם מחסנית לשמירת צמתים.:** לא נכון.

**לסיכום:**
* אלגוריתם רקורסיבי מאפשר מעבר יעיל על שני העצים.
*  הפונקציה עובדת נכון עם כל המבנים האפשריים.
*   נעשה שימוש ברקורסיה לקוד פשוט ותמציתי.

לפיכך, התשובה הנכונה היא **ג. כדי לפתור את הבעיה, יש להשתמש באלגוריתם רקורסיבי, שיסכם את ערכי הצמתים המקבילים בשני העצים.**