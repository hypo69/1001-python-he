HEX:
=================
קושי: 7
-----------------
המשחק HEX הוא משחק לוגי שבו שני שחקנים ממקמים לסירוגין את האסימונים שלהם על רשת משושה, במטרה לחבר צדדים נגדיים של הלוח. מטרת כל שחקן היא ליצור שרשרת רציפה של האסימונים שלו, המחברת את הצדדים הנגדיים שלהם על הלוח. השחקנים מניחים את האסימונים שלהם על תאים משושים עד שאחד מהם מצליח לחבר את הצדדים שלו. בגרסה זו המשחק ממומש עבור שני שחקנים: '1' ו-'2'.
כללי המשחק:
1.  שחקנים ממקמים לסירוגין את האסימונים שלהם (הסימנים '1' ו-'2') על לוח משושה.
2.  מטרת השחקן הראשון (סימן '1') היא לחבר את הצד השמאלי והימני של הלוח באמצעות האסימונים שלו.
3.  מטרת השחקן השני (סימן '2') היא לחבר את הצד העליון והתחתון של הלוח באמצעות האסימונים שלו.
4.  השחקן הראשון שמשיג את מטרתו - מנצח.
5.  המשחק נמשך עד לניצחונו של אחד השחקנים.
-----------------
אלגוריתם:
1.  אתחול:
    1.1. ליצור לוח משחק ריק בגודל 11x11 (מערך שורות).
    1.2. להגדיר את השחקן הנוכחי ל-1.
2.  לולאת המשחק הראשית:
    2.1. להציג את המצב הנוכחי של הלוח.
    2.2. לבקש מהשחקן הנוכחי קואורדינטות (שורה, עמודה) למיקום אסימון.
    2.3. לבדוק תקינות קלט: אם הקלט אינו תקין, לחזור לשלב 2.2.
    2.4. אם התא שנבחר תפוס, לחזור לשלב 2.2.
    2.5. למקם את אסימון השחקן הנוכחי בתא שנבחר.
    2.6. לבדוק האם השחקן הנוכחי ניצח.
        2.6.1. אם שחקן 1 ניצח, להציג הודעת ניצחון.
        2.6.2. אם שחקן 2 ניצח, להציג הודעת ניצחון.
        2.6.3. אם לא, לעבור לשלב 2.7.
    2.7. להחליף את השחקן הנוכחי.
3.  סיום המשחק:
    3.1. להציג הודעת ניצחון.
    3.2. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeBoard["<p align='left'>Инициализация доски:
    <code><b>
    board = empty 11x11 array
    currentPlayer = 1
    </b></code></p>"]
    InitializeBoard --> LoopStart{"Начало цикла: пока нет победителя"}
    LoopStart --> DisplayBoard["Вывести текущее состояние доски"]
    DisplayBoard --> GetInput["Запросить ввод координат от текущего игрока"]
    GetInput --> ValidateInput{"Проверка корректности ввода"}
    ValidateInput -- Некорректный ввод --> GetInput
    ValidateInput -- Корректный ввод --> CheckCellEmpty{"Проверка: <code><b>board[row][col] == ' '?</b></code>"}
    CheckCellEmpty -- Клетка занята --> GetInput
    CheckCellEmpty -- Клетка свободна --> PlaceMove["Поставить фишку игрока в <code><b>board[row][col]</b></code>"]
     PlaceMove --> CheckWin["Проверить, есть ли победитель у <code><b>currentPlayer</b></code>?"]
    CheckWin -- Игрок победил --> OutputWin["Вывод сообщения о победе игрока <code><b>currentPlayer</b></code>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет победителя --> SwitchPlayer["Сменить текущего игрока: <code><b>currentPlayer = 3 - currentPlayer</b></code>"]
    SwitchPlayer --> LoopStart
    LoopStart -- Нет победителя --> End
```
**מקרא**:
    Start - תחילת המשחק.
    InitializeBoard - אתחול לוח המשחק (מערך 11x11 ריק) והגדרת השחקן הנוכחי ל-1.
    LoopStart - תחילת לולאת המשחק, הנמשכת עד שיוכרז מנצח.
    DisplayBoard - הצגת המצב הנוכחי של לוח המשחק על המסך.
    GetInput - בקשת קואורדינטות (מספר שורה ועמודה) מהשחקן הנוכחי למיקום אסימון.
    ValidateInput - בדיקת תקינות הקואורדינטות שהוזנו.
    CheckCellEmpty - בדיקה האם התא שנבחר על הלוח פנוי.
    PlaceMove - מיקום אסימון השחקן הנוכחי בתא שנבחר.
    CheckWin - בדיקה האם יש מנצח לאחר מיקום האסימון.
    OutputWin - הצגת הודעה על ניצחון, אם הוכרז מנצח.
    SwitchPlayer - החלפת השחקן הנוכחי לשחקן הנגדי.
    End - סיום המשחק.
```

import sys
def print_board(board):
    """מציגה את המצב הנוכחי של הלוח."""
    print("   ", end="")
    for i in range(len(board)):
        print(chr(ord('A') + i), end=" ")
    print()
    for i, row in enumerate(board):
        print(f"{i+1:2d} ", end="")
        for cell in row:
            print(cell, end=" ")
        print()


def get_move(board, player):
     """מבקשת מהשחקן קואורדינטות עבור מהלך."""
     while True:
          try:
              move = input(f"Ход игрока {player}. Введите координаты (например, A1): ").strip().upper()
              if len(move) < 2:
                  raise ValueError
              col = ord(move[0]) - ord('A')
              row = int(move[1:]) - 1
              if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == ' ':
                    return row, col
                else:
                     print("Эта клетка занята, выберите другую")
              else:
                   print("Неверные координаты, попробуйте еще раз")
          except ValueError:
            print("Неверный формат ввода, попробуйте еще раз (пример A1)")


def check_win(board, player):
    """בודקת האם השחקן ניצח."""

    def is_valid(row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    def dfs(row, col, visited, player):
        if not is_valid(row, col) or (row, col) in visited or board[row][col] != player:
           return False
        visited.add((row, col))

        if player == '1':
           if col == len(board[0])-1:
              return True # start from the left
           directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
        elif player == '2':
           if row == len(board)-1:
               return True # start from the top
           directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]

        for dr, dc in directions:
            if dfs(row + dr, col + dc, visited, player):
               return True

        return False


    if player == '1':
        for i in range(len(board)):
            if board[i][0] == '1': # start from the left
                if dfs(i, 0, set(), '1'):
                   return True
    elif player == '2':
        for j in range(len(board[0])):
            if board[0][j] == '2': # start from the top
                if dfs(0, j, set(), '2'):
                    return True
    return False
    
def play_hex():
    """פונקציה ראשית של המשחק."""
    board_size = 11
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)] # יוצרת לוח ריק
    current_player = '1' # מתחילים עם שחקן ראשון

    while True:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player # מניחים אסימון

        if check_win(board, current_player):
              print_board(board)
              print(f"Игрок {current_player} победил!")
              break
        current_player = '2' if current_player == '1' else '1'


if __name__ == "__main__":
    play_hex()

```
"""
הסבר קוד:
1.  **ייבוא מודול `sys`**:
    -   `import sys`: מייבא את מודול `sys`, המשמש ליציאה מהתוכנית.

2.  **פונקציה `print_board(board)`:**
    -   מציגה את המצב הנוכחי של לוח המשחק בקונסולה.
    -   מדפיסה תחילה את סימוני האותיות של העמודות (A, B, C, ...), לאחר מכן עוברת להדפסת השורות, כאשר כל שורה מתחילה בסימון מספרי ובהמשך מודפסים תאי הלוח.

3.  **פונקציה `get_move(board, player)`:**
    -   מבקשת מהשחקן להזין קואורדינטות עבור מהלך.
    -   משתמשת בלולאת while True כדי להבטיח קלט תקין.
    -   ממירה את הקואורדינטות שהוזנו (לדוגמה, "A1") לאינדקסים של שורה ועמודה.
    -   בודקת את תקינות הקואורדינטות שהוזנו, וכן האם התא תפוס, ואם הכל תקין, מחזירה את הקואורדינטות כקורטז' (row,col).

4.  **פונקציה `check_win(board, player)`:**
    -   בודקת האם יש מנצח על הלוח.
    -   משתמשת בפונקציה רקורסיבית `dfs` (חיפוש לעומק) לניתוח הקישוריות של אסימוני השחקן.
    -   הפונקציה `is_valid` משמשת לבדיקת חוקיות הקואורדינטות.
    -   עבור שחקן 1, הבדיקה מתחילה מהצד השמאלי של הלוח ומחפשת נתיב לצד הימני, עבור שחקן 2 - מלמעלה למטה.
    -   אם נתיב נמצא, מחזירה `True`, אחרת `False`.

5.  **פונקציה `play_hex()`:**
    -   מכילה את הלוגיקה הראשית של המשחק "הקס".
    -   יוצרת לוח משחק ריק board בגודל 11x11.
    -   מגדירה את השחקן הנוכחי current_player ל-'1'.
    -   בלולאת while True:
        -   קוראת ל-`print_board()` להצגת הלוח.
        -   קוראת ל-`get_move()` לקבלת מהלך מהשחקן.
        -   ממקמת את אסימון השחקן על הלוח.
        -   קוראת ל-`check_win()` כדי לבדוק האם יש מנצח.
        -   אם יש מנצח, מציגה הודעה על ניצחון ומסיימת את המשחק.
        -   מחליפה את השחקן הנוכחי (מ-'1' ל-'2' ולהיפך) אם אין מנצח.

6.  **בלוק `if __name__ == "__main__":`:**
    -   מבטיח שהפונקציה `play_hex()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    -   קוראת ל-`play_hex()` לתחילת המשחק.
"""