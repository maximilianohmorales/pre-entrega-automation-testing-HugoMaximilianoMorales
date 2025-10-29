from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_exitoso(driver):
    
    driver.get("https://www.saucedemo.com")

    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    
    driver.find_element(By.ID, "login-button").click()

    
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )
    except Exception:
        assert False, "El login falló. No se redirigió a /inventory.html"