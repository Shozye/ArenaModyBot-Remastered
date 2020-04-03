from Pages.StartPage import StartPage
from Pages.GamePage import GamePage


class BaseBot:
    def __init__(self, browser, user):
        self.browser = browser
        self.user = user

    def login(self):
        startPage = StartPage(self.browser, self.user)
        startPage.go_to()
        startPage.turn_off_cookies_notification()
        startPage.open_login_form()
        startPage.type_username()
        startPage.type_password()
        startPage.submit_login()

    def is_in_game(self):
        gamePage = GamePage(self.browser, self.user)
        return gamePage.is_at()
