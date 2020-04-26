from selenium.webdriver.common.by import By


class Constant:
    """
    That Class is used to easier introduce changes to code,
    if selectors of web elements change
    It also helps in readability of code.
    """
    def __init__(self):
        self.Locator = self.Locator()
        self.Url = self.Url()
        self.Script = self.Script()

    class Locator:
        def __init__(self):
            # BasePage
            # ChallengePage
            self.enemy_clothes = (By.CSS_SELECTOR, 'div.rightLadyContent div div img')
            self.challenge_button_second = (By.ID, 'challengeLady')
            # EnemyPage
            self.challenge_button_first = (By.CLASS_NAME, 'chalange')
            self.overview = (By.CLASS_NAME, 'overview')
            self.club_name = (By.CLASS_NAME, 'div.user-guild div.rightRow a')
            self.enemy_level = (By.CLASS_NAME, 'level')
            self.enemy_style = (By.CSS_SELECTOR, 'div.style div.value')
            self.enemy_creativity = (By.CSS_SELECTOR, 'div.creativity div.value')
            self.enemy_devotion = (By.CSS_SELECTOR, 'div.devotion div.value')
            self.enemy_beauty = (By.CSS_SELECTOR, 'div.beauty div.value')
            self.enemy_generosity = (By.CSS_SELECTOR, 'div.generosity div.value')
            self.enemy_loyalty = (By.CSS_SELECTOR, 'div.loyalty div.value')
            self.booster_indicator = (By.CSS_SELECTOR, '#stats > span')
            # GamePage
            self.chat_button = (By.ID, 'js-chat-toggle-button')
            self.photo_session_timer = (By.ID, 'activity-timer')
            self.photo_session_emerald = (By.ID, 'activity-indicator-photosession')
            self.dollars = (By.ID, 'ladyDollars')
            self.emeralds = (By.ID, 'ladyEmerald')
            self.level = (By.ID, 'currentLevel')
            self.energy = (By.ID, 'ladyEnergy')
            self.popularity_button = (By.CSS_SELECTOR, 'div.hide button.fp-button')
            self.my_style = (By.ID, 'stat_style_all')
            self.my_creativity = (By.ID, 'stat_creativity_all')
            self.my_devotion = (By.ID, 'stat_devotion_all')
            self.my_beauty = (By.ID, 'stat_beauty_all')
            self.my_generosity = (By.ID, 'stat_generosity_all')
            self.my_loyalty = (By.ID, 'stat_loyalty_all')
            # RankPage
            self.turn_to_next_page_button = (By.CLASS_NAME, 'pagingRight')
            self.player_name = (By.CLASS_NAME, 'player-name')
            # StartPage
            self.login_button = (By.ID, 'login-btn')
            self.cookies_button = (By.CSS_SELECTOR, 'div>a.cc_btn.cc_btn_accept_all')
            self.user_field = (By.NAME, 'login_user')
            self.pass_field = (By.NAME, 'login_pass')
            self.submit_login = (By.ID, 'loginSubmit')
            # WorkPage
            self.photo_session_chance_button = (By.CSS_SELECTOR, 'span#ftvChanceBox-1 > a')
            self.photo_session_start_button = (By.CSS_SELECTOR, 'div#startWorkingFtvButton-1 > a')

    class Url:
        def __init__(self):
            # BasePage
            # ChallengePage
            # EnemyPage
            self.base_profile = 'https://g.arenamody.pl/profile.php?id='
            # GamePage
            # RankPage
            self.ranking = 'https://g.arenamody.pl/ranking.php'
            # StartPage
            self.start_page = 'https://arenamody.pl'
            # WorkPage
            self.work_page = 'https://g.arenamody.pl/jobs.php'

    class Script:
        def __init__(self):
            # RankPage
            self.change_rank_won_duels_begin = "getRanking('daily','duels_won',"
            self.change_rank_exp_begin = "getRanking('daily','exp',"
            self.change_rank_won_dollars_begin = "getRanking('daily','duels_money_won',"
            self.change_rank_end = ')'
            # WorkPage
            self.open_inventory = "ftvJobBoosters(1)"
            self.close_popup = "closePopup(1);"
