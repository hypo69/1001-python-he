"""
AWARI:
=================
רמת קושי: 6
-----------------
המשחק "אוארי" הוא משחק לוח המדמה את משחק המנקלה המסורתי, שבו שני שחקנים בתורות מעבירים "אבנים" (במקרה זה, מספרים) מתאים בלוח, בניסיון ללכוד כמה שיותר אבנים לתוך "מאגרי"הם. זוהי גרסה פשוטה של המשחק, שבה שחקן אחד משחק נגד המחשב.

חוקי המשחק:
1. לוח המשחק מורכב מ-14 תאים, הממוספרים מ-0 עד 13. תאים 6 ו-13 הם "מאגרי" השחקנים.
2. בתחילת המשחק, בכל אחד מ-12 התאים (0-5 ו-7-12) מצויות 4 אבנים.
3. השחקן (האדם) מתחיל את המשחק.
4. בוחר תא עם האבנים שלו (0-5).
5. כל האבנים מהתא הנבחר מפוזרות אחת אחת לכל תא עוקב בכיוון השעון, כולל לתוך ה"מאגר" של השחקן עצמו.
6. אם האבן האחרונה הגיעה ל"מאגר" של השחקן, השחקן רשאי לבצע מהלך נוסף.
7. אם האבן האחרונה הגיעה לתא ריק בצד של השחקן, ומול תא זה מצויות אבנים, אזי השחקן לוקח את האבנים מתא זה ומהתא שמולו ל"מאגר" שלו.
8. המחשב מבצע מהלך באופן דומה.
9. המשחק מסתיים כאשר כל התאים עם האבנים מתרוקנים.
10. מנצח השחקן שיש לו יותר אבנים ב"מאגר".
-----------------
אלגוריתם:
1. אתחול הלוח (מערך) בן 14 תאים, עם 4 אבנים בכל אחד, למעט תאים 6 ו-13, אשר שווים ל-0.
2. התחלת לולאה "כל עוד המשחק לא הסתיים"
3. מהלך השחקן:
    3.1 בקשת קלט של מספר התא מהשחקן (מ-0 עד 5).
    3.2 הזזת האבנים מהתא הנבחר בכיוון השעון.
    3.3 בדיקה האם האבן האחרונה הגיעה ל"מאגר" של השחקן (תא 6). אם כן, מתן מהלך נוסף לשחקן.
    3.4 בדיקה האם האבן האחרונה הגיעה לתא ריק בצד השחקן. אם כן, לכידת האבנים מתא זה ומהתא שמולו.
4. מהלך המחשב (בדומה למהלך השחקן, אך בחירת התא היא אקראית מ-7 עד 12).
5. אם כל התאים עם האבנים ריקים, סיום המשחק.
6. הצגת התוצאה (מספר האבנים ב"מאגרים" של השחקן והמחשב).
7. קביעת המנצח (למי יש יותר אבנים ב"מאגר").
-----------------

"""
import random

# אתחול הלוח.
# תאים 0-5 - תאי השחקן, 6 - המאגר של השחקן
# תאים 7-12 - תאי המחשב, 13 - המאגר של המחשב
board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]


def display_board():
    """מציג את המצב הנוכחי של לוח המשחק."""
    print("----------------------------------------------------")
    print(f"  {board[12]:2}  {board[11]:2}  {board[10]:2}  {board[9]:2}  {board[8]:2}  {board[7]:2}   ")
    print("----------------------------------------------------")
    print(f"{board[13]:2}                                 {board[6]:2}")
    print("----------------------------------------------------")
    print(f"  {board[0]:2}  {board[1]:2}  {board[2]:2}  {board[3]:2}  {board[4]:2}  {board[5]:2}  ")
    print("----------------------------------------------------")


def player_turn():
    """מטפל במהלכים של השחקן."""
    while True:
        try:
            cell = int(input("בחר תא (0-5): "))
            if 0 <= cell <= 5 and board[cell] > 0:
                break
            else:
                print("בחירה לא חוקית. בחר תא עם אבנים בטווח 0 עד 5.")
        except ValueError:
            print("קלט שגוי. אנא הזן מספר.")

    stones = board[cell]
    board[cell] = 0
    current_cell = cell

    while stones > 0:
        current_cell = (current_cell + 1) % 14
        board[current_cell] += 1
        stones -= 1

    # בדיקה האם האבן האחרונה הגיעה ל"מאגר" של השחקן לצורך מהלך נוסף
    if current_cell == 6:
        print("השחקן מקבל מהלך נוסף.")
        display_board()
        player_turn()
        return

    # לכידת אבנים
    if 0 <= current_cell <= 5 and board[current_cell] == 1:
        opposite_cell = 12 - current_cell
        if board[opposite_cell] > 0:
             board[6] += board[opposite_cell] + 1
             board[opposite_cell]=0
             board[current_cell] = 0
             print(f"השחקן לוכד אבנים מהתאים {current_cell} ו- {opposite_cell}")


def computer_turn():
    """מטפל במהלכים של המחשב."""
    possible_moves = [i for i in range(7, 13) if board[i] > 0]
    if not possible_moves:
        return  # אם אין מהלכים זמינים עבור המחשב, צא

    cell = random.choice(possible_moves)
    print(f"המחשב בוחר את תא {cell}")
    stones = board[cell]
    board[cell] = 0
    current_cell = cell

    while stones > 0:
         current_cell = (current_cell + 1) % 14
         board[current_cell] += 1
         stones -= 1

    # בדיקה האם האבן האחרונה הגיעה ל"מאגר" של המחשב לצורך מהלך נוסף
    if current_cell == 13:
        print("המחשב מקבל מהלך נוסף.")
        display_board()
        computer_turn()
        return

    # לכידת אבנים
    if 7 <= current_cell <= 12 and board[current_cell] == 1:
          opposite_cell = 12 - current_cell
          if board[opposite_cell] > 0:
             board[13] += board[opposite_cell] + 1
             board[opposite_cell]=0
             board[current_cell] = 0
             print(f"המחשב לוכד אבנים מהתאים {current_cell} ו- {opposite_cell}")

def is_game_over():
    """בדיקה האם המשחק הסתיים."""
    player_side_empty = all(board[i] == 0 for i in range(0, 6))
    computer_side_empty = all(board[i] == 0 for i in range(7, 13))
    return player_side_empty or computer_side_empty


def calculate_winner():
    """קביעת המנצח והצגת התוצאות."""
    player_score = board[6]
    computer_score = board[13]

    print(f"שחקן: {player_score} נקודות")
    print(f"מחשב: {computer_score} נקודות")

    if player_score > computer_score:
        print("ניצחת!")
    elif computer_score > player_score:
        print("המחשב ניצח!")
    else:
        print("תיקו!")


# לולאת המשחק הראשית
while True:
    display_board()
    player_turn()
    if is_game_over():
        break
    display_board()
    computer_turn()
    if is_game_over():
       break


# לאחר סיום המשחק
display_board()
calculate_winner()