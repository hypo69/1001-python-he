### `question_734.md`

**שאלה 734.** נתונה לכם מחרוזת `s` המכילה מספר מילים המופרדות באמצעות רווחים (ייתכנו מספר רווחים בין מילים, וכן רווחים בתחילת או בסוף המחרוזת). פתחו אלגוריתם ב-Python אשר הופך את סדר המילים במחרוזת. במחרוזת התוצאה, בין המילים צריך להיות רווח יחיד בלבד, ולא צריכים להיות רווחים בתחילת המחרוזת ובסופה.

*   זמן ביצוע הסקריפט לא צריך לעלות על שנייה אחת.

**דוגמאות:**
```
Ввод: s = " Быстрый автомобиль "
Вывод: "автомобиль Быстрый"
```

*   א. כדי לפתור את הבעיה יש להשתמש ברקורסיה ובהחלפה סדרתית של מילים במחרוזת, ולאחר מכן לחלץ אותן מהזיכרון.
*   ב. כדי לפתור את הבעיה יש להשתמש בלולאת for וליצור מחרוזת חדשה על ידי הוספת מילים בסדר הפוך.
*   ג. כדי לפתור את הבעיה נעשה שימוש בשני מצביעים (החל מסוף המחרוזת), וכן בלולאה מקוננת לבחירת מילה והוספתה למחרוזת התוצאה.
*   ד. כדי לפתור את הבעיה יש תחילה למיין את המילים לפי אורך ולאחר מכן ליצור את המחרוזת בסדר הפוך.

**תשובה נכונה: ג**

**הסבר:**

לפתרון בעיית היפוך סדר המילים במחרוזת, תוך טיפול ברווחים מיותרים, האלגוריתם האופטימלי הוא שימוש באלגוריתם המשתמש בשני מצביעים, הנעים מסוף המחרוזת לראשה, ותוך כדי כך חולץ מילים ומוסיף אותן למחרוזת התוצאה. אלגוריתם כזה מאפשר לפתור את הבעיה בזמן לינארי O(n), ותוך הימנעות משימוש בזיכרון מיותר.

*   **אלגוריתם (שני מצביעים):**
    1.  **בדיקה:** אם המחרוזת המקורית ריקה או מורכבת מרווחים בלבד, מחזירים מחרוזת ריקה.
    2.  **אתחול:** מאתחלים מצביע `start` לסוף המחרוזת המקורית `len(str)-1`, וכן מחרוזת ריקה `ans`.
    3.  **מעבר מהסוף:** לולאת `while` מתבצעת כל עוד `start` לא הגיע לתחילת המחרוזת:
        *   **דילוג על רווחים:** אם התו הנוכחי (שעליו מצביע `start`) הוא רווח, ממשיכים להזיז את `start` שמאלה עד שהוא מפסיק להיות רווח.
        *   **הוספת רווח:** אם מחרוזת התוצאה `ans` אינה ריקה, מוסיפים רווח בסוף `ans`.
        *   **חילוץ מילה:** לאחר מכן יש לולאת `while` פנימית, שבה `j` נע מ-`start` אחורה עד לרווח, ויוצר את המילה.
        *   **הוספה למחרוזת התוצאה:** מוסיפים את המילה שנחתכה למחרוזת התוצאה `ans`.
        *   מעדכנים את `start` למיקום `j`.
    4.  **תוצאה:** לאחר עיבוד כל התווים, מחזירים את מחרוזת התוצאה `ans` (אשר תכיל את המילים בסדר הפוך).

*   **יתרונות האלגוריתם:**
    *   **מורכבות לינארית:** האלגוריתם עובר על המחרוזת פעם אחת בלבד, מה שמבטיח מורכבות זמן של O(n), כאשר n הוא אורך המחרוזת.
    *   **יעילות:** האלגוריתם אינו דורש מבנים נתונים נוספים, זיכרון או מיון.
    *   **טיפול ברווחים:** מתחשב ברווחים מרובים.

**דוגמאות (קוד פסאודו):**

```
function reverse_words(str):
    if str is empty or all chars are spaces
        return ""

    ans = ""
    start = length(str) - 1

    while start >= 0:
      if str[start] is space:
           start = start - 1
       else:
         if length(ans)> 0 :
           ans = ans + " "
         j = start;
        while j >= 0 and str[j] is not space:
          j = j -1;
         ans = ans + substring(str, j+1, start) # add word to ans
        start = j
    return ans
```
**דוגמאות מימוש ב-Python:**
```python
def reverseString(str: str) -> str:
    if(str == "" or str == " "):
        return ""
    ans = ''

    start = len(str) - 1

    while(start >= 0):
        if(str[start] == ' '):
            start-=1
        else:
            if(len(ans) > 0):
                ans += (' ')

            j = start

            while(j >= 0 and str[j] != ' '):
                j-=1

            ans +=  (str[j+1: j+1+start-j])
            start = j

    return ans

str1 = " Быстрый автомобиль "
print(f"Ввод: s = '{str1}'")
print(f"Вывод: '{reverseString(str1)}'") # פלט: 'автомобиль Быстрый'


str2 = "   test   test2 test3  "
print(f"Ввод: s = '{str2}'")
print(f"Вывод: '{reverseString(str2)}'") # פלט: 'test3 test2 test'
str3 = ""
print(f"Ввод: s = '{str3}'")
print(f"Вывод: '{reverseString(str3)}'") # פלט: ''
str4 = "   "
print(f"Ввод: s = '{str4}'")
print(f"Вывод: '{reverseString(str4)}'") # פלט: ''
```

**ניתוח האפשרויות:**
*   **א. כדי לפתור את הבעיה יש להשתמש ברקורסיה ובהחלפה סדרתית של מילים במחרוזת, ולאחר מכן לחלץ אותן מהזיכרון.:** לא נכון. רקורסיה אינה יעילה בבעיה זו.
*   **ב. כדי לפתור את הבעיה יש להשתמש בלולאת for וליצור מחרוזת חדשה, על ידי הוספת מילים בסדר הפוך.:** לא נכון.
*   **ג. כדי לפתור את הבעיה נעשה שימוש בשני מצביעים (החל מסוף המחרוזת), וכן בלולאה מקוננת לבחירת מילה והוספתה למחרוזת התוצאה.:** נכון.
*   **ד. כדי לפתור את הבעיה יש תחילה למיין את המילים לפי אורך ולאחר מכן ליצור את המחרוזת בסדר הפוך.:** לא נכון.

**לסיכום:**
*   אלגוריתם עם שני מצביעים מטפל בתווי רווח ויוצר מחרוזת עם מילים בסדר הפוך.
*   לולאה כפולה מאפשרת ניתוח יעיל של המחרוזת.
*   האלגוריתם מבטיח מורכבות לינארית.

לפיכך, התשובה הנכונה היא **ג. כדי לפתור את הבעיה נעשה שימוש בשני מצביעים (החל מסוף המחרוזת), וכן בלולאה מקוננת לבחירת מילה והוספתה למחרוזת התוצאה.**