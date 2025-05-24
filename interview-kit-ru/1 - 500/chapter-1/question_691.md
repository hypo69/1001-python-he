### `question_691.md`

**שאלה 691.** איזו מתודה ניתן להשתמש בה כדי להחליף חלקים ממחרוזת במחרוזת אחרת,
ומהו התחביר של מתודה זו, אם ברצונך להחליף את 'cat' ב-'dog' במחרוזת
```python
s = "The cat sat on the mat"
```

- A. `s.replaceString('cat', 'dog')`

- B. `s.replace('cat', 'dog')`

- C. `s.stringReplace('cat', 'dog')`

- D. `s.replaceAll('cat', 'dog')`

**תשובה נכונה: B**

**הסבר:**

*   **מתודת `replace()`:** מתודת `replace()` בפייתון משמשת להחלפת תת-מחרוזת אחת במחרוזת בתת-מחרוזת אחרת. התחביר שלה: `מחרוזת.replace(מחרוזת_ישנה, מחרוזת_חדשה)`.

*   **מתודות שגויות:** המתודות `replaceString()`, `stringReplace()`, ו-`replaceAll()` אינן מתודות סטנדרטיות למחרוזות בפייתון.

**דוגמה:**

```python
s: str = "The cat sat on the mat"

# מחליפים את 'cat' ב-'dog' באמצעות replace()
new_s: str = s.replace('cat', 'dog')
print(new_s)
# פלט: The dog sat on the mat

# ננסה להשתמש בתחביר שגוי
try:
    s.replaceString('cat', 'dog') # תגרום לשגיאת AttributeError: 'str' object has no attribute 'replaceString'
except AttributeError as e:
  print(f"שגיאה: {e}")
# פלט: שגיאה: 'str' object has no attribute 'replaceString'
```

**לסיכום:**

*   אפשרות **B** `s.replace('cat', 'dog')` משתמשת נכונה במתודת `replace()` כדי להחליף את תת-המחרוזת `'cat'` ב-`'dog'` במחרוזת `s`.

*   אפשרויות **A**, **C**, ו-**D** משתמשות במתודות שאינן קיימות, ובעת השימוש בהן תיגרם שגיאת `AttributeError`.

לפיכך, תשובה **B** היא הנכונה, שכן היא מדגימה את השימוש הנכון במתודת `replace()` ואת התחביר שלה.