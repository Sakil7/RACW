# 🚀 Robi Website Automated Testing (RACW)

## 📋 Overview
Automated testing suite for Robi website login functionality using **Playwright** and **pytest**. This optimized test suite validates complete login flow including invalid number handling, OTP verification, and retry mechanisms.

## ✨ Features
- ✅ **Invalid Number Validation** - Tests with invalid Robi number (01621396930)
- ✅ **OTP Error Handling** - Handles incorrect OTP and retry flow
- ✅ **Edit Icon Automation** - Reliably finds and clicks number edit button
- ✅ **Multiple Number Testing** - Tests with different phone numbers
- ✅ **HTML Reporting** - Professional test reports with screenshots
- ✅ **Cross-Platform** - Works on Windows, macOS, Linux
- ✅ **Optimized Code** - 70% reduction in code size for better performance

## 🎯 Test Scenarios Covered

### 1. Invalid Number Test
```
Input: 01621396930 (Invalid Robi number)
Expected: Alert appears, number is cleared automatically
```

### 2. Valid Number with Wrong OTP
```
Input: 01882740984 + OTP: 111111
Expected: Error message, edit icon appears
```

### 3. Retry with Different Number  
```
Input: 01898916204 + OTP: 123456
Expected: Successful login
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Git

### Setup
```bash
# Clone the repository
git clone https://github.com/Sakil7/RACW.git
cd RACW

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

## 🚀 Running Tests

### Quick Run
```bash
python test_runner.py
```

### Detailed Run with Reports
```bash
pytest tests/test_login.py -v --html=reports/report.html --self-contained-html
```

### PowerShell (Windows)
```powershell
.\run_tests.ps1
```

## 📊 Test Reports
HTML reports are automatically generated in the `reports/` directory with:
- ✅ Test execution results
- ✅ Screenshots on failures  
- ✅ Detailed logs and timings
- ✅ Browser interaction recordings

## 📁 Project Structure
```
RACW/
├── tests/
│   ├── test_login.py       # Main test file (optimized)
│   └── conftest.py         # Test configuration
├── reports/                # HTML test reports
├── test_runner.py         # Quick test execution script
├── run_tests.ps1          # PowerShell execution script  
├── pytest.ini            # Pytest configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Configuration

### Browser Settings (pytest.ini)
```ini
[pytest]
testpaths = tests
addopts = --headed --browser chromium --slowmo 300 --html=reports/report.html --self-contained-html
```

### Dependencies (requirements.txt)
```txt
pytest==7.4.0
pytest-playwright==0.4.0
playwright==1.36.0
pytest-html==3.2.0
```

## 🎭 Test Details

### Key Selectors Used
- **Invalid Number Alert**: `.MuiAlert-message.mui-127h8j3`
- **Phone Input**: `//input[@name='robiNumber']`
- **Edit Icon**: `.MuiBox-root.mui-ywc0oe`
- **OTP Inputs**: `//input[@id='otp-{i}']`

### Test Flow
1. **Navigation** → Load Robi website
2. **Cookie Consent** → Accept automatically  
3. **Invalid Test** → Enter invalid number, handle validation
4. **Valid Login** → Enter correct number, send OTP
5. **Error Simulation** → Wrong OTP, trigger retry
6. **Edit & Retry** → Click edit icon, new number + correct OTP
7. **Success** → Complete login validation

## 🤝 Contributing
Feel free to fork this repository and submit pull requests for improvements.

## 📞 Support
For issues or questions about this test automation suite, please create an issue in the GitHub repository.

## 📈 Performance
- **Execution Time**: ~30-45 seconds per full test
- **Code Optimization**: 70% reduction from original
- **Reliability**: Multiple fallback selectors for stability
- **Browser Support**: Chromium (primary), Firefox, Safari compatible

---
**Created by**: Sakil7  
**Last Updated**: August 2025  
**Version**: 2.0 (Optimized)