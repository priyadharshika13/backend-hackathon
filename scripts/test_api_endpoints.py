# ---------------------------------------------------------------
# StaffTract.AI – Live API Endpoint Tester
# ---------------------------------------------------------------
# Purpose:
#   Test all /api/* endpoints on live Railway backend
#   Show status, latency, and JSON validity for each route
# Usage:
#   python backend/scripts/test_api_endpoints.py
# ---------------------------------------------------------------

import httpx
import asyncio
import time

BASE_URL = "https://stafftract-ai.up.railway.app"

# List of endpoints to check
ENDPOINTS = [
    "/api/recruitment/candidates",
    "/api/workforce/summary",
    "/api/performance/summary",
    "/api/community/overview",
    "/api/fraud/alerts",
    "/api/insights/trends",
]

async def test_endpoint(client, path):
    url = f"{BASE_URL}{path}"
    start = time.perf_counter()
    try:
        r = await client.get(url, timeout=10)
        duration = time.perf_counter() - start
        if r.status_code == 200:
            try:
                data = r.json()
                print(f"{path:<35} 200 OK | {len(str(data))} bytes | {duration:.2f}s")
            except Exception:
                print(f"  {path:<35} 200 OK but invalid JSON | {duration:.2f}s")
        else:
            print(f" {path:<35} {r.status_code} {r.reason_phrase}")
    except Exception as e:
        print(f" {path:<35} Failed - {e}")

async def main():
    print(f"🔍 Testing StaffTract.AI Live API: {BASE_URL}\n")
    async with httpx.AsyncClient(verify=False) as client:
        await asyncio.gather(*[test_endpoint(client, e) for e in ENDPOINTS])
    print("\n Live test complete.\n")

if __name__ == "__main__":
    asyncio.run(main())
