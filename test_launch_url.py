import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
from test_data import url



@pytest.mark.usefixtures("set_up_browser")
class Test_Launch_Application:

    @pytest.mark.parametrize("url",url)
    def test_lauch_app(self,url,set_up_browser):
        driver = set_up_browser
        driver.get(url)
        title = driver.title
        print(title)
# #
# url = 'https://demoqa.com/'
# obj = Test_Launch_Application()
# obj.test_lauch_app(url)