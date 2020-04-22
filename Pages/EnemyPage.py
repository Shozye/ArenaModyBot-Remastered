from Pages.GamePage import GamePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium


class EnemyPage(GamePage):
    def __init__(self, browser, user, _id):
        super().__init__(browser, user)
        self.id = _id
        self.enemy_url = self.Url.base_profile + _id

    def go_to(self):
        self.browser.get(self.enemy_url)
        self.logger.debug('Entered {}'.format(self.enemy_url))

    def enemy_club(self):
        self.browser.implicitly_wait(0)
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.Locator.overview))
        by, value = self.Locator.club_name
        try:
            club_name = self.browser.find_element(by, value).text
            self.logger.debug('Enemy club was {}'.format(club_name))
        except selenium.common.exceptions.NoSuchElementException:
            club_name = None
            self.logger.debug('Enemy wasnt in any club')
        self.browser.implicitly_wait(30)
        return club_name

    def enemy_level(self):
        return int(self.get_text(self.Locator.enemy_level).split(' ')[1])

    def enemy_style(self):
        return int(self.get_text(self.Locator.enemy_style))

    def enemy_creativity(self):
        return int(self.get_text(self.Locator.enemy_creativity))

    def enemy_devotion(self):
        return int(self.get_text(self.Locator.enemy_devotion))

    def enemy_beauty(self):
        return int(self.get_text(self.Locator.enemy_beauty))

    def enemy_generosity(self):
        return int(self.get_text(self.Locator.enemy_generosity))

    def enemy_loyalty(self):
        return int(self.get_text(self.Locator.enemy_loyalty))

    def enemy_stats(self):
        stats = {
            "style": self.enemy_style(),
            "devotion": self.enemy_devotion(),
            "beauty": self.enemy_beauty(),
            "generosity": self.enemy_generosity(),
            "loyalty": self.enemy_loyalty(),
            "creativity": self.enemy_creativity()
        }
        return stats

    def challenge_button_exist(self):
        by, value = self.Locator.challenge_button
        if len(self.browser.find_elements(by, value)) == 0:
            return False
        return True

    def challenge(self):
        self.retry_click(self.Locator.challenge_button)
        self.logger.debug('Challenged lady with ID {}'.format(self.id))

    def has_boosters(self):
        by, value = self.Locator.booster_indicator
        if len(self.browser.find_elements(by, value)) == 0:
            return False
        return True
