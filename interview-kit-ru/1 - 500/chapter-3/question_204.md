### `question_204.md`

**שאלה 204.** בפייתון, מה עושה האופרטור `yield from` במחולל (generator)?

א. הוא מסיים את ביצוע המחולל.
ב. הוא מעביר את הבקרה למחולל אחר, ומאפשר לו להחזיר ערכים.
ג. הוא יוצר רשימה חדשה המבוססת על הערכים המוחזרים על ידי מחולל אחר.
ד. הוא משמש לטיפול בחריגות במחולל.

**תשובה נכונה: ב**

**הסבר:**

האופרטור `yield from` בפייתון משמש בתוך מחוללים להאצלת (delegating) חלק מעבודתם למחולל אחר (או לאובייקט איטרבילי אחר). הוא מאפשר להפנות מחדש את זרם הנתונים והערכים ממחולל אחד למשנהו.

*   **אפשרות א'** אינה נכונה: לסיום מחולל משתמשים ב-`return`.
*   **אפשרות ב'** נכונה: `yield from` מאציל את האיטרציות למחולל אחר.
*   **אפשרות ג'** אינה נכונה: `yield from` אינו יוצר רשימה חדשה, אלא מחזיר ערכים.
*   **אפשרות ד'** אינה נכונה: לטיפול בחריגות משתמשים בבלוק `try-except`.

**כיצד `yield from` פועל:**

1.  כאשר בתוך מחולל נתקלים ב-`yield from other_generator`, הבקרה מועברת באופן זמני למחולל האחר `other_generator`.
2.  הערכים ש-`other_generator` מחזיר, יוחזרו גם על ידי המחולל המקורי.
3.  כאשר `other_generator` יסיים את עבודתו, הבקרה תחזור למחולל המקורי, שימשיך את הביצוע מהשורה הבאה אחרי `yield from`.

**דוגמה:**

```python
def sub_generator(n: int):
  for i in range(n):
      yield i

def main_generator(n: int):
    yield from sub_generator(n) # מאצילים את העבודה
    yield "Конец"


gen = main_generator(3)

for value in gen:
    print(value)
# פלט:
# 0
# 1
# 2
# Конец
```

**כתוצאה מכך:**

*   `main_generator` מאציל את האיטרציה ל-`sub_generator`.
*   הערכים מ-`sub_generator` מוחזרים על ידי הפונקציה `main_generator`, כאילו היו חלק מפונקציה אחת.

לפיכך, **אפשרות ב'** היא התשובה הנכונה.