import subprocess
import sys
import os

# Change to the correct directory
os.chdir(r"e:\Robi Website")

# Run the specific test
cmd = ["pytest", "tests/test_login.py::test_robi_website", "-v", "-s", "--tb=short"]

print("🚀 Running Robi login test...")
print(f"Command: {' '.join(cmd)}")
print("="*50)

try:
    result = subprocess.run(cmd)
    print(f"\nTest completed with exit code: {result.returncode}")
except Exception as e:
    print(f"Error: {e}")
