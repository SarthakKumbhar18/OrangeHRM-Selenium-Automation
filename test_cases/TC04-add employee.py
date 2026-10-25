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

# Wait for Dashboard
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[normalize-space()='Dashboard']")
    )
)

# ---------------- PIM ----------------

# Click PIM
pim = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='PIM']")
    )
)
pim.click()

# Wait for PIM page
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[normalize-space()='PIM']")
    )
)

# ---------------- ADD EMPLOYEE ----------------

# Click + Add
add_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Add']")
    )
)
add_button.click()

# Wait for Add Employee page
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[normalize-space()='Add Employee']")
    )
)

# Enter First Name
first_name = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "firstName")
    )
)
first_name.send_keys("Sarthak")

# Enter Middle Name
middle_name = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "middleName")
    )
)
middle_name.send_keys("Lahuraj")

# Enter Last Name
last_name = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "lastName")
    )
)
last_name.send_keys("Kumbhar")

# Enter Employee ID
employee_id = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//label[normalize-space()='Employee Id']/../following-sibling::div//input")
    )
)
employee_id.clear()
employee_id.send_keys("9999")

# Click Save
save_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")
    )
)
save_button.click()

# Wait for employee details page
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[normalize-space()='Personal Details']")
    )
)

# Wait a little for the page to finish loading
time.sleep(5)

# ---------------- VERIFY RESULT ----------------

personal_details = driver.find_element(
    By.XPATH, "//h6[normalize-space()='Personal Details']"
)

if personal_details.is_displayed():
    print("TC-04: PASS")
    print("New employee added successfully.")

    # Take screenshot of final result
    driver.save_screenshot("TC04_Add_Employee.png")

else:
    print("TC-04: FAIL")
    print("Employee was not added.")

# Close browser
driver.quit()