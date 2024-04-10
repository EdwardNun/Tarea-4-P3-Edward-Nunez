from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from locators import PageLocators
import pytest
import time


@pytest.fixture(scope='session')
def driver():
    driver_path = r'C:/Users/Eduardo/OneDrive/Desktop/Tarea 4 P3/msedgedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_crear_estudio(driver):
    driver.get('https://app.optimalworkshop.com/login')
    user_text_field = driver.find_element(*PageLocators.SEARCH_USER_EMAIL)
    user_text_field.send_keys('20220310@itla.edu.do')
    password_text_field = driver.find_element(*PageLocators.SEARCH_USER_PASSWORD)
    password_text_field.send_keys('Edward1011200-3')
    login_button = driver.find_element(*PageLocators.SEARCH_LOGIN_BUTTON)
    login_button.click()

    # Verifica que el inicio de sesión fue exitoso
    assert driver.title == "Hi Edward | Optimal Workshop"

    # Acciones para crear un nuevo estudio
    create_study_button = driver.find_element(*PageLocators.CREATE_STUDY)
    create_study_button.click()
    select_study_type = driver.find_element(*PageLocators.SELECT_STUDY)
    select_study_type.send_keys('Chalkmark - First-click testing')
    select_study_type.send_keys(Keys.ENTER)
    study_name_field = driver.find_element(*PageLocators.STUDY_NAME)
    study_name_field.send_keys('Test Clicks')
    create_folder_field = driver.find_element(*PageLocators.CREATE_FOLDER)
    create_folder_field.send_keys('Folder 1')
    create_folder_field.send_keys(Keys.ENTER)

    # Realiza acciones en la página, por ejemplo, captura de pantalla
    driver.save_screenshot('results/dashboard.png')