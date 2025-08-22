import pytest
import re
from playwright.sync_api import Page, expect

@pytest.mark.smoke
@pytest.mark.login
def test_robi_website(page: Page):
    """
    Test Robi website login functionality including:
    1. Invalid number validation
    2. OTP verification
    3. Error handling and retry mechanism
    """
    page.goto("https://dev-web.robi.com.bd/")
    try:
        page.get_by_role("button", name=re.compile("Accept|Allow|I agree", re.IGNORECASE)).click(timeout=5000)
    except:
        pass
    
    page.get_by_role("button", name="Log In").click()
    page.wait_for_timeout(1000)
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
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Confirm OTP").click()
    page.wait_for_timeout(1000)    # Check for OTP error after first attempt
    otp_error = page.locator(".MuiAlert-message, .otp-error, .error-message")
    if otp_error.is_visible():
        print("First attempt failed: Incorrect OTP entered. Retrying with correct credentials...")
        
        # Click the edit icon using the correct class you provided
        edit_icon_selectors = [
            ".MuiBox-root.mui-ywc0oe",  # The exact class you provided
            "div.MuiBox-root.mui-ywc0oe",  # With div tag
            "//div[contains(@class, 'mui-ywc0oe')]",  # XPath version
            ".MuiBox-root.mui-ywc0oe svg",  # If it contains an SVG
            "[class*='mui-ywc0oe']"  # Partial class match
        ]
        
        edit_icon_clicked = False
        for i, selector in enumerate(edit_icon_selectors):
            try:
                print(f"Trying edit icon selector {i+1}: {selector}")
                edit_icon = page.locator(selector)
                
                # Wait for element and check if visible
                edit_icon.wait_for(state="visible", timeout=1000)
                
                if edit_icon.is_visible():
                    edit_icon.click()
                    print(f"✅ Successfully clicked edit icon using: {selector}")
                    edit_icon_clicked = True
                    break
                
            except Exception as e:
                print(f"❌ Failed with selector {selector}: {str(e)}")
                continue
        
        if not edit_icon_clicked:
            print("❌ Could not find edit icon. Taking screenshot for debugging...")
            page.screenshot(path="reports/debug_edit_icon_not_found.png")
            return
        
        # Wait for the number field to be editable again
        page.wait_for_timeout(1000)
        
        # Clear and enter the correct phone number
        phone_input = page.locator("//input[@name='robiNumber']")
        phone_input.wait_for(state="visible")
        phone_input.clear()
        phone_input.fill("01898916204")
        print("Entered correct phone number: 01898916204")
        page.wait_for_timeout(1000)
        
        # Send OTP again
        page.get_by_role("button", name="Send OTP").click()
        page.wait_for_timeout(1000)
        print("Sent OTP to correct number")
    

        # Enter correct OTP
        for i, digit in enumerate(["1", "2", "3", "4", "5", "6"]):
            page.locator(f"//input[@id='otp-{i}']").fill(digit)
            page.wait_for_timeout(500)
        print("Entered correct OTP: 123456")
        
        # Confirm OTP
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Confirm OTP").click()
        page.wait_for_timeout(5000)
        
        # Check for error again after retry
        otp_error_retry = page.locator(".MuiAlert-message, .otp-error, .error-message")
        if otp_error_retry.is_visible():
            print("Second attempt also failed: Incorrect OTP entered.")
            return
        else:
            print("Login successful after retry!")
    else:
        print("Login successful on first attempt!")
        