### `question_004.md`

**שאלה 4.** Python תומכת במספר טיפוסי נתונים, ומחרוזות הן אחד מטיפוסי הנתונים הנפוצים ביותר בשימוש. איזו מבין הדרכים הבאות נכונה לשרשור שלוש מחרוזות ב-Python, תוך הבטחה שהתוצאה תהיה מחרוזת אחת ללא רווחים נוספים ביניהן?

- A. `"Python" + "is" + "awesome"`

- B. `"Python", "is", "awesome"`

- C. `"Python" + " " + "is" + " " + "awesome"`

- D. `"Python".join(["is", "awesome"])`

**תשובה נכונה: A**

**הסבר:**

*   **האופרטור `+`:** ב-Python, האופרטור `+` משמש לשרשור מחרוזות. כאשר משתמשים ב-`+` בין מחרוזות, הן פשוט מתאחדות למחרוזת אחת ללא הוספת תווים נוספים, אלא אם כן הם נוספים במפורש.
*   **פסיק `,`:** אם מחרוזות מופרדות בפסיקים, כמו באפשרות B, הדבר ייצור טאפל של מחרוזות, ולא מחרוזת משורשרת.
*   **הוספת רווחים:** באפשרות C, רווחים נוספים במפורש במהלך השרשור, מה שגורם להכללת רווחים בין המילים.
*   **המתודה `join()`:** המתודה `join()` משמשת לאיחוד אלמנטים של אובייקט איטרבילי (כמו רשימה) למחרוזת אחת, תוך שימוש במחרוזת שהמתודה הופעלה עליה כמפריד.

**דוגמה:**

```python
string1: str = "Python"
string2: str = "is"
string3: str = "awesome"

# שרשור נכון
concatenated_string_a: str = string1 + string2 + string3
print(f"A: {concatenated_string_a}")  # פלט: A: Pythonisawesome

# שרשור לא נכון עם טאפל
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

*   אפשרות **A** `"Python" + "is" + "awesome"` מובילה לשרשור נכון של המחרוזות ללא הוספת רווחים ביניהן.

*   אפשרות **B** `"Python", "is", "awesome"` יוצרת טאפל, ולא מחרוזת.

*   אפשרות **C** `"Python" + " " + "is" + " " + "awesome"` מוסיפה רווחים בין המחרוזות, מה שאינו תואם את דרישת השאלה.

*   אפשרות **D** `"Python".join(["is", "awesome"])` משתמשת ב-`join`, אך בדוגמה זו היא תוסיף רווח בין `is` ל-`awesome`, ובנוסף יהיה צורך להוסיף את המחרוזת "Python" בהתחלה.

לפיכך, תשובה **A** היא הנכונה, מכיוון שהיא משַרשרת את המחרוזות במדויק לאחת ללא רווחים נוספים.