### `question_702.md`

**שאלה 702.** נתונות רשימת מספרים שלמים `candidates` ומספר שלם `target`. פתחו אלגוריתם המוצא ומחזיר את כל הצירופים הייחודיים של מספרים מתוך `candidates`, שסכומם שווה ל-`target`. כל מספר מתוך הרשימה `candidates` יכול לשמש פעם אחת בלבד בכל צירוף. התוצאה אינה צריכה להכיל כפילויות.

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

- א. לפתרון הבעיה יש להשתמש במעבר ממצה (full enumeration) על כל הצירופים האפשריים עם בדיקת סכום.
- ב. לפתרון הבעיה יש להשתמש באלגוריתם חמדן (greedy algorithm) בלבד, תוך בחירת איברים מתאימים עד להגעה לערך `target` הנדרש.
- ג. לפתרון הבעיה יש להשתמש באלגוריתם מיון (sorting algorithm) בלבד.
- ד. לפתרון הבעיה יש להשתמש ברקורסיה (recursion) עם מעקב לאחור (backtracking) וגיזום (pruning) נוסף של פתרונות לא מבטיחים.

**תשובה נכונה: ד**

**הסבר:**

לפתרון הבעיה של מציאת כל הצירופים הייחודיים שסכומם שווה לערך היעד הנתון, משתמשים באלגוריתם רקורסיבי של מעקב לאחור (backtracking), המאפשר לבחון את כל הצירופים האפשריים של מספרים עם האילוצים הנתונים, וכולל גיזום (pruning) של ענפים לא מבטיחים, מה שמשפר את הביצועים.

*   **אלגוריתם (רקורסיבי עם מעקב לאחור):**
    1.  **מיון:** הרשימה המקורית `candidates` ממוינת, מה שמאפשר למנוע צירופים כפולים.
    2. **פונקציה רקורסיבית:** נוצרת פונקציה רקורסיבית, אשר:
         *   מקבלת את הצירוף הנוכחי, את הסכום הנותר `target`, את אינדקס האיבר הנוכחי, ואת רשימת התוצאות.
        * **מקרה בסיס (הצלחה):** אם `target` שווה ל-`0`, הצירוף הנוכחי מתווסף לרשימת התוצאות.
         *  **מקרה בסיס (גיזום):** אם `target` קטן מ-0, הפונקציה אינה מוסיפה דבר וחוזרת.
        *  **איטרציה ורקורסיה:** מבצעים איטרציה על האיברים, החל מהאינדקס הנוכחי:
             *    מתעלמים מכפילויות: לשם כך נדרש להשתמש בבדיקה `if i > index and candidates[i] == candidates[i-1]: continue`.
            *  קוראים לפונקציה רקורסיבית, מקטינים את הסכום הנותר ומעבירים לרקורסיה את ערך האינדקס הנוכחי + 1.
        *  **מעקב לאחור (Backtracking):** מבטלים את הבחירה הנוכחית (לא מוסיפים את האיבר לצירוף), כדי לשקול אפשרויות אחרות.

*  **יתרונות האלגוריתם:**
    *   **מציאת כל הצירופים:** בוחן את כל תתי-הקבוצות האפשריות הנותנות את הסכום הרצוי.
    *   **מעקב לאחור (Backtracking):** פוסל אפשרויות לא מתאימות.
    *  **גיזום (Pruning):** גיזום על כפילויות ועל סכום שלילי, לצורך אופטימיזציה של הפתרון.

**דוגמאות (פסאודו-קוד):**

```
function find_combinations(candidates, target, index, current_combination, result):
   if target == 0:
        add current_combination to result
        return

   if target < 0:
        return

    for i from index to length(candidates) - 1:
      if i > index and candidates[i] == candidates[i-1]:
        continue

            # כלול
            current_combination.append(candidates[i])
            find_combinations(candidates, target-candidates[i], i+1, current_combination, result)
             current_combination.removeLast() # מעקב לאחור
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
        current_combination.pop() # מעקב לאחור

    backtrack(0, [], target) # מתחילים חיפוש רקורסיבי
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
*   **א. לפתרון הבעיה יש להשתמש במעבר ממצה על כל הצירופים האפשריים עם בדיקת סכום.:** שגוי. מעבר ממצה אינו יעיל.
*  **ב. לפתרון הבעיה יש להשתמש באלגוריתם חמדן בלבד, תוך בחירת איברים מתאימים עד להגעה לערך target הנדרש.:** שגוי. אלגוריתם חמדן אינו מבטיח מציאת כל הפתרונות.
*  **ג. לפתרון הבעיה יש להשתמש באלגוריתם מיון בלבד.:** שגוי.
*   **ד. לפתרון הבעיה יש להשתמש ברקורסיה עם מעקב לאחור וגיזום נוסף של פתרונות לא מבטיחים.:** נכון.

**לסיכום:**
*   האלגוריתם הרקורסיבי עם מעקב לאחור מוצא את כל הצירופים האפשריים של מספרים עם האילוצים הנתונים.
*   השיטה מאפשרת לגזום פתרונות לא מבטיחים (אם הסכום הופך שלילי), וכן למנוע כפילויות.

לפיכך, התשובה הנכונה היא **ד. לפתרון הבעיה יש להשתמש ברקורסיה עם מעקב לאחור וגיזום נוסף של פתרונות לא מבטיחים.**