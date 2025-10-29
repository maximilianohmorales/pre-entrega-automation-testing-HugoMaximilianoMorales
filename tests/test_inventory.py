import pytest
from selenium.webdriver.common.by import By

from utils.helpers import login_exitoso 

# Navegación y Verificación del Catálogo
def test_verificacion_catalogo(driver):
    
    login_exitoso(driver)
    
    
    # Verificación del título de la página sea correcto
    assert driver.title == "Swag Labs"
    
    # Comprobación de existencia de productos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en la página"
    
    # Validación de elementos de la interfaz (menú, filtros)
    menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    
    assert menu_btn.is_displayed(), "El botón de menú no está visible"
    assert filtro.is_displayed(), "El filtro de productos no está visible"

    #Listas nombre/precio
    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    print(f"\nInfo Primer Producto: Nombre = '{nombre_producto}', Precio = '{precio_producto}'")
    
    assert nombre_producto != "", "El nombre del primer producto está vacío"
    assert precio_producto != "", "El precio del primer producto está vacío"