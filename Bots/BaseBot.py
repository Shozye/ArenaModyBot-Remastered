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
        enemies = dict()
        file_path = 'enemies/' + self.user.profile_name + '-enemies.csv'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as csvfile:
                enemies_reader = csv.reader(csvfile)
                next(enemies_reader)
                for row in enemies_reader:
                    enemies[row[0]] = Enemy(row[0], ceil(float(row[1])), int(row[2]), int(row[3]), int(row[4]))
        # row[0], row[1], row[2], row[3], row[4] = id, next_attack_time, am_attacks, sum_prizes, last_attack_prize
        return enemies

    def save_enemies(self):
        enemies = self.enemies.values()
        enemies = [[x.id, ceil(x.next_attack_time), x.am_attacks, x.sum_prizes, x.last_attack_prize] for x in enemies]
        file_path = 'enemies/' + self.user.profile_name + '-enemies.csv'
        with open(file_path, 'w+', newline='') as csvfile:
            enemies_writer = csv.writer(csvfile)
            enemies_writer.writerow(["ID", "next_attack_time", "am_attacks", "sum_prizes", "last_attack_prize"])
            enemies_writer.writerows(enemies)

    def login(self):
        start_page = StartPage(self.browser, self.user)
        start_page.go_to()
        start_page.open_login_form()
        start_page.type_username()
        start_page.type_password()
        start_page.submit_login()
        start_page.refresh()

    def is_in_game(self):
        game_page = GamePage(self.browser, self.user)
        return game_page.is_at()

    def refresh(self):
        base_page = BasePage(self.browser, self.user)
        base_page.refresh()

    def get_stats(self):
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
        self.update_money()
        self.update_emeralds()
        self.update_energy()
        self.update_level()
        self.logger.debug('Succesfully updated status')
        self.logger.debug('money {}, emeralds {}, energy {}, level {}'.format(self.money, self.emeralds,
                                                                              self.energy, self.level))

    def quit(self):
        self.browser.quit()

    def better_than_enemy(self, enemy_stats, has_booster):
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
        if enemy_page.enemy_club() == self.user.my_club and self.user.my_club is not None or \
                not self.level - self.user.attack_enemies_with_level_max_lower_by <= enemy_page.enemy_level() <= \
                    self.level + self.user.attack_enemies_with_level_max_higher_by or \
                not self.better_than_enemy(enemy_page.enemy_stats(), enemy_page.has_boosters()):
            return False
        else:
            return True
