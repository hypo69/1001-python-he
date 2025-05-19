# מחשבון טמפרטורה ב-Python

פרויקט זה מכיל שתי גרסאות מימוש של מחשבון טמפרטורה, המסוגל להמיר ערכים בין מעלות צלזיוס, פרנהייט וקלווין.

## קובצי הפרויקט

1.  **`convertor_kcf.py`**: מימוש של מחשבון הטמפרטורה תוך שימוש בפונקציות נפרדות.
2.  **`convertor_kcf_dataclass.py`**: מימוש של מחשבון הטמפרטורה תוך שימוש ב-`dataclass`.
3.  **`readme.md`**: קובץ זה המכיל את תיאור הפרויקט.

## תיאור `convertor_kcf.py`

קובץ זה מכיל את המימוש של מחשבון הטמפרטורה תוך שימוש בפונקציות נפרדות. הקוד מחולק למספר בלוקים:

### 1. פונקציות המרה

בבלוק זה מוגדרות הפונקציות העיקריות להמרת טמפרטורה בין יחידות מידה שונות:

```python
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
    ממיר טמפרטורה ממעלות צלזיוס לקלווין.

    Args:
        celsius: הטמפרטורה במעלות צלזיוס.

    Returns:
        הטמפרטורה בקלווין.
    """
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin: float) -> float:
    """
    ממיר טמפרטורה מקלווין למעלות צלזיוס.

    Args:
        kelvin: הטמפרטורה בקלווין.

    Returns:
        הטמפרטורה במעלות צלזיוס.
    """
    celsius = kelvin - 273.15
    return celsius


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    ממיר טמפרטורה ממעלות פרנהייט לקלווין.

    Args:
        fahrenheit: הטמפרטורה במעלות פרנהייט.

    Returns:
        הטמפרטורה בקלווין.
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    ממיר טמפרטורה מקלווין למעלות פרנהייט.

    Args:
        kelvin: הטמפרטורה בקלווין.

    Returns:
        הטמפרטורה במעלות פרנהייט.
    """
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit
```

לכל פונקציה יש:

-   **אנוטציית טיפוסים:** `(celsius: float) -> float` מציינת את טיפוס הארגומנט ואת הטיפוס של הערך המוחזר.
-   **Docstring:** מחרוזת תיעוד המתארת את ייעוד הפונקציה, הארגומנטים והערך המוחזר.
-   **לוגיקה:** הפונקציה מבצעת את ההמרה על פי הנוסחאות הידועות.

### 2. פונקציית המרה אוניברסלית

```python
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    ממיר טמפרטורה מיחידת מידה אחת לאחרת.

    Args:
        value: הטמפרטורה להמרה.
        from_unit: יחידת המקור ('C', 'F', 'K').
        to_unit: יחידת היעד ('C', 'F', 'K').

    Returns:
        הטמפרטורה המומרה.

    Raises:
        ValueError: אם צוינו יחידות מידה לא תקינות.
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

    raise ValueError("יחידות מידה לא תקינות.")
```

פונקציה זו מקבלת ערך טמפרטורה, יחידת המקור ויחידת היעד. בהתבסס על פרמטרים אלו, היא קוראת לפונקציית ההמרה המתאימה. אם יחידות המידה זהות, היא מחזירה את הערך המקורי. אם הועברו יחידות מידה לא תקינות, היא מעוררת `ValueError`.

### 3. פונקציית `main`

```python
def main():
    """
    הפונקציה הראשית לאינטראקציה עם המשתמש.
    """
    while True:
        print("\nבחר פעולה:")
        print("1. המרת טמפרטורה")
        print("2. יציאה")

        choice = input("הכנס את מספר הפעולה: ")

        if choice == '1':
            try:
                value = float(input("הכנס טמפרטורה: "))
                from_unit = input("הכנס יחידת מקור (C, F, K): ").upper()
                to_unit = input("הכנס יחידת יעד (C, F, K): ").upper()

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
            print("קלט לא תקין. נסה שוב.")

if __name__ == "__main__":
    main()
```

הפונקציה `main` מכילה לולאה אינסופית שבה מוצע למשתמש לבחור פעולה. אם המשתמש בוחר המרה, התוכנית מבקשת את ערך הטמפרטורה, יחידת המקור ויחידת היעד, קוראת לפונקציה `convert_temperature` ומדפיסה את התוצאה. בנוסף, אנו מטפלים בשגיאות קלט אפשריות באמצעות בלוק `try-except`.

## תיאור `convertor_kcf_dataclass.py`

קובץ זה מכיל את המימוש של מחשבון הטמפרטורה תוך שימוש ב-`dataclass`.

### 1. ה-`dataclass` `TemperatureConverter`

```python
from dataclasses import dataclass

@dataclass
class TemperatureConverter:
    """
    מחלקה להמרת טמפרטורות בין מעלות צלזיוס, פרנהייט וקלווין.
    """

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        ... # הגדרת מתודות ההמרה
```

-   **ייבוא `dataclass`:** אנו מייבאים את הדקורטור `dataclass` מהמודול `dataclasses`.
-   **מחלקה `TemperatureConverter`:** אנו יוצרים את המחלקה `TemperatureConverter` ומקשטים אותה באמצעות `@dataclass`. זה ייצור באופן אוטומטי בנאי ומתודות נחוצות אחרות עבור המחלקה.
-   **מתודות המחלקה:** כל פונקציות ההמרה שלנו הן כעת מתודות של המחלקה `TemperatureConverter`. הפרמטר הראשון `self` מציין את מופע המחלקה.

מתודות ההמרה דומות למתודות בקובץ `convertor_kcf.py`, למעט העובדה שהן מתודות מחלקה ומקבלות את `self` כארגומנט ראשון.

### 2. פונקציית `convert_temperature`

```python
    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        ... # קריאה למתודות המחלקה
```

פונקציה זו, בדומה לקובץ `convertor_kcf.py`, מקבלת ערך טמפרטורה, יחידת המקור ויחידת היעד. אך כעת היא קוראת למתודות של המחלקה `TemperatureConverter`.

### 3. פונקציית `main`

```python
def main():
    """
    הפונקציה הראשית לאינטראקציה עם המשתמש.
    """
    converter = TemperatureConverter()

    while True:
       ... # אינטראקציה עם המשתמש
            result = converter.convert_temperature(value, from_unit, to_unit)
        ...
```

בפונקציה `main`, אנו יוצרים מופע של המחלקה `TemperatureConverter` בשם `converter`. כעת אנו קוראים למתודות ההמרה דרך מופע זה, למשל: `converter.convert_temperature()`.

## השוואת שתי הגישות

-   **`convertor_kcf.py`:** פונקציות ההמרה קיימות באופן עצמאי זו מזו, דבר שעשוי להיות פחות מאורגן בתוכניות מורכבות יותר.
-   **`convertor_kcf_dataclass.py`:** כל פונקציות ההמרה מקובצות במחלקה אחת, מה שהופך את הקוד למודולרי וקריא יותר. `dataclass` גם מספק יצירה אוטומטית של בנאי ומתודות נוספות.

## הרצת הקוד

כדי להריץ כל אחד מהקבצים, וודא ש-Python מותקן אצלך. לאחר מכן, הרץ במסוף:

```bash
python convertor_kcf.py
```

או

```bash
python convertor_kcf_dataclass.py
```

שתי הגישות פותרות את אותה בעיה, אך תוך שימוש בדרכים שונות לארגון הקוד. `dataclass` מאפשר גישה מובנית יותר לפתרון הבעיה ומפשט את התחזוקה והרחבת הקוד.