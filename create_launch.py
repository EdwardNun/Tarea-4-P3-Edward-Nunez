from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from locators import PageLocators
import time
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

def test_realizar_lanzamiento(driver):
    driver.get('https://app.optimalworkshop.com/login')
    user_text_field = driver.find_element(*PageLocators.SEARCH_USER_EMAIL)
    user_text_field.send_keys('20220310@itla.edu.do')
    password_text_field = driver.find_element(*PageLocators.SEARCH_USER_PASSWORD)
    password_text_field.send_keys('Edward1011200-3')
    login_button = driver.find_element(*PageLocators.SEARCH_LOGIN_BUTTON)
    login_button.click()

    driver.get('https://app.optimalworkshop.com/a/x3qqpuaf/chalkmark/surveys/d91635a1-a307-4d9d-8bc5-6e581b63b236/edit#/t/setup/tasks')

    take_control_button = driver.find_element(*PageLocators.CONTROL)
    take_control_button.click()

    launch_button = driver.find_element(*PageLocators.SET_LAUNCH)
    launch_button.click()

    time.sleep(5)
    confirm_launch_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((PageLocators.CREATE_STUDY))
    ) 
    driver.save_screenshot('results/make_launch.png')
    confirm_launch_button.click()

  