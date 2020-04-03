from Pages.BasePage import BasePage
import selenium


class GamePage(BasePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def is_at(self):
        try:
            by, value = self.locator['chat-button']
            messages_icon = self.browser.find_element(by, value)
            if messages_icon.is_displayed():
                return True
            else:
                return False
        except selenium.common.exceptions.NoSuchElementException:
            return False
