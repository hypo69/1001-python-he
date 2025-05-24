### `question_630.md`

**שאלה 630.** כיצד ניתן להסיר את כל תווי הרווח ממחרוזת ב-Python? פרט/י לפחות שתי שיטות המדגימות את הסרת תווי הרווח.

- א. כדי להסיר תווי רווח, יש להשתמש בשיטה `delete_spaces()`.
- ב. כדי להסיר תווי רווח, ניתן להשתמש בשיטה `strip()` או בשיטות `lstrip()` ו-`rstrip()`.
- ג. כדי להסיר תווי רווח, ניתן להשתמש בשיטה `replace(' ', '')` או בשיטה `join(string.split())`.
- ד. כדי להסיר תווי רווח, יש להשתמש רק בביטויים רגולריים.

**תשובה נכונה: ג**

**הסבר:**

ב-Python, הסרת כל תווי הרווח ממחרוזת יכולה להתבצע במספר דרכים. הדרך הנפוצה ביותר היא באמצעות שיטת המחרוזת `replace()`. אפשרות נוספת היא לפצל את המחרוזת לפי תווי רווח ולצרף אותה מיד בחזרה, אך ללא תווי רווח, מה שמתבצע באמצעות שילוב של השיטות `split()` ו-`join()`.

* **השיטה `replace()`:**
    * **החלפת תת-מחרוזות:** השיטה `replace()` מאפשרת להחליף את כל המופעים של תת-מחרוזת אחת באחרת.
    * **הסרת תווי רווח:** כדי להסיר תווי רווח ממחרוזת, מחליפים את כל תווי הרווח `"` במחרוזת ריקה `""`, כלומר מסירים אותם.
    * **מחרוזת חדשה:** השיטה מחזירה מחרוזת חדשה, בעוד שהמחרוזת המקורית נשארת ללא שינוי.
    * **תחביר:** `string.replace(old, new)`.
* **השיטות `split()` ו-`join()`:**
    * **`split()`:** השיטה `split()` מפצלת מחרוזת לרשימת מחרוזות, באמצעות מפריד (כברירת מחדל: רווח).
    * **`join()`:** השיטה `join()` מאחדת רשימת מחרוזות למחרוזת אחת, באמצעות מחרוזת מפרידה (במקרה זה: מחרוזת ריקה).
    * בשילוב שיטות אלו, ניתן לפצל מחרוזת לפי תווי רווח ולאחר מכן לחבר אותה, אך ללא תווי רווח.
    * **מחרוזת חדשה:** השיטה מחזירה מחרוזת חדשה, בעוד שהמחרוזת המקורית נשארת ללא שינוי.
    * **תחביר:**
        * `string.split(separator)`
        * `separator.join(iterable)`

**דוגמאות:**

```python
# Example 1: Using replace() to remove spaces
my_string = ' A string with white space '
new_string = my_string.replace(' ', '')
print(f"מחרוזת מקורית: '{my_string}'")
print(f"מחרוזת ללא רווחים: '{new_string}'") # Output: String without spaces: 'Astringwithwhitespace'

# Example 2: Using split() and join() to remove spaces
my_string2 = ' A string with white space '
new_string2 = ''.join(my_string2.split())
print(f"מחרוזת מקורית: '{my_string2}'")
print(f"מחרוזת ללא רווחים: '{new_string2}'") # Output: String without spaces: 'Astringwithwhitespace'
# Example with different whitespace characters
my_string3 = "A \tstring\nwith  \rwhite space "
new_string3 = my_string3.replace(" ","").replace("\t","").replace("\n","").replace("\r","")
print(f"מחרוזת עם תווי רווח שונים: {my_string3}")
print(f"מחרוזת ללא רווחים (replace): {new_string3}") # Output: Astringwithwhitespace

new_string4 = ''.join(my_string3.split())
print(f"מחרוזת ללא רווחים (split join): {new_string4}") # Output: Astringwithwhitespace

```
**ניתוח האפשרויות:**
* **א. כדי להסיר תווי רווח, יש להשתמש בשיטה `delete_spaces()`.:** שגוי.
* **ב. כדי להסיר תווי רווח, ניתן להשתמש בשיטה `strip()` או בשיטות `lstrip()` ו-`rstrip()`.:** שגוי, שיטות אלו מסירות תווי רווח רק מתחילת ומסוף המחרוזת.
* **ג. כדי להסיר תווי רווח, ניתן להסיר תווי רווח, ניתן להשתמש בשיטה `replace(' ', '')` או בשיטה `join(string.split())`.:** נכון.
* **ד. כדי להסיר תווי רווח, יש להשתמש רק בביטויים רגולריים.:** שגוי.

**לסיכום:**
* השיטה `replace()` מאפשרת להסיר בקלות את כל מופעי תווי הרווח ממחרוזת.
* השילוב של `split()` ו-`join()` גם מאפשר להסיר תווי רווח ממחרוזת, אך דורש יותר קוד.

לפיכך, התשובה הנכונה היא **ג. כדי להסיר תווי רווח, ניתן להשתמש בשיטה `replace(' ', '')` או בשיטה `join(string.split())`.**