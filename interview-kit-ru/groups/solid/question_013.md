### `question_013.md` (SOLID - בדיקות)

**שאלה 013.** כיצד יישום עקרונות SOLID משפיע *באופן ישיר* על פישוט תהליך הבדיקה של רכיבי תוכנה בפייתון?

א. עקרונות SOLID מסבכים את הבדיקה, מכיוון שהם דורשים כתיבת מספר רב יותר של מקרי בדיקה לכל מחלקה וממשק.
ב. עקרונות SOLID אינם משפיעים כלל על תהליך הבדיקה, מכיוון שהבדיקה תלויה אך ורק בבחירת פרימוורק הבדיקה.
ג. עקרונות SOLID מפשטים את הבדיקה על ידי הפחתת הצימוד (coupling) והגברת הלכידות (cohesion), דבר המאפשר לבדוק רכיבים בודדים באופן מבודד, תוך שימוש במוקים (mocks) וסטאבים (stubs).
ד. עקרונות SOLID הופכים את הקוד לבלתי-ניתן לבדיקה, מכיוון שהם מובילים ליצירת מספר גדול מדי של הפשטות.

**תשובה נכונה: ג**

**הסבר:**

עקרונות SOLID משפיעים *באופן חיובי* על יכולת הבדיקה של הקוד, והופכים אותו לקל יותר לבדיקה ולניפוי שגיאות.

*   **כיצד SOLID מפשט את הבדיקה:**

    *   **SRP (Single Responsibility Principle):** מחלקות בעלות אחריות אחת ויחידה קלות יותר לבדיקה, מכיוון שצריך לבדוק רק פונקציונליות ספציפית אחת.
    *   **OCP (Open/Closed Principle):** האפשרות להרחיב פונקציונליות ללא שינוי קוד קיים מאפשרת להוסיף בדיקות חדשות מבלי להשפיע על הבדיקות הישנות.
    *   **LSP (Liskov Substitution Principle):** מבטיח שתת-מחלקות יכולות לשמש במקום מחלקות בסיס, דבר המאפשר שימוש בפולימורפיזם בבדיקות.
    *   **ISP (Interface Segregation Principle):** מפחית את מספר המתודות שיש לבדוק בממשקים, ומפשט את יצירת מוקים וסטאבים.
    *   **DIP (Dependency Inversion Principle):** מאפשר החלפת תלויות במוקים וסטאבים במהלך הבדיקה, דבר המפשט בדיקה מבודדת של רכיבים.

*   **מוקים (Mocks) וסטאבים (Stubs):** הודות ל-DIP ו-ISP, ניתן ליצור בקלות מוקים וסטאבים כדי לדמות התנהגות של תלויות, מה שמאפשר לבדוק קוד באופן מבודד מתלויות אמיתיות (מסדי נתונים, ממשקי API חיצוניים וכו').

*   **אפשרות א אינה נכונה:** להיפך, הבדיקה הופכת לפשוטה יותר.
*   **אפשרות ב אינה נכונה:** SOLID משפיע על תהליך הבדיקה.
*   **אפשרות ג נכונה:** זהו תיאור מדויק של השפעת SOLID על פישוט הבדיקה.
*   **אפשרות ד אינה נכונה:** SOLID הופך את הקוד ליותר ניתן לבדיקה.

**דוגמה:**

```python
from abc import ABC, abstractmethod

class EmailService(ABC):
    @abstractmethod
    def send_email(self, email, message):
        pass

class MockEmailService(EmailService): # Mock for testing
    def send_email(self, email, message):
        print(f"Mock Email sent to {email} with message: {message}")

class UserService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def create_user(self, username, email):
        # Create user logic
        self.email_service.send_email(email, "Welcome!")

# In tests
mock_email_service = MockEmailService()
user_service = UserService(mock_email_service)
user_service.create_user("testuser", "test@example.com") #Doesn't really send email
```

**כתוצאה מכך:**

עקרונות SOLID מפשטים את הבדיקה על ידי הפחתת הצימוד (coupling) והגברת הלכידות (cohesion), דבר המאפשר לבדוק רכיבים בודדים באופן מבודד, תוך שימוש במוקים וסטאבים.

לפיכך, אפשרות ג היא התשובה הנכונה.

מה נדרש לעיבוד הקובץ: question_014.md