import pytest
import re
from playwright.sync_api import Page, expect

def test_robi_website(page: Page):
    page.goto("https://dev-web.robi.com.bd/")
    try:
        page.get_by_role("button", name=re.compile("Accept|Allow|I agree", re.IGNORECASE)).click(timeout=5000)
    except:
        pass
    
    page.get_by_role("button", name="Log In").click()
    page.wait_for_timeout(2000)
      # Test corner case: Enter invalid Robi number first
    print("Testing corner case: Entering invalid Robi number...")
    page.locator("//input[@name='robiNumber']").fill("01621396930")
    page.wait_for_timeout(1000)  # Wait for validation to trigger
    
    # Check for invalid number alert/text without sending OTP
    invalid_number_alert = page.locator(".MuiAlert-message.mui-127h8j3")
    if invalid_number_alert.is_visible():
        print("Invalid number alert detected. Clearing input and continuing with valid number...")
        
        # Clear the invalid number from input field
        phone_input = page.locator("//input[@name='robiNumber']")
        phone_input.clear()
        page.wait_for_timeout(500)
        
        # Enter valid number
        phone_input.fill("01882740984")
        print("Entered valid Robi number: 01882740984")
    else:
        print("No invalid number alert detected, proceeding with test...")
    
    # Now send OTP with the valid number
    page.get_by_role("button", name="Send OTP").click()
    page.wait_for_timeout(500)
    for i, digit in enumerate(["1", "1", "1", "1", "1", "1"]):
        page.locator(f"//input[@id='otp-{i}']").fill(digit)
        page.wait_for_timeout(500)
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Confirm OTP").click()
    page.wait_for_timeout(3000)    # Check for OTP error after first attempt
    otp_error = page.locator(".MuiAlert-message, .otp-error, .error-message")
    if otp_error.is_visible():
        print("First attempt failed: Incorrect OTP entered. Retrying with correct credentials...")
        
        # Click the SVG icon to edit the number field
        edit_icon = page.locator("(//*[name()='svg'])[13]")
        edit_icon.wait_for(state="visible", timeout=5000)
        edit_icon.click()
        print("Clicked edit icon to modify phone number")
        
        # Wait for the number field to be editable again
        page.wait_for_timeout(1000)
        
        # Clear and enter the correct phone number
        phone_input = page.locator("//input[@name='robiNumber']")
        phone_input.wait_for(state="visible")
        phone_input.clear()
        phone_input.fill("01898916204")
        print("Entered correct phone number: 01898916204")
        
        # Send OTP again
        page.get_by_role("button", name="Send OTP").click()
        page.wait_for_timeout(2000)
        print("Sent OTP to correct number")
        
        # Enter correct OTP
        for i, digit in enumerate(["1", "2", "3", "4", "5", "6"]):
            page.locator(f"//input[@id='otp-{i}']").fill(digit)
            page.wait_for_timeout(500)
        print("Entered correct OTP: 123456")
        
        # Confirm OTP
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Confirm OTP").click()
        page.wait_for_timeout(3000)
        
        # Check for error again after retry
        otp_error_retry = page.locator(".MuiAlert-message, .otp-error, .error-message")
        if otp_error_retry.is_visible():
            print("Second attempt also failed: Incorrect OTP entered.")
            return
        else:
            print("Login successful after retry!")
    else:
        print("Login successful on first attempt!")
    
    # Continue with the rest of the flow after successful login
    print("Proceeding with post-login actions...")
    page.wait_for_load_state("networkidle")
    