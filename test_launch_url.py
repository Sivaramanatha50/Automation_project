import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import labels

class Test_indee_app:
    """set up the browser option"""
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,  # Disable the password manager
        "profile.password_manager_enabled": False  # Disable "Save Password" prompt
    }
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options) #driver_version="131.0.6778.205"
    driver.maximize_window()
    driver.implicitly_wait(20)


    def test_login_app(self):
        """login the application"""
        self.driver.get(labels.url)
        self.driver.find_element(By.XPATH,'//input[@id="access-code"]').send_keys(labels.acces_code)
        self.driver.find_element(By.XPATH,'//*[@id="sign-in-button"]/div').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, labels.wait_for_homepage)))
        assert self.driver.title == labels.homepage_title
        print("sucessfully loged in")
        #//*[text()=" All Titles "]

    def test_navigate_test_automation_project(self):
        """ navigating All Tiles and locating the Test Automation Project, then click the project"""
        all_titles = self.driver.find_element(By.XPATH,'//*[text()=" All Titles "]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", all_titles)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, labels.test_automation_project))).click()

    def test_switch_to_details_tab(self):
        """ moving the bottom of page and select the details tab, then switch to video tab"""
        time.sleep(10)
        bottom_page = self.driver.find_element(By.XPATH,'//*[@id="test"]')
        self.driver.execute_script("arguments[0].scrollIntoView();",bottom_page)
        time.sleep(20)
        self.driver.find_element(By.ID,'detailsSection').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, labels.deatils_data)))
    def test_switch_back_video_tab(self):
        time.sleep(10)
        self.driver.find_element(By.ID,"videosSection").click()

#//*[@id="media-player"]/div[2]/div[13]/div[4]/div[1]

    def test_play_video_and_pause(self):
        self.driver.find_element(By.XPATH,'//*[@id="vid-01j912gbvdnr5er79gqeb8k30w"]/div/div[1]/button[1]').click()
        time.sleep(15)
        self.driver.find_element(By.CLASS_NAME,"jw-video jw-reset").click()
        # actions = ActionChains(self.driver)
        # actions.send_keys(Keys.TAB)
        # time.sleep(5)
        # actions.send_keys(Keys.ENTER).perform()
        #self.driver.find_element(By.XPATH,'//div[@class="jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback"]').click()
        # actions = ActionChains(self.driver)
        # actions.move_by_offset(100, 200).perform()
        # WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[1]'))
        # ).click()