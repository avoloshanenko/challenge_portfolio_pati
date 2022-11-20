import os
import time
import unittest
from selenium import webdriver

from pages.add_a_player import TestAddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayers(unittest.TestCase):



    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)

        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        user_login2 = Dashboard(self.driver)
        user_login2.click_on_add_player_button()
        #user_login.title_of_page2()
        user_login3 = TestAddPlayer(self.driver)
        user_login3.type_in_name('User')
        user_login3.type_in_surname('User')
        user_login3.type_in_main_position('Player')
        user_login3.type_in_age('01.01.2000')
        user_login3.click_on_the_submit_button()







