NIM:
=================
רמת קושי: 5
-----------------
המשחק "NIM" הוא משחק מתמטי לשני שחקנים. בתחילת המשחק ישנן מספר ערימות של אבנים (או פריטים אחרים). שחקנים בתורם לוקחים כל כמות אבנים מערימה אחת. השחקן שלוקח את האבן האחרונה מנצח.

כללי המשחק:
1.  בתחילת המשחק ישנן מספר ערימות אבנים, מספר האבנים בכל ערימה מוגדר.
2.  שחקנים בתורם לוקחים כל כמות אבנים שאינה אפסית מערימה אחת.
3.  השחקן שלוקח את האבן האחרונה, מנצח.
-----------------
אלגוריתם:
1.  אתחול ערימות האבנים (רשימה `P`).
2.  הצגת המצב הנוכחי של ערימות האבנים.
3.  התחלת לולאת המשחק, כל עוד סך כל האבנים בערימות גדול מ-0.
4.  בקשת מספר הערימה וכמות האבנים לקחת מהשחקן הנוכחי (אדם או מחשב).
    4.1 בדיקת תקינות הקלט: מספר הערימה חייב להיות בטווח הערכים המותרים, וכמות האבנים לא תעלה על הכמות הנוכחית בערימה שנבחרה.
5.  החסרת הכמות שנבחרה של אבנים מהערימה שנבחרה.
6.  הצגת המצב הנוכחי של ערימות האבנים.
7.  החלפת התור לשחקן הבא.
8.  כאשר סך כל האבנים שווה ל-0, קביעת המנצח והכרזה עליו.
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
    DisplayPiles --> GameLoopStart{"תחילת לולאת המשחק: כל עוד יש אבנים"}
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
    GameLoopStart -- Нет --> DetermineWinner["קביעת מנצח"]
    DetermineWinner --> OutputWinner["פלט מנצח"]
    OutputWinner --> End["סיום"]
```
מקרא:
    Start - התחלת המשחק.
    InitializePiles - אתחול ערימות האבנים (piles) בערכים אקראיים מ-1 עד 10 והגדרת התור הראשון (turn) ל-0 (שחקן 1).
    DisplayPiles - הצגת המצב הנוכחי של ערימות האבנים.
    GameLoopStart - תחילת לולאת המשחק הראשית. הלולאה נמשכת, כל עוד יש לפחות אבן אחת בערימות.
    GetInput - בקשת קלט מהשחקן של מספר הערימה (pileNumber) וכמות האבנים להסרה (stonesToRemove).
    ValidateInput - בדיקת תקינות הקלט: לוודא שמספר הערימה וכמות האבנים מותרים.
    UpdatePiles - עדכון מצב הערימות, החסרת הכמות שנבחרה של אבנים מהערימה שנבחרה.
    DisplayPiles2 - הצגת המצב המעודכן של הערימות.
    SwitchPlayer - החלפת תור בין השחקנים (שחקן 1 ושחקן 2).
    OutputError - פלט הודעה על שגיאת קלט, אם הקלט אינו תקין.
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
    piles (list): רשימה, המייצגת את ערימות האבנים.
    """
    print("מצב הערימות הנוכחי:")
    for i, pile in enumerate(piles):
        print(f"ערימה {i + 1}: {pile} אבנים")
# פונקציה עבור מהלך שחקן
def get_player_move(piles, player):
        """
        מבקשת מהשחקן את מספר הערימה ואת כמות האבנים להסרה.
        
        Args:
            piles (list): רשימה, המייצגת את ערימות האבנים.
            player (int): מספר השחקן הנוכחי (1 או 2).

        Returns:
            tuple: טאפל, המכיל את מספר הערימה ואת כמות האבנים להסרה.
        """

        while True:
            try:
                pile_number = int(input(f"שחקן {player}, בחר מספר ערימה (1-{len(piles)}): ")) - 1
                if 0 <= pile_number < len(piles):
                    stones_to_remove = int(input(f"שחקן {player}, כמה אבנים לקחת מערימה {pile_number + 1}: "))
                    if 0 < stones_to_remove <= piles[pile_number]:
                        return pile_number, stones_to_remove
                    else:
                        print("כמות אבנים בלתי חוקית. אנא בחר ערך מ-1 ועד הכמות הנוכחית בערימה.")
                else:
                    print("מספר ערימה בלתי חוקי. אנא בחר ערימה קיימת.")
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
    
    # לולאת המשחק
    while sum(piles) > 0:
        display_piles(piles)
        # מהלך השחקן הנוכחי
        pile_number, stones_to_remove = get_player_move(piles, current_player + 1)
        piles[pile_number] -= stones_to_remove
        current_player = (current_player + 1) % 2 # החלפת שחקן
    # קביעת המנצח
    print(f"שחקן {current_player + 1} ניצח!")

# הפעלת המשחק
if __name__ == "__main__":
    play_nim()
"""
הסבר הקוד:

1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים (מספר האבנים בערימות).
2. **פונקציה `display_piles(piles)`**:
    -   מקבלת רשימה `piles`, המייצגת את ערימות האבנים.
    -   מציגה על המסך את המצב הנוכחי של כל ערימה, באמצעות `enumerate` להצגת מספר הערימה ומספר האבנים בה.
3. **פונקציה `get_player_move(piles, player)`**:
     - מבקשת מהשחקן הנוכחי `player` את מספר הערימה ואת כמות האבנים להסרה.
    -  בודקת את תקינות הקלט:
        -   מספר הערימה חייב להיות בטווח הערכים המותרים (מ-1 ועד מספר הערימות).
        -   כמות האבנים חייבת להיות גדולה מאפס ולא לעלות על כמות האבנים בערימה שנבחרה.
    -  מחזירה את מספר הערימה (עם אינדקס, החל מ-0) ואת כמות האבנים להסרה.
4. **פונקציה `play_nim()`**:
    -   מאתחלת שלוש ערימות אבנים בערכים אקראיים מ-1 עד 10.
    -   `current_player = 0`: מגדירה את השחקן הראשון (שחקן 1).
    -  לולאת המשחק הראשית `while sum(piles) > 0`: נמשכת, כל עוד יש אבנים בערימות.
    -   קוראת ל-`display_piles()` כדי להציג את המצב הנוכחי של הערימות.
    -   קוראת ל-`get_player_move()` כדי לקבל את מהלך השחקן הנוכחי.
    -   מעדכנת את מספר האבנים בערימה שנבחרה.
    -   מחליפה שחקן `current_player = (current_player + 1) % 2` (0 -> 1, 1 -> 0).
    -   לאחר סיום הלולאה (כאשר כל האבנים נלקחו) מכריזה על המנצח.
5.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`:  מבטיחה שהמשחק יופעל, רק אם הסקריפט מופעל ישירות.
    -   `play_nim()`: קוראת לפונקציה להתחלת המשחק.
"""