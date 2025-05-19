AMAZIN:
=================
רמת קושי: 5
-----------------
המשחק "AMAZIN" הוא משחק ניחוש מילים. המחשב בוחר מילה אקראית מרשימה מוגדרת מראש, והשחקן נדרש לנחש אותה על ידי הזנת אותיות. לאחר כל ניסיון, המחשב מדווח האם האות שהוזנה נמצאת במילה ובאיזו עמדה. על השחקן לנחש את המילה לפני שינצל את כל ניסיונותיו.

חוקי המשחק:
1. המחשב בוחר מילה אקראית מרשימה.
2. השחקן מקבל מספר מוגדר של ניסיונות (ברירת מחדל: 5).
3. השחקן מזין אות.
4. המחשב מדווח האם האות קיימת במילה, ואם כן, באילו עמדות.
5. השחקן מנסה לנחש את המילה לפי אותיות.
6. אם השחקן מנחש את המילה, המשחק מסתיים בניצחון.
7. אם השחקן מנצל את כל הניסיונות, המשחק מסתיים בהפסד.
-----------------
אלגוריתם:
1. אתחול:
    1.1. הגדרת רשימת מילים.
    1.2. בחירת מילה אקראית מהרשימה.
    1.3. הגדרת מספר הניסיונות (ברירת מחדל: 5).
    1.4. יצירת מחרוזת להצגת האותיות שנוחשו (בתחילה כל העמדות הן "_").
2. התחלת לולאה "כל עוד מספר הניסיונות גדול מ-0 והמילה לא נוחשה":
    2.1. הדפסת המחרוזת עם האותיות שנוחשו.
    2.2. בקשת קלט אות מהשחקן.
    2.3. הקטנת מספר הניסיונות ב-1.
    2.4. אם האות שהוזנה קיימת במילה הסודית:
        2.4.1. החלפת "_" באות בעמדות המתאימות במחרוזת של האותיות שנוחשו.
        2.4.2. אם מחרוזת האותיות שנוחשו זהה למילה הסודית, הדפסת הודעת ניצחון ויציאה מהלולאה.
    2.5. אם האות שהוזנה אינה קיימת במילה הסודית, הדפסת הודעה על כך שאות זו אינה קיימת.
3. אם לאחר הלולאה המילה לא נוחשה (נותרו ניסיונות והמילה לא נוחשה), הדפסת הודעת הפסד והמילה הסודית.
4. סוף המשחק.
-----------------
דיאגרמת זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация:<br>
    <code><b>wordList = [...]<br>
    targetWord = random(wordList)<br>
    attempts = 5<br>
    guessedWord = '___...'</b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла:<br><code><b>attempts > 0 и not wordGuessed</b></code>"}
    LoopStart -- Да --> OutputGuessedWord["Вывод: <code><b>guessedWord</b></code>"]
    OutputGuessedWord --> InputLetter["Ввод буквы: <code><b>userLetter</b></code>"]
    InputLetter --> DecreaseAttempts["<code><b>attempts = attempts - 1</b></code>"]
    DecreaseAttempts --> CheckLetter{"Проверка: <code><b>userLetter in targetWord</b></code>?"}
    CheckLetter -- Да --> UpdateGuessedWord["Обновить <code><b>guessedWord</b></code>"]
    UpdateGuessedWord --> CheckWin{"Проверка: <code><b>guessedWord == targetWord</b></code>?"}
     CheckWin -- Да --> OutputWin["Вывод: <b>WIN</b>"]
     OutputWin --> End["Конец"]
    CheckWin -- Нет --> LoopStart
    CheckLetter -- Нет --> OutputNoLetter["Вывод: <b>NO LETTER</b>"]
    OutputNoLetter --> LoopStart
    LoopStart -- Нет --> CheckLose{"Проверка: <code><b>attempts <=0 and not wordGuessed</b></code>"}
    CheckLose -- Да --> OutputLose["Вывод: <b>LOSE, targetWord</b>"]
    OutputLose --> End
     CheckLose -- Нет --> End

```
מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: wordList (רשימת מילים), targetWord (המילה הסודית נבחרת באקראי), attempts (מספר הניסיונות) נקבע ל-5, guessedWord (מחרוזת עם האותיות שנוחשו) מאותחלת בסימני '_' .
    LoopStart - תחילת הלולאה, שנמשכת כל עוד יש ניסיונות והמילה לא נוחשה.
    OutputGuessedWord - הדפסת המצב הנוכחי של האותיות שנוחשו.
    InputLetter - בקשת קלט אות מהמשתמש.
    DecreaseAttempts - הקטנת מספר הניסיונות הנותרים.
    CheckLetter - בדיקה האם האות שהוזנה קיימת במילה הסודית.
    UpdateGuessedWord - עדכון המחרוזת של האותיות שנוחשו.
    CheckWin - בדיקה האם המילה נוחשה.
    OutputWin - הדפסת הודעת ניצחון.
    OutputNoLetter - הדפסת הודעה על כך שהאות שהוזנה אינה במילה.
    CheckLose - בדיקה האם נגמרו הניסיונות והמילה לא נוחשה.
    OutputLose - הדפסת הודעת הפסד והמילה הסודית.
    End - סוף התוכנית.
```python
import random

# 1. אתחול
# 1.1 רשימת מילים למשחק
wordList = ["python", "java", "kotlin", "swift", "javascript", "go", "ruby"]
# 1.2 בחירת מילה אקראית
targetWord = random.choice(wordList)
# 1.3 מספר ניסיונות
attempts = 5
# 1.4 יצירת מחרוזת לשמירת אותיות שנוחשו (לדוגמה, '______' עבור 'python')
guessedWord = "_" * len(targetWord)

# 2. לולאת המשחק
while attempts > 0 and guessedWord != targetWord:
    # 2.1 הדפסת המצב הנוכחי של האותיות שנוחשו
    print("מילה:", guessedWord)
    # 2.2 בקשת קלט אות מהשחקן
    userLetter = input("הכנס אות: ").lower()
    # 2.3 הקטנת מספר הניסיונות
    attempts -= 1

    # 2.4 בדיקה האם האות נמצאת במילה הסודית
    if userLetter in targetWord:
        # 2.4.1 עדכון המחרוזת עם האותיות שנוחשו
        for i in range(len(targetWord)):
            if targetWord[i] == userLetter:
                guessedWord = guessedWord[:i] + userLetter + guessedWord[i+1:]

        # 2.4.2 בדיקה האם המילה נוחשה
        if guessedWord == targetWord:
            print("מזל טוב! ניחשת את המילה:", targetWord)
            break
    else:
        # 2.5 הודעה על כך שהאות אינה נמצאת במילה
        print("האות הזו אינה במילה.")

# 3. בדיקת הפסד
if guessedWord != targetWord:
    print("הפסדת. המילה הסודית הייתה:", targetWord)


"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את מודול random לבחירת מילה אקראית.

2.  **אתחול**:
    -   `wordList = ["python", "java", "kotlin", "swift", "javascript", "go", "ruby"]`: יוצר רשימת מילים, שממנה תיבחר המילה הסודית.
    -   `targetWord = random.choice(wordList)`: בוחר מילה אקראית מרשימת `wordList` ושומר אותה במשתנה `targetWord`. זו המילה שהשחקן צריך לנחש.
    -   `attempts = 5`: מגדיר את מספר הניסיונות העומדים לרשות השחקן.
    -   `guessedWord = "_" * len(targetWord)`: יוצר מחרוזת בשם `guessedWord`, שמורכבת בתחילה מסימני "_". מספר הסימנים שווה לאורך המילה הסודית. מחרוזת זו מציגה את התקדמות השחקן בניחוש המילה.

3.  **לולאת המשחק `while attempts > 0 and guessedWord != targetWord:`**:
    -   `while attempts > 0 and guessedWord != targetWord:`: הלולאה נמשכת כל עוד לשחקן יש ניסיונות (`attempts > 0`) והמילה טרם נוחשה (`guessedWord != targetWord`).
    -   `print("מילה:", guessedWord)`: מדפיס את המצב הנוכחי של המילה המנוחשת (לדוגמה, "_ _ t _ o _").
    -   `userLetter = input("הכנס אות: ").lower()`: מבקש מהשחקן להזין אות וממיר אותה לאות קטנה.
    -   `attempts -= 1`: מקטין את מספר הניסיונות הזמינים ב-1.

4. **בדיקת אות ועדכון `guessedWord`**:
   - `if userLetter in targetWord:`: בודק האם האות שהוזנה קיימת במילה הסודית.
    -  אם האות קיימת:
       -  `for i in range(len(targetWord)):`: לולאה העוברת על כל האינדקסים של תווים במילה הסודית.
          - `if targetWord[i] == userLetter:`: אם האות במילה הסודית זהה לאות שהוזנה, אז:
              - `guessedWord = guessedWord[:i] + userLetter + guessedWord[i+1:]`: מחליף את סימן "_" באות שנוחשה במחרוזת `guessedWord` בעמדה המתאימה.
       - `if guessedWord == targetWord:`: בודק האם המילה נוחשה בשלמותה.
          - `print("מזל טוב! ניחשת את המילה:", targetWord)`: מדפיס הודעת ברכה על ניחוש המילה.
          - `break`: מסיים את לולאת המשחק.
   -  `else:`: אם האות שהוזנה אינה קיימת במילה הסודית.
       -  `print("האות הזו אינה במילה.")`: מדפיס הודעה על כך שהאות שהוזנה אינה במילה.

5. **בדיקת הפסד**:
   -  `if guessedWord != targetWord:`: לאחר סיום הלולאה, בודק האם המילה לא נוחשה.
       -  `print("הפסדת. המילה הסודית הייתה:", targetWord)`: מדפיס הודעת הפסד ומציג את המילה הסודית.
"""