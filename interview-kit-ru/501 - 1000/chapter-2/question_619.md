### `question_619.md`

**שאלה 619.** היכן ב-Python חיפוש איבר מתבצע מהר יותר – ברשימות או במילונים, ומדוע?

-   א. חיפוש איברים ברשימות מהיר יותר מאשר במילונים, מכיוון שרשימות מאחסנות איברים במבנה סדור.
-   ב. חיפוש איברים במילונים מהיר יותר מאשר ברשימות, מכיוון שמילונים משתמשים בטבלאות גיבוב (hash tables) המספקות גישה לאיברים בממוצע בסיבוכיות זמן O(1), לעומת רשימה שבה החיפוש מתבצע בסיבוכיות זמן O(n).
-   ג. מהירות החיפוש במילונים וברשימות זהה, מכיוון שאלו טיפוסי נתונים מובנים.
-   ד. עבור כמות קטנה של איברים החיפוש מהיר יותר ברשימות, ועבור כמות גדולה - במילונים.

**תשובה נכונה: ב**

**הסבר:**

ב-Python, מהירות חיפוש איברים ברשימות ובמילונים שונה באופן מהותי בשל מבנה הנתונים הפנימי שלהם.

*   **רשימות (`list`):**
    *   **אחסון סדרתי:** איברים ברשימה מאוחסנים באופן סדרתי בזיכרון.
    *   **חיפוש ליניארי:** חיפוש איבר ברשימה מתבצע על ידי מעבר סדרתי, כלומר, מהאיבר הראשון ועד לאיבר המבוקש, ולוקח בממוצע סיבוכיות זמן O(n), כאשר n הוא מספר האיברים ברשימה.
    *   **תלות בגודל:** זמן החיפוש גדל ליניארית עם גידול גודל הרשימה.

*   **מילונים (`dict`):**
    *   **טבלאות גיבוב:** מילונים משתמשים בטבלאות גיבוב (hash tables) לאחסון זוגות של מפתח-ערך.
    *   **חיפוש מהיר:** חיפוש לפי מפתח במילון לוקח בממוצע סיבוכיות זמן O(1) (זמן קבוע), כלומר זמן החיפוש כמעט אינו תלוי בגודל המילון.
    *   **מפתחות:** המפתחות חייבים להיות אובייקטים ברי-גיבוב (hashable) (בלתי ניתנים לשינוי, למשל, מחרוזות, מספרים, tuples).

**הבדלים:**
*   **זמן חיפוש:** חיפוש במילון לוקח O(1) בממוצע, ברשימות O(n).
*   **מהירות:** מילונים מהירים יותר בדרך כלל עבור חיפוש, במיוחד עם קבוצת נתונים גדולה.
*   **תלות בגודל:** זמן החיפוש במילון אינו תלוי בגודלו, ואילו ברשימה זמן החיפוש גדל עם גידול הגודל.
*   **דרישות למפתחות:** מילונים דורשים מפתחות ייחודיים וברי-גיבוב, ואילו איברי רשימה אינם חייבים להיות ייחודיים ואין להם מגבלות כלשהן על סוגים.

**דוגמאות:**
```python
import time
# דוגמה 1: חיפוש ברשימות

my_list = list(range(100000))

start_time = time.time()
found = 99999 in my_list
end_time = time.time()
print(f"זמן חיפוש ברשימה: {end_time - start_time} שניות")


# דוגמה 2: חיפוש במילון

my_dict = {i: str(i) for i in range(100000)} # יוצרים מילון
start_time = time.time()
found = 99999 in my_dict
end_time = time.time()
print(f"זמן חיפוש במילון: {end_time - start_time} שניות")

# דוגמה 3: קבלת ערך במילון לפי מפתח

start_time = time.time()
found = my_dict[99999]
end_time = time.time()
print(f"זמן קבלת ערך במילון: {end_time - start_time} שניות")
```

**בתוצאה:**
*   חיפוש במילונים (לפי מפתח) מהיר יותר מחיפוש ברשימות בזכות השימוש בטבלאות גיבוב.
*   זמן החיפוש במילונים כמעט ואינו תלוי בגודל, ואילו ברשימות זמן החיפוש תלוי ליניארית בגודלן.

**ניתוח האפשרויות:**
*   **א. חיפוש איברים ברשימות מהיר יותר מאשר במילונים, מכיוון שרשימות מאחסנות איברים במבנה סדור.:** לא נכון.
*   **ב. חיפוש איברים במילונים מהיר יותר מאשר ברשימות, מכיוון שמילונים משתמשים בטבלאות גיבוב (hash tables) המספקות גישה לאיברים בממוצע בסיבוכיות זמן O(1), לעומת רשימה שבה החיפוש מתבצע בסיבוכיות זמן O(n).:** נכון.
*   **ג. מהירות החיפוש במילונים וברשימות זהה, מכיוון שאלו טיפוסי נתונים מובנים.:** לא נכון.
*   **ד. עבור כמות קטנה של איברים החיפוש מהיר יותר ברשימות, ועבור כמות גדולה - במילונים.:** לא נכון (בעוד שבפועל הבדל זה עשוי להיות פחות מורגש עבור קבוצות נתונים קטנות מאוד בשל תקורה, הכלל הבסיסי של סיבוכיות זמן נשאר בתוקף, וההצהרה אינה מדויקת ביסוד).

לפיכך, התשובה הנכונה היא **ב. חיפוש איברים במילונים מהיר יותר מאשר ברשימות, מכיוון שמילונים משתמשים בטבלאות גיבוב (hash tables) המספקות גישה לאיברים בממוצע בסיבוכיות זמן O(1), לעומת רשימה שבה החיפוש מתבצע בסיבוכיות זמן O(n).**