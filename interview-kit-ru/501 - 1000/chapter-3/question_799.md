### `question_799.md`

**שאלה 799.** הצפן את הטקסט `"To be, or not to be, that is the question!"` באמצעות אלגוריתם צופן קיסר (צופן הזזה), על ידי הזזת כל תו ימינה ב-1717 עמדות.

*   יש להשתמש באלפבית:
    *   אותיות לטיניות קטנות: `'abcdefghijklmnopqrstuvwxyz'`
    *   אותיות לטיניות גדולות: `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`
*  תווים שאינם שייכים לאלפבית נשארים ללא שינוי.

-   A. עבור הצפנת קיסר, יש להחליף את כל התווים ברווחים, והרישום אינו נלקח בחשבון.
- B.  עבור הצפנת קיסר יש להשתמש בפונקציה `encode()`, עם פרמטר הצפנה.
-   C.  עבור הצפנת קיסר יש להשתמש בלולאות ובהזזה של 1717, ובנוסף להרחיב את האלפבית.
-   D. לפתרון הבעיה יש להשתמש באלגוריתם עם היסט קבוע על בסיס מספר התו, תוך שימוש בלולאות, ובנוסף יש לטפל במקרה של גלישת האלפבית, על ידי מעבר מחזורי לתחילת האלפבית.

**תשובה נכונה: D**

**הסבר:**

לצורך הצפנת טקסט באמצעות צופן קיסר (צופן הזזה) משתמשים באלגוריתם המזיז כל תו במחרוזת במספר עמדות נתון ימינה (באופן מחזורי, כלומר אחרי `z` מגיע `a`), ושומר את כל התווים שאינם אותיות ללא שינוי.

*   **אלגוריתם צופן קיסר (עם הזזה):**
    1.  **הגדרת אלפביתים:** יוצרים מראש אלפביתים לתווים קטנים וגדולים.
    2.  **איטרציה על המחרוזת:** מבצעים איטרציה על מחרוזת הקלט תו אחר תו:
        *  **בדיקת רישום:** אם התו הנוכחי הוא אות גדולה, מחשבים את התו המוזז באותיות גדולות.
             *   אם התו הנוכחי הוא אות קטנה, מחשבים את התו המוזז באותיות קטנות.
          *  **הזזה מחזורית:** מוצאים את האינדקס של התו הנוכחי באלפבית.
            *  מחשבים את האינדקס החדש לאחר ההזזה, ומבטיחים הזזה מחזורית אם סכום האינדקס וההזזה עולה על אורך האלפבית.
          * **תו שאינו שייך לאלפבית:** אם התו הנוכחי אינו אות, מוסיפים אותו למחרוזת ללא שינוי.
    3. **מחרוזת תוצאה:** מחזירים את המחרוזת עם התווים המוצפנים.

*   **יתרונות האלגוריתם:**
    *   **הצפנה:** האלגוריתם מאפשר להצפין מחרוזת על ידי הזזת כל תו במספר נתון.
    *  **טיפול ברישום:** האלגוריתם מטפל נכונה הן באותיות גדולות והן באותיות קטנות.
    *  **פשטות:** הקוד מובן וקל ליישום.

**דוגמאות (פסאודו-קוד):**
```
function caesar_cipher(s, shift):
    new_string = empty string
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for symbol in string s:
      if symbol is upper:
        add shifted upper symbol from alphabet with shift
      if symbol is lower:
         add shifted lower symbol from alphabet with shift
      else:
          add symbol without change
    return new_string
```
**דוגמאות ליישום בפייתון:**
```python
def transcode(s):
    new_s = ''
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = 1717
    for i in range(len(s)):
        if s[i].isupper():
            ind = eng_upper_alphabet.find(s[i])
            while not ind + shift < len(eng_upper_alphabet):
                 eng_upper_alphabet += eng_upper_alphabet
            new_s += eng_upper_alphabet[ind + shift]
        elif s[i].islower():
            ind = eng_lower_alphabet.find(s[i])
            while not ind + shift < len(eng_lower_alphabet):
                eng_lower_alphabet += eng_lower_alphabet
            new_s += eng_lower_alphabet[ind + shift]
        else:
            new_s += s[i]
    return new_s

s = 'To be, or not to be, that is the question!'
print(f"Ввод: s = '{s}'")
print(f"Вывод: {transcode(s)}") # Выведет: Вывод: Kf sv, fi efk kf sv, kyrk zj kyv hlvjkzfe!
```

**ניתוח האפשרויות:**
*  **A. לפתרון הבעיה יש להשתמש רק באופרטור התנאי `if-elif-else`, לטיפול בכל ספרה של המספר.:** לא נכון.
*   **B. לפתרון הבעיה יש להשתמש בפונקציה `encode()`, עם פרמטר הצפנה.:** לא נכון.
*   **C. לפתרון הבעיה יש להשתמש בלולאות ובהזזה של 1717, ובנוסף להרחיב את האלפבית.:** נכון, אך אינו מתאר במפורש את ההזזה.
*   **D. לפתרון הבעיה יתאים רק אלגוריתם חמדן, שבו בכל שלב בוחרים את התו הנוכחי לקידוד.:** לא נכון.

**לסיכום:**
*  להצפנה משתמשים בהזזת תווים במספר עמדות נתון.
*   `isupper()` ו-`islower()` מאפשרים לעבוד נכונה עם תווים ברישום שונה.
*   בחישוב האינדקס, משתמשים בהזזה מחזורית.

לפיכך, התשובה הנכונה היא **C. לפתרון הבעיה יש להשתמש בלולאות ובהזזה של 1717, ובנוסף להרחיב את האלפבית.**