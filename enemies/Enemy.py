class Enemy:
    def __init__(self, enemy_id, last_attack_time=0, am_attacks=0, sum_prizes=0):
        self.id = enemy_id
        self.last_attack_time = last_attack_time
        self.am_attacks = am_attacks
        self.sum_prizes = sum_prizes
