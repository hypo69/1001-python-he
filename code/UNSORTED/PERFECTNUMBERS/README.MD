# מודול לאיתור מספרים משוכללים

מודול זה, `perfect_numbers.py`, מספק פונקציות להגדרה ולאיתור מספרים משוכללים.

## מהו מספר משוכלל?

מספר משוכלל הוא מספר שלם חיובי השווה לסכום מחלקיו החיוביים העצמיים (למעט המספר עצמו).

דוגמאות:

- 6 = 1 + 2 + 3
- 28 = 1 + 2 + 4 + 7 + 14
- 496
- 8128

## פונקציות

### `sum_of_divisors(n)`

מחשבת את סכום כל המחלקים העצמיים של המספר `n`.

**ארגומנטים:**

- `n`: מספר שלם.

**מחזירה:**

- סכום המחלקים העצמיים של המספר `n`.

### `is_perfect_number(n)`

בודקת האם המספר `n` הוא מספר משוכלל.

**ארגומנטים:**

- `n`: מספר שלם.

**מחזירה:**

- `True` אם המספר `n` הוא מספר משוכלל, אחרת `False`.

### `find_perfect_numbers(limit)`

מאתרת את כל המספרים המשוכללים בטווח מ-1 עד `limit` (כולל).

**ארגומנטים:**

- `limit`: הגבול העליון של הטווח.

**מחזירה:**

- רשימה של כל המספרים המשוכללים בטווח הנתון.

## שימוש

לשימוש במודול:

1.  שמור את קוד ה-Python בקובץ `perfect_numbers.py`.
2.  יבא את הפונקציות לפרויקט שלך:

    ```python
    from perfect_numbers import find_perfect_numbers, is_perfect_number

    limit = 10000
    perfect_numbers = find_perfect_numbers(limit)
    print(f"מספרים משוכללים עד {limit}: {perfect_numbers}")


    number_to_check = 28
    if is_perfect_number(number_to_check):
       print(f"{number_to_check} הוא מספר משוכלל")
    else:
        print(f"{number_to_check} אינו מספר משוכלל")
    ```
    דוגמת קריאה יודפס בעת הרצת הסקריפט `perfect_numbers.py`.
## דוגמת פלט:
    מספרים משוכללים עד 10000: [6, 28, 496, 8128]
    28 הוא מספר משוכלל
## הרצה
`python perfect_numbers.py`