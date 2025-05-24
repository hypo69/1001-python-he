AMAZIN:
=================
מורכבות: 5
-----------------
המשחק "AMAZIN" הוא משחק ניחוש מילים. המחשב בוחר מילה אקראית מרשימה מוגדרת מראש, והשחקן צריך לנחש אותה על ידי הזנת אותיות. לאחר כל ניסיון, המחשב מודיע האם האות שהוזנה קיימת במילה ובאיזו עמדה. על השחקן לנחש את המילה לפני שיאזלו כל הניסיונות.

כללי המשחק:
1. המחשב בוחר מילה אקראית מרשימה.
2. השחקן מקבל מספר מוגדר של ניסיונות (ברירת מחדל 5).
3. השחקן מזין אות.
4. המחשב מודיע האם האות קיימת במילה, ואם כן - באילו עמדות.
5. השחקן מנסה לנחש את המילה לפי האותיות.
6. אם השחקן מנחש את המילה, המשחק מסתיים בניצחון.
7. אם השחקן מסיים את כל הניסיונות, המשחק מסתיים בהפסד.
-----------------
אלגוריתם:
1. אתחול:
    1.1. הגדרת רשימת מילים.
    1.2. בחירת מילה אקראית מהרשימה.
    1.3. הגדרת מספר הניסיונות (ברירת מחדל 5).
    1.4. יצירת מחרוזת להצגת האותיות שניחשו (בתחילה כל העמדות מסומנות ב-"_").
2. התחלת לולאה "כל עוד מספר הניסיונות גדול מ-0 והמילה לא נוחשה":
    2.1. הדפסת המחרוזת עם האותיות שניחשו.
    2.2. בקשת קלט אות מהשחקן.
    2.3. הקטנת מספר הניסיונות ב-1.
    2.4. אם האות שהוזנה קיימת במילה שניחשו:
        2.4.1. החלפת הסימן "_" באות בעמדות המתאימות במחרוזת עם האותיות שניחשו.
        2.4.2. אם מחרוזת האותיות שניחשו שווה למילה שניחשו, הדפסת הודעת ניצחון ויציאה מהלולאה.
    2.5. אם האות שהוזנה אינה קיימת במילה שניחשו, הדפסת הודעה שאין אות כזו.
3. אם לאחר הלולאה המילה לא נוחשה (נותרו ניסיונות והמילה לא נוחשה), הדפסת הודעת הפסד והמילה שניחשו.
4. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול:<br>
    <code><b>wordList = [...]<br>
    targetWord = random(wordList)<br>
    attempts = 5<br>
    guessedWord = '___...'</b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה:<br><code><b>attempts > 0 and not wordGuessed</b></code>"}
    LoopStart -- Yes --> OutputGuessedWord["פלט: <code><b>guessedWord</b></code>"]
    OutputGuessedWord --> InputLetter["קלט אות: <code><b>userLetter</b></code>"]
    InputLetter --> DecreaseAttempts["<code><b>attempts = attempts - 1</b></code>"]
    DecreaseAttempts --> CheckLetter{"בדיקה: <code><b>userLetter in targetWord</b></code>?"}
    CheckLetter -- Yes --> UpdateGuessedWord["עדכון <code><b>guessedWord</b></code>"]
    UpdateGuessedWord --> CheckWin{"בדיקה: <code><b>guessedWord == targetWord</b></code>?"}
     CheckWin -- Yes --> OutputWin["פלט: <b>ניצחון</b>"]
     OutputWin --> End["סיום"]
    CheckWin -- No --> LoopStart
    CheckLetter -- No --> OutputNoLetter["פלט: <b>אין אות כזו</b>"]
    OutputNoLetter --> LoopStart
    LoopStart -- No --> CheckLose{"בדיקה: <code><b>attempts <=0 and not wordGuessed</b></code>"}
    CheckLose -- Yes --> OutputLose["פלט: <b>הפסד, targetWord</b>"]
    OutputLose --> End
     CheckLose -- No --> End

```
מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: wordList (רשימת מילים), targetWord (המילה שיש לנחש נבחרת באופן אקראי), attempts (מספר הניסיונות) נקבע ל-5, guessedWord (המחרוזת עם האותיות שניחשו) מאותחלת בתווים "_".
    LoopStart - תחילת לולאה, הנמשכת כל עוד יש ניסיונות והמילה לא נוחשה.
    OutputGuessedWord - הדפסת המצב הנוכחי של האותיות שניחשו.
    InputLetter - בקשת קלט אות מהמשתמש.
    DecreaseAttempts - הקטנת מספר הניסיונות שנותרו.
    CheckLetter - בדיקה האם האות שהוזנה קיימת במילה שניחשו.
    UpdateGuessedWord - עדכון המחרוזת של האותיות שניחשו.
    CheckWin - בדיקה האם המילה נוחשה.
    OutputWin - הדפסת הודעת ניצחון.
    OutputNoLetter - הדפסת הודעה שהאות שהוזנה אינה קיימת במילה.
    CheckLose - בדיקה האם נגמרו הניסיונות והמילה לא נוחשה.
    OutputLose - הדפסת הודעת הפסד והמילה שניחשו.
    End - סיום התוכנית.
```
import random

# 1. אתחול
# 1.1 רשימת המילים למשחק
wordList = ["python", "java", "kotlin", "swift", "javascript", "go", "ruby"]
# 1.2 בחירת מילה אקראית
targetWord = random.choice(wordList)
# 1.3 מספר הניסיונות
attempts = 5
# 1.4 יצירת מחרוזת לאחסון האותיות שניחשו (לדוגמה, "_ _ _ _ _ _" עבור "python")
guessedWord = "_" * len(targetWord)

# 2. לולאת המשחק
while attempts > 0 and guessedWord != targetWord:
    # 2.1 הדפסת המצב הנוכחי של האותיות שניחשו
    print("מילה:", guessedWord)
    # 2.2 בקשת קלט אות
    userLetter = input("הזן אות: ").lower()
    # 2.3 הקטנת מספר הניסיונות
    attempts -= 1

    # 2.4 בדיקה האם האות קיימת במילה שניחשו
    if userLetter in targetWord:
        # 2.4.1 עדכון המחרוזת עם האותיות שניחשו
        for i in range(len(targetWord)):
            if targetWord[i] == userLetter:
                guessedWord = guessedWord[:i] + userLetter + guessedWord[i+1:]

        # 2.4.2 בדיקה האם המילה נוחשה
        if guessedWord == targetWord:
            print("ברכות! ניחשת את המילה:", targetWord)
            break
    else:
        # 2.5 הודעה שאין אות כזו
        print("אין אות כזו במילה.")

# 3. בדיקת הפסד
if guessedWord != targetWord:
    print("הפסדת. המילה שניחשו הייתה:", targetWord)


"""
הסבר קוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את המודול random לבחירת מילה אקראית.

2.  **אתחול**:
    -   `wordList = ["python", "java", "kotlin", "swift", "javascript", "go", "ruby"]`: יוצר רשימה של מילים שמתוכן תיבחר המילה שיש לנחש.
    -   `targetWord = random.choice(wordList)`: בוחר מילה אקראית מהרשימה `wordList` ושומר אותה ב-`targetWord`. זו המילה שהשחקן צריך לנחש.
    -   `attempts = 5`: מגדיר את מספר הניסיונות העומדים לרשות השחקן.
    -   `guessedWord = "_" * len(targetWord)`: יוצר מחרוזת `guessedWord`, המורכבת בתחילה מתווים "_". מספר ה-"_" תואם לאורך המילה שיש לנחש. מחרוזת זו מציגה את התקדמות ניחוש המילה על ידי השחקן.

3.  **לולאת המשחק `while attempts > 0 and guessedWord != targetWord:`**:
    -   `while attempts > 0 and guessedWord != targetWord:`: הלולאה נמשכת כל עוד יש לשחקן ניסיונות (`attempts > 0`) והמילה עדיין לא נוחשה (`guessedWord != targetWord`).
    -   `print("מילה:", guessedWord)`: מדפיס את המצב הנוכחי של המילה שניחשו (לדוגמה, "_ _ t _ o _").
    -   `userLetter = input("הזן אות: ").lower()`: מבקש קלט אות מהשחקן וממיר אותה לאות קטנה.
    -   `attempts -= 1`: מקטין את מספר הניסיונות הזמינים ב-1.

4. **בדיקת האות ועדכון `guessedWord`**:
   - `if userLetter in targetWord:`: בודק האם האות שהוזנה קיימת במילה שיש לנחש.
    -  אם האות קיימת:
       -  `for i in range(len(targetWord)):`: לולאה עוברת על כל אינדקסי התווים של המילה שיש לנחש.
          - `if targetWord[i] == userLetter:`: אם האות במילה שיש לנחש תואמת לאות שהוזנה, אזי:
              - `guessedWord = guessedWord[:i] + userLetter + guessedWord[i+1:]`: מחליף את התו "_" באות שניחשו במחרוזת `guessedWord` בעמדה המתאימה.
       - `if guessedWord == targetWord:`: בודק האם המילה נוחשה במלואה.
          - `print("ברכות! ניחשת את המילה:", targetWord)`: מדפיס ברכה על ניחוש המילה.
          - `break`: מסיים את לולאת המשחק.
   -  `else:`: אם האות שהוזנה אינה קיימת במילה שיש לנחש.
       -  `print("אין אות כזו במילה.")`: מדפיס הודעה על כך שהאות שהוזנה אינה קיימת במילה.

5. **בדיקת הפסד**:
   -  `if guessedWord != targetWord:`: לאחר סיום הלולאה בודק האם המילה לא נוחשה.
       -  `print("הפסדת. המילה שניחשו הייתה:", targetWord)`: מדפיס הודעה על הפסד ומציג את המילה שיש לנחש.
"""