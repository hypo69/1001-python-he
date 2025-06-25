בטח, הנה התרגום של הפוסט לעברית:

# 🧲 איך "לתפוס" את `print()` בפייתון: לכידת `stdout` ללא ספריות חיצוניות

בפייתון, אפשר ללכוד את מה שמוצג על המסך דרך הפקודה `print()`.
אני אראה איך לפתור את המשימה הזו באלגנטיות – ללא תלויות חיצוניות, באמצעות הספרייה הסטנדרטית וכמה שורות קוד בודדות.

---

## 📦 הקשר קצר: לכידת stdout

הדרך הפשוטה ביותר היא להקצות מחדש באופן זמני את `sys.stdout` לאובייקט `io.StringIO()` בתוך מנהל הקשר (context manager):

```python
from contextlib import contextmanager
import sys
import io

@contextmanager
def capture_stdout():
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout
```

דוגמת שימוש:

```python
with capture_stdout() as out:
    print("זהו פלט שנלכד")

print("התוצאה:", out.getvalue())
```

---

## 🔧 רוצים יותר שליטה?

הנה עוד אפשרויות שימושיות:

### 💬 לכידת `stderr`

```python
@contextmanager
def capture_stderr():
    old = sys.stderr
    sys.stderr = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stderr = old
```

### 🔁 לכידת `stdout` + `stderr` משולבים

```python
@contextmanager
def capture_output():
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = sys.stderr = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
```

---

## 💡 דוגמאות מהחיים האמיתיים

### ✅ בדיקת הפלט של פונקציה

```python
def say_hello(name):
    print(f"Hello, {name}!")

with capture_stdout() as out:
    say_hello("Pythonista")

assert "Hello, Pythonista!" in out.getvalue()
```

### 🔕 השתקת פלט "רועש"

```python
with capture_stdout():
    import noisy_library
```

### 📝 רישום לוג של פלט מפקודה חיצונית

```python
with capture_output() as out:
    run_some_cli_tool()

with open("cli_output.log", "w") as f:
    f.write(out.getvalue())
```

---

## 🔀 ומה אם צריך גם לראות וגם ללכוד?

לפעמים רוצים שהפלט של `print()` **גם יוצג בטרמינל וגם יישמר**. אפשר לעשות זאת באמצעות אובייקט `Tee`:

```python
class Tee(io.StringIO):
    def __init__(self, original):
        super().__init__()
        self.original = original

    def write(self, text):
        self.original.write(text)
        super().write(text)

@contextmanager
def capture_stdout_tee():
    old_stdout = sys.stdout
    sys.stdout = tee = Tee(old_stdout)
    try:
        yield tee
    finally:
        sys.stdout = old_stdout
```

דוגמה:

```python
with capture_stdout_tee() as out:
    print("הפלט הזה נראה גם בטרמינל וגם נשמר בבאפר")

print("מהבאפר:", out.getvalue())
```

נאגד את כל הרעיונות שתוארו לעיל לכדי **כלי עזר שימושי ועצמאי** ללכידת פלט בפייתון, שניתן:

*   לייבא לכל פרויקט,
*   להשתמש בו לבדיקות, רישום לוגים וניפוי שגיאות,
*   להרחיב בקלות.

---

## 📦 קובץ: `stdout_capture.py`

```python
"""
stdout_capture.py

כלי עזר ללכידת stdout ו-stderr באמצעות מנהלי הקשר.

תומך ב:
- לכידת stdout;
- לכידת stderr;
- לכידת stdout + stderr משולבים;
- מצב "Tee" – פלט בו-זמני לטרמינל ולבאפר.

אינו דורש ספריות חיצוניות.
"""

import sys
import io
from contextlib import contextmanager


@contextmanager
def capture_stdout():
    """
    לוכד את stdout (הפלט של print).
    """
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout


@contextmanager
def capture_stderr():
    """
    לוכד את stderr (שגיאות וחריגות).
    """
    old_stderr = sys.stderr
    sys.stderr = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stderr = old_stderr


@contextmanager
def capture_output():
    """
    לוכד את stdout ו-stderr בו-זמנית.
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = sys.stderr = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


class Tee(io.StringIO):
    """
    מחלקת Tee: שומרת את הפלט ומעבירה אותו ל-stdout/stderr המקורי.
    """
    def __init__(self, original):
        super().__init__()
        self.original = original

    def write(self, text):
        self.original.write(text)
        super().write(text)

    def flush(self):
        self.original.flush()


@contextmanager
def capture_stdout_tee():
    """
    לכידת Tee של stdout – שומר ומציג בו-זמנית.
    """
    old_stdout = sys.stdout
    sys.stdout = tee = Tee(old_stdout)
    try:
        yield tee
    finally:
        sys.stdout = old_stdout


@contextmanager
def capture_output_tee():
    """
    לכידת Tee של stdout ו-stderr – שומר ומציג בו-זמנית.
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    # כשיש Tee משולב, חשוב להעביר לו את ה-stdout המקורי כדי שהוא יכתוב למסך,
    # ולא ליצור שרשרת של Tee אם משתמשים ב-Tee גם ל-stderr בנפרד.
    # כאן, אנחנו רוצים שגם stdout וגם stderr ינותבו לאותו אובייקט Tee,
    # והוא ידפיס ל-stdout המקורי.
    sys.stdout = sys.stderr = tee = Tee(old_stdout)
    try:
        yield tee
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
```

---

## ✅ דוגמאות שימוש

```python
from stdout_capture import capture_stdout, capture_output, capture_stdout_tee


def test_func():
    print("Hello from function")


# לכידה פשוטה
with capture_stdout() as out:
    test_func()

print("נלכד:", out.getvalue())


# stdout + stderr משולבים
with capture_output() as out:
    print("Something")
    try:
        raise Exception("Oops")  # ילכד גם כן
    except Exception:
        sys.stderr.write("Oops from stderr\n") # הדגמה לכתיבה ל-stderr

# שמירת הפלט והצגתו בו-זמנית
with capture_stdout_tee() as out:
    print("Visible AND captured")

print("נלכד ב-Tee:", out.getvalue())
```