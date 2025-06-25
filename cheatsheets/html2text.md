# **אמנות ההמרה: הפיכת HTML ל-Markdown באמצעות `html2text` בפייתון**

בעולם פיתוח האתרים ועיבוד התוכן, לעיתים קרובות עולה הצורך להמיר מסמכי HTML לפורמט Markdown, שהוא קל משקל וקריא יותר. בין אם מדובר בחילוץ התוכן העיקרי מדף אינטרנט, הכנת טקסט לתיעוד, או פשוט פישוט התגיות, פייתון מציעה פתרון אלגנטי בדמות הספרייה `html2text`.

**`html2text`** היא כלי קומפקטי וקל לשימוש, המיועד להמרת HTML ל-Markdown נקי ומובנה היטב. היא מתמודדת מצוין עם רכיבי עיצוב בסיסיים כמו כותרות, פסקאות, רשימות וקישורים. עם זאת, חשוב לזכור שמבני HTML מורכבים, כמו טבלאות או רכיבים התלויים מאוד ב-CSS וב-JavaScript, עשויים להיות מפושטים או שהספרייה תתעלם מהם.

**למה `html2text` יכולה להיות שימושית?**

*   **חילוץ תוכן:** קבלת טקסט עיקרי מדף במהירות, נקי מתגיות HTML.
*   **יצירת תיעוד:** אם יש לכם תיעוד ב-HTML, תוכלו להמיר אותו בקלות ל-Markdown לשימוש בפלטפורמות כמו GitHub.
*   **ניתוח אתרים (Parsing):** בשילוב עם ספריות לגירוד רשת (Web Scraping) (למשל, `requests` ו-`BeautifulSoup`), `html2text` תסייע לקבל את תוכן הטקסט של דפים בפורמט נוח.
*   **פישוט תגיות:** עבור מערכות שעובדות טוב יותר עם Markdown מאשר עם HTML מלא.

בואו נצלול לפרטי ההתקנה והשימוש בספרייה שימושית זו.

---

## **1. התקנה: מכינים את הקרקע**

כמו רוב חבילות הפייתון, `html2text` ניתנת להתקנה בקלות באמצעות `pip`:

```bash
pip install html2text
```

אם אתם משתמשים במספר גרסאות של פייתון או עובדים בסביבה וירטואלית, ייתכן שתצטרכו להשתמש ב-`pip3`:

```bash
pip3 install html2text
```

ודאו שההתקנה הצליחה על ידי ניסיון לייבא את הספרייה במפרש הפייתון:

```python
import html2text
print(html2text.__version__) # אמור להדפיס את גרסת הספרייה
```

---

## **2. שימוש בסיסי: צעדים ראשונים**

הדרך הפשוטה ביותר להשתמש ב-`html2text` היא לקרוא לפונקציה `html2text.html2text()`, ולהעביר לה מחרוזת HTML.

### **דוגמה פשוטה**

ניקח קטע HTML קטן ונראה כיצד הוא יומר:

```python
import html2text

html_content = """
<html>
<head>
    <title>עמוד מבחן</title>
</head>
<body>
    <h1>שלום, עולם!</h1>
    <p>זוהי דוגמה פשוטה להדגמת פעולת <b>html2text</b>.</p>
    <p>אנו ממירים את <i>ה-HTML הזה</i> ל-Markdown.</p>
    <ul>
        <li>פריט ראשון</li>
        <li>פריט שני</li>
    </ul>
    <a href="https://example.com">זהו קישור</a>
</body>
</html>
"""

markdown_output = html2text.html2text(html_content)

print(markdown_output)
```

**פלט:**

```markdown
שלום, עולם!
===========

זוהי דוגמה פשוטה להדגמת פעולת **html2text**.

אנו ממירים את *ה-HTML הזה* ל-Markdown.

  * פריט ראשון
  * פריט שני

[זהו קישור](https://example.com)
```

כפי שניתן לראות, כותרות (`<h1>`), פסקאות (`<p>`), הדגשה (`<b>`), הטיה (`<i>`), רשימות (`<ul><li>`) וקישורים (`<a>`) הומרו כראוי לתחביר ה-Markdown המתאים.

---

## **3. התאמה אישית של ההמרה: עבודה עדינה עם `HTML2Text`**

לשליטה גמישה יותר בתהליך ההמרה, `html2text` מספקת את המחלקה `HTML2Text`. על ידי יצירת מופע שלה, תוכלו להגדיר פרמטרים שונים לפני קריאה למתודה `handle()` לביצוע ההמרה.

### **פרמטרים עיקריים של מופע `HTML2Text`**

| פרמטר                | טיפוס  | ברירת מחדל | תיאור                                                                                                                                     |
|-----------------------|---------|--------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `bodywidth`           | `int`   | `None`       | רוחב שורה מקסימלי לפלט. אם `None` (או 0), שורות לא יגלשו.                                                                                     |
| `baseurl`             | `str`   | `''`         | כתובת URL בסיסית להמרת קישורים יחסיים לקישורים מוחלטים.                                                                                    |
| `ignore_links`        | `bool`  | `False`      | אם `True`, המערכת תתעלם מתגיות `<a>` (הטקסט בתוכן יישאר).                                                                                     |
| `ignore_images`       | `bool`  | `False`      | אם `True`, המערכת תתעלם מתגיות `<img>`.                                                                                                    |
| `ignore_emphasis`     | `bool`  | `False`      | אם `True`, תגי הדגשה (`<b>`, `<strong>`, `<i>`, `<em>`) יתעלמו מהם (הטקסט בתוכם יישאר ללא עיצוב).                                         |
| `ignore_tables`       | `bool`  | `False`      | אם `True`, טבלאות יתעלמו מהן לחלוטין. כברירת מחדל, טקסט מהתאים נשלף, אך ללא עיצוב Markdown של טבלה.                                       |
| `images_to_alt`       | `bool`  | `False`      | אם `True` ו-`ignore_images` הוא `False`, במקום `![alt](src)` יוצג רק טקסט ה-`alt` של התמונה.                                                  |
| `images_with_size`    | `bool`  | `False`      | אם `True`, מנסה להוסיף את מידות התמונה בפורמט HTML לתמונת ה-Markdown (למשל, `![alt](src){width=... height=...}`).                          |
| `escape_all`          | `bool`  | `False`      | אם `True`, יבוצע escape לכל תווי ה-Markdown המיוחדים (למשל, `*` יהפוך ל-`\*`).                                                                |
| `ul_item_mark`        | `str`   | `*`          | סמן לפריטים ברשימה לא ממוספרת (`<ul>`). יכול להיות `*`, `-` או `+`.                                                                          |
| `emphasis_mark`       | `str`   | `_`          | תו להטיה (`*` או `_`). שימו לב שכברירת מחדל נעשה שימוש ב-`_`, אך הפלט לעיתים קרובות מציג `*`.                                               |
| `strong_mark`         | `str`   | `**`         | תו להדגשה (`**` או `__`).                                                                                                                 |
| `unicode_snob`        | `bool`  | `False`      | שימוש בתווי Unicode "יפים" במקום מקביליהם ב-ASCII (למשל, עבור קו אופקי).                                                                    |
| `protect_links`       | `bool`  | `False`      | אם `True`, עוטף קישורים ב-`< >` כדי למנוע זיהוי שגוי שלהם כ-Markdown (למשל, בכתובות אימייל).                                                 |
| `google_doc`          | `bool`  | `False`      | מפעיל פתרונות עקיפים מיוחדים עבור HTML שיוצא מ-Google Docs.                                                                               |
| `default_image_alt`   | `str`   | `''`         | טקסט ברירת מחדל לתמונות שחסר להן מאפיין `alt`.                                                                                              |
| `bypass_tables`       | `bool`  | `True`       | (הוצא משימוש, השתמשו ב-`ignore_tables=False` להתנהגות הישנה). אם `True`, מעבד טבלאות על ידי חילוץ טקסט מהתאים.                                |

### **דוגמאות עם פרמטרים**

בואו נבחן כיצד פרמטרים אלה משפיעים על התוצאה.

```python
import html2text

# יוצרים מופע של הממיר
h = html2text.HTML2Text()

# 1. הגבלת רוחב שורה והתעלמות מקישורים
h.bodywidth = 30
h.ignore_links = True
html_snippet1 = '<p>זוהי שורת טקסט ארוכה מאוד שאמורה לגלוש. <a href="https://example.com">קישור</a></p>'
markdown1 = h.handle(html_snippet1)
print("--- דוגמה 1 (bodywidth, ignore_links) ---")
print(markdown1)

# מאפסים את ignore_links לדוגמאות הבאות
h.ignore_links = False

# 2. התעלמות מתמונות ושימוש בטקסט alt
h.ignore_images = False # מוודאים שתמונות מעובדות
h.images_to_alt = True
html_snippet2 = '<p>תמונה: <img src="image.png" alt="לוגו"></p>'
markdown2 = h.handle(html_snippet2)
print("--- דוגמה 2 (images_to_alt) ---")
print(markdown2)

# מאפסים את images_to_alt
h.images_to_alt = False

# 3. בריחה (escape) של תווים מיוחדים
h.escape_all = True
html_snippet3 = "<p>טקסט עם *כוכביות* ו _קווים תחתונים_.</p>"
markdown3 = h.handle(html_snippet3)
print("--- דוגמה 3 (escape_all) ---")
print(markdown3)

# מאפסים את escape_all
h.escape_all = False

# 4. שינוי סמני רשימה ועיצוב
h.ul_item_mark = '-'
h.emphasis_mark = '*' # ברירת המחדל היא לעיתים קרובות '*' עבור <i>
h.strong_mark = '__'
html_snippet4 = "<ul><li><em>חשוב</em></li><li><strong>חשוב מאוד</strong></li></ul>"
markdown4 = h.handle(html_snippet4)
print("--- דוגמה 4 (ul_item_mark, emphasis_mark, strong_mark) ---")
print(markdown4)

# 5. שימוש ב-unicode_snob למפרידים יפים
h_unicode = html2text.HTML2Text() # מופע חדש לניקיון
h_unicode.unicode_snob = True
html_snippet5 = "<hr>"
markdown5 = h_unicode.handle(html_snippet5)
print("--- דוגמה 5 (unicode_snob) ---")
print(markdown5)

# להשוואה, ללא unicode_snob
h_no_unicode = html2text.HTML2Text()
markdown5_no_unicode = h_no_unicode.handle(html_snippet5)
print("--- דוגמה 5 (ללא unicode_snob) ---")
print(markdown5_no_unicode)
```

**פלט צפוי:**

```
--- דוגמה 1 (bodywidth, ignore_links) ---
זוהי שורת טקסט ארוכה מאוד
שאמורה לגלוש. קישור

--- דוגמה 2 (images_to_alt) ---
תמונה: לוגו

--- דוגמה 3 (escape_all) ---
טקסט עם \*כוכביות\* ו \_קווים תחתונים\_.

--- דוגמה 4 (ul_item_mark, emphasis_mark, strong_mark) ---
  - *חשוב*
  - __חשוב מאוד__

--- דוגמה 5 (unicode_snob) ---
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

--- דוגמה 5 (ללא unicode_snob) ---
* * *
```
*הערה: הפלט בפועל של התווים עבור `emphasis_mark` ו-`strong_mark` עשוי להיות תלוי באילו תגי HTML נעשה שימוש (`<i>` לעומת `<em>`, `<b>` לעומת `<strong>`). ל-`html2text` עשויה להיות לוגיקה פנימית של העדפות.*

על ידי התנסות עם פרמטרים אלה, תוכלו להשיג פלט המתאים בצורה הטובה ביותר לדרישות שלכם.

---

## **4. עיבוד HTML ממקורות שונים**

`html2text` עובדת עם מחרוזות, כך שמקור ה-HTML יכול להיות כל דבר: קובץ על הדיסק, תגובה משרת אינטרנט וכו'.

### **המרת קובץ HTML**

נניח שיש לכם קובץ `input.html` עם התוכן הבא:

```html
<!-- input.html -->
<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <title>קובץ ה-HTML שלי</title>
</head>
<body>
    <h1>כותרת מהקובץ</h1>
    <p>זהו תוכן הקובץ שיעבור המרה.</p>
    <ol>
        <li>פריט ממוספר ראשון</li>
        <li>פריט ממוספר שני</li>
    </ol>
</body>
</html>
```

הקוד להמרתו:

```python
import html2text

# יוצרים מופע עם ההגדרות הרצויות (אם נדרש)
converter = html2text.HTML2Text()
converter.bodywidth = 0 # ללא גלישת שורות

try:
    with open("input.html", "r", encoding="utf-8") as f:
        html_from_file = f.read()

    markdown_from_file = converter.handle(html_from_file)
    # או פשוט: markdown_from_file = html2text.html2text(html_from_file)

    print("--- Markdown מקובץ input.html ---")
    print(markdown_from_file)

    with open("output.md", "w", encoding="utf-8") as f:
        f.write(markdown_from_file)
    print("\nהתוצאה נשמרה ב-output.md")

except FileNotFoundError:
    print("שגיאה: הקובץ input.html לא נמצא.")
```

לאחר הרצת קוד זה, בקובץ `output.md` יופיע:

```markdown
כותרת מהקובץ
=============

זהו תוכן הקובץ שיעבור המרה.

  1. פריט ממוספר ראשון
  2. פריט ממוספר שני
```

### **טעינת HTML מהאינטרנט (באמצעות `requests`)**

לקבלת קוד HTML של דף אינטרנט, לעיתים קרובות משתמשים בספריית `requests`. אם היא לא מותקנת אצלכם, התקינו אותה: `pip install requests`.

```python
import requests
import html2text

url = "https://example.com" # השתמשו בכל URL זמין

try:
    response = requests.get(url)
    response.raise_for_status()  # בדיקת שגיאות HTTP (4xx או 5xx)
    html_from_web = response.text

    # משתמשים ב-html2text עם הגדרות ברירת מחדל
    markdown_from_web = html2text.html2text(html_from_web)

    print(f"--- Markdown מהעמוד {url} ---")
    print(markdown_from_web[:500] + "...") # מדפיסים רק את ההתחלה לקיצור

except requests.exceptions.RequestException as e:
    print(f"שגיאה בעת טעינת העמוד: {e}")
except Exception as e:
    print(f"אירעה שגיאה אחרת: {e}")
```

סקריפט זה יטען את קוד ה-HTML מ-`example.com` ויהפוך אותו ל-Markdown.

---

## **5. פונקציות ומתודות של המודול: סקירה קצרה**

הפונקציונליות העיקרית מרוכזת סביב הפונקציה `html2text()` והמחלקה `HTML2Text`.

*   **`html2text.html2text(html_string, baseurl='')`**:
    *   זוהי הפונקציה ה"מהירה" העיקרית להמרה.
    *   מקבלת מחרוזת HTML (`html_string`) ו-`baseurl` אופציונלי ליישוב קישורים יחסיים.
    *   בפנים, היא יוצרת מופע של `HTML2Text` עם הגדרות ברירת מחדל וקוראת למתודה `handle()` שלו.
    *   אידיאלית כאשר הגדרות ברירת המחדל מתאימות לכם.

*   **מחלקה `html2text.HTML2Text(baseurl=None, bodywidth=None)`**:
    *   בנאי המחלקה. מאפשר אתחול של הממיר עם הגדרות בסיסיות של `baseurl` ו-`bodywidth`.
    *   פרמטרים רבים אחרים (ראו טבלה למעלה) מוגדרים כתכונות של המופע *לאחר* יצירתו: `h = HTML2Text(); h.ignore_links = True`.
    *   **מתודה `handle(html_string)`**:
        *   המתודה העיקרית של מופע `HTML2Text` לביצוע ההמרה.
        *   מקבלת מחרוזת HTML ומחזירה מחרוזת Markdown, תוך התחשבות בכל ההגדרות שנקבעו למופע זה.
    *   **מתודה `unescape(text_string)`**:
        *   מתודת עזר לפענוח ישויות HTML (למשל, `&amp;` ל-`&`). בדרך כלל נקראת מתוך `handle()`.
    *   **מתודה `feed(data)`**:
        *   לעיבוד זרם (streaming) של HTML. מאפשרת העברת HTML בחלקים. לאחר כל הקריאות ל-`feed()`, יש לקרוא ל-`close()` לקבלת התוצאה. תרחיש שימוש פחות נפוץ.
    *   **מתודה `close()`**:
        *   מסיימת את עיבוד הזרם ומחזירה את ה-Markdown שהומר. משמשת יחד עם `feed()`.

---

## **6. מגבלות ואלטרנטיבות**

למרות פשטותה ויעילותה למשימות רבות, ל-`html2text` יש מגבלות:

*   **טבלאות (`<table>`):** מומרות לטקסט מפושט. תוכן התאים נשלף ומסודר ברצף, אך ללא שימוש בתחביר Markdown לטבלאות (מפרידים `|` ו-`-`). אם הפרמטר `ignore_tables` מוגדר ל-`True`, המערכת תתעלם מטבלאות לחלוטין.
*   **רכיבי CSS/JS מורכבים:** הספרייה מתמקדת במבנה הסמנטי של ה-HTML ומתעלמת מסגנונות CSS והתנהגות JavaScript. תוכן שנוצר על ידי JavaScript בצד הלקוח לא יהיה זמין, אלא אם כן משתמשים בכלים כמו Selenium או Playwright לעיבוד מקדים של הדף.
*   **רשימות מקוננות:** במקרים מסוימים, רשימות מורכבות או מקוננות לעומק עלולות להיות מעובדות בצורה לא אידיאלית, מה שיוביל לאובדן מבנה או הזחות שגויות.
*   **מבני HTML ספציפיים:** פריסות HTML לא סטנדרטיות או מורכבות מאוד עלולות להוביל לתוצאה לא אופטימלית.

אם אתם זקוקים להמרה מדויקת או מתקדמת יותר, במיוחד עבור טבלאות או שמירה על מבנה מורכב יותר, שקלו את האלטרנטיבות הבאות:

*   **`markdownify`**: ספריית פייתון פופולרית נוספת, שלעיתים קרובות מספקת תמיכה טובה יותר בטבלאות והתאמה אישית עדינה יותר. (קישור: [GitHub - matthewwithanm/python-markdownify](https://github.com/matthewwithanm/python-markdownify))
*   **`pandoc`**: ממיר מסמכים אוניברסלי רב עוצמה, שניתן לקרוא לו מפייתון דרך `subprocess` או באמצעות עטיפות כמו `pypandoc`. Pandoc תומך במספר עצום של פורמטים ויש לו יכולות מתקדמות מאוד. (קישור: [Pandoc.org](https://pandoc.org/))

---

## **סיכום**

הספרייה `html2text` היא בחירה מצוינת להמרה מהירה ופשוטה של HTML ל-Markdown בפייתון. נקודות החוזק שלה הן תלויות מינימליות, קלות למידה וגמישות מספקת לרוב המשימות היומיומיות של חילוץ ועיצוב תוכן טקסטואלי מ-HTML.

היא אידיאלית כאשר אתם צריכים:

*   לחלץ במהירות את הטקסט העיקרי מהדף.
*   להמיר מסמכי HTML פשוטים (מאמרים, פוסטים) ל-Markdown.
*   לשלב המרת HTML בסיסית בסקריפטים של פייתון שלכם ללא סיבוכים מיותרים.

לתרחישים מורכבים יותר, הדורשים שחזור מדויק של טבלאות או שמירה על ניואנסים של פריסה מורכבת, כדאי לשקול כלים חזקים יותר, כגון `markdownify` או `pandoc`. אך למגוון רחב של משימות, `html2text` נשארת עוזר אמין ויעיל.

**קישורים נוספים:**

*   [תיעוד רשמי/מאגר html2text ב-GitHub](https://github.com/Alir3z4/html2text)
*   [דף html2text ב-PyPI](https://pypi.org/project/html2text/)

המרות מוצלחות!

---