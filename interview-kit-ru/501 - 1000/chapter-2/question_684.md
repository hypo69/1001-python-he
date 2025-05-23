### `question_684.md`

**שאלה 684.** נתונה מערך של תווים `chars`. יש לממש אלגוריתם לדחיסת המערך, בהתאם לכלל: עבור כל קבוצה של תווים רצופים חוזרים:

*   אם אורך הקבוצה שווה ל-1, יש להוסיף את התו למחרוזת הדחוסה.
*   אם אורך הקבוצה גדול מ-1, יש להוסיף את התו ולאחריו את אורך הקבוצה.

המחרוזת הדחוסה צריכה להישמר במערך הקלט `chars`. יש להחזיר את האורך החדש של המערך לאחר הדחיסה. הדרישה לאלגוריתם היא שימוש בזיכרון עזר קבוע בלבד.

**דוגמה:**

```
קלט: chars = ["a","a","b","b","c","c","c"]
פלט: 6, ו-6 האלמנטים הראשונים של המערך chars צריכים להיות: ["a","2","b","2","c","3"]

קלט: chars = ["a"]
פלט: 1, ו-1 האלמנטים הראשונים של המערך chars צריכים להיות: ["a"]

קלט: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
פלט: 4, ו-4 האלמנטים הראשונים צריכים להיות: ["a", "b", "1", "2"]
```

-   א. לפתרון בעיה זו נדרשת רקורסיה וזיכרון עזר O(n).
-   ב. לפתרון בעיה זו יש לעבור בלולאה על רשימת הקלט, לאסוף תווים חוזרים ולשמור את התוצאה ברשימה זמנית, ובסוף להחליף את הרשימה המקורית ולהחזיר את אורכה.
-   ג. לפתרון בעיה זו ניתן להשתמש בשני מצביעים, למעקב אחר תחילת וסוף רצף התווים החוזרים, ולשנות את הרשימה המקורית במקום (in-place), כאשר לא יידרש זיכרון עזר נוסף.
-   ד. לפתרון בעיה זו יש להשתמש בטבלת גיבוב (hash table) לשמירת הערכים ומספר החזרות שלהם.

**התשובה הנכונה: ג**

**הסבר:**

לפתרון בעיית דחיסת מערך תווים במקום (in-place) עם סיבוכיות זמן של O(n) וסיבוכיות מרחב קבועה של O(1) ניתן להשתמש בשיטת שני המצביעים.

*   **אלגוריתם עם שני מצביעים:**
    *   **מצביע `read`:** משמש לקריאת תווים מהרשימה המקורית.
    *   **מצביע `write`:** משמש לכתיבת הנתונים הדחוסים לרשימה המקורית.
    *   **מעבר:** עוברים על התווים עד שמגיעים לסוף הרשימה, החל מ-`read=0`.
    *   **איתור רצף:** כל עוד `read` מצביע על תחילת רצף של תווים זהים.
    *   **ספירת חזרות:** סופרים את מספר החזרות של התו הנוכחי.
    *   **כתיבה למערך הדחוס:** אם היו חזרות, כותבים למערך התוצאה את התו עצמו, ולאחר מכן את מספר החזרות (אם הן גדולות מ-1).
    *   **מעבר:** מזיזים את `read` עד התו הייחודי הבא.

*   **יתרונות האלגוריתם:**
    *   **זיכרון קבוע:** משתמש בנפח קבוע של זיכרון עזר נוסף, מכיוון שהוא משנה את המערך המקורי (in place).
    *   **סיבוכיות ליניארית:** האלגוריתם עובר על המערך פעם אחת, ולכן סיבוכיות הזמן שווה ל-O(n).

**דוגמאות (פסאודו-קוד):**
```
function compress_string(chars):
    read = 0
    write = 0
    while read < length(chars):
        start = read
        while read < length(chars) and chars[start] == chars[read]:
            read +=1
        chars[write] = chars[start]
        write+=1
        if read - start > 1:
          count = str(read-start)
          for char in count:
              chars[write] = char
              write+=1
    return write
```
**דוגמאות מימוש בפייתון:**
```python
def compress_string(chars):
    write = 0
    read = 0
    while read < len(chars):
        start = read
        while read < len(chars) and chars[start] == chars[read]:
            read += 1
        chars[write] = chars[start]
        write += 1
        if read - start > 1:
            count = str(read - start)
            for char in count:
               chars[write] = char
               write += 1
    return write


chars1 = ["a","a","b","b","c","c","c"]
length1 = compress_string(chars1)
print(f"הרשימה המצומצמת {chars1[:length1]}, אורך {length1}")  # ידפיס: הרשימה המצומצמת ['a', '2', 'b', '2', 'c', '3'], אורך 6

chars2 = ["a"]
length2 = compress_string(chars2)
print(f"הרשימה המצומצמת {chars2[:length2]}, אורך {length2}")  # ידפיס: הרשימה המצומצמת ['a'], אורך 1


chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
length3 = compress_string(chars3)
print(f"הרשימה המצומצמת {chars3[:length3]}, אורך {length3}") # ידפיס: הרשימה המצומצמת ['a', 'b', '1', '2'], אורך 4
```

**ניתוח האפשרויות:**
*   **א. לפתרון בעיה זו נדרשת רקורסיה וזיכרון עזר O(n).:** שגוי.
*   **ב. לפתרון בעיה זו יש לעבור בלולאה על רשימת הקלט, לאסוף תווים חוזרים ולשמור את התוצאה ברשימה זמנית, ובסוף להחליף את הרשימה המקורית ולהחזיר את אורכה.:** שגוי, שיטה זו דורשת זיכרון עזר נוסף.
*   **ג. לפתרון בעיה זו ניתן להשתמש בשני מצביעים, למעקב אחר תחילת וסוף רצף התווים החוזרים, ולשנות את הרשימה המקורית במקום (in-place), כאשר לא יידרש זיכרון עזר נוסף.:** נכון.
*   **ד. לפתרון בעיה זו יש להשתמש בטבלת גיבוב (hash table) לשמירת הערכים ומספר החזרות שלהם.:** שגוי. טבלת גיבוב אינה פתרון אופטימלי.

**לסיכום:**
*   שיטת שני המצביעים מאפשרת לדחוס את המחרוזת "in-place" (ללא הקצאת זיכרון עזר נוסף).
*   סיבוכיות האלגוריתם שווה ל-O(n), מכיוון שעוברים על המערך פעם אחת.

לפיכך, התשובה הנכונה היא **ג. לפתרון בעיה זו ניתן להשתמש בשני מצביעים, למעקב אחר תחילת וסוף רצף התווים החוזרים, ולשנות את הרשימה המקורית במקום (in-place), כאשר לא יידרש זיכרון עזר נוסף.**