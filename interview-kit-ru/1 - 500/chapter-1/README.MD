## שאלות ראיון ב-Python

[**שאלה 1.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, רשימה (list) היא אחד ממבני הנתונים הנפוצים ביותר בשימוש, הידועה ביכולתה לאחסן רצף של אלמנטים. מה קורה כאשר משתמשים במתודה `append()` ברשימה כדי להוסיף אלמנט חדש, ולאחר מכן מנסים להשתמש במתודה `extend()` כדי להוסיף רצף אחר לאותה רשימה?

- A. מתודת `append()` תוסיף כל תו של האלמנט החדש בנפרד, ומתודת `extend()` תיצור רשימה חדשה בתוך הרשימה הקיימת.
- B. מתודת `append()` תוסיף את האלמנט החדש כאלמנט יחיד בסוף הרשימה, ומתודת `extend()` תעבור באיטרציה על האלמנטים ותוסיף כל אחד מהם בנפרד לרשימה המקורית.
- C. שתי המתודות `append()` ו-`extend()` יוסיפו את תוכנן באותה הצורה, ויצרו רשימה מקוננת בתוך הרשימה המקורית.
- D. מתודת `append()` מחליפה את הרשימה הקיימת, ומתודת `extend()` מנקה את הרשימה לפני הוספת הרצף החדש.

[**שאלה 2.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, לולאת `for` גמישה מאוד עבור איטרציה על אובייקטים שונים הניתנים לאיטרציה. נבחן מצב שבו יש לכם מילון עם מפתחות מסוג מחרוזת וערכים מסוג מספר שלם. איזו מהאפשרויות הבאות מבצעת איטרציה נכונה הן על המפתחות והן על הערכים של מילון זה?

- A.
```python
for key, value in dictionary.items(): print(key, value)
```
- B.
```python
for key in dictionary: print(key, dictionary[key])
```
- C.
```python
for value in dictionary.values(): print(value)
```
- D.
```python
for key in dictionary.keys(): print(key)
```

[**שאלה 3.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, תחומי הגדרה (scopes) של משתנים ממלאים תפקיד חשוב בהבנת האופן שבו משתנים נגישים או משתנים בתוך בלוקים מקוננים של קוד. אם משתנה בעל אותו שם מוגדר הן בתוך פונקציה והן מחוצה לה, מה יקרה כאשר הפונקציה תנסה לשנות משתנה זה ללא כל מילת מפתח נוספת?

- A. הפונקציה תשנה ישירות את המשתנה הגלובלי ללא כל שגיאה.
- B. Python תזרוק שגיאת `SyntaxError` עקב תחומי הגדרה מתנגשים של משתנים.
- C. הפונקציה תיצור משתנה לוקלי חדש עם אותו שם כמו המשתנה הגלובלי, ותשאיר את המשתנה הגלובלי ללא שינוי.
- D. המשתנה הגלובלי יקבל העלמה (shadowed), וערכו ישתנה רק כאשר הפונקציה תסיים את ביצועה.

[**שאלה 4.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
Python תומכת במספר טיפוסי נתונים, ומחרוזות הן אחד מטיפוסי הנתונים הנפוצים ביותר. איזו מהדרכים הבאות נכונה לשרשור שלוש מחרוזות ב-Python, באופן שמבטיח שהתוצאה תהיה מחרוזת אחת ללא רווחים נוספים ביניהן?

- A.
```python
"Python" + "is" + "awesome"
```
- B.
```python
"Python", "is", "awesome"
```
- C.
```python
"Python" + " " + "is" + " " + "awesome"
```
- D.
```python
"Python".join(["is", "awesome"])
```

[**שאלה 5.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בעת הגדרת פונקציה ב-Python ניתן להגדיר ערכי פרמטרים ברירת מחדל, מה שמאפשר גמישות רבה יותר בעת קריאה לפונקציה. מה תהיה התוצאה של קריאה לפונקציה הבאה: `def multiply(a, b=2): return a * b`, אם הפונקציה נקראת כ-`multiply(5)`?

- A. הפונקציה תחזיר 5.
- B. הפונקציה תזרוק שגיאת `TypeError` עקב חסר בארגומנט.
- C. הפונקציה תחזיר 10, מכיוון שיוגדר שימוש בערך ברירת המחדל של `b`.
- D. הפונקציה תחזיר `None`, מכיוון שסופק פרמטר אחד בלבד.

[**שאלה 6.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, איזו מתודה ניתן להשתמש בה כדי להחליף חלקים ממחרוזת במחרוזת אחרת, ומהו התחביר של מתודה זו אם ברצונכם להחליף את `'cat'` ב-`'dog'` במחרוזת `s = "The cat sat on the mat"`?

- A.
```python
s.replaceString('cat', 'dog')
```
- B.
```python
s.replace('cat', 'dog')
```
- C.
```python
s.stringReplace('cat', 'dog')
```
- D.
```python
s.replaceAll('cat', 'dog')
```

[**שאלה 7.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בעת יצירת פונקציה ב-Python שמחשבת את עצרת המספר באמצעות רקורסיה, איזו מהגדרות הפונקציה הבאות מיושמת נכונה ותואמת לעקרונות הרקורסיה?

- A.
```python
def factorial(n): return n * factorial(n-1) if n > 1 else 1
```
- B.
```python
def factorial(n): return factorial(n-1) * n if n == 0 else 1
```
- C.
```python
def factorial(n): factorial(n-1) * n
```
- D.
```python
def factorial(n): return n * factorial(n) if n > 1 else 1
```

[**שאלה 8.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, איזו מהטענות הבאות אודות רשימות Python נכונה, במיוחד כשמדובר על גמישות טיפוסי האלמנטים שרשימה יכולה להכיל?

- A. רשימות Python יכולות להכיל רק אלמנטים מאותו טיפוס נתונים, כגון כל המספרים השלמים או כל המחרוזות.
- B. רשימות Python יכולות להכיל אלמנטים מטיפוסי נתונים שונים, כגון מספרים שלמים, מחרוזות ואובייקטים, באותה רשימה.
- C. רשימות Python אינן יכולות להכיל טיפוסי אוספים אחרים, כגון רשימות או מילונים אחרים.
- D. רשימות Python הן בלתי ניתנות לשינוי (immutable), כלומר לאחר יצירתן לא ניתן לשנות את האלמנטים שלהן.

[**שאלה 9.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, כיצד ניתן לשלב ביעילות מספר מחרוזות המאוחסנות ברשימה בשם `strings = ["Python", "is", "awesome"]`, כדי ליצור מחרוזת אחת `"Python is awesome"`?

- A.
```python
" ".join(strings)
```
- B.
```python
strings.join(" ")
```
- C.
```python
concatenate(" ", strings)
```
- D.
```python
strings.concatenate(" ")
```

[**שאלה 10.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
נבחן בלוק קוד Python לטיפול בחריגים בעת ניסיון להמיר מספר שלם מקלט משתמש, תוך שימוש בפונקציה `input()`. איזו יישום מטפל נכונה בקלט שאינו יכול להיות מספר שלם תקין, לדוגמה `'пять'`, ומדפיס הודעת שגיאה?

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
ב-Python, שמות משתנים רגישים לאותיות רישיות/קטנות (case-sensitive), מה שאומר ש-`variable` ו-`Variable` נחשבים שונים על ידי המפרש. בהתחשב במידע זה, איזו מהטענות הבאות תהיה נכונה, אם `variable` ו-`Variable` הוגדרו כמספרים שלמים בתסריט Python?

- A. `print(variable)` ו-`print(Variable)` ידפיסו את אותו ערך, אם לשני המשתנים יש אותו ערך.
- B. תתרחש שגיאה המודיעה ששמות המשתנים אינם יכולים להיות דומים, למעט שינוי באותיות רישיות/קטנות.
- C. Python תחליף אוטומטית את ערך המשתנה הראשון (`variable`) בערך השני (`Variable`) בכל התסריט.
- D. לא ניתן להשתמש באותו שם עם אותיות רישיות/קטנות שונות עבור משתנים שונים באותו תסריט.

[**שאלה 12.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
Python תומכת במספר טיפוסי נתונים, ומחרוזות הן אחד מטיפוסי הנתונים הנפוצים ביותר. בבחינת טיפוסי הנתונים מספר שלם (int), מספר עשרוני (float) ומחרוזת (str), איזה מקטע קוד מבין הבאים ממיר נכונה ייצוג מחרוזתי של מספר למספר עשרוני ולאחר מכן מוסיף אותו למספר שלם לפני הדפסת התוצאה?

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
בהתחשב במערכת הטיפוסים הדינמית של Python, איזה מקטע קוד מבין הבאים מדגים את הגמישות של הקצאת טיפוסים ב-Python, המאפשרת הקצאה מחדש של משתנים לטיפוסי נתונים שונים בתוך אותו תסריט?

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
פונקציות Python מוגדרות באמצעות מילת המפתח `def`, אחריה שם הפונקציה וסוגריים. איזו מההגדרות הבאות כוללת פרמטר ברירת מחדל, המאפשר קריאה לפונקציה עם פחות ארגומנטים ממספר הפרמטרים שהוגדרו?

- A.
```python
def my_function(a, b): return a + b
```
- B.
```python
def my_function(a, b=10): return a + b
```
- C.
```python
def my_function(a=5, b): return a + b
```
- D.
```python
def my_function(a): return a
```

[**שאלה 15.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בעת ביצוע איטרציה על רשימה ב-Python לחישוב סכום האלמנטים שלה, איזו ממבני הלולאה הבאים מנוסח נכונה כדי להימנע משגיאת `IndexError` ולחשב בהצלחה את הסכום הכולל?

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
מה תהיה הפלט של מקטע קוד Python הבא בעת ביצועו?
```python
x = "Welcome to Python programming where the value of y is "
y = 5*3
print(x + str(y))
```
- A. Welcome to Python programming where the value of y is 15
- B. שגיאה עקב טיפוסי נתונים לא תואמים
- C. Welcome to Python programming where the value of y is y
- D. אף אחת מהתשובות לעיל

[**שאלה 17.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מה תהיה ההתנהגות של פונקציית Python הבאה?
```python
def check_number(n):
    if n % 2 == 0:
        return "Even"
    elif n % 3 == 0:
        return "Divisible by 3"
    else:
        return "Other"
```

- A. הפונקציה תחזיר "Even" רק אם n מתחלק ב-2 וב-3.
- B. הפונקציה תחזיר "Divisible by 3" עבור כל המספרים המתחלקים ב-3, ללא קשר אם הם זוגיים.
- C. הפונקציה תחזיר "Even" עבור כל המספרים הזוגיים, ו-"Divisible by 3" עבור מספרים שאינם זוגיים אך מתחלקים ב-3.
- D. הפונקציה אינה יכולה להחזיר "Other".

[**שאלה 18.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בהינתן קוד שינוי רשימת Python הבא, מה תהיה הפלט הסופית?
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
נבחן את ביצוע הפעולות הבאות על מילון Python. מהו מצב המילון `person` לאחר השלמת כל הפעולות?
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
מה תהיה התוצאה של ביצוע לולאת Python והתנאים הבאים?
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
בתכנות Python, מהי המשמעות של מתודת `__init__` במחלקה ובמה היא שונה ממתודות אחרות שניתן להגדיר במחלקה? בפרט, הסבירו כיצד פונקציות `__init__` פועלות בתכנות מונחה עצמים, כולל תפקידה ביצירת אובייקטים, והשוו זאת למתודות כמו `__str__` ופונקציות מוגדרות על ידי המשתמש שניתן להוסיף מאוחר יותר למחלקה.

- A. מתודת `__init__` אחראית לאתחול אובייקטים שנוצרו זה עתה, ופועלת כקונסטרקטור (constructor), הקובעת את המצב ההתחלתי או המאפיינים של המופע בעת יצירת האובייקט.
- B. מתודת `__init__` מספקת ייצוג מחרוזתי של אובייקט, בעיקר למטרות דיבוג (debugging), וניתן לקרוא לה ישירות כדי לראות את המחרוזת המעוצבת.
- C. מתודת `__init__` משמשת להגדרת האופן שבו מופעי המחלקה צריכים להיות מודפסים בפורמט קריא למשתמש בקונסולה, ולרוב נקראת בעת שימוש ב-`print()` או `str()`.
- D. מתודת `__init__` היא מתודה הנקראת אוטומטית לאחר ביצוע כל פונקציה בתוך המחלקה, המספקת מנגנון לניקוי משתנים לא בשימוש.

[**שאלה 22.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, `*args` ו-`**kwargs` משמשים לעתים קרובות בהגדרות פונקציות להעברת מספר משתנה של ארגומנטים. כיצד בדיוק אלמנטים תחביריים מיוחדים אלה מרחיבים את הפונקציונליות של פונקציית Python ומהי הדרך הנכונה להשתמש בהם יחד בהגדרת פונקציה כדי לשמור על תחביר תקין ולהבטיח שהפונקציה יכולה לקבל ארגומנטים פוזיציונליים (positional) וגם ארגומנטים מבוססי מפתח (keyword) בצורה גמישה?

- A. `*args` מאפשר להעביר מספר ארגומנטים מבוססי מפתח, בעוד ש-`**kwargs` מטפל במספר ארגומנטים פוזיציונליים, מה שמפשט קריאות לפונקציות.
- B. `*args` משמש להעברת מספר משתנה של ארגומנטים פוזיציונליים בצורת טאפל (tuple), ו-`**kwargs` משמש לארגומנטים מבוססי מפתח בצורת מילון (dictionary), מה שמאפשר קלט ארגומנטים גמיש.
- C. `*args` ניתן להשתמש בו להעברת כל הארגומנטים בצורת רשימה, בעוד ש-`**kwargs` עובד רק עם ארגומנטים מבוססי מחרוזת. סדר התחביר אינו חשוב.
- D. `*args` דורש שכל הארגומנטים יהיו מאותו טיפוס נתונים, ו-`**kwargs` אוכף העברת ערכים שלמים בלבד כארגומנטים מבוססי מפתח כדי להבטיח בטיחות טיפוסים.

[**שאלה 23.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, הבנת רשימות (list comprehension) היא דרך תמציתית ליצירת רשימות. נבחן את הקוד הבא: `squared_numbers = [x**2 for x in range(10) if x % 2 == 0]`. כיצד הבנת הרשימות בדוגמה זו משתווה ליצירת רשימה מסורתית המבוססת על לולאת `for`, ומהם היתרונות של שימוש בהבנת רשימות בתכנות Python בעת עבודה עם קבוצות נתונים גדולות או טרנספורמציות מורכבות?

- A. הבנת רשימות מספקת דרך פחות יעילה ליצירת רשימות בהשוואה ללולאות מסורתיות, ולעתים קרובות מובילה לעלייה מורכבות זמן (time complexity).
- B. הבנת רשימות מציעה גישה קריאה ויעילה ליצירת רשימות בשורה אחת, מקצרת משמעותית את אורך הקוד ומשפרת את הביצועים בזכות מנגנונים פנימיים אופטימליים של Python.
- C. הבנת רשימות אינה יכולה לטפל בתנאים מסוג `if` והיתרון העיקרי שלה הוא רק בהמרת רשימה אחת לאחרת באורך זהה ללא שינויים.
- D. הבנת רשימות מוגבלת ליצירת רשימות מספריות ואינה יכולה לשמש למניפולציה של מחרוזות או ליצירת אובייקטים מורכבים בתוך הרשימה.

[**שאלה 25.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
ב-Python, מילות המפתח `global` ו-`nonlocal` משרתות מטרות שונות בעת עבודה עם תחומי הגדרה של משתנים. כיצד מילות מפתח אלה פועלות בפונקציות מקוננות או מודולים ומהי הדרך הנכונה להשתמש בהן כדי לשנות ערכים של משתנים הקיימים בתחומי הגדרה שונים, כגון בתוך פונקציה חיצונית או ברמה הגלובלית של המודול?

- A. מילת המפתח `global` משמשת לשינוי משתנים בפונקציות מקוננות, בעוד ש-`nonlocal` יכול לשמש לגישה למשתנים גלובליים ישירות מכל תחום הגדרה מקונן.
- B. מילת המפתח `global` מאפשרת שינוי משתנה ברמת המודול מתוך פונקציה, בעוד ש-`nonlocal` מספק גישה לתחום ההגדרה העוטף הקרוב ביותר שאינו גלובלי, ומסייע בניהול משתנים מקוננים של הפונקציה.
- C. מילת המפתח `global` מיועדת בעיקר להצהרה על קבועים במספר פונקציות, ו-`nonlocal` משמש אך ורק לשינוי משתנים ברמת המחלקה מתוך מתודות.
- D. מילות המפתח `global` ו-`nonlocal` ניתנות להחלפה ב-Python, ומאפשרות לשנות כל משתנה ללא קשר לתחום ההגדרה המקורי שלו.

[**שאלה 26.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מהי המשמעות של מילת המפתח `None` ב-Python?

- A. היא מציינת היעדר ערך או ערך ריק במשתנה.
- B. זהו טיפוס נתונים מיוחד שניתן להקצות רק למשתני מחרוזת.
- C. הוא מייצג ערך מספרי אפס בחישובים מספריים.
- D. הוא משמש להגדרת לולאה אינסופית בתכנות Python.

[**שאלה 27.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מה תהיה הפלט של מקטע קוד Python הבא?
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
ב-Python, מה עושה מתודת `append()` כאשר היא מיושמת על רשימה?

- A. היא ממזגת רשימה אחרת עם הרשימה הנוכחית במיקום שצוין.
- B. היא מוסיפה אלמנט חדש לסוף הרשימה, ומגדילה את גודלה.
- C. היא מחשבת את הסכום הכולל של כל האלמנטים המספריים ברשימה.
- D. היא מסירה את האלמנט האחרון ברשימה ומחזירה אותו.

[**שאלה 29.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
בהינתן מילון Python הבא, כיצד תשיגו גישה לערך המשויך למפתח `'color'`?
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}
```

- A. `car[1]`
- B. `car.get("color")`
- C. `car[color]`
- D. `car['color']`

[**שאלה 30.**](https://github.com/hypo69/interview-kit-ru/blob/master/500/chapter-1/question_055.md)
מה עושה מתודת `split()` במחרוזות Python?

- A. מפרידה את המחרוזת לתת-מחרוזות במקומות שבהם מופיע המפריד שצוין, ומחזירה את תת-המחרוזות הללו כרשימה.
- B. מאחדת מספר מחרוזות למחרוזת אחת, המופרדת על ידי התו שצוין.
- C. מבצעת חיפוש של תת-מחרוזת שצוינה במחרוזת ומחזירה את מיקומה.
- D. מחליפה אלמנטים שצוינו במחרוזת במחרוזת חדשה.