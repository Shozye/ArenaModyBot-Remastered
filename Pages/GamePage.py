from Pages.BasePage import BasePage
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GamePage(BasePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def is_at(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.Locator.chat_button))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def my_money(self):
        return int(self.get_text(self.Locator.dollars).replace(',', ''))

    def my_level(self):
        return int(self.get_text(self.Locator.level))

    def my_energy(self):
        energy = int(self.get_text(self.Locator.energy))
        self.logger.debug('My energy is '.format(energy))
        return energy

    def my_emeralds(self):
        return int(self.get_text(self.Locator.emeralds).replace(',', ''))

    def show_my_stats(self):
        self.retry_click(self.Locator.popularity_button)
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.Locator.my_loyalty)
        )

    def my_stats(self):
        # debug
        stats = {'style': int(self.get_text(self.Locator.my_style)),
                 'generosity': int(self.get_text(self.Locator.my_generosity)),
                 'creativity': int(self.get_text(self.Locator.my_creativity)),
                 'beauty': int(self.get_text(self.Locator.my_beauty)),
                 'loyalty': int(self.get_text(self.Locator.my_loyalty)),
                 'devotion': int(self.get_text(self.Locator.my_devotion))}
        return stats

    def is_during_photo_session(self):
        by, value = self.Locator.photo_session_timer
        return True if self.browser.find_element(by, value).is_displayed() else False

    def is_photo_session_to_end(self):
        by, value = self.Locator.photo_session_emerald
        return True if self.browser.find_element(by, value).is_displayed() else False
