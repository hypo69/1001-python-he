```python
import datetime
import random

def calculate_age(birth_date_str):
    """מחשב את הגיל על בסיס מחרוזת תאריך לידה."""
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
            
            print(f"\nחשבתי על תאריך לידה, נסה לנחש בן כמה האדם כעת.")
            
            guess_age = int(input("הניחוש שלך: "))
            
            if guess_age == real_age:
                print("הידד, ניחשת נכון!")
            else:
                print(f"לא ניחשת נכון, התשובה הנכונה היא: {real_age}")

            play_again = input("רוצה לשחק שוב? (כן/לא): ")
            if play_again.lower() != "כן":
                print("תודה על המשחק!")
                break

        except ValueError:
           print("קלט לא חוקי. אנא הכנס מספר שלם.")


if __name__ == "__main__":
    play_age_guessing_game()
```

**אופן הפעולה:**

1.  **`calculate_age(birth_date_str)`:** פונקציה זו מחשבת את הגיל על בסיס מחרוזת תאריך לידה.
2.  **`play_age_guessing_game()`:**
    *   מקדמת בברכה את השחקן.
    *   מריצה לולאה אינסופית (עד שהשחקן יחליט לסיים).
    *   מייצרת תאריך לידה אקראי.
    *   מחשבת את הגיל ה'נכון' באמצעות `calculate_age`.
    *   מבקשת מהמשתמש להכניס את הניחוש שלו לגיל.
    *   משווה את קלט המשתמש לגיל האמיתי ומודיעה על התוצאה.
    *   שואלת את השחקן אם הוא רוצה לשחק שוב.
    *   שוברת את הלולאה אם השחקן לא רוצה לשחק.
3.  **`if __name__ == "__main__":`:** זהו מוסכמה סטנדרטית בפייתון להפעיל את `play_age_guessing_game()` רק כאשר הסקריפט מורץ ישירות.

**כיצד להריץ:**

1.  שמור את הקוד בקובץ עם סיומת `.py` (לדוגמה, `age_game.py`).
2.  הרן את הקובץ במסוף על ידי ביצוע הפקודה:
    ```bash
    python age_game.py
    ```

**כיצד לשחק:**

1.  המשחק יציע לך לנחש את הגיל, אשר חושב על בסיס תאריך לידה אקראי.
2.  הכנס את הניחוש שלך.
3.  תראה אם ניחשת נכון או לא, ואם תרצה תוכל לשחק שוב.

**שיפורים אפשריים:**

*   ניתן להוסיף רמת קושי (לדוגמה, הגבלת זמן).
*   להפוך את הקלט לבטוח יותר (במיוחד בחלק של קלט תאריך הלידה, כאשר הוא מוזן על ידי המשתמש).
*   ניתן להוסיף רמות קושי (בהתאם לטווח השנים).