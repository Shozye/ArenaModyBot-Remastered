from Bots.BaseBot import BaseBot
from Pages.RankPage import RankPage
from Pages.EnemyPage import EnemyPage
from enemies.Enemy import Enemy
import csv
import os


class ProcessEnemiesBot(BaseBot):
    """Class used to actions such as finding new enemies, preparing enemy list to future use by WorkerBot
    """
    def __init__(self, browser, user):
        super().__init__(browser, user)
        self.potential_enemies = list()
        self.checked_enemies_file_path = 'enemies/' + self.user.profile_name + '-checked-enemies.csv'
        self.checked_enemies = self.initialize_checked_enemies()
        self.am_new_enemies = 0

    def initialize_checked_enemies(self):
        """This method takes information out of .csv file and put them into memory
        :return: list containing strings - ids of enemies
        """
        checked_enemies = list()
        if os.path.isfile(self.checked_enemies_file_path):
            with open(self.checked_enemies_file_path, 'r') as csv_file:
                checked_enemies_reader = csv.reader(csv_file)
                next(checked_enemies_reader)  # omitting header
                for row in checked_enemies_reader:
                    # row[0] is enemy id
                    checked_enemies.append(row[0])
        return checked_enemies

    def save_checked_enemies(self):
        """This method takes infomation out of memory and saves it in .csv file
        """
        with open(self.checked_enemies_file_path, 'w+', newline='') as csv_file:
            checked_enemies_writer = csv.writer(csv_file)
            checked_enemies_writer.writerow(['Enemy ID'])
            for enemy_id in self.checked_enemies:
                checked_enemies_writer.writerow([enemy_id])  # because enemy_id is a string

    def get_potential_enemies(self):
        """Method used to gather all potential enemies from rank page according to criteria specified in UserConfig.py
        """
        potential_enemies = set()
        rank_page = RankPage(self.browser, self.user)
        rank_page.go_to()
        for num_page in range(self.user.experience_begin, self.user.experience_end + 1):
            rank_page.change_to_exp_page(num_page)
            potential_enemies = potential_enemies | rank_page.gather_ids_from_page()
        for num_page in range(self.user.won_duels_begin, self.user.won_duels_end + 1):
            rank_page.change_to_won_dollars_page(num_page)
            potential_enemies = potential_enemies | rank_page.gather_ids_from_page()
        for num_page in range(self.user.won_dollars_begin, self.user.won_dollars_end + 1):
            rank_page.change_to_won_duels_page(num_page)
            potential_enemies = potential_enemies | rank_page.gather_ids_from_page()
        self.potential_enemies = list(potential_enemies)

    def sift_potential_enemies(self):
        """Method that deletes any potential enemy that is in checked_enemies list.
        """
        to_del = []
        for enemy_id in self.potential_enemies:
            if enemy_id in self.user.no_touch_girls or enemy_id in self.checked_enemies:
                to_del.append(enemy_id)
        for enemy_id in to_del:
            self.potential_enemies.remove(enemy_id)

    def should_add_to_enemies(self, enemy_id):
        """
        :param enemy_id: string
        :return: True if enemy meets level and club criteria specified in UserConfig.py
        """
        enemy_page = EnemyPage(self.browser, self.user, enemy_id)
        enemy_page.go_to()
        return self.should_attack(enemy_page)

    def add_to_enemies(self, enemy_id):
        """ Adds enemy to enemy list
        :param enemy_id: string
        """
        self.enemies[enemy_id] = Enemy(enemy_id)
        self.logger.info('{} added to enemies'.format(enemy_id))
        self.am_new_enemies += 1
        self.save_enemies()

    def add_to_checked_enemies(self, enemy_id):
        """ Adds enemy id to checked_enemies
        :param enemy_id: string
        """
        self.checked_enemies.append(enemy_id)
        self.save_checked_enemies()

    def check_potential_enemies(self):
        """Bot goes into every profile page of characters from potential_enemies and compares
        level, statistics and club if he meets criteria specified in UserConfig.py. Adds to enemies if so
        """
        for enemy_id in self.potential_enemies:
            if self.should_add_to_enemies(enemy_id):
                self.add_to_enemies(enemy_id)
            self.add_to_checked_enemies(enemy_id)

    def check_checked_enemies(self):
        """Bot goes into every profile page of characters from checked_enemies and compares
        level, statistics and club if he meets criteria specified in UserConfig.py. Adds to enemies if so
        """
        for enemy_id in self.checked_enemies:
            if self.should_add_to_enemies(enemy_id):
                self.logger.debug('Adding to enemies {}'.format(enemy_id))
                self.add_to_enemies(enemy_id)

    def check_enemies(self):
        """Bot goes into every profile page of characters from enemies and compares
        level, statistics and club if he meets criteria specified in UserConfig.py. Deletes from enemies if not.
        """
        for enemy_id in self.enemies:
            if not self.should_add_to_enemies(enemy_id):
                self.logger.debug('Deleting from enemies {}'.format(enemy_id))
                del self.enemies[enemy_id]
