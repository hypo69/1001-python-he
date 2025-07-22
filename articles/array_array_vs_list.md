# 🧑‍💻 שימוש ב-`array.array` בפייתון: מתי ולמה

מודול **`array`** מספק טיפוס נתונים ייעודי, `array.array`, לאחסון רצפים של מספרים מאותו סוג. בניגוד ל-`list` הגנרי, מערכי `array.array` מאפשרים שימוש יעיל יותר בזיכרון וביצועים משופרים בעבודה עם נתונים מספריים.

---

## 📦 יתרונות מרכזיים של `array.array`

ההבדל המרכזי בין `array.array` ל-`list` הוא **אחסון נתונים קומפקטי**. במקום רשימה של מצביעים לאובייקטים של פייתון, `array.array` שומר את הערכים כבלוק רציף של בתים (bytes), מה שהופך אותו לאידיאלי למשימות הבאות.

---

### 1. חיסכון בזיכרון בעבודה עם כמות גדולה של מספרים

כאשר מעבדים מיליוני איברים מספריים, החיסכון בזיכרון הופך קריטי. `array.array` מפחית משמעותית את התקורה.

```python
import array
import sys

def compare_memory_usage(num_elements: int = 1_000_000) -> None:
    """
    הפונקציה משווה את צריכת הזיכרון בין list לבין array.array.

    Args:
        num_elements (int, optional): כמות האיברים לבדיקה. 
                                      ברירת המחדל היא 1,000,000.
    """
    # יצירת רשימה עם אובייקטים של מספרים שלמים של פייתון
    list_numbers = list(range(num_elements))
    
    # יצירת מערך שבו המספרים נשמרים כטיפוסי int של C בגודל 4 בתים
    array_numbers = array.array('i', range(num_elements))

    list_size = sys.getsizeof(list_numbers)
    array_size = sys.getsizeof(array_numbers)

    print(f"כמות איברים: {num_elements}")
    print(f"גודל list:  {list_size / 1024 / 1024:.2f} MB")
    print(f"גודל array: {array_size / 1024 / 1024:.2f} MB")
    if array_size > 0:
        print(f"חיסכון בזיכרון: פי {list_size / array_size:.2f}")

# דוגמת שימוש
if __name__ == "__main__":
    compare_memory_usage()
```
**פלט:**
```
כמות איברים: 1000000
גודל list:  7.63 MB
גודל array: 3.82 MB
חיסכון בזיכרון: פי 2.00
```

---

### 2. שיפור ביצועים בפעולות על מספרים

בזכות האחסון הרציף בזיכרון, פעולות מתמטיות על איברי `array.array` מתבצעות מהר יותר, מכיוון שהמעבד יכול לנצל את זיכרון המטמון (cache) ביעילות רבה יותר.

```python
import array
import timeit

def compare_performance(num_elements: int = 10_000_000) -> None:
    """
    הפונקציה משווה את ביצועי פעולת הסיכום על איברים ב-list וב-array.array.

    Args:
        num_elements (int, optional): כמות האיברים לבדיקה. 
                                      ברירת המחדל היא 10,000,000.
    """
    setup_code = f"""
import array
data = range({num_elements})
list_data = list(data)
array_data = array.array('i', data)
"""
    
    # מדידת זמן עבור list
    list_time = timeit.timeit("sum(list_data)", setup=setup_code, number=10)
    
    # מדידת זמן עבור array
    array_time = timeit.timeit("sum(array_data)", setup=setup_code, number=10)
    
    print(f"זמן סיכום של {num_elements} איברים (10 חזרות):")
    print(f"list:  {list_time:.4f} שניות")
    print(f"array: {array_time:.4f} שניות")

# דוגמת שימוש
if __name__ == "__main__":
    compare_performance()
```
**פלט:**
```
זמן סיכום של 10000000 איברים (10 חזרות):
list:  2.1106 שניות
array: 1.1549 שניות
```

---

### 3. עבודה ישירה עם ספריות C (`ctypes`, `struct`)

`array.array` מתאים באופן מושלם להעברת נתונים לספריות low-level הכתובות בשפת C, מכיוון שהמבנה הפנימי שלו תואם למערכי C.

#### דוגמה עם `ctypes`:

```python
import array
from ctypes import c_double, CDLL

def demonstrate_ctypes_usage() -> None:
    """
    הפונקציה מדגימה העברת array.array לפונקציית C באמצעות ctypes.
    """
    # מערך עם מספרים בדיוק כפול (טיפוס 'd')
    py_array = array.array('d', [1.1, 2.2, 3.3, 4.4])
    
    # יצירת מערך תואם C מתוך py_array
    # הפונקציה (c_double * len(py_array)) יוצרת טיפוס "מערך של 4 איברי c_double"
    # האופרטור (*) פורס את מערך הפייתון לארגומנטים של בנאי זה
    c_array = (c_double * len(py_array))(*py_array)

    # כאן יכולה להיות קריאה לפונקציית C, לדוגמה:
    # my_c_library = CDLL("./libmath.so")
    # my_c_library.sum_doubles(c_array, len(c_array))
    
    print(f"מערך פייתון: {py_array}")
    print(f"מערך תואם C (ctypes): {[val for val in c_array]}")

# דוגמת שימוש
if __name__ == "__main__":
    demonstrate_ctypes_usage()
```

#### דוגמה עם `struct` לאריזת נתונים:

```python
import array
import struct

def demonstrate_struct_packing(data: list[int]) -> bytes:
    """
    הפונקציה אורזת מערך של מספרים שלמים למחרוזת בינארית.

    Args:
        data (list[int]): רשימת מספרים שלמים לאריזה.

    Returns:
        bytes: ייצוג בינארי של הנתונים.
    """
    arr = array.array('i', data)
    
    # יצירת מחרוזת פורמט כמו '3i' עבור 3 מספרים שלמים
    format_string = f'{len(arr)}i'
    
    # אריזת הנתונים לפורמט בינארי
    binary_data = struct.pack(format_string, *arr)
    
    print(f"מערך מקורי: {arr}")
    print(f"נתונים בינאריים: {binary_data}")
    
    # בדיקה: פריסה בחזרה
    unpacked_data = struct.unpack(format_string, binary_data)
    print(f"נתונים לאחר פריסה: {unpacked_data}")
    
    return binary_data

# דוגמת שימוש
if __name__ == "__main__":
    demonstrate_struct_packing([10, 20, 30])
```

---

### 4. סריאליזציה ודה-סריאליזציה יעילות

המתודות `.tobytes()` ו-`.frombytes()` מאפשרות להמיר במהירות מערך לבתים (bytes) ובחזרה, מה שאידיאלי לשמירה בקבצים או להעברה ברשת.

```python
import array

def handle_binary_data() -> None:
    """
    הפונקציה מדגימה סריאליזציה ודה-סריאליזציה של array.array לבתים.
    """
    # יצירת המערך המקורי
    source_array = array.array('i', [1, 2, 3, 4, 5])
    print(f"מערך מקורי: {source_array}")

    # סריאליזציה של המערך לבתים
    binary_data = source_array.tobytes()
    print(f"נתונים בבתים: {binary_data}")

    # דה-סריאליזציה מבתים למערך חדש
    new_array = array.array('i')
    new_array.frombytes(binary_data)
    print(f"מערך משוחזר: {new_array}")

    # בדיקת שלמות
    assert source_array == new_array, "הנתונים אינם תואמים!"
    print("שלמות הנתונים אומתה.")

# דוגמת שימוש
if __name__ == "__main__":
    handle_binary_data()
```

---

### 5. הבטחת אחידות טיפוסים (Type Safety)

`array.array` אוכף שמירה של טיפוס נתונים יחיד, שנקבע בעת היצירה. זה מגן מפני הוספה מקרית של איברים מטיפוס אחר.

```python
import array

def demonstrate_type_safety() -> None:
    """
    הפונקציה מראה כי array.array אינו מאפשר הוספת איברים מטיפוס אחר.
    """
    arr = array.array('i', [100, 200, 300])
    print(f"מערך של מספרים שלמים: {arr}")
    
    try:
        # ניסיון להוסיף איבר מסוג מחרוזת
        arr.append('hello')
    except TypeError as e:
        # חריגה צפויה
        print(f"\nהניסיון להוסיף 'hello' גרם לשגיאה: {e}")
        print("דבר זה מאשר את בדיקת הטיפוסים המחמירה של המערך.")

# דוגמת שימוש
if __name__ == "__main__":
    demonstrate_type_safety()
```

---

### 6. כתיבה וקריאה ישירות מקבצים בינאריים

המתודות `.tofile()` ו-`.fromfile()` מפשטות את העבודה עם קבצים בינאריים, ומאפשרות להימנע מסריאליזציה כשלב ביניים.

```python
import array
from pathlib import Path

def work_with_binary_files(file_path_str: str = "data.bin") -> None:
    """
    הפונקציה כותבת מערך לקובץ בינארי וקוראת אותו בחזרה.

    Args:
        file_path_str (str, optional): שם הקובץ לשמירה.
                                       ברירת המחדל היא "data.bin".
    """
    file_path = Path(file_path_str)
    source_array = array.array('f', [1.5, 2.7, 3.14])

    try:
        # כתיבה לקובץ
        with file_path.open('wb') as f:
            source_array.tofile(f)
        print(f"המערך {source_array} נכתב לקובץ '{file_path}'.")

        # קריאה מהקובץ
        new_array = array.array('f')
        with file_path.open('rb') as f:
            # קריאת 3 איברים מטיפוס 'f' (float)
            new_array.fromfile(f, len(source_array))
        print(f"המערך {new_array} נקרא מהקובץ.")
        
        assert source_array == new_array

    finally:
        # מחיקה מובטחת של הקובץ לאחר סיום
        if file_path.exists():
            file_path.unlink()
            print(f"קובץ זמני '{file_path}' נמחק.")

# דוגמת שימוש
if __name__ == "__main__":
    work_with_binary_files()
```

---

## 🔹 טבלת השוואה: `array.array` מול `list`

| מאפיין | `array.array` | `list` |
| :--- | :--- | :--- |
| **טיפוס נתונים** | פרימיטיבים מאותו סוג (מספרים, תווים) | כל אובייקט פייתון |
| **זיכרון** | צריכה נמוכה | צריכה גבוהה |
| **ביצועים** | גבוהים בפעולות על מספרים | נמוכים יותר בפעולות על מספרים |
| **API** | סט מתודות מוגבל | API עשיר וגמיש |
| **תאימות ל-C** | גבוהה, העברת נתונים ישירה | דורש המרות |
| **סריאליזציה בינארית** | מתודות מובנות (`.tobytes`, `.tofile`) | דורש `struct`, `pickle` וכו' |

---

**מסקנה:**

🚀 השתמשו ב-`array.array` כאשר אתם עובדים עם כמות גדולה של **נתונים מספריים מאותו סוג**, וכאשר **ביצועים** ו**שימוש יעיל בזיכרון** הם קריטיים עבורכם.

לרוב המשימות היומיומיות הדורשות גמישות ואחסון נתונים מסוגים שונים, `list` נותר הבחירה הטובה ביותר.