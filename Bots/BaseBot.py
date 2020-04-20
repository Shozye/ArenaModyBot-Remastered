from Pages.StartPage import StartPage
from Pages.GamePage import GamePage
from Pages.BasePage import BasePage
from enemies.Enemy import Enemy
from math import floor
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

    def initialize_enemies(self):
        enemies = dict()
        file_path = 'enemies/' + self.user.profile_name + '-enemies.csv'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as csvfile:
                enemies_reader = csv.reader(csvfile)
                next(enemies_reader)
                for row in enemies_reader:
                    # row[0], row[1], row[2], row[3] = id, last_attack_time, am_attacks, sum_prizes
                    enemies[row[0]] = Enemy(row[0], row[1], row[2], row[3])
        return enemies

    def save_enemies(self):
        enemies = self.enemies.values()
        enemies = [[x.id, x.last_attack_time, x.am_attacks, x.sum_prizes] for x in enemies]
        file_path = 'enemies/' + self.user.profile_name + '-enemies.csv'
        with open(file_path, 'w+', newline='') as csvfile:
            enemies_writer = csv.writer(csvfile)
            enemies_writer.writerow(["ID", "last_attack_time", "am_attacks", "sum_prizes"])
            enemies_writer.writerows(enemies)
        pass

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

    def quit(self):
        self.browser.quit()

    def better_than_enemy(self, enemy_stats):
        style_better = floor(self.user.stat_multi * self.stats['style']) > enemy_stats['style']
        creativity_better = floor(self.user.stat_multi * self.stats['creativity']) > enemy_stats['creativity']
        devotion_better = floor(self.user.stat_multi * self.stats['devotion']) > enemy_stats['devotion']
        beauty_better = floor(self.user.stat_multi * self.stats['beauty']) > enemy_stats['beauty']
        generosity_better = floor(self.user.stat_multi * self.stats['generosity']) > enemy_stats['generosity']
        loyalty_better = floor(self.user.stat_multi * self.stats['loyalty']) > enemy_stats['loyalty']
        if style_better + creativity_better + devotion_better + beauty_better + generosity_better + loyalty_better >= \
                self.user.am_of_stats_that_should_be_higher_than_enemy:
            return True
        else:
            return False
