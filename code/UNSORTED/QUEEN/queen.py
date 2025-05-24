**מלכה**
=================
רמת קושי: 5
-----------------
המשחק "מלכה" הוא משחק אסטרטגיה לשני שחקנים, כאשר כל שחקן שולט במלכה אחת על לוח שחמט בגודל 8x8. מטרת המשחק היא להגיע לקצה הנגדי של הלוח ראשון. השחקנים מזיזים את המלכה שלהם לסירוגין, כאשר המלכה יכולה לנוע אופקית, אנכית או באלכסון לכל מספר של משבצות.

חוקי המשחק:
1. שני שחקנים שולטים במלכות על לוח שחמט בגודל 8x8.
2. כל שחקן מתחיל את המשחק עם המלכה שלו באחד מהקצוות הנגדיים של הלוח.
3. השחקנים מזיזים את המלכות שלהם בתורות.
4. המלכה יכולה לנוע אופקית, אנכית או באלכסון לכל מספר של משבצות.
5. מטרת המשחק היא להגיע ראשון לקצה הנגדי של הלוח.
6. המשחק מסתיים כאשר אחת המלכות מגיעה לקצה הנגדי.
-----------------
אלגוריתם:
1. קבע את הקואורדינטות ההתחלתיות של המלכות עבור שחקן 1 (X1, Y1) ושחקן 2 (X2, Y2).
2. הצג על המסך את לוח השחמט, תוך ציון המיקום הנוכחי של המלכות.
3. התחל לולאת "כל עוד אף אחת מהמלכות לא הגיעה לצד הנגדי":
    3.1 בקש משחקן 1 את הקואורדינטות להזזת המלכה (NX, NY).
    3.2 בדוק האם המהלך של שחקן 1 חוקי (המלכה יכולה לנוע רק בקו ישר).
    3.3 אם המהלך אינו חוקי, הודע על כך ובקש מהלך חדש.
    3.4 עדכן את הקואורדינטות של המלכה של שחקן 1 (X1 = NX, Y1 = NY).
    3.5 בדוק האם המלכה של שחקן 1 הגיעה לצד הנגדי.
    3.6 אם הגיעה, הכרז על ניצחון שחקן 1 וסיים את המשחק.
    3.7 הצג על המסך את לוח השחמט, תוך ציון המיקום הנוכחי של המלכות.
    3.8 בקש משחקן 2 את הקואורדינטות להזזת המלכה (NX, NY).
    3.9 בדוק האם המהלך של שחקן 2 חוקי (המלכה יכולה לנוע רק בקו ישר).
    3.10 אם המהלך אינו חוקי, הודע על כך ובקש מהלך חדש.
    3.11 עדכן את הקואורדינטות של המלכה של שחקן 2 (X2 = NX, Y2 = NY).
    3.12 בדוק האם המלכה של שחקן 2 הגיעה לצד הנגדי.
    3.13 אם הגיעה, הכרז על ניצחון שחקן 2 וסיים את המשחק.
    3.14 הצג על המסך את לוח השחמט, תוך ציון המיקום הנוכחי של המלכות.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeQueens["אתחול:
    <code><b>
    player1X = 0, player1Y = 3<br>
    player2X = 7, player2Y = 3<br>
    </b></code>"]
    InitializeQueens --> DisplayBoard["הצג לוח עם מלכות"]
    DisplayBoard --> Player1TurnStart{"תחילת תור שחקן 1"}
    Player1TurnStart --> Player1Input["בקש קלט מהלך משחקן 1: <code><b>nextX, nextY</b></code>"]
    Player1Input --> Player1CheckMove{"בדיקת תקינות מהלך <code><b>(nextX, nextY)</b></code> עבור שחקן 1"}
    Player1CheckMove -- מהלך לא חוקי --> Player1InvalidMove["הצג הודעה: מהלך לא חוקי"]
    Player1InvalidMove --> Player1TurnStart
    Player1CheckMove -- מהלך חוקי --> Player1UpdatePosition["עדכון מיקום מלכת שחקן 1: <code><b>player1X = nextX, player1Y = nextY</b></code>"]
    Player1UpdatePosition --> Player1CheckWin{"בדיקה: האם מלכת שחקן 1 הגיעה לקצה הלוח?"}
    Player1CheckWin -- כן --> Player1Win["הצג הודעה: שחקן 1 ניצח!"]
    Player1Win --> End["סיום"]
    Player1CheckWin -- לא --> DisplayBoardAfterPlayer1["הצג לוח עם מיקום חדש של מלכת שחקן 1"]
    DisplayBoardAfterPlayer1 --> Player2TurnStart{"תחילת תור שחקן 2"}
    Player2TurnStart --> Player2Input["בקש קלט מהלך משחקן 2: <code><b>nextX, nextY</b></code>"]
    Player2Input --> Player2CheckMove{"בדיקת תקינות מהלך <code><b>(nextX, nextY)</b></code> עבור שחקן 2"}
     Player2CheckMove -- מהלך לא חוקי --> Player2InvalidMove["הצג הודעה: מהלך לא חוקי"]
     Player2InvalidMove --> Player2TurnStart
    Player2CheckMove -- מהלך חוקי --> Player2UpdatePosition["עדכון מיקום מלכת שחקן 2: <code><b>player2X = nextX, player2Y = nextY</b></code>"]
    Player2UpdatePosition --> Player2CheckWin{"בדיקה: האם מלכת שחקן 2 הגיעה לקצה הלוח?"}
     Player2CheckWin -- כן --> Player2Win["הצג הודעה: שחקן 2 ניצח!"]
    Player2Win --> End
    Player2CheckWin -- לא --> DisplayBoardAfterPlayer2["הצג לוח עם מיקום חדש של מלכת שחקן 2"]
    DisplayBoardAfterPlayer2 --> Player1TurnStart

```

מקרא:
    Start - התחלת התוכנית.
    InitializeQueens - אתחול המיקומים ההתחלתיים של מלכות שני השחקנים.
    DisplayBoard - הצגת לוח השחמט עם המיקומים הנוכחיים של המלכות.
    Player1TurnStart - תחילת תור שחקן 1.
    Player1Input - בקשת קואורדינטות המהלך הבא משחקן 1.
    Player1CheckMove - בדיקת תקינות המהלך של שחקן 1.
    Player1InvalidMove - הצגת הודעה על מהלך לא חוקי עבור שחקן 1.
    Player1UpdatePosition - עדכון מיקום מלכת שחקן 1 על הלוח.
    Player1CheckWin - בדיקה האם מלכת שחקן 1 הגיעה לקצה הלוח.
    Player1Win - הצגת הודעה על ניצחון שחקן 1.
    DisplayBoardAfterPlayer1 - הצגת הלוח לאחר מהלך שחקן 1.
    Player2TurnStart - תחילת תור שחקן 2.
    Player2Input - בקשת קואורדינטות המהלך הבא משחקן 2.
    Player2CheckMove - בדיקת תקינות המהלך של שחקן 2.
    Player2InvalidMove - הצגת הודעה על מהלך לא חוקי עבור שחקן 2.
    Player2UpdatePosition - עדכון מיקום מלכת שחקן 2 על הלוח.
    Player2CheckWin - בדיקה האם מלכת שחקן 2 הגיעה לקצה הלוח.
    Player2Win - הצגת הודעה על ניצחון שחקן 2.
    DisplayBoardAfterPlayer2 - הצגת הלוח לאחר מהלך שחקן 2.
    End - סוף התוכנית.
"""
import sys

# אתחול מיקומים התחלתיים של המלכות
player1_x = 0
player1_y = 3
player2_x = 7
player2_y = 3


def print_board(player1_x, player1_y, player2_x, player2_y):
    """
    מציג על המסך את לוח השחמט תוך ציון המיקומים הנוכחיים של המלכות.
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
    בודק האם מהלך המלכה חוקי.

    מהלך חוקי אם המלכה נעה אופקית, אנכית או באלכסון.
    """
    if next_x < 0 or next_x > 7 or next_y < 0 or next_y > 7:
        return False # בדיקת יציאה מגבולות הלוח
    
    if current_x == next_x: # תנועה אנכית
        return True
    elif current_y == next_y: # תנועה אופקית
        return True
    elif abs(current_x - next_x) == abs(current_y - next_y): # תנועה באלכסון
         return True
    else:
        return False


def get_player_move(player_number, current_x, current_y):
    """
    מבקש מהשחקן קלט קואורדינטות להזזת המלכה.
    בודק את תקינות הקואורדינטות שהוזנו.
    מחזיר את הקואורדינטות החדשות.
    """
    while True:
        try:
            move_str = input(f"שחקן {player_number}, אנא הכנס מהלך (x, y): ")
            next_x, next_y = map(int, move_str.split(','))
            if is_valid_move(current_x, current_y, next_x, next_y):
                return next_x, next_y
            else:
                print("מהלך לא חוקי. אנא נסה שוב.")
        except ValueError:
            print("פורמט קלט שגוי. הכנס שני מספרים מופרדים בפסיק, לדוגמה: 1,2")


# לולאת המשחק הראשית
while True:
    print_board(player1_x, player1_y, player2_x, player2_y) # מציגים את הלוח
    # תור שחקן 1
    print("תור שחקן 1:")
    next_player1_x, next_player1_y = get_player_move(1, player1_x, player1_y)
    player1_x, player1_y = next_player1_x, next_player1_y

    if player1_x == 7: # בדיקת ניצחון
        print("שחקן 1 ניצח!")
        break # סיום הלולאה
    # תור שחקן 2
    print_board(player1_x, player1_y, player2_x, player2_y)
    print("תור שחקן 2:")
    next_player2_x, next_player2_y = get_player_move(2, player2_x, player2_y)
    player2_x, player2_y = next_player2_x, next_player2_y

    if player2_x == 0: # בדיקת ניצחון
       print("שחקן 2 ניצח!")
       break # סיום הלולאה


"""
הסבר על הקוד:

1. **אתחול משתנים**:
   - `player1_x`, `player1_y`: קואורדינטות התחלתיות של מלכת שחקן 1.
   - `player2_x`, `player2_y`: קואורדינטות התחלתיות של מלכת שחקן 2.

2. **פונקציה `print_board`**:
   - מקבלת את הקואורדינטות הנוכחיות של המלכות של שני השחקנים.
   - מציגה על המסך את לוח השחמט, תוך שימוש ב-'.' עבור משבצות ריקות, '1' עבור מלכת שחקן 1 ו-'2' עבור מלכת שחקן 2.

3. **פונקציה `is_valid_move`**:
   - מקבלת את הקואורדינטות הנוכחיות והקואורדינטות הבאות עבור מהלך המלכה.
   - בודקת האם המהלך חוקי:
     - המלכה יכולה לנוע אופקית, אנכית או באלכסון.
     - המלכה אינה יכולה לצאת מגבולות הלוח.

4. **פונקציה `get_player_move`**:
    - מבקשת מהשחקן קלט של קואורדינטות המהלך הבא.
    - משתמשת בלולאת `while True` כדי להבטיח קלט נתונים תקינים.
    - בודקת את פורמט הקלט: הקלט צריך להיות בפורמט `x,y` (שני מספרים שלמים מופרדים בפסיק).
    - קוראת לפונקציה `is_valid_move` לבדיקת תקינות המהלך.
    - מחזירה את קואורדינטות המהלך החדשות כאשר הן תקינות.

5. **לולאת המשחק הראשית (`while True`)**:
   - מציגה את לוח השחמט על המסך.
   - מבקשת מהלך משחקן 1, באמצעות הפונקציה `get_player_move`, ומעדכנת את מיקום מלכת שחקן 1.
   - בודקת האם מלכת שחקן 1 הגיעה לקצה הלוח (x=7). אם הגיעה, מציגה הודעה על ניצחון ומסיימת את המשחק.
   - מציגה את הלוח שוב.
   - מבקשת מהלך משחקן 2, באמצעות הפונקציה `get_player_move`, ומעדכנת את מיקום מלכת שחקן 2.
   - בודקת האם מלכת שחקן 2 הגיעה לקצה הלוח (x=0). אם הגיעה, מציגה הודעה על ניצחון ומסיימת את המשחק.
   - הלולאה ממשיכה כל עוד אחד מהשחקנים לא ניצח.

6.  **הפעלת המשחק**:
    -  המשחק מופעל ישירות, ללא תנאים נוספים.
"""
```