# 🔄 עדכון פורק GitHub באמצעות PowerShell — מאפס לאוטומציה

כיצד לשמור על הפורק שלכם מעודכן מבלי להשקיע בכך זמן רב?

במאמר זה, אראה כיצד לעדכן בקלות את הפורק שלכם ב-GitHub באמצעות PowerShell. כתוצאה מכך, תקבלו כלי אשר:

*   עובד עם **כל ענף פעיל** בפורק שלכם.
*   **מושך אוטומטית שינויים חדשים** ממאגר ה-`upstream`.
*   מבצע **`rebase`** לשמירה על היסטוריית קומיטים נקייה.
*   שולח באופן כפוי (`push --force`) את הענף המעודכן לפורק שלכם (`origin`).
*   ואפילו מציג **התראות ויזואליות על התהליך ב-Windows!**

## ✅ הכנה

לפני שנתחיל:

1.  ודאו שמאגר ה-`upstream` נוסף למאגר שלכם המצביע על המאגר **המקורי**:

    ```bash
    git remote add upstream https://github.com/ОригинальныйПроект/репозиторий.git
    ```
    *(החליפו את ה-URL בכתובת המתאימה לפרויקט שלכם)*

2.  התקינו את מודול ההתראות \[BurntToast] כדי לקבל התראות על התהליך (שימושי במיוחד לאוטומציה):

    ```powershell
    Install-Module -Name BurntToast -Force -Scope CurrentUser
    ```

---

## חלק 1: עדכון פורק באמצעות פקודות ב-PowerShell (שיטה ידנית)

לפני שניצור פונקציה, בואו נבין אילו פקודות מתבצעות בפועל כדי לעדכן את הפורק. נניח שאתם כבר נמצאים בתיקייה של הפורק המקומי שלכם.

1.  **מעבר לתיקיית המאגר** (אם אינכם נמצאים בה כבר):
    ```powershell
    Set-Location -Path "C:\путь\к\вашему\форку"
    # או cd "C:\путь\к\вашему\форку"
    ```

2.  **זיהוי הענף הנוכחי**:
    ```powershell
    $currentBranch = git rev-parse --abbrev-ref HEAD
    Write-Host "ענף נוכחי: $currentBranch"
    ```

3.  **קבלת שינויים מ-`upstream`**:
    ```powershell
    Write-Host "מביא עדכונים מ-upstream..."
    git fetch upstream
    ```

4.  **ביצוע `rebase` לענף הנוכחי על בסיס הענף המקביל מ-`upstream`**:
    ```powershell
    Write-Host "מבצע rebase מול upstream/$currentBranch..."
    git rebase "upstream/$currentBranch"
    ```

5.  **טיפול בקונפליקטים (אם מתרחשים)**:
    אם `git rebase` מדווח על קונפליקטים:
    *   פתחו את הקבצים עם הקונפליקטים בעורך ופתרו אותם.
    *   הוסיפו את הקבצים המתוקנים: `git add .`
    *   המשיכו את ה-rebase: `git rebase --continue`
    *   (או דלגו על הקומיט הקונפליקטואלי: `git rebase --skip`, או בטלו את ה-rebase כולו: `git rebase --abort`)

6.  **שליחת השינויים באופן כפוי ל-`origin` (הפורק שלכם ב-GitHub)**:
    ```powershell
    Write-Host "שולח (push) ל-origin/$currentBranch (עם --force)..."
    git push origin "$currentBranch" --force
    ```
    **אזהרה:** `git push --force` דורס את ההיסטוריה בענף המרוחק. השתמשו בזהירות, במיוחד אם אנשים אחרים עובדים על הענף.

7.  **(אופציונלי) הצגת התראה**:
    ```powershell
    # (דורש את מודול BurntToast)
    if ($LASTEXITCODE -eq 0) {
        New-BurntToastNotification -Text "✅ הפורק עודכן!"
    } else {
        New-BurntToastNotification -Text "❌ שגיאה בפעולת Git"
    }
    ```

כעת, כשאנו מבינים את השלבים הבסיסיים, נעשה להם אוטומציה באמצעות פונקציה.

---

## חלק 2: יצירת פונקציית PowerShell בשם `Update-Fork`

נאחד את כל הפקודות לפונקציה נוחה.

### 🧩 שלב 1. הפונקציה עוברת לתיקייה הרצויה ומזהה את הענף הנוכחי:

```powershell
function Update-Fork {
    param(
        [string]$GitDirectory = (Get-Location) # ברירת המחדל היא התיקייה הנוכחית
    )

    # מייבא את מודול ההתראות (אם עדיין לא נטען)
    Import-Module BurntToast -ErrorAction SilentlyContinue

    Write-Host "🔄 מעדכן פורק ב: $GitDirectory" -ForegroundColor Cyan
    Set-Location -Path $GitDirectory

    $currentBranch = git rev-parse --abbrev-ref HEAD

    if (-not $currentBranch) {
        Write-Host "❌ לא ניתן היה לזהות את הענף הנוכחי. ודא שאתה נמצא במאגר Git." -ForegroundColor Red
        New-BurntToastNotification -Text "❌ שגיאה", "לא נמצא במאגר Git"
        return
    }

    Write-Host "📍 ענף נוכחי: $currentBranch" -ForegroundColor Yellow
}
```
*   `param(...)`: מאפשר להעביר נתיב למאגר או להשתמש בנתיב הנוכחי.
*   `Import-Module BurntToast`: טוען את מודול ההתראות.
*   `Set-Location`: עובר לתיקייה הרצויה.
*   `git rev-parse --abbrev-ref HEAD`: מקבל את שם הענף הנוכחי.

### 🔁 שלב 2: נוסיף fetch ו-rebase

נמשוך שינויים ונבצע `rebase`. הוסיפו את הבלוק הזה *בתוך* הפונקציה `Update-Fork`, לאחר הגדרת `$currentBranch`:

```powershell
    # ... (קוד משלב 1) ...

    Write-Host "📥 מביא עדכונים מ-upstream..." -ForegroundColor Cyan
    git fetch upstream

    Write-Host "🛠️  מבצע rebase מול upstream/$currentBranch..." -ForegroundColor Cyan
    git rebase "upstream/$currentBranch"
```
*   `git fetch upstream`: מוריד שינויים מ-`upstream`.
*   `git rebase "upstream/$currentBranch"`: מעביר את הקומיטים המקומיים שלכם מעל השינויים האחרונים מ-`upstream`.

### ⚠️ שלב 3: טיפול בקונפליקטים

אם ה-`rebase` אינו מתבצע בצורה חלקה, PowerShell יעזור לכם להתמודד. הוסיפו את הבלוק הזה לאחר `git rebase ...`:

```powershell
    # ... (קוד משלבים 1 ו-2) ...

    if ($LASTEXITCODE -ne 0) { # $LASTEXITCODE מכיל את קוד החזרה של הפקודה האחרונה
        Write-Host "❗ קונפליקטים ב-rebase!" -ForegroundColor Red
        New-BurntToastNotification -Text "⚠️ קונפליקט ב-Rebase", "פתור ידנית או בחר פעולה"

        while ($true) {
            Write-Host "`nמה עושים?"
            Write-Host "1. המשך לאחר פתרון ידני (git add . -> Enter -> git rebase --continue)"
            Write-Host "2. דלג על קומיט קונפליקטואלי זה (git rebase --skip)"
            Write-Host "3. בטל את ה-rebase כולו (git rebase --abort)"
            Write-Host "4. צא (השאר rebase לטיפול ידני)"

            $choice = Read-Host "בחירה (1-4)"

            switch ($choice) {
                "1" {
                    Read-Host "ודא שהקונפליקטים נפתרו וביצעת 'git add .' לקבצים ששונו. לחץ Enter לביצוע 'git rebase --continue'"
                    git rebase --continue
                }
                "2" { git rebase --skip }
                "3" { git rebase --abort; Write-Host "Rebase בוטל."; return } # יציאה מהפונקציה
                "4" { Write-Host "יציאה. Rebase נשאר לניהול ידני."; return } # יציאה מהפונקציה
                default { Write-Host "❌ קלט לא חוקי." -ForegroundColor Red }
            }

            # בודק אם ה-rebase הסתיים
            $gitStatusOutput = git status
            if ($gitStatusOutput -notmatch "rebase in progress" -and $gitStatusOutput -notmatch "interactive rebase in progress") {
                Write-Host "מצב ה-rebase השתנה, יוצא מהלולאה." -ForegroundColor Green
                break # יציאה מלולאת while
            } else {
                 Write-Host "Rebase עדיין בתהליך..." -ForegroundColor Yellow
            }
        }
    }
```
*   בלוק זה מציע אפשרויות פעולה במקרה של קונפליקטים במהלך ה-`rebase`.

### 🚀 שלב 4: Push והתראה

בסיום נבצע `push` עם `--force` ונציג את התוצאה. הוסיפו את הבלוק הזה בסוף הפונקציה:

```powershell
    # ... (קוד משלבים 1, 2, 3) ...

    # בדיקה שה-rebase לא נשאר בתהליך (אם המשתמש בחר לצאת מתפריט הקונפליקטים)
    if ((git status) -match "rebase in progress") {
        Write-Host "⚠️ Rebase עדיין לא הסתיים. Push בוטל." -ForegroundColor Yellow
        New-BurntToastNotification -Text "❌ Rebase לא הסתיים", "Push בוטל. השלם את ה-rebase ידנית."
        return
    }

    Write-Host "🚀 שולח (push) ל-origin/$currentBranch (עם --force)..." -ForegroundColor Cyan
    git push origin "$currentBranch" --force

    if ($LASTEXITCODE -eq 0) {
        New-BurntToastNotification -Text "✅ הפורק עודכן!", "ניתן להמשיך לעבוד"
    } else {
        New-BurntToastNotification -Text "❌ שגיאה בעת ה-push", "בדוק ידנית"
    }
} # סוף פונקציית Update-Fork
```
*   לפני ה-`push` בודקים שה-`rebase` לא נשאר במצב לא גמור.

---

### 🧩 הגרסה הסופית של הפונקציה:

להלן הקוד המלא של פונקציית `Update-Fork`:

```powershell
function Update-Fork {
    param(
        [string]$GitDirectory = (Get-Location)
    )

    Import-Module BurntToast -ErrorAction SilentlyContinue

    Write-Host "🔄 מעדכן פורק ב: $GitDirectory" -ForegroundColor Cyan
    Set-Location -Path $GitDirectory

    $currentBranch = git rev-parse --abbrev-ref HEAD

    if (-not $currentBranch) {
        Write-Host "❌ לא נמצא במאגר Git" -ForegroundColor Red
        New-BurntToastNotification -Text "❌ שגיאה", "לא נמצא במאגר Git"
        return
    }

    Write-Host "📍 ענף נוכחי: $currentBranch" -ForegroundColor Yellow
    Write-Host "📥 מביא עדכונים מ-upstream..." -ForegroundColor Cyan
    git fetch upstream
    Write-Host "🛠️  מבצע rebase מול upstream/$currentBranch..." -ForegroundColor Cyan
    git rebase "upstream/$currentBranch"

    if ($LASTEXITCODE -ne 0) {
        New-BurntToastNotification -Text "⚠️ קונפליקט ב-rebase", "בחר פעולה"

        while ($true) {
            Write-Host "`nקונפליקט ב-rebase. מה עושים?"
            Write-Host "1. המשך לאחר פתרון ידני (git add . -> Enter -> git rebase --continue)"
            Write-Host "2. דלג על קומיט קונפליקטואלי זה (git rebase --skip)"
            Write-Host "3. בטל את ה-rebase כולו (git rebase --abort)"
            Write-Host "4. צא (השאר rebase לטיפול ידני)"

            $choice = Read-Host "בחירה (1-4)"

            switch ($choice) {
                "1" { Read-Host "לאחר פתרון הקונפליקטים ו-'git add .', לחץ Enter לביצוע 'git rebase --continue'"; git rebase --continue }
                "2" { git rebase --skip }
                "3" { git rebase --abort; Write-Host "Rebase בוטל."; return }
                "4" { Write-Host "יציאה. Rebase נשאר לניהול ידני."; return }
                default { Write-Host "❌ קלט לא חוקי." -ForegroundColor Red }
            }

            $gitStatusOutput = git status
            if ($gitStatusOutput -notmatch "rebase in progress" -and $gitStatusOutput -notmatch "interactive rebase in progress") {
                Write-Host "Rebase הסתיים או בוטל." -ForegroundColor Green
                break
            } else {
                 Write-Host "Rebase עדיין בתהליך..." -ForegroundColor Yellow
            }
        }
    }

    if ((git status) -match "rebase in progress") {
        Write-Host "⚠️ Rebase עדיין לא הסתיים. Push בוטל." -ForegroundColor Yellow
        New-BurntToastNotification -Text "❌ Rebase לא הסתיים", "Push בוטל. השלם את ה-rebase ידנית."
        return
    }

    Write-Host "🚀 שולח (push) ל-origin/$currentBranch (עם --force)..." -ForegroundColor Cyan
    git push origin "$currentBranch" --force

    if ($LASTEXITCODE -eq 0) {
        New-BurntToastNotification -Text "✅ הפורק עודכן!", "מוכן לעבודה"
    } else {
        New-BurntToastNotification -Text "❌ שגיאה בעת ה-push", "טפל ידנית"
    }
}
```

---

## 💡 כיצד להריץ את הפונקציה

תוכלו להשתמש ב-`Update-Fork` בכמה דרכים:

### 1. ידנית בסשן ה-PowerShell הנוכחי

העתיקו את כל קוד הפונקציה (מהגרסה הסופית) והדביקו אותו ישירות בחלון PowerShell.
*PowerShell תומך בהדבקת קוד מרובה שורות*. לאחר מכן תוכלו לקרוא לפונקציה:

```powershell
Update-Fork
```

או, אם אתם נמצאים בתיקייה אחרת, ציינו את הנתיב לפורק שלכם:

```powershell
Update-Fork -GitDirectory "C:\Путь\К\Вашему\Форку"
```

שיטה זו מתאימה לשימוש חד פעמי, שכן עם סגירת סשן ה-PowerShell הפונקציה תישכח. 😒

---

### 2. 🛠️ הוספת פונקציית `Update-Fork` לפרופיל ה-PowerShell

זוהי הדרך הנוחה ביותר, שכן היא תהפוך את פונקציית `Update-Fork` לזמינה בכל **סשן PowerShell חדש** מבלי צורך להעתיק את הקוד בכל פעם.

פרופיל PowerShell הוא סקריפט מיוחד (קובץ `.ps1`) אשר מופעל אוטומטית בכל פעם ש-PowerShell מופעל.

#### 📂 דרך Notepad

##### ✅ שלב 1. פתחו את PowerShell

*   לחצו על **Win + R**, הקלידו `powershell`, לחצו **Enter**.
*   או פתחו את PowerShell דרך תפריט ההתחלה.

##### 📄 שלב 2. בצעו את הפקודה לפתיחת קובץ הפרופיל ב-Notepad:

```powershell
notepad $PROFILE
```
🔍 **מה הפקודה הזו עושה?**
*   `$PROFILE` — זהו משתנה PowerShell מיוחד שמכיל את הנתיב לקובץ התצורה המשתמש שלכם. בדרך כלל זה משהו כמו `C:\Users\<שםהמשתמששלך>\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`.
*   `notepad` — פקודה להפעלת Notepad עם הקובץ שצוין.

##### 🧾 מה לעשות אם הקובץ לא קיים?

אם תראו הודעה בנוסח:
> **"הקובץ C:\Users\<שם>\Documents\PowerShell\Microsoft.PowerShell_profile.ps1 אינו קיים. האם ליצור אותו?"**

— לחצו בבטחה על **"כן"**. PowerShell יצור עבורכם קובץ פרופיל ריק.

##### ✏️ שלב 3. הדביקו את קוד הפונקציה

העתיקו את **כל הטקסט של הגרסה הסופית של פונקציית `Update-Fork`** (מופיע לעיל) והדביקו אותו לתוך הקובץ שנפתח ב-Notepad.

##### 💾 שלב 4. שמרו וסגרו

*   ב-Notepad בחרו "קובץ" -> "שמור" (או לחצו **Ctrl+S**).
*   סגרו את Notepad.

##### 🔄 שלב 5. הפעילו מחדש את PowerShell

*   סגרו את חלון ה-PowerShell הנוכחי.
*   פתחו חלון PowerShell חדש.

כעת פונקציית `Update-Fork` אמורה להיות זמינה. תוכלו לבדוק זאת על ידי ביצוע:

```powershell
Get-Command Update-Fork
```
אם הפקודה נמצאה, ביצעתם הכל נכון! 🎉 כעת תוכלו לקרוא ל-`Update-Fork` בכל מאגר.

---

#### 💡 חלופה: עריכת פרופיל דרך VS Code

אם אתם משתמשים ב-[Visual Studio Code (VS Code)](https://code.visualstudio.com/), עריכת הפרופיל בו עשויה להיות נוחה יותר בזכות הדגשת תחביר ופונקציות נוספות.

##### ✅ שלב 1. ודאו שהרחבת PowerShell מותקנת

1.  פתחו את VS Code.
2.  עברו ללשונית **Extensions** (הרחבות) — האייקון עם הריבועים בסרגל הצד או `Ctrl+Shift+X`.
3.  בחיפוש הקלידו `PowerShell`.
4.  התקינו את ההרחבה **PowerShell** של Microsoft, אם אינה מותקנת כבר.

##### 📝 שלב 2. פתחו את פרופיל ה-PowerShell ב-VS Code

במסוף PowerShell (אפשר ישירות במסוף המשולב של VS Code) בצעו את הפקודה:

```powershell
code $PROFILE
```
🔍 **מה מתרחש?**
*   `$PROFILE` מצביע על קובץ הפרופיל של PowerShell.
*   `code` — זוהי פקודה להפעלת VS Code עם הקובץ שצוין.

📌 **אם הפקודה `code` אינה מזוהה:**
משמעות הדבר היא ש-VS Code לא נוסף למשתנה הסביבה `PATH`. כדי לתקן זאת:
1.  פתחו את VS Code.
2.  לחצו `Ctrl+Shift+P` (או F1) כדי לפתוח את לוח הפקודות.
3.  התחילו להקליד: `Shell Command: Install 'code' command in PATH`
4.  בחרו בפקודה זו ובצעו אותה. ייתכן שתידרש הפעלה מחדש של המסוף או המערכת.

##### ✏️ שלב 3. הדביקו את קוד הפונקציה

העתיקו את **הטקסט המלא של הגרסה הסופית של פונקציית `Update-Fork`** והדביקו אותו לתוך הקובץ `profile.ps1` שנפתח ב-VS Code.

##### 💾 שלב 4. שמרו וסגרו

*   שמרו את הקובץ ב-VS Code (`Ctrl+S`).
*   תוכלו לסגור את VS Code או להשאירו פתוח.

##### 🔄 שלב 5. הפעילו מחדש את PowerShell

*   סגרו את כל סשני ה-PowerShell.
*   פתחו סשן PowerShell חדש.

כעת פונקציית `Update-Fork` תהיה זמינה. בדקו זאת על ידי קריאה ל-`Update-Fork` במאגר שלכם.

---

*אם יתעוררו קשיים במציאת הפרופיל, הפקודה `$PROFILE` ב-PowerShell תמיד תציג את הנתיב המדויק. בהתאם לגרסת PowerShell והגדרות המערכת, `$PROFILE` עשוי להצביע על קבצים שונים (למשל, `profile.ps1` לכל ההוסטים או ספציפי לקונסולה).*

---

### 3. כקובץ `.ps1` נפרד

1.  שמרו את הקוד המלא של פונקציית `Update-Fork` בקובץ, למשל, `MyUpdateForkScript.ps1`.
2.  כדי להשתמש בפונקציה, עליכם תחילה "לטעון" את הקובץ הזה לסשן ה-PowerShell הנוכחי (זה נקרא "dot-sourcing"), ולאחר מכן לקרוא לפונקציה עצמה:

    ```powershell
    # עברו לתיקייה שבה נמצא הסקריפט שלכם
    cd C:\Путь\К\Скриптам

    # טענו את הסקריפט (שימו לב לנקודה ולרווח בתחילת השורה)
    . .\MyUpdateForkScript.ps1

    # כעת הפונקציה זמינה בסשן הנוכחי
    # עברו לתיקייה של הפורק שלכם
    cd C:\Путь\К\Вашему\Форку
    Update-Fork
    ```

    או, אם אתם נמצאים בתיקייה עם הסקריפט, והפורק במקום אחר:
    ```powershell
    . .\MyUpdateForkScript.ps1
    Update-Fork -GitDirectory "C:\Путь\К\Вашему\Форку"
    ```
    שיטה זו דורשת ביצוע הפקודה `. .\MyUpdateForkScript.ps1` בכל סשן חדש שבו תרצו להשתמש בפונקציה.

---

מוכן! כעת אתם יכולים לסנכרן את הפורק שלכם עם המקור בפקודה אחת בלבד: `Update-Fork`.