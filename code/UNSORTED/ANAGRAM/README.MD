# מחולל אנאגרמות באמצעות Google Gemini

זהו קוד פשוט ליצירת אנאגרמות בעזרת מודל השפה הגדול של Google Gemini.

## תיאור

התוכנית מקבלת קלט של אוסף אותיות רוסיות ומנסה למצוא מילה קיימת בשפה הרוסית המורכבת מאותיות אלה (תוך שימוש בכל האותיות או בחלק מהן).

## כללי אנאגרמות

*   משתמשים רק במילים קיימות בשפה הרוסית.
*   בחיפוש אנאגרמות מתחשבים רק באותיות רוסיות. ספרות וסימנים אחרים מתעלמים.
*   אם ניתן להרכיב כמה מילים, מוחזרת אחת מהן.
*   אם לא ניתן להרכיב אף מילה מהאותיות הנתונות, מוחזרת ההודעה "Нет анаграмм" (אין אנאגרמות).

## שימוש

1.  **מפתח API של Google Gemini.**

    מפתח API למודל כאן: [https://aistudio.google.com/](https://aistudio.google.com/)

    לחלופין, ניתן להשתמש במפתח שלי:

    AIzaSyCprZ9Tr-rB_xFau5zgWsKPM_6W-FmUntk

    יצרתי את המפתח לצורך למידה והבנת הקוד. אל תעמיסו יתר על המידה על המודל!

2.  **התקן את הספריות הנדרשות:**

    ```bash
    pip install google-generativeai
    ```

3.  **הרץ את הסקריפט:**

    ```bash
    python anagram_generator.py
    ```

4.  הסקריפט יבקש את מפתח ה-API. הזן אותו.
5.  לאחר מכן הזן את האותיות עבורן ברצונך למצוא אנאגרמה.

## הסבר על הקוד

*   `import google.generativeai as genai`: מייבא את הספרייה לממשק פעולה עם Gemini.
*   `import re`: מייבא את הספרייה לעבודה עם ביטויים רגולריים (לצורך ניקוי קלט).
*   הקלאס `GoogleGenerativeAI` מכיל בתוכו את הלוגיקה של ממשק הפעולה עם מודל Gemini.
*   `system_instruction`: זוהי הנחיה מערכתית (פרומפט) ל-Gemini, המסבירה מה נדרש ממנו.
*   `re.sub(r"[^а-яА-ЯёЁ]", "", q)`: שורה זו מסירה מהמחרוזת `q` כל תו שאינו אות רוסית. `[^а-яА-ЯёЁ]` - זהו ביטוי רגולרי שמשמעותו "כל תו *שאינו* נמצא בטווח а-я, А-Я ו-ёЁ".
*   הבדיקה `if not q:` בודקת האם המחרוזת הפכה ריקה לאחר הסרת כל התווים שאינם קיריליים.
*   `model.generate_content(q)`: שולח את הבקשה `q` למודל Gemini.
*   טיפול בחריגות `try...except` מאפשר להימנע מקריסת התוכנית במקרה של שגיאות בממשק הפעולה עם ה-API.

## דוגמה לשימוש

```
הזן את האותיות לפיהן Gemini ימצא אנאגרמה: сон
нос
הזן את האותיות לפיהן Gemini ימצא אנאגרמה: апельсин
спаниель
הזן את האותיות לפיהן Gemini ימצא אנאגרמה: 12345абвг
абвг
הזן את האותיות לפיהן Gemini ימצא אנאגרמה: 
```