<#
==========================================================
 StaffTract.AI – Hackathon MVP Cleanup Script (v7.0)
 Author  : StaffTract Crew
 Purpose : Keep only essential 6 backend modules for MVP
==========================================================
#>

Write-Host ""
Write-Host "----------------------------------------------" -ForegroundColor Cyan
Write-Host " StaffTract.AI Hackathon MVP Cleanup (v7.0)" -ForegroundColor Cyan
Write-Host "----------------------------------------------" -ForegroundColor Cyan
Write-Host ""

# --- Resolve paths dynamically ---
$scriptPath   = $MyInvocation.MyCommand.Definition
$projectRoot  = Split-Path -Parent $scriptPath
$appDir       = Join-Path $projectRoot "backend\app"
$modulesDir   = Join-Path $appDir "modules"
$backupDir    = Join-Path $projectRoot "backup_non_mvp"

Write-Host "Project root  : $projectRoot"
Write-Host "App directory : $appDir"
Write-Host ""

# --- Create backup directory ---
if (!(Test-Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir | Out-Null
    Write-Host "Backup folder created at: $backupDir" -ForegroundColor Yellow
}

# --- Define core MVP module names ---
$coreModules = @(
    "recruitment_copilot",
    "workforce_optimizer",
    "fraud_monitor",
    "community_planner",
    "ai_insights",
    "performance_eval"
)

# --- Move non-MVP modules to backup ---
if (Test-Path $modulesDir) {
    Get-ChildItem -Directory $modulesDir | ForEach-Object {
        if ($coreModules -notcontains $_.Name) {
            $src = $_.FullName
            $dest = Join-Path $backupDir $_.Name
            Move-Item -Path $src -Destination $dest -Force
            Write-Host "Moved non-MVP module: $($_.Name)" -ForegroundColor DarkGray
        }
    }
} else {
    Write-Host "❌ Modules directory not found at $modulesDir" -ForegroundColor Red
}

# --- Clean up unneeded backend folders ---
$deleteDirs = @(
    "backend\app\auth",
    "backend\app\notifications",
    "backend\app\communication",
    "backend\app\analytics",
    "backend\app\monitoring",
    "backend\app\multitenancy",
    "backend\app\novamate_v2",
    "backend\app\company",
    "backend\app\compliance",
    "backend\app\ai_agents"
)

foreach ($dir in $deleteDirs) {
    if (Test-Path $dir) {
        Move-Item -Path $dir -Destination $backupDir -Force
        Write-Host "Archived: $dir" -ForegroundColor DarkGray
    }
}

# --- Optional: delete caches ---
$cacheDirs = @(
    "backend\__pycache__",
    "backend\app\__pycache__",
    "backend\app\modules\__pycache__"
)
foreach ($cache in $cacheDirs) {
    if (Test-Path $cache) {
        Remove-Item -Recurse -Force $cache
        Write-Host "Removed cache: $cache"
    }
}

# --- Confirm final structure ---
Write-Host ""
Write-Host "✅ Cleanup complete. The following modules remain:" -ForegroundColor Green
$coreModules | ForEach-Object { Write-Host " - $_" -ForegroundColor Cyan }

Write-Host ""
Write-Host "📦 All non-MVP items have been safely archived at: $backupDir" -ForegroundColor Yellow
Write-Host ""
Write-Host "Hackathon MVP Edition Ready!" -ForegroundColor Green
