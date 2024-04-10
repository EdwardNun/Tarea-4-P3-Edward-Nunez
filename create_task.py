from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from locators import PageLocators
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='session')
def driver():
    driver_path = r'C:/Users/Eduardo/OneDrive/Desktop/Tarea 4 P3/msedgedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

def test_crear_tarea(driver):
    driver.get('https://app.optimalworkshop.com/login')
    user_text_field = driver.find_element(*PageLocators.SEARCH_USER_EMAIL)
    user_text_field.send_keys('20220310@itla.edu.do')
    password_text_field = driver.find_element(*PageLocators.SEARCH_USER_PASSWORD)
    password_text_field.send_keys('Edward1011200-3')
    login_button = driver.find_element(*PageLocators.SEARCH_LOGIN_BUTTON)
    login_button.click()

    enter_study_button = driver.find_element(*PageLocators.ENTER_STUDY)
    enter_study_button.click()

    setup_button = driver.find_element(*PageLocators.SETUP)
    setup_button.click()

    take_over_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((PageLocators.TAKE_OVER))
    )
    take_over_button.click()

    choose_image_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((PageLocators.TASK_IMAGE))
    )
    choose_image_button.click()

    upload_image_button = driver.find_element(*PageLocators.UPLOAD_IMAGE)
    upload_image_button.click()

    task_text_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((PageLocators.TASK_TEXT))
    )
    task_text_field.click()
    task_text_field.send_keys('Registro Centro Medico')

    driver.save_screenshot('results/task.png')