### `question_119.md`

**שאלה 119.** מה התפקיד של הפונקציה `enumerate()` בלולאה בפייתון?

- א. היא מוסיפה מונה לאובייקט ניתן לאיטרציה ומחזירה אותו כאובייקט `enumerate`, שניתן להשתמש בו בלולאות כדי לקבל גם את האינדקס וגם את הערך של כל איבר.
- ב. היא ממיינת את האובייקט הניתן לאיטרציה לפני הלולאה כדי לשפר את יעילות הלולאה.
- ג. היא ממירה את כל האיברים הניתנים לאיטרציה לאינדקסים מספריים, ומתעלמת מהערכים המקוריים.
- ד. היא משמשת למיזוג שני אובייקטים שונים הניתנים לאיטרציה לאובייקט אחד הניתן לאיטרציה עבור הלולאה.

**תשובה נכונה: א**

**הסבר:**

הפונקציה `enumerate()` בפייתון משמשת לאיטרציה על פני רצף (כגון רשימה, טיפל) תוך גישה בו-זמנית לאינדקס ולערך של כל איבר.

*   **אפשרות א** נכונה: `enumerate()` מוסיפה מונה ומחזירה טיפל, כאשר האיבר הראשון הוא האינדקס, והשני הוא הערך.
*   **אפשרות ב** אינה נכונה: `enumerate()` אינה ממיינת את האובייקט הניתן לאיטרציה, אלא רק יוצרת איטרטור עם אינדקסים.
*   **אפשרות ג** אינה נכונה: `enumerate` אינה משנה את האיברים לאינדקסים מספריים.
*   **אפשרות ד** אינה נכונה: `enumerate` אינה מאחדת אובייקטים ניתנים לאיטרציה; לשם כך קיימת הפונקציה `zip`.

**כיצד פועלת הפונקציה `enumerate()`:**

1.  הפונקציה `enumerate()` מקבלת כאוסף קלט אובייקט ניתן לאיטרציה (רשימה, טיפל, וכו').
2.  היא מחזירה איטרטור, אשר יוצר זוגות `(index, element)` עבור כל איבר באובייקט הניתן לאיטרציה.
3.  האינדקס כברירת מחדל מתחיל מ-0, אך ניתן לשנות זאת על ידי העברת פרמטר אופציונלי `start`.

**דוגמה:**

```python
my_list: list[str] = ["apple", "banana", "cherry"]

# שימוש ב-enumerate() כדי לקבל אינדקסים וערכים
for index, value in enumerate(my_list):
    print(f"Индекс: {index}, Значение: {value}")
# פלט:
# אינדקס: 0, ערך: apple
# אינדקס: 1, ערך: banana
# אינדקס: 2, ערך: cherry

# שימוש ב-enumerate() עם אינדקס התחלתי
for index, value in enumerate(my_list, start=1):
    print(f"Индекс: {index}, Значение: {value}")
# פלט:
# אינדקס: 1, ערך: apple
# אינדקס: 2, ערך: banana
# אינדקס: 3, ערך: cherry
```

**לסיכום:**
*   `enumerate(my_list)` מחזירה אובייקט ניתן לאיטרציה, אשר בלולאת `for` יוצר טיפל `(index, element)`.
*   `enumerate(my_list, start=1)` משתמשת באינדקס התחלתי `1` במקום `0`.

לכן, **אפשרות א** היא הנכונה.