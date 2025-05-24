MATHDI:
=================
דרגת קושי: 5
-----------------
המשחק "בעיות מתמטיות" מציע למשתמש לפתור בעיה מתמטית פשוטה (חיבור, חיסור, כפל או חילוק) ובודק את נכונות התשובה. המשחק מייצר מספרים אקראיים ופעולה אקראית.
-----------------
כללי המשחק:
1.  המחשב מייצר ביטוי מתמטי אקראי (שני מספרים אקראיים ופעולה אקראית אחת מתוך +,-,*,/).
2.  מוצע לשחקן לפתור ביטוי זה ולהזין את תשובתו.
3.  המחשב בודק האם התשובה שהשחקן נתן נכונה.
4.  אם התשובה נכונה, המשחק מודיע על כך ומסתיים.
5.  אם התשובה שגויה, המשחק מודיע שהתשובה אינה נכונה והמשחק מתחיל מחדש.
-----------------
אלגוריתם:
1.  להגדיר את דגל סיום המשחק ל-`False`.
2.  להתחיל לולאה "כל עוד המשחק לא הסתיים":
    2.1 לייצר שני מספרים שלמים אקראיים `number1` ו-`number2` בטווח 1 עד 10.
    2.2 לבחור פעולה אקראית `operation` מתוך הרשימה: "+", "-", "*", "/".
    2.3 ליצור מחרוזת ביטוי `expression` המבוססת על המספרים והפעולה שנוצרו.
    2.4 להציג למשתמש את הביטוי המתמטי.
    2.5 לקבל מהמשתמש את התשובה ולהמיר אותה למספר.
    2.6 לחשב את התוצאה הנכונה של הביטוי.
    2.7 אם תשובת המשתמש שווה לתוצאה הנכונה, להציג הודעה "CORRECT" ולהגדיר את דגל סיום המשחק ל-`True`.
    2.8 אם תשובת המשתמש אינה שווה לתוצאה הנכונה, להציג הודעה "INCORRECT. TRY AGAIN.".
3.  סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    isGameOver = False
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока <code><b>!isGameOver</b></code>"}
    LoopStart -- Да --> GenerateNumbers["<p align='left'>Генерация случайных чисел:
    <code><b>
    number1 = random(1, 10)
    number2 = random(1, 10)
    </b></code></p>"]
    GenerateNumbers --> SelectOperation["<p align='left'>Выбор случайной операции:
    <code><b>operation = random choice ['+', '-', '*', '/']</b></code></p>"]
    SelectOperation --> CreateExpression["<p align='left'>Формирование выражения:
    <code><b>expression = f'{number1} {operation} {number2}'</b></code></p>"]
    CreateExpression --> OutputExpression["Вывод выражения: <code><b>print(expression)</b></code>"]
    OutputExpression --> InputAnswer["Ввод ответа пользователем: <code><b>userAnswer</b></code>"]
    InputAnswer --> CalculateResult["<p align='left'>Вычисление правильного результата:
    <code><b>correctResult = eval(expression)</b></code></p>"]
    CalculateResult --> CheckAnswer{"Проверка: <code><b>userAnswer == correctResult?</b></code>"}
    CheckAnswer -- Да --> OutputCorrect["Вывод сообщения: <b>CORRECT</b>"]
    OutputCorrect --> SetGameOver["<code><b>isGameOver = True</b></code>"]
    SetGameOver --> LoopEnd
    CheckAnswer -- Нет --> OutputIncorrect["Вывод сообщения: <b>INCORRECT. TRY AGAIN.</b>"]
    OutputIncorrect --> LoopStart
    LoopStart -- Нет --> LoopEnd["Конец цикла: <code><b>isGameOver == True</b></code>"]
    LoopEnd --> End["Конец"]
```
**מקרא**:
    Start - תחילת התוכנית.
    InitializeVariables - אתחול המשתנה isGameOver לערך False.
    LoopStart - תחילת לולאה הנמשכת כל עוד isGameOver אינו הופך ל-True.
    GenerateNumbers - יצירת שני מספרים שלמים אקראיים number1 ו-number2 בטווח 1 עד 10.
    SelectOperation - בחירת פעולה מתמטית אקראית (חיבור, חיסור, כפל, חילוק).
    CreateExpression - יצירת הביטוי המתמטי כמחרוזת מהמספרים והפעולה שנוצרו.
    OutputExpression - הצגת הביטוי המתמטי שנוצר למשתמש.
    InputAnswer - קבלת התשובה מהמשתמש והמרתה למספר.
    CalculateResult - חישוב התוצאה הנכונה של הביטוי באמצעות הפונקציה eval().
    CheckAnswer - בדיקה האם תשובת המשתמש שווה לתוצאה הנכונה.
    OutputCorrect - הצגת ההודעה "CORRECT" אם התשובה נכונה.
    SetGameOver - הגדרת המשתנה isGameOver ל-True לסיום הלולאה.
    OutputIncorrect - הצגת ההודעה "INCORRECT. TRY AGAIN." אם התשובה שגויה.
    LoopEnd - סוף הלולאה, כאשר isGameOver הופך ל-True.
    End - סוף התוכנית.

```python
import random

# דגל לשליטה בלולאת המשחק
isGameOver = False

# לולאת המשחק הראשית
while not isGameOver:
    # מייצרים שני מספרים אקראיים מ-1 עד 10
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    
    # בוחרים פעולה אקראית
    operations = ["+", "-", "*", "/"]
    operation = random.choice(operations)
    
    # יוצרים את הביטוי המתמטי כמחרוזת
    expression = f"{number1} {operation} {number2}"
    
    # מציגים את הביטוי למשתמש
    print(f"פתור: {expression} = ?")
    
    # מקבלים את התשובה מהמשתמש
    try:
        userAnswer = float(input("תשובתך: "))
    except ValueError:
        print("קלט לא תקין. אנא הכנס מספר.")
        continue
    
    # מחשבים את התשובה הנכונה
    try:
      correctResult = eval(expression)
    except ZeroDivisionError:
      print("חילוק באפס אינו אפשרי. נסה שוב.")
      continue

    # בודקים את התשובה
    if userAnswer == correctResult:
        print("CORRECT")
        isGameOver = True  # מסיימים את המשחק אם התשובה נכונה
    else:
        print("INCORRECT. TRY AGAIN.")


"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים ובחירת פעולה אקראית.
2. **אתחול משתנה**
   - `isGameOver = False`: הדגל isGameOver מאותחל כ-False. דגל זה ישמש לשליטה בלולאת המשחק.
3.  **לולאת המשחק הראשית `while not isGameOver:`**:
    -   לולאה זו מתבצעת כל עוד הדגל `isGameOver` נשאר `False`. ברגע שתשובת המשתמש תהיה נכונה, הדגל יוגדר ל-`True`, והלולאה תסתיים.
4.  **יצירת מספרים אקראיים ופעולה**:
    -   `number1 = random.randint(1, 10)`: יוצר מספר שלם אקראי מ-1 עד 10 ושומר אותו ב-`number1`.
    -   `number2 = random.randint(1, 10)`: יוצר מספר שלם אקראי מ-1 עד 10 ושומר אותו ב-`number2`.
    -   `operations = ["+", "-", "*", "/"]`: יוצר רשימה של פעולות מתמטיות מותרות.
    -   `operation = random.choice(operations)`: בוחר פעולה אקראית מהרשימה ושומר אותה ב-`operation`.
5.  **יצירת הביטוי**:
    -   `expression = f"{number1} {operation} {number2}"`: יוצר מחרוזת המייצגת את הביטוי המתמטי, באמצעות f-string להוספת ערכי המספרים והפעולה.
6.  **הצגת הביטוי למשתמש**:
    -   `print(f"פתור: {expression} = ?")`: מציג על המסך את הביטוי המתמטי שהמשתמש צריך לפתור.
7.  **קבלת התשובה מהמשתמש**:
    -   `try...except ValueError`: מטפל בשגיאת קלט אפשרית אם המשתמש יכניס ערך שאינו מספר.
    -   `userAnswer = float(input("תשובתך: "))`: מבקש מהמשתמש את התשובה, ממיר את הקלט למספר עשרוני (כדי לאפשר קלט של מספרים לא שלמים).
8.  **חישוב התשובה הנכונה**:
      -  `try...except ZeroDivisionError`: מטפל בשגיאת חילוק באפס אפשרית
      -   `correctResult = eval(expression)`: מחשב את התוצאה הנכונה, באמצעות הפונקציה eval(). פונקציה זו מבצעת את החישוב של הביטוי המאוחסן כמחרוזת.
9.  **בדיקת תשובת המשתמש**:
    -   `if userAnswer == correctResult:`: בודק האם התשובה שהוזנה על ידי המשתמש נכונה.
    -   `print("CORRECT")`: מציג הודעה על תשובה נכונה.
    -   `isGameOver = True`: מגדיר את הדגל `isGameOver` ל-`True`, מה שמוביל לסיום לולאת המשחק הראשית.
    -   `else:`: אם התשובה שגויה.
    -   `print("INCORRECT. TRY AGAIN.")`: מציג הודעה על תשובה שגויה ומציע לנסות שוב.
"""