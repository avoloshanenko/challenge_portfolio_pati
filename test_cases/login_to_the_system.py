import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):



    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)

        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        login_field_xpath = "//*[@id='login']"
        password_field_xpath = "//*[@id='password']"

        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')

        #user_login.type_in_field(login_field_xpath, 'user07@getnada.com')
        #user_login.type_in_field(password_field_xpath, 'Test-1234')

        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

        scouts_panel_xpath = "//header/div/h6"
        scout_panel_text = "Scouts Panel"
        user_login.assert_element_text(self.driver, scouts_panel_xpath, scout_panel_text)



    def tearDown(self):
        self.driver.quit()