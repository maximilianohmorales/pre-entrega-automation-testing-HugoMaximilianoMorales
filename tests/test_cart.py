import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import login_exitoso 

# Navegación del carrito
def test_agregar_producto_al_carrito(driver):

   
    login_exitoso(driver)


    
    # Guardado del nombre del primer producto
    nombre_producto_esperado = driver.find_element(By.XPATH, "(//div[@class='inventory_item_name '])[1]").text

    # Clickear en "Add to cart" en el primer producto
    driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()
    
    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Validar que estamos en la página del carrito
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))
    
    # Validar que el producto agregado está en la lista
    nombre_producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_producto_en_carrito == nombre_producto_esperado, "El producto en el carrito no es el que se agregó"