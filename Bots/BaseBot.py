from Pages.StartPage import StartPage
from Pages.GamePage import GamePage


class BaseBot:
    def __init__(self, browser, user):
        self.browser = browser
        self.user = user
        self.stats = None
        self.money = None
        self.emeralds = None
        self.energy = None
        self.level = None

    def login(self):
        start_page = StartPage(self.browser, self.user)
        start_page.go_to()
        start_page.open_login_form()
        start_page.type_username()
        start_page.type_password()
        start_page.submit_login()

    def is_in_game(self):
        game_page = GamePage(self.browser, self.user)
        return game_page.is_at()

    def get_stats(self):
        game_page = GamePage(self.browser, self.user)
        game_page.show_my_stats()
        self.stats = game_page.my_stats()

    def update_money(self):
        game_page = GamePage(self.browser, self.user)
        self.money = game_page.my_money()

    def update_emeralds(self):
        game_page = GamePage(self.browser, self.user)
        self.emeralds = game_page.my_emeralds()

    def update_energy(self):
        game_page = GamePage(self.browser, self.user)
        self.energy = game_page.my_energy()

    def update_level(self):
        game_page = GamePage(self.browser, self.user)
        self.level = game_page.my_level()

    def update_status(self):
        self.update_money()
        self.update_emeralds()
        self.update_energy()
        self.update_level()

    def quit(self):
        self.browser.quit()
