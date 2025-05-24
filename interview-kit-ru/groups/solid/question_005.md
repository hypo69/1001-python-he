### `question_005.md` (OCP - הפרה)

**שאלה 005.** באיזו מבין דוגמאות הקוד הבאות ב-Python מופר עקרון הפתיחות/סגירות (OCP) באופן *המובהק ביותר*?

A.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass
```

B.

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
```

C.

```python
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            # Code to process credit card payment
            pass
        elif payment_type == "paypal":
            # Code to process PayPal payment
            pass
        elif payment_type == "stripe":
            # Code to process Stripe payment
            pass
        else:
            raise ValueError("Invalid payment type")
```

D.

```python
class ReportGenerator:
    def generate_report(self, data, format):
        if format == "pdf":
            # Code to generate PDF report
            pass
        elif format == "csv":
            # Code to generate CSV report
            pass
```

**תשובה נכונה: C**

**הסבר:**

עקרון הפתיחות/סגירות (OCP) קובע שסגנונות (classes) צריכים להיות פתוחים להרחבה, אך סגורים לשינוי. באפשרות C, הסגנון `PaymentProcessor` *מפר את OCP*, מכיוון שהוספת שיטת תשלום חדשה תדרוש *לשנות* את הקוד הקיים של הסגנון `PaymentProcessor`.

*   **אפשרות A:** לסגנון אין מימושים.
*   **אפשרות B:** קיימת הרחבת סגנון, ללא שינוי סגנון האב.
*   **אפשרות C:** הסגנון `PaymentProcessor` *מפר את OCP*.
*   **אפשרות D:** הסגנון `ReportGenerator` *מפר את OCP*.

**דוגמת ריפקטור (עבור PaymentProcessor):**

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        # Code to process credit card payment
        pass

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        # Code to process PayPal payment
        pass

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount):
        payment_method.process_payment(amount)
```

**כתוצאה מכך:**

סגנונות ויישויות צריכים להיות מתוכננים כך שניתן יהיה להוסיף התנהגות חדשה ללא שינוי הקוד הקיים.

לפיכך, אפשרות C היא הנכונה.