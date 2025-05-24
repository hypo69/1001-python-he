### `question_727.md`

**שאלה 727.** נתונות שתי רשימות: `preorder` (מעבר קדם-סדר) ו-`inorder` (מעבר תוך-סדר), המייצגות מעברים של אותו עץ בינארי. פתח אלגוריתם הבונה עץ בינארי מרשימות אלו, והצג את התוצאה בפורמט ASCII.

*   **מעבר קדם-סדר (preorder):** שורש -> תת-עץ שמאלי -> תת-עץ ימני.
*   **מעבר תוך-סדר (inorder):** תת-עץ שמאלי -> שורש -> תת-עץ ימני.

**ייצוג העץ ב-ASCII:**

```
    3
   / \
  9  20
    /  \
   15  7
```
**דוגמאות:**
```
קלט:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
פלט: [3,9,20,null,null,15,7]

קלט: preorder = [-1], inorder = [-1]
פלט: [-1]
```
-   א. כדי לפתור את הבעיה יש להשתמש בשיטת הכנסת איברים לעץ על בסיס ערכם, כאשר ילד שמאלי קטן מהשורש וילד ימני גדול ממנו.
-   ב. כדי לפתור את הבעיה נדרש להשתמש באלגוריתם רקורסיבי שיבנה את העץ על פי המעברים הנתונים.
-   ג. כדי לפתור את הבעיה נדרש להשתמש באלגוריתם שסורק את העץ לרוחב (BFS).
-   ד. לפתרון הבעיה מתאים רק אלגוריתם חיפוש ליניארי.

**תשובה נכונה: ב**

**הסבר:**

כדי לבנות עץ בינארי ממעברי קדם-סדר (preorder) ותוך-סדר (inorder) שלו, הגישה האופטימלית היא שימוש באלגוריתם רקורסיבי. רקורסיה מאפשרת לעבד תתי-עצים ולבנות את העץ צעד אחר צעד.

*   **האלגוריתם (רקורסיבי):**
    1.  **מקרי בסיס:**
        *   אם `preorder` או `inorder` ריקים, החזר `null`.
    2.  **שורש:** האיבר הראשון ברשימת `preorder` הוא השורש של העץ הנוכחי.
        *   צור צומת עם ערך זה: `root = TreeNode(preorder[0])`.
    3.  **מציאת השורש ב-inorder:** מצא את האינדקס של השורש ברשימת `inorder`. אינדקס זה מחלק את `inorder` לחלק שמאלי וחלק ימני.
        *   האינדקס `root_index` מציין את מיקום השורש ב-`inorder`.
    4.  **בניית תת-העץ השמאלי:**
        *   הפרד את חלקי `preorder` ו-`inorder` המתייחסים לתת-העץ השמאלי, וקרא רקורסיבית לפונקציה עבור תת-העץ השמאלי.
            *   `preorder_left = preorder[1 : root_index +1]`
            *   `inorder_left = inorder[ : root_index]`
            *   `root.left = build_tree(preorder_left, inorder_left)`
    5.  **בניית תת-העץ הימני:**
        *   הפרד את חלקי `preorder` ו-`inorder` המתייחסים לתת-העץ הימני, וקרא רקורסיבית לפונקציה עבור תת-העץ הימני.
        *   `preorder_right = preorder[root_index + 1:]`
        *   `inorder_right = inorder[root_index + 1 : ]`
        *   `root.right = build_tree(preorder_right, inorder_right)`

    6.  **החזרת השורש:** החזר את השורש, המייצג את העץ שנבנה.

*   **יתרונות האלגוריתם:**
    *   **סריקה רקורסיבית:** מאפשרת לסרוק את העץ ולבנות אותו בקלות בכל צעד.
    *   **מבנה ברור:** מפצל את הבעיה לתתי-בעיות, מה שמאפשר ליישם את האלגוריתם עם מינימום קוד.

**דוגמאות (קוד פסאודו):**
```
function build_tree(preorder, inorder):
    if preorder is empty:
        return null
    root_val = preorder[0]
    root = new TreeNode(root_val)
    root_index = find_index(root_val, inorder)
    preorder_left = preorder[1:root_index + 1]
    inorder_left = inorder[0:root_index]
    root.left = build_tree(preorder_left, inorder_left)
    preorder_right = preorder[root_index + 1:]
    inorder_right = inorder[root_index + 1: ]
    root.right = build_tree(preorder_right, inorder_right)
     return root
```
**דוגמאות ליישום בפייתון:**

```python
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def build_tree(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    root_index = inorder.index(root_val)
    preorder_left = preorder[1:root_index + 1]
    inorder_left = inorder[ : root_index]
    root.left = build_tree(preorder_left, inorder_left)
    preorder_right = preorder[root_index + 1:]
    inorder_right = inorder[root_index + 1: ]
    root.right = build_tree(preorder_right, inorder_right)
    return root

# פונקציה להדפסת העץ כרשימה

def print_tree(root):
    if not root:
      return [None]
    else:
       return [root.val] + print_tree(root.left) + print_tree(root.right)



preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]
root1 = build_tree(preorder1, inorder1)
print(f"קלט:  preorder = {preorder1}, inorder = {inorder1}")
print(f"פלט: {print_tree(root1)}") # פלט: [3, 9, None, None, 20, 15, None, None, 7, None, None]

preorder2 = [-1]
inorder2 = [-1]
root2 = build_tree(preorder2, inorder2)
print(f"קלט:  preorder = {preorder2}, inorder = {inorder2}")
print(f"פלט: {print_tree(root2)}") # פלט: [-1]
```

**ניתוח האפשרויות:**

*   **א. כדי לפתור את הבעיה יש להשתמש בשיטת הכנסת איברים לעץ על בסיס ערכם, כאשר ילד שמאלי קטן מהשורש וילד ימני גדול ממנו.:** שגוי. שיטה זו פועלת רק עבור עצי חיפוש בינאריים (BST), והקלט אינו מבטיח עץ כזה.
*   **ב. כדי לפתור את הבעיה נדרש להשתמש באלגוריתם רקורסיבי שיבנה את העץ על פי המעברים הנתונים.:** נכון.
*   **ג. כדי לפתור את הבעיה נדרש להשתמש באלגוריתם שסורק את העץ לרוחב (BFS).:** שגוי, סריקת רוחב (BFS) אינה מאפשרת לבנות עץ באמצעות מעברי preorder ו-inorder.
*   **ד. לפתרון הבעיה מתאים רק אלגוריתם חיפוש ליניארי.:** שגוי.

**לסיכום:**
*   אלגוריתם רקורסיבי בונה ביעילות עץ בינארי תוך שימוש במעברי preorder ו-inorder.
*   האלגוריתם מפצל את הרשימות בהתאם למיקום השורש, תוך ניצול מאפייני מעברי העץ.

לפיכך, התשובה הנכונה היא **ב. כדי לפתור את הבעיה נדרש להשתמש באלגוריתם רקורסיבי שיבנה את העץ על פי המעברים הנתונים.**