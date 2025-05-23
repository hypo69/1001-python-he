### `question_192.md`

**שאלה 192.** מהו "פולימורפיזם" בתכנות מונחה-עצמים?

א. היכולת ליצור מחלקות חדשות על בסיס מחלקות קיימות.
ב. היכולת ליצור מספר מופעים (אינסטנסים) של אותה מחלקה.
ג. היכולת לעבד אובייקטים ממחלקות שונות באמצעות ממשק משותף.
ד. היכולת להסתיר נתונים בתוך מחלקה.

**תשובה נכונה: ג**

**הסבר:**

פולימורפיזם (מיוונית: "צורות רבות") בתכנות מונחה-עצמים היא היכולת להשתמש באובייקטים ממחלקות שונות באמצעות ממשק משותף. במילים אחרות, אובייקטים ממחלקות שונות יכולים להגיב לאותה מתודה, אך באופן שונה, בהתאם לטבעם הספציפי.

*   **אפשרות א** אינה נכונה: הגדרה זו מתייחסת לירושה, לא לפולימורפיזם.
*   **אפשרות ב** אינה נכונה: זהו תיאור של יצירת מופעים, אך לא של פולימורפיזם.
*   **אפשרות ג** נכונה: פולימורפיזם כרוך בעיבוד אובייקטים ממחלקות שונות באמצעות ממשק משותף.
*   **אפשרות ד** אינה נכונה: הגדרה זו מתייחסת לאנקפסולציה (כימוס), לא לפולימורפיזם.

**כיצד פועל פולימורפיזם:**

1.  במחלקות שונות יכולות להיות מתודות בעלות שמות זהים.
2.  כאשר מתודה בעלת שם משותף נקראת, הפעולה הספציפית נקבעת על ידי סוג האובייקט שדרכו נקראת המתודה (מה שמכונה "פולימורפיזם דינמי").

**דוגמה:**

```python
class Animal:
  def make_sound(self):
      print("Generic sound")

class Dog(Animal):
    def make_sound(self): # הגדרת המתודה מחדש
       print("Woof!")

class Cat(Animal):
    def make_sound(self): # הגדרת המתודה מחדש
        print("Meow!")

def animal_sound(animal: Animal):
    animal.make_sound() # קריאה למתודה אצל אובייקטים ממחלקות שונות

animal: Animal = Animal()
dog: Dog = Dog()
cat: Cat = Cat()

animal_sound(animal)  # פלט: Generic sound
animal_sound(dog) # פלט: Woof!
animal_sound(cat)  # פלט: Meow!
```

**כתוצאה מכך:**

*   הפונקציה `animal_sound()` משתמשת בפולימורפיזם כדי לעבד אובייקטים מהמחלקות השונות `Animal`, `Dog` ו-`Cat`.
*   אצל כל אובייקט נקראת המתודה `make_sound()`, אך הפלט של מתודה זו שונה, בהתאם למחלקה הספציפית.

לפיכך, **אפשרות ג** היא התשובה הנכונה.