from Pages.GamePage import GamePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium


class WorkPage(GamePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def go_to(self):
        self.browser.get(self.C.url['work-page'])

    def start_photo_session(self):
        self.retry_click(self.C.locator['photo-session-start-button'])

    def end_photo_session(self):
        self.retry_click(self.C.locator['photo-session-chance-button'])

    def close_photo_session_popup(self):
        self.browser.execute_script(self.C.script['close-popup'])

    def open_inventory(self):
        self.browser.execute_script(self.C.script['open-inventory'])

    def wait_until_photo_session_to_end(self):
        try:
            WebDriverWait(self.browser, self.user.how_much_time_wait_for_photo_session_end).until(
                EC.visibility_of_element_located(self.C.locator['photo-session-emerald'])
            )
        except selenium.common.exceptions.TimeoutException:
            self.refresh()
