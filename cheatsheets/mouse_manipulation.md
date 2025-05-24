## שליטה בעכבר ב-Python: מדריך מפורט

**שלב 1: התקנת ספריית `mouse`**

```bash
pip install mouse
```

**שלב 2: הדמיית לחיצות עכבר**

&nbsp;&nbsp;&nbsp;&nbsp; ספריית `mouse` מאפשרת לדמות לחיצות של כפתורי העכבר השמאלי, הימני והאמצעי:

```python
import mouse

# לחיצה שמאלית
mouse.click('left')

# לחיצה ימנית
mouse.click('right')

# לחיצה אמצעית
mouse.click('middle')

# בדיקת לחיצת כפתור
is_pressed = mouse.is_pressed("right")
print(f"כפתור העכבר הימני נלחץ: {is_pressed}")
```

*הערה: מומלץ לבדוק את הקוד בנפרד בסביבה אינטראקטיבית, כגון IPython או Jupyter Notebook.*

**שלב 3: קבלת מיקום סמן העכבר**

הפונקציה `mouse.get_position()` מחזירה את הקואורדינטות הנוכחיות של הסמן (x, y):

```python
position = mouse.get_position()
print(f"מיקום הסמן: {position}")
```

הקואורדינטות (0, 0) מתאימות בדרך כלל לפינה השמאלית העליונה של המסך. נוכחות של מספר מסכים עשויה להשפיע על ערכי הקואורדינטות.

**שלב 4: גרירת עכבר**

&nbsp;&nbsp;&nbsp;&nbsp; לגרירת הסמן משתמשים בפונקציה `mouse.drag()`:

```python
# גרירה מ-(0, 0) ל-(100, 100) יחסית למיקום הנוכחי (תנועה יחסית)
mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)

# גרירה ממיקום מוחלט (100, 100) למיקום מוחלט (200, 200)
mouse.drag(100, 100, 200, 200, absolute=True, duration=0.2)
```

`absolute=False` מציין תנועה יחסית, ו-`absolute=True` – תנועה מוחלטת. `duration` מגדיר את משך הגרירה בשניות.

**שלב 5: הזזת עכבר**

&nbsp;&nbsp;&nbsp;&nbsp; הפונקציה `mouse.move()` מזיזה את הסמן למיקום שצוין:

```python
# הזזה 100 פיקסלים ימינה ו-50 פיקסלים מטה יחסית למיקום הנוכחי
mouse.move(100, 50, absolute=False, duration=0.2)

# הזזה למיקום מוחלט (200, 300)
mouse.move(200, 300, absolute=True, duration=0.1)
```

**שלב 6: טיפול באירועי עכבר**

&nbsp;&nbsp;&nbsp;&nbsp; ניתן להשתמש בפונקציות `mouse.on_click()` ו-`mouse.on_right_click()` כדי ליצור מטפלים לאירועי לחיצות:

```python
def left_click_handler():
    print("כפתור העכבר השמאלי נלחץ")

def right_click_handler():
    print("כפתור העכבר הימני נלחץ")


mouse.on_click(left_click_handler)
mouse.on_right_click(right_click_handler)

# ... (הקוד שלך) ...

# להסרת המטפלים:
mouse.unhook_all()
```

**שלב 7: גלילת גלגל העכבר**

&nbsp;&nbsp;&nbsp;&nbsp; הפונקציה `mouse.wheel()` מדמה גלילה:

```python
# גלילה מטה בצעד אחד
mouse.wheel(-1)

# גלילה מעלה בשלושה צעדים
mouse.wheel(3)
```

**שלב 8: הקלטה והפעלה מחדש של אירועי עכבר**

&nbsp;&nbsp;&nbsp;&nbsp; ניתן להקליט רצף של אירועי עכבר ולאחר מכן להפעיל אותם מחדש:

```python
# הקלטת אירועים עד ללחיצה על הכפתור הימני
events = mouse.record()

# הפעלת האירועים המוקלטים מחדש (למעט האחרון - לחיצת הכפתור הימני)
mouse.play(events[:-1])
```

**שלב 9: דוגמה: ציור צורה (אופציונלי)**

&nbsp;&nbsp;&nbsp;&nbsp; דוגמה זו מציירת ריבוע ועיגול בעורך גרפי (לדוגמה, Paint):

```python
import mouse
import math
import time

def draw_square(size):
    mouse.press()  # לוחצים על הכפתור השמאלי
    mouse.move(size, 0, absolute=False, duration=0.2)
    mouse.move(0, size, absolute=False, duration=0.2)
    mouse.move(-size, 0, absolute=False, duration=0.2)
    mouse.move(0, -size, absolute=False, duration=0.2)
    mouse.release() # משחררים את הכפתור

def draw_circle(radius):
    mouse.press()
    for i in range(0, 360, 5):
        angle = math.radians(i)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        mouse.move(x, y, absolute=False, duration=0.01)
    mouse.release()

if __name__ == "__main__":
    draw_square(200)
    time.sleep(1)  # הפסקה לפני ציור העיגול
    draw_circle(100)
```

לפני הפעלת קוד זה, ודאו שסמן העכבר נמצא במיקום הרצוי בעורך הגרפי.