from Pages.GamePage import GamePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium


class EnemyPage(GamePage):
    def __init__(self, browser, user, _id):
        super().__init__(browser, user)
        self.id = _id
        self.enemy_url = self.C.url['base-profile'] + _id

    def go_to(self):
        self.browser.get(self.enemy_url)

    def enemy_club(self):
        self.browser.implicitly_wait(0)
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.C.locator['overview']))
        by, value = self.C.locator['club-name']
        try:
            club_name = self.browser.find_element(by, value).text
        except selenium.common.exceptions.NoSuchElementException:
            club_name = None
        self.browser.implicitly_wait(30)
        return club_name

    def enemy_level(self):
        return int(self.get_text(self.C.locator['enemy-level']).split(' ')[1])

    def enemy_style(self):
        return int(self.get_text(self.C.locator['enemy-style']))

    def enemy_creativity(self):
        return int(self.get_text(self.C.locator['enemy-creativity']))

    def enemy_devotion(self):
        return int(self.get_text(self.C.locator['enemy-devotion']))

    def enemy_beauty(self):
        return int(self.get_text(self.C.locator['enemy-beauty']))

    def enemy_generosity(self):
        return int(self.get_text(self.C.locator['enemy-generosity']))

    def enemy_loyalty(self):
        return int(self.get_text(self.C.locator['enemy-loyalty']))

    def challenge_button_exist(self):
        by, value = self.C.locator['challenge-button']
        if len(self.browser.find_elements(by, value)) == 0:
            return False
        return True
        pass

    def challenge(self):
        self.retry_click(self.C.locator['challenge-button'])
        pass

    def has_boosters(self):
        by, value = self.C.locator['booster-indicator']
        if len(self.browser.find_elements(by, value)) == 0:
            return False
        return True
        pass
