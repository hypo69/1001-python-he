### `question_157.md`

**שאלה 57.** מהי המטרה העיקרית בשימוש במקשטים (decorators) ב-Python?

א. לשינוי הפונקציונליות הבסיסית של פונקציות.
ב. להוספת פונקציונליות נוספת לפונקציות מבלי לשנות את קוד המקור שלהן.
ג. ליצירת עותקים של פונקציות.
ד. לניפוי שגיאות (דיבוג) בפונקציות.

**תשובה נכונה: ב**

**הסבר:**

מקשטים ב-Python משמשים להוספת פונקציונליות נוספת לפונקציות או שיטות מבלי לשנות את קוד המקור שלהן. הם מספקים דרך לעטוף פונקציה ולהוסיף לה פעולות המבוצעות לפני או אחרי הקריאה לפונקציה המקורית.

*   **אפשרות א** אינה נכונה: מקשטים אינם משנים את הפונקציונליות הבסיסית אלא מרחיבים אותה.
*   **אפשרות ב** נכונה: מקשטים מאפשרים להוסיף פונקציונליות מבלי לשנות את קוד המקור של הפונקציה.
*   **אפשרות ג** אינה נכונה: ליצירת עותק של פונקציה משתמשים ב-`copy.deepcopy()` או `copy.copy()`.
*   **אפשרות ד** אינה נכונה: מקשטים יכולים לשמש לניפוי שגיאות, אך אינם הכלים העיקריים לכך.

**כיצד מקשטים פועלים:**

1.  מקשט הוא פונקציה שמקבלת פונקציה אחרת כארגומנט.
2.  המקשט מחזיר פונקציה חדשה, שבדרך כלל עוטפת את הפונקציה המקורית.
3.  הפונקציה המקושטת מבצעת קודם כל את מעטפת המקשט, ורק אחר כך את קוד הפונקציה עצמה.

**דוגמה:**

```python
import time
from typing import Callable

def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time: float = time.time()
        result = func(*args, **kwargs)
        end_time: float = time.time()
        execution_time: float = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time:.4f} сек")
        return result
    return wrapper


@timer
def my_function(n: int) -> int:
  """פונקציה המאטה את הביצוע"""
  time.sleep(n)
  return n*2

result: int = my_function(2) # פלט: זמן ביצוע הפונקציה my_function: 2.0019 שניות
print(f"Результат: {result}")  # פלט: תוצאה: 4
```

**כתוצאה מכך:**

*   המקשט `@timer` עוטף את הפונקציה `my_function`.
*   בקריאה ל-`my_function`, מבוצע תחילה קוד המקשט `timer`, המודד את זמן הביצוע, ורק אחר כך נקראת הפונקציה `my_function` עצמה.

לפיכך, **אפשרות ב** היא הנכונה.