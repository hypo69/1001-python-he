### `question_412.md`

**שאלה 412.** מהי תוצאת הרצת קוד Python הבא וכיצד פועלת המתודה `isdisjoint()`?

```python
set_x = {0, 1, 2, 3, 4}
list_y = [5, 6, 7, 8, 9]
print(set_x.isdisjoint(list_y))

list_y[0] = 4
print(set_x.isdisjoint(list_y))

fset = frozenset(['march', 'dec', 'feb', 'may'])
tuple_y = ('july', 'aug', 'june', 'jan', 'may')
print(fset.isdisjoint(tuple_y))


fset = frozenset(['march', 'dec', 'feb'])
print(fset.isdisjoint(tuple_y))
```

-   A. `True False True False`
-   B. `False True False True`
-   C. `True False False True`
-   D. `False True True False`

**התשובה הנכונה: C**

**הסבר:**

קוד זה מדגים את השימוש במתודה `isdisjoint()` לבדיקה האם לקבוצה ולאובייקט ניתן-לאיטרציה אין איברים משותפים. המתודה `isdisjoint()` מחזירה `True` אם לקבוצה ולאובייקט ניתן-לאיטרציה אין איברים משותפים, ו-`False` אם יש להם.

1.  **בלוק ראשון:**
    *   `set_x = {0, 1, 2, 3, 4}`: נוצרת קבוצה `set_x` עם האיברים מ-0 עד 4.
    *   `list_y = [5, 6, 7, 8, 9]`: נוצרת רשימה `list_y` עם האיברים מ-5 עד 9.
    *  `set_x.isdisjoint(list_y)`: בודק האם יש איברים משותפים בין `set_x` לבין `list_y`. מכיוון שאין איברים משותפים, מוחזר `True`.
2. **בלוק שני:**
     *   `list_y[0] = 4`: משתנה האיבר הראשון ברשימה `list_y`, כך שעכשיו `list_y` היא `[4, 6, 7, 8, 9]`.
     * `set_x.isdisjoint(list_y)`: בודק האם יש איברים משותפים בין `set_x` לבין `list_y` שהשתנתה. מכיוון שהמספר 4 הוא איבר משותף, מוחזר `False`.
3.  **בלוק שלישי:**
    *   `fset = frozenset(['march', 'dec', 'feb', 'may'])`: נוצר `frozenset` (קבוצה בלתי ניתנת לשינוי) עם איברים.
    *   `tuple_y = ('july', 'aug', 'june', 'jan', 'may')`: נוצרת טאפל `tuple_y`.
     *  `fset.isdisjoint(tuple_y)`: בודקת האם יש איברים משותפים בין `fset` לבין `tuple_y`. מכיוון שיש להם איבר משותף (`may`), המתודה מחזירה `False`.
4.  **בלוק רביעי:**
    * `fset = frozenset(['march', 'dec', 'feb'])`: נוצר `frozenset` עם איברים חדשים, שאינם כלולים בתוך `tuple_y`.
    * `fset.isdisjoint(tuple_y)`: בודקת האם יש איברים משותפים בין `fset` לבין `tuple_y`. מכיוון שאין איברים משותפים, מוחזר `True`.

**ניתוח האפשרויות:**
*   **A. `True False True False`:** שגוי.
*   **B. `False True False True`:** שגוי.
*  **C. `True False False True`:** נכון.
*   **D. `False True True False`:** שגוי.

**לסיכום:**
*  המתודה `isdisjoint()` מחזירה `True` אם אין איברים משותפים, ו-`False` אם יש איברים משותפים.
*  הדוגמאות מראות כיצד נתונים הניתנים לשינוי יכולים להשפיע על תוצאת הקריאה ל-`isdisjoint`.

לפיכך, התשובה הנכונה היא **C. `True False False True`**.