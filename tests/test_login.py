import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Login
def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com")
    
    #Ingresar credenciales válidas
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    #Validar login exitoso
    
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )
    except Exception:
        pytest.fail("No se redirigió a /inventory.html después del login.")

    #Validación de visualización de titulos "Products" y "Swag Labs"
    titulo_products = driver.find_element(By.CLASS_NAME, "title").text
    titulo_general = driver.title
    
    assert titulo_products == "Products", "El título 'Products' no se encontró"
    assert titulo_general == "Swag Labs", "El título 'Swag Labs' no se encontró"