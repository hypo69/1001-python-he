### `question_008.md` (ISP - דוגמת קוד)

**שאלה 008.** איזו מהאפשרויות הבאות בקוד Python *השלמה ביותר* מדגימה את היישום של עקרון הפרדת הממשקים (Interface Segregation Principle - ISP)?

א.

```python
class Worker: # code omitted
    def work(self): pass
    def eat(self): pass

class робот(Worker):
    def work(self): pass
    def eat(self): pass
```

ב.

```python
class WorkerInterface: # code omitted
    def work(self): pass
    def eat(self): pass

class Worker(WorkerInterface):
    def work(self): pass
    def eat(self): pass
```

ג.

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Worker(Workable, Eatable):
    def work(self): pass
    def eat(self): pass

class Robot(Workable):
    def work(self): pass
```

ד.

```python
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass

class Human(Worker):
    def work(self): pass
    def eat(self): pass

class Robot(Worker):
    def work(self): pass
    # Robot doesn't need to eat, but has to implement it
    def eat(self): pass
```

**תשובה נכונה: ג**

**הסבר:**

עקרון הפרדת הממשקים (ISP) ממליץ ליצור ממשקים קטנים וממוקדים רבים במקום ממשק אחד גדול. זה מאפשר למחלקות ליישם רק את המתודות שהן אכן צריכות.

*   **אפשרות א':** אינה מדגימה את ISP, מכיוון שכל המחלקות מיישמות את אותו הממשק.
*   **אפשרות ב':** זהה לאפשרות א', אך דרך ממשק, מה שלא משנה משמעותית את המצב.
*   **אפשרות ג':** `Workable` ו-`Eatable` מוגדרות כממשקים נפרדים (מחלקות אבסטרקטית). `Worker` מיישמת את שני הממשקים, ו-`Robot` מיישמת רק את `Workable`, מה שתואם את ISP. `Robot` אינו זקוק ליישום `Eatable`, מכיוון שהוא אינו אוכל.
*   **אפשרות ד':** `Robot` נאלץ ליישם את המתודה `eat()`, שאינו זקוק לה, וזה מהווה הפרה של ISP.

**דוגמה:**

קוד זה מציג את הפרדת הממשקים, כאשר `Robot` מיישם רק את המתודות הנחוצות לו:

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        print("Worker is working")

    def eat(self):
        print("Worker is eating")

class Robot(Workable):
    def work(self):
        print("Robot is working")

worker = Worker()
worker.work()
worker.eat()

robot = Robot()
robot.work()
```

**לסיכום:**

רק אפשרות ג' מדגימה יישום נכון של ISP, כאשר הממשקים מחולקים לממשקים קטנים יותר והמחלקות מיישמות רק את הממשקים הנחוצים להן.

לפיכך, אפשרות ג' היא הנכונה.