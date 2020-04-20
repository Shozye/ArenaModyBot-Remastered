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
                EC.visibility_of_element_located(self.Locator.cookies_button)
            )
            self.retry_click(self.Locator.cookies_button)
        except selenium.common.exceptions.TimeoutException:
            pass

    def go_to(self):
        self.browser.get(self.Url.start_page)
        pass

    def open_login_form(self):
        self.retry_click(self.Locator.login_button)
        try:
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((self.Locator.submit_login))
            )
        except selenium.common.exceptions.TimeoutException:
            self.retry_click(self.Locator.login_button)

    def type_username(self):
        by, value = self.Locator.user_field
        user_field = self.browser.find_element(by, value)
        user_field.send_keys(self.user.username)

    def type_password(self):
        by, value = self.Locator.pass_field
        pass_field = self.browser.find_element(by, value)
        pass_field.send_keys(self.user.password)

    def submit_login(self):
        by, value = self.Locator.submit_login
        submit = self.browser.find_element(by, value)
        submit.click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.Locator.chat_button))
