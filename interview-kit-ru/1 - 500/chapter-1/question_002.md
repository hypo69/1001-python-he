### `question_002.md`

**שאלה 2.** בפייתון, לולאת `for` גמישה מאוד עבור איטרציה על אובייקטים הניתנים לאיטרציה מסוגים שונים. נתבונן במצב שבו יש ברשותך מילון עם מפתחות מסוג מחרוזת וערכים מסוג מספר שלם. איזו מבין האפשרויות הבאות מבצעת איטרציה נכונה הן על המפתחות והן על הערכים של מילון זה?

- A.  `for key, value in dictionary.items(): print(key, value)`

- B.  `for key in dictionary: print(key, dictionary[key])`

- C.  `for value in dictionary.values(): print(value)`

- D.  `for key in dictionary.keys(): print(key)`

**התשובה הנכונה: A**

**הסבר:**

*   **שיטת `items()`:** שיטת `items()` של מילון מחזירה *view object*, אשר מציג רשימה של זוגות מפתח-ערך בצורת טאפלים. זה מאפשר לבצע איטרציה בו-זמנית על המפתחות ועל הערכים בלולאת `for`.

*   **שיטת `keys()`:** שיטת `keys()` מחזירה *view object*, המכיל רק את מפתחות המילון.

*   **שיטת `values()`:** שיטת `values()` מחזירה *view object*, המכיל רק את ערכי המילון.

**דוגמה:**

```python
my_dictionary: dict[str, int] = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

# איטרציה נכונה על המפתחות והערכים:
print("איטרציה דרך items():")
for key, value in my_dictionary.items():
    print(f"מפתח: {key}, ערך: {value}")
# פלט:
# איטרציה דרך items():
# מפתח: apple, ערך: 1
# מפתח: banana, ערך: 2
# מפתח: cherry: 3

# איטרציה על מפתחות באמצעות dictionary[key]:
print("\nאיטרציה על מפתחות באמצעות dictionary[key]:")
for key in my_dictionary:
    print(f"מפתח: {key}, ערך: {my_dictionary[key]}")
# פלט:
# איטרציה על מפתחות באמצעות dictionary[key]:
# מפתח: apple, ערך: 1
# מפתח: banana, ערך: 2
# מפתח: cherry: 3

# איטרציה רק על ערכים:
print("\nאיטרציה רק על ערכים:")
for value in my_dictionary.values():
    print(f"ערך: {value}")
# פלט:
# איטרציה רק על ערכים:
# ערך: 1
# ערך: 2
# ערך: 3

# איטרציה רק על מפתחות:
print("\nאיטרציה רק על מפתחות:")
for key in my_dictionary.keys():
    print(f"מפתח: {key}")
# פלט:
# איטרציה רק על מפתחות:
# מפתח: apple
# מפתח: banana
# מפתח: cherry
```

**לסיכום:**

*   אפשרות **A** `for key, value in dictionary.items(): print(key, value)` מבצעת איטרציה נכונה על זוגות "מפתח-ערך" במילון, תוך שימוש בשיטת `items()`.

*   אפשרות **B** `for key in dictionary: print(key, dictionary[key])` עובדת, אך משתמשת בגישה ישירה לערך באמצעות המפתח במילון, ולא מבצעת איטרציה על טאפלים `(key, value)`.

*   אפשרויות **C** ו-**D** מבצעות איטרציה רק על הערכים, או רק על המפתחות.

לפיכך, התשובה **A** נכונה, מאחר שהיא מאפשרת לגשת בו-זמנית הן למפתחות והן לערכים בלולאת `for`.