import os
import time
import unittest
from selenium import webdriver

from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(BasePage):

    driver = None
    add_player_name_xpath = '//input[@name="name"]'
    add_player_surname_xpath = '//input[@name="surname"]'
    add_player_main_position = '//input[@name="mainPosition"]'
    add_player_age = '//input[@name="age"]'
    add_player_button_submit = '//*[contains(@ class, "MuiCardActions-root")]/child::button[1]'

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)

        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        user_login.click_on_add_player_button()
        user_login.title_of_page()
        time.sleep(5)



    @classmethod
    def tearDown(self):
        self.driver.quit()

    def type_in_name(self, name):
        return self.field_send_keys(self.add_player_name_xpath, name)

    def type_in_surname(self, surname):
        return self.field_send_keys(self.add_player_surname_xpath, surname)

    def type_in_main_position(self, position):
        return self.field_send_keys(self.add_player_main_position, position)

    def type_in_age(self, age):
        return self.field_send_keys(self.add_player_age, age)
    def click_on_the_submit_button(self):
        return self.click_on_the_element(self.add_player_button_submit)
