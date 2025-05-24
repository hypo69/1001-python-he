**חיים (LIFE):**
=================
**מורכבות: 7**
-----------------
המשחק "חיים" הוא סימולציה של אוטומט תאי, שפותחה על ידי ג'ון קונוויי. שדה המשחק מורכב מרשת של תאים, כאשר כל אחד מהם יכול להיות באחד משני מצבים: "חי" או "מת". מצב כל תא בדור הבא תלוי במצב שכניו בדור הנוכחי. מטרת המשחק היא לצפות בהתפתחות של תצורה התחלתית של תאים ולחקור דפוסים מעניינים הנוצרים בתהליך הסימולציה.

**חוקי המשחק:**
1.  שדה המשחק מורכב מתאים, כאשר כל תא יכול להיות "חי" (מסומן בתו '*') או "מת" (מסומן ברווח ' ').
2.  בתחילת המשחק, השדה מתמלא באקראי או שנקבעת תצורה ספציפית של תאים.
3.  המעבר לדור הבא מתבצע לפי החוקים הבאים:
    -  תא חי עם פחות משני שכנים חיים מת מבדידות.
    -  תא חי עם שניים או שלושה שכנים חיים שורד לדור הבא.
    -  תא חי עם יותר משלושה שכנים חיים מת מצפיפות יתר.
    -  תא מת עם שלושה שכנים חיים בדיוק קם לתחייה.
4.  המשחק נמשך מספר מוגדר של דורות.

-----------------
**אלגוריתם:**
1.  בקש מהמשתמש את מימדי השדה (מספר שורות ועמודות).
2.  בקש מהמשתמש את מספר הדורות עבור הסימולציה.
3.  צור את הדור ההתחלתי:
    -   אם המשתמש הזין נתונים התחלתיים, השתמש בהם.
    -   אם לא, מלא את השדה באקראי בתאים חיים ומתים.
4.  עבור כל דור מ-1 עד למספר הדורות המוגדר:
    4.1 הצג על המסך את הדור הנוכחי (מצב השדה).
    4.2 צור שדה חדש (הדור הבא), תוך יישום חוקי המשחק:
        -   עבור כל תא בשדה הנוכחי:
            -   ספור את מספר השכנים החיים.
            -   בהתאם למצב התא ומספר השכנים בדור הנוכחי, קבע את מצבו בשדה החדש לפי חוקי המשחק.
    4.3 עדכן את השדה הנוכחי עם השדה החדש.
5.  בסיום הסימולציה, הצג על המסך את המצב הסופי של השדה.

-----------------

"""
import random
import time

def get_grid_size():
    """מבקש מהמשתמש את מימדי הרשת."""
    while True:
        try:
            rows = int(input("הזן מספר שורות: "))
            cols = int(input("הזן מספר עמודות: "))
            if rows > 0 and cols > 0:
                return rows, cols
            else:
                print("אנא הזן ערכים חיוביים עבור שורות ועמודות.")
        except ValueError:
            print("אנא הזן מספר שלם.")

def get_generations():
    """מבקש מהמשתמש את מספר הדורות."""
    while True:
        try:
            generations = int(input("הזן מספר דורות: "))
            if generations > 0:
                return generations
            else:
                print("אנא הזן מספר דורות חיובי.")
        except ValueError:
            print("אנא הזן מספר שלם.")


def get_initial_config(rows, cols):
    """מבקש מהמשתמש להזין תצורה התחלתית או להשתמש באקראית."""
    use_random = input("להשתמש בתצורה אקראית (y/n)? ").lower()
    if use_random != 'y':
        print("הזן תצורה התחלתית, השתמש ב-'*' עבור תאים חיים ו-' ' עבור תאים מתים.")
        print("הזן כל שורה בנפרד:")
        initial_config = []
        for _ in range(rows):
            while True:
              row_input = input()
              if len(row_input) == cols and all(cell in ['*', ' '] for cell in row_input):
                  initial_config.append(row_input)
                  break
              else:
                print(f"קלט לא תקין. הזן שורה באורך {cols} תווים '*' או ' '")
        return initial_config
    else:
        return  [['*' if random.random() > 0.5 else ' ' for _ in range(cols)] for _ in range(rows)]



def create_grid(rows, cols, initial_config=None):
    """יוצר את הרשת על בסיס המימדים והתצורה ההתחלתית שסופקו."""
    if initial_config:
        return [list(row) for row in initial_config]
    else:
        return [['*' if random.random() > 0.5 else ' ' for _ in range(cols)] for _ in range(rows)]


def print_grid(grid):
    """מדפיס את הרשת על המסך."""
    for row in grid:
        print(''.join(row))
    print("-" * len(grid[0]))

def count_live_neighbours(grid, row, col):
    """סופר את מספר השכנים החיים עבור התא הנתון."""
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col) and grid[i][j] == '*':
                count += 1
    return count

def apply_rules(grid, row, col):
    """מיישם את חוקי המשחק "חיים" לקביעת מצב התא בדור הבא."""
    live_neighbours = count_live_neighbours(grid, row, col)
    if grid[row][col] == '*':
        if live_neighbours < 2 or live_neighbours > 3:
            return ' '  # התא מת
        else:
            return '*'  # התא שורד
    else:
        if live_neighbours == 3:
            return '*'  # התא קם לתחייה
        else:
            return ' '  # התא נשאר מת


def next_generation(grid):
    """יוצר את הדור הבא של הרשת."""
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            new_grid[row][col] = apply_rules(grid, row, col)
    return new_grid

def play_game_of_life():
  """הפונקציה הראשית המנהלת את סימולציית המשחק "חיים"."""
  rows, cols = get_grid_size() # בקשת גודל הרשת מהמשתמש.
  generations = get_generations() # בקשת מספר הדורות מהמשתמש.
  initial_config = get_initial_config(rows, cols) # בקשת תצורה התחלתית מהמשתמש
  grid = create_grid(rows, cols, initial_config) # יצירת רשת המשחק.

  for generation in range(generations):
    print(f"דור: {generation + 1}")
    print_grid(grid)
    grid = next_generation(grid)
    time.sleep(0.5)

  print("הסימולציה הסתיימה")
  print("המצב הסופי של השדה:")
  print_grid(grid)

if __name__ == "__main__":
    play_game_of_life()

"""
**הסבר הקוד:**
1.  **ייבוא מודולים**:
    -   `import random`: מייבאת את המודול `random` ליצירת מספרים אקראיים.
    -   `import time`: מייבאת את המודול `time` להוספת השהיה בין הדורות.
2.  **הפונקציה `get_grid_size()`**:
    -   מבקשת מהמשתמש את מימדי הרשת (מספר שורות ועמודות), תוך בדיקת תקינות הקלט.
    -   מחזירה טאפל `rows, cols` של מספרים שלמים.
3.  **הפונקציה `get_generations()`**:
    -   מבקשת מהמשתמש את מספר הדורות עבור הסימולציה, תוך בדיקת תקינות הקלט.
    -   מחזירה מספר שלם `generations`.
4.  **הפונקציה `get_initial_config(rows, cols)`**:
    -   שואלת את המשתמש האם להשתמש בתצורה התחלתית אקראית או להזין אחת משלו.
    -   אם המשתמש אינו בוחר בתצורה אקראית, היא מבקשת את התצורה ההתחלתית, שורה אחר שורה, ובודקת את תקינות הקלט.
    -   אם המשתמש בוחר באקראית, היא מחזירה תצורה התחלתית אקראית.
    -   מחזירה רשימה של שורות (התצורה ההתחלתית).
5.  **הפונקציה `create_grid(rows, cols, initial_config=None)`**:
    -   יוצרת ומחזירה רשת (רשימה של רשימות) על בסיס המימדים `rows`, `cols` והתצורה ההתחלתית `initial_config`.
    -   אם `initial_config` סופקה, היא משתמשת בה ליצירת הרשת.
    -   אם `initial_config` לא סופקה, היא מייצרת רשת אקראית, שבה לכל תא יש סיכוי של 50% להיות חי (`'*'`) או מת (`' '`).
6.  **הפונקציה `print_grid(grid)`**:
    -   מדפיסה את הרשת הנוכחית על המסך.
    -   כל שורה ברשת מודפסת בשורה נפרדת, ומוסף קו מפריד.
7.  **הפונקציה `count_live_neighbours(grid, row, col)`**:
    -   סופרת את מספר השכנים החיים של התא בקואורדינטות `row` ו-`col` ברשת `grid`.
    -   שכנים נחשבים כל התאים הצמודים לתא הנתון באופן אופקי, אנכי ואלכסוני.
    -   מחזירה מספר שלם - מספר השכנים החיים.
8.  **הפונקציה `apply_rules(grid, row, col)`**:
    -   מיישמת את חוקי המשחק "חיים" עבור התא בקואורדינטות `row` ו-`col`.
    -   מחזירה '*' אם התא אמור להיות חי, ו-' ' אם התא אמור להיות מת.
    -   מחזירה את המצב החדש של התא.
9.  **הפונקציה `next_generation(grid)`**:
    -   יוצרת ומחזירה את הרשת של הדור הבא על בסיס הרשת הנוכחית.
    -   מיישמת את הפונקציה apply_rules על כל תא.
    -   יוצרת רשת חדשה (רשימה של רשימות) ומיישמת את חוקי המשחק לקביעת מצב כל תא בדור הבא.
10. **הפונקציה `play_game_of_life()`**:
    -   הפונקציה הראשית, המנהלת את סימולציית המשחק "חיים".
    -   קוראת לפונקציות get_grid_size(), get_generations() ו-create_grid() לאתחול המשחק.
    -   בלולאת for, מדפיסה על המסך את הדור הנוכחי, מחשבת ומדפיסה את הדור הבא.
    -   לאחר לולאת for, מדפיסה על המסך את המצב הסופי של השדה.
11. **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_game_of_life()` תופעל רק אם הקובץ מורץ ישירות, ולא מיובא כמודול.
    -   `play_game_of_life()`: קוראת לפונקציה להתחלת המשחק.
"""