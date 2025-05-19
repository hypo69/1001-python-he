**מהו `dataclass`?**

`dataclass` הוא דקורטור שהוצג ב-Python 3.7, אשר יוצר אוטומטית מתודות מיוחדות (כגון `__init__`, `__repr__`, `__eq__` ואחרות) עבור מחלקות המשמשות בעיקר כמכליות (containers) לנתונים. זה חוסך את הצורך לכתוב קוד "шаблонный" (boilerplate code) רב.

**למה להשתמש ב-`dataclass`?**

1.  **קיצור קוד:** במקום להגדיר ידנית את המתודות `__init__`, `__repr__`, `__eq__` וכו', אתה פשוט מצהיר על שדות הנתונים, ו-`dataclass` עושה את כל השאר.
2.  **שיפור קריאות:** מחלקות הופכות לתמציתיות וברורות יותר, מכיוון שהן מתמקדות בנתונים ולא ביישום טכני.
3.  **צמצום שגיאות:** קוד שנוצר אוטומטית אמין לרוב יותר מקוד שנכתב ידנית.
4.  **האצת פיתוח:** אתה יכול ליצור מחלקות לעבודה עם נתונים מהר יותר, מבלי לבזבז זמן על משימות שגרתיות.

**כיצד להשתמש ב-`dataclass`?**

ראשית, עליך לייבא את הדקורטור `dataclass` מהמודול `dataclasses`:

```python
from dataclasses import dataclass
```

לאחר מכן, אתה מסמן את המחלקה בדקורטור `@dataclass`, ומגדיר את שדות הנתונים כמשתנים רגילים של המחלקה עם אנולציות טיפוסים:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

בדוגמה זו, `Point` הוא `dataclass` שיש לו שני שדות: `x` ו-`y`, שניהם מטיפוס שלם. `dataclass` ייצור אוטומטית:
*   קונסטרוקטור `__init__`, המאפשר ליצור מופעים של המחלקה, למשל `Point(1, 2)`.
*   `__repr__`, המחזיר ייצוג מחרוזתי של האובייקט, למשל `Point(x=1, y=2)`.
*   `__eq__`, המאפשר להשוות אובייקטים, למשל `Point(1, 2) == Point(1, 2)`.

**דוגמה לשימוש פשוט**
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# יצירת מופע של המחלקה
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

# הדפסה למסך
print(point1) # פלט: Point(x=1, y=2)
print(point1 == point2) # פלט: True
print(point1 == point3) # פלט: False
```

**אפשרויות ב-`dataclass`**

`dataclass` מספק מספר פרמטרים להתאמת ההתנהגות:

*   `init`: אם `True` (ברירת מחדל), נוצרת מתודת `__init__`. אם `False`, מתודת `__init__` אינה נוצרת.
*   `repr`: אם `True` (ברירת מחדל), נוצרת מתודת `__repr__`. אם `False`, מתודת `__repr__` אינה נוצרת.
*   `eq`: אם `True` (ברירת מחדל), נוצרת מתודת `__eq__`. אם `False`, מתודת `__eq__` אינה נוצרת.
*   `order`: אם `True`, נוצרות מתודות השוואה (`__lt__`, `__le__`, `__gt__`, `__ge__`). ברירת המחדל היא `False`.
*   `unsafe_hash`: אם `False` (ברירת מחדל), מתודת `__hash__` אינה נוצרת. אם `True`, מתודת `__hash__` תיצור, ו-`dataclass` יהפוך לניתן ל-hash (hashable).
*   `frozen`: אם `True`, מופעי המחלקה יהיו בלתי ניתנים לשינוי (read-only). ברירת המחדל היא `False`.

**דוגמאות לשימוש באפשרויות**
1. ביטול מתודת `__repr__` והפיכת המחלקה לבלתי ניתנת לשינוי
```python
from dataclasses import dataclass

@dataclass(repr=False, frozen=True)
class Point:
    x: int
    y: int

# יצירת מופע של המחלקה
point1 = Point(1, 2)
# הדפסה למסך
print(point1) # פלט: <__main__.Point object at 0x000001D8322F6770> (מאחר ש-`__repr__` אינה מוגדרת)

# שינוי המופע יגרום לשגיאה
try:
    point1.x = 10
except Exception as e:
    print (e) # פלט: cannot assign to field 'x'
```
2. הגדרת סדר, הוספת מתודת hash והפיכת המחלקה לבלתי ניתנת לשינוי
```python
from dataclasses import dataclass

@dataclass(order=True, unsafe_hash=True, frozen=True)
class Point:
    x: int
    y: int

# יצירת מופע של המחלקה
point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = Point(1, 2)
# הדפסה למסך
print(point1 < point2) # פלט: True
print(point1 == point3) # פלט: True

# כעת ניתן להשתמש במחלקה כמפתח במילון
my_dict = {point1: "first", point2: "second"}
print(my_dict) # פלט: {Point(x=1, y=2): 'first', Point(x=3, y=4): 'second'}
```

**ערכי ברירת מחדל**

ניתן להגדיר ערכי ברירת מחדל עבור שדות:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int = 0
    y: int = 0

# יצירת מופע של המחלקה
point1 = Point()
point2 = Point(1, 2)

# הדפסה למסך
print(point1) # פלט: Point(x=0, y=0)
print(point2) # פלט: Point(x=1, y=2)
```
בעת יצירת מופע של המחלקה, אם לא מועברים ערכים, ייעשה שימוש בערך ברירת המחדל.

**שימוש ב-`dataclass` עם טיפוסים משתנים**

יש להיזהר בעת שימוש בטיפוסי נתונים משתנים (רשימות, מילונים) כערכי ברירת מחדל. הם ייווצרו רק פעם אחת וישמשו את כל מופעי המחלקה:

```python
from dataclasses import dataclass
from typing import List

@dataclass
class BadExample:
    items: List[int] = []

bad1 = BadExample()
bad2 = BadExample()

bad1.items.append(1)
print (bad1.items) # פלט: [1]
print (bad2.items) # פלט: [1]
```
בדוגמה לעיל, שינויים ב-`bad1.items` משתקפים גם ב-`bad2.items`. זה קורה מכיוון ששני מופעי המחלקה משתמשים באותה רשימה של ברירת מחדל.

כדי להימנע מכך, השתמש ב-`dataclasses.field` וב-`default_factory`:
```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class GoodExample:
    items: List[int] = field(default_factory=list)

good1 = GoodExample()
good2 = GoodExample()

good1.items.append(1)
print (good1.items) # פלט: [1]
print (good2.items) # פלט: []
```
במקרה זה, `default_factory=list` ייצור רשימה ריקה חדשה עבור כל מופע חדש של המחלקה.

**דיאגרמה**

להלן דיאגרמה המציגה את המושגים העיקריים של `dataclass`:

```mermaid
classDiagram
    class DataClass {
        <<decorator>>
        +init: bool = True
        +repr: bool = True
        +eq: bool = True
        +order: bool = False
        +unsafe_hash: bool = False
        +frozen: bool = False
        --
        +__init__(...)
        +__repr__()
        +__eq__(...)
        +__lt__(...)
        +__le__(...)
        +__gt__(...)
        +__ge__(...)
        +__hash__()
    }
    class UserDefinedClass {
        <<class>>
        +field1: type
        +field2: type
        +field3: type = defaultValue
        +field4: type = field(default_factory=...)
    }
    DataClass <|-- UserDefinedClass
```

בדיאגרמה זו:
*   `DataClass` מייצג את הדקורטור `@dataclass` ואת פרמטריו.
*   `UserDefinedClass` היא המחלקה שאתה מצהיר עליה, תוך שימוש בדקורטור `@dataclass`.
*   החץ מ-`DataClass` ל-`UserDefinedClass` מראה ש-`DataClass` מיושם על `UserDefinedClass`.