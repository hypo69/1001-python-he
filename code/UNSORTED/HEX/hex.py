HEX:
=================
מורכבות: 7
-----------------
משחק HEX הוא משחק היגיון בו שני שחקנים מניחים לסירוגין את האסימונים שלהם על רשת משושה, במטרה לחבר צדדים נגדיים של הלוח. מטרת כל שחקן היא ליצור שרשרת רציפה של האסימונים שלו, המחברת את הצדדים הנגדיים שלו על הלוח. השחקנים מניחים את האסימונים שלהם על תאים משושים עד שאחד מהם מצליח לחבר את הצדדים שלו. בגרסה זו, המשחק מומש עבור שני שחקנים: '1' ו-'2'.
כללי המשחק:
1. שחקנים מניחים לסירוגין את האסימונים שלהם (הסמלים '1' ו-'2') על הלוח המשושה.
2. מטרת השחקן הראשון (הסמל '1') – לחבר את הצד השמאלי והימני של הלוח באמצעות האסימונים שלו.
3. מטרת השחקן השני (הסמל '2') – לחבר את הצד העליון והתחתון של הלוח באמצעות האסימונים שלו.
4. השחקן הראשון שמשיג את מטרתו – מנצח.
5. המשחק נמשך עד לניצחונו של אחד מהשחקנים.
-----------------
אלגוריתם:
1. אתחול:
   1.1. יצירת לוח משחק ריק בגודל 11x11 (מערך מחרוזות).
   1.2. הגדרת השחקן הנוכחי ל-1.
2. לולאת המשחק הראשית:
    2.1. הצגת מצב הלוח הנוכחי.
    2.2. בקשת קואורדינטות (שורה, עמודה) מהשחקן הנוכחי לצורך הצבת אסימון.
    2.3. בדיקת תקינות הקלט: אם הקלט אינו תקין, חזרה לשלב 2.2.
    2.4. אם התא הנבחר תפוס, חזרה לשלב 2.2.
    2.5. הצבת אסימון השחקן הנוכחי בתא הנבחר.
    2.6. בדיקה האם השחקן הנוכחי ניצח.
         2.6.1. אם שחקן 1 ניצח, הצגת הודעת ניצחון.
         2.6.2. אם שחקן 2 ניצח, הצגת הודעת ניצחון.
         2.6.3. אם לא, מעבר לשלב 2.7.
    2.7. החלפת השחקן הנוכחי.
3. סיום המשחק:
    3.1. הצגת הודעת ניצחון.
    3.2. סוף המשחק.
-----------------
דיאגרמת זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeBoard["<p align='left'>אתחול הלוח:
    <code><b>
    board = empty 11x11 array
    currentPlayer = 1
    </b></code></p>"]
    InitializeBoard --> LoopStart{"תחילת הלולאה: כל עוד אין מנצח"}
    LoopStart --> DisplayBoard["הצגת מצב הלוח הנוכחי"]
    DisplayBoard --> GetInput["בקשת קואורדינטות מהשחקן הנוכחי"]
    GetInput --> ValidateInput{"בדיקת תקינות הקלט"}
    ValidateInput -- Некорректный ввод --> GetInput
    ValidateInput -- Корректный ввод --> CheckCellEmpty{"בדיקה: <code><b>board[row][col] == ' '?</b></code>"}
    CheckCellEmpty -- Клетка занята --> GetInput
    CheckCellEmpty -- Клетка свободна --> PlaceMove["הצבת אסימון השחקן ב-<code><b>board[row][col]</b></code>"]
     PlaceMove --> CheckWin["בדיקה: האם יש מנצח ל-<code><b>currentPlayer</b></code>?"]
    CheckWin -- Игрок победил --> OutputWin["הצגת הודעת ניצחון עבור השחקן <code><b>currentPlayer</b></code>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет победителя --> SwitchPlayer["החלפת השחקן הנוכחי: <code><b>currentPlayer = 3 - currentPlayer</b></code>"]
    SwitchPlayer --> LoopStart
    LoopStart -- Нет победителя --> End
```
**מקרא**:
    Start - תחילת המשחק.
    InitializeBoard - אתחול לוח המשחק (מערך 11x11 ריק) והגדרת השחקן הנוכחי ל-1.
    LoopStart - תחילת לולאת המשחק, הנמשכת עד לזיהוי מנצח.
    DisplayBoard - הצגת מצב לוח המשחק הנוכחי על המסך.
    GetInput - בקשת קואורדינטות (שורה ועמודה) מהשחקן הנוכחי לצורך הצבת אסימון.
    ValidateInput - בדיקת תקינות הקואורדינטות שהוזנו.
    CheckCellEmpty - בדיקה האם התא הנבחר על הלוח פנוי.
    PlaceMove - הצבת אסימון השחקן הנוכחי בתא הנבחר.
    CheckWin - בדיקה האם יש מנצח לאחר הצבת האסימון.
    OutputWin - הצגת הודעת ניצחון, אם זוהה מנצח.
    SwitchPlayer - החלפת השחקן הנוכחי לשחקן הנגדי.
    End - סוף המשחק.
"""

import sys
def print_board(board):
    """מציגה את מצב הלוח הנוכחי."""
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
     """מבקשת מהשחקן קואורדינטות עבור המהלך."""
     while True:
          try:
              move = input(f"מהלך שחקן {player}. אנא הזן קואורדינטות (לדוגמה, A1): ").strip().upper()
              if len(move) < 2:
                  raise ValueError
              col = ord(move[0]) - ord('A')
              row = int(move[1:]) - 1
              if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == ' ':
                    return row, col
                else:
                     print("תא זה תפוס, אנא בחר תא אחר")
              else:
                   print("קואורדינטות לא תקינות, נסה שוב")
          except ValueError:
            print("פורמט קלט לא תקין, נסה שוב (לדוגמה A1)")


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
              return True # start from the left, reach the right
           directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
        elif player == '2':
           if row == len(board)-1:
               return True # start from the top, reach the bottom
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
    """הפונקציה הראשית של המשחק."""
    board_size = 11
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)] # יצירת לוח ריק
    current_player = '1' # התחלה עם שחקן ראשון

    while True:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player # הצבת אסימון

        if check_win(board, current_player):
              print_board(board)
              print(f"שחקן {current_player} ניצח!")
              break
        current_player = '2' if current_player == '1' else '1'


if __name__ == "__main__":
    play_hex()

"""
הסבר קוד:
1.  **ייבוא המודול `sys`**:
    -   `import sys`: מייבא את המודול `sys`, המשמש ליציאה מהתוכנית.

2. **הפונקציה `print_board(board)`:**
    - מציגה את מצב לוח המשחק הנוכחי בקונסולה.
    - תחילה מודפסים סימוני האותיות של העמודות (A, B, C, ...), ולאחר מכן מודפסות השורות, כאשר כל שורה מתחילה בסימון מספרי ולאחר מכן מודפסים תאי הלוח.

3.  **הפונקציה `get_move(board, player)`:**
    - מבקשת מהשחקן קלט של קואורדינטות עבור המהלך.
     -  משתמשת בלולאת while True על מנת להבטיח קלט תקין.
    - ממירה את הקואורדינטות שהוזנו (לדוגמה, "A1") לאינדקסים של שורה ועמודה.
    - בודקת את תקינות הקואורדינטות שהוזנו, וכן האם התא תפוס, ואם הכל תקין, מחזירה את הקואורדינטות כטאפל (row,col).

4.  **הפונקציה `check_win(board, player)`:**
    - בודקת האם יש מנצח על הלוח.
    - משתמשת בפונקציה רקורסיבית `dfs` (חיפוש לעומק) לניתוח קישוריות האסימונים של השחקן.
    - הפונקציה `is_valid` משמשת לבדיקת תקינות הקואורדינטות.
    - עבור שחקן 1, הבדיקה מתחילה מהצד השמאלי של הלוח ומחפשת נתיב לצד הימני; עבור שחקן 2 – מלמעלה למטה.
    - אם נמצא נתיב, הפונקציה מחזירה `True`, אחרת `False`.

5.  **הפונקציה `play_hex()`:**
    -  מכילה את הלוגיקה הראשית של משחק "הקס".
    -   יוצרת לוח משחק ריק board בגודל 11x11.
    -   מגדירה את השחקן הנוכחי current_player ל-'1'.
    -   בלולאת while True:
        -   קוראת לפונקציה `print_board()` כדי להציג את הלוח.
        -   קוראת לפונקציה `get_move()` כדי לקבל את המהלך מהשחקן.
        -   מניחה את אסימון השחקן על הלוח.
        -   קוראת לפונקציה `check_win()`, כדי לבדוק האם יש מנצח.
        -   אם יש מנצח, מציגה הודעת ניצחון ומסיימת את המשחק.
        -   מחליפה את השחקן הנוכחי (מ-'1' ל-'2' ולהיפך) אם אין מנצח.

6.  **בלוק `if __name__ == "__main__":`:**
    -   מבטיח שהפונקציה `play_hex()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    -   קוראת לפונקציה `play_hex()` כדי להתחיל את המשחק.
"""