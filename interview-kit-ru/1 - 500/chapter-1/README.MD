## שאלות ראיון בפייתון

[**שאלה 1.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, רשימה (list) היא אחד ממבני הנתונים הנפוצים ביותר לשימוש, הידועה ביכולתה לאחסן רצף של אלמנטים. מה קורה כאשר משתמשים במתודה `append()` ברשימה כדי להוסיף אלמנט חדש, ולאחר מכן מנסים להשתמש במתודה `extend()` כדי להוסיף רצף אחר לאותה רשימה?

- א. המתודה `append()` תוסיף כל תו באלמנט החדש בנפרד, והמתודה `extend()` תיצור רשימה חדשה בתוך הרשימה הקיימת.
- ב. המתודה `append()` תוסיף את האלמנט החדש כאלמנט יחיד בסוף הרשימה, והמתודה `extend()` תבצע איטרציה על האלמנטים ותוסיף כל אחד מהם בנפרד לרשימה המקורית.
- ג. שתי המתודות `append()` ו-`extend()` יוסיפו את תוכנן באופן זהה, תוך יצירת רשימה מקוננת בתוך הרשימה המקורית.
- ד. המתודה `append()` מחליפה את הרשימה הקיימת, והמתודה `extend()` מנקה את הרשימה לפני הוספת הרצף החדש.

[**שאלה 2.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, לולאת `for` גמישה מאוד לביצוע איטרציה על אובייקטים שונים הניתנים לאיטרציה (iterable). נבחן מצב שבו יש לכם מילון (dictionary) עם מפתחות מסוג מחרוזת (string) וערכים מסוג מספר שלם (integer). איזו מהאפשרויות הבאות מבצעת איטרציה נכונה גם על המפתחות וגם על הערכים של מילון זה?

- A. `for key, value in dictionary.items(): print(key, value)`
- B. `for key in dictionary: print(key, dictionary[key])`
- C. `for value in dictionary.values(): print(value)`
- D. `for key in dictionary.keys(): print(key)`

[**שאלה 3.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, טווחי ראייה של משתנים (variable scopes) משחקים תפקיד חשוב בהבנה כיצד ניגשים למשתנים או משנים אותם בתוך בלוקי קוד מקוננים. אם משתנה בעל שם זהה מוגדר גם בתוך פונקציה וגם מחוצה לה, מה יקרה כאשר הפונקציה תנסה לשנות משתנה זה ללא שימוש במילת מפתח נוספת כלשהי?

- א. הפונקציה תשנה ישירות את המשתנה הגלובלי ללא כל שגיאה.
- ב. פייתון יעלה שגיאת `SyntaxError` עקב טווחי ראייה מתנגשים של משתנים.
- ג. הפונקציה תיצור משתנה לוקלי חדש בעל שם זהה למשתנה הגלובלי, ותותיר את המשתנה הגלובלי ללא שינוי.
- ד. המשתנה הגלובלי יעבור הצללה (shadowing), וערכו ישתנה רק כאשר הפונקציה תסיים את פעולתה.

[**שאלה 4.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
פייתון תומך במספר סוגי נתונים, ומחרוזות (strings) הן אחד מסוגי הנתונים הנפוצים ביותר. איזו מהדרכים הבאות נכונה לשרשור (concatenation) של שלוש מחרוזות בפייתון, תוך הבטחה שהתוצאה תהיה מחרוזת יחידה ללא רווחים נוספים ביניהן?

- A. `"Python" + "is" + "awesome"`
- B. `"Python", "is", "awesome"`
- C. `"Python" + " " + "is" + " " + "awesome"`
- D. `"Python".join(["is", "awesome"])`

[**שאלה 5.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בעת הגדרת פונקציה בפייתון, ניתן להגדיר ערכי ברירת מחדל (default values) לפרמטרים, מה שמספק גמישות רבה יותר בעת קריאה לפונקציה. מה תהיה התוצאה של קריאה לפונקציה הבאה: `def multiply(a, b=2): return a * b`, אם הפונקציה נקראת כ-`multiply(5)`?

- א. הפונקציה תחזיר 5.
- ב. הפונקציה תעלה שגיאת `TypeError` עקב ארגומנט חסר.
- ג. הפונקציה תחזיר 10, מאחר שישתמשו בערך ברירת המחדל של `b`.
- ד. הפונקציה תחזיר `None`, מאחר שסופק רק פרמטר אחד.

[**שאלה 6.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, באיזו מתודה ניתן להשתמש כדי להחליף חלקים ממחרוזת במחרוזת אחרת, ומהו התחביר (syntax) של מתודה זו, אם ברצונכם להחליף את `'cat'` ב-`'dog'` במחרוזת `s = "The cat sat on the mat"`?

- A. `s.replaceString('cat', 'dog')`
- B. `s.replace('cat', 'dog')`
- C. `s.stringReplace('cat', 'dog')`
- D. `s.replaceAll('cat', 'dog')`

[**שאלה 7.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בעת יצירת פונקציה בפייתון המחשבת את עצרת (factorial) של מספר באמצעות רקורסיה (recursion), איזו מהגדרות הפונקציה הבאות ממומשת נכון ותואמת את עקרונות הרקורסיה?

- A. `def factorial(n): return n * factorial(n-1) if n > 1 else 1`
- B. `def factorial(n): return factorial(n-1) * n if n == 0 else 1`
- C. `def factorial(n): factorial(n-1) * n`
- D. `def factorial(n): return n * factorial(n) if n > 1 else 1`

[**שאלה 8.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
איזו מהטענות הבאות אודות רשימות בפייתון היא נכונה, במיוחד כאשר מדובר על הגמישות של סוגי האלמנטים שרשימה יכולה להכיל?

- א. רשימות בפייתון יכולות להכיל רק אלמנטים מאותו סוג נתונים, כמו למשל כל המספרים השלמים או כל המחרוזות.
- ב. רשימות בפייתון יכולות להכיל אלמנטים מסוגי נתונים שונים, כגון מספרים שלמים, מחרוזות ואובייקטים, באותה רשימה.
- ג. רשימות בפייתון אינן יכולות להכיל סוגי אוספים (collections) אחרים, כגון רשימות או מילונים אחרים.
- ד. רשימות בפייתון הן בלתי ניתנות לשינוי (immutable), כלומר לאחר יצירתן לא ניתן לשנות את האלמנטים שלהן.

[**שאלה 9.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, כיצד ניתן לאחד ביעילות מספר מחרוזות המאוחסנות ברשימה בשם `strings = ["Python", "is", "awesome"]`, כדי ליצור מחרוזת יחידה `"Python is awesome"`?

- A. `" ".join(strings)`
- B. `strings.join(" ")`
- C. `concatenate(" ", strings)`
- D. `strings.concatenate(" ")`

[**שאלה 10.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
שקלו את קטע הקוד בפייתון לטיפול בחריגות (exceptions) בעת ניסיון להמיר מספר שלם מקלט של משתמש, תוך שימוש בפונקציה `input()`. איזו מהמימושים הבאים מטפל נכון בקלט שעלול להיות מספר שלם לא חוקי, כגון `'пять'`, ומציג הודעת שגיאה?

- A.
```python
try:
    num = int(input("Введите число: "))
except ValueError:
    print("Это не является действительным числом!")
```
- B.
```python
try:
    num = int(input("Введите число: "))
    if not num:
        print("Это не является действительным числом!")
```
- C.
```python
num = int(input("Введите число: "))
except ValueError:
    print("Это не является действительным числом!")
```
- D.
```python
try:
    num = int(input("Введите число: "))
catch (ValueError):
    print("Это не является действительным числом!")
```

[**שאלה 11.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, שמות משתנים רגישים לגודל אותיות (case-sensitive), מה שאומר ש-`variable` ו-`Variable` נחשבים שונים על ידי המפרש. בהתחשב במידע זה, איזו מהטענות הבאות תהיה נכונה, אם `variable` ו-`Variable` הוגדרו כמספרים שלמים בתסריט פייתון?

- א. `print(variable)` ו-`print(Variable)` יודפסו עם אותו ערך, אם לשני המשתנים יש אותו ערך.
- ב. תתרחש שגיאה, שתציין כי שמות משתנים אינם יכולים להיות דומים למעט האותיות הגדולות/קטנות שלהם.
- ג. פייתון יכתוב מחדש אוטומטית את ערך המשתנה הראשון (`variable`) עם ערך המשתנה השני (`Variable`) בכל התסריט.
- ד. לא ניתן להשתמש באותו שם עם אותיות גדולות/קטנות שונות עבור משתנים שונים באותו תסריט.

[**שאלה 12.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
פייתון תומך במספר סוגי נתונים, ומחרוזות הן מהנפוצים ביותר. בבחינת סוגי הנתונים מספר שלם (int), מספר נקודה צפה (float), ומחרוזת (str), איזה מקטעי הקוד הבאים ממיר כהלכה ייצוג מחרוזת של מספר למספר נקודה צפה ולאחר מכן מוסיף אותו למספר השלם לפני הדפסת התוצאה?

- A.
```python
str_num = "12.5"
int_num = 5
result = float(str_num) + int_num
print(result)
```
- B.
```python
str_num = "12.5"
int_num = 5
result = str_num + int_num
print(result)
```
- C.
```python
str_num = "12.5"
int_num = 5
result = int(str_num) + int_num
print(result)
```
- D.
```python
str_num = "12.5"
int_num = 5
result = float(int_num) + str_num
print(result)
```

[**שאלה 13.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בהתחשב במערכת הטיפוסים הדינמית של פייתון (dynamic typing system), איזה מקטעי הקוד הבאים מדגים את הגמישות של הקצאת טיפוסים בפייתון, המאפשרת הקצאה מחדש של משתנים לסוגי נתונים שונים בתוך אותו תסריט?

- A.
```python
x = 10
x = "hello"
print(x)
```
- B.
```python
x = 10
y : str = "hello"
print(x+y)
```
- C.
```python
x = 10
str(x) = "hello"
print(x)
```
- D.
```python
x : int = 10
x : str = "hello"
print(x)
```

[**שאלה 14.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
פונקציות בפייתון מוגדרות באמצעות מילת המפתח `def`, ואחריה שם הפונקציה וסוגריים עגולים. איזו מההגדרות הבאות כוללת פרמטר ברירת מחדל (default parameter), המאפשר קריאה לפונקציה עם פחות ארגומנטים מאשר הוגדרו פרמטרים?

- A. `def my_function(a, b): return a + b`
- B. `def my_function(a, b=10): return a + b`
- C. `def my_function(a=5, b): return a + b`
- D. `def my_function(a): return a`

[**שאלה 15.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בעת ביצוע איטרציה על רשימה בפייתון לצורך חישוב סכום אלמנטיה, איזו ממבני הלולאה הבאים מנוסח כהלכה על מנת להימנע משגיאת `IndexError` ולחשב בהצלחה את הסכום הכולל?

- A.
```python
my_list = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(my_list)):
    sum += my_list[i+1]
```
- B.
```python
my_list = [1, 2, 3, 4, 5]
sum = 0
for i in my_list:
    sum += i
```
- C.
```python
my_list = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(my_list)+1):
    sum += my_list[i]
```
- D.
```python
my_list = [1, 2, 3, 4, 5]
sum = 0
for i in range(5):
  sum += my_list[i]
```

[**שאלה 16.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מה תהיה הפלטה של קטע הקוד הבא בפייתון בעת הפעלתו?
```python
x = "Welcome to Python programming where the value of y is "
y = 5*3
print(x + str(y))
```
- A. Welcome to Python programming where the value of y is 15
- ב. שגיאה עקב סוגי נתונים לא תואמים
- C. Welcome to Python programming where the value of y is y
- ד. אף אחת מהאפשרויות לעיל

[**שאלה 17.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מה תהיה ההתנהגות של פונקציית פייתון הבאה?
```python
def check_number(n):
    if n % 2 == 0:
        return "Even"
    elif n % 3 == 0:
        return "Divisible by 3"
    else:
        return "Other"
```

- א. הפונקציה תחזיר "Even" רק אם n מתחלק גם ב-2 וגם ב-3.
- ב. הפונקציה תחזיר "Divisible by 3" עבור כל המספרים המתחלקים ב-3, ללא קשר אם הם זוגיים.
- ג. הפונקציה תחזיר "Even" עבור כל המספרים הזוגיים, ו-"Divisible by 3" עבור מספרים שאינם זוגיים אך מתחלקים ב-3.
- ד. הפונקציה אינה יכולה להחזיר "Other".

[**שאלה 18.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
נתון קוד שינוי הרשימה בפייתון הבא, מה תהיה הפלטה הסופית?
```python
numbers = [2, 4, 6, 8, 10]
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 3
print(numbers)
```

- A. `[5, 7, 9, 11, 13]`
- B. `[2, 4, 6, 8, 10]`
- C. `[3, 6, 9, 12, 15]`
- D. `[5, 7, 9, 11, 15]`

[**שאלה 19.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
שקלו את ביצוע הפעולות הבאות על מילון פייתון. מה יהיה מצב המילון `person` לאחר סיום כל הפעולות?
```python
person = {'name': 'Alice', 'age': 25, 'city': 'London'}
del person['name']
person['age'] = 26
person['city'] = 'New York'
```

- A. `{'name': 'Alice', 'age': 26, 'city': 'New York'}`
- B. `{'age': 26}`
- C. `{'age': 26, 'city': 'New York'}`
- D. `{'name': 'Alice', 'city': 'New York'}`

[**שאלה 20.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מה תהיה התוצאה של ביצוע לולאת הפייתון והאופרטורים התנאיים הבאים?
```python
result = []
for i in range(1, 11):
    if i % 2 == 0:
        result.append(f'{i} is even')
        if i % 4 == 0:
            result.append(f'{i} is divisible by 4')
    elif i%2 != 0:
        result.append(f'{i} is odd')
print(result)
```

- A. `['2 is even', '4 is divisible by 4', '6 is even', '8 is divisible by 4', '10 is even']`
- B. `['1 is odd', '2 is even', '3 is odd', '4 is divisible by 4', '5 is odd', '6 is even', '7 is odd', '8 is divisible by 4', '9 is odd', '10 is even']`
- C. `['2 is even', '4 is even', '6 is even', '8 is even', '10 is even']`
- D. `['2 is divisible by 4', '4 is divisible by 4', '6 is divisible by 4', '8 is divisible by 4', '10 is divisible by 4']`

[**שאלה 21.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בתכנות פייתון, מהי המשמעות של המתודה `__init__` במחלקה (class) ובמה היא נבדלת ממתודות אחרות שניתן להגדיר במחלקה? בפרט, הסבירו כיצד המתודה `__init__` פועלת בתכנות מונחה עצמים (object-oriented programming), כולל תפקידה ביצירת אובייקטים, והשוו זאת למתודות כגון `__str__` ופונקציות מותאמות אישית שניתן להוסיף מאוחר יותר למחלקה.

- א. המתודה `__init__` אחראית לאתחול (initialization) של אובייקטים שנוצרו זה עתה, ומתפקדת כקונסטרקטור (constructor), תוך קביעת המצב ההתחלתי או המאפיינים של המופע (instance) בעת יצירת האובייקט.
- ב. המתודה `__init__` מספקת ייצוג מחרוזתי של אובייקט, בעיקר למטרות ניפוי שגיאות (debugging), וניתן לקרוא לה ישירות על מנת לצפות במחרוזת המעוצבת.
- ג. המתודה `__init__` משמשת להגדרת האופן שבו מופעי מחלקה יודפסו בפורמט קריא למסוף (console), ולרוב נקראת בעת שימוש ב-`print()` או `str()`.
- ד. המתודה `__init__` היא מתודה הנקראת אוטומטית לאחר ביצוע כל פונקציה בתוך המחלקה, ומספקת מנגנון לניקוי משתנים שאינם בשימוש.

[**שאלה 22.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, `*args` ו-`**kwargs` משמשים לעיתים קרובות בהגדרות פונקציות להעברת מספר משתנה של ארגומנטים. כיצד בדיוק אלמנטים תחביריים (syntax elements) מיוחדים אלו מרחיבים את הפונקציונליות של פונקציית פייתון ומהי הדרך הנכונה להשתמש בהם יחד בהגדרת פונקציה כדי לשמור על תחביר נכון ולהבטיח שהפונקציה תוכל לקבל ארגומנטים מיקומיים (positional arguments) וארגומנטים עם מילות מפתח (keyword arguments) בצורה גמישה?

- א. `*args` מאפשר העברת מספר ארגומנטים עם מילות מפתח, בעוד `**kwargs` מטפל במספר ארגומנטים מיקומיים, מה שמפשט קריאות לפונקציות.
- ב. `*args` משמש להעברת מספר משתנה של ארגומנטים מיקומיים כטופל (`tuple`), ו-`**kwargs` משמש לארגומנטים משתנים עם מילות מפתח כמילון (`dictionary`), מה שמאפשר העברת ארגומנטים גמישה.
- ג. `*args` יכול לשמש להעברת כל הארגומנטים כרשימה, בעוד `**kwargs` עובד רק עם ארגומנטים מבוססי מחרוזת. סדר התחביר אינו חשוב.
- ד. `*args` דורש שכל הארגומנטים יהיו מאותו סוג נתונים, ו-`**kwargs` כופה העברת ערכים שלמים (integer) בלבד כארגומנטים עם מילות מפתח לבטיחות טיפוסים (type safety).

[**שאלה 23.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, הבנת רשימה (list comprehension) היא דרך תמציתית ליצירת רשימות. שקלו את הקוד הבא: `squared_numbers = [x**2 for x in range(10) if x % 2 == 0]`. כיצד הבנת הרשימה בדוגמה זו מושווית ליצירת רשימה מסורתית המבוססת על לולאת `for`, ומהם היתרונות בשימוש בהבנת רשימה בתכנות פייתון בעבודה עם ערכות נתונים גדולות או טרנספורמציות מורכבות?

- א. הבנת רשימה מספקת דרך פחות יעילה ליצירת רשימות בהשוואה ללולאות מסורתיות, ולעיתים קרובות מובילה לגידול מורכבות זמן (time complexity).
- ב. הבנת רשימה מציעה גישה קריאה ויעילה ליצירת רשימות בשורה אחת, מקצרת משמעותית את אורך הקוד ומשפרת את הביצועים הודות למנגנונים פנימיים אופטימליים של פייתון.
- ג. הבנת רשימה אינה יכולה לטפל בתנאים מסוג `if` והתועלת העיקרית שלה היא רק בהמרת רשימה אחת לאחרת באותו אורך ללא שינויים.
- ד. הבנת רשימה מוגבלת ליצירת רשימות מספריות ואינה יכולה לשמש למניפולציה של מחרוזות או ליצירת אובייקטים מורכבים בתוך רשימה.

[**שאלה 25.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, מילות המפתח `global` ו-`nonlocal` משרתות מטרות שונות בעת עבודה עם טווחי ראייה של משתנים. כיצד מילות מפתח אלו מתפקדות בפונקציות מקוננות (nested functions) או מודולים ומהי הדרך הנכונה להשתמש בהן לשינוי ערכים של משתנים הקיימים בטווחי ראייה שונים, כגון בתוך פונקציה חיצונית או ברמה הגלובלית של מודול?

- א. מילת המפתח `global` משמשת לשינוי משתנים בפונקציות מקוננות, בעוד שניתן להשתמש ב-`nonlocal` כדי לגשת למשתנים גלובליים ישירות מכל טווח ראייה מקונן.
- ב. מילת המפתח `global` מאפשרת שינוי משתנה ברמת המודול מתוך פונקציה, בעוד `nonlocal` מספק גישה לטווח הראייה העוטף הקרוב ביותר שאינו גלובלי, ועוזר לנהל משתנים מקוננים של פונקציה.
- ג. מילת המפתח `global` מיועדת בעיקר להכרזת קבועים (constants) במספר פונקציות, ו-`nonlocal` משמשת באופן בלעדי לשינוי משתנים ברמת המחלקה מתוך מתודות.
- ד. מילות המפתח `global` ו-`nonlocal` ניתנות להחלפה בפייתון (interchangeable), ומאפשרות שינוי של כל משתנה ללא קשר לטווח הראייה המקורי שלו.

[**שאלה 26.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מהי המשמעות של מילת המפתח `None` בפייתון?

- א. היא מציינת היעדר ערך או ערך ריק (null value) במשתנה.
- ב. זהו סוג נתונים מיוחד שניתן להקצות רק למשתני מחרוזת.
- ג. היא מייצגת ערך מספרי אפס בחישובים מספריים.
- ד. היא משמשת להגדרת לולאה אינסופית בתכנות פייתון.

[**שאלה 27.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מה תהיה הפלטה של קטע הקוד הבא בפייתון?
```python
x = 5
y = 10
print(x < y)
```

- A. Yes
- B. No
- C. True
- D. Error

[**שאלה 28.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בפייתון, מה עושה המתודה `append()` כאשר היא מופעלת על רשימה?

- א. היא ממזגת רשימה אחרת עם הרשימה הנוכחית במיקום שצוין.
- ב. היא מוסיפה אלמנט חדש לסוף הרשימה, ומגדילה את גודלה.
- ג. היא מחשבת את הסכום הכולל של כל האלמנטים המספריים ברשימה.
- ד. היא מסירה את האלמנט האחרון מהרשימה ומחזירה אותו.

[**שאלה 29.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בהינתן מילון פייתון הבא, כיצד תיגשו לערך המשויך למפתח `'color'`?
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}
```

- A. `car[1]`
- B. `car.get("color")`
- C. `car[color]`
- D. `car['color']`

[**שאלה 30.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מה עושה המתודה `split()` במחרוזות בפייתון?

- א. היא מפצלת מחרוזת לתת-מחרוזות במקומות שבהם מופיע מפריד (separator) שצוין, ומחזירה תת-מחרוזות אלו כרשימה.
- ב. היא מאחדת מספר מחרוזות למחרוזת אחת, מופרדות על ידי תו שצוין.
- ג. היא מבצעת חיפוש של תת-מחרוזת שצוינה במחרוזת ומחזירה את מיקומה.
- ד. היא מחליפה אלמנטים שצוינו במחרוזת במחרוזת חדשה.