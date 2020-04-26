from UserConfig import UserConfig
import time


class Enemy:
    """
    Utility Class to help organise enemies
    It's main objective is to calculate expected value of money to get from enemy
    Second objective is to update it's values
    """
    def __init__(self, enemy_id, next_attack_time=0, am_attacks=0, sum_prizes=0, last_attack_prize=0):
        self.id = enemy_id
        self.next_attack_time = next_attack_time
        self.am_attacks = am_attacks
        self.sum_prizes = sum_prizes
        self.last_attack_prize = last_attack_prize
        self.user = UserConfig()

    def mean_and_last_attack(self):
        '''
        :return: integer, expected value of money to get from enemy
        '''
        return ((self.sum_prizes / self.am_attacks) + self.last_attack_prize) / 2

    def worth(self):
        '''
        This method adds an artificial expected value to real expected value
        Artificial expected value is needed to encourage bot to attack this character
        This method should be used for sorting enemies
        :return: integer
        '''
        if self.am_attacks == 0:
            return self.user.worth_of_first_attack
        worth = self.mean_and_last_attack()
        if self.am_attacks == 1:
            worth += self.user.additional_worth_of_second_attack
        if self.am_attacks == 2:
            worth += self.user.additional_worth_of_third_attack
        return worth

    def update_after_no_challenge_button(self):
        """
        Updates enemy if challenge button is not displayed for user (probably blocked or on holidays)
        """
        self.next_attack_time = time.time() + self.user.delay_after_no_challenge_button

    def update_after_fight(self, prize):
        '''
        :param prize: integer, money acquired from enemy
        '''
        self.am_attacks += 1
        self.sum_prizes += prize
        self.last_attack_prize = prize
        self.next_attack_time = time.time()
        if prize < 0 and self.user.should_give_huge_delay_after_lost_fight:  # lost fight
            self.next_attack_time += self.user.huge_delay
        elif prize < 0:
            self.next_attack_time += self.user.normal_attack_delay
        elif prize <= self.user.first_money_won_threshold_after_attack:
            self.next_attack_time += self.user.first_time_threshold_delay
        elif prize <= self.user.second_money_won_threshold_after_attack:
            self.next_attack_time += self.user.second_time_threshold_delay
        elif prize <= self.user.third_money_won_threshold_after_attack:
            self.next_attack_time += self.user.third_time_threshold_delay
        elif prize <= self.user.forth_money_won_threshold_after_attack:
            self.next_attack_time += self.user.forth_time_threshold_delay
        else:
            self.next_attack_time += self.user.normal_attack_delay

    def update_enemy_attacked_before_or_attacked_5_times(self):
        self.next_attack_time = time.time() + self.user.delay_to_enemy_attacked_before_or_5_times

    def update_enemy_shouldnt_be_attacked_not_in_range_level_or_stats(self):
        self.next_attack_time = time.time() + self.user.delay_to_enemy_that_shouldnt_be_attacked
