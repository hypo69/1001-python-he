### `question_691.md`

**שאלה 691.** איזו שיטה ניתן להשתמש בה להחלפת חלקים של מחרוזת במחרוזת אחרת, ומהו התחביר של שיטה זו, אם ברצונך להחליף את 'cat' ב-'dog' במחרוזת
```python
s = "The cat sat on the mat"
```

- A.  `s.replaceString('cat', 'dog')`

- B.  `s.replace('cat', 'dog')`

- C.  `s.stringReplace('cat', 'dog')`

- D.  `s.replaceAll('cat', 'dog')`

**תשובה נכונה: B**

**הסבר:**

*   **השיטה `replace()`:** השיטה `replace()` ב-Python משמשת להחלפת תת-מחרוזת אחת במחרוזת בתת-מחרוזת אחרת. התחביר שלה: `מחרוזת.replace(מחרוזת_ישנה, מחרוזת_חדשה)`.

*   **שיטות שגויות:** השיטות `replaceString()`, `stringReplace()`, ו-`replaceAll()` אינן שיטות מחרוזת סטנדרטיות ב-Python.

**דוגמה:**

```python
s: str = "The cat sat on the mat"

# מחליפים את 'cat' ב-'dog' באמצעות replace()
new_s: str = s.replace('cat', 'dog')
print(new_s) # פלט: The dog sat on the mat

# ננסה להשתמש בתחביר שגוי
try:
    s.replaceString('cat', 'dog') # תגרום לשגיאה AttributeError: 'str' object has no attribute 'replaceString'
except AttributeError as e:
  print(f"שגיאה: {e}") # פלט: שגיאה: 'str' object has no attribute 'replaceString'
```

**לסיכום:**

*   אפשרות **B** `s.replace('cat', 'dog')` משתמשת נכונה בשיטה `replace()` להחלפת תת-המחרוזת `'cat'` ב-`'dog'` במחרוזת `s`.

*   האפשרויות **A**, **C**, ו-**D** משתמשות בשיטות שאינן קיימות, ושימוש בהן יגרום לשגיאה `AttributeError`.

לפיכך, התשובה **B** היא הנכונה, משום שהיא מדגימה שימוש נכון בשיטה `replace()` ובתחביר שלה.