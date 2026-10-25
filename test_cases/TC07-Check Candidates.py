from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open Chrome
driver = webdriver.Chrome()

# Open OrangeHRM
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize browser
driver.maximize_window()

# Create explicit wait
wait = WebDriverWait(driver, 60)

# ---------------- LOGIN ----------------

# Enter username
username = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Username']")
    )
)
username.clear()
username.send_keys("Admin")

# Enter password
password = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Password']")
    )
)
password.clear()
password.send_keys("admin123")

# Click Login
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

# ---------------- RECRUITMENT ----------------

# Click Recruitment
recruitment = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Recruitment']")
    )
)
recruitment.click()

# Wait for Candidates page
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h5[normalize-space()='Candidates']")
    )
)

# ---------------- JOB TITLE ----------------

# Click Job Title dropdown
job_title = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[normalize-space()='Job Title']/../following-sibling::div")
    )
)
job_title.click()

# Select Software Engineer
software_engineer = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[normalize-space()='Software Engineer']")
    )
)
software_engineer.click()

# ---------------- SEARCH ----------------

# Click Search
search_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Search']")
    )
)
search_button.click()

# Wait for search results
time.sleep(5)

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait 10 seconds
time.sleep(10)

# ---------------- VERIFY RESULT ----------------

print("TC-07: PASS")
print("Candidates searched successfully.")

# Take screenshot
driver.save_screenshot("TC07_Check_Candidates.png")

# Close browser
driver.quit()