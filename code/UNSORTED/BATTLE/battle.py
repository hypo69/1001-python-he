BATTLE:
=================
מורכבות: 5
-----------------
המשחק "BATTLE" הוא סימולציה של קרב ימי בין שני שחקנים – המחשב והאדם. השחקנים "יורים" בתורות על תאים בשדה המשחק, בניסיון להטביע את ספינות היריב. המשחק נמשך עד שכל הספינות של אחד השחקנים מוטבעות.

כללי המשחק:
1.  שדה המשחק הוא רשת ריבועית בגודל 10x10.
2.  לכל שחקן יש 5 ספינות. גודל ומספר הספינות אינם מצוינים בקוד המקורי.
3.  השחקנים בתורות מציינים קואורדינטות "ירייה". הקואורדינטות מוזנות כשני מספרים: שורה ועמודה.
4.  אם "ירייה" פוגעת בספינת אויב, הספינה נחשבת לפגועה.
5.  אם "ירייה" פוגעת בתא ריק, השחקן מחטיא.
6.  המשחק נמשך עד שכל הספינות של אחד השחקנים מוטבעות.
7.  בקוד המקורי אין הגדרה של מנצח, המשחק מסתיים לאחר 30 מהלכים.
-----------------
אלגוריתם:
1.  אתחול:
    1.1. קביעת גודל שדה המשחק ל-10x10.
    1.2. יצירת שני שדות משחק (עבור המחשב ועבור השחקן), המיוצגים על ידי מערכים דו-ממדיים (מטריצות).
    1.3. מילוי שדות המשחק בערכים "0" (שדה ריק), "1" (ספינה), "2" (פגיעה), "3" (החטאה).
    1.4. מיקום 5 ספינות בשדה המחשב באופן אקראי. מיקום ספינות השחקן אינו מתוכנן בגרסה המקורית של המשחק.
    1.5. קביעת מונה מהלכים ל-0.
    1.6. הצגת שדה המשחק הריק של השחקן על המסך.
2.  התחלת לולאה "כל עוד מונה המהלכים קטן מ-30":
    2.1. הגדלת מונה המהלכים ב-1.
    2.2. בקשת קואורדינטות ירייה מהשחקן (שורה ועמודה).
    2.3. בדיקה, אם יריית השחקן פגעה בספינת המחשב:
        2.3.1. החלפת הערך במערך המחשב ל-"2" (פגיעה).
        2.3.2. הצגת ההודעה "HIT!".
    2.4. אם יריית השחקן לא פגעה בספינה:
        2.4.1. החלפת הערך במערך המחשב ל-"3" (החטאה).
        2.4.2. הצגת ההודעה "MISS".
    2.5. הצגת שדה המשחק של השחקן עם סימני הירייה על המסך.
    2.6. ביצוע "ירייה" של המחשב באופן אקראי.
    2.7. בדיקה, אם יריית המחשב פגעה בספינת השחקן:
         2.7.1 החלפת הערך במערך השחקן ל-"2" (פגיעה).
         2.7.2 הצגת ההודעה: "COMPUTER HITS!"
    2.8 אם יריית המחשב לא פגעה בספינה
        2.8.1 החלפת הערך במערך השחקן ל-"3" (החטאה).
        2.8.2 הצגת ההודעה: "COMPUTER MISSES"
    2.9. הצגת שדה המשחק של השחקן עם סימני הירייה על המסך.

3.  סוף המשחק. הצגת ההודעה "END OF GAME".
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["<p align='left'>אתחול:
    <code><b>
    boardSize = 10
    playerBoard = matrix(boardSize x boardSize, 0)
    computerBoard = matrix(boardSize x boardSize, 0)
    placeComputerShips()
    turnCount = 0
    </b></code></p>"]
    InitializeGame --> GameLoopStart{"תחילת לולאה: <code><b>turnCount < 30</b></code>"}
    GameLoopStart -- כן --> IncreaseTurnCount["<code><b>turnCount = turnCount + 1</b></code>"]
    IncreaseTurnCount --> PlayerInput["קלט קואורדינטות ירייה של השחקן: <code><b>playerRow, playerCol</b></code>"]
    PlayerInput --> CheckPlayerHit{"בדיקה: <code><b>computerBoard[playerRow][playerCol] == 1</b></code>?"}
    CheckPlayerHit -- כן --> PlayerHit["<code><b>computerBoard[playerRow][playerCol] = 2</b></code><br>פלט: <b>HIT!</b>"]
    PlayerHit --> PrintPlayerBoard["הצגת שדה המשחק של השחקן"]
     PrintPlayerBoard --> ComputerTurn["מהלך המחשב: <code><b>computerRow = random(0, boardSize-1); computerCol = random(0, boardSize-1)</b></code>"]
    CheckPlayerHit -- לא --> PlayerMiss["<code><b>computerBoard[playerRow][playerCol] = 3</b></code><br>פלט: <b>MISS</b>"]
     PlayerMiss --> PrintPlayerBoard
    ComputerTurn --> CheckComputerHit{"בדיקה: <code><b>playerBoard[computerRow][computerCol] == 1</b></code>?"}
    CheckComputerHit -- כן --> ComputerHit["<code><b>playerBoard[computerRow][computerCol] = 2</b></code><br>פלט: <b>COMPUTER HITS!</b>"]
    ComputerHit --> PrintPlayerBoard2["הצגת שדה המשחק של השחקן"]
    CheckComputerHit -- לא --> ComputerMiss["<code><b>playerBoard[computerRow][computerCol] = 3</b></code><br>פלט: <b>COMPUTER MISSES</b>"]
     ComputerMiss --> PrintPlayerBoard2
     PrintPlayerBoard2 --> GameLoopStart
    GameLoopStart -- לא --> End["סוף: <b>END OF GAME</b>"]

```
מקרא:
   Start - התחלת המשחק.
    InitializeGame - אתחול משתני ושטחי המשחק: נקבע גודל השדה, נוצרים שדות משחק ריקים לשחקן ולמחשב, ממוקמות ספינות המחשב באופן אקראי, מונה המהלכים מאופס.
    GameLoopStart - תחילת לולאת המשחק, החוזרת על עצמה כל עוד מונה המהלכים קטן מ-30.
    IncreaseTurnCount - הגדלת מונה המהלכים ב-1.
    PlayerInput - קבלת קואורדינטות ירייה מהשחקן (playerRow, playerCol).
    CheckPlayerHit - בדיקה האם יריית השחקן פגעה בספינת המחשב (ערך 1 בשדה המחשב).
    PlayerHit - אם פגע, אז: הערך בשדה המחשב משתנה ל-2 (פגיעה) ומוצגת ההודעה "HIT!".
    PlayerMiss - אם לא פגע, אז: הערך בשדה המחשב משתנה ל-3 (החטאה) ומוצגת ההודעה "MISS".
    PrintPlayerBoard - הצגת המצב הנוכחי של שדה המשחק של השחקן על המסך.
    ComputerTurn - המחשב בוחר קואורדינטות אקראיות לירייה.
    CheckComputerHit - בדיקה האם יריית המחשב פגעה בספינת השחקן.
    ComputerHit - אם פגע, אז: הערך בשדה השחקן משתנה ל-2 (פגיעה) ומוצגת ההודעה "COMPUTER HITS!".
    ComputerMiss - אם לא פגע, אז: הערך בשדה השחקן משתנה ל-3 (החטאה) ומוצגת ההודעה "COMPUTER MISSES".
    PrintPlayerBoard2 - הצגת המצב הנוכחי של שדה המשחק של השחקן על המסך.
    End - סוף המשחק. מוצגת ההודעה "END OF GAME".
```
```python
import random

# קבוע המגדיר את גודל שדה המשחק
BOARD_SIZE = 10

# פונקציה ליצירת שדה משחק (מטריצה) בגודל נתון, הממולא באפסים
def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]

# פונקציה למיקום אקראי של ספינות בשדה המשחק של המחשב
def place_computer_ships(board):
    # לשם הפשטות, ממקמים 5 ספינות בגודל 1 (תא בודד)
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
            "*" if is_computer and cell == 1 else  # מסתירים את ספינות המחשב
            "O" if cell == 0 else  # שדה ריק
            "X" if cell == 2 else  # פגיעה
            "-" if cell == 3 else # החטאה
            str(cell)
            for cell in row
        )
        print(f"{i:2} {row_str}")
    print()



# פונקציית המשחק הראשית
def play_battle():
    # יוצרים שדה משחק עבור השחקן ועבור המחשב
    player_board = create_board(BOARD_SIZE)
    computer_board = create_board(BOARD_SIZE)
    
    # ממקמים את ספינות המחשב
    place_computer_ships(computer_board)

    # מאתחלים את מונה המהלכים
    turn_count = 0

    # לולאת המשחק הראשית (עד 30 מהלכים)
    while turn_count < 30:
        turn_count += 1
        print(f"מהלך {turn_count}")
        
        # מהלך השחקן
        while True:
            try:
                player_row = int(input(f"הכנס שורה לירייה (0-{BOARD_SIZE - 1}): "))
                player_col = int(input(f"הכנס עמודה לירייה (0-{BOARD_SIZE - 1}): "))
                if 0 <= player_row < BOARD_SIZE and 0 <= player_col < BOARD_SIZE:
                    break
                else:
                     print("קואורדינטות לא חוקיות, נסה שנית.")
            except ValueError:
                print("קלט לא חוקי, הזן מספר.")
        
        # מעבדים את יריית השחקן
        if computer_board[player_row][player_col] == 1:
            computer_board[player_row][player_col] = 2  # 2 = פגיעה
            print("HIT!")
        else:
            computer_board[player_row][player_col] = 3 # 3 = החטאה
            print("MISS!")
        
        # מציגים את שדה המשחק של השחקן לאחר הירייה, מראים את תוצאות הירייה
        print("שדה המשחק שלך:")
        display_board(player_board)
        
        # מהלך המחשב
        print("מהלך המחשב...")
        computer_row = random.randint(0, BOARD_SIZE - 1)
        computer_col = random.randint(0, BOARD_SIZE - 1)
        
         # מעבדים את יריית המחשב
        if player_board[computer_row][computer_col] == 1:
            player_board[computer_row][computer_col] = 2  # 2 = פגיעה
            print("COMPUTER HITS!")
        else:
            player_board[computer_row][computer_col] = 3 # 3 = החטאה
            print("COMPUTER MISSES")
        
        # מציגים את שדה המשחק של השחקן לאחר יריית המחשב
        print("שדה המשחק שלך:")
        display_board(player_board)

    # הודעה על סיום המשחק
    print("END OF GAME")


# מריצים את המשחק אם הסקריפט הופעל ישירות
if __name__ == "__main__":
    play_battle()
```
```
הסבר הקוד:

1.  **ייבוא מודול `random`:**
    -   `import random`: מייבא את מודול random, המשמש ליצירת מספרים אקראיים.
2.  **קבוע `BOARD_SIZE`:**
    -   `BOARD_SIZE = 10`: מגדיר את גודל שדה המשחק כ-10x10.
3.  **פונקציה `create_board(size)`:**
    -   יוצרת ומחזירה רשימה דו-ממדית (מטריצה) בגודל נתון, הממולאת באפסים (תאים ריקים).
4.  **פונקציה `place_computer_ships(board)`:**
    -   ממקמת 5 ספינות בגודל 1 (תא בודד) בשדה המשחק של המחשב באופן אקראי.
    -   בודקת שהתא אינו תפוס לפני מיקום הספינה.
    -   ספינה מסומנת בערך 1 בשדה המשחק.
5.  **פונקציה `display_board(board, is_computer=False)`:**
    -   מציגה את שדה המשחק בקונסולה.
    -   אם is_computer=True, ספינות המחשב (ערך 1) מוצגות כ-"*", אחרת ספינות המחשב מוסתרות.
    -   מציגה תאים ריקים כ-"O", פגיעות כ-"X", והחטאות כ-"-".
6.  **פונקציה `play_battle()`:**
    -   יוצרת שדה משחק עבור השחקן ועבור המחשב.
    -   ממקמת את ספינות המחשב בשדה.
    -   מאתחלת את מונה המהלכים turn_count = 0.
    -   **לולאת המשחק הראשית (`while turn_count < 30`):**
        -   מגדילה את מונה המהלכים ב-1.
        -   מציגה את המהלך הנוכחי.
        -   **מהלך השחקן:**
           -   מבקשת מהמשתמש קואורדינטות לירייה (שורה ועמודה).
            -   משתמשת בלולאת `while True`, כדי להבטיח שהמשתמש יזין קואורדינטות חוקיות בפורמט מספרי.
            -   באת אם הקואורדינטות נמצאות בטווח החוקי.
            -   מטפלת בחריגת `ValueError`, אם המשתמש הזין נתונים לא חוקיים (לא מספר).
            -   אם הירייה פגעה בספינה (ערך 1), מחליפה את הערך ל-2 (פגיעה) ומציגה "HIT!".
            -   אם הירייה לא פגעה, מחליפה את הערך ל-3 (החטאה) ומציגה "MISS!".
           -   מציגה את שדה המשחק של השחקן עם סימוני יריות.
        -   **מהלך המחשב:**
             -   מייצרת קואורדינטות אקראיות לירייה.
             -   מעבדת את יריית המחשב בדומה למהלך השחקן.
            -   מציגה הודעה: "COMPUTER HITS!" או "COMPUTER MISSES".
            -   מציגה את שדה המשחק של השחקן עם סימוני יריות.
        -   הלולאה מסתיימת לאחר 30 מהלכים.
    -   מציגה את ההודעה "END OF GAME".
7.  **הפעלת המשחק:**
    -   `if __name__ == "__main__":`: מבטיחה שהפונקציה `play_battle()` תופעל רק אם הסקריפט הופעל ישירות, ולא יובא כמודול.
    -   `play_battle()`: קוראת לפונקציה להפעלת המשחק.

```