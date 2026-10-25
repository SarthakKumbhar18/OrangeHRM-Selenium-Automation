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

# Enter username
username = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Username']")
    )
)
username.send_keys("Admin")

# Enter password
password = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Password']")
    )
)
password.send_keys("admin123")

# Click Login
login_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Login']")
    )
)
login_button.click()


dashboard = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[normalize-space()='Dashboard']")
    )
)


if dashboard.is_displayed():
    print("TC-01: PASS")
    print("Login successful - Dashboard displayed.")


    driver.save_screenshot("TC01_Login_Valid.png")
else:
    print("TC-01: FAIL")
    print("Dashboard was not displayed.")


driver.quit()