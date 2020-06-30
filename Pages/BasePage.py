from Constant import Constant
import selenium
import logging


class BasePage:
    """
    Base Object to interact with web elements
    """
    def __init__(self, browser, user):
        self.browser = browser
        self.user = user
        self.logger = logging.getLogger('main')

        self.Locator = Constant().Locator
        self.Url = Constant().Url
        self.Script = Constant().Script

    def quit(self):
        self.browser.quit()

    def retry_click(self, locator):
        """
        Clicking with this method prevents from StaleElementReferenceException
        :param locator: (BY, value)
        """
        clicked = False
        attempt = 0
        by, value = locator
        while attempt < 50 and not clicked:
            try:
                self.browser.find_element(by, value).click()
                clicked = True
            except selenium.common.exceptions.StaleElementReferenceException:
                attempt += 1
        if not clicked:
            self.logger.critical('retry_click not working at value: {}'.format(str(value)))
            raise Exception('StaleElementReferenceException occurred and even 50 clicks didn\'t fix it')

    def refresh(self):
        self.browser.refresh()

    def get_text(self, locator):
        """
        Method used to get text from Web Element
        Prevents from StaleElementReferenceException
        :param locator: (By, value)
        """
        by, value = locator
        attempt = 0
        while attempt < 50:
            try:
                return self.browser.find_element(by, value).text
            except selenium.common.exceptions.StaleElementReferenceException:
                attempt += 1
        self.logger.critical('Couldn\'t get text of element {} {} because of StaleElementException')
        raise Exception('StaleElementReferenceException occurred in get text')
