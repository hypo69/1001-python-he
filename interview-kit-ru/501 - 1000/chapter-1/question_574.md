### `question_572.md`

**שאלה 572.** מהו תבנית העיצוב הפונקציונלית "Functor" (פונקטור), וכיצד היא משמשת ב-Python? הצג דוגמה לשימוש בפונקטור ליישום פונקציה על ערך בתוך הקשר.

-   A. Functor היא פונקציה לביצוע חישובים בלולאה.
-   B. Functor היא דרך לארגן קוד כאשר הנתונים משתנים, אך הפונקציות לא.
-   C. Functor הוא הקשר התומך בפעולת `map` ליישום פונקציה על ערכו הפנימי.
-   D. Functor הוא תחביר מיוחד לתיאור מחלקות ב-Python.

**תשובה נכונה: C**

**הסבר:**

בתכנות פונקציונלי, פונקטור (Functor) הוא הקשר התומך בפעולת `map`. הוא מאפשר ליישם פונקציה על ערך הנמצא "בתוך" הקשר זה, מבלי לשנות את ההקשר עצמו. פונקטורים מאפשרים להפשט מסוג הנתונים וממבנה הנתונים, ומספקים דרך אוניברסלית ליישם פונקציות.

*   **מושגי יסוד של פונקטור:**
    *   **הקשר:** מייצג מכל או עטיפה המכילה ערך.
    *   **פעולת `map`:** מתודה (או פונקציה) המאפשרת ליישם פונקציה על הערך הכלול בתוך ההקשר.
    *   **שימור ההקשר:** תוצאת פעולת `map` נשארת באותו הקשר כמו הערך המקורי.
    *   **הפשטה:** מאפשרת לטפל בערכים בתוך סוגי הקשרים שונים בצורה אחידה.

*   **מימוש ב-Python:**
    *   ב-Python ניתן לממש פונקטורים באמצעות מחלקות המגדירות מתודה שניתן לכנותה `map`.
    *   ניתן לממש זאת כמתודת מופע של מחלקה או כפונקציה המקבלת אובייקט מחלקה כארגומנט.

**דוגמאות:**

```python
# דוגמה למימוש Functor באמצעות מחלקה
class Maybe:
    def __init__(self, value):
        self.value = value

    def map(self, func):
        if self.value is None:
            return Maybe(None)
        return Maybe(func(self.value))

#שימוש ב-Maybe כ-Functor

maybe_number = Maybe(5)
squared = maybe_number.map(lambda x: x**2)
print(squared.value) # פלט: 25

nothing = Maybe(None)
squared_nothing = nothing.map(lambda x: x**2)
print(squared_nothing.value) # פלט: None

# דוגמה ל-Functor באמצעות רשימה
class ListFunctor:
    def __init__(self, value):
        self.value = value
    def map(self, func):
         return ListFunctor([func(x) for x in self.value])

list_functor = ListFunctor([1, 2, 3])
mapped_list = list_functor.map(lambda x: x*2)

print(mapped_list.value) # פלט: [2, 4, 6]

def  map_functor(func, obj):
  if  hasattr(obj, "map"):
    return obj.map(func)
  elif isinstance(obj, list):
    return [func(item) for item in obj]
  else:
      return None

# קריאה לפונקציה map_functor עבור רשימה ועבור אובייקט Maybe
list_functor = [1,2,3]
print(map_functor(lambda x:x*2, list_functor)) # פלט: [2, 4, 6]
maybe_num = Maybe(5)
print(map_functor(lambda x:x*2, maybe_num).value) # פלט: 10
```

**ניתוח הדוגמאות:**

1.  **`class Maybe`:** מממשת פונקטור היכול לאחסן ערך או כלום (`None`).
    *   `__init__(self, value)`: מקבלת ערך התחלתי.
    *   `map(self, func)`: מיישמת את הפונקציה `func` על הערך השמור, אם הוא קיים.
2.  **שימוש ב-Maybe כ-Functor:**
    *   `maybe_number` נוצר עם המספר 5.
    *   `maybe_number.map(lambda x: x**2)` מיישם את הפונקציה `x ** 2` על הערך 5.
    *   `nothing` נוצר עם הערך `None`.
    *   `nothing.map(lambda x: x**2)` מחזיר `Maybe(None)`, מכיוון שהערך שווה ל-`None`.
3.  **`class ListFunctor`**: מממשת פונקטור עבור רשימות.
    *   `__init__`: בנאי.
    *   `map(self, func)`: מיישמת את הפונקציה `func` על כל איבר ברשימה, ומחזירה `ListFunctor` חדש עם הרשימה החדשה.
4.  **`map_functor`**:
    *   בודקת אם קיימת מתודת `map` באובייקט, וקוראת לה.
    *   אם האובייקט הוא רשימה, מיישמת `map` על כל איבר.
    *   אחרת - מחזירה `None`.
5.  מיישמת את `map_functor` עבור רשימה ועבור אובייקט Maybe.

**ניתוח האפשרויות:**
*   **A. Functor היא פונקציה לביצוע חישובים בלולאה.:** לא נכון. פונקטור הוא מושג, לא רק פונקציה, ואינו קשור בהכרח ללולאות.
*   **B. Functor היא דרך לארגן קוד כאשר הנתונים משתנים, אך הפונקציות לא.:** לא נכון. זהו תיאור של אי-שונוּת (Immutability), לא של פונקטור.
*   **C. Functor הוא הקשר התומך בפעולת `map` ליישום פונקציה על ערכו הפנימי.:** נכון.
*   **D. Functor הוא תחביר מיוחד לתיאור מחלקות ב-Python.:** לא נכון.

**לסיכום:**
*   פונקטורים מאפשרים ליישם פעולות על ערכים בתוך הקשר, מבלי לדאוג למבנה ההקשר.
*   `map` היא הפעולה המרכזית של פונקטור, המאפשרת להפוך ערכים בתוך מכל.
*   פונקטורים מאפשרים לכתוב קוד גמיש יותר ועם יכולת שימוש חוזר.

לפיכך, התשובה הנכונה היא **C. Functor הוא הקשר התומך בפעולת `map` ליישום פונקציה על ערכו הפנימי.**