"""
סאלוו (SALVO):
=================
מורכבות: 7
-----------------
המשחק "סאלוו" (SALVO) הוא משחק מסוג קרב ימי, שבו השחקן מנסה להטביע את ספינות האויב הממוקמות על רשת. השחקן מזין קואורדינטות לירי, והמשחק מדווח על פגיעה או החטאה.
מטרת המשחק היא להטביע את כל ספינות האויב במספר מינימלי של מהלכים.
המשחק מסתיים כאשר כל ספינות האויב מוטבעות.

כללי המשחק:
1.  המשחק מתרחש על רשת בגודל 10x10.
2.  האויב ממקם את הספינות (כמות וגדלים אינם מצוינים בקוד).
3.  השחקן מזין קואורדינטות (X, Y) לירי.
4.  לאחר כל ירי, המשחק מדווח על התוצאה: "MISS", "HIT", או "SINK".
5.  המשחק מסתיים כאשר כל ספינות האויב מוטבעות.
6.  נשמר מונה של מספר היריות.

-----------------
אלגוריתם:
1.  אתחול לוח המשחק (10x10).
2.  מיקום ספינות האויב על הלוח (אלגוריתם המיקום אינו מצוין בקוד).
3.  אתחול מונה היריות לאפס.
4.  התחלת לולאה "כל עוד לא כל הספינות הוטבעו":
    4.1 בקשת קואורדינטות ירי (X, Y) מהשחקן.
    4.2 הגדלת מונה היריות ב-1.
    4.3 אם הירי פגע בספינה, אז:
        4.3.1 סימון התא כ-"hit".
        4.3.2 אם הספינה הוטבעה, אז הצגת ההודעה "SINK".
        4.3.3 אם הספינה לא הוטבעה, הצגת ההודעה "HIT".
    4.4 אם הירי לא פגע בספינה, אז:
        4.4.1 הצגת ההודעה "MISS".
5.  הצגת הודעת ניצחון ומספר היריות.
6.  סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["<p align='left'>אתחול לוח המשחק:
    <code><b>board[10][10] = 0</b></code><br><code><b>ships = [x, y]...</b></code></p>"]
    InitializeBoard --> InitializeShots["<code><b>numberOfShots = 0</b></code>"]
    InitializeShots --> GameLoopStart{"התחלת לולאה: כל עוד לא כל הספינות הוטבעו"}
    GameLoopStart -- Да --> InputCoordinates["הזנת קואורדינטות X,Y: <code><b>userX, userY</b></code>"]
    InputCoordinates --> IncreaseShots["<code><b>numberOfShots = numberOfShots + 1</b></code>"]
    IncreaseShots --> CheckHit{"בדיקה: <code><b>board[userX][userY] == ship?</b></code>"}
    CheckHit -- Да --> MarkHit["סימון תא: <code><b>board[userX][userY] = 'hit'</b></code>"]
    MarkHit --> CheckSink{"בדיקה: האם הספינה הוטבעה?"}
    CheckSink -- Да --> OutputSink["הצגת הודעה: <b>SINK</b>"]
    CheckSink -- Нет --> OutputHit["הצגת הודעה: <b>HIT</b>"]
    OutputHit --> GameLoopStart
    OutputSink --> GameLoopStart
    CheckHit -- Нет --> OutputMiss["הצגת הודעה: <b>MISS</b>"]
    OutputMiss --> GameLoopStart
    GameLoopStart -- Нет --> OutputWin["הצגת הודעה: <b>YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS</b>"]
    OutputWin --> End["סיום"]

```
מקרא:
    Start - התחלת התוכנית.
    InitializeBoard - אתחול לוח המשחק בגודל 10x10 ומיקום ספינות האויב.
    InitializeShots - אתחול מונה היריות, והגדרתו ל-0.
    GameLoopStart - התחלת לולאת המשחק, הנמשכת כל עוד לא כל ספינות האויב הוטבעו.
    InputCoordinates - בקשת קלט מהמשתמש עבור קואורדינטות X ו-Y לירי.
    IncreaseShots - הגדלת מונה היריות ב-1.
    CheckHit - בדיקה האם הירי פגע בספינה על לוח המשחק.
    MarkHit - סימון התא על לוח המשחק כ-"hit" אם בוצע ירי על ספינה.
    CheckSink - בדיקה האם הספינה שנפגעה מהירי הוטבעה.
    OutputSink - הצגת ההודעה "SINK" אם הספינה הוטבעה.
    OutputHit - הצגת ההודעה "HIT" אם הירי פגע בספינה אך היא לא הוטבעה.
    OutputMiss - הצגת ההודעה "MISS" אם הירי לא פגע בספינה.
    OutputWin - הצגת הודעת הניצחון, כאשר כל ספינות האויב הוטבעו, ומספר היריות הכולל.
    End - סיום התוכנית.
"""
import random

# פונקציה ליצירת לוח המשחק
def create_board(size):
    """יוצרת לוח משחק בגודל נתון, המאופס באפסים."""
    return [[0 for _ in range(size)] for _ in range(size)]

# פונקציה למיקום ספינות באופן אקראי (גרסה פשוטה)
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
    """פונקציה הבודקת האם הספינה הוטבעה"""
    row, col, orientation, length = ship
    if orientation == 'horizontal':
      return all(board[row][col + i] == 'hit' for i in range(length))
    else:
       return all(board[row + i][col] == 'hit' for i in range(length))

def print_board(board):
    """מציגה את לוח המשחק בקונסולה, תוך הסתרת מיקום הספינות."""
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
            x = int(input("Введите координату X (0-9): "))
            y = int(input("Введите координату Y (0-9): "))
            if not (0 <= x < board_size and 0 <= y < board_size):
                print("Неверные координаты. Попробуйте снова.")
                continue

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числа от 0 до 9.")
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
           print("Вы уже стреляли по этим координатам")

        print_board(board)


    print(f"YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS")

# הפעלה מותנית
if __name__ == "__main__":
    play_salvo()
"""
הסבר קוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random` לצורך יצירת מספרים אקראיים ובחירת כיוון אקראי למיקום הספינות.

2.  **פונקציה `create_board(size)`**:
    -   `def create_board(size):`: מגדירה פונקציה היוצרת לוח משחק כרשימה דו-ממדית.
    -   `return [[0 for _ in range(size)] for _ in range(size)]`: מחזירה רשימה המייצגת את לוח המשחק. כל התאים מאותחלים בערך `0`, המסמל תא ריק.

3.  **פונקציה `place_ships(board, ships_lengths)`**:
    -   `def place_ships(board, ships_lengths)`: מגדירה פונקציה למיקום ספינות על לוח המשחק. מקבלת את לוח המשחק `board` ורשימת אורכי ספינות `ships_lengths`.
    -   `ships = []`: מאתחלת רשימה לאחסון נתונים על הספינות שמוקמו.
    -   `for length in ships_lengths:`: מתחילה לולאה על אורכי הספינות.
    -    `placed = False`: מאתחל דגל לבקרת מיקום הספינה.
    -    `while not placed:`: מתחילה לולאה כל עוד הספינה טרם מוקמה בהצלחה.
    -   `orientation = random.choice(['horizontal', 'vertical'])`: בוחר כיוון אקראי (אופקי או אנכי) למיקום הספינה.
    -    בלוקי `if orientation == 'horizontal'` ו-`elif orientation == 'vertical'` אחראים לניסיון מיקום הספינה בכיוון הנבחר.
         -    `row = random.randint(0, len(board) - 1)` ו-`col = random.randint(0, len(board) - length)`: נוצרות קואורדינטות התחלה אקראיות למיקום הספינה.
        -   `all(board[row][col + i] == 0 for i in range(length))`: נבדק שכל התאים הדרושים למיקום הספינה פנויים.
    -   אם כל התנאים מתקיימים, הספינה ממוקמת (`board[row][col + i] = 1`)  על הלוח, נתוני הספינה נשמרים ברשימה `ships`, ולולאת `while not placed` מסתיימת.
    -    `return ships`: הפונקציה מחזירה את הרשימה עם נתוני הספינות שמוקמו.

4.  **פונקציה `is_sunk(board, ship)`**:
    -   `def is_sunk(board, ship):`: פונקציה הבודקת האם הספינה הוטבעה.
    -    `row, col, orientation, length = ship`: פורקת את נתוני הספינה.
    -    בלוקי `if orientation == 'horizontal'` ו-`else` מחזירים  `True`, אם כל חלקי הספינה מסומנים כ-'hit', אחרת מחזירים `False`.

5.  **פונקציה `print_board(board)`**:
    -   `def print_board(board):`: מגדירה פונקציה להצגת לוח המשחק בקונסולה.
    -    `print("  " + " ".join(str(i) for i in range(size)))`: מציגה את מספרי העמודות לנוחות המשתמש.
    -   `print(str(i) + " " + " ".join('~' if cell == 0 or cell == 1 else cell for cell in row))`: עבור כל שורה, מציגה את מספר השורה ותאי לוח המשחק:
        -   `'~'` מוצג אם בתא נמצא `0` או `1` (תא ריק או חלק לא פגוע של ספינה).
        -   ערך התא מוצג אם הוא אינו `0` ואינו `1` (לדוגמה, 'hit' או 'miss').

6.  **פונקציה `play_salvo()`**:
    -   `def play_salvo():`: מגדירה את הפונקציה הראשית של המשחק.
    -   `board_size = 10`: מגדירה את גודל לוח המשחק.
    -    `ships_lengths = [2, 3, 4, 5]`: רשימת אורכי הספינות למיקום.
    -   `board = create_board(board_size)`: יוצרת את לוח המשחק.
    -    `ships = place_ships(board, ships_lengths)`: ממקמת את הספינות על הלוח.
    -   `numberOfShots = 0`: מאתחלת את מונה היריות.
    -   `sunk_ships_count = 0`: מאתחלת את מונה הספינות שהוטבעו.
    -   `print_board(board)`: מציגה את המצב ההתחלתי של לוח המשחק.
    -    `while sunk_ships_count < len(ships)`: מריצה את לולאת המשחק כל עוד לא כל הספינות הוטבעו.
     -   `try...except ValueError`: מטפלת בשגיאה אם המשתמש הזין קלט שאינו מספר.
    -    `x = int(input("Введите координату X (0-9): "))` ו- `y = int(input("Введите координату Y (0-9): "))`  מבקשים את קואורדינטות הירי.
    -   `if not (0 <= x < board_size and 0 <= y < board_size):`: בודק שהקואורדינטות תקינות.
    -    `numberOfShots += 1`: מגדיל את מונה היריות.
        -   בלוק `if board[x][y] == 1:` מבוצע אם הירי פגע בספינה.
         - `board[x][y] = 'hit'` - סימון פגיעה בספינה.
         -  עובר על כל הספינות ובודק האם מי מהן הוטבעה, באמצעות הפונקציה `is_sunk`.
          - אם הספינה הוטבעה, אז מציג הודעה, מגדיל את מונה הספינות שהוטבעו ומוחק את נתוני הספינה שהוטבעה מרשימת `ships`.
         -  אם הספינה לא הוטבעה, אז מציג את ההודעה `HIT`.
      - `elif board[x][y] == 0:` מבוצע אם הירי לא פגע בספינה.
         -  `board[x][y] = 'miss'` מסמן את התא כתא שבו בוצע ירי אך לא הייתה פגיעה.
         - מציג את ההודעה `MISS`.
      -  `else:` מבוצע אם בוצע ירי על קואורדינטות אלו כבר קודם.
    -   `print_board(board)`: מציג את המצב הנוכחי של לוח המשחק.
    -   `print(f"YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS")`: מציג הודעת ניצחון ומספר היריות.
7.  **הפעלה מותנית**:
    -   `if __name__ == "__main__":`: בודק האם הקובץ הופעל כסקריפט הראשי.
    -   `play_salvo()`: קורא לפונקציה להפעלת המשחק.

"""
"""
הסבר קוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random` לצורך יצירת מספרים אקראיים ובחירת כיוון אקראי למיקום הספינות.

2.  **פונקציה `create_board(size)`**:
    -   `def create_board(size):`: מגדירה פונקציה היוצרת לוח משחק כרשימה דו-ממדית.
    -   `return [[0 for _ in range(size)] for _ in range(size)]`: מחזירה רשימה המייצגת את לוח המשחק. כל התאים מאותחלים בערך `0`, המסמל תא ריק.

3.  **פונקציה `place_ships(board, ships_lengths)`**:
    -   `def place_ships(board, ships_lengths)`: מגדירה פונקציה למיקום ספינות על לוח המשחק. מקבלת את לוח המשחק `board` ורשימת אורכי ספינות `ships_lengths`.
    -   `ships = []`: מאתחלת רשימה לאחסון נתונים על הספינות שמוקמו.
    -   `for length in ships_lengths:`: מתחילה לולאה על אורכי הספינות.
    -    `placed = False`: מאתחל דגל לבקרת מיקום הספינה.
    -    `while not placed:`: מתחילה לולאה כל עוד הספינה טרם מוקמה בהצלחה.
    -   `orientation = random.choice(['horizontal', 'vertical'])`: בוחר כיוון אקראי (אופקי או אנכי) למיקום הספינה.
    -    בלוקי `if orientation == 'horizontal'` ו-`elif orientation == 'vertical'` אחראים לניסיון מיקום הספינה בכיוון הנבחר.
         -    `row = random.randint(0, len(board) - 1)` ו-`col = random.randint(0, len(board) - length)`: נוצרות קואורדינטות התחלה אקראיות למיקום הספינה.
        -   `all(board[row][col + i] == 0 for i in range(length))`: נבדק שכל התאים הדרושים למיקום הספינה פנויים.
    -   אם כל התנאים מתקיימים, הספינה ממוקמת (`board[row][col + i] = 1`) על הלוח, נתוני הספינה נשמרים ברשימה `ships`, ולולאת `while not placed` מסתיימת.
    -    `return ships`: הפונקציה מחזירה את הרשימה עם נתוני הספינות שמוקמו.

4.  **פונקציה `is_sunk(board, ship)`**:
    -   `def is_sunk(board, ship):`: פונקציה הבודקת האם הספינה הוטבעה.
    -    `row, col, orientation, length = ship`: פורקת את נתוני הספינה.
    -    בלוקי `if orientation == 'horizontal'` ו-`else` מחזירים  `True`, אם כל חלקי הספינה מסומנים כ-'hit', אחרת מחזירים `False`.

5.  **פונקציה `print_board(board)`**:
    -   `def print_board(board):`: מגדירה פונקציה להצגת לוח המשחק בקונסולה.
    -    `print("  " + " ".join(str(i) for i in range(size)))`: מציגה את מספרי העמודות לנוחות המשתמש.
    -   `print(str(i) + " " + " ".join('~' if cell == 0 or cell == 1 else cell for cell in row))`: עבור כל שורה, מציגה את מספר השורה ותאי לוח המשחק:
        -   `'~'` מוצג אם בתא נמצא `0` או `1` (תא ריק או חלק לא פגוע של ספינה).
        -   ערך התא מוצג אם הוא אינו `0` ואינו `1` (לדוגמה, 'hit' או 'miss').

6.  **פונקציה `play_salvo()`**:
    -   `def play_salvo():`: מגדירה את הפונקציה הראשית של המשחק.
    -   `board_size = 10`: מגדירה את גודל לוח המשחק.
    -    `ships_lengths = [2, 3, 4, 5]`: רשימת אורכי הספינות למיקום.
    -   `board = create_board(board_size)`: יוצרת את לוח המשחק.
    -    `ships = place_ships(board, ships_lengths)`: ממקמת את הספינות על הלוח.
    -   `numberOfShots = 0`: מאתחלת את מונה היריות.
    -   `sunk_ships_count = 0`: מאתחלת את מונה הספינות שהוטבעו.
    -   `print_board(board)`: מציגה את המצב ההתחלתי של לוח המשחק.
    -    `while sunk_ships_count < len(ships)`: מריצה את לולאת המשחק כל עוד לא כל הספינות הוטבעו.
     -   `try...except ValueError`: מטפלת בשגיאה אם המשתמש הזין קלט שאינו מספר.
    -    `x = int(input("Введите координату X (0-9): "))` ו- `y = int(input("Введите координату Y (0-9): "))`  מבקשים את קואורדינטות הירי.
    -   `if not (0 <= x < board_size and 0 <= y < board_size):`: בודק שהקואורדינטות תקינות.
    -    `numberOfShots += 1`: מגדיל את מונה היריות.
        -   בלוק `if board[x][y] == 1:` מבוצע אם הירי פגע בספינה.
         - `board[x][y] = 'hit'` - סימון פגיעה בספינה.
         -  עובר על כל הספינות ובודק האם מי מהן הוטבעה, באמצעות הפונקציה `is_sunk`.
          - אם הספינה הוטבעה, אז מציג הודעה, מגדיל את מונה הספינות שהוטבעו ומוחק את נתוני הספינה שהוטבעה מרשימת `ships`.
         -  אם הספינה לא הוטבעה, אז מציג את ההודעה `HIT`.
      - `elif board[x][y] == 0:` מבוצע אם הירי לא פגע בספינה.
         -  `board[x][y] = 'miss'` מסמן את התא כתא שבו בוצע ירי אך לא הייתה פגיעה.
         - מציג את ההודעה `MISS`.
      -  `else:` מבוצע אם בוצע ירי על קואורדינטות אלו כבר קודם.
    -   `print_board(board)`: מציג את המצב הנוכחי של לוח המשחק.
    -   `print(f"YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS")`: מציג הודעת ניצחון ומספר היריות.
7.  **הפעלה מותנית**:
    -   `if __name__ == "__main__":`: בודק האם הקובץ הופעל כסקריפט הראשי.
    -   `play_salvo()`: קורא לפונקציה להפעלת המשחק.

"""