בטח, בשמחה! הנה פוסט מורחב ומפורט בבלוג בעברית, המבוסס על התמונה והרעיון שלך, עם תוספות משמעותיות, דוגמאות ופירוט טכני מעמיק.

---

### כיצד לקבל מידע על כל מדינה בעולם באמצעות פייתון ו-REST API

האם אי פעם רציתם לשלוף נתונים עדכניים על מדינה כלשהי ישירות לתוך הקוד שלכם? אולי לפרויקט לימודים, לפיתוח בוט לטלגרם, או פשוט מתוך סקרנות. היום נלמד כיצד לבנות כלי פשוט אך חזק באמצעות פייתון, המאפשר לקבל מידע מקיף על כל מדינה בעולם בעזרת API חינמי ופתוח בשם `REST Countries`.

הכלי שלנו יתבסס על שני מרכיבים עיקריים:
1.  **ספריית `requests`**: הסטנדרט דה-פקטו בפייתון לביצוע בקשות HTTP לרשת.
2.  **REST Countries API**: שירות API חינמי לחלוטין, שאינו דורש מפתח הרשאה (API Key) ומספק כמויות אדירות של מידע על מדינות.

#### שלב 1: הכנת סביבת העבודה

ראשית, ודאו שמותקן אצלכם פייתון. לאחר מכן, נתקין את ספריית `requests`. אם היא עדיין לא מותקנת, פתחו את הטרמינל או שורת הפקודה והקלידו:

```bash
pip install requests
```

#### שלב 2: הפונקציה המרכזית - קבלת מידע מפורט על מדינה

נתחיל בכתיבת הפונקציה שתקבל שם של מדינה (באנגלית) ותחזיר עליה מידע מפורט. שימו לב שהרחבנו את הפונקציה המקורית כדי לשלוף נתונים מעניינים נוספים כמו שם רשמי, מדינות גובלות, וסיומת אינטרנט.

כדי להציג את שמות המדינות הגובלות (ה-API מחזיר רק קודים), ניצור פונקציית עזר קטנה שתמיר קוד מדינה לשם מלא.

```python
import requests

# כתובת ה-API הראשית
BASE_URL = "https://restcountries.com/v3.1"

def get_country_name_by_code(code):
    """פונקציית עזר: מקבלת קוד מדינה (למשל 'USA') ומחזירה את שמה המלא."""
    try:
        response = requests.get(f"{BASE_URL}/alpha/{code}")
        response.raise_for_status() # יזרוק שגיאה אם הבקשה נכשלה
        return response.json()[0].get("name", {}).get("common", code)
    except requests.RequestException:
        return code # במקרה של שגיאה, נחזיר את הקוד המקורי

def get_country_info(country_name):
    """
    שולפת ומציגה מידע מפורט על מדינה ספציפית מ-REST Countries API.
    """
    print(f"\n--- מחפש מידע על המדינה: {country_name} ---")
    try:
        # שולחים בקשת GET לנקודת הקצה של חיפוש לפי שם מלא
        response = requests.get(f"{BASE_URL}/name/{country_name}?fullText=true")
        response.raise_for_status() # בודק אם הבקשה הצליחה (קוד 200-299)
        
        # ה-API מחזיר רשימה של מדינות, אנחנו ניקח את התוצאה הראשונה
        data = response.json()[0]
        
        # שולפים נתונים בבטחה באמצעות .get() כדי למנוע שגיאות אם מפתח חסר
        name = data.get("name", {}).get("common", "לא ידוע")
        official_name = data.get("name", {}).get("official", "אין שם רשמי")
        capital = ", ".join(data.get("capital", ["אין עיר בירה"]))
        population = data.get("population", "אין נתונים")
        area = data.get("area", "אין נתונים")
        region = data.get("region", "אין נתונים")
        subregion = data.get("subregion", "אין נתונים")
        tld = ", ".join(data.get("tld", ["אין נתונים"])) # Top-Level Domain
        
        # המטבעות מאוחסנים כמילון, אנחנו רוצים את שמות המטבעות והסמלים שלהם
        currencies_data = data.get("currencies", {})
        currencies = ", ".join([f"{details['name']} ({symbol})" for symbol, details in currencies_data.items()]) or "אין נתונים"
        
        # שפות מאוחסנות כמילון של קוד-שם
        languages_data = data.get("languages", {})
        languages = ", ".join(languages_data.values()) or "אין נתונים"

        # המדינות הגובלות מגיעות כרשימת קודים. נשתמש בפונקציית העזר שלנו
        border_codes = data.get("borders", [])
        borders = [get_country_name_by_code(code) for code in border_codes]
        borders_str = ", ".join(borders) if borders else "מדינה שהיא אי (אין גבולות יבשתיים)"

        # מדפיסים את המידע בצורה מסודרת
        print(f"מידע כללי על '{name}':")
        print(f"  - שם רשמי: {official_name}")
        print(f"  - יבשת: {region} (אזור: {subregion})")
        print(f"  - עיר בירה: {capital}")
        print(f"  - אוכלוסייה: {population:,} תושבים") # פורמט עם פסיקים
        print(f"  - שטח: {area:,.2f} קמ\"ר") # פורמט עם פסיקים ושתי נקודות עשרוניות
        print(f"  - מדינות גובלות: {borders_str}")
        print(f"  - שפות רשמיות: {languages}")
        print(f"  - מטבעות: {currencies}")
        print(f"  - סיומת אינטרנט: {tld}")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"שגיאה: המדינה '{country_name}' לא נמצאה. ודא שהשם באנגלית ומלא.")
        else:
            print(f"שגיאת HTTP: {e}")
    except requests.exceptions.RequestException as e:
        print(f"שגיאת רשת: {e}. בדוק את חיבור האינטרנט שלך.")
    except Exception as e:
        print(f"אירעה שגיאה לא צפויה: {e}")
```

**דוגמת שימוש:**
נריץ את הפונקציה עם המדינה "Switzerland":
```
--- מחפש מידע על המדינה: Switzerland ---
מידע כללי על 'Switzerland':
  - שם רשמי: Swiss Confederation
  - יבשת: Europe (אזור: Western Europe)
  - עיר בירה: Bern
  - אוכלוסייה: 8,654,622 תושבים
  - שטח: 41,284.00 קמ"ר
  - מדינות גובלות: Austria, France, Italy, Liechtenstein, Germany
  - שפות רשמיות: German, French, Italian
  - מטבעות: Swiss franc (CHF)
  - סיומת אינטרנט: .ch
```

#### שלב 3: הרחבת היכולות - חיפושים נוספים

ה-API מאפשר לנו לחפש מדינות לפי פרמטרים נוספים. בואו נוסיף פונקציות שינצלו את היכולות הללו.

##### א. חיפוש מדינות לפי מטבע

רוצים לדעת איפה משתמשים בדולר או באירו? נקודת הקצה `/currency/{code}` היא בדיוק בשביל זה.

```python
def get_countries_by_currency(currency_code):
    """מוצאת ומדפיסה רשימת מדינות המשתמשות במטבע מסוים."""
    print(f"\n--- מחפש מדינות עם המטבע: {currency_code.upper()} ---")
    try:
        response = requests.get(f"{BASE_URL}/currency/{currency_code}")
        response.raise_for_status()
        
        countries = response.json()
        print(f"נמצאו {len(countries)} מדינות:")
        country_names = sorted([c.get("name", {}).get("common", "לא ידוע") for c in countries])
        for name in country_names:
            print(f"  - {name}")
            
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"שגיאה: לא נמצאו מדינות עם המטבע '{currency_code}'.")
        else:
            print(f"שגיאת HTTP: {e}")
    except requests.RequestException as e:
        print(f"שגיאת רשת: {e}")
```
**דוגמת שימוש:** `get_countries_by_currency("ILS")` תדפיס:
```
--- מחפש מדינות עם המטבע: ILS ---
נמצאו 2 מדינות:
  - Israel
  - Palestine
```

##### ב. חיפוש מדינות לפי שפה

באותה צורה, נוכל למצוא מדינות הדוברות שפה מסוימת באמצעות נקודת הקצה `/lang/{language}`.

```python
def get_countries_by_language(language):
    """מוצאת ומדפיסה רשימת מדינות הדוברות שפה מסוימת."""
    print(f"\n--- מחפש מדינות הדוברות: {language.capitalize()} ---")
    try:
        response = requests.get(f"{BASE_URL}/lang/{language}")
        response.raise_for_status()
        
        countries = response.json()
        print(f"נמצאו {len(countries)} מדינות:")
        country_names = sorted([c.get("name", {}).get("common", "לא ידוע") for c in countries])
        for name in country_names:
            print(f"  - {name}")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"שגיאה: לא נמצאו מדינות הדוברות '{language}'.")
        else:
            print(f"שגיאת HTTP: {e}")
    except requests.RequestException as e:
        print(f"שגיאת רשת: {e}")
```
**דוגמת שימוש:** `get_countries_by_language("arabic")` תציג רשימה ארוכה של מדינות דוברות ערבית.

##### ג. חיפוש מדינות לפי אזור/יבשת

יכולת שימושית נוספת היא קבלת כל המדינות ביבשת מסוימת, למשל "Europe" או "Africa", באמצעות `/region/{name}`.

```python
def get_countries_by_region(region):
    """מוצאת ומדפיסה את כל המדינות ביבשת או אזור מסוים."""
    print(f"\n--- מחפש מדינות באזור: {region.capitalize()} ---")
    try:
        response = requests.get(f"{BASE_URL}/region/{region}")
        response.raise_for_status()

        countries = response.json()
        print(f"נמצאו {len(countries)} מדינות ב'{region.capitalize()}':")
        country_names = sorted([c.get("name", {}).get("common", "לא ידוע") for c in countries])
        for name in country_names:
            print(f"  - {name}")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"שגיאה: האזור '{region}' לא נמצא. נסה: Africa, Americas, Asia, Europe, Oceania.")
        else:
            print(f"שגיאת HTTP: {e}")
    except requests.RequestException as e:
        print(f"שגיאת רשת: {e}")
```
**דוגמת שימוש:** `get_countries_by_region("oceania")` תציג את כל מדינות אוקיאניה.

#### שלב 4: הרכבת הכלי השלם עם תפריט אינטראקטיבי

עכשיו, נאחד את כל הפונקציות שבנינו לכדי סקריפט שלם עם תפריט שמאפשר למשתמש לבחור איזו פעולה הוא רוצה לבצע.

```python
# יש למקם כאן את כל הפונקציות שכתבנו למעלה:
# get_country_name_by_code, get_country_info, get_countries_by_currency, 
# get_countries_by_language, get_countries_by_region

if __name__ == "__main__":
    print("ברוכים הבאים לכלי המידע על מדינות העולם!")
    
    while True:
        print("\n" + "="*40)
        print("תפריט ראשי:")
        print("1. קבלת מידע מפורט על מדינה לפי שם")
        print("2. חיפוש מדינות לפי קוד מטבע (למשל, EUR)")
        print("3. חיפוש מדינות לפי שפה (למשל, Spanish)")
        print("4. חיפוש מדינות לפי יבשת (למשל, Europe)")
        print("5. יציאה")
        print("="*40)
        
        choice = input("אנא בחר פעולה (1-5): ").strip()
        
        if choice == "1":
            name_input = input("הזן את שם המדינה המלא (באנגלית): ").strip()
            if name_input:
                get_country_info(name_input)
            else:
                print("שם המדינה לא יכול להיות ריק.")
        
        elif choice == "2":
            currency_input = input("הזן קוד מטבע בן 3 אותיות (למשל, USD): ").strip()
            if currency_input:
                get_countries_by_currency(currency_input)
            else:
                print("קוד המטבע לא יכול להיות ריק.")

        elif choice == "3":
            language_input = input("הזן שפה (באנגלית): ").strip()
            if language_input:
                get_countries_by_language(language_input)
            else:
                print("שם השפה לא יכול להיות ריק.")

        elif choice == "4":
            region_input = input("הזן שם יבשת (באנגלית): ").strip()
            if region_input:
                get_countries_by_region(region_input)
            else:
                print("שם היבשת לא יכול להיות ריק.")
                
        elif choice == "5":
            print("תודה שהשתמשת בכלי. להתראות!")
            break
            
        else:
            print("בחירה לא חוקית. אנא הזן מספר בין 1 ל-5.")
```

### סיכום ורעיונות להמשך

יצרנו כלי קונסולה חזק ושימושי שמדגים כמה קל ומהנה לעבוד עם שירותי REST API בפייתון. מכאן, השמיים הם הגבול. הנה כמה רעיונות איך תוכלו להמשיך ולפתח את הפרויקט:

1.  **שמירת נתונים לקובץ**: הרחב את הפונקציות כך שישמרו את התוצאות לקובץ `JSON` או `CSV` לצורך ניתוח עתידי.
2.  **ממשק גרפי (GUI)**: עטוף את הלוגיקה בממשק משתמש פשוט באמצעות ספריות כמו `Tkinter` או `PyQt`.
3.  **הצגה ויזואלית של נתונים**: השתמש בספריית `matplotlib` או `seaborn` כדי ליצור גרפים מהנתונים, למשל, תרשים עמודות המשווה את אוכלוסיית המדינות באירופה.
4.  **שילוב עם בוט**: הפוך את הסקריפט לבוט טלגרם או דיסקורד שאנשים יכולים לשאול אותו שאלות על מדינות.
5.  **אפליקציית ווב**: השתמש ב-framework כמו `Flask` או `FastAPI` כדי להפוך את הכלי לאתר אינטרנט קטן.

אנו מקווים שמדריך זה נתן לכם בסיס טוב והשראה לחקור את עולם ה-API והאפשרויות הבלתי מוגבלות שהוא פותח. תכנות מהנה