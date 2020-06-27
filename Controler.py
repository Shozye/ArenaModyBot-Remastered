import os
from selenium import webdriver
from Bots.BaseBot import BaseBot
from Bots.ProcessEnemiesBot import ProcessEnemiesBot
from Bots.WorkerBot import WorkerBot
from logger.logger import config_logging
import logging


class Controller:
    """
    Using one of methods in this class should be enough to run bot
    Names of the methods should clearly state what actions bot is going to take
    They should be run at run.py
    """
    def __init__(self, user):
        config_logging()
        self.user = user
        self.driver_path = user.driver_path if user.driver_path else os.path.join(os.getcwd(), 'chromedriver.exe')

        self.logger = logging.getLogger('main')
        self.logger.info('Bot has started, user profile is ' + self.user.profile_name)

        self.browser = webdriver.Chrome(self.driver_path)
        self.browser.maximize_window()
        self.browser.implicitly_wait(0.5)

    def find_enemies(self):
        """
        Bot needed to use methods connected with fight
        After running this method, in enemies directory, there should be
        checked_enemies.csv and enemies.csv file found that contain
        ids of enemies that are going to be attacked
        """
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
        """
        To use this method, you need to run find_enemies() method first
        """
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
        """
        to use this method, you need to run find_enemies() first
        After using this, bot will fight enemies until energy run out
        """
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

    def recheck_checked_enemies(self):
        bot = ProcessEnemiesBot(self.browser, self.user)
        bot.login()
        bot.update_status()
        bot.get_stats()
        for index in range(len(bot.checked_enemies)):
            enemy_id = bot.checked_enemies[index]
            if bot.should_add_to_enemies(enemy_id) and enemy_id not in list(bot.enemies.keys()):
                bot.add_to_enemies(enemy_id)
                self.logger.info(enemy_id + " added to enemies")

    def recheck_enemies(self):
        bot = ProcessEnemiesBot(self.browser, self.user)
        bot.login()
        bot.update_status()
        bot.get_stats()
        to_del = []
        for enemy_id in list(bot.enemies.keys()):
            if not bot.should_add_to_enemies(enemy_id):
                to_del.append(enemy_id)

        for enemy_id in to_del:
            del bot.enemies[enemy_id]
            self.logger.info(enemy_id + " deleted.")
        bot.save_enemies()