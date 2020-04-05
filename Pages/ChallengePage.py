from Pages.GamePage import GamePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChallengePage(GamePage):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def challenge_enemy(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(self.C.locator['enemy-clothes']))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.C.locator['challenge-enemy']))
        self.retry_click('challenge-enemy')
