from Pages.GamePage import GamePage
import selenium


class EnemyPage(GamePage):
    def __init__(self, browser, user, _id):
        super().__init__(browser, user)
        self.id = _id
        self.enemy_url = self.C.url['base-profile'] + _id

    def go_to(self):
        self.browser.get(self.enemy_url)

    def enemy_club(self):
        try:
            club_name = self.get_text(self.C.locator['club-name']).text
        except selenium.common.exceptions.NoSuchElementException:
            club_name = None
        return club_name

    def enemy_level(self):
        return self.get_text(self.C.locator['enemy-level']).split(' ')[1]

    def enemy_style(self):
        return self.get_text(self.C.locator['enemy-style'])

    def enemy_creativity(self):
        return self.get_text(self.C.locator['enemy-creativity'])

    def enemy_devotion(self):
        return self.get_text(self.C.locator['enemy-devotion'])

    def enemy_beauty(self):
        return self.get_text(self.C.locator['enemy-beauty'])

    def enemy_generosity(self):
        return self.get_text(self.C.locator['enemy-generosity'])

    def enemy_loyalty(self):
        return self.get_text(self.C.locator['enemy-loyalty'])

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
