from pages.base_page import BasePage


class Dashboard(BasePage):
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

   pass