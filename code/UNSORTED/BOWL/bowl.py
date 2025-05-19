"""
<BOWL>:
=================
דרגת קושי: 5
-----------------
המשחק "באולינג" הוא סימולציה טקסטואלית של משחק באולינג, בו השחקן מטיל כדור והמחשב קובע את מספר הפינים שהופלו.
המשחק מורכב מ-10 סבבים. בכל סבב, לשחקן יש שתי הטלות, אלא אם כן הוא משיג סטרייק (מפיל את כל הפינים) בהטלה הראשונה. תוצאת כל סבב מצטברת, ויוצרת את הניקוד הכולל.

כללי המשחק:
1. בתחילת כל סבב, לשחקן יש 10 פינים.
2. השחקן מטיל את הכדור (מופק מספר אקראי בין 0 ל-10).
3. מספר הפינים שהופלו מנוכה מסך הפינים הכולל.
4. אם השחקן הפיל את כל 10 הפינים בהטלה הראשונה (סטרייק), הסבב מסתיים והתור עובר לסבב הבא.
5. אם השחקן לא השיג סטרייק, הוא מבצע הטלה שנייה.
6. תוצאות כל סבב מסוכמות לניקוד הכולל.
7. המשחק מורכב מ-10 סבבים.
8. בסיום המשחק, מוצג הניקוד הכולל של השחקן.
-----------------
אלגוריתם:
1. הגדרת הניקוד הכולל (totalScore) ל-0.
2. התחלת לולאה מ-1 עד 10 (עבור 10 סבבים):
    2.1 הגדרת כמות הפינים (pins) ל-10.
    2.2 הצגת מספר הסבב הנוכחי.
    2.3 יצירת מספר אקראי בין 0 למספר הפינים הנותרים (pins) (הטלה ראשונה).
    2.4 הצגת הודעה על מספר הפינים שהופלו (firstThrow).
    2.5 חיסור מספר הפינים שהופלו (firstThrow) מכמות הפינים הכוללת (pins).
    2.6 אם מספר הפינים שהופלו שווה ל-10 (סטרייק), עבור לשלב 2.10.
    2.7 יצירת מספר אקראי בין 0 למספר הפינים הנותרים (pins) (הטלה שנייה).
    2.8 הצגת הודעה על מספר הפינים שהופלו (secondThrow).
    2.9 חיסור מספר הפינים שהופלו (secondThrow) מכמות הפינים הכוללת (pins).
    2.10 הוספת סכום הפינים שהופלו (firstThrow + secondThrow) לניקוד הכולל (totalScore).
3. הצגת הניקוד הכולל (totalScore).
4. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeScore["Инициализация: totalScore = 0"]
    InitializeScore --> RoundLoopStart{"Начало цикла: для 10 раундов"}
    RoundLoopStart -- Да --> ResetPins["pins = 10"]
    ResetPins --> DisplayRound["Вывод: 'Раунд' + roundNumber"]
    DisplayRound --> FirstThrow["firstThrow = random(0, pins)"]
    FirstThrow --> OutputFirstThrow["Вывод: 'Первый бросок:' + firstThrow"]
    OutputFirstThrow --> UpdatePins1["pins = pins - firstThrow"]
    UpdatePins1 --> CheckStrike{"Проверка: firstThrow == 10?"}
    CheckStrike -- Да --> UpdateTotalScoreStrike["totalScore = totalScore + firstThrow"]
    UpdateTotalScoreStrike --> RoundLoopEnd["Конец раунда"]
    CheckStrike -- Нет --> SecondThrow["secondThrow = random(0, pins)"]
    SecondThrow --> OutputSecondThrow["Вывод: 'Второй бросок:' + secondThrow"]
    OutputSecondThrow --> UpdatePins2["pins = pins - secondThrow"]
    UpdatePins2 --> UpdateTotalScore["totalScore = totalScore + firstThrow + secondThrow"]
    UpdateTotalScore --> RoundLoopEnd
    RoundLoopStart -- Нет --> OutputTotalScore["Вывод: 'Общий счет:' + totalScore"]
    OutputTotalScore --> End["Конец"]
    RoundLoopEnd --> RoundLoopStart
```
    
**מקרא:**
    Start - התחלת התוכנית.
    InitializeScore - אתחול המשתנה totalScore (ניקוד כולל) בערך 0.
    RoundLoopStart - תחילת הלולאה, המבוצעת 10 פעמים (עבור כל סבב).
    ResetPins - הגדרת כמות הפינים pins ל-10.
    DisplayRound - הצגת מספר הסבב הנוכחי.
    FirstThrow - יצירת מספר אקראי בין 0 לכמות הפינים הנוכחית, המייצג את ההטלה הראשונה.
    OutputFirstThrow - הצגת כמות הפינים שהופלו בהטלה הראשונה.
    UpdatePins1 - עדכון כמות הפינים הנותרים לאחר ההטלה הראשונה.
    CheckStrike - בדיקה האם ההטלה הראשונה הייתה סטרייק (הופלו כל 10 הפינים).
    UpdateTotalScoreStrike - עדכון הניקוד הכולל totalScore, אם היה סטרייק.
    RoundLoopEnd - סיום הסבב הנוכחי.
    SecondThrow - יצירת מספר אקראי בין 0 לכמות הפינים הנוכחית, המייצג את ההטלה השנייה.
    OutputSecondThrow - הצגת כמות הפינים שהופלו בהטלה השנייה.
    UpdatePins2 - עדכון כמות הפינים הנותרים לאחר ההטלה השנייה.
    UpdateTotalScore - עדכון הניקוד הכולל totalScore בסכום הפינים שהופלו בשתי ההטלות.
    OutputTotalScore - הצגת הניקוד הכולל לאחר השלמת כל הסבבים.
    End - סיום התוכנית.
"""
import random

# אתחול הניקוד הכולל
totalScore = 0

# לולאה עבור 10 סבבי משחק
for roundNumber in range(1, 11):
    # בתחילת כל סבב יש 10 פינים
    pins = 10
    print(f"סבב {roundNumber}")

    # הטלה ראשונה
    firstThrow = random.randint(0, pins)
    print(f"הטלה ראשונה: {firstThrow}")
    pins -= firstThrow

    # בדיקה לסטרייק
    if firstThrow == 10:
        totalScore += firstThrow
        print("סטרייק!")
        continue # מעבר לסבב הבא
    
    # הטלה שנייה (אם לא היה סטרייק)
    secondThrow = random.randint(0, pins)
    print(f"הטלה שנייה: {secondThrow}")
    pins -= secondThrow

    # עדכון הניקוד הכולל
    totalScore += firstThrow + secondThrow

# הצגת הניקוד הכולל
print(f"ניקוד כולל: {totalScore}")

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
   -  `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים לצורך הדמיית הטלות.
2.  **אתחול הניקוד הכולל**:
   -  `totalScore = 0`: מאתחל את המשתנה `totalScore` לאחסון כמות הנקודות הכוללת, ערך התחלתי 0.
3.  **לולאה על הסבבים**:
   -  `for roundNumber in range(1, 11):`:  לולאה, העוברת 10 פעמים (עבור כל סבב משחק).
   - `pins = 10`: בתחילת כל סבב כמות הפינים מוגדרת ל-10.
   -  `print(f"סבב {roundNumber}")`: מציג את מספר הסבב הנוכחי.
4. **הטלה ראשונה**:
    -  `firstThrow = random.randint(0, pins)`: מופק מספר אקראי בין 0 לכמות הפינים הנותרים (pins) לצורך הדמיית ההטלה הראשונה.
    - `print(f"הטלה ראשונה: {firstThrow}")`: מציג את כמות הפינים שהופלו בהטלה הראשונה.
    - `pins -= firstThrow`:  כמות הפינים שהופלו מנוכה מכמות הפינים הכוללת.
5.  **בדיקה לסטרייק**:
    -  `if firstThrow == 10:`: בודק האם ההטלה הראשונה הייתה סטרייק (הופלו כל 10 הפינים).
    -  `totalScore += firstThrow`: אם היה סטרייק, מוסיף 10 נקודות לניקוד הכולל.
    -  `print("סטרייק!")`:  מציג הודעה על סטרייק.
    - `continue`:  עובר לאיטרציה הבאה של הלולאה (לסבב הבא), מבלי לבצע את יתר הקוד בסבב הנוכחי.
6.  **הטלה שנייה (אם לא היה סטרייק)**:
    -  `secondThrow = random.randint(0, pins)`: מופק מספר אקראי בין 0 לכמות הפינים הנותרים לצורך הדמיית ההטלה השנייה.
    - `print(f"הטלה שנייה: {secondThrow}")`: מציג את כמות הפינים שהופלו בהטלה השנייה.
    -  `pins -= secondThrow`: כמות הפינים שהופלו מנוכה מכמות הפינים הכוללת.
7.  **עדכון הניקוד הכולל**:
    -  `totalScore += firstThrow + secondThrow`: לניקוד הכולל מתווסף סכום הנקודות משתי ההטלות.
8.  **הצגת הניקוד הכולל**:
    -  `print(f"ניקוד כולל: {totalScore}")`: מציג את הניקוד הכולל הסופי לאחר כל 10 הסבבים.
"""