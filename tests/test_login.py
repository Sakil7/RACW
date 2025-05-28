import pytest
import re
from playwright.sync_api import Page, expect

def test_robi_website(page: Page):
    page.goto("https://robi.com.bd/")
    try:
        page.get_by_role("button", name=re.compile("Accept|Allow|I agree", re.IGNORECASE)).click(timeout=5000)
    except:
        pass
    page.get_by_role("button", name="Log In").click()
    page.wait_for_timeout(2000)
    page.locator("//input[@name='robiNumber']").fill("01898916204")
    page.get_by_role("button", name="Send OTP").click()
    page.wait_for_timeout(2000)
    for i, digit in enumerate(["1", "2", "3", "4", "5", "6"]):
        page.locator(f"//input[@id='otp-{i}']").fill(digit)
        page.wait_for_timeout(500)
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Confirm OTP").click()
    page.wait_for_timeout(3000)

    otp_error = page.locator(".MuiAlert-message, .otp-error, .error-message")
    if otp_error.is_visible():
        print("Test failed: Incorrect OTP entered. Error message displayed.")
        return
