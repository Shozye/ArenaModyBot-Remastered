class UserConfig:
    def __init__(self):
        self.profile_name = 'sample_profile'
        self.username = 'sample-username'
        self.password = 'sample-password'
        self.driver_path = None  # if None, then in the same file with Controller
        self.my_club = None  # should be string
        self.no_touch_girls = []  # type ids of characters that you don't want to attack ever
        self.enemy_level = (-5, -1)  # Attack enemies in this interval regarding to your level inclusive both
        # Left number of enemy_level should be lower than right
        self.experience_begin = 1  # inclusive
        self.experience_end = 50  # inclusive
        self.won_dollars_begin = 20  # inclusive
        self.won_dollars_end = 50  # inclusive
        self.won_duels_begin = 20  # inclusive
        self.won_duels_end = 50  # inclusive
        # before comparing stats with enemy, multiply your own stats by stat_multi
        # goal is to prevent losing
        self.stat_multi = 0.95  # Your stats are going to be multiplied by this to prevent random losing
        self.multi_booster = 1.25  # If enemy has got booster, multiply his stats by this
        self.am_of_stats_that_should_be_higher_than_enemy = 5
        self.gather_id_try = 10
        self.energy_to_attack_buffer = 6  # Bot will attack enemy if it has got higher energy than this number
        self.how_much_time_wait_for_photo_session_end = 1500
        #  Following three variables should be used to encourage bot to fight new enemies
        self.worth_of_first_attack = 1500  # enemies that haven't been attacked yet, are expected to give this  dollars
        self.additional_worth_of_second_attack = 500  # this value will be added to enemy worth was attacked once
        self.additional_worth_of_third_attack = 250  # this value will be added to enemy worth was attacked twice
        # If money acquired from enemy will be less that amount of money_won_threshold_after_attack
        # time of next attack will be delayed by time_threshold_delay
        # value of delay should be longer than 1 hour
        # put 0 in money_won_threshold to disable
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
        # enemy 'shouldnt' be attacked if he has got level that do not match previous config
        # or if he is in your club
        # or if he has got better stats than your character
        self.delay_to_enemy_that_shouldnt_be_attacked = 60 * 60 * 24  # 1 day
        self.delay_after_no_challenge_button = 144000  # 40 hours
        self.worthy_lady_dollar_threshold = 500
