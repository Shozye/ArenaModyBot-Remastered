from Bots.BaseBot import BaseBot
from Pages.GamePage import GamePage
from Pages.WorkPage import WorkPage


class WorkerBot(BaseBot):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def during_any_photo_session_activity(self):
        game_page = GamePage(self.browser, self.user)
        if not game_page.is_during_photo_session() and not game_page.is_photo_session_to_end():
            return True
        else:
            return False

    def attack(self, enemy_id):
        pass

    def choose_enemy(self):
        pass

    def make_emerald_action(self):
        work_page = WorkPage(self.browser, self.user)
        work_page.go_to()
        if work_page.is_during_photo_session():
            work_page.wait_until_photo_session_to_end()
        elif work_page.is_photo_session_to_end():
            work_page.end_photo_session()
            work_page.close_photo_session_popup()
        else:
            work_page.start_photo_session()
