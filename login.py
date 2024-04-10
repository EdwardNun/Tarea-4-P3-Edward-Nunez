# test_iniciar_sesion.py
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from locators import PageLocators
import pytest

@pytest.fixture
def driver():
    driver_path = r'C:/Users/Eduardo/OneDrive/Desktop/Tarea 4 P3/msedgedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

def test_iniciar_sesion(driver):
    driver.get('https://app.optimalworkshop.com/login')
    user_text_field = driver.find_element(*PageLocators.SEARCH_USER_EMAIL)
    user_text_field.send_keys('20220310@itla.edu.do')
    password_text_field = driver.find_element(*PageLocators.SEARCH_USER_PASSWORD)
    password_text_field.send_keys('Edward1011200-3')
    login_button = driver.find_element(*PageLocators.SEARCH_LOGIN_BUTTON)
    login_button.click()

    # Agrega aquí las aserciones necesarias para verificar que el inicio de sesión fue exitoso
    # Por ejemplo, puedes verificar el título de la página después de iniciar sesión
    assert driver.title == "Hi Edward | Optimal Workshop"

