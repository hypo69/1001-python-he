ORBIT:
=================
רמת קושי: 5
-----------------
המשחק "ORBIT" הוא משחק מבוסס טקסט בו השחקן שולט על חללית המסתחררת סביב כוכב לכת. מטרת המשחק היא להגדיר מהירות וזווית התחלתיות כך שהחללית תיכנס למסלול יציב. על השחקן לנחש את ערכי המהירות והזווית ההתחלתיות כדי להכניס את החללית למסלול. המשחק משתמש בסימולציית משיכה כבידתית לחישוב מסלול הטיסה של החללית.
כללי המשחק:
1. השחקן מזין מהירות וזווית התחלתיות עבור החללית.
2. המשחק מדמה את מסלול הטיסה של החללית תחת השפעת הכבידה.
3. אם החללית אינה יוצאת למסלול, מוצע לשחקן להזין ערכי מהירות וזווית חדשים.
4. המשחק ממשיך עד שהחללית יוצאת למסלול, או עד שמספר הניסיונות אוזל.
5. אם החללית יוצאת למסלול, המשחק מודיע על כך לשחקן.
-----------------
אלגוריתם:
1. איתחול משתנים:
   - הגדרת מספר הניסיונות ההתחלתי ל-0.
   - הגדרת מספר הניסיונות המרבי (לדוגמה, 10).
2. התחלת לולאה "כל עוד מספר הניסיונות קטן מהמספר המרבי":
    2.1. הגדלת מספר הניסיונות ב-1.
    2.2. בקשת קלט מהשחקן עבור מהירות התחלתית (V).
    2.3. בקשת קלט מהשחקן עבור זווית התחלתית (A).
    2.4. המרת הזווית ממעלות לרדיאנים.
    2.5. חישוב רכיבי המהירות ההתחלתית Vx ו-Vy (Vx = V * Cos(A), Vy = V * Sin(A)).
    2.6. הגדרת קואורדינטות התחלתיות x ו-y.
    2.7. התחלת סימולציית תנועה (לולאה):
        2.7.1. חישוב המרחק מכוכב הלכת R (R = שורש(x*x + y*y)).
        2.7.2. חישוב רכיבי התאוצה Ax ו-Ay (Ax = -x / R^3, Ay = -y / R^3).
        2.7.3. עדכון רכיבי המהירות (Vx = Vx + Ax, Vy = Vy + Ay).
        2.7.4. עדכון קואורדינטות (x = x + Vx, y = y + Vy).
        2.7.5. בדיקה האם הגוף יצא למסלול יציב (אם x^2 + y^2 בקירוב שווה ל-R^2 למשך פרק זמן מסוים).
        2.7.6. אם הגוף יצא למסלול או יצא מחוץ לגבולות, יציאה מלולאת הסימולציה.
    2.8. אם הגוף יצא למסלול יציב, הצגת הודעה "ORBIT ESTABLISHED" ומעבר לשלב 3.
    2.9. אם הגוף לא יצא למסלול, הצגת הודעה "FAILED", וחזרה על הלולאה משלב 2.
3. סוף המשחק.
-----------------
דיאגרמת זרימה:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    numberOfTries = 0<br>
    maxTries = 10
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: <code><b>numberOfTries &lt; maxTries</b></code>"}
    LoopStart -- Да --> IncreaseTries["<code><b>numberOfTries = numberOfTries + 1</b></code>"]
    IncreaseTries --> InputVelocity["Ввод начальной скорости: <code><b>initialVelocity</b></code>"]
    InputVelocity --> InputAngle["Ввод начального угла: <code><b>initialAngle</b></code>"]
    InputAngle --> CalculateVelocityComponents["<p align='left'>Вычисление:
    <code><b>
    angleInRadians = initialAngle * PI / 180<br>
    velocityX = initialVelocity * cos(angleInRadians)<br>
    velocityY = initialVelocity * sin(angleInRadians)
    </b></code></p>"]
    CalculateVelocityComponents --> InitializePosition["<p align='left'>Инициализация:
    <code><b>
    x = initialX<br>
    y = initialY
    </b></code></p>"]
    InitializePosition --> SimulationLoopStart{"Начало симуляции: пока не на орбите или не вышли за рамки"}
    SimulationLoopStart --> CalculateDistance["<p align='left'>Расчет расстояния:
        <code><b>distance = sqrt(x^2 + y^2)</b></code></p>"]
    CalculateDistance --> CalculateAcceleration["<p align='left'>Расчет ускорения:
        <code><b>
        accelerationX = -x / distance^3<br>
        accelerationY = -y / distance^3
        </b></code></p>"]
    CalculateAcceleration --> UpdateVelocity["<p align='left'>Обновление скорости:
        <code><b>
        velocityX = velocityX + accelerationX<br>
        velocityY = velocityY + accelerationY
        </b></code></p>"]
    UpdateVelocity --> UpdatePosition["<p align='left'>Обновление позиции:
        <code><b>
        x = x + velocityX<br>
        y = y + velocityY
        </b></code></p>"]
    UpdatePosition --> CheckOrbit{"Проверка: <code><b>На орбите?</b></code>"}
    CheckOrbit -- Да --> OutputOrbitEstablished["Вывод: <b>ORBIT ESTABLISHED</b>"]
    OutputOrbitEstablished --> End["Конец"]
    CheckOrbit -- Нет --> CheckOutOfBound{"Проверка: <code><b>Вышли за рамки?</b></code>"}
    CheckOutOfBound -- Да --> SimulationLoopEnd["Конец цикла симуляции"]
    CheckOutOfBound -- Нет --> SimulationLoopStart
     SimulationLoopEnd --> CheckTries{"Проверка: <code><b>numberOfTries < maxTries?</b></code>"}
    CheckTries -- Да --> LoopStart
    CheckTries -- Нет --> OutputFailed["Вывод: <b>FAILED</b>"]
    OutputFailed --> End
    LoopStart -- Нет --> End
```

**מקרא:**
    Start - התחלת התוכנית.
    InitializeVariables - איתחול משתנים: מספר הניסיונות (numberOfTries) מוגדר ל-0, ומספר הניסיונות המרבי (maxTries) מוגדר ל-10.
    LoopStart - התחלת לולאה שנמשכת כל עוד מספר הניסיונות קטן מהמקסימלי.
    IncreaseTries - הגדלת מונה מספר הניסיונות ב-1.
    InputVelocity - בקשת קלט מהמשתמש עבור המהירות ההתחלתית ושמירתה במשתנה initialVelocity.
    InputAngle - בקשת קלט מהמשתמש עבור הזווית ההתחלתית ושמירתה במשתנה initialAngle.
    CalculateVelocityComponents - חישוב רכיבי המהירות ההתחלתית: הזווית מומרת לרדיאנים, ומחושבים רכיבי velocityX ו-velocityY.
    InitializePosition - איתחול הקואורדינטות ההתחלתיות x ו-y.
    SimulationLoopStart - התחלת לולאת הסימולציה, הנמשכת כל עוד לא הושג מסלול יציב או יציאה מגבולות.
    CalculateDistance - חישוב המרחק מהאובייקט למרכז כוכב הלכת.
    CalculateAcceleration - חישוב התאוצה בצירים x ו-y, על בסיס המרחק מכוכב הלכת.
    UpdateVelocity - עדכון מהירות האובייקט על בסיס התאוצה.
    UpdatePosition - עדכון מיקום האובייקט על בסיס המהירות.
    CheckOrbit - בדיקה האם האובייקט הוכנס למסלול יציב.
    OutputOrbitEstablished - הצגת הודעה המציינת שהמסלול הוגדר.
    End - סוף התוכנית.
    CheckOutOfBound - בדיקה האם האובייקט לא יצא מגבולות המודל.
    SimulationLoopEnd - סיום לולאת הסימולציה.
    CheckTries - בדיקה האם מספר הניסיונות לא חרג מהערך המרבי.
    OutputFailed - הצגת הודעה המציינת שלא עלה בידי להיכנס למסלול.
```python
import math

# Константы для симуляции
INITIAL_X = 100  # Начальная координата X
INITIAL_Y = 0   # Начальная координата Y
TIME_STEP = 0.1   # Шаг времени для симуляции
ORBIT_TOLERANCE = 10  # Допустимое отклонение для определения стабильной орбиты
MAX_STEPS = 1000  # Максимальное количество шагов симуляции
MAX_TRIES = 10 # Максимальное количество попыток

def simulate_orbit(initial_velocity, initial_angle):
    """
    Моделирует орбиту космического корабля вокруг планеты.

    Args:
        initial_velocity (float): Начальная скорость корабля.
        initial_angle (float): Начальный угол направления корабля в градусах.

    Returns:
         bool: True, если орбита установлена; False в противном случае.
    """
    # Преобразуем угол из градусов в радианы
    angle_in_radians = math.radians(initial_angle)

    # Вычисляем компоненты начальной скорости
    velocity_x = initial_velocity * math.cos(angle_in_radians)
    velocity_y = initial_velocity * math.sin(angle_in_radians)

    # Начальные координаты
    x = INITIAL_X
    y = INITIAL_Y
    
    # Переменные для проверки стабильной орбиты
    last_distance = 0
    orbit_count = 0
    
    # Моделирование движения
    for step in range(MAX_STEPS):
        # Рассчитываем расстояние до планеты
        distance = math.sqrt(x * x + y * y)

        # Рассчитываем ускорение (гравитация)
        acceleration_x = -x / (distance ** 3)
        acceleration_y = -y / (distance ** 3)

        # Обновляем скорость
        velocity_x += acceleration_x * TIME_STEP
        velocity_y += acceleration_y * TIME_STEP

        # Обновляем позицию
        x += velocity_x * TIME_STEP
        y += velocity_y * TIME_STEP

        # Проверяем стабильность орбиты.
        if abs(distance - last_distance) < ORBIT_TOLERANCE:
           orbit_count += 1
        else:
           orbit_count = 0
        
        if orbit_count > 50: # Проверяем, что у нас 50 раз подряд расстояние не меняется.
            return True # Орбита стабильна

        last_distance = distance
        
        # Проверка выхода за рамки
        if abs(x) > 500 or abs(y) > 500 :
            return False
    
    return False # Не удалось установить орбиту
   
# Основной цикл игры
def play_orbit_game():
    """
    Запускает игру по моделированию орбиты.
    """
    
    number_of_tries = 0

    while number_of_tries < MAX_TRIES:
        number_of_tries += 1
        
        try:
            # Запрашиваем у пользователя начальную скорость и угол
            initial_velocity = float(input("Введите начальную скорость (например, 5): "))
            initial_angle = float(input("Введите начальный угол в градусах (например, 45): "))
        except ValueError:
            print("Пожалуйста, введите корректные числовые значения.")
            continue

        # Запускаем моделирование
        orbit_established = simulate_orbit(initial_velocity, initial_angle)

        if orbit_established:
            print("ORBIT ESTABLISHED")
            return  # Завершаем игру
        else:
             print("FAILED")
    print("GAME OVER")


# Запускаем игру, только если скрипт исполняется напрямую.
if __name__ == "__main__":
    play_orbit_game()

```

"""
הסבר הקוד:

1. **ייבוא המודול `math`**:
   - `import math`: מייבא את המודול `math`, המשמש לפעולות מתמטיות כמו `cos`, `sin`, `sqrt` ו-`radians`.

2. **קבועים**:
    - `INITIAL_X`, `INITIAL_Y`: קואורדינטות התחלתיות של החללית.
    - `TIME_STEP`: צעד זמן לסימולציית התנועה.
    - `ORBIT_TOLERANCE`: סטייה מותרת במרחק להגדרת מסלול יציב.
    - `MAX_STEPS`: מספר הצעדים המרבי בסימולציה, למניעת לולאה אינסופית.
    - `MAX_TRIES`: מספר הניסיונות המרבי עבור המשתמש להכניס את החללית למסלול.
    
3. **הפונקציה `simulate_orbit(initial_velocity, initial_angle)`**:
    -   `angle_in_radians = math.radians(initial_angle)`: ממירה את הזווית ממעלות לרדיאנים, מכיוון שפונקציות טריגונומטריות ב-Python עובדות עם רדיאנים.
    -   `velocity_x = initial_velocity * math.cos(angle_in_radians)`: מחשבת את רכיב המהירות ההתחלתי בציר X.
    -   `velocity_y = initial_velocity * math.sin(angle_in_radians)`: מחשבת את רכיב המהירות ההתחלתי בציר Y.
    -   `x = INITIAL_X`, `y = INITIAL_Y`: קובעת את הקואורדינטות ההתחלתיות של החללית.
    -   **לולאת הסימולציה**:
        -   `for step in range(MAX_STEPS)`: לולאה המדמה את תנועת החללית במהלך `MAX_STEPS` צעדים.
        -   `distance = math.sqrt(x * x + y * y)`: מחשבת את המרחק מהחללית למרכז כוכב הלכת.
        -   `acceleration_x = -x / (distance ** 3)`: מחשבת את התאוצה בציר X (משיכה כבידתית).
        -   `acceleration_y = -y / (distance ** 3)`: מחשבת את התאוצה בציר Y (משיכה כבידתית).
        -   `velocity_x += acceleration_x * TIME_STEP`: מעדכנת את המהירות בציר X.
        -   `velocity_y += acceleration_y * TIME_STEP`: מעדכנת את המהירות בציר Y.
        -   `x += velocity_x * TIME_STEP`: מעדכנת את קואורדינטת X.
        -   `y += velocity_y * TIME_STEP`: מעדכנת את קואורדינטת Y.
        -   **בדיקת מסלול יציב**:
            -   `if abs(distance - last_distance) < ORBIT_TOLERANCE:`: בודקים האם המרחק למרכז כוכב הלכת השתנה בערך מותר.
            -   `orbit_count += 1`: מגדילים את המונה אם המרחק בטווח הסבילות.
            -   `else: orbit_count = 0`: מאפסים את המונה אם המרחק משתנה.
            -   `if orbit_count > 50`: בודקים שהמרחק אינו משתנה ברציפות במשך 50 פעמים.
            -   `return True`: מחזירה `True`, אם החללית נכנסה למסלול יציב.
        -   `last_distance = distance`: שומרים את ערך המרחק האחרון.
        -    **בדיקת יציאה מגבולות**:
            -  `if abs(x) > 500 or abs(y) > 500`: בודקת האם החללית יצאה מחוץ לגבולות הסימולציה.
            -  `return False`: מחזירה `False`, אם החללית יצאה מגבולות.
    -  `return False`: מחזירה `False`, אם לא עלה בידי להגדיר מסלול בתוך `MAX_STEPS` צעדים.

4. **הפונקציה `play_orbit_game()`**:
    -   `number_of_tries = 0`: מאתחלת את מונה ניסיונות המשתמש.
    -   **לולאה `while number_of_tries < MAX_TRIES`**: לולאה הנמשכת כל עוד מספר הניסיונות לא הגיע ל-`MAX_TRIES`.
    -   `number_of_tries += 1`: מגדילה את מונה הניסיונות.
    -   `try...except ValueError`: טיפול בחריגות, אם המשתמש הזין ערך לא תקין.
    -   `initial_velocity = float(input("Введите начальную скорость (например, 5): "))`: מבקשת קלט מהמשתמש עבור המהירות ההתחלתית.
    -   `initial_angle = float(input("Введите начальный угол в градусах (например, 45): "))`: מבקשת קלט מהמשתמש עבור הזווית ההתחלתית במעלות.
    -   `orbit_established = simulate_orbit(initial_velocity, initial_angle)`: קוראת לפונקציה `simulate_orbit` לסימולציית המסלול.
    -   `if orbit_established: print("ORBIT ESTABLISHED"); return`: אם המסלול הוגדר, מוצגת הודעה והמשחק מסתיים.
    -   `else: print("FAILED")`: אם המסלול לא הוגדר, מוצגת הודעת כישלון.
    -   `print("GAME OVER")`: מוצג בסוף המשחק, אם לא עלה בידי להכניס למסלול בתוך `MAX_TRIES` ניסיונות.

5. **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בודקת האם הסקריפט מורץ ישירות.
    -   `play_orbit_game()`: קוראת לפונקציה `play_orbit_game` כדי להתחיל את המשחק.

"""