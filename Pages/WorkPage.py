from Pages.GamePage import GamePage


class WorkPage(GamePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def start_photo_session(self):
        self.retry_click(self.C.locator['photo-session-start-button'])

    def chance_photo_session(self):
        self.retry_click(self.C.locator['photo-session-chance-button'])

    def close_photo_session_popup(self):
        self.browser.execute_script(self.C.script['close-popup'])

    def open_inventory(self):
        self.browser.execute_script(self.C.script['open-inventory'])
