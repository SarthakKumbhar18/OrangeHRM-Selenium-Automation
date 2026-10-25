from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

wait = WebDriverWait(driver, 60)

# ---------------- LOGIN ----------------

username = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Username']")
    )
)
username.clear()
username.send_keys("Admin")

password = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Password']")
    )
)
password.clear()
password.send_keys("admin123")

login_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Login']")
    )
)
login_button.click()

# Wait for Dashboard
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[normalize-space()='Dashboard']")
    )
)

# ---------------- PROFILE ----------------

profile = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(@class,'oxd-userdropdown-tab')]")
    )
)
profile.click()

# Wait for dropdown
logout = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//a[normalize-space()='Logout']")
    )
)

# Screenshot of profile dropdown
driver.save_screenshot("TC09_Logout_Dropdown.png")

# ---------------- LOGOUT ----------------

logout.click()

# Wait for Login page
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//button[normalize-space()='Login']")
    )
)

# Screenshot after logout
driver.save_screenshot("TC09_Logout_Result.png")

print("TC-09: PASS")
print("Logout successful.")

driver.quit()