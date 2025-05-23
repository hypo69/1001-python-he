### `question_586.md`

**שאלה 586.** מהו התפקיד של מילת המפתח `self` בפייתון?

-   A. `self` היא מילת מפתח המשמשת לציון משתנים גלובליים בפייתון.
-   B. `self` היא מילת מפתח המשמשת להגדרת משתנים סטטיים במחלקות פייתון.
-   C. `self` היא מילת מפתח המשמשת להתייחסות למופע (אובייקט) של המחלקה, ומשמשת כפרמטר הראשון בעת הגדרת מתודות של המחלקה.
-   D. `self` היא מילת מפתח המשמשת להגדרת המחלקה אליה משתייכת מתודה נתונה זו.

**תשובה נכונה: C**

**הסבר:**

בפייתון, `self` היא מילת מפתח המשמשת כפרמטר הראשון בעת הגדרת מתודות בתוך מחלקה. היא מהווה הפניה למופע (אובייקט) של המחלקה שעבורו נקראת המתודה, ומאפשרת לגשת למאפייניו ולמתודותיו.

*   **תפקידים עיקריים של `self`:**
    *   **הפניה למופע:** `self` מפנה לאובייקט (המופע) של המחלקה שעבורו נקראה המתודה.
    *   **גישה למאפיינים:** `self` משמשת לגישה למאפייני המופע, כגון משתני מופע שהוגדרו בבנאי (`__init__`).
    *   **גישה למתודות:** `self` משמשת לקריאה למתודות אחרות של המופע מתוך המתודה הנוכחית.
    *   **הבחנה:** מסייעת להבחין בין מאפיינים ומתודות של המחלקה לבין משתנים מקומיים שהוגדרו במתודה.
    *   **פרמטר ראשון:** `self` הוא הפרמטר הראשון של מתודות המחלקה (אך לא של מתודות סטטיות), ופייתון מעבירה באופן אוטומטי את מופע המחלקה כפרמטר זה בעת קריאה למתודה.
*   **שימוש ב-`self` ב-`__init__`:**
    *   במתודה `__init__` (הבנאי), `self` מפנה למופע *שנוצר זה עתה* של המחלקה.
    *   `self` משמשת לאתחול מאפייני המופע.
*   **שימוש ב-`self` במתודות אחרות:**
    *   במתודות אחרות, `self` מפנה למופע *שכבר נוצר* של המחלקה, שהמתודה שלו נקראה.
    *   `self` משמשת לגישה ו/או שינוי מאפייני המופע ולקריאה למתודות אחרות.

**דוגמאות:**

```python
class MyClass:
    def __init__(self, x, y):
        self.x = x # self.x is an instance variable
        self.y = y

    def my_method(self):
        print(f"x: {self.x}, y: {self.y}") #  accessing attributes using self
        self.another_method()

    def another_method(self):
         print("Another method called") # accessing other methods via self
obj = MyClass(10, 20)
obj.my_method()
# x: 10, y: 20
# Another method called

#  Removing self from my_method will cause the code to fail
class MyClass2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def my_method(): # self was removed
        print(f"x: {self.x}, y: {self.y}")
        # self.another_method()

obj2 = MyClass2(10, 20)
try:
    obj2.my_method() # Will raise an exception
except Exception as e:
    print(e) # my_method() takes 0 positional arguments but 1 was given

```

**ניתוח האפשרויות:**
*   **A. `self` היא מילת מפתח המשמשת לציון משתנים גלובליים בפייתון.:** לא נכון.
*   **B. `self` היא מילת מפתח המשמשת להגדרת משתנים סטטיים במחלקות פייתון.:** לא נכון.
*   **C. `self` היא מילת מפתח המשמשת להתייחסות למופע (אובייקט) של המחלקה, ומשמשת כפרמטר הראשון בעת הגדרת מתודות של המחלקה.:** נכון.
*   **D. `self` היא מילת מפתח המשמשת להגדרת המחלקה אליה משתייכת מתודה נתונה זו.:** לא נכון.

**לסיכום:**
*   `self` מאפשרת למתודות המחלקה לקיים אינטראקציה עם מופע ספציפי של המחלקה.
*   `self` מאפשרת לגשת למאפיינים ולמתודות של המופע מתוך המחלקה.
*   `self` היא הפרמטר הראשון של כל מתודת מחלקה שאינה סטטית.

לפיכך, התשובה הנכונה היא **C. `self` היא מילת מפתח המשמשת להתייחסות למופע (אובייקט) של המחלקה, ומשמשת כפרמטר הראשון בעת הגדרת מתודות של המחלקה.**