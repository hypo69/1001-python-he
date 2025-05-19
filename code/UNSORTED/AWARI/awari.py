AWARI:
=================
מורכבות: 6
-----------------
המשחק "אוארי" הינו משחק לוח המדמה את משחק מנקלה המסורתי, בו שני שחקנים מזיזים לסירוגין "אבנים" (במקרה זה, מספרים) מתאים על הלוח, בניסיון ללכוד כמה שיותר אבנים ל"מחסנים" שלהם. זוהי גרסה מפושטת של המשחק, בה השחקן משחק נגד המחשב.

כללי המשחק:
1. שדה המשחק מורכב מ-14 תאים, הממוספרים מ-0 עד 13. תאים 6 ו-13 הם "מחסני" השחקנים.
2. בתחילת המשחק, בכל אחד מ-12 התאים (0-5 ו-7-12) נמצאות 4 אבנים.
3. השחקן (אדם) מתחיל את המשחק.
4. בוחר תא המכיל את אבניו (0-5).
5. כל האבנים מהתא הנבחר מוזזות, אחת אחת, לכל תא עוקב בכיוון השעון, כולל המחסן של השחקן עצמו.
6. אם האבן האחרונה נפלה למחסן של השחקן, לשחקן יש זכות לבצע מהלך נוסף.
7. אם האבן האחרונה נפלה לתא ריק בצד של השחקן, ומול תא זה יש אבנים, אזי השחקן לוקח את האבנים מתא זה ומהתא הנגדי למחסן שלו.
8. המחשב מבצע את המהלך באופן דומה.
9. המשחק מסתיים כאשר כל התאים עם האבנים הופכים לריקים.
10. השחקן עם כמות האבנים הגדולה ביותר במחסן מנצח.
-----------------
אלגוריתם:
1. לאתחל את הלוח (מערך) של 14 תאים עם 4 אבנים בכל אחד, למעט תאים 6 ו-13, השווים ל-0.
2. להתחיל לולאה "כל עוד המשחק לא הסתיים".
3. מהלך השחקן:
    3.1 לבקש מהשחקן להזין את מספר התא (מ-0 עד 5).
    3.2 להזיז את האבנים מהתא הנבחר בכיוון השעון.
    3.3 לבדוק האם האבן האחרונה נפלה למחסן של השחקן (תא 6). אם כן, לתת לשחקן מהלך נוסף.
    3.4 לבדוק האם האבן האחרונה נפלה לתא ריק בצד של השחקן. אם כן, ללכוד את האבנים מתא זה ומהתא הנגדי.
4. מהלך המחשב (בדומה למהלך השחקן, אך בחירת התא היא אקראית מ-7 עד 12).
5. אם כל התאים עם האבנים ריקים, לסיים את המשחק.
6. להציג את התוצאה (כמות האבנים במחסנים של השחקן והמחשב).
7. לקבוע את המנצח (למי יש יותר אבנים במחסן).
-----------------

"""
import random

# אתחול הלוח.
# תאים 0-5 - תאי השחקן, 6 - מחסן השחקן
# תאים 7-12 - תאי המחשב, 13 - מחסן המחשב
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
    """מטפל במהלך השחקן."""
    while True:
        try:
            cell = int(input("בחר תא (0-5): "))
            if 0 <= cell <= 5 and board[cell] > 0:
                break
            else:
                print("בחירה לא חוקית. בחר תא עם אבנים מ-0 עד 5.")
        except ValueError:
            print("קלט לא חוקי. נא הזן מספר.")
    
    stones = board[cell]
    board[cell] = 0
    current_cell = cell
    
    while stones > 0:
        current_cell = (current_cell + 1) % 14
        board[current_cell] += 1
        stones -= 1

    # בדיקה למהלך נוסף אם האבן האחרונה נפלה למחסן השחקן
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
             print(f"השחקן לוכד אבנים מתאים {current_cell} ו- {opposite_cell}")
         
        
def computer_turn():
    """מטפל במהלך המחשב."""
    possible_moves = [i for i in range(7, 13) if board[i] > 0]
    if not possible_moves:
        return  # אם אין מהלכים זמינים עבור המחשב, יש לצאת
    
    cell = random.choice(possible_moves)
    print(f"המחשב בוחר תא {cell}")
    stones = board[cell]
    board[cell] = 0
    current_cell = cell

    while stones > 0:
         current_cell = (current_cell + 1) % 14
         board[current_cell] += 1
         stones -= 1

    # בדיקה למהלך נוסף אם האבן האחרונה נפלה למחסן המחשב
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
             print(f"המחשב לוכד אבנים מתאים {current_cell} ו- {opposite_cell}")

def is_game_over():
    """בודק האם המשחק הסתיים."""
    player_side_empty = all(board[i] == 0 for i in range(0, 6))
    computer_side_empty = all(board[i] == 0 for i in range(7, 13))
    return player_side_empty or computer_side_empty


def calculate_winner():
    """קובע את המנצח ומציג את התוצאות."""
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