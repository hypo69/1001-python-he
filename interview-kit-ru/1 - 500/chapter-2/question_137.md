### `question_137.md`

**שאלה 37.** כיצד נעשה שימוש באופרטורי התנאי המקוננים `if`?

A. עבור ביצוע מספר בלוקים שונים של קוד בו זמנית.
B. לציון תנאי שחייב להיות נכון, בטרם ייבדק תנאי אחר.
C. לאופטימיזציית ביצועי הקוד באמצעות הפחתת מספר בדיקות התנאים.
D. ללכידת חריגות (exceptions) שעשויות להתרחש בקוד.

**תשובה נכונה: B**

**הסבר:**

אופרטורי התנאי המקוננים `if` משמשים ליצירת לוגיקה מורכבת יותר, כאשר ביצוע פעולות מסוימות תלוי במספר תנאים. אופרטור ה-`if` החיצוני בודק את התנאי הראשון, ואם הוא מתקיים, מתרחש מעבר לאופרטור ה-`if` הפנימי, הבוחן את התנאי השני, וכך הלאה.

*   **אפשרות A** שגויה: `if` מבצע רק בלוק אחד בכל פעם.
*   **אפשרות B** נכונה: `if` מקוננים נחוצים כדי לבדוק תנאי רק אם התקיים התנאי הקודם.
*   **אפשרות C** שגויה: `if` מקוננים עשויים להפחית את הביצועים, כיוון שהם מוסיפים בדיקות חדשות.
*   **אפשרות D** שגויה: `try-except` משמשים ללכידת חריגות (exceptions).

**דוגמה:**

```python
x: int = 10
y: int = 5

if x > 0:
    print("x הוא מספר חיובי")
    if y > 0:
        print("y הוא מספר חיובי")
        if x > y:
            print("x גדול מ-y")
        else:
            print("x אינו גדול מ-y")
    else:
        print("y אינו מספר חיובי")
else:
  print("x אינו מספר חיובי")
```

**תוצאה:**
ב קוד שלעיל, אופרטורי ה-`if` הפנימיים מבוצעים רק אם מתקיים התנאי הראשון `if x > 0`.

לפיכך, **אפשרות B** הינה נכונה.