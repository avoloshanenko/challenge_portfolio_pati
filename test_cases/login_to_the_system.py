import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):
    sign_in_button_xpath = "//*/button[contains(@ class, 'MuiButton')]"

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)

        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):

        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        user_login.click_on_the_sign_in_button()


        scouts_panel_xpath = "//header/div/h6"
        scout_panel_text = "PANEL SKAUTINGOWY"
        user_login.assert_element_text(self.driver, scouts_panel_xpath, scout_panel_text)



    def tearDown(self):
        self.driver.quit()