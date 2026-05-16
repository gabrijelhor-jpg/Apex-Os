# Pokreni web lokalno — download.json i gumbi rade ispravno
Set-Location $PSScriptRoot
Write-Host "Apex web: http://localhost:8080" -ForegroundColor Cyan
python -m http.server 8080
