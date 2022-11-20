from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*/button[contains(@ class, 'MuiButton')]"
    login_url = "https://scouts-test.futbolkolektyw.pl"
    expected_title = "Scouts panel - sign in"
    add_player_button_xpath = "//*[text () = 'Add player']/ancestor::button"
    scouts_panel_xpath = "//header/div/h6"
    login_url2 = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title2 = "Add player"
    button_sign_out = "//*[@ class = 'MuiList-root MuiList-padding'][2]/child::div[2]"
    button_language = "//*[@ class = 'MuiList-root MuiList-padding'][2]/child::div[1]"
    button_players = "//*[@ class = 'MuiList-root MuiList-padding'][1]/child::div[2]"

    def type_in_email(self, email):
        return self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        return self.field_send_keys(self.password_field_xpath, password)


    def click_on_the_sign_in_button(self):
        return self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert  self.get_page_title(self.login_url) == self.expected_title

    def title_of_page2(self):
        assert self.get_page_title(self.login_url2) == self.expected_title2

    def click_on_add_player_button(self):
        return self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_sign_out_button(self):
        return self.click_on_the_element(self.button_sign_out)

    def click_on_the_language_button(self):
        return self.click_on_the_element(self.button_language)

    def click_on_the_players_button(self):
        return self.click_on_the_element(self.button_players)




