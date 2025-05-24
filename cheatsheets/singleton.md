# סינגלטון (Singleton) ב-`Python`

ב-`Python`, סינגלטון הוא תבנית עיצוב שמבטיחה שלמחלקה יהיה מופע (instance) יחיד בלבד, ומספקת נקודת גישה גלובלית למופע זה. משמעות הדבר היא שבעת ניסיון ליצור אובייקט חדש של מחלקה זו, תמיד תקבל את אותו האובייקט.

סינגלטונים שימושיים כאשר יש צורך להגביל את מספר המופעים של מחלקה, לדוגמה:

*   לניהול חיבור למסד נתונים (כדי לא לפתוח חיבורים רבים).
*   לאחסון תצורת יישום גלובלית (כדי שכל חלקי היישום ישתמשו באותה תצורה).
*   לרישום יומן (logging) (כדי שכל ההודעות יישלחו לקובץ יחיד).

להלן מספר דרכים למימוש סינגלטון ב-`Python`.

<hr>

**דרכים למימוש סינגלטון:**

1.  **באמצעות דריסת המתודה `__new__`**

    *   המתודה `__new__` אחראית ליצירת מופע של מחלקה. על ידי דריסתה, ניתן לשלוט בתהליך זה.
    *   בדוגמה זו, המופע היחיד של המחלקה יישמר במשתנה `_instance`.
    *   אם מופע עדיין לא קיים, הוא ייצור אותו, אחרת יחזיר את המופע הקיים.
    *   **`Python` Code:**

        ```python
        class Singleton:
            _instance = None  # Holds the single instance

            def __new__(cls, *args, **kwargs):
                """
                Overrides the __new__ method to control instance creation.

                Args:
                    cls: The class for which the instance is created.
                    *args: Positional arguments for the constructor.
                    **kwargs: Keyword arguments for the constructor.

                Returns:
                    The single instance of the class.
                """
                if not cls._instance: # If the instance has not been created yet
                    cls._instance = super().__new__(cls, *args, **kwargs) # Creates a new instance
                return cls._instance # Returns the existing instance

        # Example usage
        s1 = Singleton()
        s2 = Singleton()

        print(s1 is s2)  # Will print True, as it's the same object
        ```
<hr>

2.  **באמצעות דקורטור**

    *   דקורטור הוא פונקציה המבצעת שינוי על מחלקה.
    *   בדוגמה זו, תיצור פונקציית דקורטור `singleton` שמקבלת מחלקה ומחזירה את הגרסה העטופה שלה.
    *   בתוך הדקורטור, המופעים של המחלקות נשמרים במילון `instances`.
    *   אם מופע של המחלקה עדיין לא נוצר, היא תיצור אותו ותשמור אותו במילון, אחרת היא תחזיר את המופע הקיים.
    *   **`Python` Code:**

        ```python
        def singleton(cls):
            """
            Decorator for creating a singleton.

            Args:
                cls: The class to be made a singleton.

            Returns:
                The modified class which is a singleton.
            """
            instances = {} # Stores class instances

            def wrapper(*args, **kwargs):
                """
                Wrapper function that returns the single instance of the class.

                Args:
                   *args: Positional arguments for the constructor.
                   **kwargs: Keyword arguments for the constructor.

                Returns:
                    The single instance of the class.
                """
                if cls not in instances: # If the instance has not been created yet
                    instances[cls] = cls(*args, **kwargs) # Creates an instance and saves it
                return instances[cls] # Returns the existing instance
            return wrapper

        @singleton # Applies the decorator to the class
        class MyClass:
            pass

        # Example usage
        obj1 = MyClass()
        obj2 = MyClass()

        print(obj1 is obj2)  # Will print True, as it's the same object
        ```
<hr>

3.  **באמצעות מטה-מחלקה**

    *   מטה-מחלקה (metaclass) מאפשרת לשלוט ביצירת מחלקות.
    *   בדוגמה זו, תיצור מטה-מחלקה בשם `SingletonMeta` שתפקח על יצירת מופעים.
    *   המטה-מחלקה שומרת מופעים של מחלקות במילון `_instances`.
    *   בעת יצירת מופע חדש, המטה-מחלקה בודקת אם הוא כבר קיים במילון; אם לא – היא יוצרת אותו, אחרת היא מחזירה את המופע הקיים.
    *   **`Python` Code:**

        ```python
        class SingletonMeta(type):
            """
            Metaclass for creating a singleton.
            """
            _instances = {} # Stores instances

            def __call__(cls, *args, **kwargs):
                """
                Overrides the __call__ method to control instance creation.

                Args:
                    cls: The class for which the instance is created.
                    *args: Positional arguments for the constructor.
                    **kwargs: Keyword arguments for the constructor.

                Returns:
                    The single instance of the class.
                """
                if cls not in cls._instances: # If the instance has not been created yet
                    cls._instances[cls] = super().__call__(*args, **kwargs) # Creates a new instance
                return cls._instances[cls] # Returns the existing instance

        class Singleton(metaclass=SingletonMeta):
            """
            A class that is a singleton.
            """
            pass

        # Example usage
        s1 = Singleton()
        s2 = Singleton()

        print(s1 is s2)  # Will print True, as it's the same object
             ```
  <hr>

4.  **באמצעות מודול**

    *   ב-`Python`, מודול כשלעצמו הוא סינגלטון.
    *   ניתן ליצור אובייקט בתוך מודול, והוא יהיה המופע היחיד.
    *   **`Python` Code:**
        ```python
        # File singleton.py
        class Singleton:
            pass

        instance = Singleton()
        ```
        ```python
        # In another file
        from singleton import instance

        obj1 = instance
        obj2 = instance

        print(obj1 is obj2)  # Will print True, as it's the same object
        ```

**יתרונות הסינגלטון:**

*   **אחריות למופע יחיד:** סינגלטון מבטיח שלמחלקה יהיה רק מופע אחד. זה שימושי לניהול משאבים שחייבים להיות ייחודיים.
*   **גישה גלובלית:** סינגלטון מספק נקודת גישה גלובלית למופע של המחלקה, מה שמפשט את השימוש במופע זה בכל חלק של התוכנית.

**חסרונות הסינגלטון:**

*   **מצב גלובלי:** סינגלטון עלול להוביל לשימוש במצב גלובלי, דבר שיכול לגרום לתופעות לוואי בלתי צפויות ולהקשות על הבדיקה.
*   **הפרת עקרונות תכנות מונחה עצמים:** סינגלטון יכול להפר את עקרון האחריות היחידה ואת עיקרון האכפוס (encapsulation).

**מתי להשתמש בסינגלטון?**

*   כאשר אתה זקוק שאובייקט יתקיים במופע יחיד (לדוגמה, תצורה, רשם יומן, חיבור למסד נתונים).
*   כאשר אתה דורש גישה גלובלית לאובייקט זה.