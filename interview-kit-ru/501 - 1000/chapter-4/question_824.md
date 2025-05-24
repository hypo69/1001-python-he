בסדר גמור, להלן תרגום המסמך לעברית בהתאם להנחיות:

### `question_279_interview.md`

**שאלה 279.** מה יודפס למסך כתוצאה מהרצת קוד Python הבא?

```python
class student:
    'Base class for all students'
    def __init__(self, roll_no, grade):
        self.roll_no = roll_no
        self.grade = grade

    def display(self):
        print("Roll no : ", self.roll_no, ", Grade: ", self.grade)

print(student.__doc__)
```

A.  תיזרק חריגה
B.  `__main__`
C.  שום דבר לא יודפס
D.  `Base class for all students`

**תשובה נכונה: D**

**הסבר:**

קוד זה מדגים את השימוש במאפיין `__doc__`, המשמש לגישה למחרוזות תיעוד (docstrings) של אובייקט. Docstring היא מחרוזת המופיעה מיד לאחר הגדרת מודול, מחלקה, פונקציה או מתודה, ומשמשת לתיאור מטרתם.

1.  **`class student:`**:
    *   מוגדרת המחלקה `student`.
    *   המחרוזת `'Base class for all students'` היא ה-docstring של מחלקה זו.
2.  **`print(student.__doc__)`**:
    *   המאפיין `__doc__` משמש לגישה ל-docstring של מחלקה, מודול או פונקציה.
    *   במקרה זה, `student.__doc__` מחזיר את ה-docstring שהוגדר עבור המחלקה `student`.
    *   פונקציית ה-`print` מדפיסה docstring זה למסך.

*   **אפשרות A אינה נכונה:** הקוד אינו מכיל שגיאות שיגרמו לזריקת חריגה.
*   **אפשרות B אינה נכונה:** `__main__` הוא שם המודול בעת הרצת קוד ישירות, אך אינו docstring.
*   **אפשרות C אינה נכונה:** הקוד ידפיס את ה-docstring של המחלקה student.
*   **אפשרות D נכונה:** ה-docstring של המחלקה `student` יודפס למסך.

**כיצד פועלים docstrings והמאפיין `__doc__`:**

1.  Docstrings הן מחרוזות שניתן להוסיף בתחילת מודול, מחלקה, פונקציה או מתודה.
2.  Docstrings משמשות לתיעוד קוד.
3.  ניתן לקבל docstring באמצעות המאפיין `__doc__` או באמצעות הפונקציה המובנית `help()`.

**כתוצאה מכך:**

ה-docstring של המחלקה `student`, שהוקצה לה בעת הגדרת המחלקה והוא המחרוזת `Base class for all students`, יודפס למסך.

לפיכך, אפשרות D היא הנכונה.