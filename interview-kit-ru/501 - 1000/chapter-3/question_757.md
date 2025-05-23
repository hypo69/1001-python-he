### `question_757.md`

**שאלה 757.** נתונה מחרוזת `s` בפורמט `k[encoded_string]`, כאשר `k` הוא מספר החזרות של המחרוזת המקודדת. פתח אלגוריתם להמרת מחרוזת זו לצורתה המפוענחת, תוך התחשבות בכך שהמחרוזת עשויה להכיל תת-מחרוזות מקודדות מקוננות.

**דוגמאות:**

```
קלט: s = "3[a]2[bc]"
פלט: "aaabcbc"

קלט: s = "3[a2[c]]"
פלט: "accaccacc"
```

- א. לפתרון הבעיה יש להשתמש בביטויים רגולריים בלבד, ובכל איטרציה לחלץ את תת-המחרוזת ומספר החזרות, ולאחר מכן לחבר אותן.
- ב. לפתרון הבעיה יש להשתמש במחסנית לאחסון תוצאות ביניים, ובעזרת לולאות לעבור על המחרוזת, תוך עיבוד ספרות, אותיות וסוגריים.
- ג. לפתרון הבעיה יש להשתמש באלגוריתם רקורסיבי בלבד, ולקרוא לפונקציה ברציפות עבור כל רמת קינון.
- ד. לפתרון הבעיה מתאים רק אלגוריתם חמדן, שיוסיף סימנים חדשים לסוף המחרוזת.

**תשובה נכונה: ב**

**הסבר:**

לפתרון בעיית פענוח מחרוזת עם חזרות, האופטימלי הוא שימוש במחסנית, מכיוון שהיא מאפשרת לעבד נכונה סוגריים מקוננים ולעקוב נכונה אחר סדר האלמנטים, וזאת תוך שימוש במעבר בודד בלבד על המחרוזת המקורית.

*   **אלגוריתם (איטרטיבי עם מחסנית):**
    1.  **אתחול:**
        *   נוצרת מחסנית לאחסון תוצאות ביניים.
        *   נוצר משתנה `curr_num` לאחסון זמני של מספר החזרות.
        *   נוצר משתנה `curr_str` לאחסון זמני של המחרוזת התוצאתית.
    2.  **איטרציה על המחרוזת:** עוברים תו-אחר-תו על המחרוזת `s`:
        *   **ספרה:** אם התו הנוכחי הוא ספרה, מוסיפים אותה ל- `curr_num`.
        *   **סוגר פותח `[`:** שומרים את הערכים הנוכחיים של `curr_str` ו- `curr_num` במחסנית ומאפסים אותם.
        *   **סוגר סוגר `]`:** שולפים מהמחסנית את הערכים השמורים `prev_str`, ו- `prev_num`, וחוזרים על ה- `curr_str` הנוכחי `prev_num` פעמים ומוסיפים את התוצאה ל- `prev_str`, את התוצאה מקצים ל- `curr_str`.
        *   **תו:** אם התו הנוכחי הוא אות, מוסיפים אותה ל- `curr_str`.
    3.  **תוצאה:** לאחר מעבר על כל התווים מחזירים את המחרוזת התוצאתית `curr_str`.

*   **יתרונות האלגוריתם:**
    *   **מחסנית:** המחסנית מאפשרת לעקוב אחר רמת קינון הסוגריים ולשמור מצבי ביניים בפענוח.
    *   **סיבוכיות לינארית:** האלגוריתם בעל סיבוכיות O(n), כאשר n היא אורך המחרוזת, מכיוון שהוא עובר על המחרוזת פעם אחת בלבד.
    *   **יעילות:** האלגוריתם מעבד ביעילות מחרוזות מקוננות.

**דוגמאות (פסאודו-קוד):**
```
function decodeString(s):
  stack = Stack()
    curr_num = 0
    curr_str = ""

    for char in s:
        if char is digit:
           curr_num = curr_num *10 + to_int(char)
        elif char is '[':
            stack.push((curr_str, curr_num))
            curr_str = ""
             curr_num = 0
        elif char is ']':
           prev_str, prev_num = stack.pop()
           curr_str =  prev_str  +  curr_str * prev_num
        else:
            curr_str = curr_str + char
        return curr_str
```
**דוגמאות מימוש ב-Python:**
```python
def decodeString(s):
    stack = []
    curr_num = 0
    curr_str = ""

    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif char == ']':
            prev_str, prev_num = stack.pop()
            curr_str = prev_str + curr_str * prev_num
        else:
            curr_str += char
    return curr_str

s1 = "3[a]2[bc]"
print(f"קלט: s = '{s1}'")
print(f"פלט: {decodeString(s1)}") # פלט: aaabcbc

s2 = "3[a2[c]]"
print(f"קלט: s = '{s2}'")
print(f"פלט: {decodeString(s2)}")  # פלט: accaccacc
```

**ניתוח האפשרויות:**
*   א. לפתרון הבעיה יש להשתמש בביטויים רגולריים בלבד, ובכל איטרציה לחלץ את תת-המחרוזת ומספר החזרות, ולאחר מכן לחבר אותן.: שגוי.
*   ב. לפתרון הבעיה יש להשתמש במחסנית לאחסון תוצאות ביניים, ובעזרת לולאות לעבור על המחרוזת, תוך עיבוד ספרות, אותיות וסוגריים.: נכון.
*   ג. לפתרון הבעיה יש להשתמש באלגוריתם רקורסיבי בלבד, ולקרוא לפונקציה ברציפות עבור כל רמת קינון.: שגוי. רקורסיה אינה הפתרון האופטימלי.
*   ד. לפתרון הבעיה מתאים רק אלגוריתם חמדן, שיוסיף סימנים חדשים לסוף המחרוזת.: שגוי. אלגוריתם חמדן לא יתאים.

**לסיכום:**
*   המחסנית מאפשרת לעבד ביעילות סוגריים מקוננים.
*   האלגוריתם מאפשר לעבד את המחרוזת ברציפות מההתחלה ועד הסוף.
*   היציאה מרקורסיה (stack unwinding) בסדר הנכון, מאפשרת לקבל את המחרוזת התוצאתית.

לפיכך, התשובה הנכונה היא **ב. לפתרון הבעיה יש להשתמש במחסנית לאחסון תוצאות ביניים, ובעזרת לולאות לעבור על המחרוזת, תוך עיבוד ספרות, אותיות וסוגריים.**