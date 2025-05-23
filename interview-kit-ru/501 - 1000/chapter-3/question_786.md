### `question_786.md`

**שאלה 786.** נתון מערך של מספרים שלמים `nums` בגודל `n`. פתח אלגוריתם בפייתון למציאה והחזרה של האיבר הרובני (majority element) במערך.

*   **איבר רובני** — זהו איבר המופיע במערך יותר מ-`n / 2` פעמים, והוא תמיד קיים.

**דוגמאות:**
```
קלט: nums = [4, 2, 4]
פלט: 4

קלט: nums = [8, 8, 6, 6, 6, 8, 8]
פלט: 8
```
- א. כדי לפתור את הבעיה, יש להשתמש במיון ובחיפוש אחר האיבר המרכזי, אשר יהיה האיבר הרובני.
- ב. כדי לפתור את הבעיה, יש לעבור על כל איברי המערך, ולבדוק כל אחד מהם לגבי התאמה לתנאי, כלומר, לגבי מספר מופעים הגדול מ- n/2.
- ג. כדי לפתור את הבעיה, יש להשתמש באלגוריתם חיפוש לרוחב (BFS).
- ד. כדי לפתור את הבעיה ניתן להשתמש באלגוריתם ההצבעה של בויר-מור (Boyer-Moore Majority Vote Algorithm), המאפשר למצוא את האיבר הרובני במעבר יחיד עם סיבוכיות זמן לינארית.

**תשובה נכונה: ד**

**הסבר:**

לפתרון בעיית מציאת האיבר הרובני (האיבר המופיע יותר מ-`n / 2` פעמים) במערך, הגישה האופטימלית היא שימוש באלגוריתם ההצבעה של בויר-מור. אלגוריתם זה מאפשר למצוא את האיבר הרובני במעבר יחיד על המערך (זמן לינארי), ללא צורך במיון או אחסון מידע נוסף על כל איבר.

*   **אלגוריתם ההצבעה של בויר-מור:**
    1.  **אתחול:** מגדירים מועמד `candidate` כ-`None`, ומונה `count` כ-`0`.
    2.  **איטרציה על המערך:** עוברים על המערך `nums`:
        *   אם המונה שווה ל-0, מגדירים את האיבר הנוכחי במערך כמועמד `candidate`.
        *   אם האיבר הנוכחי שווה למועמד, מגדילים את המונה `count`.
        *   אם לא שווה, מקטינים את המונה `count`.
    3. **בדיקה:** עוברים על המערך וסופרים את מספר המופעים של `candidate`.
        *   אם הערך גדול מ-`n/2` מחזירים את המועמד `candidate`, אחרת, אם מועמד כזה אינו קיים, מחזירים `None`.

*   **יתרונות האלגוריתם:**
    *   **סיבוכיות לינארית:** מבטיח סיבוכיות זמן של O(n), כלומר תלוי באופן לינארי במספר איברי המערך.
    *   **זיכרון קבוע:** דורש רק כמות זיכרון קבועה.
    *   **יעילות:** מאפשר למצוא את האיבר הרובני במעבר יחיד.

*   **מדוע גישות אחרות אינן מתאימות:**
    *   **מיון וחיפוש איבר מרכזי:** מיון וחיפוש האיבר המרכזי אינו מבטיח מציאת האיבר הרובני ובעל סיבוכיות O(n log n).
    *   **מעבר מלא (Full traversal):** בדיקת כל מועמד להתאמה לתנאי תיקח זמן ריבועי `O(n^2)` ואינה יעילה.
    *   **BFS:** BFS אינו ישים בבעיה זו.

**דוגמאות (פסאודו-קוד):**

```
function majority_element(nums):
    candidate = null
    count = 0
    for element in nums:
        if count == 0:
             candidate = element;
        if element == candidate:
             count = count +1;
        else:
           count  = count -1
     count2 = 0
    for element in nums:
       if element = candidate:
         count2 +=1
    if count2 > length(nums)/2:
      return candidate
    return null
```
**דוגמאות מימוש בפייתון:**

```python
def find_majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
           count += 1
        else:
          count -= 1

    count2 = 0
    for num in nums:
      if num == candidate:
           count2+=1
    if count2 > len(nums) / 2:
      return candidate
    return None


nums1 = [4, 2, 4]
print(f"קלט: nums = {nums1}")
print(f"פלט: {find_majority_element(nums1)}") # יוצג: פלט: 4

nums2 = [8, 8, 6, 6, 6, 8, 8]
print(f"קלט: nums = {nums2}")
print(f"פלט: {find_majority_element(nums2)}") # יוצג: פלט: 8

nums3 = [1,2,3,4,5,6,7]
print(f"קלט: nums = {nums3}")
print(f"פלט: {find_majority_element(nums3)}") # יוצג None
```

**ניתוח אפשרויות:**
*   **א. כדי לפתור את הבעיה, יש להשתמש במיון ובחיפוש אחר האיבר המרכזי, אשר יהיה האיבר הרובני.:** שגוי. מיון אינו יעיל ואינו ישים לבעיה זו.
*   **ב. כדי לפתור את הבעיה, יש לעבור על כל איברי המערך, ולבדוק כל אחד מהם לגבי התאמה לתנאי, כלומר, לגבי מספר מופעים הגדול מ- n/2.:** שגוי. לפתרון זה יש סיבוכיות `O(n^2)`.
*   **ג. כדי לפתור את הבעיה, יש להשתמש באלגוריתם חיפוש לרוחב (BFS).:** שגוי.
*   **ד. כדי לפתור את הבעיה ניתן להשתמש באלגוריתם ההצבעה של בויר-מור (Boyer-Moore Majority Vote Algorithm), המאפשר למצוא את האיבר הרובני במעבר יחיד עם סיבוכיות זמן לינארית.:** נכון.

**לסיכום:**
*   אלגוריתם בויר-מור פותר ביעילות את בעיית מציאת האיבר הרובני.
*   האלגוריתם עובר על המערך פעם אחת בלבד, ומחזיר את התוצאה באמצעות בדיקות וספירות יעילות.
*   בעל סיבוכיות לינארית O(n), המהווה פתרון אופטימלי לבעיה.

לפיכך, התשובה הנכונה היא **ד. כדי לפתור את הבעיה ניתן להשתמש באלגוריתם ההצבעה של בויר-מור (Boyer-Moore Majority Vote Algorithm), המאפשר למצוא את האיבר הרובני במעבר יחיד עם סיבוכיות זמן לינארית.**