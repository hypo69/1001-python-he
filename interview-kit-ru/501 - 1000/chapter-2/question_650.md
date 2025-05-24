### `question_650.md`

**שאלה 650.** מהי תוצאת הרצת קוד Python הבא וכיצד פועלת המתודה `isdisjoint()`?

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

-   א. `True False True False`
-   ב. `False True False True`
-   ג. `True False False True`
-   ד. `False True True False`

**תשובה נכונה: C**

**הסבר:**

קוד זה מדגים את השימוש במתודה `isdisjoint()` לבדיקה האם קיימים אלמנטים משותפים בין קבוצה לאובייקט איטרבילי. המתודה `isdisjoint()` מחזירה `True` אם לקבוצה ולאובייקט האיטרבילי אין אלמנטים משותפים, ומחזירה `False` אם קיימים אלמנטים משותפים.

1.  **בלוק ראשון:**
    *   `set_x = {0, 1, 2, 3, 4}`: נוצרת קבוצה `set_x` עם האלמנטים מ-0 עד 4.
    *   `list_y = [5, 6, 7, 8, 9]`: נוצרת רשימה `list_y` עם האלמנטים מ-5 עד 9.
    *   `set_x.isdisjoint(list_y)`: בודק האם קיימים אלמנטים משותפים בין `set_x` לבין `list_y`. מאחר שאין אלמנטים משותפים, מוחזר `True`.
2. **בלוק שני:**
     *   `list_y[0] = 4`: האלמנט הראשון ברשימה `list_y` משתנה, כך שכעת `list_y` היא `[4, 6, 7, 8, 9]`.
     *   `set_x.isdisjoint(list_y)`: בודק האם קיימים אלמנטים משותפים בין `set_x` לבין `list_y` שהשתנתה. מאחר שהמספר 4 הוא אלמנט משותף, מוחזר `False`.
3.  **בלוק שלישי:**
    *   `fset = frozenset(['march', 'dec', 'feb', 'may'])`: נוצר `frozenset` (קבוצה בלתי ניתנת לשינוי) עם האלמנטים.
    *   `tuple_y = ('july', 'aug', 'june', 'jan', 'may')`: נוצרת טאפל `tuple_y`.
    *   `fset.isdisjoint(tuple_y)`: בודק האם קיימים אלמנטים משותפים בין `fset` לבין `tuple_y`. מאחר שיש להם אלמנט משותף (`may`), המתודה מחזירה `False`.
4.  **בלוק רביעי:**
    *   `fset = frozenset(['march', 'dec', 'feb'])`: נוצר `frozenset` עם אלמנטים חדשים שאינם קיימים ב-`tuple_y`.
    *   `fset.isdisjoint(tuple_y)`: בודק האם קיימים אלמנטים משותפים בין `fset` לבין `tuple_y`. מאחר שאין אלמנטים משותפים, מוחזר `True`.

**ניתוח האפשרויות:**
*   **א. `True False True False`:** שגוי.
*   **ב. `False True False True`:** שגוי.
*   **ג. `True False False True`:** נכון.
*   **ד. `False True True False`:** שגוי.

**לסיכום:**
*   המתודה `isdisjoint()` מחזירה `True` אם אין אלמנטים משותפים, ומחזירה `False` אם קיימים אלמנטים משותפים.
*   הדוגמאות מראות כיצד נתונים ניתנים לשינוי עשויים להשפיע על תוצאת קריאה ל-`isdisjoint`.

לפיכך, התשובה הנכונה היא **C. `True False False True`**.