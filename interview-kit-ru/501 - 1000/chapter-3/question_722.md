### `question_722.md`

**שאלה 722.** ניתן מערך של מחרוזות `words`, שבו מובטח שקיימת לפחות מחרוזת אחת. פתחו אלגוריתם לחיפוש ולהחזרת התת-מחרוזת-תחילית המשותפת הארוכה ביותר (ההתחלה המשותפת) עבור כל המחרוזות במערך. אם לא קיימת תת-מחרוזת-תחילית משותפת, החזירו מחרוזת ריקה `""`.

**דוגמאות:**

```
קלט: words = ["дог", "домен", "домра", "доширак"]
פלט: "до"

קלט: words = ["документ", "кот", "кум", "ум"]
פלט: ""
```

- א. כדי לפתור את הבעיה, יש לעבור על כל התחיליות האפשריות של כל מחרוזת ולבדוק את התאמתן.
- ב. כדי לפתור את הבעיה, יש להשתמש רק בלולאות ובתנאים ולבדוק את התחיליות אחת-אחת.
- ג. כדי לפתור את הבעיה, יש להשתמש בשיטה המשווה תווים במחרוזות תו אחר תו עד אשר נמצא הבדל, או עד שהושג סופה של אחת המחרוזות.
- ד. כדי לפתור את הבעיה, יש למיין את כל המחרוזות לפי אורכן ולהשתמש במחרוזת הקצרה ביותר, מכיוון שהיא עשויה להכיל את התחילית המשותפת המקסימלית.

**תשובה נכונה: C**

**הסבר:**

כדי לפתור את בעיית מציאת התחילית המשותפת הארוכה ביותר במערך מחרוזות, יהיה אופטימלי להשתמש באלגוריתם המשווה תווים במחרוזות תו אחר תו. גישה זו מבטיחה בדיקה של כמות מינימלית של תווים, תוך הימנעות מהשוואות מיותרות, ומבטיחה את נכונות התוצאה.

*   **אלגוריתם (השוואת תווים תו אחר תו):**
    1.  **מחרוזת ריקה:** אם מערך `words` ריק, אז מחזירים מחרוזת ריקה.
    2.  **קביעת המילה הראשונה:** לוקחים את האיבר הראשון במערך בתור `first_word`.
        *   אם יש מחרוזת ריקה - מחזירים מחרוזת ריקה מיד.
    3.  **השוואת תווים תו אחר תו:** מבצעים איטרציה על התווים של `first_word`.
        *   בכל איטרציה מבצעים איטרציה על שאר המחרוזות במערך `words`:
            *   אם האינדקס חורג מגבולות האורך של מחרוזת אחרת, או שהתווים באינדקס זה אינם זהים, אז מחזירים את החלק מ-`first_word` עד האינדקס הנוכחי.
        *   אם כל הבדיקות עברו, אז נבדק התו הבא.
    4.  **תוצאה:** מחזירים את תת-המחרוזת שנבנתה עד הנקודה בה נמצא הבדל או הושג קצה של מחרוזת. אם יצאנו מיד (כלומר, באינדקס 0), מוחזרת מחרוזת ריקה.

*   **יתרונות האלגוריתם:**
    *   **יעילות:** לאלגוריתם יש סיבוכיות זמן לינארית `O(m * n)`, כאשר `n` הוא אורך המערך, ו-`m` הוא אורך המחרוזת הקצרה ביותר במערך.
    *   **השוואת תווים תו אחר תו:** מאפשר להימנע מהשוואות מיותרות, בזכות בדיקת התווים תו אחר תו.
    *   **פשטות:** קל להבין את הקוד ולממש אותו.

**דוגמאות (פסאודו-קוד):**
```
function longest_common_prefix(words):
  if length(words) == 0:
      return ""
  first_word = words[0]
  for index from 0 to length(first_word) -1 :
     for other_word in words:
        if index is beyond length of other_word or first_word[index] != other_word[index]
           return  first_word[0,index]

    return first_word
```

**דוגמאות מימוש בפייתון:**
```python
def longest_common_prefix(words):
    if not words:
        return ""
    first_word = words[0]
    for index, char in enumerate(first_word):
        for other_word in words:
            if index >= len(other_word) or other_word[index] != char:
                return first_word[:index]
    return first_word


words1 = ["дог", "домен", "домра", "доширак"]
print(f"קלט: words = {words1}")
print(f"פלט: '{longest_common_prefix(words1)}'") # יוצג: פלט: 'до'

words2 = ["документ", "кот", "кум", "ум"]
print(f"קלט: words = {words2}")
print(f"פלט: '{longest_common_prefix(words2)}'") # יוצג: פלט: ''

words3 = ["flower","flow","flight"]
print(f"קלט: words = {words3}")
print(f"פלט: '{longest_common_prefix(words3)}'") # יוצג: פלט: 'fl'
```

**ניתוח האפשרויות:**
*   **א. כדי לפתור את הבעיה, יש לעבור על כל תת-המחרוזות האפשריות של כל מחרוזת ולבדוק את התאמתן.:** שגוי, גישה כזו אינה יעילה.
*   **ב. כדי לפתור את הבעיה, יש להשתמש רק בלולאות ובתנאים ולבדוק את התחיליות אחת-אחת.:** שגוי.
*   **ג. כדי לפתור את הבעיה, יש להשתמש בשיטה המשווה תווים במחרוזות תו אחר תו עד אשר נמצא הבדל, או עד שהושג סופה של אחת המחרוזות.:** נכון.
*   **ד. כדי לפתור את הבעיה, יש למיין את כל המחרוזות לפי אורכן ולהשתמש במחרוזת הקצרה ביותר, מכיוון שהיא עשויה להכיל את התחילית המשותפת המקסימלית.:** שגוי. מיון אינו נחוץ.

**לסיכום:**
*   השוואת תווים תו אחר תו מאפשרת למצוא ביעילות את התחילית המשותפת.
*   האלגוריתם בוחן תווים במחרוזת, כל עוד התווים במחרוזות האחרות זהים וכל עוד לא הושג סופה של לפחות מחרוזת אחת.

לפיכך, התשובה הנכונה היא **ג. כדי לפתור את הבעיה, יש להשתמש בשיטה המשווה תווים במחרוזות תו אחר תו עד אשר נמצא הבדל, או עד שהושג סופה של אחת המחרוזות.**