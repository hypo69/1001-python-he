<TRAP>:
=================
**מורכבות:** 5
-----------------
המשחק "מלכודת" הוא משחק לשני שחקנים, שבו כל שחקן בתורו מניח את סימניו (המספרים 1 ו-2) על לוח המשחק. מטרת המשחק היא להקיף משבצת של היריב במשבצותיו. אם שחקן מקיף משבצת של היריב מכל הצדדים, משבצת היריב נלכדת.

**חוקי המשחק:**
1.  לוח המשחק הוא רשת מרובעת בגודל 7x7.
2.  שני שחקנים מזינים בתורם קואורדינטות של משבצת להנחת סימנם (1 או 2).
3.  אם משבצת מוקפת מארבעה צדדים בסימני היריב, הסימן נלכד ומוחלף בסימן של השחקן הלוכד.
4.  המשחק מסתיים כאשר כל המשבצות תפוסות. השחקן בעל מספר הסימנים הגדול ביותר על הלוח מנצח.
-----------------
**אלגוריתם:**
1.  אתחל את לוח המשחק כרשת ריקה בגודל 7x7.
2.  קבע את השחקן הנוכחי כשחקן הראשון (1).
3.  התחל את לולאת המשחק הראשית:
    3.1 הצג את מצבו הנוכחי של לוח המשחק.
    3.2 בקש מהשחקן הנוכחי קואורדינטות להנחת הסימן.
    3.3 בדוק האם המשבצת שנבחרה ריקה.
    3.4 אם המשבצת אינה ריקה, הודע לשחקן על שגיאה וחזור לשלב 3.2.
    3.5 הנח את סימן השחקן הנוכחי על המשבצת שנבחרה.
    3.6 בדוק האם יש צורך ללכוד משבצות כלשהן של היריב:
        3.6.1 עבור כל משבצת המקיפה את המשבצת הנוכחית:
            3.6.1.1 אם המשבצת השכנה שייכת ליריב:
                3.6.1.1.1 בדוק האם היא מוקפת מכל הצדדים בסימני השחקן הנוכחי.
                3.6.1.1.2 אם מוקפת, החלף את סימן היריב בסימן של השחקן הנוכחי.
    3.7 החלף את השחקן הנוכחי (מ-1 ל-2 או מ-2 ל-1).
    3.8 חזור על הלולאה עד שכל המשבצות יהיו תפוסות.
4.  ספור את מספר הסימנים של כל שחקן.
5.  הכרז על המנצח (השחקן עם מספר הסימנים הגדול ביותר).
-----------------
**בלוק-סכמה:**
```mermaid
flowchart TD
    Start["Начало"] --> InitializeBoard["Инициализация игрового поля: 7x7 (пустые клетки)"]
    InitializeBoard --> SetCurrentPlayer["Установить текущего игрока: player = 1"]
    SetCurrentPlayer --> GameLoopStart{"Начало игрового цикла: пока не все клетки заполнены"}
    GameLoopStart -- Да --> DisplayBoard["Вывести текущее состояние игрового поля"]
    DisplayBoard --> GetMove["Ввод хода игрока: координаты клетки (row, col)"]
    GetMove --> ValidateMove{"Проверка: клетка (row, col) пуста?"}
    ValidateMove -- Нет --> DisplayError["Вывести сообщение об ошибке: клетка занята"]
    DisplayError --> GetMove
    ValidateMove -- Да --> PlaceMove["Разместить метку текущего игрока на клетке (row, col)"]
    PlaceMove --> CheckCaptureStart{"Начало цикла проверки захвата для соседних клеток"}
    CheckCaptureStart --> CheckNeighbors{"Проверить соседние клетки"}
     CheckNeighbors -- Соседняя клетка принадлежит противнику --> CheckSurrounded{"Проверить, окружена ли клетка противника метками текущего игрока?"}
       CheckSurrounded -- Да --> CaptureCell["Захватить клетку противника"]
        CaptureCell --> CheckCaptureEnd["Конец цикла проверки захвата"]
        CheckSurrounded -- Нет --> CheckCaptureEnd
     CheckNeighbors -- Соседняя клетка не принадлежит противнику --> CheckCaptureEnd
    CheckCaptureEnd --> SwitchPlayer["Переключить текущего игрока: если player=1, то player=2, иначе player=1"]
    SwitchPlayer --> CheckBoardFull{"Проверка: все клетки на поле заполнены?"}
    CheckBoardFull -- Нет --> GameLoopStart
     CheckBoardFull -- Да --> CalculateScores["Подсчитать количество меток каждого игрока"]
    CalculateScores --> DetermineWinner["Определить победителя"]
    DetermineWinner --> End["Конец игры"]
    GameLoopStart -- Нет --> End
```
**מקרא:**
    Start - תחילת המשחק.
    InitializeBoard - אתחול לוח המשחק: יצירת רשת 7x7 ומילוי שלה במשבצות ריקות.
    SetCurrentPlayer - קביעת השחקן הנוכחי כשחקן הראשון (1).
    GameLoopStart - תחילת לולאת המשחק הראשית, הנמשכת עד שכל המשבצות על הלוח מלאות.
    DisplayBoard - הצגת מצבו הנוכחי של לוח המשחק במסוף.
    GetMove - בקשת קואורדינטות המשבצת (שורה ועמודה), שבה השחקן הנוכחי רוצה להניח את סימנו, מהשחקן.
    ValidateMove - בדיקה האם המשבצת שנבחרה ריקה.
    DisplayError - הצגת הודעת שגיאה אם המשבצת שנבחרה כבר תפוסה.
    PlaceMove - הנחת סימן השחקן הנוכחי על המשבצת (row, col).
    CheckCaptureStart - תחילת לולאת בדיקת לכידת משבצות היריב.
    CheckNeighbors - בדיקת המשבצות השכנות מסביב לסימן שהונח זה עתה.
    CheckSurrounded - בדיקה האם המשבצת השכנה של היריב מוקפת מכל הצדדים בסימני השחקן הנוכחי.
    CaptureCell - לכידת משבצת היריב, החלפתה בסימן של השחקן הנוכחי.
    CheckCaptureEnd - סיום לולאת בדיקת לכידת משבצות.
    SwitchPlayer - החלפת השחקן הנוכחי: אם השחקן היה 1, הופך ל-2, ולהיפך.
    CheckBoardFull - בדיקה האם כל המשבצות בלוח המשחק מלאות.
    CalculateScores - חישוב מספר המשבצות התפוסות על ידי כל שחקן.
    DetermineWinner - קביעת המנצח על בסיס ספירת המשבצות התפוסות.
    End - סוף המשחק.
```python
import copy

# גודל לוח המשחק
BOARD_SIZE = 7

# פונקציה ליצירת לוח משחק ריק
def create_board():
    # יוצרת רשימה דו-ממדית, המייצגת את לוח המשחק, המלאה באפסים (משבצות ריקות)
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# פונקציה להצגת מצבו הנוכחי של לוח המשחק
def display_board(board):
    # מציגה את מספרי העמודות
    print("  ", end="")
    for col in range(BOARD_SIZE):
        print(f"{col} ", end="")
    print()
    # עבור כל שורה בלוח המשחק
    for row in range(BOARD_SIZE):
        # מציגה את מספר השורה
        print(f"{row} ", end="")
        # עבור כל משבצת בשורה הנוכחית
        for col in range(BOARD_SIZE):
             # מציגה את תוכן המשבצת, ומחליפה את 0 ב'.', 1 ב-'1', 2 ב-'2'
            print(f"{'.' if board[row][col] == 0 else str(board[row][col])} ", end="")
        # מעבר לשורה חדשה
        print()


# פונקציה לבדיקה האם קואורדינטה נמצאת בטווח לוח המשחק
def is_valid_move(row, col):
    # בודקת האם הקואורדינטות נמצאות בטווח קביל (0 עד BOARD_SIZE - 1)
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

# פונקציה לבדיקה האם משבצת ריקה
def is_cell_empty(board, row, col):
    # מחזירה True אם המשבצת ריקה (ערך 0), אחרת False
    return board[row][col] == 0

# פונקציה לקבלת משבצות שכנות
def get_neighbors(row, col):
    # מחזירה רשימה של קואורדינטות המשבצות השכנות (מעל, מתחת, משמאל, מימין)
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
         new_row, new_col = row + dr, col + dc
         if is_valid_move(new_row, new_col):
             neighbors.append((new_row, new_col))
    return neighbors

# פונקציה לבדיקה האם משבצת של היריב ניתנת ללכידה
def can_capture(board, row, col, current_player):
    # מקבלת את מספר היריב (אם השחקן הנוכחי הוא 1, אז היריב הוא 2, ולהיפך)
    opponent_player = 3 - current_player
     # אם המשבצת אינה שייכת ליריב, אז היא אינה ניתנת ללכידה
    if board[row][col] != opponent_player:
        return False
    
    # מקבלת את המשבצות השכנות
    neighbors = get_neighbors(row, col)
    # בודקת האם משבצת היריב מוקפת במשבצות של השחקן הנוכחי
    # אם מספר המשבצות השכנות קטן מ-4, אז המשבצת אינה ניתנת ללכידה
    if len(neighbors) < 4:
        return False
    # בודקת האם כל המשבצות השכנות הן סימני השחקן הנוכחי
    for neighbor_row, neighbor_col in neighbors:
        if board[neighbor_row][neighbor_col] != current_player:
            return False
    # אם כל הבדיקות עברו, המשבצת ניתנת ללכידה
    return True

# פונקציה ללכידת משבצת
def capture_cell(board, row, col, current_player):
    # משנה את ערך המשבצת לערך של השחקן הנוכחי
    board[row][col] = current_player

# פונקציה לביצוע מהלך של השחקן
def make_move(board, row, col, current_player):
    # מניחה את סימן השחקן הנוכחי על המשבצת שנבחרה
    board[row][col] = current_player
    # מקבלת רשימה של משבצות שכנות
    neighbors = get_neighbors(row, col)
    # בודקת האם משבצת של היריב ניתנת ללכידה
    for neighbor_row, neighbor_col in neighbors:
       # אם המשבצת השכנה ניתנת ללכידה
       if can_capture(board, neighbor_row, neighbor_col, current_player):
            # לוכדת את המשבצת
           capture_cell(board, neighbor_row, neighbor_col, current_player)


# פונקציה להחלפת השחקן הנוכחי
def switch_player(current_player):
    # מחליפה את השחקן מ-1 ל-2 או מ-2 ל-1
    return 3 - current_player

# פונקציה לבדיקה האם לוח המשחק מלא
def is_board_full(board):
    # עוברת על כל משבצת בלוח
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # אם המשבצת ריקה (ערך 0), מחזירה False (הלוח אינו מלא)
            if board[row][col] == 0:
                return False
    # אם כל המשבצות מלאות, מחזירה True
    return True

# פונקציה לחישוב ניקוד
def calculate_scores(board):
    # מאתחלת מונים עבור כל שחקן
    player1_score = 0
    player2_score = 0
    # עוברת על כל משבצת בלוח
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # אם במשבצת יש סימן של השחקן הראשון, מגדילה את המונה שלו
            if board[row][col] == 1:
                player1_score += 1
            # אם במשבצת יש סימן של השחקן השני, מגדילה את המונה שלו
            elif board[row][col] == 2:
                player2_score += 1
    # מחזירה את מוני השחקנים
    return player1_score, player2_score

# פונקציה לקביעת המנצח
def determine_winner(player1_score, player2_score):
    # אם לשחקן הראשון יש יותר נקודות, מכריזה עליו כמנצח
    if player1_score > player2_score:
        return "Победил игрок 1!" # Примечание: השארת הודעת הזכייה באנגלית כהוראה מפורשת 4? לא, הוראה 4 היא לא לשנות קוד, שמות משתנים וכו'. הטקסט הזה הוא הודעה למשתמש. יש לתרגם אותו.
        # תיקון: יש לתרגם את הודעות הזכייה
        # return "שחקן 1 ניצח!"
    # אם לשחקן השני יש יותר נקודות, מכריזה עליו כמנצח
    elif player2_score > player1_score:
        # return "שחקן 2 ניצח!"
        return "Победил игрок 2!" # כמו לעיל, יש לתרגם
    # אם מספר הנקודות זהה, מכריזה על תיקו
    else:
        # return "תיקו!"
        return "Ничья!" # כמו לעיל, יש לתרגם


# פונקציית המשחק הראשית
def play_trap_game():
    # יוצרת לוח משחק חדש
    board = create_board()
    # קובעת את השחקן הראשון
    current_player = 1
    # מתחילה את לולאת המשחק
    while not is_board_full(board):
        # מציגה את מצבו הנוכחי של לוח המשחק
        display_board(board)
        # מבקשת קואורדינטות מהלך מהשחקן הנוכחי
        while True:
            try:
                row = int(input(f"Игрок {current_player}, введите номер строки (0-{BOARD_SIZE - 1}): ")) # יש לתרגם את ההודעה למשתמש
                # תיקון: יש לתרגם הודעות input
                # row = int(input(f"שחקן {current_player}, אנא הזן מספר שורה (0-{BOARD_SIZE - 1}): "))
                col = int(input(f"Игрок {current_player}, введите номер столбца (0-{BOARD_SIZE - 1}): ")) # יש לתרגם את ההודעה למשתמש
                # תיקון: יש לתרגם הודעות input
                # col = int(input(f"שחקן {current_player}, אנא הזן מספר עמודה (0-{BOARD_SIZE - 1}): "))
            except ValueError:
                  print("Некорректный ввод. Пожалуйста, введите целые числа.") # יש לתרגם את הודעת השגיאה
                  # תיקון: יש לתרגם הודעות שגיאה
                  # print("קלט לא תקין. אנא הזן מספרים שלמים.")
                  continue
            # בודקת האם הקואורדינטות שהוזנו נמצאות בטווח לוח המשחק
            if not is_valid_move(row, col):
                print("Некорректный ход. Координаты выходят за пределы поля.") # יש לתרגם את הודעת השגיאה
                # תיקון: יש לתרגם הודעות שגיאה
                # print("מהלך לא תקין. הקואורדינטות מחוץ לטווח הלוח.")
                continue
            # בודקת האם המשבצת שנבחרה ריקה
            if not is_cell_empty(board, row, col):
                print("Некорректный ход. Клетка уже занята.") # יש לתרגם את הודעת השגיאה
                # תיקון: יש לתרגם הודעות שגיאה
                # print("מהלך לא תקין. המשבצת כבר תפוסה.")
                continue
            # אם כל הבדיקות עברו, יוצאת מהלולאה הפנימית
            break
         # מבצעת את מהלך השחקן
        make_move(board, row, col, current_player)
        # מחליפה את השחקן הנוכחי
        current_player = switch_player(current_player)
    
    # מציגה את מצבו הסופי של לוח המשחק
    display_board(board)
    # מחשבת את מספר הנקודות של כל שחקן
    player1_score, player2_score = calculate_scores(board)
    # קובעת את המנצח
    winner = determine_winner(player1_score, player2_score) # הפונקציה determine_winner תוקנה לתרגום
    # מציגה את תוצאת המשחק
    print(f"Игрок 1: {player1_score} очков") # יש לתרגם את הודעת הניקוד
    # תיקון: יש לתרגם הודעת ניקוד
    # print(f"שחקן 1: {player1_score} נקודות")
    print(f"Игрок 2: {player2_score} очков") # יש לתרגם את הודעת הניקוד
    # תיקון: יש לתרגם הודעת ניקוד
    # print(f"שחקן 2: {player2_score} נקודות")
    print(winner)

# מפעילה את המשחק
if __name__ == "__main__":
    play_trap_game()
```
**הסבר הקוד:**
1.  **ייבוא מודול `copy`**:
    -   `import copy`: מייבאת את מודול `copy` ליצירת עותקים עמוקים של רשימות (לוח המשחק).
2.  **קבועים**:
    -   `BOARD_SIZE = 7`: מגדיר את גודל לוח המשחק (7x7).
3.  **פונקציה `create_board()`**:
    -   יוצרת ומחזירה לוח משחק ריק בצורת רשימה דו-ממדית, המלאה באפסים.
4.  **פונקציה `display_board(board)`**:
    -   מקבלת את לוח המשחק כארגומנט.
    -   מציגה את מצבו הנוכחי של לוח המשחק במסוף, תוך שימוש בתווים '.' עבור משבצות ריקות, '1' עבור סימני השחקן הראשון ו-'2' עבור סימני השחקן השני.
5.  **פונקציה `is_valid_move(row, col)`**:
    -   בודקת האם הקואורדינטות (row, col) נמצאות בטווח לוח המשחק.
    -   מחזירה `True` אם הקואורדינטות תקינות, אחרת `False`.
6.  **פונקציה `is_cell_empty(board, row, col)`**:
    -   בודקת האם המשבצת עם הקואורדינטות (row, col) ריקה (שווה ל-0).
    -   מחזירה `True` אם המשבצת ריקה, אחרת `False`.
7.  **פונקציה `get_neighbors(row, col)`**:
    -   מחזירה רשימה של קואורדינטות המשבצות השכנות עבור משבצת נתונה (מעל, מתחת, משמאל ומימין).
    -   מוציאה קואורדינטות החורגות מגבולות לוח המשחק.
8.  **פונקציה `can_capture(board, row, col, current_player)`**:
    -   בודקת האם משבצת של היריב (עם הקואורדינטות row, col) ניתנת ללכידה על ידי השחקן הנוכחי.
    -   מחזירה `True` אם המשבצת ניתנת ללכידה, אחרת `False`.
9.  **פונקציה `capture_cell(board, row, col, current_player)`**:
    -   לוכדת משבצת של היריב, משנה את ערכה לערך של השחקן הנוכחי.
10. **פונקציה `make_move(board, row, col, current_player)`**:
    -   מניחה את סימן השחקן הנוכחי על המשבצת שנבחרה.
    -   בודקת ולכדת משבצות שכנות של היריב, אם הן ניתנות ללכידה.
11. **פונקציה `switch_player(current_player)`**:
    -   מחליפה את השחקן הנוכחי (מ-1 ל-2 או מ-2 ל-1).
12. **פונקציה `is_board_full(board)`**:
    -   בודקת האם כל לוח המשחק מלא.
    -   מחזירה `True` אם כל המשבצות תפוסות, אחרת `False`.
13. **פונקציה `calculate_scores(board)`**:
    -   מחשבת את מספר הסימנים של כל שחקן על לוח המשחק.
    -   מחזירה את מספר הנקודות עבור כל שחקן.
14. **פונקציה `determine_winner(player1_score, player2_score)`**:
    -   קובעת את המנצח על בסיס הניקוד המחושב.
    -   מחזירה הודעה על המנצח או על תיקו.
15. **פונקציה `play_trap_game()`**:
    -   הפונקציה הראשית המנהלת את מהלך המשחק.
    -   מאתחלת את לוח המשחק, את השחקן הנוכחי, ומפעילה את לולאת המשחק הראשית.
    -   מבקשת מהלכים מהשחקנים, מעבדת אותם, בודקת תקינות, לוכדת משבצות ומחליפה שחקנים.
    -   מציגה את מצבו הנוכחי של לוח המשחק ואת תוצאות המשחק.
16. **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_trap_game()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    -   `play_trap_game()`: קוראת לפונקציה להתחלת המשחק.