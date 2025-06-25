
## 🧠 מהו GIL בפייתון, ולמה זה חשוב?

### 🔒 מה זה בעצם GIL?

ה־**GIL (Global Interpreter Lock)** הוא מנגנון פנימי במפרש של פייתון (בגרסת CPython), שמוודא ש **רק שרשור אחד** מריץ קוד פייתון בכל רגע נתון – גם אם יש לך כמה ליבות מעבד פנויות.

> כן, אפילו אם יצרת 10 שרשורים – רק אחד מהם מריץ קוד פייתון בזמן נתון.

---

### 🧪 למה זה קיים?

המנעול הזה קיים כדי **לפשט את ניהול הזיכרון** בפייתון, שמתבסס על מנגנון של ספירת הפניות (Reference Counting). בלי GIL, היינו צריכים לטפל בהרבה תקלות תחרות (Race Conditions) בניהול זיכרון, וזה היה הופך את CPython למסובך יותר וחשוף לבעיות.

---

## 🐢 איך GIL משפיע על הביצועים?

### 💻 קוד שמבצע חישובים:

אם אתה מריץ קוד שכולו חישובים מתמטיים, לולאות, ניתוח נתונים – תראה ש־**שימוש בשרשורים לא נותן שיפור אמיתי בביצועים**. לפעמים אפילו יהיה איטי יותר.

```python
from threading import Thread
from time import perf_counter

def cpu_task():
    print('מתחילים חישוב כבד...')
    total = 0
    for i in range(10**7):
        total += i
    print('סיימנו חישוב.')

start = perf_counter()
threads = [Thread(target=cpu_task) for _ in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join()

end = perf_counter()
print(f'סה"כ זמן: {end - start:.2f} שניות')
```

> התוצאה? בערך כמו אם היית מריץ את הפונקציה ברצף 4 פעמים. לא באמת מקבילי.

---

### 🌐 קוד מבוסס קלט/פלט:

כאן GIL **לא מפריע** כי ברגע ששרשור מחכה (למשל לקריאה מקובץ או רשת), הוא "משחרר" את ה־GIL ומאפשר לשרשור אחר לרוץ. לכן במקרים של עבודה עם API, מסד נתונים, קבצים וכו' – threading עוזר.

---

## 🚀 פתרונות – איך כן מריצים קוד מקבילי "אמיתי"?

### 🧩 1. שימוש ב־`multiprocessing`

המודול `multiprocessing` יוצר **תהליכים נפרדים**, ולא שרשורים – ולכן כל תהליך מקבל GIL משלו.

```python
from multiprocessing import Process

def cpu_task():
    total = 0
    for i in range(10**7):
        total += i

processes = [Process(target=cpu_task) for _ in range(4)]

for p in processes:
    p.start()
for p in processes:
    p.join()
```

> ✅ תוצאות: הרבה יותר מהיר כשמדובר על חישובים כבדים. כל תהליך רץ על ליבה משלו.

---

### ⚙️ 2. שימוש ב־`asyncio`

כשיש הרבה פעולות קלט/פלט – אפשר גם להשתמש ב־`asyncio`, שהוא פתרון מבוסס לולאת אירועים. זה לא "מקבילי אמיתי" אבל **מאוד יעיל וחסכוני** במשאבים.

```python
import asyncio

async def fetch_data():
    print("מתחילים קריאה לשרת...")
    await asyncio.sleep(1)
    print("קיבלנו תגובה.")

async def main():
    await asyncio.gather(*(fetch_data() for _ in range(5)))

asyncio.run(main())
```

---

## 🧭 לסיכום

| סוג משימה     | פתרון מועדף              |
| ------------- | ------------------------ |
| חישובים כבדים | `multiprocessing`        |
| קלט/פלט (I/O) | `threading` / `asyncio`  |
| עבודה עם APIs | `asyncio` או `threading` |
| ריבוי קבצים   | `threading`              |

---
