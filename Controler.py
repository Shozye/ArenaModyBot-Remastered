import logging
import os
from selenium import webdriver
import time
from Bots.BaseBot import BaseBot


class Controler:
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

        self.browser = webdriver.Chrome(self.driver_path)
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()

    def login_test(self):
        logging.info('login_test method executed')
        bot = BaseBot(self.browser, self.user)
        bot.login()
        assert bot.is_in_game(), 'Bot has not logged successfully'
        logging.info('Login_test was a success')
