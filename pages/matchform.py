from pages.base_page import BasePage


class MatchForm(BasePage):
    input_my_team = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[1]"
    input_enemy_team = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[2]"
    input_my_team_score = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[3]"
    input_enemy_team_score = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[4]"
    input_date = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[5]"
    check_box_match = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[6]"
    input_color = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[7]"
    input_league = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[8]"
    input_time_played = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[9]"
    input_number = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[10]"
    input_web_match = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[11]"
    input_general = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[12]"
    input_rating = "//*[contains(@ class, 'MuiGrid-spacing-x')]/child::div[13]"
    button_submit = "//*[contains(@ class, 'MuiCard')]/child::button[1]"
    button_clear = "//*[contains(@ class, 'MuiCard')]/child::button[2]"
    button_name_player = "//*[contains(@ class, 'MuiList-root')][2]/child::div[1]"
    button_matches = "//*[contains(@ class, 'MuiList-root')][2]/child::div[2]"
    button_reports = "//*[contains(@ class, 'MuiList-root')][2]/child::div[3]"

