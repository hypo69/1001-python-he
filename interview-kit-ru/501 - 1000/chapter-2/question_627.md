### `question_627.md`

**שאלה 627.** כיצד ניתן ב-Python לשלב שתי רשימות לרשימת טאפלים (tuples), כאשר כל טאפל מכיל איברים בעלי אותם אינדקסים מהרשימות המקוריות?

-   א. ניתן לשלב שתי רשימות לרשימת טאפלים באמצעות שיטת (method) `join_tuples()`.
-   ב. ניתן לשלב שתי רשימות לרשימת טאפלים באמצעות האופרטור `+`.
-   ג. ניתן לשלב שתי רשימות לרשימת טאפלים באמצעות הפונקציה `zip()` ומחולל רשימות (list comprehension).
-   ד. שילוב שתי רשימות לרשימת טאפלים אינו אפשרי.

**תשובה נכונה: ג**

**הסבר:**

ב-Python, לשילוב שתי רשימות או יותר לרשימת טאפלים, בה כל טאפל מכיל איברים בעלי אותם אינדקסים מהרשימות המקוריות, משתמשים בפונקציה המובנית `zip()` בשילוב עם list comprehension (מחולל רשימות).

*   **הפונקציה `zip()`:**
    *   **יוצרת איטרטור (iterator):** מקבלת מספר אובייקטים הניתנים לאיטרציה (iterable) (לדוגמה, רשימות, טאפלים) ויוצרת איטרטור.
    *   **טאפלים:** האיטרטור מחזיר טאפלים, כאשר כל טאפל מכיל איברים בעלי אותו אינדקס מתוך האובייקטים הניתנים לאיטרציה שהועברו.
    *   **הגבלה באורך:** איטרטור ה-`zip` נעצר כאשר האובייקט הניתן לאיטרציה הקצר ביותר מבין האובייקטים שהועברו מסתיים.
*   **List comprehension:**
   *    `[(k,v) for k,v in zip(list1, list2)]`: ניתן ליצור רשימה עם טאפלים באמצעות שימוש במחולל רשימות.

**דוגמאות:**

```python
# דוגמה 1: שילוב שתי רשימות לרשימת טאפלים
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
tuple_list = [(k, v) for k, v in zip(list1, list2)]
print(f"רשימת טאפלים משולבת: {tuple_list}") # פלט: [('a', 1), ('b', 2), ('c', 3)]

# דוגמה 2: שילוב שתי רשימות באורכים שונים (הערכים הנותרים יתעלמו)
list3 = ['a', 'b', 'c']
list4 = [1, 2]
tuple_list2 = [(k, v) for k, v in zip(list3, list4)]
print(f"רשימת טאפלים משולבת (אורכים שונים): {tuple_list2}") # פלט: [('a', 1), ('b', 2)]


# דוגמה 3: שילוב יותר משתי רשימות
list5 = ['a', 'b', 'c']
list6 = [1, 2, 3]
list7 = ["one", "two", "three"]
tuple_list3 = [(k, v, w) for k, v, w in zip(list5, list6, list7)]
print(f"רשימת טאפלים משולבת משלוש רשימות: {tuple_list3}") # פלט: [('a', 1, 'one'), ('b', 2, 'two'), ('c', 3, 'three')]

# דוגמה 4: העברת טאפל
tuple1 = ('a','b','c')
tuple2 = (1,2,3)
tuple_list4 = [(k,v) for k,v in zip(tuple1, tuple2)]
print(f"רשימת טאפלים משולבת משני טאפלים: {tuple_list4}") # פלט [('a', 1), ('b', 2), ('c', 3)]

# דוגמה לשילוב עם מילון
list11 = ['a', 'b', 'c']
dict12 = {1:'x', 2:'y', 3:'z'}
tuple_list5 = [(k,v) for k,v in zip(list11, dict12.values())] #
print(f"רשימת טאפלים משולבת (מילון ורשימה): {tuple_list5}") # פלט [('a', 'x'), ('b', 'y'), ('c', 'z')]
```

**ניתוח האפשרויות:**
*   **א. ניתן לשלב שתי רשימות לרשימת טאפלים באמצעות שיטת (method) `join_tuples()`. :** שגוי. שיטה זו אינה קיימת בפייתון למטרה זו.
*   **ב. ניתן לשלב שתי רשימות לרשימת טאפלים באמצעות האופרטור `+`. :** שגוי. האופרטור `+` עבור רשימות מבצע שרשור (concatenation), לא יוצר רשימת טאפלים.
*  **ג. ניתן לשלב שתי רשימות לרשימת טאפלים באמצעות הפונקציה `zip()` ומחולל רשימות. :** נכון. זו הדרך הסטנדרטית והיעילה בפייתון לבצע זאת.
*  **ד. שילוב שתי רשימות לרשימת טאפלים אינו אפשרי. :** שגוי. כפי שהודגם, זה אפשרי באמצעות `zip` ומחולל רשימות.

**לסיכום:**
*  `zip` ומחולל רשימות (list comprehension) מאפשרים לשלב שתי רשימות או יותר לרשימת טאפלים.
*   `zip` יוצר איטרטור של טאפלים.

לפיכך, התשובה הנכונה היא **ג. ניתן לשלב שתי רשימות לרשימת טאפלים באמצעות הפונקציה `zip()` ומחולל רשימות.**