from Bots.BaseBot import BaseBot
from Pages.GamePage import GamePage
from Pages.WorkPage import WorkPage
from Pages.EnemyPage import EnemyPage
import time


class WorkerBot(BaseBot):
    def __init__(self, browser, user):
        super().__init__(browser, user)
        self.gathered_emeralds = 0

    def during_any_photo_session_activity(self):
        game_page = GamePage(self.browser, self.user)
        if game_page.is_during_photo_session() or game_page.is_photo_session_to_end():
            self.logger.debug('Bot is during photo session activity')
            return True
        else:
            self.logger.debug('Bot is NOT during photo session activity')
            return False

    def attack(self, enemy_id):
        enemy_page = EnemyPage(self.browser, self.user, enemy_id)
        enemy_page.go_to()
        money_before = self.money
        if self.should_attack(enemy_page):
            if enemy_page.challenge_button_exist():
                challenge_page = enemy_page.challenge()
                challenge_page.challenge_enemy()

                prize = challenge_page.my_money() - money_before
                if prize == 0:
                    challenge_page.refresh()
                    prize = challenge_page.my_money() - money_before
                if prize == 0:
                    self.enemies[enemy_id].update_enemy_attacked_before_or_attacked_5_times()
                else:
                    self.logger.info('Money acquired from {} is {}'.format(enemy_id, prize))
                    self.enemies[enemy_id].update_after_fight(prize)
            else:
                self.enemies[enemy_id].update_after_no_challenge_button()
            self.save_enemies()
        else:
            self.enemies[enemy_id].update_enemy_shouldnt_be_attacked_not_in_range_level_or_stats()
            self.logger.debug('Enemy {} shouldn\'t be attacked, skipping.'.format(enemy_id))

    def choose_enemy(self):
        values = list(self.enemies.values())
        values.sort(key=lambda x: x.worth(), reverse=True)
        for enemy in values:
            print(enemy.next_attack_time, time.time())
            if enemy.next_attack_time < time.time():
                self.logger.debug('Enemy chosen to be attacked is {}'.format(enemy.id))
                return enemy.id
        raise Exception('You cant attack any enemy at the moment because their next_attack_time is in future')
        pass

    def make_emerald_action(self):
        work_page = WorkPage(self.browser, self.user)
        work_page.go_to()
        if work_page.is_during_photo_session():
            work_page.wait_until_photo_session_to_end()
        elif work_page.is_photo_session_to_end():
            emeralds_before = work_page.my_emeralds()
            work_page.end_photo_session()
            work_page.close_photo_session_popup()
            emeralds_after = work_page.my_emeralds()
            change = emeralds_after - emeralds_before
            self.logger.info('Amount of gathered emeralds {}. Thats {} in total'.format(change, self.gathered_emeralds))
            self.refresh()
        else:
            work_page.start_photo_session()
