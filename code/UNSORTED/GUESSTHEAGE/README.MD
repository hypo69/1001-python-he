```python
import datetime
import random

def calculate_age(birth_date_str):
    """מחשב את הגיל על בסיס מחרוזת המכילה תאריך לידה."""
    birth_date = datetime.datetime.strptime(birth_date_str, '%d.%m.%Y').date()
    current_date = datetime.date.today()
    age_years = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (
            current_date.month == birth_date.month and current_date.day < birth_date.day):
        age_years -= 1
    return age_years


def play_age_guessing_game():
    """משחק ניחוש גיל."""
    print("ברוכים הבאים למשחק 'נחש את הגיל'! ")

    while True:
        try:
            birth_year = random.randint(1900, datetime.date.today().year)
            birth_month = random.randint(1, 12)
            birth_day = random.randint(1, 28) # מפשטים כדי לא לבדוק ימים בכל חודש

            birth_date_str = f"{birth_day:02}.{birth_month:02}.{birth_year}"  # יוצרים את מחרוזת התאריך

            real_age = calculate_age(birth_date_str)

            print(f"\nהגרלתי תאריך לידה, נסה לנחש בן כמה האדם כרגע.")

            guess_age = int(input("הניחוש שלך: "))

            if guess_age == real_age:
                print("הידד, ניחשת נכון!")
            else:
                print(f"לא ניחשת נכון, התשובה הנכונה היא: {real_age}")

            play_again = input("נשחק שוב? (כן/לא): ")
            if play_again.lower() != "д":
                print("תודה ששיחקת!")
                break

        except ValueError:
           print("קלט לא תקין. אנא הזן מספר שלם.")


if __name__ == "__main__":
    play_age_guessing_game()
```

**אופן הפעולה:**

1.  **`calculate_age(birth_date_str)`:** פונקציה זו מחשבת את הגיל מתוך מחרוזת, כפי שמוצג בדוגמה מהתמונה.
2.  **`play_age_guessing_game()`:**
    *   מברך את השחקן.
    *   מפעיל לולאה אינסופית (עד שהשחקן יבחר לסיים).
    *   מייצר באופן אקראי תאריך לידה.
    *   מחשב את הגיל ה'נכון' באמצעות `calculate_age`.
    *   מבקש מהמשתמש להזין את הניחוש שלו לגיל.
    *   משווה את קלט המשתמש לגיל האמיתי ומדווח על התוצאה.
    *   שואל את השחקן האם ברצונו לשחק שוב.
    *   מפסיק את הלולאה אם השחקן אינו מעוניין לשחק.
3.  **`if __name__ == "__main__":`:** זהו קונספט פייתון סטנדרטי להפעלה של `play_age_guessing_game()` רק כאשר הסקריפט מורץ ישירות.

**כיצד להפעיל:**

1.  שמור את הקוד בקובץ עם סיומת `.py` (לדוגמה, `age_game.py`).
2.  הרץ את הקובץ בטרמינל באמצעות הפקודה:
    ```bash
    python age_game.py
    ```

**כיצד לשחק:**

1.  המשחק יציע לך לנחש את הגיל שחושב על בסיס תאריך לידה אקראי.
2.  הזן את הניחוש שלך.
3.  תראה אם ניחשת נכון או לא, ותוכל לבחור לשחק שוב אם תרצה.

**שיפורים אפשריים:**

*   ניתן להוסיף רמות קושי (לדוגמה, הגבלת זמן).
*   לאבטח יותר את הקלט (במיוחד בהקשר של הזנת תאריך לידה, כאשר המשתמש מזין אותו).
*   ניתן להוסיף רמות קושי (בהתאם לטווח השנים).