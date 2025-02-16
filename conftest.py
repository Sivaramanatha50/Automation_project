import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(params=['chrome','firefox'],scope='class')
def set_up_browser(request):
    if request.param == 'chrome':
        webdriver.Chrome(ChromeDriverManager().install())
    if request.param == 'firefox':
        webdriver.Firefox(GeckoDriverManager().install())
    request.cls.driver = webdriver
    yield
    webdriver.close()

@pytest.mark.usefixtures("set_up_browser")
class TestLaunchApp:

    def test_launch_all(self):
        self.driver.get("google.com")


