from Pages.GamePage import GamePage


class RankPage(GamePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def go_to(self):
        self.browser.get(self.C.url['ranking'])

    def change_to_experience(self):
        self.browser.execute_script(self.C.script['change-to-exp'])

    def change_to_won_duels(self):
        self.browser.execute_script(self.C.script['change-to-won-duels'])

    def change_to_won_dollars(self):
        self.browser.execute_script(self.C.script['change-to-won-dollars'])

    def turn_to_next_page(self):
        self.retry_click(self.C.locator['turn-to-next-page-button'])

    def gather_ids_from_page(self):
        by, value = self.C.locator['player-name']
        elements = self.browser.find_elements(by, value)
        hrefs = list(map(lambda x: x.getAttribute['href'], elements))
        ids = list(map(lambda x: x.split('=')[1], hrefs))
        return ids
