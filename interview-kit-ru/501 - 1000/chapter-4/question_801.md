להלן תרגום המסמך מרוסית לעברית, בהתאם להנחיות:

מהו docstring?
מהו slice?
מדוע אין להשתמש ברשימה ריקה כארגומנט ברירת מחדל?
לשם מה נועדה המתודה id()?
לשם מה משמשת מילת המפתח yield?
במה שונות המתודות __iter__ ו- __next__?
לשם מה משמש המאפיין __slots__ במחלקה?
אילו מרחבי שמות קיימים בפייתון?
לשם מה נחוץ pdb?
מה תהיה התוצאה של הביטוי הבא? len(' '.join(list(map(str, [[0], [1]]))))
מתי יבוצע ענף ה-else במבנה try…except…else?
האם פייתון תומך בירושה מרובה?
כיצד ממומשים dict ו-set פנימית? מהי מורכבות קבלת אלמנט? כמה זיכרון צורכת כל מבנה נתונים?
מה יודפס כתוצאה מהרצת הקוד הבא?
```python
import sys
arr_1 = []
arr_2 = arr_1
print(sys.getrefcount(arr_1))
```
מהם דסקריפטורים (descriptors)? האם קיים הבדל בין דסקריפטור לדקורטור (decorator)?
מדוע לא כל הזיכרון משוחרר בכל פעם שפייתון מסיים ריצה?
מה יודפס כתוצאה מהרצת הקוד הבא?
```python
class Variable:

   def __init__(self, name, value):
      self._name = name
      self._value = value

   @property
   def value(self):
      print(self._name, 'GET', self._value)
      return self._value

   @value.setter
   def value(self, value):
      print(self._name, 'SET', self._value)
      self._value = value

var_1 = Variable('var_1', 'val_1')
var_2 = Variable('var_2', 'val_2')
var_1.value, var_2.value = var_2.value, var_1.value
```
מהי אינטרניזציה של מחרוזות? מדוע היא קיימת בפייתון?
מדוע אין בפייתון אופטימיזציית רקורסיה זנבית (tail call optimization)? כיצד ניתן לממש זאת?
מהם wheels ו-eggs? מה ההבדל ביניהם?
כיצד ניתן לגשת למודול שכתוב בפייתון משפת C, ולהיפך?
מהי __pycache__? מהם קבצי .pyc?