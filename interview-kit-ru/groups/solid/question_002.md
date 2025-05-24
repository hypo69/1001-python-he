### `question_002.md` (SRP - דוגמה להפרה)

**שאלה 002.** איזו מהדוגמאות הבאות לקוד Python *מפרה באופן המובהק ביותר* את עקרון האחריות היחידה (SRP)?

A.
```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_password(self, new_password):
        self.password = new_password
```

B.

```python
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def send_email(self, message):
        # Code to send email
        pass
```

C.

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, password):
        return self.password == password
```

D.

```python
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def save_to_database(self):
        # Code to save user data to database
        pass

    def send_welcome_email(self):
        # Code to send a welcome email to the user
        pass
```

**תשובה נכונה: D**

**הסבר:**

עקרון האחריות היחידה (SRP) קובע שלמחלקה צריכה להיות רק סיבה אחת לשינוי. באפשרות D, למחלקת ה-`User` יש *שתי אחריויות מובחנות באופן מובהק*: ניהול נתוני משתמש ואינטראקציה עם מסד הנתונים ושליחת דוא"ל קבלת פנים.

*   **אפשרות A:** מחלקת ה-`User` אחראית רק על אחסון ושינוי נתוני משתמש.
*   **אפשרות B:** מחלקת ה-`User` אחראית רק על אחסון נתוני משתמש ושליחת דוא"ל.
*   **אפשרות C:** מחלקת ה-`User` אחראית רק על אחסון נתוני משתמש ואותנטיקציה.
*   **אפשרות D:** מחלקת ה-`User` אחראית על:
    *   ניהול נתוני משתמש.
    *   שמירת הנתונים במסד הנתונים.
    *   שליחת דוא"ל קבלת פנים. - *הפרת SRP*

**דוגמה לרפקטורינג (פשוטה):**

```python
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def save(self, user: User):
        # Code to save user data to database
        pass

class EmailService:
    def send_welcome_email(self, user: User):
        # Code to send a welcome email to the user
        pass
```
**תוצאה:**

ההפרה המובהקת ביותר של SRP מתרחשת באפשרות D, שבה למחלקת ה-`User` יש מספר אחריויות שאינן קשורות.

לפיכך, אפשרות D היא התשובה הנכונה.