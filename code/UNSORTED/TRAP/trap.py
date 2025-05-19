<TRAP>:
=================
רמת קושי: 5
-----------------
המשחק "המלכודת" הוא משחק לשני שחקנים, שבו כל שחקן בתורו מניח את הסימונים שלו (הספרות 1 ו-2) על לוח המשחק. מטרת המשחק היא להקיף תא של היריב באמצעות תאים השייכים לשחקן הנוכחי. אם שחקן מקיף תא של יריב מכל הצדדים, התא של היריב נלכד.

כללי המשחק:
1.  לוח המשחק הוא רשת ריבועית בגודל 7x7.
2.  שני שחקנים מזינים בתורם את קואורדינטות התא שבו הם רוצים למקם את הסימון שלהם (1 או 2).
3.  אם תא מוקף מכל ארבעת צדדיו בסימונים של היריב, הסימון שבו נלכד ומוחלף בסימון של השחקן הלוכד.
4.  המשחק מסתיים כאשר כל התאים תפוסים. השחקן שיש לו יותר סימונים על הלוח מנצח.
-----------------
אלגוריתם:
1.  אתחול לוח המשחק כרשת ריקה בגודל 7x7.
2.  הגדרת השחקן הנוכחי כשחקן הראשון (1).
3.  התחלת לולאת המשחק הראשית:
    3.1 הצגת המצב הנוכחי של לוח המשחק.
    3.2 בקשת קואורדינטות מהשחקן הנוכחי למיקום הסימון.
    3.3 בדיקה האם התא שנבחר ריק.
    3.4 אם התא אינו ריק, דיווח על שגיאה לשחקן וחזרה לשלב 3.2.
    3.5 מיקום סימון השחקן הנוכחי על התא שנבחר.
    3.6 בדיקה האם יש ללכוד תאים כלשהם של היריב:
        3.6.1 עבור כל תא המקיף את התא הנוכחי:
            3.6.1.1 אם התא הסמוך שייך ליריב:
                3.6.1.1.1 בדיקה האם הוא מוקף מכל הצדדים בסימונים של השחקן הנוכחי.
                3.6.1.1.2 אם מוקף, החלפת סימון היריב בסימון של השחקן הנוכחי.
    3.7 החלפת השחקן הנוכחי (מ-1 ל-2 או מ-2 ל-1).
    3.8 חזרה על הלולאה עד שכל התאים תפוסים.
4.  ספירת מספר הסימונים של כל שחקן.
5.  הכרזה על המנצח (השחקן עם מספר הסימונים הגדול ביותר).
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["אתחול לוח המשחק: 7x7 (תאים ריקים)"]
    InitializeBoard --> SetCurrentPlayer["הגדרת שחקן נוכחי: player = 1"]
    SetCurrentPlayer --> GameLoopStart{"תחילת לולאת המשחק: כל עוד לא כל התאים מלאים"}
    GameLoopStart -- כן --> DisplayBoard["הצגת המצב הנוכחי של לוח המשחק"]
    DisplayBoard --> GetMove["קלט מהלך שחקן: קואורדינטות תא (row, col)"]
    GetMove --> ValidateMove{"בדיקה: האם התא (row, col) ריק?"}
    ValidateMove -- לא --> DisplayError["הצגת הודעת שגיאה: התא תפוס"]
    DisplayError --> GetMove
    ValidateMove -- כן --> PlaceMove["מיקום סימון השחקן הנוכחי על התא (row, col)"]
    PlaceMove --> CheckCaptureStart{"תחילת לולאת בדיקת לכידה לתאים סמוכים"}
    CheckCaptureStart --> CheckNeighbors{"בדיקת תאים סמוכים"}
     CheckNeighbors -- תא סמוך שייך ליריב --> CheckSurrounded{"בדיקה: האם התא של היריב מוקף בסימוני השחקן הנוכחי?"}
       CheckSurrounded -- כן --> CaptureCell["לכידת תא היריב"]
        CaptureCell --> CheckCaptureEnd["סיום לולאת בדיקת לכידה"]
        CheckSurrounded -- לא --> CheckCaptureEnd
     CheckNeighbors -- תא סמוך לא שייך ליריב --> CheckCaptureEnd
    CheckCaptureEnd --> SwitchPlayer["החלפת שחקן נוכחי: אם player=1, אז player=2, אחרת player=1"]
    SwitchPlayer --> CheckBoardFull{"בדיקה: האם כל התאים בלוח מלאים?"}
    CheckBoardFull -- לא --> GameLoopStart
     CheckBoardFull -- כן --> CalculateScores["ספירת מספר הסימונים של כל שחקן"]
    CalculateScores --> DetermineWinner["קביעת המנצח"]
    DetermineWinner --> End["סיום המשחק"]
    GameLoopStart -- לא --> End
```
**מקרא:**
    התחלה - תחילת המשחק.
    אתחול לוח המשחק - יצירת רשת 7x7 ומילוי התאים בתאים ריקים.
    הגדרת שחקן נוכחי - קביעת השחקן הנוכחי כשחקן הראשון (1).
    תחילת לולאת המשחק - תחילת לולאת המשחק הראשית, שממשיכה כל עוד לא כל התאים על הלוח מלאים.
    הצגת המצב הנוכחי של לוח המשחק - הצגת המצב הנוכחי של לוח המשחק בקונסולה.
    קלט מהלך שחקן - בקשת קואורדינטות התא (שורה ועמודה) מהשחקן הנוכחי, שבו הוא רוצה לשים את הסימון שלו.
    בדיקה: האם התא ריק? - בדיקה האם התא הנבחר ריק.
    הצגת הודעת שגיאה - הצגת הודעת שגיאה אם התא הנבחר כבר תפוס.
    מיקום סימון השחקן הנוכחי - מיקום סימון השחקן הנוכחי על התא הנבחר.
    תחילת לולאת בדיקת לכידה - תחילת לולאת בדיקת לכידת תאי יריב.
    בדיקת תאים סמוכים - בדיקת התאים הסמוכים סביב הסימון שהונח זה עתה.
    בדיקה: האם התא של היריב מוקף? - בדיקה האם תא סמוך של יריב מוקף מכל הצדדים בסימונים של השחקן הנוכחי.
    לכידת תא היריב - לכידת תא של יריב, והחלפתו בסימון של השחקן הנוכחי.
    סיום לולאת בדיקת לכידה - סיום לולאת בדיקת לכידת תאים.
    החלפת שחקן נוכחי - החלפת השחקן הנוכחי: אם השחקן היה 1, הוא הופך ל-2, ולהיפך.
    בדיקה: האם כל התאים בלוח מלאים? - בדיקה האם כל התאים על לוח המשחק מלאים.
    ספירת מספר הסימונים של כל שחקן - ספירת מספר התאים שתפוסים על ידי כל שחקן.
    קביעת המנצח - קביעת המנצח בהתבסס על ספירת התאים התפוסים.
    סיום המשחק - סיום המשחק.
"""
import copy

# גודל לוח המשחק
BOARD_SIZE = 7

# פונקציה ליצירת לוח משחק ריק
def create_board():
    # יוצרים רשימה דו-ממדית שמייצגת את לוח המשחק, ממולאת באפסים (תאים ריקים)
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# פונקציה להצגת המצב הנוכחי של לוח המשחק
def display_board(board):
    # מציגים את מספרי העמודות
    print("  ", end="")
    for col in range(BOARD_SIZE):
        print(f"{col} ", end="")
    print()
    # עבור כל שורה בלוח המשחק
    for row in range(BOARD_SIZE):
        # מציגים את מספר השורה
        print(f"{row} ", end="")
        # עבור כל תא בשורה הנוכחית
        for col in range(BOARD_SIZE):
             # מציגים את תוכן התא, מחליפים 0 ב'.', 1 ב-'1', 2 ב-'2'
            print(f"{'.' if board[row][col] == 0 else str(board[row][col])} ", end="")
        # מעבר לשורה חדשה
        print()


# פונקציה לבדיקה האם קואורדינטה נמצאת בתוך גבולות לוח המשחק
def is_valid_move(row, col):
    # בודקים האם הקואורדינטות נמצאות בטווח החוקי (מ-0 עד BOARD_SIZE - 1)
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

# פונקציה לבדיקה האם תא ריק
def is_cell_empty(board, row, col):
    # מחזירים True אם התא ריק (ערך 0), אחרת False
    return board[row][col] == 0

# פונקציה לקבלת תאים סמוכים
def get_neighbors(row, col):
    # מחזירה רשימה של קואורדינטות התאים הסמוכים (מלמעלה, מלמטה, משמאל, מימין)
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
         new_row, new_col = row + dr, col + dc
         if is_valid_move(new_row, new_col):
             neighbors.append((new_row, new_col))
    return neighbors

# פונקציה לבדיקה האם תא יריב יכול להילכד
def can_capture(board, row, col, current_player):
    # מקבלים את מספר היריב (אם השחקן הנוכחי 1, היריב הוא 2, ולהיפך)
    opponent_player = 3 - current_player
     # אם התא לא שייך ליריב, הוא לא יכול להילכד
    if board[row][col] != opponent_player:
        return False
    
    # מקבלים את התאים הסמוכים
    neighbors = get_neighbors(row, col)
    # בודקים האם תא היריב מוקף בסימונים של השחקן הנוכחי
    # אם יש פחות מ-4 תאים סמוכים, התא לא יכול להילכד
    if len(neighbors) < 4:
        return False
    # בודקים האם כל התאים הסמוכים הם סימונים של השחקן הנוכחי
    for neighbor_row, neighbor_col in neighbors:
        if board[neighbor_row][neighbor_col] != current_player:
            return False
    # אם כל הבדיקות עברו, התא יכול להילכד
    return True

# פונקציה ללכידת תא
def capture_cell(board, row, col, current_player):
    # משנים את ערך התא לערך של השחקן הנוכחי
    board[row][col] = current_player

# פונקציה לביצוע מהלך שחקן
def make_move(board, row, col, current_player):
    # ממקמים את הסימון של השחקן הנוכחי על התא הנבחר
    board[row][col] = current_player
    # מקבלים רשימה של תאים סמוכים
    neighbors = get_neighbors(row, col)
    # בודקים האם תא יריב יכול להילכד
    for neighbor_row, neighbor_col in neighbors:
       # אם התא הסמוך יכול להילכד
       if can_capture(board, neighbor_row, neighbor_col, current_player):
            # לוכדים את התא
           capture_cell(board, neighbor_row, neighbor_col, current_player)


# פונקציה להחלפת השחקן הנוכחי
def switch_player(current_player):
    # מחליפים את השחקן מ-1 ל-2 או מ-2 ל-1
    return 3 - current_player

# פונקציה לבדיקה האם לוח המשחק מלא
def is_board_full(board):
    # עוברים על כל תא בלוח
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # אם התא ריק (ערך 0), מחזירים False (הלוח לא מלא)
            if board[row][col] == 0:
                return False
    # אם כל התאים מלאים, מחזירים True
    return True

# פונקציה לספירת נקודות
def calculate_scores(board):
    # מאתחלים מוני לכל שחקן
    player1_score = 0
    player2_score = 0
    # עוברים על כל תא בלוח
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # אם בתא יש סימון של השחקן הראשון, מגדילים את המונה שלו
            if board[row][col] == 1:
                player1_score += 1
            # אם בתא יש סימון של השחקן השני, מגדילים את המונה שלו
            elif board[row][col] == 2:
                player2_score += 1
    # מחזירים את מוני השחקנים
    return player1_score, player2_score

# פונקציה לקביעת המנצח
def determine_winner(player1_score, player2_score):
    # אם לשחקן הראשון יש יותר נקודות, מכריזים עליו כמנצח
    if player1_score > player2_score:
        return "השחקן 1 ניצח!"
    # אם לשחקן השני יש יותר נקודות, מכריזים עליו כמנצח
    elif player2_score > player1_score:
        return "השחקן 2 ניצח!"
    # אם מספר הנקודות זהה, מכריזים על תיקו
    else:
        return "תיקו!"


# פונקציית המשחק הראשית
def play_trap_game():
    # יוצרים לוח משחק חדש
    board = create_board()
    # מגדירים את השחקן הראשון
    current_player = 1
    # מתחילים את לולאת המשחק
    while not is_board_full(board):
        # מציגים את המצב הנוכחי של לוח המשחק
        display_board(board)
        # מבקשים את קואורדינטות המהלך מהשחקן הנוכחי
        while True:
            try:
                row = int(input(f"שחקן {current_player}, הזן מספר שורה (0-{BOARD_SIZE - 1}): "))
                col = int(input(f"שחקן {current_player}, הזן מספר עמודה (0-{BOARD_SIZE - 1}): "))
            except ValueError:
                  print("קלט לא תקין. נא להזין מספרים שלמים.")
                  continue
            # בודקים האם הקואורדינטות שהוזנו נמצאות בתוך גבולות לוח המשחק
            if not is_valid_move(row, col):
                print("מהלך לא תקין. קואורדינטות מחוץ לגבולות הלוח.")
                continue
            # בודקים האם התא הנבחר ריק
            if not is_cell_empty(board, row, col):
                print("מהלך לא תקין. התא כבר תפוס.")
                continue
            # אם כל הבדיקות עברו, יוצאים מהלולאה הפנימית
            break
         # מבצעים את מהלך השחקן
        make_move(board, row, col, current_player)
        # מחליפים את השחקן הנוכחי
        current_player = switch_player(current_player)
    
    # מציגים את המצב הסופי של לוח המשחק
    display_board(board)
    # סופרים את מספר הנקודות של כל שחקן
    player1_score, player2_score = calculate_scores(board)
    # קובעים את המנצח
    winner = determine_winner(player1_score, player2_score)
    # מציגים את תוצאת המשחק
    print(f"שחקן 1: {player1_score} נקודות")
    print(f"שחקן 2: {player2_score} נקודות")
    print(winner)

# מפעילים את המשחק
if __name__ == "__main__":
    play_trap_game()
"""
הסבר קוד:
1. **ייבוא מודול `copy`**:
   - `import copy`: מייבא את מודול `copy` ליצירת עותקים עמוקים (deep copies) של רשימות (לוח המשחק).
2. **קבועים**:
   - `BOARD_SIZE = 7`: מגדיר את גודל לוח המשחק (7x7).
3. **פונקציה `create_board()`**:
   - יוצרת ומחזירה לוח משחק ריק בתור רשימה דו-ממדית, שממולאת באפסים.
4. **פונקציה `display_board(board)`**:
    - מקבלת את לוח המשחק כארגומנט.
    - מציגה את המצב הנוכחי של לוח המשחק בקונסולה, באמצעות התו '.' לתאים ריקים, '1' לסימוני השחקן הראשון ו-'2' לסימוני השחקן השני.
5.  **פונקציה `is_valid_move(row, col)`**:
   - בודקת האם הקואורדינטות (row, col) נמצאות בתוך גבולות לוח המשחק.
   - מחזירה `True` אם הקואורדינטות חוקיות, אחרת `False`.
6.  **פונקציה `is_cell_empty(board, row, col)`**:
    - בודקת האם התא עם הקואורדינטות (row, col) ריק (שווה ל-0).
    - מחזירה `True` אם התא ריק, אחרת `False`.
7.  **פונקציה `get_neighbors(row, col)`**:
    - מחזירה רשימה של קואורדינטות התאים הסמוכים לתא הנתון (מלמעלה, מלמטה, משמאל ומימין).
    - מתעלמת מקואורדינטות היוצאות מחוץ לגבולות לוח המשחק.
8.  **פונקציה `can_capture(board, row, col, current_player)`**:
   - בודקת האם תא יריב (עם הקואורדינטות row, col) יכול להילכד על ידי השחקן הנוכחי.
   - מחזירה `True` אם התא יכול להילכד, אחרת `False`.
9.  **פונקציה `capture_cell(board, row, col, current_player)`**:
    - לוכדת תא יריב, ומשנה את ערכו לערך של השחקן הנוכחי.
10. **פונקציה `make_move(board, row, col, current_player)`**:
     - ממקמת את הסימון של השחקן הנוכחי על התא הנבחר.
     - בודקת ולוכדת תאים סמוכים של יריב, אם הם יכולים להילכד.
11. **פונקציה `switch_player(current_player)`**:
    - מחליפה את השחקן הנוכחי (מ-1 ל-2 או מ-2 ל-1).
12. **פונקציה `is_board_full(board)`**:
    - בודקת האם כל לוח המשחק מלא.
    - מחזירה `True` אם כל התאים תפוסים, אחרת `False`.
13. **פונקציה `calculate_scores(board)`**:
    - סופרת את מספר הסימונים של כל שחקן על לוח המשחק.
    - מחזירה את מספר הנקודות עבור כל שחקן.
14. **פונקציה `determine_winner(player1_score, player2_score)`**:
    - קובעת את המנצח בהתבסס על הנקודות שנספרו.
    - מחזירה הודעה על המנצח או על תיקו.
15. **פונקציה `play_trap_game()`**:
    - הפונקציה הראשית, שמנהלת את מהלך המשחק.
    - מאתחלת את לוח המשחק, את השחקן הנוכחי, ומפעילה את לולאת המשחק הראשית.
    - מבקשת את מהלכי השחקנים, מעבדת אותם, בודקת תקינות, לוכדת תאים ומחליפה שחקנים.
    - מציגה את המצב הנוכחי של לוח המשחק ואת תוצאות המשחק.
16. **הפעלת המשחק**:
   -  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_trap_game()` תורץ רק אם הקובץ מורץ ישירות, ולא אם הוא מיובא כמודול.
   -  `play_trap_game()`: קוראת לפונקציה לתחילת המשחק.
"""