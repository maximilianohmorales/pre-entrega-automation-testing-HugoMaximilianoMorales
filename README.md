# Pre-Entrega: Automatización QA - Hugo Maximiliano Morales

# Propósito del Proyecto 
Este proyecto automatiza los flujos de prueba básicos (Login, Catálogo y Carrito) para el sitio web `saucedemo.com`

# Tecnologías Utilizadas 
Python
Pytest
Selenium WebDriver
Git y GitHub
webdriver-manager
pytest-html

# Instrucciones de instalación de dependencias
1.  Clonar este repositorio.
    git clone https://github.com/maximilianohmorales/pre-entrega-automation-testing-HugoMaximilianoMorales.git
2.  Instala las librerías:
    pip install -r requirements.txt

## Comando para ejecutar las pruebas
Para ejecutar todas las pruebas y generar el reporte HTML, usar el siguiente comando. El reporte se guardará en la carpeta "reports".

pytest -v --html=reports/reporte.html