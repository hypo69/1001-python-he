from dataclasses import dataclass


@dataclass
class TemperatureConverter:
    """
    מחלקה להמרת טמפרטורות בין מעלות צלזיוס, פרנהייט וקלווין.
    """

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        ממיר טמפרטורה ממעלות צלזיוס למעלות פרנהייט.

        Args:
            celsius: הטמפרטורה במעלות צלזיוס.

        Returns:
            הטמפרטורה במעלות פרנהייט.
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        """
        ממיר טמפרטורה ממעלות פרנהייט למעלות צלזיוס.

        Args:
            fahrenheit: הטמפרטורה במעלות פרנהייט.

        Returns:
            הטמפרטורה במעלות צלזיוס.
        """
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    def celsius_to_kelvin(self, celsius: float) -> float:
        """
        ממיר טמפרטורה ממעלות צלזיוס לקלווין.

        Args:
            celsius: הטמפרטורה במעלות צלזיוס.

        Returns:
            הטמפרטורה בקלווין.
        """
        kelvin = celsius + 273.15
        return kelvin

    def kelvin_to_celsius(self, kelvin: float) -> float:
        """
        ממיר טמפרטורה מקלווין למעלות צלזיוס.

        Args:
            kelvin: הטמפרטורה בקלווין.

        Returns:
            הטמפרטורה במעלות צלזיוס.
        """
        celsius = kelvin - 273.15
        return celsius

    def fahrenheit_to_kelvin(self, fahrenheit: float) -> float:
        """
        ממיר טמפרטורה ממעלות פרנהייט לקלווין.

        Args:
            fahrenheit: הטמפרטורה במעלות פרנהייט.

        Returns:
            הטמפרטורה בקלווין.
        """
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        kelvin = self.celsius_to_kelvin(celsius)
        return kelvin

    def kelvin_to_fahrenheit(self, kelvin: float) -> float:
        """
        ממיר טמפרטורה מקלווין למעלות פרנהייט.

        Args:
            kelvin: הטמפרטורה בקלווין.

        Returns:
            הטמפרטורה במעלות פרנהייט.
        """
        celsius = self.kelvin_to_celsius(kelvin)
        fahrenheit = self.celsius_to_fahrenheit(celsius)
        return fahrenheit

    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        ממיר טמפרטורה מיחידת מדידה אחת לאחרת.

        Args:
            value: הטמפרטורה להמרה.
            from_unit: יחידת המדידה המקורית ('C', 'F', 'K').
            to_unit: יחידת המדידה היעד ('C', 'F', 'K').

        Returns:
            הטמפרטורה המומרת.

        Raises:
            ValueError: אם צוינו יחידות מדידה שגויות.
        """
        if from_unit == to_unit:
            return value  # אין צורך בהמרה

        if from_unit == 'C':
            if to_unit == 'F':
                return self.celsius_to_fahrenheit(value)
            elif to_unit == 'K':
                return self.celsius_to_kelvin(value)
        elif from_unit == 'F':
            if to_unit == 'C':
                return self.fahrenheit_to_celsius(value)
            elif to_unit == 'K':
                return self.fahrenheit_to_kelvin(value)
        elif from_unit == 'K':
            if to_unit == 'C':
                return self.kelvin_to_celsius(value)
            elif to_unit == 'F':
                return self.kelvin_to_fahrenheit(value)

        raise ValueError("יחידות מדידה שגויות.")


def main():
    """
    פונקציה ראשית לאינטראקציה עם המשתמש.
    """
    converter = TemperatureConverter()

    while True:
        print("\nבחר פעולה:")
        print("1. המרת טמפרטורה")
        print("2. יציאה")

        choice = input("הזן מספר פעולה: ")

        if choice == '1':
            try:
                value = float(input("הזן טמפרטורה: "))
                from_unit = input("הזן את יחידת המדידה המקורית (C, F, K): ").upper()
                to_unit = input("הזן את יחידת המדידה היעד (C, F, K): ").upper()

                result = converter.convert_temperature(value, from_unit, to_unit)
                print(f"תוצאה: {result:.2f} {to_unit}")

            except ValueError as e:
                print(f"שגיאה: {e}")
            except Exception as e:
                 print(f"שגיאה בלתי צפויה: {e}")


        elif choice == '2':
            print("להתראות!")
            break
        else:
            print("קלט שגוי. נסה שוב.")


if __name__ == "__main__":
    main()