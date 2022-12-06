import time

from pages.base_page import BasePage



class Dashboard(BasePage):
   expected_title = "Scouts panel"
   dashboard_url = "https://scouts.futbolkolektyw.pl/en"
   header_xpath = "//header"
   side_navigation = "//*[contains(@class, 'MuiDrawer-root')]"
   section_scouts_panel = "//*[contains(@class, 'MuiGrid-spacing-xs-2')][2]/child::div[1]"
   section_shortcuts = "//*[contains(@class, 'MuiGrid-spacing-xs-2')][2]/child::div[2]"
   section_activity = "//*[contains(@class, 'MuiGrid-spacing-xs-2')][2]/child::div[3]"
   section_players_count = "//*[contains(@class, 'MuiGrid-spacing-xs-2')][1]/child::div[1]"
   section_matches_count = "//*[contains(@class, 'MuiGrid-spacing-xs-2')][1]/child::div[2]"
   section_reports_count = "//*[contains(@class, 'MuiGrid-spacing-xs-2')][1]/child::div[3]"
   section_events_count = "//*[contains(@class, 'MuiGrid-spacing-xs-2')][1]/child::div[4]"
   button_main_page = "//*[@ class = 'MuiList-root MuiList-padding'][1]/child::div[1]"
   button_players = "//*[@ class = 'MuiList-root MuiList-padding'][1]/child::div[2]"
   button_language = "//*[@ class = 'MuiList-root MuiList-padding'][2]/child::div[1]"
   button_sign_out = "//*[@ class = 'MuiList-root MuiList-padding'][2]/child::div[2]"
   players_url = "https://scouts.futbolkolektyw.pl/en/players"
   add_player_button_xpath = "//*[text () = 'Add player']/ancestor::button"

   def title_of_page(self):
      self.wait_for_element_to_be_clickable(self.button_players)
      assert self.get_page_title(self.dashboard_url) == self.expected_title

   def click_on_add_player_button(self):
      return self.click_on_the_element(self.add_player_button_xpath)