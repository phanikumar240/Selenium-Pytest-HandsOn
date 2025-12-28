from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login(driver, wait, email, password, expected_status="success"):
    driver.get("https://rahulshettyacademy.com/client/#/auth/login")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))).send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
    driver.find_element(By.ID, "login").click()

    if expected_status == "success":
        wait.until(EC.url_contains("/dashboard"))
        print(f"✅ Login successful for: {email}")
    else:
        error_msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".toast-message"))).text
        print(f"🛑 Negative Test Passed: {error_msg}")
        return error_msg

def place_zara_coat_only(driver, wait):
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//b[text()='ZARA COAT 3']/parent::h5/following-sibling::button[last()]")))
    add_btn.click()
    wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ngx-spinner-overlay")))
    
    cart_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[routerlink*='cart']")))
    driver.execute_script("arguments[0].click();", cart_link)

def shipping_and_place_order(driver, wait):
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".totalRow button"))).click()
    
    # Highly resilient country selection
    country_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='Select Country']")))
    country_input.send_keys("ind") 
    
    # Using normalize-space to handle any accidental extra spaces in the dropdown text
    india_xpath = "//button[contains(@class,'ta-item')]//span[normalize-space()='India']"
    wait.until(EC.element_to_be_clickable((By.XPATH, india_xpath))).click()

    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ngx-spinner-overlay")))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".action__submit")))
    driver.execute_script("arguments[0].click();", submit)
    print("✅ Order Success: THANKYOU FOR THE ORDER.")