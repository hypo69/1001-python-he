from tkinter import *
import time
import random
import pygame  # אף על פי שיובא, אינו בשימוש בקוד

class Ball():
    """
    מחלקה המייצגת את הכדור במשחק.
    """
    def __init__(self, canvas: Canvas, platform: object, color: str) -> None:
        """
        אתחול הכדור.
        
        ארגומנטים:
            canvas: בד ה-Tkinter שעליו מצויר הכדור.
            platform: אובייקט הפלטפורמה לקביעת התנגשויות.
            color: צבע הכדור.
        """
        self.canvas = canvas
        self.platform = platform
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.dir = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(self.dir)
        self.y = -1
        self.touch_bottom = False

    def touch_platform(self, ball_pos: tuple) -> bool:
        """
        בודק התנגשות של הכדור עם הפלטפורמה.
        
        ארגומנטים:
             ball_pos: קואורדינטות הכדור (x1, y1, x2, y2).
        החזרות:
            True, אם הכדור התנגש בפלטפורמה, אחרת False.
        """
        platform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True
        return False

    def draw(self) -> None:
         """
        מזיז את הכדור על הבד ומטפל בהתנגשויות עם קירות ופלטפורמה.
        """
        self.canvas.move(self.oval, self.x, self.y)
        pos = self.canvas.coords(self.oval)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 400:
            self.touch_bottom = True
        if self.touch_platform(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3

class Platform():
    """
    מחלקה המייצגת את הפלטפורמה במשחק.
    """
    def __init__(self, canvas: Canvas, color: str) -> None:
        """
        אתחול הפלטפורמה.
        
        ארגומנטים:
             canvas: בד ה-Tkinter שעליו מצוירת הפלטפורמה.
             color: צבע הפלטפורמה.
        """
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def left(self, event: object) -> None:
         """
        מטפל באירוע לחיצת מקש "שמאלה".
        
        ארגומנטים:
            event: אירוע לחיצת המקש.
        """
        self.x = -2

    def right(self, event: object) -> None:
        """
         מטפל באירוע לחיצת מקש "ימינה".
         
        ארגומנטים:
            event: אירוע לחיצת המקש.
        """
        self.x = 2

    def draw(self) -> None:
        """
        מזיז את הפלטפורמה על הבד ומטפל בהתנגשויות עם קירות.
        """
        self.canvas.move(self.rect, self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0

# אתחול החלון
window = Tk()
window.title("ארקייד")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=500, height=400)
canvas.pack()

platform = Platform(canvas, 'green')
ball = Ball(canvas, platform, 'red')

while True:
    if not ball.touch_bottom:
        ball.draw()
        platform.draw()
    else:
        break

    window.update()
    time.sleep(0.01)

window.mainloop()