### question_763.md
```

**שאלה 763.** נתון מערך של מספרים שלמים `nums`, כאשר כל איבר `nums[i]` מייצג את אורך הקפיצה המקסימלי מהעמדה `i`. אתם מתחילים מהעמדה הראשונה (אינדקס 0) של המערך. פתח אלגוריתם בפייתון אשר קובע האם ניתן להגיע לאינדקס האחרון של המערך, באמצעות ביצוע קפיצות התואמות לערכים במערך.

**דוגמאות:**
```
קלט: nums = [1, 3, 1, 1, 4]
פלט: True
הסבר: ניתן להגיע לאינדקס האחרון על ידי ביצוע קפיצה באורך 1 מאינדקס 0 לאינדקס 1, ולאחר מכן קפיצה באורך 3 מאינדקס 1 לאחרון.

קלט: nums = [3, 2, 1, 0, 4]
פלט: False
הסבר: לא קיימת דרך להגיע מהאינדקס ההתחלתי עד הסוף.
```

- א. לפתרון הבעיה יש להשתמש באלגוריתם סריקה ממצה של כל הנתיבים האפשריים.
- ב. לפתרון הבעיה יש להשתמש באלגוריתם של מיון ובדיקת איברים.
- ג. לפתרון הבעיה יש להשתמש באלגוריתם חיפוש לרוחב (BFS).
- ד. לפתרון הבעיה ניתן להשתמש באלגוריתם חמדן (greedy algorithm), אשר מחשב בכל צעד מהו הערך המקסימלי שניתן להגיע אליו מהעמדה הנוכחית.

**תשובה נכונה: ד**

**הסבר:**

לפתרון בעיה זו, הגישה האופטימלית היא שימוש באלגוריתם חמדן (Greedy Algorithm). שיטה זו בוחרת בכל איטרציה את הפתרון האופטימלי מקומית (הקפיצה המקסימלית), מה שמאפשר להגיע ליעד הסופי, או להראות שהוא אינו בר השגה.

*   **האלגוריתם (גישה חמדנית):**
    1.  **אתחול:** מאתחלים את `max_reach` בערך `0` (כיוון שמתחילים מהעמדה ההתחלתית), המהווה את המרחק המקסימלי שניתן להגיע אליו.
     2. **איטרציה:** עוברים על המערך, כל עוד האינדקס הנוכחי `i` נמצא בטווח המרחק הניתן להשגה `max_reach` (כלומר, כל עוד `i <= max_reach` ):
          *  בכל צעד, אנו מעדכנים את `max_reach` באמצעות הערך המקסימלי בין `max_reach` הנוכחי לבין המיקום הנוכחי `i` + ערך הקפיצה ב-`nums[i]`.
         *  אם `max_reach` הגיע או עבר את גבולות סוף המערך, אזי נחזיר `True` (הגעה לאיבר האחרון).
    3.  **תוצאה:** אם לאחר מעבר על כל האיברים הלולאה מסתיימת, אך `max_reach` לא הגיע לסוף המערך, אזי מחזירים `False`, כיוון שלא ניתן להגיע לעמדה האחרונה.

*   **יתרונות האלגוריתם:**
    *  **סיבוכיות לינארית:** לאלגוריתם סיבוכיות זמן של `O(n)`.
   *  **פשטות:** הקוד קריא וקל ליישום.
     *    **יעילות:** האלגוריתם מאפשר למצוא פתרון מבלי לעבור על כל הנתיבים האפשריים, מה שהופך אותו לשיטה יעילה עבור בעיה זו.

**דוגמאות (פסאודו-קוד):**

```
function can_reach_end(nums):
    max_reach = 0
    for i from 0 to length(nums)-1:
        if i > max_reach:
            return False # it is impossible to reach current pos
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= length(nums) - 1:
          return True # found correct path.
    return False # not able to finish with success
```
**דוגמאות מימוש בפייתון:**
```python
def can_reach_end(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False # it is impossible to reach current pos
        max_reach = max(max_reach, i + jump)
        if max_reach >= len(nums) - 1:
             return True # found path to end

    return False

nums1 = [1,3,1,1,4]
print(f"קלט: nums = {nums1}")
print(f"פלט: {can_reach_end(nums1)}") # יציג: פלט: True

nums2 = [3,2,1,0,4]
print(f"קלט: nums = {nums2}")
print(f"פלט: {can_reach_end(nums2)}")  # יציג:  פלט: False
```

**ניתוח האפשרויות:**
* **א. לפתרון הבעיה יש להשתמש באלגוריתם סריקה ממצה של כל הנתיבים האפשריים.:** לא נכון. סריקה ממצה תהיה לא יעילה.
*  **ב. לפתרון הבעיה יש להשתמש באלגוריתם של מיון ובדיקת איברים.:** לא נכון.
*   **ג. לפתרון הבעיה יש להשתמש באלגוריתם חיפוש לרוחב (BFS).:** לא נכון. BFS אינו פתרון אופטימלי במקרה זה.
*  **ד. לפתרון הבעיה ניתן להשתמש באלגוריתם חמדן, אשר מחשב בכל צעד מהו הערך המקסימלי שניתן להגיע אליו מהעמדה הנוכחית.:** נכון.

**לסיכום:**
*  אלגוריתם חמדן מאפשר לפתור את הבעיה בזמן לינארי.
*  האלגוריתם עוקב אחר המרחק המקסימלי שניתן להגיע אליו, ומחזיר האם האיבר האחרון במערך בר השגה או לא.
*  בכל צעד נבדק האם האינדקס הנוכחי בר השגה, מה שמבטל בדיקות מיותרות.

לפיכך, התשובה הנכונה היא **ד. לפתרון הבעיה ניתן להשתמש באלגוריתם חמדן, אשר מחשב בכל צעד מהו הערך המקסימלי שניתן להגיע אליו מהעמדה הנוכחית.**.