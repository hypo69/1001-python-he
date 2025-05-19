בטח, הנה התרגום של המסמך מרוסית לעברית, תוך שמירה על ההנחיות:

# כיצד לתקן את השגיאה SSLCertVerificationError ב-Python

&nbsp;&nbsp;&nbsp;&nbsp; האם נתקלת בשגיאה `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` בעת ניסיון לבצע בקשת HTTPS ב-Python באמצעות `requests` או `urllib3`?
במאמר זה אראה כיצד לאבחן ולתקן בעיה זו.

השגיאה מציינת ש-Python לא הצליח לאמת את תעודת ה-SSL/TLS של אתר האינטרנט שאליו אתה מתחבר, כיוון שלא מצא תעודת בסיס מהימנה במאגר שלו.

## שלב 1: אבחון הבעיה באמצעות OpenSSL (מומלץ)

&nbsp;&nbsp;&nbsp;&nbsp; לפני שינוי קוד ה-Python, בדוק את חיבור ה-SSL באמצעות כלי השירות `openssl`. זה יסייע להבין האם הבעיה ספציפית ל-Python או קשורה להגדרות מערכת או לשרת עצמו.

1.  **התקן את OpenSSL**, אם אינו מותקן אצלך (לעתים קרובות מותקן מראש בלינוקס/macOS; עבור Windows הורד מ-[האתר הרשמי](https://www.openssl.org/source/) או השתמש במנהלי חבילות כמו Chocolatey/Scoop).
2.  **בצע את הפקודה** בטרמינל (שורת הפקודה) שלך, החלף את `<hostname>` בכתובת האתר (ללא `https://`) ואת `<port>` בפורט (בדרך כלל 443 עבור HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # דוגמה עבור rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **נתח את הפלט:** שים לב לשורה `Verify return code`. אם היא מכילה שגיאה כמו `unable to get local issuer certificate` (קוד 20) או `certificate verify failed` (קוד 21), זה מאשר את הבעיה באמון בתעודה ברמת המערכת או המאגר שבו OpenSSL משתמש.

## שלב 2: בחר שיטת פתרון

&nbsp;&nbsp;&nbsp;&nbsp; קיימות מספר שיטות לתיקון השגיאה `SSLCertVerificationError`. בחר בזו המתאימה ביותר למצבך.

### שיטה 1: כיבוי אימות SSL (מהיר, אך אינו בטוח)

&nbsp;&nbsp;&nbsp;&nbsp; שיטה זו מכבה לחלוטין את אימות התעודה. השתמש בה **רק** לבדיקה זמנית, סקריפטים חד-פעמיים ו**רק** עבור אתרים שבהם אתה בוטח לחלוטין.

⚠️ **אזהרה:** כיבוי האימות הופך את החיבור שלך לפגיע בפני התקפות 'אדם באמצע' (MITM). **לעולם אל תשתמש ב-`verify=False` בקוד ייצור (production) או בעבודה עם נתונים רגישים!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # דוגמה ל-URL

# מכבה את אימות ה-SSL
try:
    # מדחיק אזהרות לגבי בקשה לא בטוחה (אופציונלי)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # בודק שגיאות HTTP (4xx, 5xx)

    # הקוד שלך לעיבוד התגובה, למשל שמירת קובץ
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("הקובץ הורד בהצלחה (עם אימות SSL כבוי).")

except requests.exceptions.RequestException as e:
    print(f"שגיאה בעת הורדת הקובץ: {e}")

finally:
    # חשוב: אם כיבית אזהרות גלובלית,
    # ייתכן שתרצה להפעיל אותן שוב לאחר ביצוע הבקשה,
    # למרות שבדרך כלל אין צורך בכך אם הסקריפט מסיים ריצה.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### שיטה 2: התקנה/עדכון של תעודות עבור Python (תלוי פלטפורמה)

&nbsp;&nbsp;&nbsp;&nbsp; Python עשוי להגיע עם סקריפטים להתקנה או עדכון של אוסף תעודות בסיס מחבילת `certifi`.

*   **ב-macOS:**
    1.  עבור לתיקיית ההתקנה של Python (בדרך כלל `/Applications/Python <גרסה>/`).
    2.  אתר ולחץ לחיצה כפולה על הקובץ `Install Certificates.command`. הוא יתקין/יעדכן את `certifi` ויקשר את המודול הסטנדרטי `ssl` לתעודות אלו.
*   **ב-Windows:**
    1.  לעתים, בעת התקנת Python נוצר סקריפט `install_certificates.bat`. חפש אותו בספריית `Scripts` בתוך תיקיית ההתקנה של Python (לדוגמה, `C:\Users\<שם_משתמש>\AppData\Local\Programs\Python\Python<גרסה>\Scripts\`).
    2.  אם מצאת אותו, הפעל אותו.
    3.  אם הסקריפט אינו קיים, שיטה זו, קרוב לוודאי, לא תעבוד. השתמש בשיטה 3.

### שיטה 3: שימוש ישיר בחבילת certifi (מומלץ, חוצה פלטפורמות)

&nbsp;&nbsp;&nbsp;&nbsp; זוהי השיטה האמינה ביותר לציין במפורש ל-Python באיזה אוסף של תעודות בסיס להשתמש.

1.  **התקן את `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **השתמש ב-`certifi` בקוד שלך:** העבר את הנתיב לקובץ התעודות של `certifi` לפרמטר `verify` של הפונקציה `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # דוגמה ל-URL

    try:
        # מציין במפורש להשתמש בתעודות מ-certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # הקוד שלך לעיבוד התגובה
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("הקובץ הורד בהצלחה באמצעות תעודות certifi.")

    except requests.exceptions.RequestException as e:
        print(f"שגיאה בעת הורדת הקובץ: {e}")
    ```
    גם אם `requests` עשוי להשתמש ב-`certifi` כברירת מחדל, ציון מפורש של `verify=certifi.where()` מבטיח התנהגות זו.

### שיטה 4: שימוש במאגרי מערכת או במשתני סביבה (מתקדם)

&nbsp;&nbsp;&nbsp;&nbsp; המודול `ssl` של Python יכול גם לחפש תעודות במאגרי מערכת או בנתיבים המצוינים במשתני סביבה. זה שימושי, לדוגמה, בסביבות תאגידיות עם מרכזי אימות (CA) משלהם.

1.  **מאגרי מערכת:**
    *   **לינוקס/macOS:** Python משתמש לעתים קרובות באופן אוטומטי בתעודות המערכת (לדוגמה, מתוך `/etc/ssl/certs/`). וודא שהמערכת שלך מכילה תעודות בסיס עדכניות (`sudo apt update && sudo apt install ca-certificates` עבור Debian/Ubuntu, `sudo yum update ca-certificates` עבור CentOS/RHEL).
    *   **Windows:** Python *עשוי* לנסות להשתמש במאגר המערכת של Windows, אך זה לא תמיד עובד באופן אמין ללא חבילות נוספות (לדוגמה, `python-certifi-win32`). מומלץ להשתמש ב-`certifi` (שיטה 3).
2.  **משתני סביבה:** ניתן לציין במפורש נתיב לקובץ או ספרייה עם תעודות:
    *   `SSL_CERT_FILE`: ציין נתיב ל*קובץ* (בפורמט PEM) המכיל את כל תעודות הבסיס המהימנות.
    *   `SSL_CERT_DIR`: ציין נתיב ל*ספרייה* שבה כל תעודה נמצאת בקובץ PEM נפרד עם שם בצורת hash (השתמש ב-`c_rehash` מתוך OpenSSL להכנת הספרייה).

    **כיצד להגדיר משתני סביבה:**

    *   **לינוקס/macOS (זמני, עבור הסשן הנוכחי):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, זמני):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, זמני):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    כדי להוסיף CA משלך (לדוגמה, ארגוני), עליך להוסיף את התעודה שלו לקובץ `SSL_CERT_FILE` או לספרייה `SSL_CERT_DIR`.

## שלב 3 (בונוס): כיצד ליצור תעודה בחתימה עצמית לפיתוח מקומי

&nbsp;&nbsp;&nbsp;&nbsp; אם אתה מפתח שרת ווב מקומי (API, אתר) ורוצה לבדוק אותו באמצעות HTTPS, תזדקק לתעודת SSL. מכיוון שאין לך דומיין ציבורי לקבלת תעודה מ-CA רגיל, באפשרותך ליצור תעודה *בחתימה עצמית*.

**שימוש ב-OpenSSL (חוצה פלטפורמות):**

1.  **בצע את הפקודה:** פקודה זו תיצור מפתח פרטי (`key.pem`) ואת התעודה עצמה (`cert.pem`), תקפה למשך 10 שנים, עבור `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: יוצר מפתח ללא הגנה באמצעות סיסמה (נוח לפיתוח).
    *   `-subj "/CN=localhost"`: מגדיר את ה-Common Name.
    *   `-addext "subjectAltName = ..."`: מוסיף Subject Alternative Names (חשוב עבור דפדפנים ולקוחות מודרניים).

2.  **השתמש ב-`key.pem` וב-`cert.pem`** בהגדרות של שרת הווב המקומי שלך (Flask, Django, Node.js וכו') כדי להפעיל HTTPS.

**שימוש ב-PowerShell (Windows 10/11):**

1.  **בצע את הפקודה ב-PowerShell (עם הרשאות מנהל מערכת):** פקודה זו תיצור תעודה ותכניס אותה למאגר התעודות של המחשב.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    ייתכן שתזדקק לייצא תעודה זו מתוך המאגר (`certlm.msc`) לקבצי `.pfx` או `.pem` כדי ששרת הווב שלך יוכל להשתמש בה.

**הערה:** דפדפנים ולקוחות HTTP (כולל `requests` ב-Python כברירת מחדל) לא יאמנו בתעודות בחתימה עצמית. בעת גישה לשרת כזה, תקבל אזהרה או שגיאת SSL. לצורך בדיקות תצטרך either להוסיף תעודה זו לתעודות הבסיס המהימנות של המערכת/הדפדפן שלך, או להשתמש ב-`verify=False` (עבור `requests`), או לציין את הנתיב לקובץ `cert.pem` שלך באמצעות `verify='/path/to/cert.pem'`.