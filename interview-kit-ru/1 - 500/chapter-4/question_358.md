### `question_358.md`

**שאלה 358.** כיצד ניתן לבדוק האם `"apple"` הוא מפתח במילון `fruit`?

- A.  `"apple" in fruit.keys()`
- B.  `"apple" in fruit`
- C.  `fruit.has_key("apple")`
- D.  גם A וגם B נכונים.

**תשובה נכונה: D**

**הסבר:**

בשפת Python קיימות מספר דרכים לבדוק האם מפתח קיים במילון:
*   שימוש באופרטור `in`.
*   שימוש במתודה `keys()`.
*   שימוש במתודה המיושנת `has_key()` (שאינה מומלצת לשימוש).

*   **אפשרות A** נכונה: `“apple" in fruit.keys()` בודקת האם `"apple"` הוא מפתח ברשימת המפתחות של המילון.

*   **אפשרות B** נכונה: `“apple" in fruit` היא דרך אידיומטית וישירה יותר לבדוק נוכחות של מפתח במילון.

*   **אפשרות C** אינה נכונה: `fruit.has_key("apple")` היא מתודה מיושנת, שאינה מומלצת לשימוש.

*   **אפשרות D** נכונה: גם `“apple" in fruit.keys()` וגם `“apple" in fruit` בודקות נכונה את נוכחות המפתח, ולכן אפשרות זו נכונה.

**דוגמאות:**

```python
fruit: dict[str, str] = {"apple": "red", "banana": "yellow", "orange": "orange"}

# בדיקה באמצעות "in fruit.keys()"
if "apple" in fruit.keys():
    print("apple - ключ в словаре") # פלט: apple - מפתח במילון
else:
    print("apple - не ключ в словаре")

# בדיקה באמצעות "in fruit" (דרך אידיומטית יותר)
if "apple" in fruit:
    print("apple - ключ в словаре") # פלט: apple - מפתח במילון
else:
    print("apple - не ключ в словаре")

# בדיקה באמצעות המתודה המיושנת
try:
    if fruit.has_key("apple"):
        print("apple - ключ в словаре")
    else:
        print("apple - не ключ в словаре")
except AttributeError:
   print("Метод has_key не поддерживается")
```

**לסיכום:**

*   שימוש ב-`in fruit.keys()` וב-`in fruit` בודק נכונה את נוכחות המפתח.
*   המתודה `has_key()` מיושנת ועלולה לגרום ל-`AttributeError` בגרסאות חדשות של Python.

לפיכך, **אפשרות D** נכונה, מכיוון שאפשרויות A ו-B נכונות.