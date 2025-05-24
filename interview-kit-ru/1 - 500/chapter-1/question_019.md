### `question_019.md`

**שאלה 19.** התבונן בביצוע הפעולות הבאות על מילון פייתון. מהו מצב המילון `person` לאחר השלמת כל הפעולות?

```python
person = {'name': 'Alice', 'age': 25}
person['age'] = 26
person.update({'city': 'New York'})
del person['name']
```

- A. `{'name': 'Alice', 'age': 26, 'city': 'New York'}`
- B. `{'age': 26}`
- C. `{'age': 26, 'city': 'New York'}`
- D. `{'name': 'Alice', 'city': 'New York'}`

**התשובה הנכונה: C**

**הסבר:**

בקוד זה מתבצעות הפעולות הבאות על המילון `person`:

1.  **אתחול:** `person = {'name': 'Alice', 'age': 25}` - נוצר מילון `person` עם זוגות מפתח-ערך התחלתיים: `name`: `'Alice'` ו-`age`: `25`.
2.  **עדכון ערך:** `person['age'] = 26` - ערך המפתח `'age'` משתנה מ-`25` ל-`26`.
3.  **הוספת איבר:** `person.update({'city': 'New York'})` - מוסיף זוג מפתח-ערך חדש `'city': 'New York'` למילון.
4.  **מחיקת איבר:** `del person['name']` - מוחק את זוג המפתח-ערך עם המפתח `'name'` מהמילון.

עקוב אחר מצב המילון `person` לאחר כל פעולה:
*   מצב התחלתי: `{'name': 'Alice', 'age': 25}`
*   לאחר שינוי `age`: `{'name': 'Alice', 'age': 26}`
*   לאחר הוספת `city`: `{'name': 'Alice', 'age': 26, 'city': 'New York'}`
*   לאחר מחיקת `name`: `{'age': 26, 'city': 'New York'}`

**דוגמה:**

```python
person: dict[str, str | int] = {'name': 'Alice', 'age': 25}
print(f"מצב התחלתי: {person}")

person['age'] = 26
print(f"לאחר שינוי הגיל: {person}")

person.update({'city': 'New York'})
print(f"לאחר הוספת העיר: {person}")

del person['name']
print(f"לאחר מחיקת השם: {person}")
```
**בתוצאה:**

לאחר ביצוע כל הפעולות, המילון `person` יכיל את זוגות המפתח-ערך `{'age': 26, 'city': 'New York'}`. המפתח `'name'` יימחק, וערך המפתח `'age'` יעודכן.

לפיכך, **אפשרות C** נכונה.