import Controler


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
        self.experience_end = 8  # inclusive
        self.won_dollars_begin = 1  # inclusive
        self.won_dollars_end = 0  # inclusive
        self.won_duels_begin = 1  # inclusive
        self.won_duels_end = 0  # inclusive
        # before comparing stats with enemy, multiply your own stats by stat_multi
        # goal is to prevent losing
        self.stat_multi = 0.95
        self.am_of_stats_that_should_be_higher_than_enemy = 5
        self.gather_id_try = 10
        self.energy_to_attack_buffer = 8
        self.how_much_time_wait_for_photo_session_end = 1500
