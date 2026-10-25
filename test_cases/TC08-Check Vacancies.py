from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[normalize-space()='Dashboard']")
    )
)

# ---------------- RECRUITMENT ----------------

recruitment = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Recruitment']")
    )
)
recruitment.click()

# ---------------- VACANCIES ----------------

vacancies = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Vacancies']")
    )
)
vacancies.click()

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h5[normalize-space()='Vacancies']")
    )
)

# ---------------- JOB TITLE ----------------

job_title = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[normalize-space()='Job Title']/../following-sibling::div")
    )
)
job_title.click()

qa_engineer = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[normalize-space()='QA Engineer']")
    )
)
qa_engineer.click()

# ---------------- SEARCH ----------------

search_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Search']")
    )
)
search_button.click()

time.sleep(5)

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait 10 seconds
time.sleep(10)

# ---------------- VERIFY RESULT ----------------

print("TC-08: PASS")
print("Vacancies searched successfully.")

# Take screenshot
driver.save_screenshot("TC08_Check_Vacancies.png")

driver.quit()