from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium


class StartPage(BasePage):
    """Page Object to navigate through login screen.
    """
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def go_to(self):
        self.browser.get(self.Url.start_page)
        self.logger.debug('Browser is at start page')
        pass

    def open_login_form(self):
        self.retry_click(self.Locator.login_button)
        try:
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(self.Locator.submit_login)
            )
        except selenium.common.exceptions.TimeoutException:
            self.retry_click(self.Locator.login_button)
        self.logger.debug('login form has been opened')

    def type_username(self):
        by, value = self.Locator.user_field
        user_field = self.browser.find_element(by, value)
        user_field.send_keys(self.user.username)
        self.logger.debug('Username typed')

    def type_password(self):
        by, value = self.Locator.pass_field
        pass_field = self.browser.find_element(by, value)
        pass_field.send_keys(self.user.password)
        self.logger.debug('Password typed')

    def submit_login(self):
        by, value = self.Locator.submit_login
        submit = self.browser.find_element(by, value)
        submit.click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.Locator.chat_button))
        self.logger.debug('Logged to game')
