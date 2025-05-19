"""
שירה:
=================
מורכבות: 5
-----------------
המשחק "שירה" הינו משחק בו המחשב מייצר משפטים אקראיים, באמצעות בחירה אקראית של מילים מתוך רשימות מוגדרות מראש. השחקן יכול להשפיע על תהליך היצירה על ידי הזנת קודים שונים המשנים את מקור המילים. מטרת המשחק היא לצפות ולהעריך את התוצאות האקראיות ולעיתים אבסורדיות של יצירת הביטויים.

כללי המשחק:
1.  בתחילת המשחק, המחשב מציג ברכה והוראות.
2.  המחשב בוחר מילים באופן אקראי מתוך רשימות של שמות עצם, פעלים, שמות תואר ומילות יחס.
3.  באמצעות המילים שנבחרו, המחשב מרכיב משפט אקראי.
4.  השחקן יכול להשפיע על הפלט על ידי הזנת הקודים הבאים:
    -   1: משנה את רשימת שמות העצם.
    -   2: משנה את רשימת הפעלים.
    -   3: משנה את רשימת שמות התואר.
    -   4: משנה את רשימת מילות היחס.
    -   0: מסיים את המשחק.
5.  לאחר הזנת הקוד, המחשב מחליף את הרשימה המתאימה ברשימה חדשה, ומציע ביטוי חדש שנוצר.
6.  המשחק נמשך עד שהשחקן מזין את הקוד 0.
-----------------
אלגוריתם:
1.  אתחל את רשימות שמות העצם (Nouns), הפעלים (Verbs), שמות התואר (Adjectives) ומילות היחס (Prepositions) עם ערכים התחלתיים.
2.  הצג את ברכת הפתיחה וההוראות.
3.  התחל לולאה הנמשכת עד שהשחקן יבחר באפשרות 0:
    3.1 צור מספר אקראי בין 1 ל-4.
    3.2 אם המספר שווה ל-1, צור ביטוי אקראי תוך שימוש בערכים הנוכחיים של הרשימות:
        - בחר שם עצם אקראי מרשימת שמות העצם.
        - בחר פועל אקראי מרשימת הפעלים.
        - בחר שם תואר אקראי מרשימת שמות התואר.
        - בחר מילת יחס אקראית מרשימת מילות היחס.
        - הרכב משפט והצג אותו על המסך.
        - שאל את המשתמש מה ברצונו לשנות (הזן 0 ליציאה).
    3.3 אם המספר אינו 1, בקש מהשחקן להזין קוד (0, 1, 2, 3, או 4).
    3.4 אם הקלט הוא 1, שנה את רשימת שמות העצם לרשימה חדשה.
    3.5 אם הקלט הוא 2, שנה את רשימת הפעלים לרשימה חדשה.
    3.6 אם הקלט הוא 3, שנה את רשימת שמות התואר לרשימה חדשה.
    3.7 אם הקלט הוא 4, שנה את רשימת מילות היחס לרשימה חדשה.
    3.8 אם הקלט הוא 0, סיים את המשחק.
4.  הצג את ההודעה "BYE".
5.  סיים את התוכנית.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeLists["<p align='left'>Инициализация списков:
    <code><b>
    nouns = ['BIRDS','CATS'...]
    verbs = ['FLY','RUN'...]
    adjectives = ['RED','BLUE'...]
    prepositions = ['OVER','UNDER'...]
    </b></code></p>"]
    InitializeLists --> OutputInstructions["Вывод инструкций"]
    OutputInstructions --> LoopStart{"Начало цикла: пока ввод не 0"}
    LoopStart -- Да --> GenerateRandomNumber["<code><b>randomNumber = random(1,4)</b></code>"]
    GenerateRandomNumber --> CheckRandomNumber{"Проверка: <code><b>randomNumber == 1?</b></code>"}
    CheckRandomNumber -- Да --> GeneratePhrase["<p align='left'>Генерация случайной фразы:
    <code><b>
    randomNoun = random(nouns)
    randomVerb = random(verbs)
    randomAdjective = random(adjectives)
    randomPreposition = random(prepositions)
    phrase = 'THE' + randomAdjective + randomNoun + randomVerb + randomPreposition + 'THE FOREST'
    </b></code></p>"]
    GeneratePhrase --> OutputPhrase["Вывод фразы: <code><b>phrase</b></code>"]
    OutputPhrase --> InputCode["Ввод кода пользователем: <code><b>userCode</b></code>"]
    InputCode --> CheckUserCode{"Проверка: <code><b>userCode == 0?</b></code>"}
    CheckUserCode -- Да --> OutputBye["Вывод сообщения: <b>BYE</b>"]
    OutputBye --> End["Конец"]
    CheckUserCode -- Нет --> ProcessCode["Обработка кода: <code><b>if/else</b></code>"]
    ProcessCode --> LoopStart
    CheckRandomNumber -- Нет --> InputCode2["Ввод кода пользователем: <code><b>userCode</b></code>"]
    InputCode2 --> CheckUserCode2{"Проверка: <code><b>userCode == 0?</b></code>"}
    CheckUserCode2 -- Да --> OutputBye2["Вывод сообщения: <b>BYE</b>"]
    OutputBye2 --> End
    CheckUserCode2 -- Нет --> ProcessCode2["Обработка кода: <code><b>if/else</b></code>"]
    ProcessCode2 --> LoopStart
```

מקרא:
    Start - תחילת התוכנית.
    InitializeLists - אתחול רשימות nouns, verbs, adjectives ו-prepositions עם ערכים התחלתיים.
    OutputInstructions - הצגת ההוראות למשתמש על המסך.
    LoopStart - תחילת הלולאה החוזרת על עצמה עד שהמשתמש יזין 0.
    GenerateRandomNumber - יצירת מספר אקראי בין 1 ל-4.
    CheckRandomNumber - בדיקה האם המספר האקראי שווה ל-1.
    GeneratePhrase - יצירת ביטוי אקראי המבוסס על רשימות המילים הנוכחיות.
    OutputPhrase - הצגת הביטוי שנוצר על המסך.
    InputCode - בקשת הזנת קוד מהמשתמש.
    CheckUserCode - בדיקה האם הקוד שהוזן שווה ל-0 לצורך סיום המשחק.
    OutputBye - הצגת ההודעה "BYE" לפני סיום התוכנית.
    End - סיום התוכנית.
    ProcessCode - קריאה לתהליך עיבוד הקוד, לשינוי רשימות המילים.
    InputCode2 - בקשת הזנת קוד מהמשתמש.
    CheckUserCode2 - בדיקה האם הקוד שהוזן שווה ל-0 לצורך סיום המשחק.
    OutputBye2 - הצגת ההודעה "BYE" לפני סיום התוכנית.
    ProcessCode2 - קריאה לתהליך עיבוד הקוד, לשינוי רשימות המילים.
"""
import random

# רשימות מילים התחלתיות
nouns = ["BIRDS", "CATS", "DOGS", "FISH", "TREES", "FLOWERS", "RIVERS", "MOUNTAINS", "CLOUDS", "STARS"]
verbs = ["FLY", "RUN", "SWIM", "JUMP", "GROW", "BLOOM", "FLOW", "CLIMB", "FLOAT", "SHINE"]
adjectives = ["RED", "BLUE", "GREEN", "YELLOW", "TALL", "SHORT", "BIG", "SMALL", "BRIGHT", "DARK"]
prepositions = ["OVER", "UNDER", "IN", "ON", "BY", "NEAR", "THROUGH", "AROUND", "ACROSS", "ALONG"]


def change_list(list_name):
    """פונקציה לשינוי רשימת מילים."""
    new_list = input(f"Введите новые слова для списка {list_name} через запятую: ").upper().split(",")
    return new_list


print("Добро пожаловать в игру POETRY!")
print("Нажмите:")
print("1 чтобы поменять существительные")
print("2 чтобы поменять глаголы")
print("3 чтобы поменять прилагательные")
print("4 чтобы поменять предлоги")
print("0 чтобы выйти")

while True:
    # מייצרים מספר אקראי בין 1 ל-4
    randomNumber = random.randint(1, 4)
    
    if randomNumber == 1:
       # מייצרים משפט
       random_noun = random.choice(nouns)
       random_verb = random.choice(verbs)
       random_adjective = random.choice(adjectives)
       random_preposition = random.choice(prepositions)

       phrase = f"THE {random_adjective} {random_noun} {random_verb} {random_preposition} THE FOREST"
       print(f"Случайная фраза: {phrase}")
       user_code = input("Введите код (0 для выхода): ")
       if user_code == "0":
            break
       else:
          try:
            user_code = int(user_code)
          except ValueError:
            print ("Неверный ввод, введите 0, 1, 2, 3 или 4")
            continue

    else:
       user_code = input("Введите код (0 для выхода): ")
       if user_code == "0":
            break
       else:
          try:
            user_code = int(user_code)
          except ValueError:
            print ("Неверный ввод, введите 0, 1, 2, 3 или 4")
            continue
          
    if user_code == 1:
            nouns = change_list("существительных")
    elif user_code == 2:
            verbs = change_list("глаголов")
    elif user_code == 3:
            adjectives = change_list("прилагательных")
    elif user_code == 4:
            prepositions = change_list("предлогов")
print("BYE")

"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים ובחירה של אלמנטים אקראיים מרשימה.

2.  **אתחול רשימות מילים**:
    -   `nouns = [...]`: מאתחל את רשימת שמות העצם.
    -   `verbs = [...]`: מאתחל את רשימת הפעלים.
    -   `adjectives = [...]`: מאתחל את רשימת שמות התואר.
    -   `prepositions = [...]`: מאתחל את רשימת מילות היחס.
    
3.  **פונקציה `change_list(list_name)`**:
    -   מגדירה את הפונקציה `change_list`, המאפשרת למשתמש לשנות רשימת מילים.
    -   `new_list = input(...)`: מבקשת מהמשתמש להזין מילים חדשות מופרדות בפסיקים, ממירה את הקלט לאותיות גדולות ומפצלת לרשימה.
    -   `return new_list`: מחזירה את רשימת המילים החדשה.

4.  **ברכת פתיחה והוראות**:
    -   מציגה על המסך ברכת פתיחה והוראות למשתמש.

5. **הלולאה הראשית `while True`**:
    -   לולאה אינסופית הנמשכת עד שהמשתמש יזין `0`.
    - `randomNumber = random.randint(1, 4)`: מייצרים מספר אקראי בין 1 ל-4.
    -  **תנאי יצירת הביטוי**:
      - `if randomNumber == 1`: בודקים אם המספר האקראי שווה ל-1.
      -  `random_noun = random.choice(nouns)`: בוחרים שם עצם אקראי מהרשימה.
      -  `random_verb = random.choice(verbs)`: בוחרים פועל אקראי מהרשימה.
      -  `random_adjective = random.choice(adjectives)`: בוחרים שם תואר אקראי מהרשימה.
      -  `random_preposition = random.choice(prepositions)`: בוחרים מילת יחס אקראית מהרשימה.
      -  `phrase = f"THE {random_adjective} {random_noun} {random_verb} {random_preposition} THE FOREST"`: מרכיבים ביטוי אקראי תוך שימוש במילים שנבחרו.
      -   `print(f"Случайная фраза: {phrase}")`: מציגים את הביטוי שנוצר על המסך.
      -   `user_code = input("Введите код (0 для выхода): ")`: מבקשים מהמשתמש להזין קוד לשינוי רשימת מילים.
      -   `if user_code == "0": break`: אם המשתמש מזין `0`, מסיימים את הלולאה (את המשחק).
    -  **תנאי שינוי הרשימות**:
      - `else:`: אם המספר האקראי אינו שווה ל-1, מבקשים קוד לשינוי הרשימות.
      -   `user_code = input("Введите код (0 для выхода): ")`: מבקשים מהמשתמש להזין קוד לשינוי רשימת מילים.
      -   `if user_code == "0": break`: אם המשתמש מזין `0`, מסיימים את הלולאה (את המשחק).
       - `try/except`: מטפלים בקלט שגוי.
    -  `if user_code == 1:`: אם המשתמש מזין `1`, קוראים לפונקציה `change_list` לשינוי רשימת שמות העצם.
    -   `elif user_code == 2:`: אם המשתמש מזין `2`, קוראים לפונקציה `change_list` לשינוי רשימת הפעלים.
    -   `elif user_code == 3:`: אם המשתמש מזין `3`, קוראים לפונקציה `change_list` לשינוי רשימת שמות התואר.
    -   `elif user_code == 4:`: אם המשתמש מזין `4`, קוראים לפונקציה `change_list` לשינוי רשימת מילות היחס.
   
6.  **סיום המשחק**:
    -   `print("BYE")`: מציגה את ההודעה "BYE" לאחר סיום הלולאה (כאשר המשתמש הזין 0).
"""