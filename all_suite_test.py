import unittest

from unittest.loader import makeSuite



from test_cases.add_player import TestAddPlayers
from test_cases.change_language_main_page import TestChangeLanguage
from test_cases.click_on_players_button import TestClickButton
from test_cases.framework import Test
from test_cases.login_out import TestLoginOut
from test_cases.login_to_the_system import TestLoginPage


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddPlayers))
   test_suite.addTest(makeSuite(TestLoginOut))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestClickButton))
   test_suite.addTest(makeSuite(TestChangeLanguage))
   test_suite.addTest(makeSuite(Test))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())