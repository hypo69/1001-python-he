POETRY:
=================
דרגת קושי: 5
-----------------
המשחק "פואטרי" הוא משחק שבו המחשב מייצר ביטויים אקראיים על ידי בחירה של מילים אקראיות מתוך רשימות מוגדרות מראש. השחקן יכול להשפיע על תהליך הייצור באמצעות הזנת קודים שונים, אשר משנים את מקור המילים.
מטרת המשחק היא לצפות ולהעריך את התוצאות האקראיות, ולעתים אבסורדיות, של יצירת הביטויים.

כללי המשחק:
1. בתחילת המשחק, המחשב מציג ברכה והוראות.
2. המחשב בוחר באופן אקראי מילים מתוך רשימות של שמות עצם, פעלים, שמות תואר ומילות יחס.
3. באמצעות המילים שנבחרו, המחשב מרכיב משפט אקראי.
4. השחקן יכול להשפיע על הפלט באמצעות הזנת הקודים הבאים:
    - 1: משנה את רשימת שמות העצם.
    - 2: משנה את רשימת הפעלים.
    - 3: משנה את רשימת שמות התואר.
    - 4: משנה את רשימת מילות היחס.
    - 0: מסיים את המשחק.
5. לאחר הזנת קוד, המחשב מחליף את הרשימה המתאימה ברשימה חדשה, ומציג ביטוי חדש שנוצר.
6. המשחק נמשך עד שהשחקן מזין את הקוד 0.
-----------------
אלגוריתם:
1. אתחול רשימות שמות העצם (Nouns), הפעלים (Verbs), שמות התואר (Adjectives) ומילות היחס (Prepositions) עם ערכי התחלה.
2. הצגת ברכה והוראות.
3. התחלת לולאה שנמשכת כל עוד השחקן לא בחר באפשרות 0:
    3.1 ייצור מספר אקראי בין 1 ל-4.
    3.2 אם המספר שווה ל-1, ייצור ביטוי אקראי באמצעות הערכים הנוכחיים ברשימות:
        - בחירת שם עצם אקראי מרשימת שמות העצם.
        - בחירת פועל אקראי מרשימת הפעלים.
        - בחירת שם תואר אקראי מרשימת שמות התואר.
        - בחירת מילת יחס אקראית מרשימת מילות היחס.
        - הרכבת המשפט והצגתו על המסך.
        - שאילת המשתמש מה ברצונו לשנות (להזין 0 ליציאה).
    3.3 אם המספר אינו 1, בקשת קלט קוד מהשחקן (0, 1, 2, 3, או 4).
    3.4 אם הקלט הוא 1, שינוי רשימת שמות העצם לרשימה חדשה.
    3.5 אם הקלט הוא 2, שינוי רשימת הפעלים לרשימה חדשה.
    3.6 אם הקלט הוא 3, שינוי רשימת שמות התואר לרשימה חדשה.
    3.7 אם הקלט הוא 4, שינוי רשימת מילות היחס לרשימה חדשה.
    3.8 אם הקלט הוא 0, סיום המשחק.
4. הצגת ההודעה "BYE".
5. סיום התוכנית.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeLists["<p align='left'>אתחול רשימות:
    <code><b>
    nouns = ['BIRDS','CATS'...]
    verbs = ['FLY','RUN'...]
    adjectives = ['RED','BLUE'...]
    prepositions = ['OVER','UNDER'...]
    </b></code></p>"]
    InitializeLists --> OutputInstructions["הצגת הוראות"]
    OutputInstructions --> LoopStart{"תחילת לולאה: כל עוד הקלט אינו 0"}
    LoopStart -- כן --> GenerateRandomNumber["<code><b>randomNumber = random(1,4)</b></code>"]
    GenerateRandomNumber --> CheckRandomNumber{"בדיקה: <code><b>randomNumber == 1?</b></code>"}
    CheckRandomNumber -- כן --> GeneratePhrase["<p align='left'>ייצור ביטוי אקראי:
    <code><b>
    randomNoun = random(nouns)
    randomVerb = random(verbs)
    randomAdjective = random(adjectives)
    randomPreposition = random(prepositions)
    phrase = 'THE' + randomAdjective + randomNoun + randomVerb + randomPreposition + 'THE FOREST'
    </b></code></p>"]
    GeneratePhrase --> OutputPhrase["הצגת ביטוי: <code><b>phrase</b></code>"]
    OutputPhrase --> InputCode["קלט קוד מהמשתמש: <code><b>userCode</b></code>"]
    InputCode --> CheckUserCode{"בדיקה: <code><b>userCode == 0?</b></code>"}
    CheckUserCode -- כן --> OutputBye["הצגת הודעה: <b>BYE</b>"]
    OutputBye --> End["סוף"]
    CheckUserCode -- לא --> ProcessCode["עיבוד קוד: <code><b>if/else</b></code>"]
    ProcessCode --> LoopStart
    CheckRandomNumber -- לא --> InputCode2["קלט קוד מהמשתמש: <code><b>userCode</b></code>"]
    InputCode2 --> CheckUserCode2{"בדיקה: <code><b>userCode == 0?</b></code>"}
    CheckUserCode2 -- כן --> OutputBye2["הצגת הודעה: <b>BYE</b>"]
    OutputBye2 --> End
    CheckUserCode2 -- לא --> ProcessCode2["עיבוד קוד: <code><b>if/else</b></code>"]
    ProcessCode2 --> LoopStart
```

מקרא:
    Start - התחלת התוכנית.
    InitializeLists - אתחול רשימות nouns, verbs, adjectives ו-prepositions בערכי התחלה.
    OutputInstructions - הצגת הוראות למשתמש על המסך.
    LoopStart - תחילת לולאה, החוזרת על עצמה כל עוד המשתמש לא הזין 0.
    GenerateRandomNumber - ייצור מספר אקראי בין 1 ל-4.
    CheckRandomNumber - בדיקה האם המספר האקראי שווה ל-1.
    GeneratePhrase - ייצור ביטוי אקראי על בסיס רשימות המילים הנוכחיות.
    OutputPhrase - הצגת הביטוי שנוצר על המסך.
    InputCode - בקשת קלט קוד מהמשתמש.
    CheckUserCode - בדיקה האם הקוד שהוזן שווה ל-0 לסיום המשחק.
    OutputBye - הצגת ההודעה "BYE" לפני סיום התוכנית.
    End - סוף התוכנית.
    ProcessCode - קריאה לעיבוד קוד, לשינוי רשימות המילים.
    InputCode2 - בקשת קלט קוד מהמשתמש.
    CheckUserCode2 - בדיקה האם הקוד שהוזן שווה ל-0 לסיום המשחק.
    OutputBye2 - הצגת ההודעה "BYE" לפני סיום התוכנית.
    ProcessCode2 - קריאה לעיבוד קוד, לשינוי רשימות המילים.
```
import random

# רשימות מילים התחלתיות
nouns = ["BIRDS", "CATS", "DOGS", "FISH", "TREES", "FLOWERS", "RIVERS", "MOUNTAINS", "CLOUDS", "STARS"]
verbs = ["FLY", "RUN", "SWIM", "JUMP", "GROW", "BLOOM", "FLOW", "CLIMB", "FLOAT", "SHINE"]
adjectives = ["RED", "BLUE", "GREEN", "YELLOW", "TALL", "SHORT", "BIG", "SMALL", "BRIGHT", "DARK"]
prepositions = ["OVER", "UNDER", "IN", "ON", "BY", "NEAR", "THROUGH", "AROUND", "ACROSS", "ALONG"]


def change_list(list_name):
    """פונקציה לשינוי רשימת מילים."""
    new_list = input(f"הזן מילים חדשות לרשימת ה{list_name} מופרדות בפסיקים: ").upper().split(",")
    return new_list


print("ברוכים הבאים למשחק POETRY!")
print("הקש:")
print("1 כדי לשנות את שמות העצם")
print("2 כדי לשנות את הפעלים")
print("3 כדי לשנות את שמות התואר")
print("4 כדי לשנות את מילות היחס")
print("0 כדי לצאת")

while True:
    # מייצרים מספר אקראי בין 1 ל-4
    randomNumber = random.randint(1, 4)
    
    if randomNumber == 1:
       # מייצרים משפט
       random_noun = random.choice(nouns)
       random_verb = random.choice(verbs)
       random_adjective = random.choice(adjectives)
       random_preposition = random.choice(prepositions)

       phrase = f"THE {random_adjective} {random_noun} {random_verb} {random_preposition} THE FOREST"
       print(f"ביטוי אקראי: {phrase}")
       user_code = input("הזן קוד (0 ליציאה): ")
       if user_code == "0":
            break
       else:
          try:
            user_code = int(user_code)
          except ValueError:
            print ("קלט לא תקין, הזן 0, 1, 2, 3 או 4")
            continue

    else:
       user_code = input("הזן קוד (0 ליציאה): ")
       if user_code == "0":
            break
       else:
          try:
            user_code = int(user_code)
          except ValueError:
            print ("קלט לא תקין, הזן 0, 1, 2, 3 או 4")
            continue
          
    if user_code == 1:
            nouns = change_list("שמות העצם")
    elif user_code == 2:
            verbs = change_list("הפעלים")
    elif user_code == 3:
            adjectives = change_list("שמות התואר")
    elif user_code == 4:
            prepositions = change_list("מילות היחס")
print("BYE")

"""
הסבר קוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים ובחירת אלמנטים אקראיים מתוך רשימה.

2.  **אתחול רשימות מילים**:
    -   `nouns = [...]`: מאתחל את רשימת שמות העצם.
    -   `verbs = [...]`: מאתחל את רשימת הפעלים.
    -   `adjectives = [...]`: מאתחל את רשימת שמות התואר.
    -   `prepositions = [...]`: מאתחל את רשימת מילות היחס.
    
3.  **פונקציה `change_list(list_name)`**:
    -   מגדיר פונקציה `change_list`, המאפשרת למשתמש לשנות רשימת מילים.
    -   `new_list = input(...)`: מבקש קלט מהמשתמש עבור מילים חדשות מופרדות בפסיקים, ממיר את הקלט לאותיות גדולות ומפצל אותו לרשימה.
    -   `return new_list`: מחזיר את רשימת המילים החדשה.

4.  **ברכה והוראות**:
    -   מציג על המסך ברכה והוראות למשתמש.

5. **הלולאה הראשית `while True`**:
    -   לולאה אינסופית, הנמשכת כל עוד המשתמש לא הזין `0`.
    - `randomNumber = random.randint(1, 4)`: מייצרים מספר אקראי בין 1 ל-4.
    -  **תנאי ייצור ביטוי**:
      - `if randomNumber == 1`: בודקים האם המספר האקראי שווה ל-1.
      -  `random_noun = random.choice(nouns)`: בוחרים באופן אקראי שם עצם מהרשימה.
      -  `random_verb = random.choice(verbs)`: בוחרים באופן אקראי פועל מהרשימה.
      -  `random_adjective = random.choice(adjectives)`: בוחרים באופן אקראי שם תואר מהרשימה.
      -  `random_preposition = random.choice(prepositions)`: בוחרים באופן אקראי מילת יחס מהרשימה.
      -  `phrase = f"THE {random_adjective} {random_noun} {random_verb} {random_preposition} THE FOREST"`: מרכיבים ביטוי אקראי, באמצעות המילים שנבחרו.
      -   `print(f"ביטוי אקראי: {phrase}")`: מציגים את הביטוי שנוצר על המסך.
      -   `user_code = input("הזן קוד (0 ליציאה): ")`: מבקשים מהמשתמש להזין קוד לשינוי רשימת מילים.
      -   `if user_code == "0": break`: אם המשתמש מזין `0`, אזי מסיימים את הלולאה (את המשחק).
    -  **תנאי שינוי רשימות**:
      - `else:`: אם המספר האקראי אינו 1, אזי מתבקש קלט קוד לשינוי הרשימות.
      -   `user_code = input("הזן קוד (0 ליציאה): ")`: מבקשים מהמשתמש להזין קוד לשינוי רשימת מילים.
      -   `if user_code == "0": break`: אם המשתמש מזין `0`, אזי מסיימים את הלולאה (את המשחק).
       - `try/except`: מטפלים בקלט שגוי.
    -  `if user_code == 1:`: אם המשתמש מזין `1`, אזי קוראים לפונקציה `change_list` לשינוי רשימת שמות העצם.
    -   `elif user_code == 2:`: אם המשתמש מזין `2`, אזי קוראים לפונקציה `change_list` לשינוי רשימת הפעלים.
    -   `elif user_code == 3:`: אם המשתמש מזין `3`, אזי קוראים לפונקציה `change_list` לשינוי רשימת שמות התואר.
    -   `elif user_code == 4:`: אם המשתמש מזין `4`, אזי קוראים לפונקציה `change_list` לשינוי רשימת מילות היחס.
   
6.  **סיום המשחק**:
    -   `print("BYE")`: מציג את ההודעה "BYE" לאחר סיום הלולאה (כאשר המשתמש הזין 0).
"""