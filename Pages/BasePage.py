from Constant import Constant
import selenium


class BasePage:
    def __init__(self, browser, user):
        self.browser = browser
        self.user = user

        const = Constant()
        self.url = const.url
        self.locator = const.locator

    def quit(self):
        self.browser.quit()

    def turn_off_cookies_notification(self):
        pass

    def retry_click(self, locator):
        clicked = False
        attempt = 0
        while attempt < 50 and not clicked:
            try:
                by, value = locator
                self.browser.find_element(by, value).click()
                clicked = True
            except selenium.common.exceptions.StaleElementReferenceException:
                pass
        if not clicked:
            raise Exception('StaleElementReferenceException occurred and even 50 clicks didnt fix it')

    def refresh(self):
        self.browser.refresh()
