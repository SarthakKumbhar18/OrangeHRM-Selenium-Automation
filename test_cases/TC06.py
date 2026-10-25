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

# ---------------- MY INFO ----------------

# Click My Info
my_info = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='My Info']")
    )
)
my_info.click()

# Wait for Personal Details
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[normalize-space()='Personal Details']")
    )
)

# ---------------- PERSONAL DETAILS ----------------

# First Name
first_name = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "firstName")
    )
)
first_name.clear()
first_name.send_keys("Sarthak")

# Middle Name
middle_name = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "middleName")
    )
)
middle_name.clear()
middle_name.send_keys("Lahuraj")

# Last Name
last_name = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "lastName")
    )
)
last_name.clear()
last_name.send_keys("Kumbhar")

# Employee ID
employee_id = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//label[normalize-space()='Employee Id']/../following-sibling::div//input")
    )
)
employee_id.clear()
employee_id.send_keys("3690")

# Other ID
other_id = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//label[normalize-space()='Other Id']/../following-sibling::div//input")
    )
)
other_id.clear()
other_id.send_keys("987654")

# Driver's License Number
license_number = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//label[normalize-space()=\"Driver's License Number\"]/../following-sibling::div//input")
    )
)
license_number.clear()
license_number.send_keys("MH123456")

# License Expiry Date
license_expiry = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//label[normalize-space()='License Expiry Date']/../following-sibling::div//input")
    )
)
license_expiry.clear()
license_expiry.send_keys("2028-12-31")

# ---------------- NATIONALITY ----------------

# Wait for form loader to disappear
wait.until(
    EC.invisibility_of_element_located(
        (By.CLASS_NAME, "oxd-form-loader")
    )
)

# Click Nationality dropdown
nationality = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[normalize-space()='Nationality']/../following-sibling::div")
    )
)
nationality.click()

# Select Indian
indian = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[normalize-space()='Indian']")
    )
)
indian.click()

# ---------------- MARITAL STATUS ----------------

# Wait for form loader to disappear
wait.until(
    EC.invisibility_of_element_located(
        (By.CLASS_NAME, "oxd-form-loader")
    )
)

# Click Marital Status dropdown
marital_status = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[normalize-space()='Marital Status']/../following-sibling::div")
    )
)
marital_status.click()

# Select Single
single = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[normalize-space()='Single']")
    )
)
single.click()

# ---------------- DATE OF BIRTH ----------------

# Date of Birth
date_of_birth = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//label[normalize-space()='Date of Birth']/../following-sibling::div//input")
    )
)
date_of_birth.clear()
date_of_birth.send_keys("2000-01-15")

# ---------------- GENDER ----------------

# Wait for form loader to disappear
wait.until(
    EC.invisibility_of_element_located(
        (By.CLASS_NAME, "oxd-form-loader")
    )
)

# Select Male
male = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[contains(normalize-space(), 'Male')]")
    )
)
male.click()

# ---------------- SAVE ----------------

# Wait for form loader to disappear
wait.until(
    EC.invisibility_of_element_located(
        (By.CLASS_NAME, "oxd-form-loader")
    )
)

# Click Save
save_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")
    )
)
save_button.click()

# ---------------- VERIFY SUCCESS ----------------

# Wait for success toast
success_message = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class,'oxd-toast--success')]")
    )
)

print("Success message appeared.")

# Wait until the form finishes loading
wait.until(
    EC.invisibility_of_element_located(
        (By.CLASS_NAME, "oxd-form-loader")
    )
)

# Verify that updated First Name is displayed
updated_first_name = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "firstName")
    )
)

# Check the updated value
if updated_first_name.get_attribute("value") == "Sarthak":

    print("TC-06: PASS")
    print("Personal details updated successfully.")

    # Take screenshot immediately while success toast is visible
    driver.save_screenshot("TC06_Personal_Details_Updated.png")

else:

    print("TC-06: FAIL")
    print("Updated personal details were not displayed.")

# Close browser
driver.quit()

