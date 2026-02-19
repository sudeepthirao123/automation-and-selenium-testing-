
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    print("Opening website...")

    # Example test (dummy fields)
    try:
        driver.find_element(By.TAG_NAME, "h1")
        print("Page loaded successfully ✅")
    except:
        print("Test failed ❌")

    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    test_login()
