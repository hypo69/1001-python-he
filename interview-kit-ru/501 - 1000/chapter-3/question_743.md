### `question_743.md`

**שאלה 743.** מהן פיקסטורות (fixtures) ב-PyTest, ואילו פיקסטורות מובנות אתם מכירים המשמשות לבדיקת זרמי קלט/פלט, רישום לוגים ודוחות?

- א. פיקסטורות הן דרך ליצירת והרצת בדיקות ב-PyTest, שאינה דורשת תיאור קוד.
- ב. פיקסטורות הן דקורטורים מיוחדים לפונקציות, שמחזירות ערכים שיכולים לשמש בפונקציות בדיקה. Pytest מספק מגוון פיקסטורות מובנות, כגון: `capfd`, `capfdbinary`, `capsys`, `capsysbinary` (לעבודה עם זרמי קלט/פלט), `caplog` (לרישום לוגים) ו-`recwarn` (לטיפול באזהרות).
- ג. פיקסטורות הן אובייקטים המשמשים ליצירת מחלקות דינמיות, המשנות את התנהגות הפונקציות.
- ד. פיקסטורות הן דרך חלופית לתיאור פונקציות ב-PyTest.

**תשובה נכונה: ב**

**הסבר:**

ב-PyTest, פיקסטורות (fixtures) הן מנגנון רב עוצמה המאפשר ליצור ולנהל סביבות בדיקה, לספק נתוני בדיקה ומשאבים לפונקציות בדיקה. PyTest מספק פיקסטורות מובנות רבות למטרות שונות.

*   **מאפיינים עיקריים של פיקסטורות:**
    *   **הכנה לבדיקות:** פיקסטורות יכולות לשמש להכנת נתונים, משאבים או סביבה הנחוצים לבדיקות.
    *   **שימוש חוזר:** מאפשרות שימוש חוזר באותו קוד להכנת בדיקות.
    *   **אוטומציה:** פיקסטורות יכולות לרוץ אוטומטית לפני או אחרי בדיקה.
    *   **ארגומנטים:** פונקציות בדיקה יכולות לקבל פיקסטורות כארגומנטים (הזרקת תלויות - dependency injection).
    *   **ניהול משאבים:** מאפשרות לנהל משאבים (לדוגמה, פתיחה או סגירת קבצים).
*   **פיקסטורות מובנות של PyTest:**
        *   **לעבודה עם זרמי קלט/פלט:**
            *   `capfd` - ליירוט זרמי קלט ופלט סטנדרטיים, ברמת מערכת ההפעלה (מחזיר טקסט).
            *   `capfdbinary` - ליירוט זרמי קלט ופלט סטנדרטיים, ברמת מערכת ההפעלה (מחזיר בתים).
            *   `capsys` - ליירוט זרמי קלט ופלט סטנדרטיים ברמת Python (מחזיר טקסט).
            *   `capsysbinary` - ליירוט זרמי קלט ופלט סטנדרטיים ברמת Python (מחזיר בתים).
        *   **לרישום לוגים:**
            *   `caplog` - לעבודה עם לוגים של קוד Python, מאפשר לשנות רמות רישום, ליירט ולסנן הודעות.
        *   **למעקב אחר אזהרות:**
            *   `recwarn` - משמש למעקב אחר אזהרות.
        *   **ליצירת דוחות:**
            *   `doctest_namespace` - לעבודה עם ספריית `doctest`, המאפשרת לבדוק קוד בתיעוד.
*   **כיצד פיקסטורות עובדות**
    *   Pytest מזהה אוטומטית פונקציות עם הדקורטור `@pytest.fixture`.
    *   בעת קריאה לפונקציית בדיקה, אם נעשה שימוש בשם של פיקסטורה בפרמטרים של הפונקציה, היא תופעל אוטומטית.
    *   תוצאת ריצת הפיקסטורה תועבר כארגומנט לפונקציית הבדיקה.

**דוגמאות:**

```python
import pytest
import os
import logging
import warnings
import numpy # This import was outside the code block in the original, moved it inside for consistency

# פיקסטורה לעבודה עם os
def test_system_echo(capfd):
      os.system('echo "hello"')
      captured = capfd.readouterr()
      assert captured.out == "hello\n"
# פיקסטורה לעבודה עם bytes
def test_system_echo2(capfdbinary):
      os.system('echo "hello"')
      captured = capfdbinary.readouterr()
      assert captured.out == b"hello\n"
# פיקסטורה לזרם פלט של python
def test_output(capsys):
        print("hello")
        captured = capsys.readouterr()
        assert captured.out == "hello\n"

def test_output2(capsysbinary):
        print("hello")
        captured = capsysbinary.readouterr()
        assert captured.out == b"hello\n"

# פיקסטורה ללוגים
def test_foo(caplog):
    caplog.set_level(logging.INFO)
    logging.info("test message for info level")
    for message in caplog.messages:
        assert "debug level" not in message

def func_under_test():
  logging.info("this is info")
  logging.warning("this is warning")
  logging.error("this is error")

def test_baz(caplog):
    func_under_test()
    for record in caplog.records:
        assert record.levelname != "CRITICAL"
    assert "wally" not in caplog.text

# פיקסטורה למעקב אחר אזהרות
def test_check_warnings(recwarn):
    warnings.warn("hello", UserWarning)
    assert len(recwarn) == 1
    warn = recwarn.pop(UserWarning)
    assert issubclass(warn.category, UserWarning)
    assert str(warn.message) == "hello"
    assert warn.filename


@pytest.fixture(autouse=True)
def add_np(doctest_namespace):
    doctest_namespace["np"] = numpy

# פיקסטורה ליצירת דוחות (doctest)
def arange():
    """
    >>> a = np.arange(10)
    >>> len(a)
    10
    """
    pass

```
**ניתוח האפשרויות:**
*   **א. פיקסטורות הן דרך ליצירת והרצת בדיקות ב-PyTest, שאינה דורשת תיאור קוד.:** לא נכון.
*   **ב. פיקסטורות הן דקורטורים מיוחדים לפונקציות, שמחזירות ערכים שיכולים לשמש בפונקציות בדיקה. Pytest מספק מגוון פיקסטורות מובנות, כגון: `capfd`, `capfdbinary`, `capsys`, `capsysbinary` (לעבודה עם זרמי קלט/פלט), `caplog` (לרישום לוגים) ו-`recwarn` (לטיפול באזהרות).:** נכון.
*   **ג. פיקסטורות הן אובייקטים המשמשים ליצירת מחלקות דינמיות, המשנות את התנהגות הפונקציות.:** לא נכון.
*   **ד. פיקסטורות הן דרך חלופית לתיאור פונקציות ב-PyTest.:** לא נכון.

**לסיכום:**
*   פיקסטורות מאפשרות ליצור סביבת בדיקה גמישה וניתנת לשימוש חוזר.
*   Pytest מספק מגוון רחב של פיקסטורות מובנות למשימות שונות.
*   `capfd`, `capfdbinary`, `capsys`, `capsysbinary` מאפשרות עבודה עם זרמי קלט/פלט.
*   `caplog` מאפשר עבודה עם רישום לוגים.
*   `recwarn` מאפשר טיפול באזהרות.
*   `doctest_namespace` מאפשר עבודה עם doctests.

לפיכך, התשובה הנכונה היא **ב. פיקסטורות הן דקורטורים מיוחדים לפונקציות, שמחזירות ערכים שיכולים לשמש בפונקציות בדיקה. Pytest מספק מגוון פיקסטורות מובנות, כגון: `capfd`, `capfdbinary`, `capsys`, `capsysbinary` (לעבודה עם זרמי קלט/פלט), `caplog` (לרישום לוגים) ו-`recwarn` (לטיפול באזהרות).**