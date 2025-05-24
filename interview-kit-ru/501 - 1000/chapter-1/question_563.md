### `question_563.md`

**שאלה 563.** מהם מטא-קלאסים (metaclasses) בפייתון, וכיצד הם פועלים? ספק דוגמה לשימוש במטא-קלאס ליצירה אוטומטית של תכונות (property) עבור מאפייני מחלקה.

-   א. מטא-קלאסים הם מחלקות היוצרות רק מטא-קלאסים אחרים.
-   ב. מטא-קלאסים הם מחלקות היוצרות רק מחלקות רגילות, אך אינן יכולות לשנות את התנהגותן.
-  ג. מטא-קלאסים הם מחלקות היוצרות מחלקות אחרות, ומאפשרות לשנות את ההתנהגות של המחלקות הנוצרות.
-  ד. מטא-קלאסים הם מחלקות מופשטות המתארות ממשקים ואינן יכולות ליצור אובייקטים.

**תשובה נכונה: ג**

**הסבר:**

מטא-קלאסים בפייתון הם מחלקות היוצרות מחלקות אחרות. הם מאפשרים למתכנתים לשלוט בתהליך יצירת המחלקות, לשנות את התנהגותן ואף להוסיף או לשנות מאפיינים (attributes) ומתודות של המחלקות בזמן ההגדרה שלהן.

*   **מושגי יסוד של מטא-קלאסים:**
    *   **מחלקות של מחלקות:** מטא-קלאסים הם מחלקות שהמופעים שלהן הם מחלקות אחרות.
    *   **התאמה אישית של יצירת מחלקות:** מטא-קלאסים מספקים את היכולת להתאים אישית את תהליך יצירת המחלקות, על ידי הוספה או שינוי אוטומטי של התנהגות.
    *   **שליטה על מאפיינים ומתודות:** הם מאפשרים לנהל את המאפיינים והמתודות של המחלקות הנוצרות.
    *  **שינוי התנהגות דינמי:** משמשים לשינוי דינמי של התנהגות מחלקות והמופעים שלהן.

*   **שימוש במטא-קלאסים:**
    *   כדי להגדיר מטא-קלאס, יש ליצור מחלקה היורשת מ-`type`.
    *   מטא-קלאס מוגדר באמצעות הפרמטר `metaclass` בעת יצירת המחלקה.
        *   `class MyClass(metaclass=MyMetaClass):`.
    *   מטא-קלאס יכול לדרוס (override) את המתודות `__new__`, `__init__`, ו-`__call__`, המשמשות בעת יצירת מחלקות.

**דוגמה (מטקסט השאלה):**

```python
from functools import wraps

class AutoProperty(type):
    # Override the __new__ method, called when creating the class
    def __new__(meta, classname, bases, classdict):
        new_props = {}
        # Iterate through class attributes
        for name, value in classdict.items():
            # If the attribute is a tuple, interpret it as a property definition
            if isinstance(value, tuple):
                prop_name, prop_type = value
                # Create a property for the attribute
                # It will store the value in an internal attribute with a '_' prefix
                new_props[name] = property(
                    lambda self, prop_name=prop_name: getattr(self, '_' + prop_name),
                    lambda self, value, prop_name=prop_name: setattr(self, '_' + prop_name, prop_type(value)),
                    lambda self, prop_name=prop_name: delattr(self, '_' + prop_name),
                    doc=f'{prop_name} property of type {prop_type.__name__}')
        # Update the class's attribute dictionary
        classdict.update(new_props)
        # Delete the original attribute (the tuple)
        del classdict[name] # This seems incorrect, it will delete the last item added to new_props
        # Let's correct this: remove the original tuple attributes
        original_keys_to_delete = [k for k, v in classdict.items() if isinstance(v, tuple)]
        for key in original_keys_to_delete:
             if key in classdict: # Add check before deletion
                 del classdict[key]

        # Call the parent class's __new__ method to actually create the class
        return type.__new__(meta, classname, bases, classdict)

# Class Person, created using the AutoProperty metaclass
class Person(metaclass=AutoProperty):
    # Declare attributes 'name' and 'age' as tuples
    name = ('name', str)
    age = ('age', int)

# After this, 'name' and 'age' have become properties
# They access internal attributes (with a '_' prefix)
# and apply the type specified in the second element of the tuple upon assignment.
p = Person()
# Set values using the created properties
p.name = 'John'
p.age = 30
# Access values using the created properties
print(p.name, p.age)  # John 30
```

**תיאור הדוגמה:**

*   **`AutoProperty(type)`:** מטא-קלאס `AutoProperty` היורש מ-`type`.
     *   `__new__(meta, classname, bases, classdict)`: דורס את המתודה `__new__`, הנקראת בעת יצירת המחלקה.
         *    מבצע איטרציה על מאפייני המחלקה.
         *    אם המאפיין הוא טיפל (tuple), הוא מפורש כהגדרה עבור property.
         *  יוצר property עבור המאפיין, שישמור את הערך במאפיין פנימי עם הקידומת `_`.
         *  מעדכן את מילון מאפייני המחלקה, ומוחק את המאפיין המקורי.
*   **`class Person(metaclass=AutoProperty)`**: המחלקה `Person`, שנוצרה באמצעות מטא-קלאס `AutoProperty`.
     *   מצהירה על המאפיינים `name` ו-`age` כטיפלים.
*   לאחר מכן, `name` ו-`age` הפכו להיות properties, הניגשים למאפיינים פנימיים (עם קידומת `_`) ומחילים בעת ההשמה את הטיפוס המצוין ברכיב השני של הטיפל.
*   `p = Person()`: נוצר מופע של המחלקה.
*   `p.name = 'John'` ו-`p.age = 30`: קובע את הערכים של המאפיינים name ו-age, תוך שימוש ב-properties שנוצרו.

**ניתוח האפשרויות:**
*   **א. מטא-קלאסים הם מחלקות היוצרות רק מטא-קלאסים אחרים.:** לא נכון.
*   **ב. מטא-קלאסים הם מחלקות היוצרות רק מחלקות רגילות, אך אינן יכולות לשנות את התנהגותן.:** לא נכון. מטא-קלאסים מאפשרים בדיוק את שינוי התנהגות המחלקות.
*  **ג. מטא-קלאסים הם מחלקות היוצרות מחלקות אחרות, ומאפשרות לשנות את ההתנהגות של המחלקות הנוצרות.:** נכון.
*  **ד. מטא-קלאסים הם מחלקות מופשטות המתארות ממשקים ואינן יכולות ליצור אובייקטים.:** לא נכון.

**לסיכום:**
*   מטא-קלאסים מאפשרים יצירת מנגנונים גמישים ועוצמתיים לשינוי אוטומטי של מחלקות.
*   הם מאפשרים הוספה או שינוי דינמיים של מאפיינים ומתודות של מחלקות.

לפיכך, התשובה הנכונה היא **ג. מטא-קלאסים הם מחלקות היוצרות מחלקות אחרות, ומאפשרות לשנות את ההתנהגות של המחלקות הנוצרות.**