# מחשבון טמפרטורה ב-Python

פרויקט זה מכיל שתי גרסאות של יישום מחשבון טמפרטורה שיכול להמיר ערכים בין מעלות צלזיוס, פרנהייט וקלוין.

## קבצי הפרויקט

1.  **`convertor_kcf.py`**: יישום מחשבון הטמפרטורה באמצעות פונקציות נפרדות.
2.  **`convertor_kcf_dataclass.py`**: יישום מחשבון הטמפרטורה באמצעות `dataclass`.
3.  **`readme.md`**: קובץ זה עם תיאור הפרויקט.

## תיאור `convertor_kcf.py`

קובץ זה מכיל את היישום של מחשבון טמפרטורה באמצעות פונקציות נפרדות. הקוד מחולק למספר בלוקים:

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

-   **אננוטציית טיפוסים:** `(celsius: float) -> float` מציין את טיפוס הארגומנט וטיפוס הערך המוחזר.
-   **Docstring:** מחרוזת תיעוד המתארת את מטרת הפונקציה, הארגומנטים והערך המוחזר.
-   **לוגיקה:** הפונקציה מבצעת את ההמרה לפי הנוסחאות הידועות.

### 2. פונקציית המרה אוניברסלית

```python
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
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

    raise ValueError("יחידות מדידה שגויות.")
```

פונקציה זו מקבלת ערך טמפרטורה, יחידת המדידה המקורית ויחידת המדידה היעד. על בסיס פרמטרים אלו, היא קוראת לפונקציית ההמרה המתאימה. אם יחידות המדידה זהות, היא מחזירה את הערך המקורי. אם הועברו יחידות מדידה שגויות, היא מעוררת `ValueError`.

### 3. פונקציה `main`

```python
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
                from_unit = input("הזן את יחידת המדידה המקורית (C, F, K): ").upper()
                to_unit = input("הזן את יחידת המדידה היעד (C, F, K): ").upper()

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
            print("קלט שגוי. נסה שוב.")

if __name__ == "__main__":
    main()
```

פונקציית `main` מכילה לולאה אינסופית שבה מוצע למשתמש לבחור פעולה. אם המשתמש בוחר המרה, התוכנית מבקשת את ערך הטמפרטורה, יחידת המדידה המקורית ויחידת המדידה היעד, קוראת לפונקציה `convert_temperature` ומציגה את התוצאה. כמו כן, אנו מטפלים בשגיאות קלט אפשריות באמצעות בלוק `try-except`.

## תיאור `convertor_kcf_dataclass.py`

קובץ זה מכיל את היישום של מחשבון הטמפרטורה באמצעות `dataclass`.

### 1. ה-`dataclass` `TemperatureConverter`

```python
from dataclasses import dataclass

@dataclass
class TemperatureConverter:
    """
    מחלקה להמרת טמפרטורות בין מעלות צלזיוס, פרנהייט וקלוין.
    """

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        ... # הגדרת שיטות ההמרה
```

-   **ייבוא `dataclass`:** אנו מייבאים את הדקורטור `dataclass` מהמודול `dataclasses`.
-   **מחלקה `TemperatureConverter`:** אנו יוצרים את המחלקה `TemperatureConverter` ומקשטים אותה באמצעות `@dataclass`. זה ייצור אוטומטית את הפונקציה הבונה (constructor) ושיטות נוספות הנדרשות למחלקה.
-   **שיטות המחלקה:** כל פונקציות ההמרה שלנו הן כעת שיטות של המחלקה `TemperatureConverter`. הפרמטר הראשון `self` מצביע על מופע המחלקה.

שיטות ההמרה דומות לשיטות ב-`convertor_kcf.py`, למעט העובדה שהן שיטות מחלקה ומקבלות `self` כארגומנט הראשון.

### 2. פונקציה `convert_temperature`

```python
    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        ... # קריאה לשיטות המחלקה
```

פונקציה זו, בדומה ל-`convertor_kcf.py`, מקבלת ערך טמפרטורה, יחידת המדידה המקורית ויחידת המדידה היעד. אך כעת היא קוראת לשיטות של המחלקה `TemperatureConverter`.

### 3. פונקציה `main`

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

בפונקציה `main` אנו יוצרים מופע של המחלקה `TemperatureConverter` בשם `converter`. כעת אנו קוראים לשיטות ההמרה דרך מופע זה, למשל: `converter.convert_temperature()`.

## השוואת שתי הגישות

-   **`convertor_kcf.py`:** פונקציות ההמרה קיימות באופן עצמאי זו מזו, מה שיכול להיות פחות מאורגן עבור תוכניות מורכבות יותר.
-   **`convertor_kcf_dataclass.py`:** כל פונקציות ההמרה מקובצות במחלקה, מה שהופך את הקוד למודולרי וקריא יותר. `dataclass` גם מספק יצירה אוטומטית של פונקציה בונה ושיטות נוספות.

## הפעלת הקוד

כדי להפעיל כל אחד מהקבצים, ודא שמותקן לך Python. לאחר מכן הרץ בטרמינל:

```bash
python convertor_kcf.py
```

או

```bash
python convertor_kcf_dataclass.py
```

שתי הגישות פותרות את אותה בעיה, אך משתמשות בדרכים שונות לארגון הקוד. `dataclass` מאפשר גישה מובנית יותר לפתרון הבעיה ומפשט את התחזוקה וההרחבה של הקוד.