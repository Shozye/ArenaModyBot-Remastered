from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium


class StartPage(BasePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def go_to(self):
        self.browser.get(self.url['StartPage'])
        pass

    def open_login_form(self):
        self.retry_click(self.locator['login-button'])
        try:
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((self.locator['submit-login']))
            )
        except selenium.common.exceptions.TimeoutException:
            self.retry_click(self.locator['login-button'])

    def type_username(self):
        by, value = self.locator['user-field']
        user_field = self.browser.find_element(by, value)
        user_field.send_keys(self.user.username)

    def type_password(self):
        by, value = self.locator['pass-field']
        pass_field = self.browser.find_element(by, value)
        pass_field.send_keys(self.user.password)

    def submit_login(self):
        by, value = self.locator['submit-login']
        submit = self.browser.find_element(by, value)
        submit.click()
        WebDriverWait(self.browser, 10).until(EC.url_contains('welcome.php'))
