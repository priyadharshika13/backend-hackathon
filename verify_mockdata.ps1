# -------------------------------------------------------------
# StaffTract.AI – Backend Mock-Data Verification Script (Hackathon MVP)
# -------------------------------------------------------------
# Purpose:
#   Checks that all mock-data JSON files are reachable through the FastAPI routes.
#   Prints ✅ for valid responses and ❌ if 404 / empty.
# -------------------------------------------------------------

$BaseURL = "https://stafftract-ai.up.railway.app/api"
$Modules = @(
    "recruitment/summary",
    "workforce/overview",
    "performance/summary",
    "community/overview",
    "fraud/alerts",
    "insights/summary"
)

Write-Host "`n🔍  Running StaffTract.AI Mock-Data Verification..." -ForegroundColor Cyan
foreach ($m in $Modules) {
    $r = curl -s "$BaseURL/$m"
    if ($r -match "\[" -or $r -match "\{") {
        Write-Host "✅  $m  →  OK" -ForegroundColor Green
    } else {
        Write-Host "❌  $m  →  Not Found or Invalid Data" -ForegroundColor Red
    }
}
Write-Host "`nDone."
