class UserConfig:
    def __init__(self):
        self.profile_name = 'sample_profile'
        self.username = 'sample-username'
        self.password = 'sample-password'
        self.driver_path = None  # if None, then in the same file with Controller
        self.my_club = None  # should be string
        self.no_touch_girls = []  # type ids of characters that you don't want to attack ever
        self.attack_enemies_with_level_max_lower_by = 5
        self.attack_enemies_with_level_max_higher_by = 0
        self.experience_begin = 1  # inclusive
        self.experience_end = 30  # inclusive
        self.won_dollars_begin = 30  # inclusive
        self.won_dollars_end = 50  # inclusive
        self.won_duels_begin = 1  # inclusive
        self.won_duels_end = 0  # inclusive
        # before comparing stats with enemy, multiply your own stats by stat_multi
        # goal is to prevent losing
        self.stat_multi = 0.95
        self.multi_booster = 1.25
        self.am_of_stats_that_should_be_higher_than_enemy = 5
        self.gather_id_try = 10
        self.energy_to_attack_buffer = 8
        self.how_much_time_wait_for_photo_session_end = 1500
        self.additional_worth_of_second_attack = 500
        self.worth_of_first_attack = 1500
        self.additional_worth_of_third_attack = 250
        self.delay_after_no_challenge_button = 144000  # 40 hours
        self.first_money_won_threshold_after_attack = 300  # inclusive
        self.first_time_threshold_delay = 60 * 60 * 18
        self.second_money_won_threshold_after_attack = 1000  # inclusive
        self.second_time_threshold_delay = 60 * 60 * 6
        self.third_money_won_threshold_after_attack = 1500  # inclusive
        self.third_time_threshold_delay = 60 * 60 * 3
        self.forth_money_won_threshold_after_attack = 0  # inclusive
        self.forth_time_threshold_delay = 0
        self.normal_attack_delay = 60 * 60 + 1
        self.should_give_huge_delay_after_lost_fight = True
        self.huge_delay = 60 * 60 * 24 * 15  # 15 days
        self.delay_to_enemy_attacked_before_or_5_times = 60 * 60 * 1.5  # 1.5 hour
        self.delay_to_enemy_that_shouldnt_be_attacked = 60 * 60 * 24
