import os
import time
import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginOut(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_out_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        sign_out_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
        sign_out_text = "Logout"
        user_login.assert_element_text(self.driver, sign_out_xpath, sign_out_text)
        user_login.click_on_the_sign_out_button()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()
