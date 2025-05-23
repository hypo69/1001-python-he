### `question_803.md`

**שאלה 803.** מהי "הפשטה" בתכנות מונחה עצמים (OOP)?

A. זו היכולת ליצור מחלקות חדשות על בסיס מחלקות קיימות.
B. זו היכולת של אובייקטים ממחלקות שונות להתנהג באופן אחיד באמצעות ממשק משותף.
C. זהו עיקרון המאפשר להסתיר את פרטי המימוש של אובייקט ולספק גישה אליו דרך ממשק ציבורי.
D. זהו מנגנון לטיפול בשגיאות וחריגים.

**תשובה נכונה: C**

**הסבר:**

בתכנות מונחה עצמים (OOP), הפשטה היא עיקרון של הסתרת המימוש הפנימי המורכב של אובייקט ומתן ממשק פשוט ומובן לעבודה איתו. הפשטה מאפשרת לעבוד עם אובייקט מבלי לדעת את פרטי המבנה הפנימי שלו.

*   **אפשרות A** אינה נכונה: זו ההגדרה של ירושה.
*   **אפשרות B** אינה נכונה: זו ההגדרה של פולימורפיזם.
*   **אפשרות C** נכונה: הפשטה היא הסתרת המימוש הפנימי ומתן גישה אליו דרך ממשק ציבורי.
*   **אפשרות D** אינה נכונה: זו ההגדרה לבלוקי try-except.

**כיצד פועלת הפשטה:**

1.  הפשטה מאפשרת להסתיר את פרטי המימוש המורכבים של אובייקט, ולהשאיר רק את הממשק הדרוש לאינטראקציה.
2.  היא מאפשרת למפתחים לעבוד עם האובייקט ברמה גבוהה יותר, מבלי להיכנס לפרטים.
3.  היא תורמת למודולריות ומפשטת את התחזוקה והשינויים בקוד.
4. בפייתון, הפשטה יכולה להיות ממומשת באמצעות מחלקות מופשטות (abstract classes) או ממשקים (interfaces).

**דוגמה:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
       """שיטה מופשטת"""
       pass
class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> float: # מממשים את שיטת המחלקה Shape
        """חישוב שטח מעגל."""
        return 3.14 * self.radius**2

class Square(Shape):
  def __init__(self, side: int):
    self.side = side

  def area(self) -> float: # מממשים את שיטת המחלקה Shape
    """חישוב שטח ריבוע"""
    return self.side**2

circle: Circle = Circle(5)
square: Square = Square(10)

def display_area(shape: Shape):
   print(f"שטח: {shape.area()}") # קריאה פולימורפית לשיטה area()

display_area(circle) # פלט: שטח: 78.5
display_area(square) # פלט: שטח: 100
```
**תוצאה:**

*   אנו יכולים לעבוד עם circle ו-square, תוך שימוש בממשק המשותף shape (השיטה area), מבלי לדעת את פרטי המימוש שלהם.

לסיכום, **אפשרות C** היא התשובה הנכונה.