from Pages.BasePage import BasePage
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GamePage(BasePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def is_at(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.C.locator['chat-button']))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def my_money(self):
        return int(self.get_text(self.C.locator['dollars']).replace(',', ''))

    def my_level(self):
        return int(self.get_text(self.C.locator['level']))

    def my_energy(self):
        return int(self.get_text(self.C.locator['energy']))

    def my_emeralds(self):
        return int(self.get_text(self.C.locator['emeralds']).replace(',', ''))

    def show_my_stats(self):
        self.retry_click(self.C.locator['popularity-button'])
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.C.locator['my-loyalty'])
        )

    def my_stats(self):
        # debug
        stats = {'style': int(self.get_text(self.C.locator['my-style'])),
                 'generosity': int(self.get_text(self.C.locator['my-generosity'])),
                 'creativity': int(self.get_text(self.C.locator['my-creativity'])),
                 'beauty': int(self.get_text(self.C.locator['my-beauty'])),
                 'loyalty': int(self.get_text(self.C.locator['my-loyalty'])),
                 'devotion': int(self.get_text(self.C.locator['my-devotion']))}
        return stats

    def is_during_photo_session(self):
        by, value = self.C.locator['photo-session-timer']
        return True if self.browser.find_element(by, value).is_displayed() else False

    def is_photo_session_to_end(self):
        by, value = self.C.locator['photo-session-emerald']
        return True if self.browser.find_element(by, value).is_displayed() else False
