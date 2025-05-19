להלן תרגום המסמך מרוסית לעברית, בהתאם להנחיות שסופקו:

**1. רשימות (Lists)**

*   **הגדרה:** רשימות ב-Python הן אוספים של איברים סדורות וניתנות לשינוי. משמעות הדבר היא שניתן להוסיף, להסיר ולשנות איברים ברשימה, ולסדר האיברים יש חשיבות.
*   **ייצוג:** רשימות נוצרות באמצעות סוגריים מרובעים `[]`, והאיברים מופרדים בפסיקים.

*   **דוגמאות:**

    ```python
    # יצירת רשימה
    boris_list = ["Борис", "Москва", 30, "инженер"]
    print(f"יצירת רשימה: {boris_list}")

    # גישה לפי אינדקס
    print(f"איבר באינדקס 0: {boris_list[0]}")

    # שינוי איבר
    boris_list[2] = 31
    print(f"שינוי איבר: {boris_list}")

    # הוספת איבר בסוף
    boris_list.append("женат")
    print(f"הוספה בסוף: {boris_list}")

    # הוספת איבר לפי אינדקס
    boris_list.insert(1, "Россия")
    print(f"הוספת איבר: {boris_list}")

    # הסרת איבר לפי ערך
    boris_list.remove("инженер")
    print(f"הסרת איבר לפי ערך: {boris_list}")

    # הסרת איבר לפי אינדקס
    del boris_list[2]
    print(f"הסרת איבר לפי אינדקס: {boris_list}")

    # הרחבת רשימה באמצעות רשימה אחרת
    boris_list.extend(["хобби", "рыбалка"])
    print(f"הרחבת רשימה: {boris_list}")

    # הסרת איבר מהסוף
    boris_list.pop()
    print(f"הסרת איבר מהסוף: {boris_list}")

    ```

**2. מילונים (Dictionaries)**

*   **הגדרה:** מילונים ב-Python הם אוספים של איברים בלתי סדורות, כאשר כל איבר מורכב מזוג של "מפתח-ערך".
*   **ייצוג:** מילונים נוצרים באמצעות סוגריים מסולסלים `{}`, וזוגות "מפתח-ערך" מופרדים בנקודתיים `:`.

*   **דוגמאות:**
    ```python
    # יצירת מילון
    alice_dict = {"name": "Алиса", "age": 25, "city": "Лондон", "occupation": "художница"}
    print(f"יצירת מילון: {alice_dict}")

    # גישה לפי מפתח
    print(f"ערך עבור המפתח 'name': {alice_dict['name']}")

    # שינוי ערך
    alice_dict["age"] = 26
    print(f"שינוי ערך: {alice_dict}")

    # הוספת זוג מפתח-ערך
    alice_dict["hobby"] = "рисование"
    print(f"הוספת זוג: {alice_dict}")

    # הסרת זוג לפי מפתח
    del alice_dict["city"]
    print(f"הסרת זוג: {alice_dict}")

    # הסרה זוג באמצעות שיטת pop (עם החזרת הערך)
    hobby = alice_dict.pop("hobby")
    print(f"הסרה עם החזרת ערך: {alice_dict}, ערך: {hobby}")

    # בדיקת קיום מפתח
    print(f"קיום מפתח 'name': {'name' in alice_dict}")
    ```

**3. מבני Tuple (Tuples)**

*   **הגדרה:** מבני Tuple ב-Python הם אוספים של איברים סדורות ו**בלתי ניתנות לשינוי**.
*   **ייצוג:** מבני Tuple נוצרים באמצעות סוגריים עגולים `()`, והאיברים מופרדים בפסיקים.

*   **דוגמאות:**

    ```python
    # יצירת tuple
    boris_tuple = ("Борис", "Москва", 30, "инженер")
    print(f"יצירת tuple: {boris_tuple}")

    # גישה לפי אינדקס
    print(f"איבר באינדקס 2: {boris_tuple[2]}")

    # לא ניתן לשנות איבר
    # boris_tuple[0] = "Борис" # זה יגרום לשגיאה: TypeError: 'tuple' object does not support item assignment

    # לא ניתן להוסיף איבר
    # boris_tuple.append(4) # זה יגרום לשגיאה: AttributeError: 'tuple' object has no attribute 'append'

    # לא ניתן להסיר איבר
    # del boris_tuple[0]  # זה יגרום לשגיאה: TypeError: 'tuple' object doesn't support item deletion
    ```

**4. SimpleNamespace**

*   **הגדרה:** `SimpleNamespace` מהמודול `types` היא מחלקה פשוטה המאפשרת יצירת אובייקטים שבהם ניתן להגדיר מאפיינים (attributes) הן בזמן היצירה והן לאחר מכן.
*   **ייצוג:** ליצירת אובייקט `SimpleNamespace` יש לייבא אותה מתוך `types` ולהעביר לה ארגומנטים בשם (או לא להעביר כלל):
     ```python
    from types import SimpleNamespace

    alice_namespace = SimpleNamespace(name="Алиса", age=25, city="Лондон")
    ```
*  **מאפיינים מיוחדים:**
    *  מאפשר יצירת אובייקטים עם מאפיינים דינמיים (בדומה למילון).
    *  נוח ליצירת אובייקטים פשוטים לאחסון נתונים.
    *  המאפיינים נגישים באמצעות נקודה, כמו באובייקטים רגילים: `alice_namespace.name`
    *  בשונה ממילונים, סדר המאפיינים נשמר.
    *  ניתן לשנות שדות קיימים, אך לא ניתן להוסיף שדות חדשים באמצעות השמה ישירה (`obj.new_field = value`). הוספה אפשרית באמצעות `setattr`.

*  **דוגמאות:**
    ```python
    from types import SimpleNamespace

    # יצירת SimpleNamespace
    alice_namespace = SimpleNamespace(name="Алиса", age=25, city="Лондон")
    print(f"יצירת SimpleNamespace: {alice_namespace}")

    # גישה למאפיין
    print(f"מאפיין 'name': {alice_namespace.name}")

    # שינוי מאפיין
    alice_namespace.age = 26
    print(f"שינוי מאפיין: {alice_namespace}")

    # לא ניתן להוסיף מאפיין חדש באמצעות השמה ישירה
    # alice_namespace.occupation = "художница" # זה יגרום לשגיאה: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

   # הוספה באמצעות setattr
    setattr(alice_namespace, "occupation", "художница")
    print(f"הוספת מאפיין: {alice_namespace}")

    # הסרה באמצעות delattr
    delattr(alice_namespace, "city")
    print(f"הסרת מאפיין: {alice_namespace}")
    ```