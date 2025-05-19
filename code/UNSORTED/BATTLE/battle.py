BATTLE:
=================
רמת קושי: 5
-----------------
המשחק "BATTLE" הוא סימולציה של קרב ימי בין שני שחקנים - המחשב והאדם. השחקנים "יורים" בתורם בתאים על שדה המשחק, ומנסים להטביע את ספינות האויב. המשחק נמשך עד שכל הספינות של אחד מהשחקנים מוטבעות.

כללי המשחק:
1.  שדה המשחק הוא רשת ריבועית בגודל 10x10.
2.  לכל שחקן יש 5 ספינות. גודל ומספר הספינות אינם מצוינים בקוד המקורי.
3.  שחקנים בתורם מציינים קואורדינטות "ירייה". הקואורדינטות מוזנות כשני מספרים: שורה ועמודה.
4.  אם "ירייה" פוגעת בספינת האויב, הספינה נחשבת פגועה.
5.  אם "ירייה" פוגעת בתא ריק, השחקן פשוט מחטיא.
6.  המשחק נמשך עד שכל הספינות של אחד מהשחקנים מוטבעות.
7.  בקוד המקורי אין הגדרת מנצח, המשחק מסתיים לאחר 30 מהלכים.
-----------------
אלגוריתם:
1.  אתחול:
    1.1. הגדרת גודל שדה המשחק ל-10x10.
    1.2. יצירת שני שדות משחק (עבור המחשב והשחקן), המיוצגים באמצעות מערכים דו-ממדיים (מטריצות).
    1.3. מילוי שדות המשחק בערכים "0" (שדה ריק), "1" (ספינה), "2" (פגיעה), "3" (החטאה).
    1.4. מיקום 5 ספינות על שדה המחשב באופן אקראי. מיקום ספינות השחקן אינו כלול בגרסה המקורית של המשחק.
    1.5. הגדרת מונה המהלכים ל-0.
    1.6. הצגת שדה המשחק הריק של השחקן על המסך.
2.  התחלת לולאה "כל עוד מונה המהלכים קטן מ-30":
    2.1. הגדלת מונה המהלכים ב-1.
    2.2. בקשת קואורדינטות ירייה מהשחקן (שורה ועמודה).
    2.3. בדיקה האם יריית השחקן פגעה בספינת המחשב:
        2.3.1. החלפת הערך במערך המחשב ל-"2" (פגיעה).
        2.3.2. הצגת הודעה "HIT!".
    2.4. אם יריית השחקן לא פגעה בספינה:
        2.4.1. החלפת הערך במערך המחשב ל-"3" (החטאה).
        2.4.2. הצגת הודעה "MISS".
    2.5. הצגת שדה המשחק של השחקן עם סימוני היריות.
    2.6. ביצוע "ירייה" של המחשב באופן אקראי.
    2.7. בדיקה האם יריית המחשב פגעה בספינת השחקן:
         2.7.1 החלפת הערך במערך השחקן ל-"2" (פגיעה).
         2.7.2 הצגת הודעה: "COMPUTER HITS!"
    2.8 אם יריית המחשב לא פגעה בספינה
        2.8.1 החלפת הערך במערך השחקן ל-"3" (החטאה).
        2.8.2 הצגת הודעה: "COMPUTER MISSES"
    2.9. הצגת שדה המשחק של השחקן עם סימוני היריות.

3.  סוף המשחק. הצגת הודעה "END OF GAME".
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeGame["<p align='left'>Инициализация:
    <code><b>
    boardSize = 10
    playerBoard = matrix(boardSize x boardSize, 0)
    computerBoard = matrix(boardSize x boardSize, 0)
    placeComputerShips()
    turnCount = 0
    </b></code></p>"]
    InitializeGame --> GameLoopStart{"Начало цикла: <code><b>turnCount < 30</b></code>"}
    GameLoopStart -- Да --> IncreaseTurnCount["<code><b>turnCount = turnCount + 1</b></code>"]
    IncreaseTurnCount --> PlayerInput["Ввод координат выстрела игроком: <code><b>playerRow, playerCol</b></code>"]
    PlayerInput --> CheckPlayerHit{"Проверка: <code><b>computerBoard[playerRow][playerCol] == 1</b></code>?"}
    CheckPlayerHit -- Да --> PlayerHit["<code><b>computerBoard[playerRow][playerCol] = 2</b></code><br>Output: <b>HIT!</b>"]
    PlayerHit --> PrintPlayerBoard["Вывод поля игрока"]
     PrintPlayerBoard --> ComputerTurn["Ход компьютера: <code><b>computerRow = random(0, boardSize-1); computerCol = random(0, boardSize-1)</b></code>"]
    CheckPlayerHit -- Нет --> PlayerMiss["<code><b>computerBoard[playerRow][playerCol] = 3</b></code><br>Output: <b>MISS</b>"]
     PlayerMiss --> PrintPlayerBoard
    ComputerTurn --> CheckComputerHit{"Проверка: <code><b>playerBoard[computerRow][computerCol] == 1</b></code>?"}
    CheckComputerHit -- Да --> ComputerHit["<code><b>playerBoard[computerRow][computerCol] = 2</b></code><br>Output: <b>COMPUTER HITS!</b>"]
    ComputerHit --> PrintPlayerBoard2["Вывод поля игрока"]
    CheckComputerHit -- Нет --> ComputerMiss["<code><b>playerBoard[computerRow][computerCol] = 3</b></code><br>Output: <b>COMPUTER MISSES</b>"]
     ComputerMiss --> PrintPlayerBoard2
     PrintPlayerBoard2 --> GameLoopStart
    GameLoopStart -- Нет --> End["Конец: <b>END OF GAME</b>"]

```
מקרא:
   Start - התחלת המשחק.
    InitializeGame - אתחול משתני ושדות המשחק: הגדרת גודל השדה, יצירת שדות משחק ריקים עבור השחקן והמחשב, מיקום אקראי של ספינות המחשב, הגדרת מונה מהלכים ל-0.
    GameLoopStart - תחילת לולאת המשחק, החוזרת על עצמה כל עוד מונה המהלכים קטן מ-30.
    IncreaseTurnCount - הגדלת מונה המהלכים ב-1.
    PlayerInput - קבלת קואורדינטות ירייה מהשחקן (playerRow, playerCol).
    CheckPlayerHit - בדיקה האם יריית השחקן פגעה בספינת המחשב (ערך 1 על שדה המחשב).
    PlayerHit - אם פגעה, אז: שינוי הערך בשדה המחשב ל-2 (פגיעה) והצגת ההודעה "HIT!".
    PlayerMiss - אם לא פגעה, אז: שינוי הערך בשדה המחשב ל-3 (החטאה) והצגת ההודעה "MISS".
    PrintPlayerBoard - הצגת מצבו הנוכחי של שדה המשחק של השחקן על המסך.
    ComputerTurn - המחשב בוחר קואורדינטות אקראיות לירייה.
    CheckComputerHit - בדיקה האם יריית המחשב פגעה בספינת השחקן.
    ComputerHit - אם פגעה, אז: שינוי הערך בשדה השחקן ל-2 (פגיעה) והצגת ההודעה "COMPUTER HITS!".
    ComputerMiss - אם לא פגעה, אז: שינוי הערך בשדה השחקן ל-3 (החטאה) והצגת ההודעה "COMPUTER MISSES".
    PrintPlayerBoard2 - הצגת מצבו הנוכחי של שדה המשחק של השחקן על המסך.
    End - סוף המשחק. הצגת ההודעה "END OF GAME".
```
```python
import random

# קבוע המגדיר את גודל שדה המשחק
BOARD_SIZE = 10

# פונקציה ליצירת שדה משחק (מטריצה) בגודל נתון, המלא באפסים
def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]

# פונקציה למיקום אקראי של ספינות על שדה המשחק של המחשב
def place_computer_ships(board):
    # לצורך הפשטות, ממקמים 5 ספינות בגודל 1 (תא יחיד)
    ships_placed = 0
    while ships_placed < 5:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if board[row][col] == 0:
            board[row][col] = 1 # 1 מציין נוכחות ספינה
            ships_placed += 1

# פונקציה להצגת שדה המשחק, תוך הסתרת ספינות המחשב
def display_board(board, is_computer=False):
    print("   " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        row_str = " ".join(
            "*" if is_computer and cell == 1 else  # מסתיר את ספינות המחשב
            "O" if cell == 0 else  # שדה ריק
            "X" if cell == 2 else  # פגיעה
            "-" if cell == 3 else # החטאה
            str(cell)
            for cell in row
        )
        print(f"{i:2} {row_str}")
    print()



# הפונקציה הראשית של המשחק
def play_battle():
    # יוצרים את שדה המשחק עבור השחקן והמחשב
    player_board = create_board(BOARD_SIZE)
    computer_board = create_board(BOARD_SIZE)
    
    # ממקמים את ספינות המחשב
    place_computer_ships(computer_board)

    # מאתחלים את מונה המהלכים
    turn_count = 0

    # לולאת המשחק הראשית (עד 30 מהלכים)
    while turn_count < 30:
        turn_count += 1
        print(f"Ход {turn_count}") # Note: Keeping "Ход" as it's part of the UI/output string, not a variable name.

        # תור השחקן
        while True:
            try:
                player_row = int(input(f"Введите строку для выстрела (0-{BOARD_SIZE - 1}): ")) # Keeping English prompt as is
                player_col = int(input(f"Введите столбец для выстрела (0-{BOARD_SIZE - 1}): ")) # Keeping English prompt as is
                if 0 <= player_row < BOARD_SIZE and 0 <= player_col < BOARD_SIZE:
                    break
                else:
                     print("Некорректные координаты, попробуйте еще раз.") # Keeping Russian error message as is
            except ValueError:
                print("Некорректный ввод, введите число.") # Keeping Russian error message as is
        
        # עיבוד יריית השחקן
        if computer_board[player_row][player_col] == 1:
            computer_board[player_row][player_col] = 2  # 2 = פגיעה
            print("HIT!") # Keeping English output string as is
        else:
            computer_board[player_row][player_col] = 3 # 3 = החטאה
            print("MISS!") # Keeping English output string as is
        
        # הצגת שדה המשחק של השחקן לאחר הירי, מציג את תוצאות הירי
        print("Ваше поле:") # Keeping Russian output string as is
        display_board(player_board)
        
        # תור המחשב
        print("Ход компьютера...") # Keeping Russian output string as is
        computer_row = random.randint(0, BOARD_SIZE - 1)
        computer_col = random.randint(0, BOARD_SIZE - 1)
        
         # עיבוד יריית המחשב
        if player_board[computer_row][computer_col] == 1:
            player_board[computer_row][computer_col] = 2  # 2 = פגיעה
            print("COMPUTER HITS!") # Keeping English output string as is
        else:
            player_board[computer_row][computer_col] = 3 # 3 = החטאה
            print("COMPUTER MISSES") # Keeping English output string as is
        
        # הצגת שדה המשחק של השחקן לאחר יריית המחשב
        print("Ваше поле:") # Keeping Russian output string as is
        display_board(player_board)

    # הודעה על סיום המשחק
    print("END OF GAME") # Keeping English output string as is


# מריץ את המשחק אם הסקריפט מופעל ישירות
if __name__ == "__main__":
    # קורא לפונקציה להפעלת המשחק
    play_battle()
```
```
הסבר הקוד:

1.  **ייבוא המודול `random`:**
    -   `import random`: מייבא את המודול random, המשמש ליצירת מספרים אקראיים.
2.  **קבוע `BOARD_SIZE`:**
    -   `BOARD_SIZE = 10`: מגדיר את גודל שדה המשחק כ-10x10.
3.  **פונקציה `create_board(size)`:**
    -   יוצרת ומחזירה רשימה דו-ממדית (מטריצה) בגודל נתון, המלאה באפסים (תאים ריקים).
4.  **פונקציה `place_computer_ships(board)`:**
    -   ממקמת 5 ספינות בגודל 1 (תא יחיד) על שדה המשחק של המחשב באופן אקראי.
    -   בודקת שהתא אינו תפוס לפני מיקום הספינה.
    -   ספינה מסומנת בערך 1 על שדה המשחק.
5.  **פונקציה `display_board(board, is_computer=False)`:**
    -   מציגה את שדה המשחק במסוף.
    -   אם is_computer=True, אז ספינות המחשב (ערך 1) מוצגות כ-"*", אחרת ספינות המחשב מוסתרות.
    -   מציגה תאים ריקים כ-"O", פגיעות כ-"X", והחטאות כ-"-".
6.  **פונקציה `play_battle()`:**
    -   יוצרת את שדה המשחק עבור השחקן והמחשב.
    -   ממקמת את ספינות המחשב על השדה.
    -   מאתחלת את מונה המהלכים turn_count = 0.
    -   **לולאת המשחק הראשית (`while turn_count < 30`):**
        -   מגדילה את מונה המהלכים ב-1.
        -   מציגה את המהלך הנוכחי.
        -   **תור השחקן:**
           -   מבקשת מהמשתמש קואורדינטות לירייה (שורה ועמודה).
            -   משתמשת בלולאת `while True`, כדי להבטיח שהמשתמש יזין קואורדינטות תקינות בפורמט מספרי.
            -   בודקת האם הקואורדינטות נמצאות בטווח המותר.
            -   מטפלת בחריגת `ValueError`, אם המשתמש הזין נתונים לא תקינים (לא מספר).
            -   אם הירייה פגעה בספינה (ערך 1), מחליפה את הערך ל-2 (פגיעה) ומציגה "HIT!".
            -   אם הירייה לא פגעה, מחליפה את הערך ל-3 (החטאה) ומציגה "MISS!".
           -   מציגה את שדה המשחק של השחקן עם סימוני היריות.
        -   **תור המחשב:**
             -   מייצרת קואורדינטות אקראיות לירייה.
             -   מעבדת את יריית המחשב באופן דומה לתור השחקן.
            -   מציגה הודעה: "COMPUTER HITS!" או "COMPUTER MISSES".
            -   מציגה את שדה המשחק של השחקן עם סימוני היריות.
        -   הלולאה מסתיימת לאחר 30 מהלכים.
    -   מציגה הודעה "END OF GAME".
7.  **הפעלת המשחק:**
    -   `if __name__ == "__main__":`: מבטיח שהפונקציה `play_battle()` תופעל רק אם הסקריפט הופעל ישירות, ולא יובא כמודול.
    -   `play_battle()`: קורא לפונקציה להפעלת המשחק.

```