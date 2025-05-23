### `question_135.md`

**שאלה 35.** מה יקרה אם התנאי בלולאת `while` תמיד מוערך כ־`True`?

A. הלולאה לעולם לא תבוצע.
B. הלולאה תבוצע פעם אחת בלבד.
C. תתרחש שגיאת זמן ריצה.
D. תיווצר לולאה אינסופית.

**התשובה הנכונה: D**

**הסבר:**

אם התנאי בלולאת `while` תמיד מוערך כ־`True`, הלולאה תמשיך להתבצע באופן אינסופי, אלא אם כן היא תיקטע על ידי האופרטור `break` או שתתרחש חריגה (exception).

*   **אפשרות A** שגויה: הלולאה תתבצע אם התנאי הוא `True`.
*   **אפשרות B** שגויה: הלולאה לא תיעצר לאחר האיטרציה הראשונה.
*   **אפשרות C** שגויה: לולאה אינסופית כשלעצמה אינה גורמת לשגיאה, אלא אם כן היא מובילה למיצוי משאבים.
*   **אפשרות D** נכונה: הלולאה תמשיך להתבצע באופן אינסופי עד שלא תיקטע.

**דוגמה:**

```python
x: int = 0

while True: # לולאה אינסופית
  x += 1
  print(x)
  if x > 5:
     break # קוטעים את הלולאה לאחר 5 איטרציות
```

**כתוצאה מכך:**

*   הלולאה תתבצע באופן אינסופי אם לא יהיה אופרטור `break`.
*   בדוגמה שלעיל, הלולאה תיקטע כאשר `x` יהיה גדול מ-5.

לפיכך, **אפשרות D** היא התשובה הנכונה.