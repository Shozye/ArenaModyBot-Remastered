from Pages.GamePage import GamePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium


class WorkPage(GamePage):
    """Page Object to navigate through work page.
    """
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def go_to(self):
        self.browser.get(self.Url.work_page)
        self.logger.debug('Browser is at work page')

    def start_photo_session(self):
        self.retry_click(self.Locator.photo_session_start_button)
        self.logger.debug('Photo session started')

    def end_photo_session(self):
        self.retry_click(self.Locator.photo_session_chance_button)
        self.logger.debug('Photo session ended')

    def close_photo_session_popup(self):
        self.browser.execute_script(self.Script.close_popup)
        self.logger.debug('Photo session closed popup')

    def wait_until_photo_session_to_end(self):
        try:
            WebDriverWait(self.browser, self.user.how_much_time_wait_for_photo_session_end).until(
                EC.visibility_of_element_located(self.Locator.photo_session_emerald)
            )
        except selenium.common.exceptions.TimeoutException:
            self.refresh()
