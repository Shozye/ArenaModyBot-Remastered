import logging
import os
from selenium import webdriver
import time
from Bots.BaseBot import BaseBot
from Bots.ProcessEnemiesBot import ProcessEnemiesBot
from Bots.WorkerBot import WorkerBot


class Controller:
    def __init__(self, user):
        self.user = user
        self.driver_path = user.driver_path if user.driver_path else os.path.join(os.getcwd(), 'chromedriver.exe')

        log_dir = os.path.join(os.getcwd(), 'logs')
        log_name = time.strftime("%Y%m%d%H%M%S") + '.log'
        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)
        logging.basicConfig(filename=os.path.join(log_dir, log_name),
                            level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        logging.info('Bot has started, user profile is ' + self.user.profile_name)

        self.browser = webdriver.Chrome(self.driver_path)
        self.browser.maximize_window()

    def login_test(self):
        logging.info('login_test method executed')
        bot = BaseBot(self.browser, self.user)
        bot.login()
        assert bot.is_in_game(), 'Bot has not logged successfully'
        logging.info('Login_test was a success!')
        bot.quit()

    def find_enemies(self):
        logging.info('find_enemies method executed')
        bot = ProcessEnemiesBot(self.browser, self.user)
        bot.login()
        bot.get_stats()
        bot.update_status()
        bot.get_potential_enemies()
        bot.sift_potential_enemies()
        bot.check_potential_enemies()

    def gather_emeralds(self):
        logging.info('gather_emeralds method executed')
        bot = WorkerBot(self.browser, self.user)
        bot.login()
        bot.update_status()
        while True:
            bot.make_emerald_action()
            bot.update_status()
            pass

    def gather_emeralds_and_fight(self):
        logging.info('gather_emeralds_and_fight method executed')
        bot = WorkerBot(self.browser, self.user)
        bot.login()
        bot.update_status()
        while True:
            if not bot.during_any_photo_session_activity():
                while bot.energy > self.user.energy_to_attack_buffer:
                    bot.attack(bot.choose_enemy())
                    bot.update_status()
            bot.make_emerald_action()
            pass

    def fight(self):
        logging.info('fight method executed')
        bot = WorkerBot(self.browser, self.user)
        bot.login()
        bot.update_status()
        if not bot.during_any_photo_session_activity():
            while bot.energy > 0:
                bot.attack(bot.choose_enemy())
                bot.update_status()
