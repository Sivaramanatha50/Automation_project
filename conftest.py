import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def set_up_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="131.0.6778.205").install()))
    driver.maximize_window()
    yield driver
    driver.quit()


