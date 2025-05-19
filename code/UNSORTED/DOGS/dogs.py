**DOGS:**
=================
**רמת קושי:** 5
-----------------
המשחק "כלבים" הוא משחק מבוסס טקסט, בו השחקן שולט בשני כלבים ומנסה לתפוס שני גנבים. השחקן מזין פקודות להזזת הכלבים, בעוד שהגנבים זזים באקראי. מטרת המשחק היא לתפוס את הגנבים במספר המהלכים המינימלי.
**חוקי המשחק:**
1. לשחקן מוצג שדה בגודל 10x10.
2. שני כלבים ושני גנבים ממוקמים על השדה באופן אקראי.
3. השחקן שולט בכלבים על ידי הזנת פקודות:
    - 'L' - הזזת שני הכלבים שמאלה.
    - 'R' - הזזת שני הכלבים ימינה.
    - 'U' - הזזת שני הכלבים למעלה.
    - 'D' - הזזת שני הכלבים למטה.
    - 'F' - הזזת הכלב הראשון.
    - 'S' - הזזת הכלב השני.
4. בכל מהלך, הגנבים זזים באופן אקראי.
5. מטרת המשחק היא לתפוס את הגנבים על ידי הזזת הכלבים לאותן עמדות כמו הגנבים.
6. המשחק מסתיים כאשר שני הכלבים תופסים את הגנבים.

-----------------
**אלגוריתם:**
1. אתחול שדה בגודל 10x10.
2. מיקום שני כלבים (D1 ו-D2) ושני גנבים (T1 ו-T2) בעמדות אקראיות על השדה.
3. אתחול מונה מהלכים ל-0.
4. כל עוד שני הכלבים לא תפסו את הגנבים:
    4.1 הגדלת מונה המהלכים ב-1.
    4.2 הצגת מצב השדה הנוכחי עם עמדות הכלבים והגנבים.
    4.3 בקשת הזנת פקודת הזזה מהשחקן (L, R, U, D, F, S).
    4.4 עיבוד קלט השחקן:
        - אם הפקודה היא 'L': הזזת שני הכלבים שמאלה (אם אפשרי).
        - אם הפקודה היא 'R': הזזת שני הכלבים ימינה (אם אפשרי).
        - אם הפקודה היא 'U': הזזת שני הכלבים למעלה (אם אפשרי).
        - אם הפקודה היא 'D': הזזת שני הכלבים למטה (אם אפשרי).
        - אם הפקודה היא 'F': הזזת הכלב הראשון בהתאם לקלט המשתמש (למעלה, למטה, ימינה, שמאלה).
        - אם הפקודה היא 'S': הזזת הכלב השני בהתאם לקלט המשתמש (למעלה, למטה, ימינה, שמאלה).
    4.5 הזזת הגנבים (T1 ו-T2) בכיוון אקראי.
    4.6 בדיקה האם הכלבים תפסו את הגנבים:
        - אם D1 == T1 ו-D2 == T2, הצגת הודעת ניצחון וסיום המשחק.
        - אם D1 == T2 ו-D2 == T1, הצגת הודעת ניצחון וסיום המשחק.
5. הצגת המספר הכולל של המהלכים שלקחו לתפיסת הגנבים.
-----------------
**תרשים זרימה:**
```mermaid
flowchart TD
    Start["Начало"] --> InitializeGame["Инициализация игры:<br><code><b>
    field = 10x10<br>
    dog1 = random_position<br>
    dog2 = random_position<br>
    thief1 = random_position<br>
    thief2 = random_position<br>
    moves = 0
    </b></code>"]
    InitializeGame --> LoopStart{"Начало цикла: пока воры не пойманы"}
    LoopStart -- Да --> IncreaseMoves["<code><b>moves = moves + 1</b></code>"]
    IncreaseMoves --> DisplayField["Вывод поля<br>с позициями собак<br>и воров"]
    DisplayField --> InputCommand["Ввод команды<br>игроком: <code><b>command</b></code>"]
    InputCommand --> MoveDogs{"Перемещение<br>собак в соответствии<br>с командой"}
    MoveDogs --> MoveThieves["Перемещение<br>воров случайным<br>образом"]
    MoveThieves --> CheckCatch{"Проверка:<br><code><b>dog1 == thief1 and dog2 == thief2</b></code><br>или<br><code><b>dog1 == thief2 and dog2 == thief1</b></code>"}
     CheckCatch -- Да --> OutputWin["Вывод сообщения о победе и количестве ходов"]
    OutputWin --> End["Конец"]
    CheckCatch -- Нет --> LoopStart
    LoopStart -- Нет --> End
```
**מקרא:**
   - Start - תחילת התוכנית.
   - InitializeGame - אתחול משתני המשחק: יצירת שדה המשחק, קביעת עמדות התחלה אקראיות עבור שני הכלבים ושני הגנבים, וכן אתחול מונה המהלכים.
   - LoopStart - תחילת לולאת המשחק, הנמשכת כל עוד הגנבים לא נתפסו.
   - IncreaseMoves - הגדלת מונה המהלכים.
   - DisplayField - הצגת מצב שדה המשחק הנוכחי עם עמדות הכלבים והגנבים.
   - InputCommand - קבלת פקודה מהשחקן להזזת הכלבים.
   - MoveDogs - הזזת הכלבים על שדה המשחק בהתאם לפקודה שהתקבלה.
   - MoveThieves - הזזת הגנבים באופן אקראי על שדה המשחק.
   - CheckCatch - בדיקה האם הגנבים נתפסו. התנאי מתקיים אם קואורדינטות הכלב הראשון תואמות לקואורדינטות הגנב הראשון, וקואורדינטות הכלב השני תואמות לקואורדינטות הגנב השני, או להפך.
   - OutputWin - הצגת הודעת ניצחון ומספר המהלכים שבוצעו.
   - End - סוף התוכנית.
"""

import random

# קבועים לגודל השדה
FIELD_SIZE = 10

# פונקציה ליצירת שדה המשחק
def create_field():
    """
    יוצרת שדה משחק בגודל FIELD_SIZE x FIELD_SIZE, המיוצג כרשימה של רשימות.
    """
    return [['.' for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

# פונקציה למיקום אקראי של אובייקט על השדה
def place_object(field, symbol):
  """
  ממקמת אובייקט (כלב או גנב) בעמדה אקראית פנויה על השדה.

  :param field: רשימה דו-ממדית המייצגת את שדה המשחק.
  :param symbol: סמל האובייקט שיש למקם על השדה.
  :return: טאפל המכיל את הקואורדינטות (row, col) של האובייקט הממוקם.
  """
  while True:
    row = random.randint(0, FIELD_SIZE - 1)
    col = random.randint(0, FIELD_SIZE - 1)
    if field[row][col] == '.': # בודקים שהמקום פנוי
      field[row][col] = symbol
      return row, col

# פונקציה להצגת השדה על המסך
def print_field(field):
  """
    מציגה את מצב שדה המשחק הנוכחי על המסך.

    :param field: רשימה דו-ממדית המייצגת את שדה המשחק.
    """
  for row in field:
    print(' '.join(row))


# פונקציה לעיבוד קלט פקודות המשתמש
def get_user_command():
  """
  מבקשת מהמשתמש פקודה להזזת הכלבים.
  פקודות:
    - 'L' - הזזת שני הכלבים שמאלה
    - 'R' - הזזת שני הכלבים ימינה
    - 'U' - הזזת שני הכלבים למעלה
    - 'D' - הזזת שני הכלבים למטה
    - 'F' - הזזת הכלב הראשון
    - 'S' - הזזת הכלב השני
  :return: מחרוזת - פקודת המשתמש.
  """
  while True:
        command = input("Введите команду (L/R/U/D/F/S): ").upper()
        if command in ('L', 'R', 'U', 'D', 'F', 'S'):
            return command
        else:
            print("Неверная команда. Попробуйте снова.")

# פונקציה להזזת הכלבים
def move_dogs(field, dog1, dog2, command):
    """
    מזיזה את הכלבים בהתאם לפקודת המשתמש.
    :param field: שדה המשחק
    :param dog1: קואורדינטות הכלב הראשון
    :param dog2: קואורדינטות הכלב השני
    :param command: פקודת המשתמש
    """
    dog1_row, dog1_col = dog1
    dog2_row, dog2_col = dog2
    # הזזת שני הכלבים
    if command == 'L':
        if dog1_col > 0:
           field[dog1_row][dog1_col] = '.' # מנקים את המיקום הישן
           dog1_col -= 1
        if dog2_col > 0:
           field[dog2_row][dog2_col] = '.'
           dog2_col -= 1
    elif command == 'R':
        if dog1_col < FIELD_SIZE - 1:
          field[dog1_row][dog1_col] = '.'
          dog1_col += 1
        if dog2_col < FIELD_SIZE - 1:
          field[dog2_row][dog2_col] = '.'
          dog2_col += 1
    elif command == 'U':
        if dog1_row > 0:
           field[dog1_row][dog1_col] = '.'
           dog1_row -= 1
        if dog2_row > 0:
           field[dog2_row][dog2_col] = '.'
           dog2_row -= 1
    elif command == 'D':
        if dog1_row < FIELD_SIZE - 1:
          field[dog1_row][dog1_col] = '.'
          dog1_row += 1
        if dog2_row < FIELD_SIZE - 1:
           field[dog2_row][dog2_col] = '.'
           dog2_row += 1
    # הזזת אחד הכלבים
    elif command == 'F':
      while True:
          direction = input("Введите направление для первой собаки (L/R/U/D): ").upper()
          if direction in ('L', 'R', 'U', 'D'):
              break
          else:
            print("Неверное направление. Попробуйте снова.")
      field[dog1_row][dog1_col] = '.' # מנקים את המיקום הישן
      if direction == 'L' and dog1_col > 0:
          dog1_col -= 1
      elif direction == 'R' and dog1_col < FIELD_SIZE - 1:
          dog1_col += 1
      elif direction == 'U' and dog1_row > 0:
          dog1_row -= 1
      elif direction == 'D' and dog1_row < FIELD_SIZE - 1:
          dog1_row += 1
    elif command == 'S':
      while True:
        direction = input("Введите направление для второй собаки (L/R/U/D): ").upper()
        if direction in ('L', 'R', 'U', 'D'):
            break
        else:
            print("Неверное направление. Попробуйте снова.")
      field[dog2_row][dog2_col] = '.'  # מנקים את המיקום הישן
      if direction == 'L' and dog2_col > 0:
        dog2_col -= 1
      elif direction == 'R' and dog2_col < FIELD_SIZE - 1:
        dog2_col += 1
      elif direction == 'U' and dog2_row > 0:
        dog2_row -= 1
      elif direction == 'D' and dog2_row < FIELD_SIZE - 1:
        dog2_row += 1

    field[dog1_row][dog1_col] = 'D'
    field[dog2_row][dog2_col] = 'D'
    return (dog1_row, dog1_col), (dog2_row, dog2_col)


# פונקציה להזזת הגנבים
def move_thieves(field, thief1, thief2):
  """
    מזיזה את הגנבים באופן אקראי על שדה המשחק.

    :param field: רשימה דו-ממדית המייצגת את שדה המשחק.
    :param thief1: קואורדינטות הגנב הראשון (row, col).
    :param thief2: קואורדינטות הגנב השני (row, col).
    :return: טאפלים עם הקואורדינטות החדשות של הגנבים ((row1, col1), (row2, col2)).
    """
  thief1_row, thief1_col = thief1
  thief2_row, thief2_col = thief2
  
  field[thief1_row][thief1_col] = '.'
  field[thief2_row][thief2_col] = '.'

  # הזזה אקראית של הגנב הראשון
  while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief1_row, new_thief1_col = thief1_row, thief1_col
        if direction == 'L' and thief1_col > 0:
            new_thief1_col -= 1
        elif direction == 'R' and thief1_col < FIELD_SIZE - 1:
            new_thief1_col += 1
        elif direction == 'U' and thief1_row > 0:
            new_thief1_row -= 1
        elif direction == 'D' and thief1_row < FIELD_SIZE - 1:
            new_thief1_row += 1
        
        if field[new_thief1_row][new_thief1_col] == '.' or (new_thief1_row, new_thief1_col) == (thief2_row, thief2_col):
            thief1_row, thief1_col = new_thief1_row, new_thief1_col
            break

  # הזזה אקראית של הגנב השני
  while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief2_row, new_thief2_col = thief2_row, thief2_col
        if direction == 'L' and thief2_col > 0:
            new_thief2_col -= 1
        elif direction == 'R' and thief2_col < FIELD_SIZE - 1:
            new_thief2_col += 1
        elif direction == 'U' and thief2_row > 0:
            new_thief2_row -= 1
        elif direction == 'D' and thief2_row < FIELD_SIZE - 1:
            new_thief2_row += 1
            
        if field[new_thief2_row][new_thief2_col] == '.' or (new_thief2_row, new_thief2_col) == (thief1_row, thief1_col):
            thief2_row, thief2_col = new_thief2_row, new_thief2_col
            break

  field[thief1_row][thief1_col] = 'T'
  field[thief2_row][thief2_col] = 'T'
  return (thief1_row, thief1_col), (thief2_row, thief2_col)


# פונקציה לבדיקה האם הגנבים נתפסו
def check_catch(dog1, dog2, thief1, thief2):
  """
    בודקת האם הכלבים תפסו את הגנבים. מחזירה True אם נתפסו, אחרת False.
    :param dog1: טאפל עם קואורדינטות הכלב הראשון (row, col).
    :param dog2: טאפל עם קואורדינטות הכלב השני (row, col).
    :param thief1: טאפל עם קואורדינטות הגנב הראשון (row, col).
    :param thief2: טאפל עם קואורדינטות הגנב השני (row, col).
    :return: True אם הגנבים נתפסו, False אחרת.
    """
  if (dog1 == thief1 and dog2 == thief2) or (dog1 == thief2 and dog2 == thief1):
    return True
  return False


# פונקציית המשחק הראשית
def play_dogs_game():
    """
    הפונקציה הראשית המפעילה את המשחק "כלבים".
    """
    # אתחול המשחק
    field = create_field() # יוצרים שדה ריק
    dog1 = place_object(field, 'D') # ממקמים את הכלב הראשון
    dog2 = place_object(field, 'D') # ממקמים את הכלב השני
    thief1 = place_object(field, 'T') # ממקמים את הגנב הראשון
    thief2 = place_object(field, 'T') # ממקמים את הגנב השני
    moves = 0 # מונה מהלכים

    # לולאת המשחק הראשית
    while True:
        moves += 1
        print(f"Ход: {moves}")
        print_field(field) # מציגים את מצב השדה הנוכחי
        
        command = get_user_command()
        dog1, dog2 = move_dogs(field, dog1, dog2, command)
        thief1, thief2 = move_thieves(field, thief1, thief2)

        # בודקים האם הגנבים נתפסו
        if check_catch(dog1, dog2, thief1, thief2):
            print_field(field)
            print(f"ПОЗДРАВЛЯЮ! Вы поймали воров за {moves} ходов!")
            break # מסיימים את המשחק אם הגנבים נתפסו


# התנאי `if __name__ == "__main__":`
if __name__ == "__main__":
    # מבטיח שהמשחק יופעל רק כאשר הקובץ מופעל ישירות, ולא כאשר הוא מיובא כמודול.
    # קורא לפונקציה `play_dogs_game()` להתחלת המשחק.
    play_dogs_game()

"""
**הסבר הקוד:**
1. **ייבוא מודול `random`:**
    -   `import random`: מייבאת את המודול `random` ליצירת מספרים אקראיים ובחירת הזזות אקראיות.
2. **קבוע `FIELD_SIZE`**:
    -   `FIELD_SIZE = 10`: מגדיר את גודל שדה המשחק.
3. **פונקציה `create_field()`**:
    -   יוצרת שדה משחק בגודל `FIELD_SIZE x FIELD_SIZE` ומחזירה אותו כרשימה של רשימות, המלאות בנקודות המייצגות תאים ריקים.
4. **פונקציה `place_object(field, symbol)`**:
    -   ממקמת אובייקט (`symbol`) בעמדה אקראית פנויה בתוך `field`.
    -   מחזירה את קואורדינטות האובייקט הממוקם.
5. **פונקציה `print_field(field)`**:
    -   מציגה את מצב שדה המשחק הנוכחי `field` על המסך.
6. **פונקציה `get_user_command()`**:
    -   מבקשת מהמשתמש פקודה לשליטה בכלבים (L, R, U, D, F, S).
    -   בודקת את תקינות הקלט ומחזירה את הפקודה באותיות גדולות.
7. **פונקציה `move_dogs(field, dog1, dog2, command)`**:
    -   מזיזה את הכלבים בהתאם לפקודה שהוזנה:
        -   `L`, `R`, `U`, `D` - מזיזות את שני הכלבים.
        -   `F` - מזיזה את הכלב הראשון בהתאם לקלט כיוון נוסף (L, R, U, D).
        -   `S` - מזיזה את הכלב השני בהתאם לקלט כיוון נוסף (L, R, U, D).
    -   מעדכנת את עמדות הכלבים בשדה ומחזירה את הקואורדינטות החדשות.
8. **פונקציה `move_thieves(field, thief1, thief2)`**:
    -   מזיזה את הגנבים לעמדה אקראית פנויה.
    -   מעדכנת את עמדות הגנבים בשדה ומחזירה את הקואורדינטות החדשות שלהם.
9. **פונקציה `check_catch(dog1, dog2, thief1, thief2)`**:
    -   בודקת האם הגנבים נתפסו. מחזירה `True` אם הכלב הראשון נמצא באותה עמדה כמו הגנב הראשון והכלב השני נמצא באותה עמדה כמו הגנב השני, או להפך, אחרת מחזירה `False`.
10. **פונקציה `play_dogs_game()`**:
    -   פונקציית המשחק הראשית:
        -   יוצרת את השדה, ממקמת את הכלבים והגנבים.
        -   מפעילה את לולאת המשחק, הנמשכת כל עוד הגנבים לא נתפסו.
        -   מציגה את מצב השדה הנוכחי ומבקשת פקודת משתמש.
        -   מזיזה את הכלבים והגנבים.
        -   בודקת האם הגנבים נתפסו, ומציגה הודעת ניצחון אם כן.
11. **התנאי `if __name__ == "__main__":`**:
    -   מבטיח שהמשחק יופעל רק בעת הפעלת הקובץ ישירות, ולא בעת ייבואו כמודול.
    -   קורא לפונקציה `play_dogs_game()` להתחלת המשחק.
"""