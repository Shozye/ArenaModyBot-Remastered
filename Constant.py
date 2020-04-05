from selenium.webdriver.common.by import By


class Constant:
    def __init__(self):
        self.locator = self.init_locator()
        self.url = self.init_url()
        self.script = self.init_script()

    def init_locator(self):
        locator = {
            # BasePage
            # ChallengePage
            'enemy-clothes': (By.CSS_SELECTOR, 'div.rightLadyContent div div img'),
            'challenge-button': (By.ID, 'challengeLady'),
            # EnemyPage
            'club-name': (By.CSS_SELECTOR, '.user-guild li a'),
            'enemy-level': (By.CLASS_NAME, 'level'),
            'enemy-style': (By.CSS_SELECTOR, 'div.style div.value'),
            'enemy-creativity': (By.CSS_SELECTOR, 'div.creativity div.value'),
            'enemy-devotion': (By.CSS_SELECTOR, 'div.devotion div.value'),
            'enemy-beauty': (By.CSS_SELECTOR, 'div.beauty div.value'),
            'enemy-generosity': (By.CSS_SELECTOR, 'div.generosity div.value'),
            'enemy-loyalty': (By.CSS_SELECTOR, 'div.loyalty div.value'),
            # GamePage
            'chat-button': (By.ID, 'js-chat-toggle-button'),
            'photo-session-timer': (By.ID, 'activity-timer'),
            'photo-session-emerald': (By.ID, 'activity-indicator-photosession'),
            'dollars': (By.ID, 'ladyDollars'),
            'emeralds': (By.ID, 'ladyEmerald'),
            'level': (By.ID, 'currentLevel'),
            'energy': (By.ID, 'ladyEnergy'),
            'popularity-button': (By.CSS_SELECTOR, 'div.hide button.fp-button'),
            'my-style': (By.ID, 'stat_style_all'),
            'my-creativity': (By.ID, 'stat_creativity_all'),
            'my-devotion': (By.ID, 'stat_devotion_all'),
            'my-beauty': (By.ID, 'stat_beauty_all'),
            'my-generosity': (By.ID, 'stat_generosity_all'),
            'my-loyalty': (By.ID, 'stat_loyalty_all'),
            # RankPage
            'turn-to-next-page-button': (By.CLASS_NAME, 'pagingRight'),
            'player-name': (By.CLASS_NAME, 'player-name'),
            # StartPage
            'login-button': (By.ID, 'login-btn'),
            'cookies-button': (By.CSS_SELECTOR, 'div>a.cc_btn.cc_btn_accept_all'),
            'user-field': (By.NAME, 'login_user'),
            'pass-field': (By.NAME, 'login_pass'),
            'submit-login': (By.ID, 'loginSubmit'),
            # WorkPage
            'photo-session-chance-button': (By.CSS_SELECTOR, 'span#ftvChanceBox-1 > a'),
            'photo-session-start-button': (By.CSS_SELECTOR, 'div#startWorkingFtvButton-1 > a'),
        }
        return locator

    def init_url(self):
        url = {
            # BasePage
            # ChallengePage
            # EnemyPage
            'base-profile': 'https://g.arenamody.pl/profile.php?id=',
            # GamePage
            # RankPage
            'ranking': 'https://g.arenamody.pl/ranking.php',
            # StartPage
            'StartPage': 'https://arenamody.pl'
            # WorkPage
        }
        return url

    def init_script(self):
        script = {
            # RankPage
            'change-to-exp': "getRanking(currentType, 'exp'); return false;",
            'change-to-won-duels': "getRanking(currentType, 'duels_won'); return false;",
            'change-to-won-dollars': "getRanking(currentType, 'duels_money_won'); return false;",
            # WorkPage
            'open-inventory': "ftvJobBoosters(1)",
            'close-popup': "closePopup(1);",
        }
        return script
