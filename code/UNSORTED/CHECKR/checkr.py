CHECKR:
=================
רמת מורכבות: 5
-----------------
המשחק "דמקה" הוא יישום טקסטואלי של גרסה פשוטה של משחק הדמקה. המשחק מתרחש על לוח בגודל 8x8, כאשר השחקן משחק נגד המחשב. מטרת המשחק היא להגיע לקצה הנגדי של הלוח עם אחד מכלי השחקן, תוך הימנעות מלכידת כלי היריב.

כללי המשחק:
1.  השחקן והמחשב נעים בתורות.
2.  השחקן שולט בכלים המסומנים ב-'1'.
3.  המחשב שולט בכלים המסומנים ב-'2'.
4.  הלוח הוא רשת בגודל 8x8, כאשר '.' מסמל מקום ריק.
5.  השחקן מזין קואורדינטות של המיקום הנוכחי והמיקום הרצוי.
6.  מהלך רגיל של כלי הוא תנועה באלכסון קדימה בתא אחד.
7.  כלי יכול לקפוץ מעל כלי יריב אם קיימת שדה פנוי אחריו (לא מיושם בקוד).
8.  אם כלי מגיע לקצה הנגדי של הלוח, הוא הופך למלכה (לא מיושם בקוד).
9.  המחשב מבצע מהלך אקראי חוקי.
10. המשחק מסתיים אם אחד מהצדדים מגיע לקצה הלוח או שאין לו מהלכים חוקיים.
-----------------
אלגוריתם:
1.  אתחול לוח בגודל 8x8 עם הסידור הראשוני של הכלים.
2.  שרטוט הלוח.
3.  התחלת לולאת המשחק:
    3.1. בקשת קלט מהשחקן עבור מהלך (מיקום נוכחי ומיקום רצוי).
    3.2. בדיקת תקינות הקלט.
    3.3. אם הקלט לא תקין, בקשת קלט חוזר.
    3.4. ביצוע מהלך השחקן, אם המהלך חוקי.
    3.5. בדיקה האם השחקן הגיע לקצה הנגדי של הלוח. אם כן, סיום המשחק.
    3.6. תור המחשב:
        3.6.1. מציאת כל המהלכים האפשריים של המחשב.
        3.6.2. בחירת מהלך אקראי מתוך המהלכים האפשריים.
        3.6.3. ביצוע מהלך המחשב.
    3.7. בדיקה האם המחשב הגיע לקצה הנגדי של הלוח. אם כן, סיום המשחק.
    3.8. שרטוט הלוח.
4.  אם אף אחד מהצדדים לא ניצח, מעבר לשלב 3.
5.  בסיום המשחק, הדפסת הודעת ניצחון או הפסד.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["אתחול לוח: <code><b>board[8][8]</b></code> עם הסידור הראשוני של הכלים"]
    InitializeBoard --> DrawBoard["שרטוט הלוח"]
    DrawBoard --> GameLoopStart{"התחלת לולאת המשחק"}
    GameLoopStart --> PlayerInput["קלט שחקן: <code><b>currentPosition, nextPosition</b></code>"]
    PlayerInput --> ValidateInput{"בדיקת תקינות קלט: <code><b>isInputValid(currentPosition, nextPosition)</b></code>"}
    ValidateInput -- קלט לא תקין --> PlayerInput
    ValidateInput -- קלט תקין --> PlayerMove{"ביצוע מהלך שחקן: <code><b>updateBoard(currentPosition, nextPosition)</b></code>"}
    PlayerMove --> PlayerWinCheck{"בדיקת ניצחון שחקן: <code><b>checkWin(player)</b></code>"}
    PlayerWinCheck -- כן --> OutputPlayerWin["הדפסת הודעה: <b>השחקן ניצח</b>"]
    OutputPlayerWin --> End["סיום"]
    PlayerWinCheck -- לא --> ComputerTurn{"תור המחשב"}
    ComputerTurn --> FindPossibleMoves["מציאת מהלכים אפשריים של המחשב"]
    FindPossibleMoves --> ChooseRandomMove["בחירת מהלך אקראי של המחשב"]
    ChooseRandomMove --> ComputerMove{"ביצוע מהלך מחשב: <code><b>updateBoard(currentPosition, nextPosition)</b></code>"}
    ComputerMove --> ComputerWinCheck{"בדיקת ניצחון מחשב: <code><b>checkWin(computer)</b></code>"}
    ComputerWinCheck -- כן --> OutputComputerWin["הדפסת הודעה: <b>המחשב ניצח</b>"]
    OutputComputerWin --> End
    ComputerWinCheck -- לא --> DrawBoard
     GameLoopStart  -- סוף משחק --> End
```
מקרא:
    Start - תחילת התוכנית.
    InitializeBoard - אתחול לוח המשחק (8x8) עם הסידור הראשוני של הכלים.
    DrawBoard - שרטוט המצב הנוכחי של לוח המשחק לקונסול.
    GameLoopStart - תחילת לולאת המשחק הראשית.
    PlayerInput - בקשת קואורדינטות מהשחקן עבור המיקום הנוכחי והמיקום הרצוי למהלך.
    ValidateInput - בדיקת הקואורדינטות שהוזנו לוודאות שהן תקינות ותואמות את כללי המשחק.
    PlayerMove - ביצוע מהלך השחקן על לוח המשחק.
    PlayerWinCheck - בדיקה האם השחקן השיג את תנאי הניצחון (הגעה לקצה הנגדי של הלוח).
    OutputPlayerWin - הדפסת הודעה על ניצחון השחקן.
    ComputerTurn - מעבר התור למחשב.
    FindPossibleMoves - איתור כל המהלכים האפשריים עבור המחשב.
    ChooseRandomMove - בחירת מהלך אקראי חוקי עבור המחשב.
    ComputerMove - ביצוע מהלך המחשב על לוח המשחק.
    ComputerWinCheck - בדיקה האם המחשב השיג את תנאי הניצחון (הגעה לקצה הנגדי של הלוח).
    OutputComputerWin - הדפסת הודעה על ניצחון המחשב.
     End - סיום המשחק.
```
import random

# משתנים גלובליים לייצוג הלוח
BOARD_SIZE = 8
EMPTY = '.'
PLAYER = '1'
COMPUTER = '2'


def initialize_board():
    """מאתחל את הלוח בגודל 8x8 עם הסידור הראשוני של הכלים."""
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # ממקמים את כלי השחקן והמחשב במיקומים ההתחלתיים
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
    """משרטט את המצב הנוכחי של הלוח לקונסול."""
    print("  ", end="")
    for i in range(BOARD_SIZE):
        print(i, end=" ")
    print()
    for i, row in enumerate(board):
        print(i, " ".join(row))


def is_valid_move(board, row, col, new_row, new_col, player):
    """בדיקה האם מהלך השחקן חוקי."""

    if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE):
        return False

    if board[row][col] != player:
        return False

    if board[new_row][new_col] != EMPTY:
        return False

    row_diff = new_row - row
    col_diff = new_col - col
    
    if abs(row_diff) != 1 or abs(col_diff) != 1:
        return False
    
    if player == PLAYER and row_diff > 0:
        return False
    
    if player == COMPUTER and row_diff < 0:
        return False

    return True
def update_board(board, row, col, new_row, new_col):
    """מעדכן את הלוח לאחר מהלך."""
    board[new_row][new_col] = board[row][col]
    board[row][col] = EMPTY


def check_win(board, player):
    """בדיקה האם השחקן או המחשב השיגו ניצחון."""
    if player == PLAYER:
        for j in range(BOARD_SIZE):
          if board[BOARD_SIZE-1][j] == PLAYER:
            return True
    if player == COMPUTER:
        for j in range(BOARD_SIZE):
          if board[0][j] == COMPUTER:
            return True
    return False


def get_computer_moves(board):
    """מאתר את כל המהלכים האפשריים של המחשב."""
    moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == COMPUTER:
                for dr in [-1, 1]:
                    for dc in [-1, 1]:
                       new_row, new_col = row + dr , col + dc
                       if is_valid_move(board, row, col, new_row, new_col,COMPUTER):
                            moves.append((row, col, new_row, new_col))
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
            current_row = int(input("הכנס את שורת המיקום הנוכחי (0-7): "))
            current_col = int(input("הכנס את עמודת המיקום הנוכחי (0-7): "))
            new_row = int(input("הכנס את שורת המיקום החדש (0-7): "))
            new_col = int(input("הכנס את עמודת המיקום החדש (0-7): "))
            if is_valid_move(board, current_row, current_col, new_row, new_col, PLAYER):
                update_board(board, current_row, current_col, new_row, new_col)
                break
            else:
              print("מהלך לא חוקי, נסה שוב.")
        except ValueError:
            print("שגיאת קלט. אנא הכנס מספרים שלמים.")


def play_checkers():
    """הפונקציה הראשית של משחק הדמקה."""
    board = initialize_board()
    draw_board(board)
    while True:
        player_turn(board)
        if check_win(board, PLAYER):
            print("ברכות! ניצחת!")
            break
        
        computer_turn(board)
        if check_win(board, COMPUTER):
            print("המחשב ניצח!")
            break
        draw_board(board)


if __name__ == "__main__":
    play_checkers()
```
הסבר הקוד:

1.  **ייבוא מודול random**:
    *   `import random`: מייבא את מודול `random`, המשמש לבחירת מהלך אקראי של המחשב.

2.  **משתנים גלובליים**:
    *   `BOARD_SIZE`: גודל הלוח (8x8).
    *   `EMPTY`: תו המייצג תא ריק.
    *   `PLAYER`: תו המייצג כלי שחקן ('1').
    *   `COMPUTER`: תו המייצג כלי מחשב ('2').

3.  **פונקציה `initialize_board()`**:
    *   יוצרת ומאתחלת את לוח המשחק כרשימת רשימות (מערך דו-ממדי).
    *   ממקמת את כלי השחקן ('1') וכלי המחשב ('2') במיקומים ההתחלתיים.

4.  **פונקציה `draw_board(board)`**:
    *   מקבלת את המצב הנוכחי של הלוח.
    *   מציגה את הלוח לקונסול עם מספור שורות ועמודות לנוחות המשתמש.

5.  **פונקציה `is_valid_move(board, row, col, new_row, new_col, player)`**:
    *   בדיקה האם מהלך של שחקן או מחשב חוקי:
        *   בדיקה שהמיקום נמצא בתוך גבולות הלוח.
        *   בדיקה שהכלי במיקום הנוכחי שייך לשחקן שמבצע את המהלך.
        *   בדיקה שתא היעד ריק.
        *   בדיקה לתנועה אלכסונית בלבד בתא אחד.
        *   בדיקה שכלי השחקן נע קדימה בלבד (שורות עולות במספרן).
        *   בדיקה שכלי המחשב נע קדימה בלבד (שורות יורדות במספרן).

6.  **פונקציה `update_board(board, row, col, new_row, new_col)`**:
    *   מעדכן את הלוח לאחר מהלך:
        *   מעביר את הכלי מהמיקום הנוכחי למיקום החדש.
        *   מסמן את המיקום הנוכחי כריק.

7.  **פונקציה `check_win(board, player)`**:
    *   בדיקה האם השחקן או המחשב השיגו ניצחון (הגעה לקצה הלוח).
    *   עבור השחקן, נבדקת הגעת כלי כלשהו לשורה האחרונה בלוח.
    *   עבור המחשב, נבדקת הגעת כלי כלשהו לשורה הראשונה בלוח.

8.  **פונקציה `get_computer_moves(board)`**:
    *   מאתר את כל המהלכים האפשריים של המחשב:
        *   עובר על כל תאי הלוח ומחפש את כלי המחשב.
        *   עבור כל כלי מחשב, בודק את כל המהלכים האלכסוניים האפשריים בתא אחד.
        *   מחזיר רשימת טאפלים `(row, col, new_row, new_col)` של מהלכים זמינים.

9.  **פונקציה `computer_turn(board)`**:
    *   מבצע את מהלך המחשב:
        *   מקבל רשימת מהלכים אפשריים.
        *   בוחר מהלך אקראי מהרשימה.
        *   מעדכן את הלוח בהתאם למהלך שנבחר.

10. **פונקציה `player_turn(board)`**:
    *   מבקש מהשחקן קלט עבור קואורדינטות המיקום הנוכחי והמיקום הרצוי.
    *   בדיקת תקינות הקלט והמהלך.
    *   מבצע את המהלך אם הקלט והמהלך תקינים.
    *   אם הקלט או המהלך אינם תקינים, מבקש קלט חוזר.

11. **פונקציה `play_checkers()`**:
    *   הפונקציה הראשית של משחק הדמקה:
        *   מאתחלת את הלוח.
        *   מציגה את הלוח על המסך.
        *   מריצה לולאת משחק, הנמשכת עד הושג ניצחון על ידי אחת מהצדדים:
            *   תור השחקן.
            *   בדיקת ניצחון שחקן.
            *   תור המחשב.
            *   בדיקת ניצחון מחשב.
            *   הצגת הלוח לאחר כל מהלך.

12. **הפעלת המשחק**:
    *   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_checkers()` תורץ רק אם הקובץ מורץ ישירות, ולא אם הוא מיובא כמודול.
    *   `play_checkers()`: קריאה לפונקציה כדי להתחיל את המשחק.