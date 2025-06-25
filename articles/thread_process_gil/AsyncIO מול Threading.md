
## ⚔️ AsyncIO מול Threading – מה עדיף?

כשעובדים עם משימות שדורשות קלט/פלט (I/O), כמו שליחה או קבלה של בקשות רשת, גישה למסדי נתונים או קריאה מקבצים – שתי גישות עיקריות עומדות לרשותנו:
**`threading`** ו־**`asyncio`**.

אבל מתי נשתמש בכל אחת מהן? ואיזו גישה יעילה יותר?

---

### 🧵 Threading – ריבוי שרשורים

מודול `threading` מאפשר להריץ **כמה שרשורים (Threads)** במקביל, כאשר כל אחד מהם מטפל במשימה שונה.

#### ✅ יתרונות:

* פשוט להבנה – נראה כמו קוד רגיל.
* מתאים לשילוב בקוד קיים בלי שינויים רבים.
* תומך בקוד חוסם (blocking) כמו `requests.get()` או `open()`.

#### ❌ חסרונות:

* צריכת זיכרון גבוהה יותר – כל שרשור צורך סטאק נפרד.
* קשה לנהל תקלות או תלויות בין שרשורים.
* GIL עדיין מגביל ביצוע של קוד פייתון במקביל.

#### 📦 דוגמה:

```python
from threading import Thread
import time

def download():
    print("מוריד נתונים...")
    time.sleep(2)
    print("הורדה הושלמה.")

threads = [Thread(target=download) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
```

---

### 🌀 AsyncIO – תכנות אסינכרוני

`asyncio` הוא מודול שמבוסס על **לולאת אירועים (Event Loop)**. כל פעולה "ממתינה" באמצעות `await`, והלולאה שולטת מתי להריץ כל פעולה.

#### ✅ יתרונות:

* יעילות גבוהה – מעט מאוד זיכרון.
* אידיאלי לאלפי משימות I/O מקבילות.
* שליטה טובה יותר על זרימת התוכנית וחריגות.

#### ❌ חסרונות:

* דורש חשיבה שונה – async/await בכל מקום.
* ספריות רבות לא תומכות ב־async (למשל `requests`).
* קוד חוסם (blocking) יפגע בביצועים אם לא מטופל נכון.

#### 📦 דוגמה:

```python
import asyncio

async def download():
    print("מוריד נתונים...")
    await asyncio.sleep(2)
    print("הורדה הושלמה.")

async def main():
    tasks = [download() for _ in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

---

### ⚖️ השוואה מהירה

| קריטריון          | Threading                    | AsyncIO                        |
| ----------------- | ---------------------------- | ------------------------------ |
| ביצועים (I/O)     | טוב                          | מצוין (יעיל יותר)              |
| תמיכה בקוד קיים   | נוחה מאוד                    | דורש שכתוב ל־`async`/`await`   |
| תמיכה בקוד חוסם   | טובה (טבעית)                 | בעיה – דורש טיפול מיוחד        |
| שימוש בזיכרון     | גבוה (Stack נפרד לכל Thread) | נמוך (קורוטינות משתפות זיכרון) |
| מתאים ל־CPU-bound | לא – GIL מגביל               | לא – גם כאן GIL קיים           |
| קריאות קוד        | פשוט                         | מורכב יותר                     |

---

### 🧠 אז במה לבחור?

* אם אתה עובד עם **ספריות חוסמות** כמו `requests`, עדיף להשתמש ב־**Threading**.
* אם אתה בונה **מערכת חדשה** שצריכה לטפל בהרבה בקשות במקביל – **AsyncIO** תהיה בחירה יעילה ואלגנטית יותר.
* לשימושי **חישוב כבד (CPU-bound)** – שני אלו לא יעזרו. עבור ל־`multiprocessing`.

---

### 🎁 טיפ בונוס: רוצה שילוב של שניהם?

תוכל להריץ קוד `asyncio` בתוך שרשור או ההפך – לפעמים שימוש **היברידי** נותן את הפתרון האופטימלי למערכות מורכבות.

בשמחה! הנה דוגמה מתקדמת המשלבת בין `asyncio` לבין `threading`, וכן דוגמה נוספת להורדת קבצים מהאינטרנט בצורה אסינכרונית עם `aiohttp`.

---

## 🔄 שילוב בין AsyncIO ו־Threading

לעיתים נרצה להריץ לולאת `asyncio` בתוך תוכנה מבוססת שרשורים – לדוגמה: אפליקציה גרפית, או שרת שמריץ משימות רקע אסינכרוניות.

### 📌 דוגמה – הרצת קוד אסינכרוני מתוך Thread:

```python
import asyncio
from threading import Thread

async def async_task():
    print("התחלנו את המשימה האסינכרונית")
    await asyncio.sleep(2)
    print("סיימנו את המשימה האסינכרונית")

def run_async_in_thread():
    asyncio.run(async_task())

# יוצרים שרשור שמריץ את הקוד האסינכרוני
t = Thread(target=run_async_in_thread)
t.start()
t.join()
```

> 💡 שימושי במיוחד כשיש לך לוגיקה אסינכרונית, אבל אתה בתוך סביבה שלא תומכת ב־`asyncio.run()` ישירות.

---

## 🌐 הורדת קבצים עם aiohttp בצורה אסינכרונית

מודול `aiohttp` הוא ספריית HTTP אסינכרונית – אידאלית להורדות או קריאות API.

### 📦 דוגמה – הורדה מקבילה של מספר קבצים:

```python
import asyncio
import aiohttp
import os

async def download_file(session, url, filename):
    async with session.get(url) as response:
        content = await response.read()
        with open(filename, 'wb') as f:
            f.write(content)
        print(f"הקובץ נשמר בשם: {filename}")

async def main():
    urls = [
        ("https://example.com/file1.jpg", "file1.jpg"),
        ("https://example.com/file2.jpg", "file2.jpg"),
        ("https://example.com/file3.jpg", "file3.jpg"),
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [
            download_file(session, url, name)
            for url, name in urls
        ]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```

> 🛡️ טיפ: ניתן לשלב גם `semaphore` להגבלת מספר ההורדות במקביל.

---

## 🧠 סיכום: שילוב מנצח

| מתי נשתמש בזה?                       | כיצד נשלב?                               |
| ------------------------------------ | ---------------------------------------- |
| לוגיקה אסינכרונית בתוך GUI או Thread | נריץ `asyncio.run()` מתוך שרשור.         |
| קריאות רשת רבות בבת אחת              | נשתמש ב־`aiohttp` בתוך `asyncio.gather`. |
| ממשק API שמגיב לאירועים              | נשתמש בלולאת אירועים בתוך שרשור נפרד.    |

---
מצוין! הנה שתי דוגמאות נוספות שיכולות לשדרג כל מדריך מתקדם על ביצועים אסינכרוניים בפייתון:

---

## 🧯 שליטה בעומס עם `asyncio.Semaphore`

כאשר אנו שולחים עשרות או מאות בקשות במקביל (למשל API או הורדות), חשוב **לשלוט בעומס** כדי לא להציף את השרת או את המערכת.

`asyncio.Semaphore` מאפשר לנו **להגביל את מספר המשימות שרצות בו־זמנית**.

### 📦 דוגמה – הורדה מוגבלת עם Semaphore:

```python
import asyncio
import aiohttp

sem = asyncio.Semaphore(3)  # מריצים עד 3 בקשות בו-זמנית

async def download(session, url):
    async with sem:  # רק 3 הורדות בו זמנית
        print(f"מוריד {url}")
        async with session.get(url) as resp:
            await resp.read()
        print(f"סיים {url}")

async def main():
    urls = [
        f"https://example.com/file{i}.jpg" for i in range(1, 11)
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [download(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())
```

> 🎛️ הסמפור מבטיח שהמערכת תישאר יציבה גם כשיש הרבה משימות במקביל.

---

## 🧵 שילוב קוד חסום (`Blocking`) עם `ThreadPoolExecutor`

מה אם יש לך קוד שאינו תומך ב־`async`? לדוגמה: קריאה לספריית `PIL` או `requests`?
אפשר להריץ אותו בצורה אסינכרונית בתוך לולאת `asyncio` באמצעות `run_in_executor`.

### 🛠️ דוגמה – קריאה חסומה מתוך async:

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests

# קוד שחוסם – לא תומך ב-async
def get_website(url):
    print(f"מוריד {url}")
    resp = requests.get(url)
    print(f"{url} החזיר {resp.status_code}")
    return resp.text

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://python.org"
    ]
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [
            loop.run_in_executor(executor, get_website, url)
            for url in urls
        ]
        results = await asyncio.gather(*tasks)
    print("הסתיים")

asyncio.run(main())
```

> ⚡ פתרון מצוין כשמשלבים קוד חוסם בפרויקט אסינכרוני.

---

### 🎁 בונוס – מתי להשתמש במה?

| תרחיש                                  | פתרון מומלץ                     |
| -------------------------------------- | ------------------------------- |
| צריך להגביל את כמות הקריאות במקביל     | `asyncio.Semaphore`             |
| קוד חוסם (blocking) בתוך לולאת asyncio | `run_in_executor` עם ThreadPool |
| הורדה מהירה מאתרי רשת                  | `aiohttp` עם `asyncio.gather`   |

---

