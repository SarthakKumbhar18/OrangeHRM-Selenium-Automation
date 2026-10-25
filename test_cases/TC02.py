from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Chrome
driver = webdriver.Chrome()

# Open OrangeHRM
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize browser
driver.maximize_window()

# Create explicit wait
wait = WebDriverWait(driver, 30)

# Enter invalid username
username = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='username']")
    )
)
username.send_keys("Test")

# Enter invalid password
password = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='password']")
    )
)
password.send_keys("Test@123")

# Click Login
login_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Login']")
    )
)
login_button.click()

# Wait for Invalid credentials message
invalid_message = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[normalize-space()='Invalid credentials']")
    )
)

# Verify result
if invalid_message.is_displayed():
    print("TC-02: PASS")
    print("Invalid credentials message displayed.")

    # Take screenshot of final result
    driver.save_screenshot("TC02_Login_Invalid.png")

else:
    print("TC-02: FAIL")
    print("Invalid credentials message was not displayed.")

# Close browser
driver.quit()