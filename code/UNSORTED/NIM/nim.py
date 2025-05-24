NIM:
=================
מורכבות: 5
-----------------
המשחק "NIM" הוא משחק מתמטי לשני שחקנים. בתחילת המשחק ישנן מספר ערימות של אבנים (או פריטים אחרים). השחקנים לוקחים בתורם כל כמות של אבנים מערימה אחת. מנצח השחקן שלקח את האבן האחרונה.

כללי המשחק:
1.  בתחילת המשחק ישנן מספר ערימות של אבנים, כמות האבנים בכל ערימה ניתנת מראש.
2.  שחקנים לוקחים בתורם כל כמות חיובית של אבנים מערימה אחת.
3.  השחקן שלוקח את האבן האחרונה, מנצח.
-----------------
אלגוריתם:
1.  לאתחל את ערימות האבנים (מערך `P`).
2.  להציג את המצב הנוכחי של ערימות האבנים.
3.  להתחיל מחזור משחק, כל עוד סך כל האבנים בערימות גדול מ-0.
4.  לבקש מהשחקן הנוכחי (אדם או מחשב) את מספר הערימה ואת כמות האבנים לקחת.
    4.1 לבדוק את תקינות הקלט, מספר הערימה חייב להיות בטווח הערכים המותר, וכמות האבנים לא תעלה על הכמות הנוכחית בערימה הנבחרת.
5.  לחסר את כמות האבנים שנבחרה מהערימה הנבחרת.
6.  להציג את המצב הנוכחי של ערימות האבנים.
7.  להחליף תור לשחקן הבא.
8.  כאשר סך כל האבנים שווה ל-0, לקבוע ולהכריז על המנצח.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializePiles["<p align='left'>אתחול ערימות:
    <code><b>
    piles = [random(1,10),random(1,10),random(1,10)]
    turn = 0
    </b></code></p>"]
    InitializePiles --> DisplayPiles["הצגת ערימות"]
    DisplayPiles --> GameLoopStart{"תחילת מחזור המשחק: כל עוד יש אבנים"}
    GameLoopStart -- Да --> GetInput["<p align='left'>קלט שחקן:
    <code><b>
    pileNumber
    stonesToRemove
    </b></code></p>"]
    GetInput --> ValidateInput{"<p align='left'>בדיקת קלט:
    <code><b>
    pileNumber valid?
    stonesToRemove valid?
    </b></code></p>"}
    ValidateInput -- Да --> UpdatePiles["<code><b>piles[pileNumber] -= stonesToRemove</b></code>"]
    UpdatePiles --> DisplayPiles2["הצגת ערימות"]
    DisplayPiles2 --> SwitchPlayer["<code><b>turn = (turn + 1) % 2</b></code>"]
    SwitchPlayer --> GameLoopStart
    ValidateInput -- Нет --> OutputError["פלט שגיאת קלט"]
    OutputError --> GetInput
    GameLoopStart -- Нет --> DetermineWinner["קביעת המנצח"]
    DetermineWinner --> OutputWinner["פלט המנצח"]
    OutputWinner --> End["סוף"]
```
מקרא:
    Start - תחילת המשחק.
    InitializePiles - אתחול ערימות האבנים (`piles`) בערכים אקראיים מ-1 עד 10 והגדרת התור הראשון (`turn`) ל-0 (שחקן 1).
    DisplayPiles - הצגת המצב הנוכחי של ערימות האבנים.
    GameLoopStart - תחילת מחזור המשחק הראשי. המחזור נמשך כל עוד יש לפחות אבן אחת בערימות.
    GetInput - בקשת קלט מהשחקן - מספר הערימה (`pileNumber`) וכמות האבנים להסרה (`stonesToRemove`).
    ValidateInput - בדיקת תקינות הקלט: לוודא שמספר הערימה וכמות האבנים חוקיים.
    UpdatePiles - עדכון מצב הערימות, חיסור כמות האבנים שנבחרה מהערימה הנבחרת.
    SwitchPlayer - החלפת התור בין השחקנים (שחקן 1 ושחקן 2).
    OutputError - פלט הודעת שגיאת קלט, אם הקלט אינו תקין.
    DetermineWinner - קביעת המנצח לאחר סיום המשחק.
    OutputWinner - פלט הודעה על ניצחון השחקן המתאים.
    End - סיום המשחק.
"""
import random

# פונקציה להצגת ערימות האבנים
def display_piles(piles):
    """
    מציגה את המצב הנוכחי של ערימות האבנים.
    
    Args:
    piles (list): רשימה המייצגת את ערימות האבנים.
    """
    print("מצב הערימות הנוכחי:")
    for i, pile in enumerate(piles):
        print(f"ערימה {i + 1}: {pile} אבנים")
# פונקציה עבור תור השחקן
def get_player_move(piles, player):
        """
        מבקשת מהשחקן את מספר הערימה ואת כמות האבנים להסרה.
        
        Args:
            piles (list): רשימה המייצגת את ערימות האבנים.
            player (int): מספר השחקן הנוכחי (1 או 2).

        Returns:
            tuple: טאפל המכיל את מספר הערימה ואת כמות האבנים להסרה.
        """

        while True:
            try:
                pile_number = int(input(f"שחקן {player}, בחר מספר ערימה (1-{len(piles)}): ")) - 1
                if 0 <= pile_number < len(piles):
                    stones_to_remove = int(input(f"שחקן {player}, כמה אבנים לקחת מהערימה {pile_number + 1}: "))
                    if 0 < stones_to_remove <= piles[pile_number]:
                        return pile_number, stones_to_remove
                    else:
                        print("כמות אבנים לא חוקית. אנא בחר ערך בין 1 לכמות הנוכחית בערימה.")
                else:
                    print("מספר ערימה לא חוקי. אנא בחר ערימה קיימת.")
            except ValueError:
                print("קלט לא תקין. אנא הזן מספרים שלמים.")
# פונקציית המשחק הראשית
def play_nim():
    """
    מממשת את משחק NIM.
    """
    # אתחול ערימות האבנים
    piles = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    current_player = 0  # 0 - שחקן 1, 1 - שחקן 2
    
    # מחזור המשחק
    while sum(piles) > 0:
        display_piles(piles)
        # תור השחקן הנוכחי
        pile_number, stones_to_remove = get_player_move(piles, current_player + 1)
        piles[pile_number] -= stones_to_remove
        current_player = (current_player + 1) % 2 # החלפת שחקן
    # קביעת המנצח
    print(f"שחקן {current_player + 1} ניצח!")

# הפעלת המשחק
if __name__ == "__main__":
    play_nim()
"""
**הסבר על הקוד:**

1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים (כמות האבנים בערימות).
2. **פונקציה `display_piles(piles)`**:
    -   מקבלת רשימה `piles`, המייצגת את ערימות האבנים.
    -   מציגה על המסך את המצב הנוכחי של כל ערימה, תוך שימוש ב-`enumerate` להצגת מספר הערימה וכמות האבנים בה.
3. **פונקציה `get_player_move(piles, player)`**:
     - מבקשת מהשחקן הנוכחי `player` את מספר הערימה ואת כמות האבנים להסרה.
    -  בודקת את תקינות הקלט:
        -   מספר הערימה חייב להיות בטווח הערכים המותר (מ-1 עד מספר הערימות).
        -   כמות האבנים חייבת להיות גדולה מאפס ולא לעלות על כמות האבנים בערימה הנבחרת.
    -  מחזירה את מספר הערימה (עם אינדקס, החל מ-0) ואת כמות האבנים להסרה.
4. **פונקציה `play_nim()`**:
    -   מאתחלת שלוש ערימות אבנים בערכים אקראיים מ-1 עד 10.
    -   `current_player = 0`: מגדירה את השחקן הראשון (שחקן 1).
    -  מחזור המשחק הראשי `while sum(piles) > 0`: נמשך כל עוד יש אבנים בערימות.
    -   קוראת ל-`display_piles()` להצגת המצב הנוכחי של הערימות.
    -   קוראת ל-`get_player_move()` לקבלת תור השחקן הנוכחי.
    -   מעדכנת את כמות האבנים בערימה הנבחרת.
    -   מחליפה שחקן `current_player = (current_player + 1) % 2` (0 -> 1, 1 -> 0).
    -   לאחר סיום המחזור (כשכל האבנים נלקחו) מכריזה על המנצח.
5.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: מבטיח שהמשחק יופעל רק אם הסקריפט הופעל ישירות.
    -   `play_nim()`: קוראת לפונקציה להתחלת המשחק.
"""