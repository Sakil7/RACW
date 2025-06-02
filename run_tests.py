#!/usr/bin/env python3
"""
Script to run tests and generate HTML reports
"""
import subprocess
import sys
import os
from datetime import datetime

def run_tests():
    """Run pytest with HTML reporting"""
    # Create reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)
    
    # Generate timestamp for report filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"reports/test_report_{timestamp}.html"
    
    # Run pytest with HTML reporting
    cmd = [
        "pytest", 
        "tests/test_login.py",
        "--html=" + report_file,
        "--self-contained-html",
        "--verbose",
        "--tb=short"
    ]
    
    print(f"Running tests and generating HTML report: {report_file}")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        print("\n" + "="*50)
        print("TEST RESULTS")
        print("="*50)
        print(result.stdout)
        
        if result.stderr:
            print("\nERRORS:")
            print(result.stderr)
        
        if result.returncode == 0:
            print(f"\n✅ Tests completed successfully!")
            print(f"📊 HTML Report generated: {report_file}")
        else:
            print(f"\n❌ Tests failed with return code: {result.returncode}")
            print(f"📊 HTML Report still generated: {report_file}")
            
        return result.returncode
        
    except FileNotFoundError:
        print("❌ Error: pytest not found. Please install pytest first:")
        print("pip install pytest pytest-html")
        return 1
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())
