### `question_004.md`

**שאלה 4.** Python תומכת במספר סוגי נתונים, ומחרוזות הן אחד מסוגי הנתונים הנפוצים ביותר. איזו מהדרכים הבאות נכונה לשרשור שלוש מחרוזות ב-Python, כך שהתוצאה תהיה מחרוזת אחת ללא רווחים נוספים ביניהן?

- A. `"Python" + "is" + "awesome"`

- B. `"Python", "is", "awesome"`

- C. `"Python" + " " + "is" + " " + "awesome"`

- D. `"Python".join(["is", "awesome"])`

**תשובה נכונה: A**

**הסבר:**

*   **אופרטור `+`:** ב-Python, אופרטור `+` משמש לשרשור מחרוזות. כאשר משתמשים ב-+ בין מחרוזות, הן פשוט מתאחדות למחרוזת אחת ללא הוספת תווים נוספים, אלא אם כן הם מוספים במפורש.
*   **פסיק `,`:** אם המחרוזות מופרדות בפסיקים, כפי שמוצג באפשרות B, נוצר טאפל של מחרוזות ולא מחרוזת משורשרת.
*   **הוספת רווחים:** באפשרות C, רווחים מוספים במפורש במהלך השרשור, מה שגורם להכללת רווחים בין המילים.
*   **מתודת `join()`:** מתודת `join()` משמשת לאיחוד אלמנטים של אובייקט איטרבילי (כמו רשימה) למחרוזת אחת, תוך שימוש במחרוזת שעליה המתודה מופעלת כמפריד.

**דוגמה:**

```python
string1: str = "Python"
string2: str = "is"
string3: str = "awesome"

# שרשור נכון
concatenated_string_a: str = string1 + string2 + string3
print(f"A: {concatenated_string_a}")  # פלט: A: Pythonisawesome

# שרשור שגוי עם טאפל
concatenated_string_b: tuple[str, str, str] = (string1, string2, string3)
print(f"B: {concatenated_string_b}")  # פלט: B: ('Python', 'is', 'awesome')

# שרשור עם רווחים
concatenated_string_c: str = string1 + " " + string2 + " " + string3
print(f"C: {concatenated_string_c}")  # פלט: C: Python is awesome

# שימוש ב-join
concatenated_string_d: str = " ".join([string2, string3])
print(f"D: {string1}{concatenated_string_d}")  # פלט: D: Pythonis awesome
```

**כתוצאה מכך:**

*   אפשרות **A** `"Python" + "is" + "awesome"` מביאה לשרשור נכון של המחרוזות למחרוזת אחת ללא הוספת רווחים ביניהן.

*   אפשרות **B** `"Python", "is", "awesome"` יוצרת טאפל, ולא מחרוזת.

*   אפשרות **C** `"Python" + " " + "is" + " " + "awesome"` מוסיפה רווחים בין המחרוזות, מה שאינו תואם את דרישת השאלה.

*   אפשרות **D** `"Python".join(["is", "awesome"])` משתמשת ב-`join`, אך בדוגמה זו היא תוסיף רווח בין `is` לבין `awesome`, ובנוסף יהיה צורך להוסיף את המחרוזת "Python" בתחילת התוצאה.

לפיכך, התשובה **A** היא הנכונה, מכיוון שהיא משרשרת במדויק את המחרוזות לאחת ללא רווחים נוספים.