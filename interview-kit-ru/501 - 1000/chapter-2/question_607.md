### question_607.md

**שאלה 607.** כיצד פועלת פעולת כפל רשימה במספר שלם בפייתון? תאר/י את תוצאת פעולה זו ואת מאפייניה.

-   A. כפל רשימה במספר שלם מוחל על כל איבר ברשימה, אם איברים אלה הם מסוגים מספריים.
-   B. כפל רשימה במספר שלם חוזר על הרשימה המקורית את מספר הפעמים שצוין, ויוצר רשימה חדשה.
-   C. כפל רשימה במספר שלם יוצר רשימה חדשה, משכפל את איברי הרשימה המקורית, תוך יצירת העתקה עמוקה של האיברים.
-   D. כפל רשימה במספר שלם מסיר את כל הכפילויות מהרשימה המקורית.

**תשובה נכונה: B**

**הסבר:**

בפייתון, פעולת כפל רשימה במספר שלם (`list * n`) מובילה ליצירת רשימה חדשה שבה איברי הרשימה המקורית חוזרים על עצמם `n` פעמים. חשוב להבין שפעולה זו אינה משנה את הרשימה המקורית, אלא יוצרת רשימה חדשה. כמו כן, יש לציין שמדובר בהעתקה שטחית (shallow copy), ואם הרשימה מכילה סוגי נתונים משתנים מקוננים, הם לא ישוכפלו (לא תיווצר להם העתקה עמוקה).

*   **מאפיינים עיקריים של כפל רשימה:**
    *   **חזרה על איברים:** יוצר רשימה חדשה על ידי חזרה על הרשימה המקורית את מספר הפעמים שצוין.
    *   **כופל שלם:** האופרנד הימני (הכופל) חייב להיות מספר שלם.
    *   **אובייקט חדש:** הפעולה תמיד מחזירה רשימה חדשה, ואינה משנה את הרשימה המקורית.
    *   **סדר האיברים:** ברשימה החדשה, האיברים שומרים על סדרם המקורי.
    *   **העתקה שטחית:** מיושמת העתקה שטחית של איברי הרשימה, כלומר במקרה של איברים משתנים מקוננים, הם אינם מועתקים, אלא מועברים על ידי הפניה (reference).

*   **שגיאות בכפל רשימה:**
    *   כפל רשימה במספר שאינו שלם יגרום לשגיאת `TypeError`.
    *   כפל רשימה במחרוזת אחרת או ברשימה אחרת גם יגרום לשגיאת `TypeError`.

**דוגמאות:**

```python
# דוגמה 1: כפל רשימה במספר שלם חיובי
my_list = [1, 2, 3]
repeated_list = my_list * 3
print(f"רשימה מקורית: {my_list}")
print(f"תוצאת הכפל: {repeated_list}") # פלט: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# דוגמה 2: כפל רשימה באפס
my_list2 = [1,2,3]
empty_list = my_list2 * 0
print(f"רשימה מקורית: {my_list2}")
print(f"תוצאת הכפל: {empty_list}") # פלט: []

# דוגמה 3: כפל רשימה עם רשימות מקוננות (העתקה שטחית)
nested_list = [[1,2], [3,4]]
repeated_nested_list = nested_list * 2
print(f"רשימה מקורית (מקוננת): {nested_list}")
print(f"תוצאת הכפל (רשימה מקוננת): {repeated_nested_list}") # [[1, 2], [3, 4], [1, 2], [3, 4]]

nested_list[0].append(10) # משנים את האיבר הראשון ברשימה, ושינוי זה ישתקף גם ב-repeated_nested_list
print(f"רשימה מקורית שהשתנתה (מקוננת): {nested_list}") # פלט: [[1, 2, 10], [3, 4]]
print(f"תוצאת הכפל (רשימה מקוננת) לאחר השינוי: {repeated_nested_list}") # פלט: [[1, 2, 10], [3, 4], [1, 2, 10], [3, 4]]

# דוגמה 4: קומוטטיביות
my_list3 = [1,2]
print(my_list3 * 3 == 3 * my_list3) # פלט: True

try:
  print([1,2,3] * 3.14) # תגרום לשגיאה
except TypeError as e:
    print(e) # can't multiply sequence by non-int of type 'float'

try:
  print([1,2,3] * "test") # תגרום לשגיאה
except TypeError as e:
    print(e) # can't multiply sequence by non-int of type 'str'
```

**ניתוח האפשרויות:**
*   **A. כפל רשימה במספר שלם מוחל על כל איבר ברשימה, אם איברים אלה הם מסוגים מספריים.:** לא נכון.
*   **B. כפל רשימה במספר שלם חוזר על הרשימה המקורית את מספר הפעמים שצוין, ויוצר רשימה חדשה.:** נכון.
*   **C. כפל רשימה במספר שלם יוצר רשימה חדשה, משכפל את איברי הרשימה המקורית, תוך יצירת העתקה עמוקה של האיברים.:** לא נכון.
*   **D. כפל רשימה במספר שלם אינו נתמך ויגרום לשגיאת `TypeError`. :** לא נכון.

**לסיכום:**
*   פעולת כפל רשימה במספר שלם יוצרת רשימה חדשה על ידי חזרה על הרשימה המקורית.
*   פעולת כפל רשימה במספר שלם יוצרת העתקה שטחית, שבה איברי רשימות מקוננות אינם מועתקים בהעתקה עמוקה.
*   כפל רשימה במספר שאינו שלם או ברשימה אחרת יגרום לשגיאת `TypeError`.

לפיכך, התשובה הנכונה היא **B. כפל רשימה במספר שלם חוזר על הרשימה המקורית את מספר הפעמים שצוין, ויוצר רשימה חדשה.**