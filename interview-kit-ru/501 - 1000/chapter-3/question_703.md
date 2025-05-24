### `שאלה 703.md`

**שאלה 703.** נתונה רשימה של מספרים שלמים `candidates` ומספר שלם `target`. פיתחו אלגוריתם המוצא ומחזיר את כל הצירופים הייחודיים של מספרים מתוך `candidates`, שסכומם שווה ל-`target`. כל מספר מהרשימה `candidates` יכול לשמש פעם אחת בלבד בכל צירוף. התוצאה לא אמורה להכיל צירופים כפולים.

**דוגמאות:**

```
קלט: candidates = [10,1,2,7,6,1,5], target = 8
פלט: [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

קלט: candidates = [2,5,2,1,2], target = 5
פלט: [
[1,2,2],
[5]
]
```

- א. על מנת לפתור את הבעיה, יש להשתמש במעבר מלא על כל הצירופים האפשריים עם בדיקה של הסכום.
- ב. על מנת לפתור את הבעיה, יש להשתמש רק באלגוריתם חמדן, בוחרים אלמנטים מתאימים עד להגעה לערך ה-target הנדרש.
- ג. על מנת לפתור את הבעיה, יש להשתמש רק באלגוריתם מיון.
- ד. על מנת לפתור את הבעיה, יש להשתמש ברקורסיה עם Backtracking וגיזום נוסף של פתרונות לא מבטיחים.

**תשובה נכונה: D**

**הסבר:**

על מנת לפתור את בעיית מציאת כל הצירופים הייחודיים שסכומם שווה לערך יעד נתון, נעשה שימוש באלגוריתם רקורסיבי של Backtracking, המאפשר מעבר על כל הצירופים האפשריים של מספרים עם האילוצים הנתונים, וכן גיזום של ענפים לא מבטיחים, מה שמשפר את הביצועים.

*   **אלגוריתם (רקורסיבי עם Backtracking):**
    1.  **מיון:** הרשימה המקורית `candidates` ממוינת, מה שמאפשר הימנעות מצירופים כפולים.
    2. **פונקציה רקורסיבית:** נוצרת פונקציה רקורסיבית אשר:
         *   מקבלת את הצירוף הנוכחי, את הסכום הנותר `target`, את אינדקס האלמנט הנוכחי, ואת רשימת התוצאות.
        * **מקרה בסיס (הצלחה):** אם `target` שווה ל-`0`, אזי הצירוף הנוכחי מתווסף לרשימת התוצאות.
         *  **מקרה בסיס (גיזום):** אם `target` קטן מ-0, אזי הפונקציה לא מוסיפה דבר וחוזרת.
        *  **איטרציה ורקורסיה:** עוברים באיטרציה על האלמנטים, החל מהאינדקס הנוכחי:
             *    מתעלמים מכפילויות: לשם כך נדרש להשתמש בבדיקה `if i > index and candidates[i] == candidates[i-1]: continue`.
            *  קוראים רקורסיבית לפונקציה, מקטינים את הסכום הנותר ומעבירים לרקורסיה את ערך האינדקס הנוכחי + 1.
        *  **Backtracking:** מבטלים את הבחירה הנוכחית (לא מוסיפים את האלמנט לצירוף), על מנת לשקול אפשרויות אחרות.

*  **יתרונות האלגוריתם:**
    *   **מציאת כל הצירופים:** עובר על כל תת-הקבוצות האפשריות שסכומן מניב את הסכום הנדרש.
    *   **Backtracking:** מבטל אפשרויות לא מתאימות.
    *  **גיזום:** גיזום על כפילויות וסכום שלילי, לצורך אופטימיזציית הפתרון.

**דוגמאות (פסאודו-קוד):**

```
פונקציה find_combinations(candidates, target, index, current_combination, result):
   if target == 0:
        add current_combination to result
        return

   if target < 0:
        return

    for i from index to length(candidates) - 1:
      if i > index and candidates[i] == candidates[i-1]:
        continue

        # include
        current_combination.append(candidates[i])
        find_combinations(candidates, target-candidates[i], i+1, current_combination, result)
         current_combination.removeLast() # Backtracking
```

**דוגמאות מימוש ב-Python:**

```python
def find_combinations(candidates, target):
    result = []
    candidates.sort()
    def backtrack(index, current_combination, remaining_target):
      if remaining_target == 0:
         result.append(current_combination.copy())
         return
      if remaining_target < 0:
         return

      for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i-1]:
            continue
        current_combination.append(candidates[i])
        backtrack(i+1, current_combination, remaining_target - candidates[i])
        current_combination.pop() # Backtracking

    backtrack(0, [], target) # מתחילים את החיפוש הרקורסיבי
    return result


candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
print(f"קלט: candidates = {candidates1}, target = {target1}")
print(f"פלט: {find_combinations(candidates1, target1)}") # פלט:  [['1', '1', '6'], ['1', '2', '5'], ['1', '7'], ['2', '6']]

candidates2 = [2, 5, 2, 1, 2]
target2 = 5
print(f"קלט: candidates = {candidates2}, target = {target2}")
print(f"פלט: {find_combinations(candidates2, target2)}")  # פלט: [['1', '2', '2'], ['5']]
```

**ניתוח האפשרויות:**
*   **א. על מנת לפתור את הבעיה, יש להשתמש במעבר מלא על כל הצירופים האפשריים עם בדיקה של הסכום.:** לא נכון. מעבר מלא אינו יעיל.
*  **ב. על מנת לפתור את הבעיה, יש להשתמש רק באלגוריתם חמדן, בוחרים אלמנטים מתאימים עד להגעה לערך ה-target הנדרש.:** לא נכון. אלגוריתם חמדן אינו מבטיח מציאת כל הפתרונות.
*  **ג. על מנת לפתור את הבעיה, יש להשתמש רק באלגוריתם מיון.:** לא נכון.
*   **ד. על מנת לפתור את הבעיה, יש להשתמש ברקורסיה עם Backtracking וגיזום נוסף של פתרונות לא מבטיחים.:** נכון.

**לסיכום:**
*   האלגוריתם הרקורסיבי עם Backtracking מוצא את כל הצירופים האפשריים של מספרים עם האילוצים הנתונים.
*   השיטה מאפשרת גיזום פתרונות לא מבטיחים (אם הסכום הופך לשלילי), וכן הימנעות מכפילויות.

לפיכך, התשובה הנכונה היא **ד. על מנת לפתור את הבעיה, יש להשתמש ברקורסיה עם Backtracking וגיזום נוסף של פתרונות לא מבטיחים.**