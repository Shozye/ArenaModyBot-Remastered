from Constant import Constant
import selenium
import logging


class BasePage:
    def __init__(self, browser, user):
        self.browser = browser  # type: selenium.webdriver.chrome.webdriver.WebDriver
        self.user = user
        self.logger = logging.getLogger('main')

        self.Locator = Constant().Locator
        self.Url = Constant().Url
        self.Script = Constant().Script

    def quit(self):
        self.browser.quit()

    def retry_click(self, locator):
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
            raise Exception('StaleElementReferenceException occurred and even 50 clicks didnt fix it')

    def refresh(self):
        self.browser.refresh()

    def get_text(self, locator):
        by, value = locator
        attempt = 0
        while attempt < 50:
            try:
                return self.browser.find_element(by, value).text
            except selenium.common.exceptions.StaleElementReferenceException:
                attempt += 1
        self.logger.critical('Couldnt get text of element {} {} because of StaleElementException')
        raise Exception('StaleElementReferenceException occured in get text')
