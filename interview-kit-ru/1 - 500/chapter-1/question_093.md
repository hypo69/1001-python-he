### `question_93.md`

**שאלה 93.** איזה מהאפשרויות הבאות אינה מזהה Python קביל?

*   A. `_myvar`
*   B. `2myvar`
*   C. `my_var`
*   D. `myVar`

**תשובה נכונה: B**

**הסבר:**

מזהים (Identifiers) ב-Python הם השמות המשמשים לציון משתנים, פונקציות, מחלקות ואובייקטים אחרים. קיימים כללים מסוימים ליצירת מזהים קבילים.

*   **אפשרות A** נכונה: `_myvar` הוא מזהה קביל. הוא מתחיל בקו תחתון, ולאחר מכן אותיות.
*   **אפשרות B** אינה נכונה: `2myvar` הוא מזהה לא קביל. הוא מתחיל בספרה.
*   **אפשרות C** נכונה: `my_var` הוא מזהה קביל. הוא מתחיל באות ומכיל אותיות וקווים תחתונים.
*   **אפשרות D** נכונה: `myVar` הוא מזהה קביל. הוא מתחיל באות ויכול להכיל אותיות באותיות רישיות וקטנות.

**כללים למזהי Python:**

1.  **מתחיל באות או בקו תחתון:** מזהים חייבים להתחיל באות (a-z, A-Z) או בקו תחתון `_`.
2.  **מכיל אותיות, ספרות או קווים תחתונים:** לאחר הסימן הראשון, מזהים יכולים להכיל אותיות, ספרות (0-9) וקווים תחתונים.
3.  **רגישים לרישיות:** `myVar`, `MyVar`, ו-`MYVAR` יהיו מזהים שונים.
4.  **לא יכולים להיות מילות שמורות:** אסור להשתמש במילות שמורות של Python (לדוגמה: `if`, `else`, `for`, `while`, `def`, `class` וכו') כמזהים.

**דוגמה:**

```python
_myvar = 10 # מזהה קביל
print(_myvar) # פלט: 10

# 2myvar = 20 # SyntaxError: invalid syntax (תחביר לא חוקי)
my_var = "test" # מזהה קביל
print(my_var) # פלט: test

myVar = [1,2,3]
print(myVar) # פלט: [1, 2, 3]
```

**לסיכום:**

`_myvar`, `my_var`, ו-`myVar` הם מזהים קבילים, בעוד ש-`2myvar` גורם לשגיאת תחביר, מכיוון שהוא מתחיל בספרה.

לפיכך, **אפשרות B** היא הנכונה.