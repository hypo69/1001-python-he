# כיצד לתקן את השגיאה SSLCertVerificationError ב-Python

&nbsp;&nbsp;&nbsp;&nbsp; נתקלתם בשגיאה `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` בעת ניסיון לבצע בקשת HTTPS ב-Python באמצעות `requests` או `urllib3`?
במאמר זה אציג כיצד לאבחן ולתקן בעיה זו.

השגיאה מצביעה על כך ש-Python לא הצליחה לאמת את אישור ה-SSL/TLS של אתר האינטרנט שאליו אתם מנסים להתחבר, מכיוון שהיא לא מצאה אישור בסיס (root certificate) מהימן במאגר שלה.

## שלב 1: אבחון הבעיה באמצעות OpenSSL (מומלץ)

&nbsp;&nbsp;&nbsp;&nbsp; לפני שאתם משנים את קוד ה-Python, בדקו את חיבור ה-SSL באמצעות כלי העזר `openssl`. זה יעזור להבין אם הבעיה ספציפית ל-Python או קשורה להגדרות המערכת או לשרת עצמו.

1.  **התקינו את OpenSSL**, אם אין לכם אותו (לרוב מותקן מראש ב-Linux/macOS; עבור Windows הורידו מה [אתר הרשמי](https://www.openssl.org/source/) או השתמשו במנהלי חבילות כמו Chocolatey/Scoop).
2.  **הריצו את הפקודה** במסוף (שורת הפקודה) שלכם, החליפו את `<hostname>` בכתובת האתר (ללא `https://`) ואת `<port>` בפורט (בדרך כלל 443 עבור HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # דוגמה עבור rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **נתחו את הפלט:** שימו לב לשורה `Verify return code`. אם היא מכילה שגיאה כמו `unable to get local issuer certificate` (קוד 20) או `certificate verify failed` (קוד 21), זה מאשר את הבעיה עם האמון באישור ברמת המערכת או המאגר שבו משתמש OpenSSL.

## שלב 2: בחרו שיטת פתרון

&nbsp;&nbsp;&nbsp;&nbsp; קיימות מספר דרכים לתיקון השגיאה `SSLCertVerificationError`. בחרו את הדרך המתאימה ביותר למצבכם.

### שיטה 1: לבטל את אימות SSL (מהיר, אך לא בטוח)

&nbsp;&nbsp;&nbsp;&nbsp; שיטה זו מבטלת לחלוטין את אימות האישור. השתמשו בה **רק** לצורך בדיקות זמניות, סקריפטים חד-פעמיים ו**רק** עבור אתרים שאתם בוטחים בהם לחלוטין.

⚠️ **אזהרה:** ביטול האימות הופך את החיבור שלכם לפגיע להתקפות "אדם באמצע" (MITM). **לעולם אל תשתמשו ב-`verify=False` בקוד בסביבת ייצור (production) או בעבודה עם נתונים רגישים!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # דוגמה לכתובת URL

# מבטלים את אימות SSL
try:
    # מדכאים אזהרות על בקשות לא מאובטחות (אופציונלי)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # בודקים שגיאות HTTP (4xx, 5xx)

    # הקוד שלכם לטיפול בתגובה, לדוגמה, שמירת קובץ
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("הקובץ הורד בהצלחה (עם אימות SSL מושבת).")

except requests.exceptions.RequestException as e:
    print(f"שגיאה בעת הורדת הקובץ: {e}")

finally:
    # חשוב: אם ביטלתם אזהרות באופן גלובלי,
    # ייתכן שתרצו להפעיל אותן שוב לאחר ביצוע הבקשה,
    # אם כי לרוב זה לא נדרש אם הסקריפט מסתיים.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### שיטה 2: להתקין/לעדכן אישורים עבור Python (תלוי פלטפורמה)

&nbsp;&nbsp;&nbsp;&nbsp; Python עשויה להגיע עם סקריפטים להתקנה או עדכון של אוסף אישורי הבסיס מחבילת `certifi`.

*   **ב-macOS:**
    1.  עברו לתיקיית ההתקנה של Python (בדרך כלל `/Applications/Python <גרסה>/`).
    2.  מצאו ולחצו פעמיים על הקובץ `Install Certificates.command`. הוא יתקין/יעדכן את `certifi` ויקשר את מודול ה-`ssl` הסטנדרטי לאישורים אלה.
*   **ב-Windows:**
    1.  לפעמים בעת התקנת Python נוצר סקריפט בשם `install_certificates.bat`. חפשו אותו בספריית `Scripts` בתוך תיקיית ההתקנה של Python (לדוגמה, `C:\Users\<שם_משתמש>\AppData\Local\Programs\Python\Python<גרסה>\Scripts\`).
    2.  אם מצאתם אותו, הריצו אותו.
    3.  אם הסקריפט לא קיים, שיטה זו כנראה לא תעבוד. השתמשו בשיטה 3.

### שיטה 3: להשתמש בחבילת `certifi` ישירות (מומלץ, חוצת-פלטפורמות)

&nbsp;&nbsp;&nbsp;&nbsp; זו הדרך האמינה ביותר לציין במפורש ל-Python באיזה אוסף של אישורי בסיס להשתמש.

1.  **התקינו את `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **השתמשו ב-`certifi` בקוד שלכם:** העבירו את הנתיב לקובץ האישורים של `certifi` לפרמטר `verify` בפונקציה `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # דוגמה לכתובת URL

    try:
        # מציינים במפורש להשתמש באישורים מ-certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # הקוד שלכם לטיפול בתגובה
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("הקובץ הורד בהצלחה באמצעות אישורי certifi.")

    except requests.exceptions.RequestException as e:
        print(f"שגיאה בעת הורדת הקובץ: {e}")
    ```
    גם אם `requests` יכול להשתמש ב-`certifi` כברירת מחדל, ציון מפורש של `verify=certifi.where()` מבטיח התנהגות זו.

### שיטה 4: להשתמש במאגרים מערכתיים או במשתני סביבה (מתקדם)

&nbsp;&nbsp;&nbsp;&nbsp; מודול ה-`ssl` ב-Python יכול גם לחפש אישורים במאגרים המערכתיים או בנתיבים המצוינים במשתני סביבה. זה שימושי, למשל, בסביבות ארגוניות עם רשויות אישורים (CA) משלהן.

1.  **מאגרים מערכתיים:**
    *   **Linux/macOS:** Python לרוב משתמש אוטומטית באישורים המערכתיים (לדוגמה, מתוך `/etc/ssl/certs/`). ודאו שלמערכת שלכם יש אישורי בסיס עדכניים (`sudo apt update && sudo apt install ca-certificates` עבור Debian/Ubuntu, `sudo yum update ca-certificates` עבור CentOS/RHEL).
    *   **Windows:** Python *עשויה* לנסות להשתמש במאגר המערכתי של Windows, אך זה לא תמיד עובד באמינות ללא חבילות נוספות (לדוגמה, `python-certifi-win32`). מומלץ להשתמש ב-`certifi` (שיטה 3).
2.  **משתני סביבה:** אתם יכולים לציין במפורש נתיב לקובץ או לספרייה עם אישורים:
    *   `SSL_CERT_FILE`: ציינו נתיב ל*קובץ* (בפורמט PEM) המכיל את כל אישורי הבסיס המהימנים.
    *   `SSL_CERT_DIR`: ציינו נתיב ל*ספרייה* שבה כל אישור נמצא בקובץ PEM נפרד עם שם בצורת גיבוב (hash) (השתמשו ב-`c_rehash` מתוך OpenSSL להכנת הספרייה).

    **כיצד להגדיר משתני סביבה:**

    *   **Linux/macOS (זמנית, לסשן הנוכחי):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, זמנית):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, זמנית):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    כדי להוסיף רשות אישורים (CA) מותאמת אישית משלכם (לדוגמה, ארגונית), עליכם להוסיף את האישור שלה לקובץ `SSL_CERT_FILE` או לספרייה `SSL_CERT_DIR`.

## שלב 3 (בונוס): כיצד ליצור אישור בחתימה עצמית לפיתוח מקומי

&nbsp;&nbsp;&nbsp;&nbsp; אם אתם מפתחים שרת ווב מקומי (API, אתר) ורוצים לבדוק אותו באמצעות HTTPS, תזדקקו לאישור SSL. מכיוון שאין לכם דומיין ציבורי לצורך קבלת אישור מרשות אישורים (CA) רגילה, תוכלו ליצור אישור *בחתימה עצמית*.

**שימוש ב-OpenSSL (חוצה-פלטפורמות):**

1.  **הריצו את הפקודה:** פקודה זו תיצור מפתח פרטי (`key.pem`) ואת האישור עצמו (`cert.pem`), תקפים ל-10 שנים, עבור `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: יוצר מפתח ללא הגנת סיסמה (נוח לפיתוח).
    *   `-subj "/CN=localhost"`: מגדיר את ה-Common Name.
    *   `-addext "subjectAltName = ..."`: מוסיף Subject Alternative Names (חשוב עבור דפדפנים ולקוחות מודרניים).

2.  **השתמשו בקבצים `key.pem` ו-`cert.pem`** בהגדרות שרת הווב המקומי שלכם (Flask, Django, Node.js וכו') כדי להפעיל HTTPS.

**שימוש ב-PowerShell (Windows 10/11):**

1.  **הריצו את הפקודה ב-PowerShell (עם הרשאות מנהל):** פקודה זו תיצור את האישור ותניח אותו במאגר האישורים של המחשב.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    ייתכן שתידרשו לייצא אישור זה מהמאגר (`certlm.msc`) לקבצי `.pfx` או `.pem` לצורך שימוש על ידי שרת הווב שלכם.

**הערה:** דפדפנים ולקוחות HTTP (כולל Python `requests` כברירת מחדל) לא יבטחו באישורים בחתימה עצמית. בעת גישה לשרת כזה תקבלו אזהרה או שגיאת SSL. לצורך בדיקות תצטרכו או להוסיף אישור זה לאישורי הבסיס המהימנים של המערכת/דפדפן שלכם, או להשתמש ב-`verify=False` (עבור `requests`), או לציין את הנתיב לקובץ `cert.pem` שלכם באמצעות `verify='/path/to/cert.pem'`.