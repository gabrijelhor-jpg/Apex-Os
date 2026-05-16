# Pravi ZIP koji SIGURNO sadrzi skrivenu mapu .github (za upload na GitHub)
$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$zip = Join-Path $root "Apex-za-GitHub.zip"

if (-not (Test-Path (Join-Path $root ".github\workflows\build-iso.yml"))) {
  Write-Host "GRESKA: Nedostaje .github\workflows\build-iso.yml" -ForegroundColor Red
  Write-Host "Provjeri da si u mapi Apex na Desktopu."
  exit 1
}

if (Test-Path $zip) { Remove-Item $zip -Force }

# Staging — kopira sve ukljucujuci skrivene mape
$stage = Join-Path $env:TEMP "Apex-github-upload"
if (Test-Path $stage) { Remove-Item $stage -Recurse -Force }
New-Item -ItemType Directory -Path $stage | Out-Null

robocopy $root $stage /E /XD ".git" "os\archiso\out" "os\archiso\work" /XF "*.iso" | Out-Null

Compress-Archive -Path (Join-Path $stage "*") -DestinationPath $zip -Force
Remove-Item $stage -Recurse -Force

Write-Host ""
Write-Host "Gotovo: $zip" -ForegroundColor Green
Write-Host ""
Write-Host "Sljedeci koraci:"
Write-Host "  1. github.com -> tvoj repo -> Add file -> Upload files"
Write-Host "  2. Povuci Apex-za-GitHub.zip (ili raspakiraj i uploadaj sve)"
Write-Host "  3. Tab Actions -> Build Apex ISO"
Write-Host ""
