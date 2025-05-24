<BOWL>:
=================
רמת קושי: 5
-----------------
המשחק "באולינג" הוא סימולציית טקסט של משחק באולינג, שבו השחקן זורק כדור, והמחשב קובע את מספר הפינים שהופלו.
המשחק מורכב מ-10 סיבובים. בכל סיבוב, לשחקן יש שתי זריקות, אלא אם כן הוא מפיל סטרייק (מפיל את כל הפינים) בזריקה הראשונה. תוצאת כל סיבוב מצטברת ויוצרת את הניקוד הכולל.

כללי המשחק:
1. בתחילת כל סיבוב, לשחקן יש 10 פינים.
2. השחקן זורק כדור (מוזן מספר אקראי בין 0 ל-10).
3. מספר הפינים שהופלו מחוסר ממספר הפינים הכולל.
4. אם השחקן הפיל את כל 10 הפינים בזריקה הראשונה (סטרייק), הסיבוב מסתיים, והתור עובר לסיבוב הבא.
5. אם השחקן לא עשה סטרייק, הוא מבצע זריקה שנייה.
6. תוצאות כל סיבוב מסוכמות לניקוד כולל.
7. המשחק מורכב מ-10 סיבובים.
8. בסיום המשחק, מוצג הניקוד הכולל של השחקן.
-----------------
אלגוריתם:
1. הגדרת הניקוד הכולל (totalScore) ל-0.
2. התחלת לולאה מ-1 עד 10 (עבור 10 סיבובים):
    2.1 הגדרת כמות הפינים (pins) ל-10.
    2.2 הדפסת מספר הסיבוב הנוכחי.
    2.3 יצירת מספר אקראי מ-0 עד מספר הפינים שנותרו (pins) (זריקה ראשונה).
    2.4 הדפסת הודעה על מספר הפינים שהופלו (firstThrow).
    2.5 חיסור מספר הפינים שהופלו (firstThrow) מכמות הפינים הכוללת (pins).
    2.6 אם מספר הפינים שהופלו שווה ל-10 (סטרייק), מעבר לשלב 2.10.
    2.7 יצירת מספר אקראי מ-0 עד מספר הפינים שנותרו (pins) (זריקה שנייה).
    2.8 הדפסת הודעה על מספר הפינים שהופלו (secondThrow).
    2.9 חיסור מספר הפינים שהופלו (secondThrow) מכמות הפינים (pins).
    2.10 הוספת סכום הפינים שהופלו (firstThrow + secondThrow) לניקוד הכולל (totalScore).
3. הדפסת הניקוד הכולל (totalScore).
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
    Start - תחילת התוכנית.
    InitializeScore - אתחול המשתנה totalScore (ניקוד כולל) בערך 0.
    RoundLoopStart - תחילת הלולאה המבצעת 10 חזרות (עבור כל סיבוב).
    ResetPins - קביעת כמות הפינים pins ל-10.
    DisplayRound - הדפסת מספר הסיבוב הנוכחי.
    FirstThrow - יצירת מספר אקראי בין 0 לכמות הפינים הנוכחית, המייצג את הזריקה הראשונה.
    OutputFirstThrow - הדפסת מספר הפינים שהופלו בזריקה הראשונה.
    UpdatePins1 - עדכון מספר הפינים שנותרו לאחר הזריקה הראשונה.
    CheckStrike - בדיקה האם הזריקה הראשונה הייתה סטרייק (הופלו כל 10 הפינים).
    UpdateTotalScoreStrike - עדכון הניקוד הכולל totalScore, אם היה סטרייק.
    RoundLoopEnd - סיום הסיבוב הנוכחי.
    SecondThrow - יצירת מספר אקראי בין 0 לכמות הפינים הנוכחית, המייצג את הזריקה השנייה.
    OutputSecondThrow - הדפסת מספר הפינים שהופלו בזריקה השנייה.
    UpdatePins2 - עדכון מספר הפינים שנותרו לאחר הזריקה השנייה.
    UpdateTotalScore - עדכון הניקוד הכולל totalScore בסכום הפינים שהופלו בשתי הזריקות.
    OutputTotalScore - הדפסת הניקוד הכולל לאחר השלמת כל הסיבובים.
    End - סיום התוכנית.
```python
import random

# אתחול הניקוד הכולל
totalScore = 0

# לולאה עבור 10 סיבובי משחק
for roundNumber in range(1, 11):
    # בתחילת כל סיבוב יש לנו 10 פינים
    pins = 10
    print(f"סיבוב {roundNumber}")

    # זריקה ראשונה
    firstThrow = random.randint(0, pins)
    print(f"זריקה ראשונה: {firstThrow}")
    pins -= firstThrow

    # בדיקה עבור סטרייק
    if firstThrow == 10:
        totalScore += firstThrow
        print("סטרייק!")
        continue # מעבר לסיבוב הבא
    
    # זריקה שנייה (אם לא היה סטרייק)
    secondThrow = random.randint(0, pins)
    print(f"זריקה שנייה: {secondThrow}")
    pins -= secondThrow

    # עדכון הניקוד הכולל
    totalScore += firstThrow + secondThrow

# הדפסת הניקוד הכולל
print(f"ניקוד כולל: {totalScore}")

```
"""
הסבר קוד:
1. **ייבוא מודול `random`**:
   - `import random`: מייבא את מודול `random`, המשמש ליצירת מספרים אקראיים עבור הדמיית הזריקות.
2. **אתחול הניקוד הכולל**:
   - `totalScore = 0`: מאתחל את המשתנה `totalScore` לאחסון כמות הנקודות הכוללת, עם ערך התחלתי 0.
3. **לולאה לפי סיבובים**:
   - `for roundNumber in range(1, 11):`: לולאה שעוברת 10 פעמים (עבור כל סיבוב משחק).
   - `pins = 10`: בתחילת כל סיבוב, כמות הפינים נקבעת ל-10.
   - `print(f"סיבוב {roundNumber}")`: מדפיס את מספר הסיבוב הנוכחי.
4. **זריקה ראשונה**:
    - `firstThrow = random.randint(0, pins)`: נוצר מספר אקראי מ-0 עד כמות הפינים שנותרו (pins) עבור הדמיית הזריקה הראשונה.
    - `print(f"זריקה ראשונה: {firstThrow}")`: מדפיס את מספר הפינים שהופלו בזריקה הראשונה.
    - `pins -= firstThrow`: כמות הפינים שהופלו מחוסרת מכמות הפינים הכוללת.
5. **בדיקה עבור סטרייק**:
    - `if firstThrow == 10:`: בודק האם הזריקה הראשונה הייתה סטרייק (הופלו כל 10 הפינים).
    - `totalScore += firstThrow`: אם היה סטרייק, מוסיף 10 נקודות לניקוד הכולל.
    - `print("סטרייק!")`: מדפיס הודעה על סטרייק.
    - `continue`: עובר לאיטרציה הבאה של הלולאה (לסיבוב הבא), מבלי לבצע את יתרת הקוד בסיבוב הנוכחי.
6. **זריקה שנייה (אם לא היה סטרייק)**:
    - `secondThrow = random.randint(0, pins)`: נוצר מספר אקראי מ-0 עד כמות הפינים שנותרו עבור הדמיית הזריקה השנייה.
    - `print(f"זריקה שנייה: {secondThrow}")`: מדפיס את מספר הפינים שהופלו בזריקה השנייה.
    - `pins -= secondThrow`: כמות הפינים שהופלו מחוסרת מכמות הפינים.
7. **עדכון הניקוד הכולל**:
    - `totalScore += firstThrow + secondThrow`: לניקוד הכולל מתווסף סכום הנקודות עבור הזריקות הראשונה והשנייה.
8. **הדפסת הניקוד הכולל**:
    - `print(f"ניקוד כולל: {totalScore}")`: מדפיס את הניקוד הכולל הסופי לאחר כל 10 הסיבובים.
"""