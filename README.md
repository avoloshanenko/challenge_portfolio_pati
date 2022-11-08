# Task 1: software configuration.
## Subtask 1: Why did I choose to participate in the Dare IT Challenge
I decided to take up the challenge. I want to change my life and for that, I have to do other things which I haven't done before.   I have chosen this project because what you have promised me isn't easy way. Valuable knowledge isn't given easily as well as experience. I have enough dreams which I haven't carried through yet. It's time for their realization. I look forward to gaining experience as a tester and I'm ready to learn hard
You will hardly hear from me: "I'm interested in doing testing", you will see it in my accomplishments.

# Task 2: selectors
## Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page.
**sign_in_button_xpath**  
//*[text()='Sign in']  
//*/span[@ class = 'MuiButton-label']  
//*[@id="__next"]/form/div/div[2]/button/span[1]  

**scouts_panel_xpath**  
//*[text()='Scouts Panel']
//h5[contains(@ class, 'MuiTypography-root')]
//*[@id="__next"]/form/div/div[1]/h5

**password_xpath**  
//div[contains(@ class, 'MuiCardContent-root' )]/child::div[2]
//*[text()='Password']/parent::div
//*[@id="__next"]/form/div/div[1]/div[2]

**password_label_xpath**  
//*[text()='Password']
//*[@id="password-label"]

**password_input_xpath**  
//*[@id="password"] 

**login_hyperlink_xpath**  
//div[contains(@ class, 'MuiCardContent-root' )]/child::div[1]
//*[text()='Login']/parent::div
//*[@id="__next"]/form/div/div[1]/div[1]

**login_label_xpath**  
//*[text()='Login']
//*[@id="login-label"]

**login_input_xpath**  
//*[@id="login"]


**language_button_xpath**  
//div[contains(@ class, 'MuiSelect-select')]
//*[@id="__next"]/form/div/div[2]/div/div
//*[text()='English']

**remaind_password_hyperlink_xpath**  
//*[@id="__next"]/form/div/div[1]/a
//*[text()="Remind password"]
//child::div/a






