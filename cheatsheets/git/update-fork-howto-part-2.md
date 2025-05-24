# PowerShell: אוטומציה של עדכון פורק GitHub

## חלק 2. פונקציה סופית `Update-Fork`

### פונקציה מוכנה `Update-Fork`

```powershell
function Update-Fork {
    param(
        [Parameter(Mandatory)]
        [string]$RepoPath,
        [string]$TelegramToken,
        [string]$TelegramChatId
    )

    Set-Location -Path $RepoPath

    $logPath = "$RepoPath\update-log.txt"
    "[$(Get-Date)] Starting update for $RepoPath" | Out-File -FilePath $logPath -Append

    try {
        git remote -v | Out-Null
    } catch {
        Write-Error "אינו מאגר git: $RepoPath"
        "[$(Get-Date)] ❌ Not a git repository" | Out-File -FilePath $logPath -Append
        return
    }

    if (-not (git remote | Select-String -Pattern 'upstream')) {
        Write-Error "'upstream' מרוחק לא נמצא"
        "[$(Get-Date)] ❌ 'upstream' not found" | Out-File -FilePath $logPath -Append
        return
    }

    try {
        git checkout main
        git fetch upstream
        git rebase upstream/main
        git push origin main --force

        "[$(Get-Date)] ✅ Fork successfully updated" | Out-File -FilePath $logPath -Append

        if (Get-Command New-BurntToastNotification -ErrorAction SilentlyContinue) {
            New-BurntToastNotification -Text "פורק עודכן", "מאגר: $RepoPath"
        } else {
            Write-Host "✅ פורק עודכן: $RepoPath"
        }

        if ($TelegramToken -and $TelegramChatId) {
            Send-TelegramMessage -Message "✅ פורק עודכן: $RepoPath" -Token $TelegramToken -ChatId $TelegramChatId
        }
    } catch {
        Write-Error "שגיאה בעת עדכון הפורק: $_"
        "[$(Get-Date)] ❌ Error: $_" | Out-File -FilePath $logPath -Append

        if (Get-Command New-BurntToastNotification -ErrorAction SilentlyContinue) {
            New-BurntToastNotification -Text "שגיאת עדכון פורק", $_.Exception.Message
        }

        if ($TelegramToken -and $TelegramChatId) {
            Send-TelegramMessage -Message "❌ שגיאה בעת עדכון הפורק: $RepoPath" -Token $TelegramToken -ChatId $TelegramChatId
        }
    }
}
```

---

### דרכי שימוש

#### 1. עדכון מאגר בודד:

```powershell
Update-Fork -RepoPath "C:\Projects\my-fork" -TelegramToken "<TOKEN>" -TelegramChatId "<CHAT_ID>"
```

#### 2. עדכון מספר פורקים מתוך רשימה:

```powershell
$forks = @(
    "C:\Projects\repo1",
    "C:\Projects\repo2"
)

foreach ($fork in $forks) {
    Update-Fork -RepoPath $fork -TelegramToken "<TOKEN>" -TelegramChatId "<CHAT_ID>"
}
```

---

### שגיאות נפוצות וסיבותיהן

| שגיאה                        | סיבה                                                |
| ----------------------------- | ------------------------------------------------------ |
| `fatal: not a git repository` | הנתיב אינו מצביע על מאגר git                   |
| `error: could not apply`      | קונפליקטים בעת rebase — דורש פתרון ידני      |
| `upstream not found`          | ה-remote `upstream` אינו מוגדר                          |
| `! [rejected]` при push       | Rebase לא בוצע, הענף מתפצל מ-origin/main |

---

### אוטומציה באמצעות קיצור דרך

צור קיצור דרך `.ps1`:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Scripts\update-forks.ps1"
```

תוכן `update-forks.ps1`:

```powershell
$token = "<TOKEN>"
$chatId = "<CHAT_ID>"
$forks = Get-Content "C:\Scripts\repos.txt"
foreach ($repo in $forks) {
    Update-Fork -RepoPath $repo -TelegramToken $token -TelegramChatId $chatId
}
```

קובץ `repos.txt`:

```
C:\Projects\repo1
C:\Projects\repo2
```

---

## חלק 3. ייצוא לוגים ו-Telegram

(ראה לעיל — משולב ב-`Update-Fork`)

פונקציית שליחת הודעות:

```powershell
function Send-TelegramMessage {
    param(
        [string]$Message,
        [string]$Token,
        [string]$ChatId
    )

    $uri = "https://api.telegram.org/bot$Token/sendMessage"
    $body = @{ chat_id = $ChatId; text = $Message }
    Invoke-RestMethod -Uri $uri -Method Post -Body $body
}
```

---

## חלק 4. ממשק GUI ב-Windows Forms

```powershell
Add-Type -AssemblyName System.Windows.Forms

$form = New-Object Windows.Forms.Form
$form.Text = "Update Forks"
$form.Size = New-Object Drawing.Size(400,200)

$button = New-Object Windows.Forms.Button
$button.Text = "עדכון פורקים"
$button.Dock = "Top"
$button.Add_Click({
    $repos = Get-Content "C:\Scripts\repos.txt"
    $token = "<TOKEN>"
    $chatId = "<CHAT_ID>"
    foreach ($repo in $repos) {
        Update-Fork -RepoPath $repo -TelegramToken $token -TelegramChatId $chatId
    }
})

$form.Controls.Add($button)
$form.ShowDialog()
```

---

בחלק הבא ניתן לארוז את היישום כקובץ `.exe`, להוסיף בחירת טוקנים דרך ממשק משתמש גרפי, שילוב עם מתזמן המשימות של Windows או הפעלה אוטומטית.

```python
import shutil
import os
import subprocess

# Prepare project structure
project_dir = "/mnt/data/UpdateForkApp"
script_path = os.path.join(project_dir, "UpdateForkApp.ps1")
form_code_path = os.path.join(project_dir, "UpdateForkForm.ps1")
installer_script_path = os.path.join(project_dir, "installer.iss")

# Create project directory
os.makedirs(project_dir, exist_ok=True)

# Content of the main PowerShell script
script_content = """
param (
    [string]$Token = "<TOKEN>",
    [string]$ChatId = "<CHAT_ID>"
)

function Send-TelegramMessage {
    param(
        [string]$Message,
        [string]$Token,
        [string]$ChatId
    )

    $uri = "https://api.telegram.org/bot$Token/sendMessage"
    $body = @{ chat_id = $ChatId; text = $Message }
    Invoke-RestMethod -Uri $uri -Method Post -Body $body
}

function Update-Fork {
    param(
        [Parameter(Mandatory)]
        [string]$RepoPath,
        [string]$TelegramToken,
        [string]$TelegramChatId
    )

    Set-Location -Path $RepoPath
    $logPath = "$RepoPath\\update-log.txt"
    "[$(Get-Date)] Starting update for $RepoPath" | Out-File -FilePath $logPath -Append

    try {
        git remote -v | Out-Null
    } catch {
        "[$(Get-Date)] ❌ Not a git repository" | Out-File -FilePath $logPath -Append
        return
    }

    if (-not (git remote | Select-String -Pattern 'upstream')) {
        "[$(Get-Date)] ❌ 'upstream' not found" | Out-File -FilePath $logPath -Append
        return
    }

    try {
        git checkout main
        git fetch upstream
        git rebase upstream/main
        git push origin main --force

        "[$(Get-Date)] ✅ Fork successfully updated" | Out-File -FilePath $logPath -Append

        if ($TelegramToken -and $TelegramChatId) {
            Send-TelegramMessage -Message "✅ פורק עודכן: $RepoPath" -Token $TelegramToken -ChatId $TelegramChatId
        }
    } catch {
        "[$(Get-Date)] ❌ Error: $_" | Out-File -FilePath $logPath -Append

        if ($TelegramToken -and $TelegramChatId) {
            Send-TelegramMessage -Message "❌ שגיאה בעת עדכון הפורק: $RepoPath" -Token $TelegramToken -ChatId $TelegramChatId
        }
    }
}

# Read repository list from file
$repos = Get-Content "$PSScriptRoot\\repos.txt"
foreach ($repo in $repos) {
    Update-Fork -RepoPath $repo -TelegramToken $Token -TelegramChatId $ChatId
}
"""

# Save the PowerShell script
with open(script_path, "w", encoding="utf-8") as f:
    f.write(script_content)

# Save GUI wrapper example separately (if needed to run form standalone)
form_code = """
Add-Type -AssemblyName System.Windows.Forms

$form = New-Object Windows.Forms.Form
$form.Text = "Update Forks"
$form.Size = New-Object Drawing.Size(400,200)

$button = New-Object Windows.Forms.Button
$button.Text = "עדכון פורקים"
$button.Dock = "Top"
$button.Add_Click({
    & "$PSScriptRoot\\UpdateForkApp.ps1" -Token "<TOKEN>" -ChatId "<CHAT_ID>"
})

$form.Controls.Add($button)
$form.ShowDialog()
"""
with open(form_code_path, "w", encoding="utf-8") as f:
    f.write(form_code)

# Prepare script for Inno Setup
installer_script = f"""
[Setup]
AppName=UpdateForkApp
AppVersion=1.0
DefaultDirName={{pf}}\\UpdateForkApp
DefaultGroupName=UpdateForkApp
OutputDir={project_dir}
OutputBaseFilename=UpdateForkAppInstaller

[Files]
Source: "{script_path}"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{form_code_path}"; DestDir: "{{app}}"; Flags: ignoreversion

[Icons]
Name: "{{group}}\\Update Fork GUI"; Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -File \\"{{app}}\\\\UpdateForkForm.ps1\\""; WorkingDir: "{{app}}"
"""
with open(installer_script_path, "w", encoding="utf-8") as f:
    f.write(installer_script)

project_dir
```