<#
==============================================================
 StaffTract.AI – Hackathon Cleanup Script (v3.1)
 Author  : StaffTract Crew
 Purpose : Simplify repository for Roshn Hackathon demo
==============================================================
#>

Write-Host ""
Write-Host "Starting StaffTract.AI Hackathon Cleanup..." -ForegroundColor Cyan
Write-Host ""

# --- Define paths ---
$projectRoot = Split-Path -Parent $PSScriptRoot
$appDir      = Join-Path $projectRoot "app"

# --- Backup non-essential folders ---
$backupDir = Join-Path $projectRoot "backup_nonessential_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path $backupDir | Out-Null

$nonEssential = @("workforce","compliance","payments","docs","deploy","demo_assets","data","tests","migrations","frontend/public/locales")

foreach ($folder in $nonEssential) {
    $path = Join-Path $projectRoot $folder
    if (Test-Path $path) {
        Write-Host "Backing up $folder ..." -ForegroundColor Yellow
        Move-Item $path $backupDir -Force
    }
}

# --- Clean empty directories ---
Get-ChildItem $projectRoot -Directory | Where-Object { $_.GetFileSystemInfos().Count -eq 0 } | Remove-Item -Recurse -Force

# --- Confirm essentials ---
Write-Host ""
Write-Host "Essentials preserved: core, api, models, mock_data" -ForegroundColor Green
Write-Host "Non-essential modules moved to: $backupDir" -ForegroundColor DarkGray
Write-Host ""
Write-Host "Hackathon Edition ready to run: python -m uvicorn app.main:app --reload --port 8000" -ForegroundColor Cyan
Write-Host ""
