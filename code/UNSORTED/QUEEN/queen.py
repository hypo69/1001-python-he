QUEEN:
=================
רמת קושי: 5
-----------------
המשחק "פרז" הוא משחק אסטרטגיה לשני שחקנים, כאשר כל שחקן שולט בפרז על לוח שחמט בגודל 8x8. מטרת המשחק היא להגיע לקצה הנגדי של הלוח ראשון. השחקנים מזיזים את הפרז שלהם לסירוגין, כאשר הפרז יכול לזוז אופקית, אנכית או באלכסון לכל מספר של משבצות.

חוקי המשחק:
1. שני שחקנים שולטים בפרזים על לוח שחמט בגודל 8x8.
2. כל שחקן מתחיל את המשחק עם הפרז שלו על אחד מהקצוות הנגדיים של הלוח.
3. השחקנים מזיזים את הפרזים שלהם בתורות.
4. הפרז יכול לזוז אופקית, אנכית או באלכסון לכל מספר של משבצות.
5. מטרת המשחק היא להגיע לקצה הנגדי של הלוח ראשון.
6. המשחק מסתיים כאשר אחד הפרזים מגיע לקצה הנגדי.
-----------------
אלגוריתם:
1. קביעת קואורדינטות התחלה עבור פרזי שחקן 1 (X1, Y1) ושחקן 2 (X2, Y2).
2. הצגת לוח השחמט על המסך, עם ציון מיקום הפרזים הנוכחי.
3. התחלת לולאה "כל עוד אחד מהפרזים לא הגיע לצד הנגדי":
    3.1 בקשת קואורדינטות עבור הזזת הפרז משחקן 1 (NX, NY).
    3.2 בדיקה אם המהלך של שחקן 1 חוקי (הפרז יכול לזוז רק בקו ישר).
    3.3 אם המהלך אינו חוקי, יש להודיע על כך ולבקש מהלך חדש.
    3.4 עדכון קואורדינטות פרז שחקן 1 (X1 = NX, Y1 = NY).
    3.5 בדיקה, האם פרז שחקן 1 הגיע לצד הנגדי.
    3.6 אם הגיע, יש להכריז על ניצחון שחקן 1 ולסיים את המשחק.
    3.7 הצגת לוח השחמט על המסך, עם ציון מיקום הפרזים הנוכחי.
    3.8 בקשת קואורדינטות עבור הזזת הפרז משחקן 2 (NX, NY).
    3.9 בדיקה אם המהלך של שחקן 2 חוקי (הפרז יכול לזוז רק בקו ישר).
    3.10 אם המהלך אינו חוקי, יש להודיע על כך ולבקש מהלך חדש.
    3.11 עדכון קואורדינטות פרז שחקן 2 (X2 = NX, Y2 = NY).
    3.12 בדיקה, האם פרז שחקן 2 הגיע לצד הנגדי.
    3.13 אם הגיע, יש להכריז על ניצחון שחקן 2 ולסיים את המשחק.
    3.14 הצגת לוח השחמט על המסך, עם ציון מיקום הפרזים הנוכחי.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeQueens["אתחול:
    <code><b>
    player1X = 1, player1Y = 4<br>
    player2X = 8, player2Y = 4<br>
    </b></code>"]
    InitializeQueens --> DisplayBoard["הצגת לוח עם פרזים"]
    DisplayBoard --> Player1TurnStart{"תחילת תור שחקן 1"}
    Player1TurnStart --> Player1Input["בקשת קלט מהלך משחקן 1: <code><b>nextX, nextY</b></code>"]
    Player1Input --> Player1CheckMove{"בדיקת חוקיות מהלך <code><b>(nextX, nextY)</b></code> עבור שחקן 1"}
    Player1CheckMove -- מהלך לא חוקי --> Player1InvalidMove["הצגת הודעה: מהלך לא חוקי"]
    Player1InvalidMove --> Player1TurnStart
    Player1CheckMove -- מהלך חוקי --> Player1UpdatePosition["עדכון עמדת פרז שחקן 1: <code><b>player1X = nextX, player1Y = nextY</b></code>"]
    Player1UpdatePosition --> Player1CheckWin{"בדיקה: האם פרז שחקן 1 הגיע לסוף הלוח?"}
    Player1CheckWin -- כן --> Player1Win["הצגת הודעה: שחקן 1 ניצח!"]
    Player1Win --> End["סוף"]
    Player1CheckWin -- לא --> DisplayBoardAfterPlayer1["הצגת לוח עם עמדת פרז שחקן 1 החדשה"]
    DisplayBoardAfterPlayer1 --> Player2TurnStart{"תחילת תור שחקן 2"}
    Player2TurnStart --> Player2Input["בקשת קלט מהלך משחקן 2: <code><b>nextX, nextY</b></code>"]
    Player2Input --> Player2CheckMove{"בדיקת חוקיות מהלך <code><b>(nextX, nextY)</b></code> עבור שחקן 2"}
     Player2CheckMove -- מהלך לא חוקי --> Player2InvalidMove["הצגת הודעה: מהלך לא חוקי"]
     Player2InvalidMove --> Player2TurnStart
    Player2CheckMove -- מהלך חוקי --> Player2UpdatePosition["עדכון עמדת פרז שחקן 2: <code><b>player2X = nextX, player2Y = nextY</b></code>"]
    Player2UpdatePosition --> Player2CheckWin{"בדיקה: האם פרז שחקן 2 הגיע לסוף הלוח?"}
     Player2CheckWin -- כן --> Player2Win["הצגת הודעה: שחקן 2 ניצח!"]
    Player2Win --> End
    Player2CheckWin -- לא --> DisplayBoardAfterPlayer2["הצגת לוח עם עמדת פרז שחקן 2 החדשה"]
    DisplayBoardAfterPlayer2 --> Player1TurnStart

```

מקרא:
    Start - התחלת התוכנית.
    InitializeQueens - אתחול עמדות התחלה של פרזי שני השחקנים.
    DisplayBoard - הצגת לוח השחמט עם עמדות הפרזים הנוכחיות.
    Player1TurnStart - תחילת תור שחקן 1.
    Player1Input - בקשת קואורדינטות מהלך הבא משחקן 1.
    Player1CheckMove - בדיקת חוקיות מהלך שחקן 1.
    Player1InvalidMove - הצגת הודעה על מהלך לא חוקי עבור שחקן 1.
    Player1UpdatePosition - עדכון עמדת פרז שחקן 1 על הלוח.
    Player1CheckWin - בדיקה, האם פרז שחקן 1 הגיע לסוף הלוח.
    Player1Win - הצגת הודעה על ניצחון שחקן 1.
    DisplayBoardAfterPlayer1 - הצגת הלוח לאחר מהלך שחקן 1.
    Player2TurnStart - תחילת תור שחקן 2.
    Player2Input - בקשת קואורדינטות מהלך הבא משחקן 2.
    Player2CheckMove - בדיקת חוקיות מהלך שחקן 2.
    Player2InvalidMove - הצגת הודעה על מהלך לא חוקי עבור שחקן 2.
     Player2UpdatePosition - עדכון עמדת פרז שחקן 2 על הלוח.
    Player2CheckWin - בדיקה, האם פרז שחקן 2 הגיע לסוף הלוח.
    Player2Win - הצגת הודעה על ניצחון שחקן 2.
     DisplayBoardAfterPlayer2 - הצגת הלוח לאחר מהלך שחקן 2.
    End - סוף התוכנית.
"""
import sys

# אתחול עמדות התחלה של פרזים
player1_x = 0
player1_y = 3
player2_x = 7
player2_y = 3


def print_board(player1_x, player1_y, player2_x, player2_y):
    """
    מציגה על המסך את לוח השחמט עם ציון עמדות הפרזים הנוכחיות.
    """
    print("   0  1  2  3  4  5  6  7")
    for row in range(8):
        row_str = str(row) + " "
        for col in range(8):
            if row == player1_y and col == player1_x:
                row_str += " 1 "
            elif row == player2_y and col == player2_x:
                row_str += " 2 "
            else:
                row_str += " . "
        print(row_str)


def is_valid_move(current_x, current_y, next_x, next_y):
    """
    בודקת האם מהלך פרז חוקי.

    מהלך חוקי אם הפרז נע אופקית, אנכית או באלכסון.
    """
    if next_x < 0 or next_x > 7 or next_y < 0 or next_y > 7:
        return False # בדיקה של יציאה מגבולות הלוח
    
    if current_x == next_x: # תזוזה אנכית
        return True
    elif current_y == next_y: # תזוזה אופקית
        return True
    elif abs(current_x - next_x) == abs(current_y - next_y): # תזוזה באלכסון
         return True
    else:
        return False


def get_player_move(player_number, current_x, current_y):
    """
    מבקשת מהשחקן קלט קואורדינטות עבור הזזת הפרז.
    בודקת את חוקיות הקואורדינטות שהוזנו.
    מחזירה את הקואורדינטות החדשות.
    """
    while True:
        try:
            move_str = input(f"שחקן {player_number}, הזן מהלך (x, y): ")
            next_x, next_y = map(int, move_str.split(','))
            if is_valid_move(current_x, current_y, next_x, next_y):
                return next_x, next_y
            else:
                print("מהלך לא חוקי. נסה שוב.")
        except ValueError:
            print("פורמט קלט שגוי. הזן שני מספרים מופרדים בפסיק, לדוגמה: 1,2")


# לולאת המשחק הראשית
while True:
    print_board(player1_x, player1_y, player2_x, player2_y) # מציגים את הלוח
    # תור שחקן 1
    print("תור שחקן 1:")
    next_player1_x, next_player1_y = get_player_move(1, player1_x, player1_y)
    player1_x, player1_y = next_player1_x, next_player1_y

    if player1_x == 7: # בדיקה לניצחון
        print("שחקן 1 ניצח!")
        break # מסיימים את הלולאה
    # תור שחקן 2
    print_board(player1_x, player1_y, player2_x, player2_y)
    print("תור שחקן 2:")
    next_player2_x, next_player2_y = get_player_move(2, player2_x, player2_y)
    player2_x, player2_y = next_player2_x, next_player2_y

    if player2_x == 0: # בדיקה לניצחון
       print("שחקן 2 ניצח!")
       break # מסיימים את הלולאה


"""
הסבר קוד:

1. **אתחול משתנים**:
   - `player1_x`, `player1_y`: קואורדינטות התחלה של פרז שחקן 1.
   - `player2_x`, `player2_y`: קואורדינטות התחלה של פרז שחקן 2.

2. **פונקציה `print_board`**:
   - מקבלת את הקואורדינטות הנוכחיות של פרזי שני השחקנים.
   - מציגה על המסך את לוח השחמט, תוך שימוש ב-'.' עבור משבצות ריקות, '1' עבור פרז שחקן 1 ו-'2' עבור פרז שחקן 2.

3. **פונקציה `is_valid_move`**:
   - מקבלת קואורדינטות נוכחיות ובאות של מהלך הפרז.
   - בודקת האם המהלך חוקי:
     - הפרז יכול לזוז אופקית, אנכית או באלכסון.
     - הפרז אינו יכול לצאת מגבולות הלוח.

4. **פונקציה `get_player_move`**:
    - מבקשת מהשחקן קלט של קואורדינטות המהלך הבא.
    - משתמשת בלולאת `while True` כדי להבטיח קלט נתונים נכונים.
    - בודקת את פורמט הקלט: הקלט צריך להיות בפורמט `x,y` (שני מספרים שלמים מופרדים בפסיק).
    - קוראת לפונקציה `is_valid_move` כדי לבדוק את חוקיות המהלך.
    - מחזירה את קואורדינטות המהלך החדשות כאשר הן חוקיות.

5. **לולאת המשחק הראשית (`while True`)**:
   - מציגה את לוח השחמט על המסך.
   - מבקשת מהלך משחקן 1, תוך שימוש בפונקציה `get_player_move`, ומעדכנת את עמדת פרז שחקן 1.
   - בודקת, האם פרז שחקן 1 הגיע לסוף הלוח (x=7). אם הגיע, מציגה הודעה על ניצחון ומסיימת את המשחק.
   - מציגה את הלוח שוב.
   - מבקשת מהלך משחקן 2, תוך שימוש בפונקציה `get_player_move`, ומעדכנת את עמדת פרז שחקן 2.
   - בודקת, האם פרז שחקן 2 הגיע לסוף הלוח (x=0). אם הגיע, מציגה הודעה על ניצחון ומסיימת את המשחק.
   - הלולאה ממשיכה כל עוד אחד השחקנים לא ניצח.

6.  **הפעלת המשחק**:
    -  המשחק מופעל ישירות, ללא תנאים נוספים.
"""