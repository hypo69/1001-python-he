**מדריך לפקודות PowerShell**

**1. יסודות הניווט ועבודה עם קבצים ומדריכים**

*   **`Get-ChildItem` (או `gci`, `ls`, `dir`)**: מקבל רשימה של קבצים ותת-מדריכים במיקום שצוין.
    *   **תחביר**: `Get-ChildItem [path] [parameters]`
    *   **פרמטרים עיקריים:**
        *   `-Path`: מציין את הנתיב למדריך.
        *   `-Include`: מסנן לפי שם קובץ (עם תווי כלליות `*` ו-`?`).
        *   `-Exclude`: מוציא קבצים לפי שם.
        *   `-Recurse`: מציג קבצים ותיקיות בכל תת-המדריכים.
        *   `-Force`: הצג קבצים מוסתרים.
        *   `-File`: הצג קבצים בלבד.
        *   `-Directory`: הצג תיקיות בלבד.
    *   **דוגמאות:**
        *   `Get-ChildItem`: רשימת קבצים ותיקיות במדריך הנוכחי.
        *   `Get-ChildItem -Path C:\Users\User\Documents`: רשימת קבצים ותיקיות ב-`C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt`: רשימה של קבצי טקסט בלבד במדריך הנוכחי.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory`: הצגת כל המדריכים בכונן C.
        *   `Get-ChildItem -Force`: הצגת כל הקבצים, כולל מוסתרים.

*   **`Set-Location` (או `sl`, `cd`)**: משנה את המדריך הנוכחי.
    *   **תחביר**: `Set-Location [path]`
    *   **דוגמאות:**
        *   `Set-Location C:\Windows`: מעבר למדריך `C:\Windows`.
        *   `Set-Location ..`: מעבר למדריך האב.
        *   `Set-Location /`: מעבר לשורש הכונן.

*   **`New-Item`**: יוצר קובץ או מדריך חדש.
    *   **תחביר**: `New-Item -Path [path] -ItemType [type] -Name [name]`
    *   **פרמטרים עיקריים:**
        *   `-ItemType`: `file` או `directory`.
        *   `-Name`: שם הפריט החדש.
        *   `-Value`: תוכן הקובץ.
    *   **דוגמאות:**
        *   `New-Item -ItemType directory -Name NewFolder`: יצירת תיקייה בשם `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt`: יצירת קובץ ריק בשם `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"`: יצירת קובץ בשם `myfile.txt` עם תוכן.

*   **`Remove-Item` (או `rm`, `del`, `erase`)**: מוחק קבצים ומדריכים.
    *   **תחביר:** `Remove-Item [path] [parameters]`
    *   **פרמטרים עיקריים:**
        *   `-Recurse`: מחיקת כל תת-המדריכים.
        *   `-Force`: מחיקה בכפייה (כולל קבצים "לקריאה בלבד" ומדריכים).
        *   `-Confirm`: בקשת אישור לכל מחיקה.
    *   **דוגמאות:**
        *   `Remove-Item myfile.txt`: מחיקת הקובץ `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force`: מחיקת התיקייה `C:\Temp` עם כל התיקיות והקבצים המקוננים.

*   **`Copy-Item`**: מעתיק קבצים ומדריכים.
    *   **תחביר**: `Copy-Item [source_path] [destination_path] [parameters]`
    *   **פרמטרים עיקריים:**
        *   `-Recurse`: העתקת כל תת-המדריכים.
        *   `-Force`: דריסה של קבצים קיימים ללא בקשה.
    *   **דוגמאות:**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt`: העתקת הקובץ `myfile.txt` ל-`mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse`: העתקת התיקייה `C:\Source` עם כל תת-המדריכים לתיקייה `D:\Backup`.

*   **`Move-Item`**: מעביר קבצים ומדריכים.
    *   **תחביר**: `Move-Item [source_path] [destination_path] [parameters]`
    *   `-Force`: העברה ודריסה בכפייה.
    *   **דוגמאות:**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents`: העברת הקובץ `myfile.txt` לתיקייה `D:\Documents`.
        *   `Move-Item -Path "C:\MyFolder" -Destination "D:\" -Force`: העברת התיקייה `C:\MyFolder` לכונן `D:\` בכפייה, גם אם קיימת שם כבר תיקייה באותו השם.

*   **`Rename-Item`**: משנה שם של קובץ או מדריך.
    *   **תחביר**: `Rename-Item -Path [path] -NewName [new_name]`
    *   **דוגמה:**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt`: שינוי שם הקובץ `myfile.txt` ל-`newfile.txt`.

*   **`Get-Content` (או `gc`)**: מציג או מקבל את תוכן הקובץ.
    *   **תחביר**: `Get-Content [path]`
    *   **דוגמה:**
        *   `Get-Content myfile.txt`: הצגת תוכן הקובץ `myfile.txt`.

*   **`Set-Content`**: מחליף או יוצר תוכן של קובץ.
    *   **תחביר:** `Set-Content [path] [parameters]`
    *   `-value`: טקסט לכתיבה.
    *   **דוגמה:** `Set-Content myfile.txt "Новый текст"`: החלפת הטקסט של הקובץ `myfile.txt`.

*   **`Add-Content`**: מוסיף תוכן לסוף קובץ.
    *   **תחביר:** `Add-Content [path] [parameters]`
    *   `-value`: טקסט להוספה.
    *   **דוגמה:** `Add-Content myfile.txt "Еще текст"`: הוספת טקסט לסוף `myfile.txt`.

**2. ניהול תהליכים:**

*   **`Get-Process` (או `gps`)**: מקבל רשימה של תהליכים פועלים.
    *   **תחביר**: `Get-Process [parameters]`
    *   **פרמטרים עיקריים:**
        *   `-Name`: סינון לפי שם התהליך.
        *   `-Id`: סינון לפי מזהה התהליך.
        *   `-IncludeUserName`: הצגת המשתמש שהריץ את התהליך.
    *   **דוגמאות:**
        *   `Get-Process`: רשימה של כל התהליכים הפועלים.
        *   `Get-Process -Name notepad`: רשימה של תהליכים בשם `notepad`.
        *   `Get-Process -IncludeUserName`: רשימה של כל התהליכים הפועלים כולל המשתמשים.

*   **`Stop-Process`**: מסיים תהליך.
    *   **תחביר**: `Stop-Process [parameters]`
    *   `-Id`: ציון מזהה התהליך.
    *   `-Name`: ציון שם התהליך.
    *   `-Force`: סיום התהליך בכפייה.
    *   **דוגמאות:**
        *   `Stop-Process -Name notepad`: סיום כל התהליכים בשם `notepad`.
        *   `Stop-Process -Id 1234`: סיום התהליך עם המזהה 1234.
        *   `Stop-Process -Name chrome -Force`: סיום בכפייה של כל התהליכים בשם `chrome`.

**3. ניהול שירותים:**

*   **`Get-Service`**: מקבל רשימה של שירותים.
    *   **תחביר**: `Get-Service [parameters]`
    *   **פרמטרים עיקריים:**
        *   `-Name`: הצגת שירותים עם השם שצוין בלבד.
        *   `-DisplayName`: הצגת שירותים עם השם המוצג שצוין בלבד.
        *   `-Status`: סינון לפי סטטוס (Running, Stopped).
    *   **דוגמאות:**
        *   `Get-Service`: רשימה של כל השירותים.
        *   `Get-Service -Name Spooler`: הצגת השירות Spooler.
        *   `Get-Service -Status Running`: הצגת שירותים פועלים.

*   **`Start-Service`**: מפעיל שירות.
    *   **תחביר**: `Start-Service [service_name]`
    *   **דוגמה:** `Start-Service Spooler`: הפעלת השירות Spooler.

*   **`Stop-Service`**: עוצר שירות.
    *   **תחביר**: `Stop-Service [service_name]`
    *   `-Force`: עצירת השירות בכפייה.
    *   **דוגמה:** `Stop-Service Spooler`: עצירת השירות Spooler.
        *   `Stop-Service Spooler -Force`: עצירת השירות Spooler בכפייה.

*   **`Restart-Service`**: מפעיל שירות מחדש.
    *   **תחביר:** `Restart-Service [service_name]`
    *   **דוגמה:** `Restart-Service Spooler`: הפעלת השירות Spooler מחדש.

**4. עבודה עם רשת**

*   **`Test-NetConnection`**: בודק חיבור רשת.
    *   **תחביר**: `Test-NetConnection [hostname_or_ip_address] [parameters]`
    *   `-Port`: מספר פורט.
    *   **דוגמאות:**
        *   `Test-NetConnection google.com`: בדיקת חיבור ל-`google.com`.
        *   `Test-NetConnection google.com -Port 80`: בדיקת חיבור ל-`google.com` בפורט 80.

*   **`Get-NetIPConfiguration`**: מקבל את תצורת הרשת.
    *   **תחביר**: `Get-NetIPConfiguration`
    *   **דוגמה:**
        *   `Get-NetIPConfiguration`: הצגת תצורת הרשת.

*   **`Resolve-DnsName`**: מבקש מידע אודות DNS.
    *   **תחביר**: `Resolve-DnsName [hostname]`
    *   **דוגמה:** `Resolve-DnsName google.com`: בקשת מידע DNS עבור `google.com`.

**5. עבודה עם ה-Registry**

*   **`Get-ItemProperty`**: מקבל את ערך המאפיין מה-Registry.
    *   **תחביר**: `Get-ItemProperty -Path [registry_path]`
    *   **דוגמה:** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`

*   **`Set-ItemProperty`**: מגדיר ערך של מאפיין ב-Registry.
    *   **תחביר**: `Set-ItemProperty -Path [registry_path] -Name [property_name] -Value [value]`
    *   **דוגמה:** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

**6. אחר**

*   **`Clear-Host`**: מנקה את מסך הקונסולה.
    *   **תחביר:** `Clear-Host`

*   **`Get-Date`**: מקבל את התאריך והשעה הנוכחיים.
    *   **תחביר:** `Get-Date`

*   **`Start-Process`**: מפעיל תוכנית או פותח קובץ.
    *   **תחביר:** `Start-Process [program_or_file_name] [options]`
    *   **דוגמאות:**
        *   `Start-Process notepad.exe`: הפעלת Notepad.
        *   `Start-Process myfile.txt`: פתיחת הקובץ `myfile.txt` עם התוכנית המוגדרת כברירת מחדל.
        *   `Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com"`: פתיחת אתר ב-Chrome.

*   **`Get-Help`**: מציג עזרה אודות פקודה.
    *   **תחביר**: `Get-Help [command_name]`
    *   **דוגמה:** `Get-Help Get-Process`: הצגת עזרה אודות הפקודה `Get-Process`.

*   **`Exit`**: מסיים את סשן ה-PowerShell.
    *   **תחביר:** `Exit`

*   **`Get-Variable`**: מציג את המשתנים הנוכחיים.
    *   **תחביר**: `Get-Variable`

*   **`Get-Alias`**: מציג את כינויי הפקודות (aliases).
    *   **תחביר**: `Get-Alias`

*   **`Set-Alias`**: יוצר כינוי (alias) עבור פקודה.
    *   **תחביר**: `Set-Alias [alias_name] [command_name]`
    *   **דוגמה**: `Set-Alias gci Get-ChildItem`

**הערות:**

*   פקודות `PowerShell` (cmdlets) הן בדרך כלל בצורת `פועל-שם_עצם` (לדוגמה, `Get-Process`, `Set-Location`).
*   `PowerShell` אינו תלוי רישיות (case-insensitive), לכן ניתן לכתוב פקודות כ-`Get-ChildItem` או `get-childitem`.
*   `PowerShell` עובד עם אובייקטים, ולכן ניתן להשתמש באופרטור `|` להעברת הפלט של פקודה אחת לקלט של פקודה אחרת (לדוגמה, `Get-Process | Sort-Object -Property CPU`).
*   פקודות רבות תומכות בשימוש בתווי כלליות (wildcards - *) לעבודה עם מספר קבצים (לדוגמה, `Get-ChildItem *.txt`).
*   עבור עבודה עם פקודות מסוימות נדרשות הרשאות מנהל מערכת.