### `question_672.md`

**שאלה 672.** מהו Method Resolution Order (MRO) בפייתון ומה מטרתו?

-   א. Method Resolution Order (MRO) הוא הסדר שבו מתבצעות קריאות למתודות בקריאות רקורסיביות של פונקציות.
-   ב. Method Resolution Order (MRO) הוא הסדר שבו מתודות מוכרזות במחלקה, ובעת קריאה נעשה שימוש בסדר ההכרזה.
-   ג. Method Resolution Order (MRO) הוא הסדר שבו פייתון מחפש מתודות בעת ירושה מרובה, והוא קובע כיצד המפרש מיישב קריאות למתודות בירושה.
-   ד. Method Resolution Order (MRO) הוא הסדר שבו משתנים מוכרזים בתוך מחלקה.

**תשובה נכונה: C**

**הסבר:**

Method Resolution Order (MRO) בפייתון הוא הסדר שבו מפרש השפה מחפש מתודות בעת ירושה מרובה (כאשר מחלקה יורשת ממספר מחלקות אב). MRO קובע כיצד פייתון מיישב קריאות למתודות, במיוחד אם במחלקות האב מופיעות מתודות בעלות שמות זהים.

*   **מטרות עיקריות של MRO:**
    *   **פתרון קונפליקטים:** מבטיח סדר נכון של חיפוש מתודות בהיררכיית המחלקות, וכאשר למחלקות שונות יש מתודות בעלות שם זהה.
    *   **התנהגות צפויה:** מבטיח סדר צפוי של קריאות למתודות, מה שהופך את הקוד לאמין יותר.
    *   **ניהול ירושה מרובה:** מאפשר שימוש יעיל בירושה מרובה.

*   **ליניאריזציית C3:**
    *   **אלגוריתם:** פייתון משתמש באלגוריתם ליניאריזציית C3, שהוא הנפוץ ביותר ובשימוש כברירת מחדל.
    *   **הבטחות:** C3 מבטיח שבעת מעקב אחר ה-MRO יישמרו כל הסדרים המקוריים, תוך שמירה על הסדר הלוקלי שלהם.
    *   **הגדרה:** אלגוריתם C3 בונה את ה-MRO תוך שמירה על כל כללי הירושה ופסילת עמימות אפשרית.

*   **כיצד פועל MRO:**
    *   כאשר מתודה נקראת מאובייקט, פייתון בודק את היררכיית המחלקות (היורשות ממחלקות הבסיס) בסדר ה-MRO, עד שהוא מוצא מתודה התואמת את הבקשה.

**דוגמאות:**

```python
# דוגמה 1: היררכיית ירושה פשוטה (ירושה יחידה)
class A:
    def method(self):
        print("Method of A")

class B(A):
    def method(self):
        print("Method of B")

b = B()
b.method()  # ידפיס: Method of B (נקראת המתודה ממחלקת הבן)

# דוגמה 2: ירושה מרובה (בעיית היהלום)

class A2:
    def method2(self):
        print("Method of A")

class B2(A2):
    def method2(self):
        print("Method of B")
class C2(A2):
    pass
class D2(B2, C2): # ירושה מרובה
    pass

d = D2()
d.method2() #  Method of B (בזכות ה-MRO, המתודה ממחלקה B נמצאת מוקדם יותר)

print(D2.__mro__)

# דוגמה 3: שימוש ב-super() לקריאה למתודות אב
class Base:
    def hello(self):
       print("Hello from Base")
class Mixin(Base):
    def hello(self):
      super().hello() # קריאה למתודת האב
      print("Hello from Mixin")

class MyClass(Mixin):
   def hello(self):
      super().hello()
      print("Hello from MyClass")

MyClass().hello()
# ידפיס:
# Hello from Base
# Hello from Mixin
# Hello from MyClass
```

**ניתוח האפשרויות:**

*   **א. Method Resolution Order (MRO) הוא הסדר שבו מתבצעות קריאות למתודות בקריאות רקורסיביות של פונקציות.:** שגוי.
*   **ב. Method Resolution Order (MRO) הוא הסדר שבו מתודות מוכרזות במחלקה, ובעת קריאה נעשה שימוש בסדר ההכרזה.:** שגוי.
*   **ג. Method Resolution Order (MRO) הוא הסדר שבו פייתון מחפש מתודות בעת ירושה מרובה, והוא קובע כיצד המפרש מיישב קריאות למתודות בירושה.:** נכון.
*   **ד. Method Resolution Order (MRO) הוא הסדר שבו משתנים מוכרזים בתוך מחלקה.:** שגוי.

**לסיכום:**
*   MRO מבטיח חיפוש צפוי ומובן של מתודות.
*   MRO חשוב להבנת עקרונות הפעולה של ירושה מרובה.
*   פייתון משתמש כברירת מחדל באלגוריתם ליניאריזציית C3.

לפיכך, התשובה הנכונה היא **ג. Method Resolution Order (MRO) הוא הסדר שבו פייתון מחפש מתודות בעת ירושה מרובה, והוא קובע כיצד המפרש מיישב קריאות למתודות בירושה.**