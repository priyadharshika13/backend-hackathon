# ------------------------------------------------------------
# StaffTract.AI - Backend Health Verification Script
# ------------------------------------------------------------
Write-Host "🔍 Checking StaffTract.AI backend health..." -ForegroundColor Cyan

$BASE_URL = "https://stafftract-ai.up.railway.app"
$endpoints = @(
    "/api/recruitment/summary",
    "/api/workforce/summary",
    "/api/performance/summary",
    "/api/community/summary",
    "/api/fraud/summary",
    "/api/insights/summary"
)

foreach ($ep in $endpoints) {
    $url = "$BASE_URL$ep"
    try {
        $response = Invoke-RestMethod -Uri $url -Method Get -ErrorAction Stop
        if ($null -ne $response) {
            Write-Host "✅ $ep - OK (mock data loaded)" -ForegroundColor Green
        } else {
            Write-Host "⚠️  $ep - Empty response" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "❌ $ep - Failed to connect or invalid response" -ForegroundColor Red
    }
}

Write-Host "------------------------------------------------------------"
Write-Host "✅ Health check completed. Check above for any red ❌ entries."
Write-Host "------------------------------------------------------------"
