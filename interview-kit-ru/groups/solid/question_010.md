### `question_010.md` (DIP - יישום מעשי)

**שאלה 010.** איזה מבין קטעי הקוד הבאים בפייתון מדגים את יישום עקרון היפוך התלויות (Dependency Inversion Principle - DIP) *בצורה המדויקת ביותר*?

A.

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()
```

B.

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Switch:
    def __init__(self):
        self.bulb = LightBulb()

    def operate(self):
        self.bulb.turn_on()
```

C.

```python
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self): pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()
```

D.

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Switch:
    def __init__(self):
        pass

    def operate(self, bulb: LightBulb):
        bulb.turn_on()
```

**תשובה נכונה: C**

**הסבר:**

עקרון היפוך התלויות (DIP) קובע שמודולים ברמה גבוהה לא צריכים להיות תלויים במודולים ברמה נמוכה. שניהם צריכים להיות תלויים באבסטרקציות. וריאנט C מדגים זאת *בצורה המדויקת ביותר*.

*   **וריאנט A:** `Switch` תלוי ישירות ב-`LightBulb` (מודול ברמה נמוכה). זוהי *הפרה* של DIP.
*   **וריאנט B:** זהה ל-A. `Switch` יוצר מופע של `LightBulb`, מה שמגדיל את התלות.
*   **וריאנט C:** `Switch` תלוי באבסטרקציה `Switchable` (ממשק). `LightBulb` מיישם ממשק זה. זה תואם ל-DIP. `Switch` אינו יודע מה הוא מפעיל, אלא רק שהאובייקט יודע לבצע `turn_on`.
*   **וריאנט D:** התלות מועברת דרך ארגומנט המתודה `operate`, מה שמפחית את הצימוד, אך עדיין אינו משתמש באבסטרקציה.

**דוגמה:**

בדוגמה זו קל להחליף את `LightBulb` בהתקן אחר המיישם את `Switchable`, לדוגמה `Fan`, מבלי לשנות את הקוד של `Switch`:

```python
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self): pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: Fan started")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()

bulb = LightBulb()
switch = Switch(bulb)
switch.operate() # Output: LightBulb: Bulb turned on

fan = Fan()
switch = Switch(fan)
switch.operate() # Output: Fan: Fan started
```

**לסיכום:**

וריאנט C מדגים את DIP בצורה המדויקת ביותר, שכן `Switch` תלוי באבסטרקציה `Switchable`, ולא במימוש ספציפי של `LightBulb`.

לפיכך, וריאנט C הוא התשובה הנכונה.