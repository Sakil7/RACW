"""
Pytest configuration file for Robi Website tests
"""
import pytest
from datetime import datetime

def pytest_html_report_title(report):
    """Customize the HTML report title"""
    report.title = "Robi Website Test Report"

def pytest_configure(config):
    """Configure pytest with additional metadata"""
    config._metadata = {
        "Project": "Robi Website Automation",
        "Test Suite": "Login Flow Tests",
        "Environment": "Development",
        "Tester": "Automation Team",
        "Test Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Browser": "Chromium",
        "Framework": "Playwright + Pytest"
    }

def pytest_html_results_summary(prefix, summary, postfix):
    """Add custom content to the HTML report summary"""
    prefix.extend([
        "<h2>Test Scope</h2>",
        "<p>This report covers the automated testing of Robi website login functionality.</p>",
        "<ul>",
        "<li>✅ Invalid phone number validation</li>",
        "<li>✅ OTP verification process</li>", 
        "<li>✅ Error handling and retry mechanisms</li>",
        "<li>✅ Successful login completion</li>",
        "</ul>"
    ])

@pytest.fixture(autouse=True)
def test_metadata(request):
    """Add metadata to each test"""
    # Add test metadata
    if hasattr(request.node, 'add_marker'):
        request.node.add_marker(pytest.mark.test_id(f"TEST_{request.node.name}"))
