### `question_141.md`

**פרק 1. שאלה 141.** כיצד ניתן לבדוק האם `"apple"` הוא מפתח במילון `fruit`?

- א. `"apple" in fruit.keys()`
- ב. `"apple" in fruit`
- ג. `fruit.has_key("apple")`
- ד. גם א' וגם ב' נכונות.

**תשובה נכונה: ד**

**הסבר:**

בשפת Python קיימות מספר דרכים לבדוק האם מפתח קיים במילון:
* באמצעות האופרטור `in`.
* באמצעות המתודה `keys()`.
* באמצעות המתודה המיושנת `has_key()` (אינה מומלצת לשימוש).

*   **אפשרות א'** נכונה: `"apple" in fruit.keys()` בודקת האם `"apple"` הוא מפתח ברשימת המפתחות של המילון.

*   **אפשרות ב'** נכונה: `"apple" in fruit` היא דרך מומלצת וישירה יותר לבדוק קיום מפתח במילון.

*   **אפשרות ג'** אינה נכונה: `fruit.has_key("apple")` היא מתודה מיושנת שאינה מומלצת לשימוש.

*   **אפשרות ד'** נכונה: גם `"apple" in fruit.keys()` וגם `"apple" in fruit` בודקות קיום מפתח באופן תקין, ולכן אפשרות זו נכונה.

**דוגמאות:**

```python
fruit: dict[str, str] = {"apple": "red", "banana": "yellow", "orange": "orange"}

# בדיקה באמצעות "in fruit.keys()"
if "apple" in fruit.keys():
    print("apple - מפתח במילון") # פלט: apple - מפתח במילון
else:
    print("apple - אינו מפתח במילון")

# בדיקה באמצעות "in fruit" (דרך מומלצת יותר)
if "apple" in fruit:
    print("apple - מפתח במילון") # פלט: apple - מפתח במילון
else:
    print("apple - אינו מפתח במילון")

# בדיקה באמצעות מתודה מיושנת
try:
    if fruit.has_key("apple"):
        print("apple - מפתח במילון")
    else:
        print("apple - אינו מפתח במילון")
except AttributeError:
   print("המתודה has_key אינה נתמכת")
```

**לסיכום:**

*   השימוש ב-`in fruit.keys()` וב-`in fruit` שניהם בודקים את קיום המפתח באופן נכון.
* המתודה `has_key()` מיושנת ועלולה לגרום לשגיאת `AttributeError` בגרסאות Python חדשות.

לפיכך, **אפשרות ד'** היא הנכונה, מאחר שאפשרויות א' וב' שתיהן נכונות.