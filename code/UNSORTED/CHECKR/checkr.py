"""
CHECKR:
=================
רמת מורכבות: 5
-----------------
המשחק "דמקה" הינו מימוש טקסטואלי של גרסה פשוטה של משחק הדמקה. המשחק מתנהל על לוח בגודל 8x8, בו שחקן משחק נגד המחשב. מטרת המשחק היא להגיע לקצה הנגדי של הלוח עם אחד מכלי המשחק שלך, תוך הימנעות מלכידת כלי המשחק של היריב.

כללי המשחק:
1.  השחקן והמחשב מבצעים מהלכים לסירוגין.
2.  השחקן שולט על כלי משחק המסומנים '1'.
3.  המחשב שולט על כלי משחק המסומנים '2'.
4.  הלוח מיוצג על ידי רשת 8x8, כאשר '.' מסמן מקום ריק.
5.  השחקן מזין קואורדינטות של מיקום נוכחי ומיקום רצוי.
6.  מהלך של כלי משחק - תנועה של תא אחד באלכסון קדימה.
7.  כלי משחק יכול לקפוץ מעל כלי משחק של היריב, אם יש מקום פנוי אחריו.
8.  אם כלי משחק מגיע לקצה הנגדי של הלוח, הוא הופך לדמקה (זה לא ממומש בקוד).
9.  המחשב מבצע מהלך חוקי אקראי.
10. המשחק מסתיים אם אחד מהצדדים מגיע לקצה הלוח או שאין לו מהלכים חוקיים.
-----------------
אלגוריתם:
1.  אתחול לוח 8x8 עם סידור התחלתי של כלי המשחק.
2.  הצגת הלוח.
3.  התחלת מחזור המשחק:
    3.1. בקשת קלט מהלך מהשחקן (מיקום נוכחי ומיקום רצוי).
    3.2. בדיקת תקינות הקלט.
    3.3. אם הקלט אינו תקין, בקשת קלט חוזר.
    3.4. ביצוע מהלך השחקן, אם המהלך חוקי.
    3.5. בדיקה האם השחקן הגיע לקצה הנגדי של הלוח. אם כן, סיום המשחק.
    3.6. תור המחשב:
        3.6.1. מציאת כל המהלכים האפשריים של המחשב.
        3.6.2. בחירת מהלך אקראי מבין האפשריים.
        3.6.3. ביצוע מהלך המחשב.
    3.7. בדיקה האם המחשב הגיע לקצה הנגדי של הלוח. אם כן, סיום המשחק.
    3.8. הצגת הלוח.
4.  אם אף אחד מהצדדים לא ניצח, מעבר לשלב 3.
5.  בסיום המשחק, הצגת הודעה על ניצחון או הפסד.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["אתחול הלוח: <code><b>board[8][8]</b></code> עם סידור התחלתי של כלי המשחק"]
    InitializeBoard --> DrawBoard["הצגת הלוח"]
    DrawBoard --> GameLoopStart{"תחילת מחזור המשחק"}
    GameLoopStart --> PlayerInput["קלט מהלך השחקן: <code><b>currentPosition, nextPosition</b></code>"]
    PlayerInput --> ValidateInput{"בדיקת תקינות הקלט: <code><b>isInputValid(currentPosition, nextPosition)</b></code>"}
    ValidateInput -- קלט לא תקין --> PlayerInput
    ValidateInput -- קלט תקין --> PlayerMove{"ביצוע מהלך השחקן: <code><b>updateBoard(currentPosition, nextPosition)</b></code>"}
    PlayerMove --> PlayerWinCheck{"בדיקת ניצחון השחקן: <code><b>checkWin(player)</b></code>"}
    PlayerWinCheck -- כן --> OutputPlayerWin["פלט הודעה: <b>השחקן ניצח</b>"]
    OutputPlayerWin --> End["סיום"]
    PlayerWinCheck -- לא --> ComputerTurn{"תור המחשב"}
    ComputerTurn --> FindPossibleMoves["מציאת המהלכים האפשריים של המחשב"]
    FindPossibleMoves --> ChooseRandomMove["בחירת מהלך אקראי של המחשב"]
    ChooseRandomMove --> ComputerMove{"ביצוע מהלך המחשב: <code><b>updateBoard(currentPosition, nextPosition)</b></code>"}
    ComputerMove --> ComputerWinCheck{"בדיקת ניצחון המחשב: <code><b>checkWin(computer)</b></code>"}
    ComputerWinCheck -- כן --> OutputComputerWin["פלט הודעה: <b>המחשב ניצח</b>"]
    OutputComputerWin --> End
    ComputerWinCheck -- לא --> DrawBoard
     GameLoopStart  -- סיום משחק --> End
```
מקרא:
    Start - התחלת התוכנית.
    InitializeBoard - אתחול לוח המשחק (8x8) עם מיקום התחלתי של כלי המשחק.
    DrawBoard - הצגת המצב הנוכחי של לוח המשחק במסוף.
    GameLoopStart - תחילת מחזור המשחק הראשי.
    PlayerInput - בקשת קלט מהשחקן עבור קואורדינטות המיקום הנוכחי והמיקום הרצוי למהלך.
    ValidateInput - בדיקת הקואורדינטות שהוזנו לתקינות והתאמה לחוקי המשחק.
    PlayerMove - ביצוע מהלך השחקן על לוח המשחק.
    PlayerWinCheck - בדיקה האם השחקן הגיע לתנאי ניצחון (הגעה לקצה הנגדי של הלוח).
    OutputPlayerWin - הצגת הודעה על ניצחון השחקן.
    ComputerTurn - מעבר התור למחשב.
    FindPossibleMoves - מציאת כל המהלכים האפשריים עבור המחשב.
    ChooseRandomMove - בחירת מהלך חוקי אקראי עבור המחשב.
    ComputerMove - ביצוע מהלך המחשב על לוח המשחק.
    ComputerWinCheck - בדיקה האם המחשב הגיע לתנאי ניצחון (הגעה לקצה הנגדי של הלוח).
    OutputComputerWin - הצגת הודעה על ניצחון המחשב.
     End - סיום המשחק.
"""
import random

# Глобальные переменные для представления доски
BOARD_SIZE = 8
EMPTY = '.'
PLAYER = '1'
COMPUTER = '2'


def initialize_board():
    """מאתחל לוח בגודל 8x8 עם מיקום התחלתי של כלי המשחק."""
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # ממקם את כלי המשחק של השחקן והמחשב במיקומים ההתחלתיים
    for i in range(3):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 != 0:
                board[i][j] = PLAYER
    for i in range(BOARD_SIZE - 3, BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 != 0:
                board[i][j] = COMPUTER
    return board


def draw_board(board):
    """מציג את מצב הלוח הנוכחי במסוף."""
    print("  ", end="")
    for i in range(BOARD_SIZE):
        print(i, end=" ")
    print()
    for i, row in enumerate(board):
        print(i, " ".join(row))


def is_valid_move(board, row, col, new_row, new_col, player):
    """בדיקה האם מהלך חוקי עבור השחקן הנתון."""

    # בדיקה שהמיקום נמצא בתוך גבולות הלוח.
    if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE):
        return False

    # בדיקה שהכלי שייך לשחקן.
    if board[row][col] != player:
        return False

    # בדיקה שהתא היעד ריק.
    if board[new_row][new_col] != EMPTY:
        return False

    row_diff = new_row - row
    col_diff = new_col - col

    # בדיקה של תנועה אלכסונית בתא אחד בלבד.
    if abs(row_diff) != 1 or abs(col_diff) != 1:
        return False

    # בדיקה של תנועת כלי השחקן קדימה בלבד.
    if player == PLAYER and row_diff > 0:
        return False

    # בדיקה של תנועת כלי המחשב קדימה בלבד.
    if player == COMPUTER and row_diff < 0:
        return False

    return True
def update_board(board, row, col, new_row, new_col):
    """מעדכן את הלוח לאחר מהלך."""
    board[new_row][new_col] = board[row][col]
    board[row][col] = EMPTY


def check_win(board, player):
    """בדיקה האם השחקן או המחשב הגיעו לתנאי ניצחון."""
    if player == PLAYER:
        # עבור השחקן, בודק הגעת כלי לשורה האחרונה.
        for j in range(BOARD_SIZE):
          if board[BOARD_SIZE-1][j] == PLAYER:
            return True
    if player == COMPUTER:
        # עבור המחשב, בודק הגעת כלי לשורה הראשונה.
        for j in range(BOARD_SIZE):
          if board[0][j] == COMPUTER:
            return True
    return False


def get_computer_moves(board):
    """מוצא את כל המהלכים האפשריים של המחשב."""
    moves = []
    # עובר על כל תאי הלוח ומחפש את כלי המחשב.
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == COMPUTER:
                # בודק את כל המהלכים האלכסוניים האפשריים עבור כל כלי.
                for dr in [-1, 1]:
                    for dc in [-1, 1]:
                       new_row, new_col = row + dr , col + dc
                       if is_valid_move(board, row, col, new_row, new_col,COMPUTER):
                            moves.append((row, col, new_row, new_col))
    # מחזיר רשימה של טאפלים (row, col, new_row, new_col) המייצגים מהלכים אפשריים.
    return moves


def computer_turn(board):
    """מבצע את מהלך המחשב."""
    possible_moves = get_computer_moves(board)
    if possible_moves:
        row, col, new_row, new_col = random.choice(possible_moves)
        update_board(board, row, col, new_row, new_col)


def player_turn(board):
    """מבקש ומבצע את מהלך השחקן."""
    while True:
        try:
            current_row = int(input("Введите строку текущей позиции (0-7): ")) # Keep original prompt text as it's user-facing input instruction.
            current_col = int(input("Введите столбец текущей позиции (0-7): ")) # Keep original prompt text.
            new_row = int(input("Введите строку новой позиции (0-7): ")) # Keep original prompt text.
            new_col = int(input("Введите столбец новой позиции (0-7): ")) # Keep original prompt text.
            if is_valid_move(board, current_row, current_col, new_row, new_col, PLAYER):
                update_board(board, current_row, current_col, new_row, new_col)
                break
            else:
              print("Недопустимый ход, попробуйте еще раз.") # Keep original error message.
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целые числа.") # Keep original error message.


def play_checkers():
    """הפונקציה הראשית של משחק הדמקה."""
    # מאתחל את הלוח.
    board = initialize_board()
    # מציג את הלוח.
    draw_board(board)
    # מפעיל את מחזור המשחק עד שאחד הצדדים משיג ניצחון:
    while True:
        # מהלך השחקן.
        player_turn(board)
        # בדיקת ניצחון השחקן.
        if check_win(board, PLAYER):
            print("Поздравляю! Вы выиграли!") # Keep original win message.
            break
        # מהלך המחשב.
        computer_turn(board)
        # בדיקת ניצחון המחשב.
        if check_win(board, COMPUTER):
            print("Компьютер выиграл!") # Keep original win message.
            break
        # הצגת הלוח לאחר כל מהלך.
        draw_board(board)


if __name__ == "__main__":
    # בלוק זה מבטיח שהפונקציה play_checkers() תופעל רק אם הקובץ מופעל ישירות, ולא מיובא כמודול.
    # קורא לפונקציה כדי להתחיל את המשחק.
    play_checkers()
"""
הסבר הקוד:

1. **ייבוא מודול random**:
   - `import random`: מייבא את המודול `random`, המשמש לבחירת מהלך אקראי עבור המחשב.

2. **משתנים גלובליים**:
   - `BOARD_SIZE`: גודל הלוח (8x8).
   - `EMPTY`: תו המייצג תא ריק.
   - `PLAYER`: תו המייצג את כלי השחקן ('1').
   - `COMPUTER`: תו המייצג את כלי המחשב ('2').

3. **פונקציה `initialize_board()`**:
   - יוצרת ומאתחלת את לוח המשחק כרשימה של רשימות (מערך דו ממדי).
   - ממקמת את המיקומים ההתחלתיים של כלי השחקן ('1') וכלי המחשב ('2').

4. **פונקציה `draw_board(board)`**:
   - מקבלת את מצב הלוח הנוכחי.
   - מציגה את הלוח במסוף עם מספור שורות וטורים לנוחות המשתמש.

5. **פונקציה `is_valid_move(board, row, col, new_row, new_col, player)`**:
   - בודקת האם מהלך השחקן או המחשב חוקי:
     - בדיקה שהמיקום נמצא בתוך גבולות הלוח.
     - בדיקה שהכלי שייך לשחקן (השחקן הנתון).
     - בדיקה שהתא היעד ריק.
     - בדיקה של תנועה אלכסונית בתא אחד בלבד.
    - בדיקה של תנועת כלי השחקן קדימה בלבד.
    - בדיקה של תנועת כלי המחשב קדימה בלבד.

6. **פונקציה `update_board(board, row, col, new_row, new_col)`**:
   - מעדכנת את הלוח לאחר מהלך:
     - מעבירה את הכלי מהמיקום הנוכחי לחדש.
     - מסמנת את המיקום הנוכחי כריק.

7.  **פונקציה `check_win(board, player)`**:
    - בודקת האם השחקן או המחשב הגיעו לסוף הלוח, מה שמשמעו ניצחון.
    - עבור השחקן, בודקת הגעת כלי לשורה האחרונה.
    - עבור המחשב, בודקת הגעת כלי לשורה הראשונה.

8.  **פונקציה `get_computer_moves(board)`**:
    - מוצאת את כל המהלכים האפשריים של המחשב:
        - עוברת על כל תאי הלוח ומחפשת את כלי המחשב.
        - בודקת את כל המהלכים האלכסוניים האפשריים עבור כל כלי.
        - מחזירה רשימה של טאפלים (row, col, new_row, new_col) המייצגים מהלכים אפשריים.

9.  **פונקציה `computer_turn(board)`**:
    - מבצעת את מהלך המחשב:
        - מקבלת רשימה של מהלכים אפשריים.
        - בוחרת מהלך אקראי מהרשימה.
        - מעדכנת את הלוח בהתאם למהלך שנבחר.

10.  **פונקציה `player_turn(board)`**:
     - מבקשת מהשחקן קלט של קואורדינטות המיקום הנוכחי והמיקום הרצוי.
     - בודקת את תקינות הקלט.
     - מבצעת את המהלך אם הקלט תקין.
     - אם הקלט אינו תקין, מבקשת קלט חוזר.

11. **פונקציה `play_checkers()`**:
    - הפונקציה הראשית של המשחק:
        - מאתחלת את הלוח.
        - מציגה את הלוח.
        - מפעילה את מחזור המשחק עד שאחד הצדדים משיג ניצחון:
            - מהלך השחקן.
            - בדיקת ניצחון השחקן.
            - מהלך המחשב.
            - בדיקת ניצחון המחשב.
            - הצגת הלוח לאחר כל מהלך.

12. **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_checkers()` תופעל רק אם הקובץ מופעל ישירות, ולא מיובא כמודול.
    - `play_checkers()`: קורא לפונקציה כדי להתחיל את המשחק.
"""