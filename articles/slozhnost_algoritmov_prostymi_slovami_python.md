## סיבוכיות אלגוריתמים במילים פשוטות ועם דוגמאות ב-Python

בפיתוח תוכנה קיימות דרכים רבות לפתרון אותה משימה. אולם, לא כל הפתרונות יעילים באותה מידה. היבט מרכזי אחד שיש לקחת בחשבון בעת פיתוח אלגוריתמים הוא הסיבוכיות שלהם. הבנת סיבוכיות של אלגוריתם מאפשרת להעריך כמה מהר הוא יפעל וכמה משאבים (למשל, זיכרון) יידרשו לביצועו, במיוחד ככל שנפח נתוני הקלט גדל. הבנת סיבוכיות אלגוריתמים היא מיומנות בסיסית המאפשרת לכתוב קוד יעיל יותר.

### מהי סיבוכיות אלגוריתם?

דמיינו שיש לכם משימה: למצוא שם ספציפי בספר טלפונים.

*   **דרך פשוטה (חיפוש לינארי):** אתם לוקחים את הספר ומתחילים לדפדף בו דף אחר דף עד שתמצאו את השם המבוקש. אם השם נמצא בסוף הספר, תיאלצו לדפדף בכל הספר!
*   **דרך חכמה (חיפוש בינארי):** אתם פותחים את הספר באמצע. אם השם שאתם מחפשים מופיע לפני השם בעמוד זה, אתם סוגרים את המחצית השנייה של הספר ומחפשים במחצית הראשונה. אם השם מופיע לאחר מכן, אתם מחפשים במחצית השנייה. אתם חוזרים על כך עד שתמצאו את השם המבוקש. בכל שלב אתם מבטלים מחצית מהספר!

**סיבוכיות אלגוריתם** היא דרך לתאר כמה "זמן" (או משאבים, למשל זיכרון) יידרש לאלגוריתם כדי לבצע את משימתו, בהתאם למידת ה"גודל" של המשימה.

*   **חיפוש לינארי:** אם בספר יש 10 עמודים, ייתכן שתיאלצו לדפדף ב-10 עמודים. אם בספר יש 100 עמודים, ייתכן שתיאלצו לדפדף ב-100 עמודים. כמות העבודה גדלה באופן *לינארי* ביחס לגודל המשימה. זה נקרא **O(n)**, כאשר 'n' הוא גודל המשימה (מספר העמודים בספר).

*   **חיפוש בינארי:** אם בספר יש 16 עמודים, יידרשו לכם לכל היותר 4 שלבים כדי למצוא שם. אם בספר יש 32 עמודים, יידרשו לכם לכל היותר 5 שלבים. כמות העבודה גדלה לאט הרבה יותר מגודל המשימה. זה נקרא **O(log n)** (נקרא "או של לוג אין").

*   אלגוריתם **O(n)** הופך להיות איטי יותר *באופן פרופורציונלי ישיר* להגדלת גודל המשימה.
*   אלגוריתם **O(log n)** הופך להיות איטי יותר *לאט הרבה יותר* ביחס לגדילת גודל המשימה.

דמיינו שאתם מפתחים מנוע חיפוש. אם תשתמשו באלגוריתם O(n) לחיפוש באינטרנט (שמכיל מיליארדי דפי אינטרנט), זה ייקח זמן רב להפליא! בעוד שאלגוריתם O(log n) יתמודד עם משימה זו מהר הרבה יותר.

### סוגי סיבוכיות אלגוריתמים עיקריים

להלן כמה מסוגי הסיבוכיות הנפוצים ביותר:

*   **O(1) – סיבוכיות קבועה:** זמן הביצוע תמיד זהה, ללא קשר לגודל המשימה. לדוגמה, קבלת האיבר הראשון מרשימה.

    ```python
    def get_first_element(my_list):
        """O(1) - קבלת האיבר הראשון ברשימה."""
        return my_list[0]
    ```

*   **O(log n) – סיבוכיות לוגריתמית:** זמן הביצוע גדל לאט מאוד עם גדילת גודל המשימה. דוגמה מצוינת היא חיפוש בינארי.

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

*   **O(n) – סיבוכיות לינארית:** זמן הביצוע גדל באופן פרופורציונלי ישיר לגודל המשימה. לדוגמה, מעבר על כל איבר ברשימה.

    ```python
    def linear_search(my_list, target):
        """O(n) - חיפוש לינארי ברשימה."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return i
        return -1  # האיבר לא נמצא
    ```

*   **O(n log n) – סיבוכיות לינארית-לוגריתמית:** נפוצה לעיתים קרובות באלגוריתמי מיון יעילים, כגון מיון מיזוג (Merge Sort) ומיון מהיר (Quick Sort).

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

*   **O(n^2) – סיבוכיות ריבועית:** זמן הביצוע גדל *בריבוע* של גודל המשימה. לדוגמה, השוואת כל איבר ברשימה לכל איבר אחר באותה רשימה.

    ```python
    def bubble_sort(my_list):
        """O(n^2) - מיון בועות."""
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1] :
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    ```

*   **O(2^n) – סיבוכיות אקספוננציאלית:** זמן הביצוע גדל מהר מאוד עם גדילת גודל המשימה. נפוצה בדרך כלל באלגוריתמים המשתמשים בבדיקה ממצה (full enumeration).

    ```python
    def fibonacci_recursive(n):
      """O(2^n) - חישוב רקורסיבי של מספר פיבונאצ'י."""
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    ```

*   **O(n!) – סיבוכיות פקטוריאלית:** סוג הסיבוכיות האיטי ביותר. נפוצה בעת מעבר על כל התמורות האפשריות של איברים.

### דוגמאות לבעיות ואלגוריתמים עם סיבוכיות שונה

נסקור מספר דוגמאות לבעיות ואלגוריתמים שונים לפתרונן, כדי לראות כיצד הסיבוכיות משפיעה על הביצועים.

**1. מיון רשימה:**

*   **בעיה:** למיין רשימת איברים בסדר מסוים (לדוגמה, בסדר עולה).
*   **אלגוריתמים:**
    *   **מיון בועות (Bubble Sort):**

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
        print("מערך ממוין:", my_list) # פלט: [11, 12, 22, 25, 34, 64, 90]
        ```

    *   **מיון מיזוג (Merge Sort):**

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
        print("מערך ממוין:", sorted_list) # פלט: [11, 12, 22, 25, 34, 64, 90]
        ```
*   **מסקנה:** עבור רשימות גדולות של איברים, אלגוריתמים עם סיבוכיות O(n log n) (מיון מיזוג) עדיפים על אלגוריתמים עם סיבוכיות O(n^2) (מיון בועות).

**2. מציאת המסלול הקצר ביותר בגרף:**

*   **בעיה:** למצוא את המסלול הקצר ביותר בין שני קודקודים בגרף (לדוגמה, בין שתי ערים על מפה).
*   **אלגוריתמים:**
    *   **אלגוריתם דייקסטרה (Dijkstra's Algorithm):**

        ```python
        import heapq

        def dijkstra(graph, start):
            """אלגוריתם דייקסטרה למציאת המסלולים הקצרים ביותר."""
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
        print(f"המסלולים הקצרים ביותר מ-{start_node}: {shortest_paths}")
        ```

*   **מסקנה:** בחירת האלגוריתם תלויה בסוג הגרף (משוקלל/לא משוקלל, קיום קשתות בעלות משקל שלילי) ובגודל הגרף. אלגוריתם דייקסטרה יעיל עבור גרפים עם משקלים אי-שליליים.

**3. חיפוש תת-מחרוזת במחרוזת:**

*   **בעיה:** למצוא את כל המופעים של תת-מחרוזת מסוימת במחרוזת גדולה יותר.
*   **אלגוריתמים:**
    *   **חיפוש נאיבי (Naive String Search):**

        ```python
        def naive_string_search(text, pattern):
            """אלגוריתם נאיבי לחיפוש תת-מחרוזת."""
            occurrences = []
            for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                    occurrences.append(i)
            return occurrences

        # דוגמת שימוש
        text = "This is a simple example text."
        pattern = "example"
        occurrences = naive_string_search(text, pattern)
        print(f"מופעים של '{pattern}' בטקסט: {occurrences}")  # פלט: [17]
        ```

*   **מסקנה:** עבור חיפוש תכוף של תת-מחרוזות במחרוזות גדולות, קיימים אלגוריתמים יעילים יותר, כגון אלגוריתם KMP.

**4. בעיית תרמיל הגב (Knapsack Problem):**

*   **בעיה:** יש לכם תרמיל בקיבולת מסוימת ואוסף פריטים בעלי משקל וערך שונים. עליכם לבחור פריטים שימקסמו את הערך הכולל, מבלי לחרוג מקיבולת התרמיל.
*   **אלגוריתמים:**
    *   **תכנון דינמי (Dynamic Programming):**

        ```python
        def knapsack_dynamic_programming(capacity, weights, values, n):
            """פתרון בעיית תרמיל הגב בשיטת התכנון הדינמי."""
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
        print(f"הערך המקסימלי: {max_value}")  # פלט: 220
        ```

*   **בחירת האלגוריתם תלויה בגודל הבעיה ובדרישות הדיוק של הפתרון.**

### סימון O גדול: פישוט הסיבוכיות

בדרך כלל, הסיבוכיות מתוארת באמצעות "האות O הגדולה" (סימון O גדול, O-notation). היא מציגה את מהירות הגידול של זמן הביצוע של אלגוריתם ביחס לגדילת גודל המשימה, *אסימפטוטית*, כלומר עבור ערכים גדולים מאוד של `n`. קבועים קטנים ופרטי מימוש לרוב מוזנחים. לדוגמה, אלגוריתם שמבצע `2n + 5` פעולות, עדיין נחשב כבעל סיבוכיות *O(n)*.

### במקרה הגרוע ביותר, במקרה הממוצע, במקרה הטוב ביותר

סיבוכיות האלגוריתם יכולה להיות תלויה בנתוני הקלט. לרוב מדברים על סיבוכיות *במקרה הגרוע ביותר* – זו כמות הזמן או המשאבים המקסימלית שייתכן שיידרשו לאלגוריתם. לעיתים מנתחים גם את הסיבוכיות במקרה הממוצע ובמקרה הטוב ביותר.