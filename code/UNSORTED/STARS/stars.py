STARS:
=================
דרגת קושי: 4
-----------------
המשחק "כוכבים" הוא משחק טקסטואלי פשוט שבו השחקן שולט במיקום של "כוכב" על המסך על ידי הזנת פקודות להזזתו. מטרת המשחק היא להזיז את הכוכב לפינה הימנית התחתונה של המסך.

כללי המשחק:
1. בתחילת המשחק הכוכב נמצא בפינה השמאלית העליונה של המסך (עמדה 1,1).
2. השחקן מזין פקודות תנועה:
   - 'R' - הזזת הכוכב ימינה
   - 'L' - הזזת הכוכב שמאלה
   - 'U' - הזזת הכוכב למעלה
   - 'D' - הזזת הכוכב למטה
3. המסך מיוצג על ידי רשת בגודל 12x12.
4. המשחק מסתיים כאשר הכוכב מגיע לפינה הימנית התחתונה של המסך (עמדה 12,12).
-----------------
אלגוריתם:
1. הגדרת מיקום התחלתי של הכוכב ב-(1, 1).
2. הדפסת מיקום התחלתי של הכוכב על המסך, הצגתו באמצעות הסימן "*".
3. התחלת לולאה:
    3.1 בקשת קלט פקודת תנועה ('R', 'L', 'U', 'D').
    3.2 עדכון מיקום הכוכב בהתאם לפקודה שהוזנה.
    3.3 בדיקה האם הכוכב הגיע לעמדה (12, 12). אם כן, הדפסת הודעת ניצחון וסיום המשחק.
    3.4 אחרת, הדפסת מיקום חדש של הכוכב על המסך.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializePosition["<p align='left'>אתחול מיקום הכוכב:
    <code><b>
    starRow = 1
    starCol = 1
    </b></code></p>"]
    InitializePosition --> DisplayBoard["הצגת מיקום התחלתי של הכוכב"]
    DisplayBoard --> LoopStart{"התחלת לולאה"}
    LoopStart --> InputMove["הזנת פקודת תנועה (R, L, U, D)"]
    InputMove --> UpdatePosition["<p align='left'>עדכון מיקום הכוכב:
    <code><b>
    starRow, starCol = updatePosition(command, starRow, starCol)
    </b></code></p>"]
    UpdatePosition --> CheckWin{"בדיקה: <code><b>starRow == 12 and starCol == 12?</b></code>"}
    CheckWin -- כן --> OutputWin["הדפסת הודעה: <b>YOU MADE IT!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> DisplayBoardUpdated["הצגת מיקום חדש של הכוכב"]
    DisplayBoardUpdated --> LoopStart
```

מקרא:
    Start - התחלת התוכנית.
    InitializePosition - אתחול מיקום התחלתי של הכוכב: starRow (שורה) ו-starCol (עמודה) מוגדרים ל-1.
    DisplayBoard - הצגת מיקום התחלתי של הכוכב על המסך.
    LoopStart - התחלת לולאת המשחק.
    InputMove - בקשת פקודת תנועה מהשחקן ('R', 'L', 'U', 'D').
    UpdatePosition - עדכון מיקום הכוכב בהתבסס על הפקודה שהוזנה.
    CheckWin - בדיקה האם הכוכב הגיע לעמדה הסופית (12, 12).
    OutputWin - הדפסת הודעת ניצחון, אם הכוכב הגיע לעמדה הסופית.
    End - סוף התוכנית.
    DisplayBoardUpdated - הצגת מיקום מעודכן של הכוכב על המסך.
```

# אתחול מיקום התחלתי של הכוכב
starRow = 1
starCol = 1
# גודל לוח המשחק
boardSize = 12

def printBoard(starRow, starCol):
  """
  מדפיס על המסך את לוח המשחק עם מיקום הכוכב הנוכחי.
  ארגומנטים:
    starRow (int): השורה שבה נמצא הכוכב.
    starCol (int): העמודה שבה נמצא הכוכב.
  """
  for row in range(1, boardSize + 1):
    line = ""
    for col in range(1, boardSize + 1):
      if row == starRow and col == starCol:
        line += "*"  # הצגת הכוכב
      else:
        line += "."  # הצגת תא ריק
    print(line)

def updatePosition(command, starRow, starCol):
    """
    מעדכן את מיקום הכוכב בהתבסס על הפקודה שהוזנה.
    ארגומנטים:
        command (str): פקודת תנועה ('R', 'L', 'U', 'D').
        starRow (int): השורה הנוכחית של הכוכב.
        starCol (int): העמודה הנוכחית של הכוכב.
    מחזיר:
        tuple (int, int): השורה והעמודה החדשות של הכוכב.
    """
    if command == 'R':  # נעים ימינה
        if starCol < boardSize:
           starCol += 1
    elif command == 'L':  # נעים שמאלה
        if starCol > 1:
            starCol -= 1
    elif command == 'U':  # נעים למעלה
        if starRow > 1:
            starRow -= 1
    elif command == 'D':  # נעים למטה
        if starRow < boardSize:
            starRow += 1
    return starRow, starCol

# הדפסת מיקום התחלתי של הכוכב
printBoard(starRow, starCol)

# לולאת המשחק הראשית
while True:
    # בקשת פקודת תנועה מהמשתמש
    command = input("Введите команду (R/L/U/D): ").upper()

    # עדכון מיקום הכוכב בהתבסס על הפקודה שהוזנה
    starRow, starCol = updatePosition(command, starRow, starCol)

    # הדפסת המיקום החדש של הכוכב על המסך
    printBoard(starRow, starCol)

    # בדיקה האם הכוכב הגיע לעמדה הסופית
    if starRow == boardSize and starCol == boardSize:
        print("מזל טוב! העברת את הכוכב לפינה הימנית התחתונה!")
        break  # סיום המשחק

"""
הסבר על הקוד:
1.  **אתחול משתנים**:
    -   `starRow = 1`:  השורה ההתחלתית של הכוכב (שורה עליונה).
    -   `starCol = 1`:  העמודה ההתחלתית של הכוכב (עמודה שמאלית).
    -   `boardSize = 12`: גודל לוח המשחק (12x12).
2.  **פונקציה `printBoard(starRow, starCol)`**:
    -  מקבלת את הקואורדינטות הנוכחיות של הכוכב (שורה `starRow` ועמודה `starCol`).
    -   מדפיסה את לוח המשחק למסוף. הכוכב '*' מציין את המיקום הנוכחי של הכוכב, ו-'.' מציין תאים ריקים.
    -   משתמשת בשתי לולאות מקוננות למעבר על כל השורות והעמודות של הלוח.
3.  **פונקציה `updatePosition(command, starRow, starCol)`**:
    -   מקבלת פקודת תנועה (`command`) ואת הקואורדינטות הנוכחיות של הכוכב (`starRow`, `starCol`).
    -   מעדכנת את קואורדינטות הכוכב בהתאם לפקודה ('R', 'L', 'U', 'D'):
        -   'R': זז ימינה, אם לא הגיע לקצה הימני.
        -   'L': זז שמאלה, אם לא הגיע לקצה השמאלי.
        -   'U': זז למעלה, אם לא הגיע לקצה העליון.
        -   'D': זז למטה, אם לא הגיע לקצה התחתון.
    -   מחזירה את המיקום החדש של הכוכב (שורה ועמודה).
4.  **הדפסת מיקום התחלתי של הכוכב**:
    -   `printBoard(starRow, starCol)`: מדפיס על המסך את לוח המשחק עם מיקום הכוכב ההתחלתי.
5.  **לולאת המשחק הראשית `while True`**:
    -   לולאה אינסופית, עד שיתקיים תנאי הניצחון.
    -   `command = input("Введите команду (R/L/U/D): ").upper()`: מבקש מהמשתמש פקודת תנועה וממיר אותה לאותיות רישיות.
    -   `starRow, starCol = updatePosition(command, starRow, starCol)`: מעדכן את מיקום הכוכב באמצעות קריאה לפונקציה `updatePosition()`.
    -   `printBoard(starRow, starCol)`: מדפיס את מיקום הכוכב המעודכן על המסך.
    -   `if starRow == boardSize and starCol == boardSize`: בודק האם הכוכב הגיע לפינה הימנית התחתונה (12,12).
    -   `print("מזל טוב! העברת את הכוכב לפינה הימנית התחתונה!")`: מדפיס הודעת ניצחון.
    -   `break`: מסיים את לולאת המשחק (ואת המשחק).
"""