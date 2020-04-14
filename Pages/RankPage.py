from Pages.GamePage import GamePage
import selenium


class RankPage(GamePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def go_to(self):
        self.browser.get(self.C.url['ranking'])

    def change_to_exp_page(self, page_num):
        script = self.C.script['change-rank-exp-begin'] + str(page_num) + self.C.script['change-rank-end']
        self.browser.execute_script(script)

    def change_to_won_duels_page(self, page_num):
        script = self.C.script['change-rank-won-duels-begin'] + str(page_num) + self.C.script['change-rank-end']
        self.browser.execute_script(script)

    def change_to_won_dollars_page(self, page_num):
        script = self.C.script['change-rank-won-dollars-begin'] + str(page_num) + self.C.script['change-rank-end']
        self.browser.execute_script(script)

    def gather_ids_from_page(self):
        by, value = self.C.locator['player-name']
        attempt = 0
        succeed = False
        while attempt <= self.user.gather_id_try and not succeed:
            try:
                elements = self.browser.find_elements(by, value)
                hrefs = list(map(lambda x: x.get_attribute('href'), elements))
                succeed = True
            except selenium.common.exceptions.StaleElementReferenceException:
                pass
            attempt += 1
        if not succeed:
            raise Exception('Gather ids from page failed due to too many StaleElementReferenceException')
        ids = set(map(lambda x: x.split('=')[1], hrefs))
        return ids
