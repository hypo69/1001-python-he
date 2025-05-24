"""
Solver of the Checkerboard Puzzle

Rules of the Puzzle:
1. The board is an 8x8 grid (standard checkerboard).
2. Initially, 48 checkers are placed on the two outermost rows (rows 1 and 8).
3. Checkers can only move diagonally.
4. A checker can "jump" over an adjacent checker diagonally if the landing square is empty.
5. The jumped checker is removed from the board.
6. The objective is to remove as many checkers as possible by performing valid jumps.
7. The game ends when no more valid jumps are possible.
"""

"""
פותר חידת לוח הדמקה

כללי החידה:
1. הלוח הוא רשת 8x8 (לוח דמקה סטנדרטי).
2. בתחילה, 48 אבני דמקה ממוקמות בשתי השורות החיצוניות ביותר (שורות 1 ו-8).
3. אבני דמקה יכולות לנוע אך ורק באלכסון.
4. אבן דמקה יכולה "לקפוץ" מעל אבן דמקה סמוכה באלכסון אם המשבצת שאליה היא נוחתת ריקה.
5. אבן הדמקה שנקפצה מוסרת מהלוח.
6. המטרה היא להסיר כמה שיותר אבני דמקה על ידי ביצוע קפיצות חוקיות.
7. המשחק מסתיים כאשר לא ניתן לבצע עוד קפיצות חוקיות.
"""

from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Checkerboard:
    """
    Represents the checkerboard and its state.
    """
    """
    מייצג את לוח הדמקה ומצבו.
    """
    board: List[List[int]]  # 0 = empty, 1 = checker
    removed_checkers: int = 0  # Counter for removed checkers
    # removed_checkers: int = 0  # מונה עבור אבני דמקה שהוסרו

    def __post_init__(self) -> None:
        """
        Initialize the board with 48 checkers on the outermost rows.
        """
        """
        מאפס את הלוח עם 48 אבני דמקה בשורות החיצוניות ביותר.
        """
        for row in [0, 7]:  # Rows 1 and 8 (0-indexed)
            # לולאה עבור שורות 1 ו-8 (ממוספרות מ-0)
            for col in range(8):
                self.board[row][col] = 1

    def is_valid_jump(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        """
        Check if a jump is valid.
        Rules:
        - The landing position must be within the board.
        - The landing position must be empty.
        - There must be a checker to jump over.
        - The jump must be diagonal (2 squares in row and column).

        :param start: Tuple (row, col) of the starting position.
        :param end: Tuple (row, col) of the landing position.
        :return: True if the jump is valid, False otherwise.
        """
        """
        בדיקה האם קפיצה חוקית.
        כללים:
        - מיקום הנחיתה חייב להיות בתוך גבולות הלוח.
        - מיקום הנחיתה חייב להיות ריק.
        - חייבת להיות אבן דמקה לקפוץ מעליה.
        - הקפיצה חייבת להיות באלכסון (מרחק 2 משבצות בשורה ובעמודה).

        :param start: טאפל (שורה, עמודה) של מיקום ההתחלה.
        :param end: טאפל (שורה, עמודה) של מיקום הנחיתה.
        :return: True אם הקפיצה חוקית, אחרת False.
        """
        start_row, start_col = start
        end_row, end_col = end

        # Check if the landing position is within the board
        # בדיקה האם מיקום הנחיתה בתוך גבולות הלוח
        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        # Check if the landing position is empty
        # בדיקה האם מיקום הנחיתה ריק
        if self.board[end_row][end_col] != 0:
            return False

        # Calculate the middle position (the jumped checker)
        # חישוב מיקום האמצע (אבן הדמקה שנקפצה)
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2

        # Check if there is a checker to jump over
        # בדיקה האם יש אבן דמקה לקפוץ מעליה
        if self.board[mid_row][mid_col] != 1:
            return False

        # Check if the jump is diagonal
        # בדיקה האם הקפיצה באלכסון
        if abs(start_row - end_row) != 2 or abs(start_col - end_col) != 2:
            return False

        return True

    def perform_jump(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Perform a jump and remove the jumped checker.
        Rules:
        - Move the checker from the start position to the end position.
        - Remove the checker in the middle position.
        - Increment the count of removed checkers.

        :param start: Tuple (row, col) of the starting position.
        :param end: Tuple (row, col) of the landing position.
        """
        """
        ביצוע קפיצה והסרת אבן הדמקה שנקפצה.
        כללים:
        - הזזת אבן הדמקה ממיקום ההתחלה למיקום הנחיתה.
        - הסרת אבן הדמקה ממיקום האמצע.
        - הגדלת מונה אבני הדמקה שהוסרו.

        :param start: טאפל (שורה, עמודה) של מיקום ההתחלה.
        :param end: טאפל (שורה, עמודה) של מיקום הנחיתה.
        """
        start_row, start_col = start
        end_row, end_col = end

        # Move the checker
        # הזזת אבן הדמקה
        self.board[start_row][start_col] = 0
        self.board[end_row][end_col] = 1

        # Remove the jumped checker
        # הסרת אבן הדמקה שנקפצה
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        self.board[mid_row][mid_col] = 0

        # Increment the removed checkers count
        # הגדלת מונה אבני הדמקה שהוסרו
        self.removed_checkers += 1

    def find_possible_jumps(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        """
        Find all possible jumps on the board.
        Rules:
        - Scan the board for checkers.
        - For each checker, check all four diagonal directions for valid jumps.

        :return: List of tuples, where each tuple contains (start, end) positions for valid jumps.
        """
        """
        מציאת כל הקפיצות האפשריות על הלוח.
        כללים:
        - סריקת הלוח אחר אבני דמקה.
        - עבור כל אבן דמקה, בדיקה של כל ארבעת הכיוונים האלכסוניים לאיתור קפיצות חוקיות.

        :return: רשימה של טאפלים, כאשר כל טאפל מכיל את מיקומי (התחלה, סיום) עבור קפיצות חוקיות.
        """
        jumps: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == 1:
                    # Check all four diagonal directions
                    # בדיקה של כל ארבעת הכיוונים האלכסוניים
                    for dr, dc in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
                        start = (row, col)
                        end = (row + dr, col + dc)
                        if self.is_valid_jump(start, end):
                            jumps.append((start, end))
        return jumps

    def play(self) -> None:
        """
        Simulate the game by performing jumps until no more jumps are possible.
        Rules:
        - Repeatedly find and perform valid jumps.
        - Stop when no more jumps are possible.
        """
        """
        סימולציה של המשחק על ידי ביצוע קפיצות עד שלא ניתן לבצע עוד קפיצות.
        כללים:
        - מציאה וביצוע חוזרים של קפיצות חוקיות.
        - עצירה כאשר לא ניתן לבצע עוד קפיצות.
        """
        while True:
            jumps = self.find_possible_jumps()
            if not jumps:
                break  # No more jumps possible
                # אין יותר קפיצות אפשריות

            # Perform the first valid jump (can be optimized further)
            # ביצוע הקפיצה החוקית הראשונה (ניתן לשפר בהמשך)
            start, end = jumps[0]
            self.perform_jump(start, end)

        print(f"Total checkers removed: {self.removed_checkers}")
        print(f"סה\"כ אבני דמקה שהוסרו: {self.removed_checkers}")

    def display_board(self) -> None:
        """
        Display the current state of the board.
        Rules:
        - Print the board with '•' for checkers and '.' for empty squares.
        """
        """
        הצגת המצב הנוכחי של הלוח.
        כללים:
        - הדפסת הלוח עם '•' עבור אבני דמקה ו-'.' עבור משבצות ריקות.
        """
        for row in self.board:
            print(" ".join("•" if cell == 1 else "." for cell in row))
        print()


# Main program
# תוכנית ראשית
if __name__ == "__main__":
    print("Initial Board:")
    print("לוח התחלתי:")
    # Initialize the board with empty squares
    # אתחול הלוח עם משבצות ריקות
    initial_board = [[0 for _ in range(8)] for _ in range(8)]
    game = Checkerboard(board=initial_board)
    game.display_board()

    print("Playing the game...")
    print("מריץ את המשחק...")
    game.play()

    print("Final Board:")
    print("לוח סופי:")
    game.display_board()