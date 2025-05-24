### `question_817.md`
**שאלה 817**

בעת יצירת יישום Python שאמור להסתיים בצורה תקינה בעת קבלת האות `SIGINT` (לדוגמה, בעת לחיצה על CTRL+C), איזה מבין קטעי הקוד הבאים משתמש במודול `signal` בצורה *הנכונה ביותר* לרישום מטפל באות?

**אפשרויות התשובה:**

*   **A:**
    ```python
    import signal

    def handler(signum, frame):
        print("האות התקבל!")

    signal.signal(signal.SIGINT, handler())
    ```

*   **B:**
    ```python
    import signal

    def handler(signum, frame):
        print("האות התקבל!")

    signal.signal(signal.SIGINT, handler)
    ```

*   **C:**
    ```python
    import signal

    def handler():
        print("האות התקבל!")

    signal.signal(signal.SIGINT, handler)
    ```

*   **D:**
    ```python
    import signal

    def handler(signum):
        print("האות התקבל!")

    signal.signal(signal.SIGINT, handler)
    ```

**התשובה הנכונה:**

*   **B**

**הסבר:**

הפונקציה `signal.signal()` מקבלת שני ארגומנטים: מספר האות (לדוגמה, `signal.SIGINT`) ו-*פונקציה מטפלת*. חשוב להעביר את *הפונקציה עצמה* (שמה) בתור ארגומנט, ולא את תוצאת הקריאה לה. אפשרות B מעבירה את `handler`, וזה נכון. אפשרות A מעבירה את `handler()`, מה שיפעיל את הפונקציה מיד ויעביר את תוצאת הביצוע שלה (במקרה זה, `None`) ל-`signal.signal()`, דבר שיוביל לשגיאה או לפעולה שגויה. פונקציית המטפל צריכה לקבל 2 ארגומנטים.

**דוגמה:**

```python
import signal
import time

def handler(signum, frame):
    print("האות SIGINT התקבל! מסיים את התוכנית...")
    exit(0)

signal.signal(signal.SIGINT, handler)

print("התוכנית הופעלה. לחץ CTRL+C כדי לסיים.")

while True:
    print("פועל...")
    time.sleep(1)
```

בדוגמה זו, כאשר המשתמש לוחץ על CTRL+C, הפונקציה `handler` תיקרא, תדפיס הודעה ותסיים את התוכנית.