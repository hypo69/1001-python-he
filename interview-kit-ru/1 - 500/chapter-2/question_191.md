### `question_191.md`

**שאלה 191.** ב-Python, איזה אופרטור משמש לצורך בדיקה שאלמנט *אינו* נמצא ברצף (כגון רשימה, מחרוזת, tuple וכו')?

A. `not in`
B. `is not`
C. `not`
D. `!=`

**תשובה נכונה: A**

**הסבר:**

האופרטור `not in` ב-Python משמש לצורך בדיקה שאלמנט *אינו* נמצא באף רצף (כגון רשימה, מחרוזת, tuple וכו').

*   **אפשרות A** נכונה: `not in` בודק היעדרות של אלמנט באוסף.
*   **אפשרות B** אינה נכונה: `is not` בודק ששני אובייקטים אינם אותו אובייקט בדיוק, ולא בודק חברות באוסף.
*   **אפשרות C** אינה נכונה: `not` הופך ערך בוליאני, אך אינו בודק חברות באוסף.
*   **אפשרות D** אינה נכונה: `!=` בודק ששני אובייקטים אינם שווים בערכם, ולא בודק חברות באוסף.

**כיצד פועל `not in`:**

1.  האופרטור `not in` מחזיר `True` אם האלמנט לא נמצא ברצף שצוין.
2.  הוא מחזיר `False` אם האלמנט קיים ברצף.

**דוגמה:**

```python
my_list: list[int] = [1, 2, 3, 4, 5]

if 6 not in my_list:
   print("המספר 6 אינו קיים ברשימה") # פלט: המספר 6 אינו קיים ברשימה

if 3 not in my_list:
   print("המספר 3 אינו קיים ברשימה") # התנאי שקרי, ולכן הבלוק לא מבוצע.
```

**כתוצאה מכך:**

*   בדוגמה הראשונה, התנאי `6 not in my_list` הוא אמיתי (`True`), היות שהמספר 6 אינו נמצא ברשימה `my_list`.
*   בדוגמה השנייה, התנאי `3 not in my_list` הוא שקרי (`False`), היות שהמספר 3 נמצא ברשימה.

לפיכך, **אפשרות A** היא התשובה הנכונה.