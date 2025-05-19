SALVO:
=================
קושי: 7
-----------------
המשחק "SALVO" הוא משחק קרב ימי שבו השחקן מנסה להטביע ספינות אויב הממוקמות על רשת. השחקן מזין קואורדינטות לירי, והמשחק מודיע על פגיעה או החטאה.
מטרת המשחק היא להטביע את כל ספינות האויב במינימום מהלכים אפשרי.
המשחק מסתיים כאשר כל ספינות האויב הוטבעו.

חוקי המשחק:
1.  המשחק מתרחש על רשת בגודל 10x10.
2.  היריב ממקם ספינות (כמות וגדלים אינם מצוינים בקוד).
3.  השחקן מזין קואורדינטות (X, Y) לירי.
4.  לאחר כל ירייה, המשחק מודיע על התוצאה: "MISS", "HIT", או "SINK".
5.  המשחק מסתיים כאשר כל ספינות האויב הוטבעו.
6.  נשמר מונה של מספר היריות.

-----------------
אלגוריתם:
1. אתחול לוח המשחק (10x10).
2. מיקום ספינות האויב על הלוח (אלגוריתם המיקום אינו מצוין בקוד).
3. אתחול מונה היריות לאפס.
4. התחלת לולאה "כל עוד לא כל הספינות הוטבעו":
    4.1 בקשת קואורדינטות ירי מהשחקן (X, Y).
    4.2 הגדלת מונה היריות ב-1.
    4.3 אם הירייה פגעה בספינה:
        4.3.1 סימון התא כ-"hit".
        4.3.2 אם הספינה הוטבעה, הצגת ההודעה "SINK".
        4.3.3 אם הספינה לא הוטבעה, הצגת ההודעה "HIT".
    4.4 אם הירייה לא פגעה בספינה:
        4.4.1 הצגת ההודעה "MISS".
5. הצגת הודעת ניצחון ומספר היריות.
6. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeBoard["<p align='left'>Инициализация игрового поля:
    <code><b>board[10][10] = 0</b></code><br><code><b>ships = [x, y]...</b></code></p>"]
    InitializeBoard --> InitializeShots["<code><b>numberOfShots = 0</b></code>"]
    InitializeShots --> GameLoopStart{"Начало цикла: пока не все корабли потоплены"}
    GameLoopStart -- Да --> InputCoordinates["Ввод координат X,Y: <code><b>userX, userY</b></code>"]
    InputCoordinates --> IncreaseShots["<code><b>numberOfShots = numberOfShots + 1</b></code>"]
    IncreaseShots --> CheckHit{"Проверка: <code><b>board[userX][userY] == ship?</b></code>"}
    CheckHit -- Да --> MarkHit["Отметить клетку: <code><b>board[userX][userY] = 'hit'</b></code>"]
    MarkHit --> CheckSink{"Проверка: корабль потоплен?"}
    CheckSink -- Да --> OutputSink["Вывод сообщения: <b>SINK</b>"]
    CheckSink -- Нет --> OutputHit["Вывод сообщения: <b>HIT</b>"]
    OutputHit --> GameLoopStart
    OutputSink --> GameLoopStart
    CheckHit -- Нет --> OutputMiss["Вывод сообщения: <b>MISS</b>"]
    OutputMiss --> GameLoopStart
    GameLoopStart -- Нет --> OutputWin["Вывод сообщения: <b>YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS</b>"]
    OutputWin --> End["Конец"]

```
מקרא:
    Start - תחילת התוכנית.
    InitializeBoard - אתחול לוח המשחק בגודל 10x10 ומיקום ספינות האויב.
    InitializeShots - אתחול מונה היריות, הגדרתו ל-0.
    GameLoopStart - התחלת מחזור המשחק, שנמשך כל עוד לא הוטבעו כל ספינות האויב.
    InputCoordinates - בקשת קואורדינטות X ו-Y מהמשתמש עבור הירייה.
    IncreaseShots - הגדלת מונה היריות ב-1.
    CheckHit - בדיקה האם הירייה פגעה בספינה על לוח המשחק.
    MarkHit - סימון התא על לוח המשחק כ-"hit" אם בוצעה ירייה על ספינה.
    CheckSink - בדיקה האם הספינה שעליה בוצעה הירייה הוטבעה.
    OutputSink - הצגת ההודעה "SINK" אם הספינה הוטבעה.
    OutputHit - הצגת ההודעה "HIT" אם הירייה פגעה בספינה אך היא לא הוטבעה.
    OutputMiss - הצגת ההודעה "MISS" אם הירייה לא פגעה בספינה.
    OutputWin - הצגת הודעת הניצחון כאשר כל ספינות האויב הוטבעו, ומספר היריות.
    End - סיום התוכנית.
"""
import random

# פונקציה ליצירת לוח המשחק
def create_board(size):
    """יוצרת לוח משחק בגודל נתון, הממולא באפסים."""
    return [[0 for _ in range(size)] for _ in range(size)]

# פונקציה למיקום אקראי של ספינות (גרסה פשוטה)
def place_ships(board, ships_lengths):
    """ממקמת ספינות על לוח המשחק."""
    ships = []
    for length in ships_lengths:
        placed = False
        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board) - length)
                if all(board[row][col + i] == 0 for i in range(length)):
                     for i in range(length):
                         board[row][col + i] = 1
                     ships.append((row, col, orientation, length))
                     placed = True

            elif orientation == 'vertical':
                row = random.randint(0, len(board) - length)
                col = random.randint(0, len(board) - 1)
                if all(board[row + i][col] == 0 for i in range(length)):
                    for i in range(length):
                        board[row + i][col] = 1
                    ships.append((row, col, orientation, length))
                    placed = True

    return ships

def is_sunk(board, ship):
    # פונקציה שבודקת האם ספינה הוטבעה
    row, col, orientation, length = ship
    # פורקת את נתוני הספינה
    if orientation == 'horizontal':
      return all(board[row][col + i] == 'hit' for i in range(length))
    else:
       return all(board[row + i][col] == 'hit' for i in range(length))
    
def print_board(board):
    """מציגה את לוח המשחק בקונסולה, מסתירה את מיקום הספינות."""
    size = len(board)
    print("  " + " ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join('~' if cell == 0 or cell == 1 else cell for cell in row))

def play_salvo():
    """הפונקציה הראשית של משחק Salvo."""
    board_size = 10
    ships_lengths = [2, 3, 4, 5]
    board = create_board(board_size)
    ships = place_ships(board, ships_lengths)
    numberOfShots = 0
    sunk_ships_count = 0
    print_board(board)
    while sunk_ships_count < len(ships):
        try:
            x = int(input("הכנס קואורדינטת X (0-9): "))
            y = int(input("הכנס קואורדינטת Y (0-9): "))
            if not (0 <= x < board_size and 0 <= y < board_size):
                print("קואורדינטות שגויות. נסה שוב.")
                continue

        except ValueError:
            print("קלט שגוי. אנא הכנס מספרים בין 0 ל-9.")
            continue

        numberOfShots += 1
        if board[x][y] == 1:
            board[x][y] = 'hit'
            ship_sunk = False
            for ship in ships:
              if is_sunk(board, ship):
                  print("SINK")
                  ship_sunk = True
                  sunk_ships_count += 1
                  ships.remove(ship)
                  break
            if not ship_sunk:
              print("HIT")
        elif board[x][y] == 0:
            board[x][y] = 'miss'
            print("MISS")
        else:
           print("כבר ירית על הקואורדינטות האלו")
        
        print_board(board)


    print(f"YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS")

if __name__ == "__main__":
    play_salvo()
"""
הסבר קוד:
1.  **ייבוא מודול random**:
    - `import random`: מייבא את מודול random ליצירת מספרים אקראיים ובחירת כיוון אקראי למיקום הספינות.

2.  **פונקציה create_board(size)**:
    -   `def create_board(size):`: מגדירה פונקציה, שיוצרת לוח משחק בצורת רשימה דו-ממדית.
    -   `return [[0 for _ in range(size)] for _ in range(size)]`: מחזירה רשימה, המייצגת את לוח המשחק. כל התאים מאותחלים לערך `0`, שמשמעותו שדה ריק.

3.  **פונקציה place_ships(board, ships_lengths)**:
    - `def place_ships(board, ships_lengths)`: מגדירה פונקציה למיקום ספינות על לוח המשחק. מקבלת את לוח המשחק `board` ורשימת אורכי הספינות `ships_lengths`.
    - `ships = []`: מאתחלת רשימה לאחסון נתונים על הספינות הממוקמות.
    - `for length in ships_lengths:`: מתחילה לולאה על אורכי הספינות.
    -  `placed = False`: מאתחלת דגל לשליטה על מיקום הספינה.
    -  `while not placed:`: מתחילה לולאה, עד שהספינה תמוקם בהצלחה.
    - `orientation = random.choice(['horizontal', 'vertical'])`: בוחרת כיוון אקראי (אופקי או אנכי) למיקום הספינה.
    -  בלוקים `if orientation == 'horizontal'` ו-`elif orientation == 'vertical'` אחראים לניסיון מיקום הספינה בכיוון הנבחר.
         -  `row = random.randint(0, len(board) - 1)` ו-`col = random.randint(0, len(board) - length)`: מייצרות קואורדינטות התחלה אקראיות למיקום הספינה.
        - `all(board[row][col + i] == 0 for i in range(length))`: בודקת שכל התאים, הדרושים למיקום הספינה, פנויים.
    -   אם כל התנאים מתקיימים, הספינה ממוקמת (`board[row][col + i] = 1`) על הלוח, נתוני הספינה נשמרים ברשימה `ships`, ולולאת `while not placed` מסתיימת.
    -  `return ships`: הפונקציה מחזירה רשימה עם נתונים על הספינות הממוקמות.

4.  **פונקציה is_sunk(board, ship)**:
    - `def is_sunk(board, ship):`: פונקציה שבודקת האם ספינה הוטבעה.
    -  `row, col, orientation, length = ship`: פורקת את נתוני הספינה.
    -   בלוקים `if orientation == 'horizontal'` ו-`else` מחזירים `True`, אם כל חלקי הספינה מסומנים כ-'hit', אחרת מחזירים `False`.

5.  **פונקציה print_board(board)**:
    -   `def print_board(board):`: מגדירה פונקציה להצגת לוח המשחק בקונסולה.
    -  `print("  " + " ".join(str(i) for i in range(size)))`: מציגה את מספרי העמודות לנוחות המשתמש.
    - `print(str(i) + " " + " ".join('~' if cell == 0 or cell == 1 else cell for cell in row))`: עבור כל שורה, מציגה את מספר השורה ואת תאי לוח המשחק:
        -   `'~'` מוצג אם בתא יש `0` או `1` (תא ריק או חלק בלתי פגוע של ספינה).
        -   ערך התא מוצג אם הוא אינו `0` ואינו `1` (לדוגמה, 'hit' או 'miss').

6.  **פונקציה play_salvo()**:
    -   `def play_salvo():`: מגדירה את הפונקציה הראשית של המשחק.
    -   `board_size = 10`: מגדירה את גודל לוח המשחק.
    -  `ships_lengths = [2, 3, 4, 5]`: רשימת אורכי הספינות למיקום.
    -   `board = create_board(board_size)`: יוצרת את לוח המשחק.
    -  `ships = place_ships(board, ships_lengths)`: ממקמת את הספינות על הלוח.
    -   `numberOfShots = 0`: מאתחלת את מונה היריות.
    -   `sunk_ships_count = 0`: מאתחלת את מונה הספינות שהוטבעו.
    -   `print_board(board)`: מציגה את המצב ההתחלתי של לוח המשחק.
    -  `while sunk_ships_count < len(ships)`: מריצה את מחזור המשחק, כל עוד לא כל הספינות הוטבעו.
     -   `try...except ValueError`: מטפלת בשגיאה, אם המשתמש הכניס קלט שאינו מספרים.
    -  `x = int(input("הכנס קואורדינטת X (0-9): "))` ו-`y = int(input("הכנס קואורדינטת Y (0-9): "))` מבקשות קואורדינטות ירי.
    -   `if not (0 <= x < board_size and 0 <= y < board_size):`: בודקת שהקואורדינטות תקינות.
    -  `numberOfShots += 1`: מגדילה את מונה היריות.
        -   בלוק `if board[x][y] == 1:` מתבצע, אם הירייה פגעה בספינה.
         - `board[x][y] = 'hit'` - סימון פגיעה בספינה.
         -  עוברת על כל הספינות ובודקת, האם אחת מהן הוטבעה, באמצעות הפונקציה `is_sunk`.
          - אם ספינה הוטבעה, מוצגת הודעה, מונה הספינות שהוטבעו גדל, ונתוני הספינה שהוטבעה נמחקים מרשימת `ships`.
         -  אם הספינה לא הוטבעה, מוצגת ההודעה `HIT`.
      - `elif board[x][y] == 0:` מתבצע, אם הירייה לא פגעה בספינה.
         -  `board[x][y] = 'miss'` מסמן את התא כתא שעליו בוצעה ירייה אך לא הייתה פגיעה.
         - מציגה את ההודעה `MISS`.
      -  `else:` מתבצע, אם על קואורדינטות אלו כבר בוצעה ירייה.
    -   `print_board(board)`: מציגה את המצב הנוכחי של לוח המשחק.
    -   `print(f"YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS")`: מציגה הודעת ניצחון ומספר היריות.
7.  **הרצה מותנית**:
    -   `if __name__ == "__main__":`: בודקת שהקובץ הופעל כסקריפט ראשי.
    -   `play_salvo()`: קוראת לפונקציה להפעלת המשחק.

"""