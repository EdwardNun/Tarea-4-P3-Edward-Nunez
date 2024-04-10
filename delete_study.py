from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from locators import PageLocators
import time
import pytest

@pytest.fixture(scope='session')
def driver():
    driver_path = r'C:/Users/Eduardo/OneDrive/Desktop/Tarea 4 P3/msedgedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

def test_borrar_estudio(driver):
    driver.get('https://app.optimalworkshop.com/login')
    user_text_field = driver.find_element(*PageLocators.SEARCH_USER_EMAIL)
    user_text_field.send_keys('20220310@itla.edu.do')
    password_text_field = driver.find_element(*PageLocators.SEARCH_USER_PASSWORD)
    password_text_field.send_keys('Edward1011200-3')
    login_button = driver.find_element(*PageLocators.SEARCH_LOGIN_BUTTON)
    login_button.click()

    driver.get('https://app.optimalworkshop.com/a/x3qqpuaf/studies')
    driver.set_window_size(1200, 800)

    open_folder_button = driver.find_element(*PageLocators.OPEN_FOLDER)
    open_folder_button.click()
    

    select_test_button = driver.find_element(*PageLocators.SELECT_TEST)
    select_test_button.click()
    

    delete_test_button = driver.find_element(*PageLocators.DELETE_TEST)
    delete_test_button.click()

    confirm_delete_button = driver.find_element(*PageLocators.CONFIRM_DELETE)
    confirm_delete_button.click()

    driver.refresh()

    driver.save_screenshot('results/delete_study.png')
