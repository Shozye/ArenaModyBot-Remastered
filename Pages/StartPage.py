from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium


class StartPage(BasePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def turn_off_cookies_notification(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(self.C.locator['cookies-button'])
            )
            self.retry_click(self.C.locator['cookies-button'])
        except selenium.common.exceptions.TimeoutException:
            pass

    def go_to(self):
        self.browser.get(self.C.url['start-page'])
        pass

    def open_login_form(self):
        self.retry_click(self.C.locator['login-button'])
        try:
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((self.C.locator['submit-login']))
            )
        except selenium.common.exceptions.TimeoutException:
            self.retry_click(self.C.locator['login-button'])

    def type_username(self):
        by, value = self.C.locator['user-field']
        user_field = self.browser.find_element(by, value)
        user_field.send_keys(self.user.username)

    def type_password(self):
        by, value = self.C.locator['pass-field']
        pass_field = self.browser.find_element(by, value)
        pass_field.send_keys(self.user.password)

    def submit_login(self):
        by, value = self.C.locator['submit-login']
        submit = self.browser.find_element(by, value)
        submit.click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.C.locator['chat-button']))
