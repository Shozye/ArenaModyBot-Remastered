from Bots.BaseBot import BaseBot
from Pages.GamePage import GamePage
from Pages.WorkPage import WorkPage
from Pages.EnemyPage import EnemyPage
import time


class WorkerBot(BaseBot):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def during_any_photo_session_activity(self):
        game_page = GamePage(self.browser, self.user)
        if not game_page.is_during_photo_session() and not game_page.is_photo_session_to_end():
            return True
        else:
            return False

    def attack(self, enemy_id):
        enemy_page = EnemyPage(self.browser, self.user, enemy_id)
        enemy_page.go_to()
        if enemy_page.enemy_club() == self.user.my_club and self.user.my_club is not None:
            return False
        if not self.level - self.user.attack_enemies_with_level_max_lower_by <= enemy_page.enemy_level() <= \
               self.level + self.user.attack_enemies_with_level_max_higher_by:
            return False
        return True if self.better_than_enemy(enemy_page.enemy_stats()) else False

    def choose_enemy(self):
        self.enemies.sort(key=lambda x: x.sorting_function(), reverse=True)
        for enemy in self.enemies:
            if enemy.next_attack_time > time.time():
                return enemy
        raise Exception('Every next_attack_time in enemies is in future')
        pass

    def make_emerald_action(self):
        work_page = WorkPage(self.browser, self.user)
        work_page.go_to()
        if work_page.is_during_photo_session():
            work_page.wait_until_photo_session_to_end()
        elif work_page.is_photo_session_to_end():
            work_page.end_photo_session()
            work_page.close_photo_session_popup()
        else:
            work_page.start_photo_session()
