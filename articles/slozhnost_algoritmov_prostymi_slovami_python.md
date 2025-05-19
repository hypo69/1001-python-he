## מורכבות אלגוריתמים במילים פשוטות ועם דוגמאות ב-Python

בתכנות קיימות דרכים רבות לפתור את אותה בעיה. אולם, לא כל הפתרונות יעילים במידה שווה. אחד ההיבטים המרכזיים שיש לשקול בעת פיתוח אלגוריתמים הוא המורכבות שלהם. הבנת מורכבות של אלגוריתם מאפשרת להעריך כמה מהר הוא יפעל וכמה משאבים (למשל, זיכרון) יידרשו לביצועו, במיוחד ככל שנפח נתוני הקלט גדל. הבנת מורכבות אלגוריתמים היא מיומנות יסוד המאפשרת לכתוב קוד יעיל יותר.

### מהי מורכבות אלגוריתם?

דמיינו שיש לכם משימה: למצוא שם ספציפי בספר טלפונים.

*   **דרך פשוטה (חיפוש לינארי):** אתם לוקחים את הספר ומתחילים לדפדף בו דף אחר דף, עד שתמצאו את השם המבוקש. אם השם נמצא בסוף הספר, תצטרכו לדפדף בכל הספר!
*   **דרך חכמה (חיפוש בינארי):** אתם פותחים את הספר באמצע. אם השם שאתם מחפשים מופיע לפני השם שבדף זה, אתם סוגרים את המחצית השנייה של הספר ומחפשים במחצית הראשונה. אם השם מופיע מאוחר יותר, אתם מחפשים במחצית השנייה. אתם חוזרים על פעולה זו עד שתמצאו את השם המבוקש. בכל צעד אתם נפטרים ממחצית הספר!

**מורכבות אלגוריתם** היא דרך לתאר כמה "זמן" (או משאבים, כמו זיכרון) יידרש לאלגוריתם כדי לבצע את משימתו, כתלות בכמה "גדולה" המשימה.

*   **חיפוש לינארי:** אם בספר יש 10 דפים, ייתכן שתצטרכו לדפדף ב-10 דפים. אם בספר יש 100 דפים, ייתכן שתצטרכו לדפדף ב-100 דפים. כמות העבודה גדלה *לינארית* עם גודל המשימה. זה נקרא **O(n)**, כאשר 'n' הוא גודל המשימה (מספר הדפים בספר).

*   **חיפוש בינארי:** אם בספר יש 16 דפים, יידרשו לכם לכל היותר 4 צעדים למצוא את השם. אם בספר יש 32 דפים, יידרשו לכם לכל היותר 5 צעדים. כמות העבודה גדלה הרבה יותר לאט מגודל המשימה. זה נקרא **O(log n)** (נקרא "או של לוג אין").

*   אלגוריתם **O(n)** הופך לאיטי יותר *ביחס ישר* לגידול בגודל המשימה.
*   אלגוריתם **O(log n)** הופך לאיטי יותר *הרבה יותר לאט* מגידול גודל המשימה.

דמיינו שאתם מפתחים מנוע חיפוש. אם תשתמשו באלגוריתם O(n) לחיפוש באינטרנט (המכיל מיליארדי דפי אינטרנט), זה ייקח כמות עצומה של זמן! ואילו אלגוריתם O(log n) יתמודד עם המשימה הרבה יותר מהר.

### סוגי מורכבות אלגוריתמים עיקריים

להלן כמה מסוגי המורכבות הנפוצים ביותר:

*   **O(1) – מורכבות קבועה:** זמן הביצוע תמיד זהה, ללא קשר לגודל המשימה. לדוגמה, קבלת האיבר הראשון מרשימה.

    ```python
    def get_first_element(my_list):
        """O(1) - קבלת האיבר הראשון ברשימה."""
        return my_list[0]
    ```

*   **O(log n) – מורכבות לוגריתמית:** זמן הביצוע גדל לאט מאוד עם גידול גודל המשימה. דוגמה מצוינת – חיפוש בינארי.

    ```python
    def binary_search(my_list, target):
        """O(log n) - חיפוש בינארי ברשימה ממוינת."""
        low = 0
        high = len(my_list) - 1

        while low <= high:
            mid = (low + high) // 2
            if my_list[mid] == target:
                return mid
            elif my_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1  # האיבר לא נמצא
    ```

*   **O(n) – מורכבות לינארית:** זמן הביצוע גדל ביחס ישר לגודל המשימה. לדוגמה, מעבר על כל איבר ברשימה.

    ```python
    def linear_search(my_list, target):
        """O(n) - חיפוש לינארי ברשימה."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return i
        return -1  # האיבר לא נמצא
    ```

*   **O(n log n) – מורכבות לינארית-לוגריתמית:** נפוץ באלגוריתמי מיון יעילים, כמו Merge Sort ו-Quick Sort.

    ```python
    def merge_sort(my_list):
        """O(n log n) - מיון מיזוג."""
        if len(my_list) <= 1:
            return my_list

        mid = len(my_list) // 2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])

        return merge(left, right)

    def merge(left, right):
        """פונקציית עזר עבור merge_sort."""
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    ```

*   **O(n^2) – מורכבות ריבועית:** זמן הביצוע גדל *בריבוע* של גודל המשימה. לדוגמה, השוואת כל איבר ברשימה לכל איבר אחר באותה רשימה.

    ```python
    def bubble_sort(my_list):
        """O(n^2) - מיון בועות."""
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1] :
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    ```

*   **O(2^n) – מורכבות אקספוננציאלית:** זמן הביצוע גדל מהר מאוד עם גידול גודל המשימה. בדרך כלל נמצא באלגוריתמים המשתמשים בכוח גס (full enumeration).

    ```python
    def fibonacci_recursive(n):
      """O(2^n) - חישוב רקורסיבי של מספר פיבונאצ'י."""
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    ```

*   **O(n!) – מורכבות עצרתית (פקטוריאלית):** הסוג האיטי ביותר של מורכבות. נמצא במעבר על כל התמורות האפשריות של איברים.

### דוגמאות לבעיות ואלגוריתמים עם מורכבות שונה

נסקור כמה דוגמאות לבעיות ואלגוריתמים שונים לפתרונן, כדי לראות כיצד המורכבות משפיעה על הביצועים.

**1. מיון רשימה:**

*   **הבעיה:** למיין רשימת איברים בסדר מסוים (לדוגמה, עולה).
*   **אלגוריתמים:**
    *   **Bubble Sort:**

        ```python
        def bubble_sort(my_list):
            n = len(my_list)
            for i in range(n):
                for j in range(0, n-i-1):
                    if my_list[j] > my_list[j+1] :
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        # דוגמת שימוש
        my_list = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(my_list)
        print("Отсортированный массив:", my_list) # פלט: [11, 12, 22, 25, 34, 64, 90]
        ```

    *   **Merge Sort:**

        ```python
        def merge_sort(my_list):
            if len(my_list) <= 1:
                return my_list

            mid = len(my_list) // 2
            left = merge_sort(my_list[:mid])
            right = merge_sort(my_list[mid:])

            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        # דוגמת שימוש
        my_list = [64, 34, 25, 12, 22, 11, 90]
        sorted_list = merge_sort(my_list)
        print("Отсортированный массив:", sorted_list) # פלט: [11, 12, 22, 25, 34, 64, 90]
        ```
*   **מסקנה:** עבור רשימות גדולות, אלגוריתמים עם O(n log n) (Merge Sort) עדיפים על אלגוריתמים עם O(n^2) (Bubble Sort).

**2. מציאת המסלול הקצר ביותר בגרף:**

*   **הבעיה:** למצוא את המסלול הקצר ביותר בין שני קודקודים בגרף (לדוגמה, בין שתי ערים על מפה).
*   **אלגוריתמים:**
    *   **אלגוריתם דייקסטרה (Dijkstra's Algorithm):**

        ```python
        import heapq

        def dijkstra(graph, start):
            """אלגוריתם דייקסטרה למציאת מסלולים קצרים ביותר."""
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            priority_queue = [(0, start)]  # (distance, node)

            while priority_queue:
                distance, node = heapq.heappop(priority_queue)

                if distance > distances[node]:
                    continue

                for neighbor, weight in graph[node].items():
                    new_distance = distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(priority_queue, (new_distance, neighbor))

            return distances

        # דוגמת שימוש
        graph = {
            'A': {'B': 5, 'C': 1},
            'B': {'A': 5, 'C': 2, 'D': 1},
            'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
            'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
            'E': {'C': 8, 'D': 3},
            'F': {'D': 6}
        }
        start_node = 'A'
        shortest_paths = dijkstra(graph, start_node)
        print(f"Кратчайшие пути от {start_node}: {shortest_paths}")
        ```

*   **מסקנה:** בחירת האלגוריתם תלויה בסוג הגרף (משוקלל/לא משוקלל, קיום קצוות בעלי משקל שלילי) ובגודל הגרף. אלגוריתם דייקסטרה יעיל עבור גרפים עם משקלים אי-שליליים.

**3. חיפוש תת-מחרוזת במחרוזת:**

*   **הבעיה:** למצוא את כל ההופעות של תת-מחרוזת ספציפית במחרוזת גדולה יותר.
*   **אלגוריתמים:**
    *   **חיפוש נאיבי (Naive String Search):**

        ```python
        def naive_string_search(text, pattern):
            """אלגוריתם חיפוש תת-מחרוזת נאיבי."""
            occurrences = []
            for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                    occurrences.append(i)
            return occurrences

        # דוגמת שימוש
        text = "This is a simple example text."
        pattern = "example"
        occurrences = naive_string_search(text, pattern)
        print(f"Вхождения '{pattern}' в текст: {occurrences}")  # פלט: [17]
        ```

*   **מסקנה:** לחיפוש תת-מחרוזות תדיר במחרוזות גדולות, קיימים אלגוריתמים יעילים יותר, כמו KMP.

**4. בעיית התרמיל (Knapsack Problem):**

*   **הבעיה:** ברשותכם תרמיל בקיבולת מסוימת ואוסף של פריטים בעלי משקל וערך שונים. עליכם לבחור פריטים שימקסמו את הערך הכולל, מבלי לחרוג מקיבולת התרמיל.
*   **אלגוריתמים:**
    *   **תכנון דינמי (Dynamic Programming):**

        ```python
        def knapsack_dynamic_programming(capacity, weights, values, n):
            """פתרון בעיית התרמיל בשיטת תכנון דינמי."""
            dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

            for i in range(n + 1):
                for w in range(capacity + 1):
                    if i == 0 or w == 0:
                        dp[i][w] = 0
                    elif weights[i-1] <= w:
                        dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],  dp[i-1][w])
                    else:
                        dp[i][w] = dp[i-1][w]

            return dp[n][capacity]

        # דוגמת שימוש
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(values)
        max_value = knapsack_dynamic_programming(capacity, weights, values, n)
        print(f"Максимальная ценность: {max_value}")  # פלט: 220
        ```

*   **בחירת האלגוריתם תלויה בגודל הבעיה ובדרישות לדיוק הפתרון.**

### סימון O גדול (O-notation): פישוט המורכבות

בדרך כלל המורכבות מתוארת באמצעות "אות O גדולה" (סימון O גדול). היא מציגה את קצב הגידול של זמן ביצוע האלגוריתם עם גידול גודל הבעיה, *אסימפטוטית*, כלומר עבור ערכים גדולים מאוד של `n`. קבועים קטנים ופרטי מימוש בדרך כלל מתעלמים. לדוגמה, אלגוריתם שמבצע `2n + 5` פעולות עדיין נחשב *O(n)*.

### במקרה הגרוע ביותר, במקרה הממוצע, במקרה הטוב ביותר

מורכבות האלגוריתם יכולה להיות תלויה בנתוני הקלט. בדרך כלל מדברים על מורכבות *במקרה הגרוע ביותר* – זו הכמות המקסימלית של זמן או משאבים שעלולה להידרש לאלגוריתם. לעיתים גם מנתחים את המורכבות במקרה הממוצע ובמקרה הטוב ביותר.