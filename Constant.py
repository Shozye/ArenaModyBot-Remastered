from selenium.webdriver.common.by import By


class Constant:
    def __init__(self):
        self.locator = self.init_locator()
        self.url = self.init_url()

    def init_locator(self):
        locator = {
            'chat-button': (By.ID, 'js-chat-toggle-button'),
            'login-button': (By.ID, 'login-btn'),
            'cookies-button': (By.CSS_SELECTOR, 'div>a.cc_btn.cc_btn_accept_all'),
            'user-field': (By.NAME, 'login_user'),
            'pass-field': (By.NAME, 'login_pass'),
            'submit-login': (By.ID, 'loginSubmit')

        }
        return locator

    def init_url(self):
        url = {
            'StartPage': 'https://arenamody.pl'
        }
        return url
