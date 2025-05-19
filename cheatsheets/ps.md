**מדריך לפקודות PowerShell**

**1. יסודות ניווט ועבודה עם קבצים ומדריכים**

*   **`Get-ChildItem` (או `gci`, `ls`, `dir`)**: מקבל רשימה של קבצים ותת-מדריכים במיקום שצוין.
    *   **תחביר**: `Get-ChildItem [נתיב] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Path`: מציין את הנתיב למדריך.
        *   `-Include`: מסנן לפי שם קובץ (עם תווים כלליים `*` ו-`?`).
        *   `-Exclude`: מדיר קבצים לפי שם.
        *   `-Recurse`: מציג קבצים ותיקיות בכל תת-המדריכים.
        *   `-Force`: הצג קבצים מוסתרים
        *   `-File`: הצג קבצים בלבד
        *   `-Directory`: הצג תיקיות בלבד
    *   **דוגמאות:**
        *   `Get-ChildItem`: רשימת קבצים ותיקיות במדריך הנוכחי.
        *   `Get-ChildItem -Path C:\Users\User\Documents`: רשימת קבצים ותיקיות ב-`C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt`: רשימת קבצי טקסט בלבד במדריך הנוכחי.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory`: הצג את כל המדריכים בכונן C
        *  `Get-ChildItem -Force`: הצג את כל הקבצים, כולל מוסתרים

*   **`Set-Location` (או `sl`, `cd`)**: משנה את המדריך הנוכחי.
    *   **תחביר**: `Set-Location [נתיב]`
    *   **דוגמאות:**
        *   `Set-Location C:\Windows`: מעבר למדריך `C:\Windows`.
        *   `Set-Location ..`: מעבר למדריך האב.
        * `Set-Location /` - מעבר לשורש הכונן
*   **`New-Item`**: יוצר קובץ או מדריך חדש.
    *   **תחביר**: `New-Item -Path [נתיב] -ItemType [סוג] -Name [שם]`
    *   **פרמטרים עיקריים:**
        *   `-ItemType`: `file` או `directory`.
        *   `-Name`: שם הפריט החדש.
        *   `-Value`: תוכן הקובץ.
    *   **דוגמאות:**
        *   `New-Item -ItemType directory -Name NewFolder`: יצירת תיקייה `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt`: יצירת קובץ ריק `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"`: יצירת קובץ `myfile.txt` עם תוכן.

*  **`Remove-Item` (או `rm`, `del`, `erase`)**: מסיר קבצים ומדריכים.
    *   **תחביר:** `Remove-Item [נתיב] [פרמטרים]`
    *   **פרמטרים עיקריים:**
         *   `-Recurse`:  הסר את כל תת-המדריכים
        *   `-Force`: הסרה כפויה (כולל קבצים "לקריאה בלבד" ומדריכים).
       *  `-Confirm` - בקש אישור עבור כל הסרה
    *   **דוגמאות:**
        *   `Remove-Item myfile.txt`: הסרת קובץ `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force`: הסרת תיקייה `C:\Temp` עם כל התיקיות והקבצים המקוננים.

*   **`Copy-Item`**: מעתיק קבצים ומדריכים.
    *   **תחביר**: `Copy-Item [נתיב_מקור] [נתיב_יעד] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Recurse`: העתקת כל תת-המדריכים.
        *   `-Force`: דריסת קבצים קיימים ללא בקשה.
    *   **דוגמאות:**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt`: העתקת קובץ `myfile.txt` ל-`mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse`: העתקת תיקייה `C:\Source` עם כל תת-המדריכים לתיקייה `D:\Backup`.

*   **`Move-Item`**: מזיז קבצים ומדריכים.
    *   **תחביר**: `Move-Item [נתיב_מקור] [נתיב_יעד] [פרמטרים]`
      *  `-Force` - העבר בכפייה ודרוס

    *   **דוגמאות:**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents`: העברת קובץ `myfile.txt` לתיקייה `D:\Documents`.
         *   `Move-Item -Path "C:\MyFolder" -Destination "D:\" -Force`: העברת תיקייה C:\MyFolder ל-D:\ בכפייה, גם אם כבר קיימת שם תיקייה בשם זה

*   **`Rename-Item`**: משנה שם של קובץ או מדריך.
    *   **תחביר**: `Rename-Item -Path [נתיב] -NewName [שם_חדש]`
    *   **דוגמה:**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt`: שינוי שם קובץ `myfile.txt` ל-`newfile.txt`.

*   **`Get-Content` (או `gc`)**: מציג או מקבל את תוכן הקובץ.
    *   **תחביר**: `Get-Content [נתיב]`
    *   **דוגמה:**
        *   `Get-Content myfile.txt`: הצגת תוכן קובץ `myfile.txt`.
*   **`Set-Content`**: מחליף או יוצר תוכן קובץ.
    *  **תחביר:** `Set-Content [נתיב] [פרמטרים]`
        *  `-value` - טקסט לכתיבה
   *   **דוגמה:** `Set-Content myfile.txt "Новый текст"` - החלפת טקסט קובץ `myfile.txt`

*   **`Add-Content`**: מוסיף תוכן בסוף הקובץ.
   * **תחביר:** `Add-Content [נתיב] [פרמטרים]`
       *  `-value` - טקסט להוספה

   *   **דוגמה:** `Add-Content myfile.txt "Еще текст"` - הוספת טקסט בסוף `myfile.txt`

**2. ניהול תהליכים:**

*   **`Get-Process` (או `gps`)**: מקבל רשימה של תהליכים פועלים.
    *   **תחביר**: `Get-Process [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Name`: סינון לפי שם תהליך.
        *   `-Id`: סינון לפי מזהה תהליך.
        *    `-IncludeUserName`: הצגת המשתמש שהפעיל את התהליך
    *   **דוגמאות:**
        *   `Get-Process`: רשימת כל התהליכים הפועלים.
        *   `Get-Process -Name notepad`: רשימת תהליכים בשם `notepad`.
        *    `Get-Process -IncludeUserName`: רשימת כל התהליכים הפועלים עם המשתמשים.

*   **`Stop-Process`**: מסיים תהליך.
    *   **תחביר**: `Stop-Process [פרמטרים]`
     *  `-Id` - ציין מזהה תהליך
    *   `-Name` - ציין שם תהליך
    *  `-Force` - סיים תהליך בכפייה
    *   **דוגמאות:**
        *   `Stop-Process -Name notepad`: סיום כל תהליכי `notepad`.
         *    `Stop-Process -Id 1234` : סיום תהליך עם מזהה 1234.
        *    `Stop-Process -Name chrome -Force` : סיום כל תהליכי `chrome` בכפייה.

**3. ניהול שירותים:**

*   **`Get-Service`**: מקבל רשימה של שירותים.
    *   **תחביר**: `Get-Service [פרמטרים]`
    *   **פרמטרים עיקריים:**
         * `-Name`: הצג שירותים עם השם שצוין בלבד
         * `-DisplayName`: הצג שירותים עם השם המוצג שצוין בלבד
        *   `-Status`: מסנן לפי מצב (Running, Stopped).
    *   **דוגמאות:**
        *   `Get-Service`: רשימת כל השירותים.
        *   `Get-Service -Name Spooler`: הצג את השירות Spooler.
       *   `Get-Service -Status Running`: הצגת שירותים פועלים.
*  **`Start-Service`**: מפעיל שירות.
   *   **תחביר**: `Start-Service [שם_שירות]`
   *   **דוגמה:** `Start-Service Spooler` - הפעלת שירות Spooler

*   **`Stop-Service`**: עוצר שירות.
    *   **תחביר**: `Stop-Service [שם_שירות]`
        *  `-Force` - עצור שירות בכפייה
    *   **דוגמה:** `Stop-Service Spooler`: עצירת שירות Spooler.
        *   `Stop-Service Spooler -Force` - עצירת שירות Spooler בכפייה.

*  **`Restart-Service`**: מפעיל מחדש שירות.
   *   **תחביר:** `Restart-Service [שם_שירות]`
   *   **דוגמה:** `Restart-Service Spooler` - הפעלה מחדש של שירות Spooler.

**4. עבודה עם רשת**

*   **`Test-NetConnection`**: בודק חיבור רשת.
    *   **תחביר**: `Test-NetConnection [שם_מארח_או_כתובת_ip] [פרמטרים]`
    *  `-Port` - מספר פורט
    *   **דוגמאות:**
        *   `Test-NetConnection google.com`: בדיקת חיבור ל-`google.com`.
        * `Test-NetConnection google.com -Port 80`: בדיקת חיבור ל-google.com בפורט 80
*   **`Get-NetIPConfiguration`**: מקבל את תצורת הרשת.
    *   **תחביר**: `Get-NetIPConfiguration`
    *   **דוגמה:**
        *   `Get-NetIPConfiguration`: הצגת תצורת הרשת.
*   **`Resolve-DnsName`**: מאחזר מידע DNS.
    *   **תחביר**: `Resolve-DnsName [שם_מארח]`
    *   **דוגמה:** `Resolve-DnsName google.com`: אחזור מידע DNS עבור `google.com`.

**5. עבודה עם הרישום (Registry)**

*   **`Get-ItemProperty`**: מקבל ערך מאפיין מהרישום.
    *   **תחביר**: `Get-ItemProperty -Path [נתיב_ברישום]`
    *   **דוגמה:** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`
*   **`Set-ItemProperty`**: קובע ערך מאפיין ברישום.
    *   **תחביר**: `Set-ItemProperty -Path [נתיב_ברישום] -Name [שם_מאפיין] -Value [ערך]`
    *   **דוגמה:** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

**6. שונות**

*   **`Clear-Host`**: מנקה את מסך הקונסולה.
    *   **תחביר:** `Clear-Host`
*   **`Get-Date`**: מקבל את התאריך והשעה הנוכחיים.
    *   **תחביר:** `Get-Date`
*    **`Start-Process`**: מפעיל תוכנית או פותח קובץ.
    *   **תחביר:** `Start-Process [שם_תוכנית_או_קובץ] [אפשרויות]`
   *   **דוגמאות:**
        *   `Start-Process notepad.exe`: הפעלת פנקס רשימות.
        *   `Start-Process myfile.txt`: פתיחת קובץ `myfile.txt` באמצעות התוכנית ברירת מחדל.
        *   `Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com"` - פתיחת אתר בכרום

*   **`Get-Help`**: מציג עזרה עבור פקודה.
    *   **תחביר**: `Get-Help [שם_פקודה]`
    *   **דוגמה:** `Get-Help Get-Process`: הצגת עזרה עבור פקודה `Get-Process`.
*   **`Exit`**: מסיים סשן PowerShell
    *   **תחביר:** `Exit`
*  **`Get-Variable`**: מציג משתנים נוכחיים
    *  **תחביר**: `Get-Variable`
*  **`Get-Alias`**: מציג כינויי פקודות
    *   **תחביר**: `Get-Alias`
*   **`Set-Alias`**: יוצר כינוי לפקודה
    *  **תחביר**: `Set-Alias [שם_כינוי] [שם_פקודה]`
    *  **דוגמה**: `Set-Alias gci Get-ChildItem`

**הערות:**

*   פקודות (`cmdlets`) ב-`PowerShell` בדרך כלל בעלות מבנה של `פועל-שם עצם` (לדוגמה, `Get-Process`, `Set-Location`).
*   `PowerShell` אינו תלוי רישיות, כך שניתן לכתוב פקודות כ-`Get-ChildItem` או `get-childitem`.
*   `PowerShell` עובד עם אובייקטים, כך שניתן להשתמש באופרטור `|` להעברת פלט של פקודה אחת כקלט לפקודה אחרת (לדוגמה, `Get-Process | Sort-Object -Property CPU`).
*  פקודות רבות תומכות בשימוש בתווים כלליים (`*`) לעבודה עם מספר קבצים (לדוגמה `Get-ChildItem *.txt`).
*   נדרשות הרשאות מנהל מערכת עבור עבודה עם חלק מהפקודות.