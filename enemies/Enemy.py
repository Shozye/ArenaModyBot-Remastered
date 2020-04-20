from UserConfig import UserConfig
class Enemy:
    def __init__(self, enemy_id, next_attack_time=0, am_attacks=0, sum_prizes=0, last_attack_prize=0):
        self.id = enemy_id
        self.next_attack_time = next_attack_time
        self.am_attacks = am_attacks
        self.sum_prizes = sum_prizes
        self.last_attack_prize = last_attack_prize
        self.user = UserConfig()

    def mean_and_last_attack(self):
        return ((self.sum_prizes / self.am_attacks) + self.last_attack_prize) / 2

    def worth(self):
        if self.am_attacks == 0:
            return self.user.worth_of_first_attack
        worth = self.mean_and_last_attack()
        if self.am_attacks == 1:
            worth += self.user.additional_worth_of_second_attack
        if self.am_attacks == 2:
            worth += self.user.additional_worth_of_third_attack
        return worth
