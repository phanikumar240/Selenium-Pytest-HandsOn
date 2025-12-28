from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def verify_and_print_order_summary(driver, wait):
    success_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".hero-primary")))
    success_text = success_element.text
    assert "THANKYOU FOR THE ORDER" in success_text.upper()

    order_id_raw = driver.find_element(By.CSS_SELECTOR, "label.ng-star-inserted").text
    order_id = order_id_raw.replace("|", "").strip()

    print("\n--- Final Order Summary ---")
    print(f"✅ Assertion Passed: {success_text}")
    print(f"🆔 Order ID: {order_id}")