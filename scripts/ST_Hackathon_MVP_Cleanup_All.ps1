<#
==========================================================
 StaffTract.AI – Full Hackathon MVP Cleanup (v10.0)
 Author  : StaffTract Crew
 Purpose : Keep only essential backend + configs for Hackathon MVP
==========================================================
#>

Write-Host ""
Write-Host "----------------------------------------------" -ForegroundColor Cyan
Write-Host " StaffTract.AI – Full Hackathon MVP Cleanup " -ForegroundColor Cyan
Write-Host "----------------------------------------------" -ForegroundColor Cyan
Write-Host ""

# --- Resolve paths dynamically ---
# Determine project root safely (works in VS Code and PowerShell)
$projectRoot = (Get-Location).Path
$backendDir  = Join-Path $projectRoot "backend"
$appDir      = Join-Path $backendDir "app"
$modulesDir  = Join-Path $appDir "modules"
$backupDir   = Join-Path $projectRoot "backup_non_mvp"

Write-Host "Project root  : $projectRoot"
Write-Host "Backend dir   : $backendDir"
Write-Host "Current location: $(Get-Location)"
Write-Host ""

# --- Create backup directory if not exists ---
if (!(Test-Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir | Out-Null
    Write-Host "Backup folder created at: $backupDir" -ForegroundColor Yellow
}

# --- Define MVP Modules ---
$coreModules = @(
    "recruitment_copilot.py",
    "workforce_optimizer.py",
    "fraud_monitor.py",
    "community_planner.py",
    "ai_insights.py",
    "performance_eval.py"
)

# --- Move non-MVP module files to backup ---
if (Test-Path $modulesDir) {
    Write-Host "`nChecking backend modules..." -ForegroundColor Yellow
    Get-ChildItem -Path $modulesDir -File | ForEach-Object {
        if ($coreModules -notcontains $_.Name) {
            Move-Item -Path $_.FullName -Destination $backupDir -Force
            Write-Host "Moved non-MVP module: $($_.Name)" -ForegroundColor DarkGray
        }
    }
}

# =====================================================================
# StaffTract.AI – Hackathon MVP Final Cleanup with Logging
# Purpose: Move non-essential folders to backup_non_mvp/
#          Remove __pycache__ and generate cleanup_log.txt
# =====================================================================

Write-Host "`nArchiving non-essential folders from project root..." -ForegroundColor Yellow

# Create log file
$logPath = Join-Path $backupDir "cleanup_log_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
"=== StaffTract.AI Hackathon MVP Cleanup Log ===" | Out-File -FilePath $logPath -Encoding utf8
"Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" | Out-File -FilePath $logPath -Append
"Project Root: $projectRoot" | Out-File -FilePath $logPath -Append
"`n--- Archiving Non-Essential Folders ---" | Out-File -FilePath $logPath -Append

# Archive non-backend folders
$rootFolders = Get-ChildItem -Path $projectRoot -Directory
foreach ($folder in $rootFolders) {
    if ($folder.Name -ne "backend" -and $folder.Name -ne "backup_non_mvp") {
        try {
            $destination = Join-Path $backupDir $folder.Name
            Move-Item -Path $folder.FullName -Destination $destination -Force
            $msg = "Archived folder: $($folder.Name)"
            Write-Host $msg -ForegroundColor DarkGray
            $msg | Out-File -FilePath $logPath -Append
        }
        catch {
            $warn = "⚠️ Could not move folder: $($folder.Name) - $($_.Exception.Message)"
            Write-Host $warn -ForegroundColor Yellow
            $warn | Out-File -FilePath $logPath -Append
        }
    }
}

# Remove all __pycache__ folders
"`n--- Removing __pycache__ Folders ---" | Out-File -FilePath $logPath -Append
Get-ChildItem -Path $projectRoot -Recurse -Directory -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -eq "__pycache__" } |
    ForEach-Object {
        try {
            Remove-Item -Recurse -Force $_.FullName
            $msg = "Removed cache: $($_.FullName)"
            Write-Host $msg -ForegroundColor DarkGray
            $msg | Out-File -FilePath $logPath -Append
        }
        catch {
            $warn = "⚠️ Failed to remove cache: $($_.FullName)"
            Write-Host $warn -ForegroundColor Yellow
            $warn | Out-File -FilePath $logPath -Append
        }
    }

# --- Final Confirmation ---
Write-Host "`n✅ Cleanup complete. Only essential Hackathon MVP files remain." -ForegroundColor Green
Write-Host "📦 Archived folders are located at: $backupDir" -ForegroundColor Green
Write-Host "Log file created at: $logPath" -ForegroundColor Cyan

$summaryLine = "`n--- Summary ---`n"
$summaryLine | Out-File -FilePath $logPath -Append
$timestamp = Get-Date -Format 'HH:mm:ss'
$completionMsg = 'Cleanup completed successfully at ' + $timestamp
$completionMsg | Out-File -FilePath $logPath -Append
$archiveMsg = 'Archived content located at: ' + $backupDir
$archiveMsg | Out-File -FilePath $logPath -Append
$endLog = '--- End of Log ---'
$endLog | Out-File -FilePath $logPath -Append
