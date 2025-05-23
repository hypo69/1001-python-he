### `question_66.md`

**שאלה 66.** איזה טיפוס נתונים יהיה המתאים ביותר לאחסון מזהי משתמש ייחודיים (user IDs) ב-Python?

- A. רשימה (List)
- B. מילון (Dictionary)
- C. קבוצה (Set)
- D. טאפל (Tuple)

**תשובה נכונה: C**

**הסבר:**

ב-Python, טיפוס הנתונים המתאים ביותר לאחסון איברים ייחודיים הוא `set` (קבוצה).

*   **אפשרות A** אינה נכונה: רשימות יכולות להכיל איברים כפולים ושומרות על סדר האיברים.
*   **אפשרות B** אינה נכונה: מילונים מאחסנים זוגות מפתח-ערך, ובעוד שהמפתחות חייבים להיות ייחודיים, אחסון מזהי משתמש ייחודיים בלבד באמצעותם אינו יעיל.
*   **אפשרות C** נכונה: קבוצות מאחסנות רק איברים ייחודיים בסדר שרירותי ואינן תומכות בכפילויות.
*   **אפשרות D** אינה נכונה: טאפלים הם בלתי ניתנים לשינוי (immutable) ויכולים להכיל איברים כפולים.

**מדוע קבוצה (`set`) מתאימה לאחסון מזהי משתמש ייחודיים:**

1.  **ייחודיות איברים:** קבוצות מסירות אוטומטית כפילויות, מה שהופך אותן לאידיאליות לאחסון מזהים ייחודיים.
2.  **בדיקת קיום מהירה:** בדיקת קיום איבר בקבוצה מתבצעת מהר מאוד (בממוצע O(1)), בזכות מימוש המבוסס על טבלת גיבוב (hash table).
3.  **חוסר סדר:** קבוצות אינן מבטיחות שמירה על סדר האיברים, דבר המקובל עבור מזהי משתמש.
4.  **שינויים (Mutability):** קבוצות ניתנות לשינוי (אפשר להוסיף או להסיר איברים).

**דוגמה:**

```python
# דוגמה לשימוש בקבוצה לאחסון מזהי משתמש
user_ids: set[str] = {"user123", "user456", "user789", "user123"}
print(f"מזהי משתמש ייחודיים: {user_ids}") # פלט: מזהי משתמש ייחודיים: {'user789', 'user123', 'user456'}

user_ids.add("user000")
print(f"מזהים לאחר הוספה: {user_ids}") # פלט: מזהים לאחר הוספה: {'user789', 'user000', 'user123', 'user456'}

print(f"בדיקת קיום user123: {'user123' in user_ids}") # פלט: בדיקת קיום user123: True
print(f"בדיקת קיום user999: {'user999' in user_ids}")  # פלט: בדיקת קיום user999: False
```

**בתוצאה:**

*   בעת יצירת הקבוצה, כפילויות מוסרות, ולכן "user123" מופיע רק פעם אחת.
*   איברי הקבוצה אינם מסודרים, ולכן סדר הפלט שלהם עשוי לא להתאים לסדר ההוספה.
*   פעולת `in` לבדיקת קיום איבר בקבוצה מתבצעת במהירות.

לכן, **אפשרות C** נכונה.