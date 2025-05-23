
### מאפייני קבוצות (`set`) והשוואה לרשימות (`list`) וטאפלים (`tuple`)

מהו המאפיין העיקרי של קבוצות (`set`) בפייתון המבדיל אותן מרשימות (`list`) וטאפלים (`tuple`), ולאילו משימות הן מתאימות ביותר?

**A.** קבוצות מסודרות ויכולות להכיל אלמנטים כפולים, מה שהופך אותן לאידיאליות לפעולות מתמטיות.
**B.** קבוצות אינן מסודרות ומאחסנות רק אלמנטים ייחודיים. הן יעילות לבדיקת שייכות של אלמנט ולביצוע פעולות מתורת הקבוצות (איחוד, חיתוך).
**C.** קבוצות ניתנות לשינוי ויכולות להכיל אלמנטים מסוגים שונים, אך אינן תומכות באינדקסציה. הן משמשות בעיקר לאחסון הגדרות.
**D.** קבוצות הן קולקציות אי-שינויות ומסודרות, המיועדות לחיפוש מהיר של אלמנטים לפי ערכם.

✅ **תשובה נכונה: B**

---

### 🧠 הסבר:

לקבוצות (`set`) בפייתון שני מאפיינים עיקריים:

* **ייחודיות אלמנטים:** לא ניתן לאחסן את אותו אלמנט פעמיים. ניסיונות להוספת ערך שכבר קיים יתעלמו ממנו.
* **אי-סדר:** אין סדר קבוע לאלמנטים, ואין אפשרות גישה לפי אינדקס.

---

### 🧰 מתי להשתמש בקבוצות:

1. **הסרת כפילויות** מתוך רשימה או רצף אחר – על ידי המרה ל־`set`.
2. **בדיקת שייכות** מהירה של ערכים (בממוצע O(1)).
3. **פעולות מתמטיות**: איחוד, חיתוך, הפרש, הפרש סימטרי.

---

### 🧩 היבטי מפתח:

* **\[1]** ייחודיות אלמנטים
* **\[2]** אי-סדר ואי-תמיכה באינדקסים
* **\[3]** יעילות בבדיקת שייכות ובפעולות מתמטיות בין קבוצות

---

### 🧪 דוגמה:

```python
# רשימה עם כפילויות
my_list_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]

# הסרת כפילויות על ידי המרה לקבוצה
unique_elements = set(my_list_with_duplicates)
print(f"קבוצת אלמנטים ייחודיים: {unique_elements}")  # הסדר עשוי להשתנות

# פעולות בין קבוצות
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"איחוד: {set1 | set2}")
print(f"חיתוך: {set1 & set2}")
print(f"הפרש: {set1 - set2}")

# בדיקת שייכות
element_to_check = 3
if element_to_check in set1:
    print(f"האלמנט {element_to_check} נמצא ב־set1")
```

---

### 🎯 לסיכום:

קבוצות בפייתון שונות מרשימות וטאפלים בכך שהן אינן מסודרות ומאחסנות אך ורק ערכים ייחודיים. הן יעילות במיוחד להסרת כפילויות, לבדוק שייכות של ערך, ולבצע פעולות מתמטיות בין אוספים.

🟩 **לכן התשובה הנכונה היא: B**

---

רוצה שאבנה כך שאלות נוספות?
