# Course Recommender Dashboard Launcher
# Double-click this file to launch the dashboard!

Write-Host "🎓 Course Recommender Pro - Dashboard Launcher" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""

# Check if streamlit is installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
try {
    $null = python -c "import streamlit" 2>&1
    Write-Host "✅ Streamlit is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Streamlit not found. Installing..." -ForegroundColor Red
    pip install -r requirements.txt
}

Write-Host ""
Write-Host "🚀 Launching dashboard..." -ForegroundColor Green
Write-Host ""
Write-Host "📱 The dashboard will open in your browser at: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Launch streamlit
streamlit run app.py
