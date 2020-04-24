import os
from selenium import webdriver
from Bots.BaseBot import BaseBot
from Bots.ProcessEnemiesBot import ProcessEnemiesBot
from Bots.WorkerBot import WorkerBot
from logger.logger import config_logging
import logging


class Controller:
    def __init__(self, user):
        config_logging()
        self.user = user
        self.driver_path = user.driver_path if user.driver_path else os.path.join(os.getcwd(), 'chromedriver.exe')

        self.logger = logging.getLogger('main')
        self.logger.info('Bot has started, user profile is ' + self.user.profile_name)

        self.browser = webdriver.Chrome(self.driver_path)
        self.browser.maximize_window()

    def login_test(self):
        try:
            self.logger.info('login_test method executed')
            bot = BaseBot(self.browser, self.user)
            bot.login()
            assert bot.is_in_game(), 'Bot has not logged successfully'
            self.logger.info('Login_test was a success!')
            bot.quit()
        except Exception:
            self.logger.critical('logging_test thrown exception', exc_info=True)
            raise

    def find_enemies(self):
        try:
            self.logger.info('find_enemies method executed')
            bot = ProcessEnemiesBot(self.browser, self.user)
            bot.login()
            bot.get_stats()
            bot.update_status()
            bot.get_potential_enemies()
            bot.sift_potential_enemies()
            bot.check_potential_enemies()
            self.logger.info('Added {} new enemies to enemy list'.format(bot.am_new_enemies))
        except Exception:
            self.logger.critical('logging_test thrown exception', exc_info=True)
            raise

    def gather_emeralds(self):
        try:
            self.logger.info('gather_emeralds method executed')
            bot = WorkerBot(self.browser, self.user)
            bot.login()
            bot.update_status()
            while True:
                bot.make_emerald_action()
                bot.update_status()

        except Exception:
            self.logger.critical('gather_emeralds thrown exception', exc_info=True)
            raise

    def gather_emeralds_and_fight(self):
        try:
            self.logger.info('gather_emeralds_and_fight method executed')
            bot = WorkerBot(self.browser, self.user)
            bot.login()
            bot.update_status()
            bot.get_stats()
            while True:
                if not bot.during_any_photo_session_activity():
                    while bot.energy > self.user.energy_to_attack_buffer:
                        bot.attack(bot.choose_enemy())
                        bot.update_status()
                bot.make_emerald_action()
                bot.update_status()
        except Exception:
            self.logger.critical('gathered emeralds and fight thrown exception', exc_info=True)
            raise

    def fight(self):
        try:
            self.logger.info('fight method executed')
            bot = WorkerBot(self.browser, self.user)
            bot.login()
            bot.update_status()
            if not bot.during_any_photo_session_activity():
                while bot.energy > 0:
                    bot.attack(bot.choose_enemy())
                    bot.update_status()
        except Exception:
            self.logger.critical('fight thrown exception', exc_info=True)
            raise

    def test_logger(self):
        self.logger.info('info test')
        self.logger.debug('debug test')
        self.logger.error('error test')
        self.logger.critical('critical test')
