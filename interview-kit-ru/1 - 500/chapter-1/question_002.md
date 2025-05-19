### `question_002.md`

**שאלה 2.** ב-Python, לולאת `for` גמישה מאוד לאיטרציה על אובייקטים איטרביליים שונים. נשקול מצב שבו יש לכם מילון עם מפתחות מסוג מחרוזת וערכים מסוג מספר שלם. איזו מבין האפשרויות הבאות מבצעת איטרציה נכונה הן על המפתחות והן על הערכים של מילון זה?

- A.  `for key, value in dictionary.items(): print(key, value)`

- B.  `for key in dictionary: print(key, dictionary[key])`

- C.  `for value in dictionary.values(): print(value)`

- D.  `for key in dictionary.keys(): print(key)`

**תשובה נכונה: A**

**הסבר:**

*   **המתודה `items()`:** מתודת המילון `items()` מחזירה *אובייקט תצוגה* (view object), שמציג רשימה של זוגות "מפתח-ערך" בצורת טאפלים (tuples). זה מאפשר איטרציה בו זמנית על המפתחות והערכים בלולאת `for`.

*   **המתודה `keys()`:** המתודה `keys()` מחזירה *אובייקט תצוגה* (view object), המכיל רק את המפתחות של המילון.

*   **המתודה `values()`:** המתודה `values()` מחזירה *אובייקט תצוגה* (view object), המכיל רק את הערכים של המילון.

**דוגמה:**

```python
my_dictionary: dict[str, int] = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

# איטרציה נכונה על מפתחות וערכים:
print("איטרציה דרך items():")
for key, value in my_dictionary.items():
    print(f"מפתח: {key}, ערך: {value}")
# פלט:
# איטרציה דרך items():
# מפתח: apple, ערך: 1
# מפתח: banana, ערך: 2
# מפתח: cherry, ערך: 3

# איטרציה על המפתחות באמצעות dictionary[key]:
print("\nאיטרציה על המפתחות באמצעות dictionary[key]:")
for key in my_dictionary:
    print(f"מפתח: {key}, ערך: {my_dictionary[key]}")
# פלט:
# איטרציה על המפתחות באמצעות dictionary[key]:
# מפתח: apple, ערך: 1
# מפתח: banana, ערך: 2
# מפתח: cherry, ערך: 3

# איטרציה רק על הערכים:
print("\nאיטרציה רק על הערכים:")
for value in my_dictionary.values():
    print(f"ערך: {value}")
# פלט:
# איטרציה רק על הערכים:
# ערך: 1
# ערך: 2
# ערך: 3

# איטרציה רק על המפתחות:
print("\nאיטרציה רק על המפתחות:")
for key in my_dictionary.keys():
    print(f"מפתח: {key}")
# פלט:
# איטרציה רק על המפתחות:
# מפתח: apple
# מפתח: banana
# מפתח: cherry
```

**לסיכום:**

*   אפשרות **A** `for key, value in dictionary.items(): print(key, value)` מבצעת איטרציה נכונה על זוגות "מפתח-ערך" של המילון, באמצעות המתודה `items()`.

*   אפשרות **B** `for key in dictionary: print(key, dictionary[key])` עובדת, אך משתמשת בגישה ישירה לערך דרך המפתח במילון, במקום לבצע איטרציה על טאפלים (key, value).

*   אפשרויות **C** ו-**D** מבצעות איטרציה רק על הערכים או רק על המפתחות.

לפיכך, תשובה **A** היא הנכונה, מכיוון שהיא מאפשרת גישה בו זמנית הן למפתחות והן לערכים בלולאת `for`.