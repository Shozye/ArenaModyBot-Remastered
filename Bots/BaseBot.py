from Pages.StartPage import StartPage
from Pages.GamePage import GamePage
from Pages.BasePage import BasePage
from enemies.Enemy import Enemy
from math import floor
from math import ceil
import logging
import csv
import os


class BaseBot:
    def __init__(self, browser, user):
        self.browser = browser
        self.user = user
        self.stats = None
        self.money = None
        self.emeralds = None
        self.energy = None
        self.level = None
        self.enemies = self.initialize_enemies()
        self.logger = logging.getLogger('main')

    def initialize_enemies(self):
        """This method takes information from enemies.csv and creates dictionary with information where key = ID
        :return: dictionary containing information about enemy characters.
        """
        enemies = dict()
        file_path = 'enemies/' + self.user.profile_name + '-enemies.csv'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as csv_file:
                enemies_reader = csv.reader(csv_file)
                next(enemies_reader)
                for row in enemies_reader:
                    enemies[row[0]] = Enemy(row[0], ceil(float(row[1])), int(row[2]), int(row[3]), int(row[4]))
        # row[0], row[1], row[2], row[3], row[4] = id, next_attack_time, am_attacks, sum_prizes, last_attack_prize
        return enemies

    def save_enemies(self):
        """This function saves information about enemies to enemies.csv
        """
        enemies = list(self.enemies.values())
        enemies.sort(key=lambda x: x.worth(), reverse=True)
        enemies = [[x.id, ceil(x.next_attack_time), x.am_attacks, x.sum_prizes, x.last_attack_prize] for x in enemies]
        file_path = 'enemies/' + self.user.profile_name + '-enemies.csv'
        with open(file_path, 'w+', newline='') as csv_file:
            enemies_writer = csv.writer(csv_file)
            enemies_writer.writerow(["ID", "next_attack_time", "am_attacks", "sum_prizes", "last_attack_prize"])
            enemies_writer.writerows(enemies)

    def login(self):
        """If WebDriver is not logged in, bot will log in to arenamody.pl with login/password from UserConfig.py
        """
        start_page = StartPage(self.browser, self.user)
        start_page.go_to()
        start_page.open_login_form()
        start_page.type_username()
        start_page.type_password()
        start_page.submit_login()
        game_page = GamePage(self.browser, self.user)
        game_page.refresh()
        game_page.turn_off_cookies_notification()

    def is_in_game(self):
        """
        :return: True if Web driver is at logged in and at site arenamody.pl
        """
        game_page = GamePage(self.browser, self.user)
        return game_page.is_at()

    def refresh(self):
        base_page = BasePage(self.browser, self.user)
        base_page.refresh()

    def get_stats(self):
        """Sets stats attribute to dictionary with keys=stat_name
        Web driver has to click popularity button to be able to acquire information.
        """
        game_page = GamePage(self.browser, self.user)
        game_page.show_my_stats()
        self.stats = game_page.my_stats()

    def update_money(self):
        game_page = GamePage(self.browser, self.user)
        self.money = game_page.my_money()

    def update_emeralds(self):
        game_page = GamePage(self.browser, self.user)
        self.emeralds = game_page.my_emeralds()

    def update_energy(self):
        game_page = GamePage(self.browser, self.user)
        self.energy = game_page.my_energy()

    def update_level(self):
        game_page = GamePage(self.browser, self.user)
        self.level = game_page.my_level()

    def update_status(self):
        """Updates money, emeralds, energy, level and put them into bot attributes.
        """
        self.refresh()
        self.update_money()
        self.update_emeralds()
        self.update_energy()
        self.update_level()
        self.logger.debug('Successfully updated status')
        self.logger.debug('money {}, emeralds {}, energy {}, level {}'.format(self.money, self.emeralds,
                                                                              self.energy, self.level))

    def quit(self):
        self.browser.quit()

    def better_than_enemy(self, enemy_stats, has_booster):
        """ Method that compares enemy stats to mine with uncertainty specified in UserConfig.py
        :param enemy_stats: dictionary with keys=stat_name, where values are enemy_stats
        :param has_booster: True if enemy uses any popularity booster, False otherwise
        :return: True if amount of better stats is bigger than value specified in UserConfig.py, False otherwise
        """
        multi = self.user.multi_booster if has_booster else 1
        style_better = floor(self.user.stat_multi * self.stats['style']) > enemy_stats['style'] * multi
        creativ_better = floor(self.user.stat_multi * self.stats['creativity']) > enemy_stats['creativity'] * multi
        devotion_better = floor(self.user.stat_multi * self.stats['devotion']) > enemy_stats['devotion'] * multi
        beauty_better = floor(self.user.stat_multi * self.stats['beauty']) > enemy_stats['beauty'] * multi
        generosity_better = floor(self.user.stat_multi * self.stats['generosity']) > enemy_stats['generosity'] * multi
        loyalty_better = floor(self.user.stat_multi * self.stats['loyalty']) > enemy_stats['loyalty'] * multi

        am_better = style_better + creativ_better + devotion_better + beauty_better + generosity_better + loyalty_better
        self.logger.debug('Amount of better stats {}'.format(am_better))
        if am_better >= self.user.am_of_stats_that_should_be_higher_than_enemy:
            return True
        else:
            return False

    def should_attack(self, enemy_page):
        """ Character should attack enemy if enemy meets level and club criteria specified in UserConfig.py
        :param enemy_page: EnemyPage page object
        :return: True if should attack else False
        """
        if enemy_page.enemy_club() == self.user.my_club and self.user.my_club is not None:
            return False
        enemy_level_range = range(self.user.enemy_level[0] + self.level, self.user.enemy_level[1] + self.level + 1)
        if enemy_page.enemy_level() in enemy_level_range and \
                self.better_than_enemy(enemy_page.enemy_stats(), enemy_page.has_boosters()):
            return True
        else:
            return False
