# PowerShell script to run tests and generate HTML reports
# Usage: .\run_tests.ps1

Write-Host "🚀 Starting Robi Website Tests..." -ForegroundColor Green

# Create reports directory if it doesn't exist
if (!(Test-Path "reports")) {
    New-Item -ItemType Directory -Path "reports" -Force
    Write-Host "📁 Created reports directory" -ForegroundColor Yellow
}

# Generate timestamp for report filename
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$reportFile = "reports/test_report_$timestamp.html"

# Run pytest with HTML reporting
$pytestCmd = "pytest tests/test_login.py --html=$reportFile --self-contained-html --verbose --tb=short"

Write-Host "📊 Generating HTML report: $reportFile" -ForegroundColor Cyan
Write-Host "⚡ Running command: $pytestCmd" -ForegroundColor Gray

try {
    Invoke-Expression $pytestCmd
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Tests completed successfully!" -ForegroundColor Green
        Write-Host "📊 HTML Report generated: $reportFile" -ForegroundColor Cyan
        
        # Ask if user wants to open the report
        $openReport = Read-Host "Would you like to open the HTML report? (y/n)"
        if ($openReport -eq "y" -or $openReport -eq "Y") {
            Start-Process $reportFile
        }
    } else {
        Write-Host "❌ Tests failed with exit code: $LASTEXITCODE" -ForegroundColor Red
        Write-Host "📊 HTML Report still generated: $reportFile" -ForegroundColor Cyan
    }
} catch {
    Write-Host "❌ Error running tests: $_" -ForegroundColor Red
    Write-Host "💡 Make sure pytest and pytest-html are installed:" -ForegroundColor Yellow
    Write-Host "   pip install pytest pytest-html pytest-playwright" -ForegroundColor Gray
}

Write-Host "🏁 Test execution completed." -ForegroundColor Green
