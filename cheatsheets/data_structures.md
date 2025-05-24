**1. רשימות (Lists)**

*   **הגדרה:** רשימות ב-Python הן אוספים סדורים, הניתנים לשינוי, של איברים. משמעות הדבר היא שניתן להוסיף, למחוק ולשנות איברים ברשימה, ולסדר האיברים יש חשיבות.
*   **ייצוג:** רשימות נוצרות באמצעות סוגריים מרובעים `[]`, והאיברים מופרדים בפסיקים.

*   **דוגמאות:**

    ```python
    # Создание списка
    # יצירת רשימה
    boris_list = ["Борис", "Москва", 30, "инженер"]
    print(f"Создание списка: {boris_list}")
    # יצירת רשימה:
    print(f"יצירת רשימה: {boris_list}")

    # Доступ по индексу
    # גישה לפי אינדקס
    print(f"Элемент по индексу 0: {boris_list[0]}")
    # איבר באינדקס 0:
    print(f"איבר באינדקס 0: {boris_list[0]}")

    # Изменение элемента
    # שינוי איבר
    boris_list[2] = 31
    print(f"Изменение элемента: {boris_list}")
    # שינוי איבר:
    print(f"שינוי איבר: {boris_list}")

    # Добавление элемента в конец
    # הוספת איבר לסוף
    boris_list.append("женат")
    print(f"Добавление в конец: {boris_list}")
    # הוספה לסוף:
    print(f"הוספה לסוף: {boris_list}")

    # Вставка элемента по индексу
    # הוספת איבר לפי אינדקס
    boris_list.insert(1, "Россия")
    print(f"Вставка элемента: {boris_list}")
    # הוספת איבר:
    print(f"הוספת איבר: {boris_list}")

    # Удаление элемента по значению
    # מחיקת איבר לפי ערך
    boris_list.remove("инженер")
    print(f"Удаление элемента по значению: {boris_list}")
    # מחיקת איבר לפי ערך:
    print(f"מחיקת איבר לפי ערך: {boris_list}")

    # Удаление элемента по индексу
    # מחיקת איבר לפי אינדקס
    del boris_list[2]
    print(f"Удаление элемента по индексу: {boris_list}")
    # מחיקת איבר לפי אינדקס:
    print(f"מחיקת איבר לפי אינדקס: {boris_list}")

    # Расширение списка другим списком
    # הרחבת רשימה ברשימה אחרת
    boris_list.extend(["хобби", "рыбалка"])
    print(f"Расширение списка: {boris_list}")
    # הרחבת רשימה:
    print(f"הרחבת רשימה: {boris_list}")

    # Удаление элемента с конца
    # מחיקת איבר מהסוף
    boris_list.pop()
    print(f"Удаление элемента с конца: {boris_list}")
    # מחיקת איבר מהסוף:
    print(f"מחיקת איבר מהסוף: {boris_list}")

    ```

**2. מילונים (Dictionaries)**

*   **הגדרה:** מילונים ב-Python הם אוספים בלתי סדורים של איברים, כאשר כל איבר מורכב מזוג "מפתח-ערך".
*   **ייצוג:** מילונים נוצרים באמצעות סוגריים מסולסלים `{}`, וזוגות "מפתח-ערך" מופרדים בנקודתיים `:`.

*   **דוגמאות:**
    ```python
    # Создание словаря
    # יצירת מילון
    alice_dict = {"name": "Алиса", "age": 25, "city": "Лондон", "occupation": "художница"}
    print(f"Создание словаря: {alice_dict}")
    # יצירת מילון:
    print(f"יצירת מילון: {alice_dict}")

    # Доступ по ключу
    # גישה לפי מפתח
    print(f"Значение по ключу 'name': {alice_dict['name']}")
    # ערך לפי מפתח 'name':
    print(f"ערך לפי מפתח 'name': {alice_dict['name']}")

    # Изменение значения
    # שינוי ערך
    alice_dict["age"] = 26
    print(f"Изменение значения: {alice_dict}")
    # שינוי ערך:
    print(f"שינוי ערך: {alice_dict}")

    # Добавление пары ключ-значение
    # הוספת זוג מפתח-ערך
    alice_dict["hobby"] = "рисование"
    print(f"Добавление пары: {alice_dict}")
    # הוספת זוג:
    print(f"הוספת זוג: {alice_dict}")

    # Удаление пары по ключу
    # מחיקת זוג לפי מפתח
    del alice_dict["city"]
    print(f"Удаление пары: {alice_dict}")
    # מחיקת זוג:
    print(f"מחיקת זוג: {alice_dict}")

    # Удаление пары методом pop (с возвращением значения)
    # מחיקת זוג באמצעות מתודת pop (עם החזרת הערך)
    hobby = alice_dict.pop("hobby")
    print(f"Удаление с возвратом значения: {alice_dict}, значение: {hobby}")
    # מחיקה עם החזרת ערך:
    print(f"מחיקה עם החזרת ערך: {alice_dict}, ערך: {hobby}")

    # Проверка наличия ключа
    # בדיקת קיום מפתח
    print(f"Наличие ключа 'name': {'name' in alice_dict}")
    # קיום מפתח 'name':
    print(f"קיום מפתח 'name': {'name' in alice_dict}")
    ```

**3. טאפלים (Tuples)**

*   **הגדרה:** טאפלים ב-Python הם אוספים סדורים, **בלתי ניתנים לשינוי**, של איברים.
*   **ייצוג:** טאפלים נוצרים באמצעות סוגריים עגולים `()`, והאיברים מופרדים בפסיקים.

*   **דוגמאות:**

    ```python
    # Создание кортежа
    # יצירת טאפל
    boris_tuple = ("Борис", "Москва", 30, "инженер")
    print(f"Создание кортежа: {boris_tuple}")
    # יצירת טאפל:
    print(f"יצירת טאפל: {boris_tuple}")

    # Доступ по индексу
    # גישה לפי אינדקס
    print(f"Элемент по индексу 2: {boris_tuple[2]}")
    # איבר באינדקס 2:
    print(f"איבר באינדקס 2: {boris_tuple[2]}")

    # Нельзя изменить элемент
    # לא ניתן לשנות איבר
    # boris_tuple[0] = "Борис" # Это вызовет ошибку: TypeError: 'tuple' object does not support item assignment
    # boris_tuple[0] = "Борис" # פעולה זו תגרום לשגיאה: TypeError: 'tuple' object does not support item assignment

    # Нельзя добавить элемент
    # לא ניתן להוסיף איבר
    # boris_tuple.append(4) # Это вызовет ошибку: AttributeError: 'tuple' object has no attribute 'append'
    # boris_tuple.append(4) # פעולה זו תגרום לשגיאה: AttributeError: 'tuple' object has no attribute 'append'

    # Нельзя удалить элемент
    # לא ניתן למחוק איבר
    # del boris_tuple[0]  # Это вызовет ошибку: TypeError: 'tuple' object doesn't support item deletion
    # del boris_tuple[0]  # פעולה זו תגרום לשגיאה: TypeError: 'tuple' object doesn't support item deletion
    ```

**4. SimpleNamespace**

*   **הגדרה:** `SimpleNamespace` מהמודול `types` הוא מחלקה פשוטה המאפשרת יצירת אובייקטים שתכונותיהם (מאפייניהם) ניתנות להגדרה הן בעת היצירה והן לאחר מכן.
*   **ייצוג:** ליצירת אובייקט `SimpleNamespace` יש לייבא אותו מתוך `types` ולהעביר אליו ארגומנטים בעלי שם (או לא להעביר כלל):
     ```python
    from types import SimpleNamespace

    alice_namespace = SimpleNamespace(name="Алиса", age=25, city="Лондон")
    ```
*  **מאפיינים:**
    *  מאפשר ליצור אובייקטים עם תכונות דינמיות (בדומה למילון).
    *  נוח ליצירת אובייקטים פשוטים לצורך אחסון נתונים.
    *  התכונות נגישות באמצעות נקודה, כמו באובייקטים רגילים: `alice_namespace.name`
    *  בניגוד למילונים, סדר התכונות נשמר.
    *  ניתן לשנות את הערכים של התכונות, אך לא ניתן להוסיף תכונות חדשות באופן ישיר.

*  **דוגמאות:**
    ```python
    from types import SimpleNamespace

    # Создание SimpleNamespace
    # יצירת SimpleNamespace
    alice_namespace = SimpleNamespace(name="Алиса", age=25, city="Лондон")
    print(f"Создание SimpleNamespace: {alice_namespace}")
    # יצירת SimpleNamespace:
    print(f"יצירת SimpleNamespace: {alice_namespace}")

    # Доступ к атрибуту
    # גישה לתכונה
    print(f"Атрибут 'name': {alice_namespace.name}")
    # תכונה 'name':
    print(f"תכונה 'name': {alice_namespace.name}")

    # Изменение атрибута
    # שינוי תכונה
    alice_namespace.age = 26
    print(f"Изменение атрибута: {alice_namespace}")
    # שינוי תכונה:
    print(f"שינוי תכונה: {alice_namespace}")

    # Нельзя добавить новый атрибут
    # לא ניתן להוסיף תכונה חדשה באופן ישיר
    # alice_namespace.occupation = "художница" # Это вызовет ошибку: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'
    # alice_namespace.occupation = "художница" # פעולה זו תגרום לשגיאה: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

   # Добавление через setattr
   # הוספה באמצעות setattr
    setattr(alice_namespace, "occupation", "художница")
    print(f"Добавление атрибута: {alice_namespace}")
    # הוספת תכונה:
    print(f"הוספת תכונה: {alice_namespace}")

    # Удаление через delattr
    # מחיקה באמצעות delattr
    delattr(alice_namespace, "city")
    print(f"Удаление атрибута: {alice_namespace}")
    # מחיקת תכונה:
    print(f"מחיקת תכונה: {alice_namespace}")
    ```