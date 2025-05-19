def celsius_to_fahrenheit(celsius: float) -> float:
    """
    ממיר טמפרטורה ממעלות צלזיוס למעלות פרנהייט.

    Args:
        celsius: הטמפרטורה במעלות צלזיוס.

    Returns:
        הטמפרטורה במעלות פרנהייט.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    ממיר טמפרטורה ממעלות פרנהייט למעלות צלזיוס.

    Args:
        fahrenheit: הטמפרטורה במעלות פרנהייט.

    Returns:
        הטמפרטורה במעלות צלזיוס.
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    """
    ממיר טמפרטורה ממעלות צלזיוס לקלווינים.

    Args:
        celsius: הטמפרטורה במעלות צלזיוס.

    Returns:
        הטמפרטורה בקלווינים.
    """
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin: float) -> float:
    """
    ממיר טמפרטורה מקלווינים למעלות צלזיוס.

    Args:
        kelvin: הטמפרטורה בקלווינים.

    Returns:
        הטמפרטורה במעלות צלזיוס.
    """
    celsius = kelvin - 273.15
    return celsius


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    ממיר טמפרטורה ממעלות פרנהייט לקלווינים.

    Args:
        fahrenheit: הטמפרטורה במעלות פרנהייט.

    Returns:
        הטמפרטורה בקלווינים.
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    ממיר טמפרטורה מקלווינים למעלות פרנהייט.

    Args:
        kelvin: הטמפרטורה בקלווינים.

    Returns:
        הטמפרטורה במעלות פרנהייט.
    """
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    ממיר טמפרטורה מיחידת מידה אחת לאחרת.

    Args:
        value: הטמפרטורה המיועדת להמרה.
        from_unit: יחידת המידה המקורית ('C', 'F', 'K').
        to_unit: יחידת המידה היעד ('C', 'F', 'K').

    Returns:
        הטמפרטורה שהומרה.

    Raises:
        ValueError: אם צוינו יחידות מידה שגויות.
    """
    if from_unit == to_unit:
        return value  # אין צורך בהמרה

    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(value)
    elif from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        elif to_unit == 'F':
            return kelvin_to_fahrenheit(value)

    raise ValueError("יחידות מידה שגויות.")


def main():
    """
    הפונקציה הראשית לאינטראקציה עם המשתמש.
    """
    while True:
        print("\nבחר פעולה:")
        print("1. המרת טמפרטורה")
        print("2. יציאה")

        choice = input("הזן מספר פעולה: ")

        if choice == '1':
            try:
                value = float(input("הזן טמפרטורה: "))
                from_unit = input("הזן יחידת מידה מקורית (C, F, K): ").upper()
                to_unit = input("הזן יחידת מידה יעד (C, F, K): ").upper()

                result = convert_temperature(value, from_unit, to_unit)
                print(f"תוצאה: {result:.2f} {to_unit}")

            except ValueError as e:
                print(f"שגיאה: {e}")
            except Exception as e:
                 print(f"שגיאה בלתי צפויה: {e}")


        elif choice == '2':
            print("להתראות!")
            break
        else:
            print("קלט שגוי. אנא נסה שוב.")


if __name__ == "__main__":
    main()