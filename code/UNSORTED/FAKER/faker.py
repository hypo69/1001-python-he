import random
import string
from typing import List, Optional

class FakeDataGenerator:
    """
    יצירת נתונים פיקטיביים.

    מיישמת פונקציות בסיסיות, כגון יצירת שמות, כתובות, מספרי טלפון ונתונים אחרים.
    """

    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    streets = ['Main St', 'Elm St', '2nd Ave', 'Park Blvd', 'Oak Dr']
    domains = ['example.com', 'mail.com', 'test.org', 'website.net']

    def random_name(self) -> str:
        """
        יצירת שם מלא אקראי.

        Returns:
            str: שם מלא, המורכב משם פרטי ושם משפחה אקראיים.
        """
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return f'{first_name} {last_name}'

    def random_email(self) -> str:
        """
        יצירת כתובת דוא"ל אקראית.

        Returns:
            str: כתובת דוא"ל בפורמט `שם.משפחה@דומיין`.
        """
        first_name = random.choice(self.first_names).lower()
        last_name = random.choice(self.last_names).lower()
        domain = random.choice(self.domains)
        return f'{first_name}.{last_name}@{domain}'

    def random_phone(self) -> str:
        """
        יצירת מספר טלפון אקראי בפורמט `+1-XXX-XXX-XXXX`.

        Returns:
            str: מספר הטלפון.
        """
        return f'+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}'

    def random_address(self) -> str:
        """
        יצירת כתובת אקראית.

        Returns:
            str: הכתובת בפורמט `רחוב, עיר`.
        """
        street = random.choice(self.streets)
        city = random.choice(self.cities)
        house_number = random.randint(1, 9999)
        return f'{house_number} {street}, {city}'

    def random_string(self, length: int = 10) -> str:
        """
        יצירת מחרוזת אקראית באורך נתון.

        Args:
            length (int, optional): אורך המחרוזת. ברירת מחדל 10.

        Returns:
            str: מחרוזת אקראית המכילה אותיות וספרות.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def random_int(self, min_value: int = 0, max_value: int = 100) -> int:
        """
        יצירת מספר שלם אקראי בטווח נתון.

        Args:
            min_value (int, optional): ערך מינימלי. ברירת מחדל 0.
            max_value (int, optional): ערך מקסימלי. ברירת מחדל 100.

        Returns:
            int: המספר השלם האקראי.
        """
        return random.randint(min_value, max_value)

    def random_choice(self, options: List[str]) -> str:
        """
        בחירת פריט אקראי מרשימה.

        Args:
            options (List[str]): רשימת ערכים לבחירה.

        Returns:
            str: הפריט האקראי מהרשימה.
        """
        return random.choice(options)

# דוגמה לשימוש
if __name__ == '__main__':
    faker = FakeDataGenerator()

    print(f'Name: {faker.random_name()}')
    print(f'Email: {faker.random_email()}')
    print(f'Phone: {faker.random_phone()}')
    print(f'Address: {faker.random_address()}')
    print(f'Random String: {faker.random_string(12)}')
    print(f'Random Int: {faker.random_int(50, 150)}')
    print(f'Random Choice: {faker.random_choice(["Option1", "Option2", "Option3"])}')