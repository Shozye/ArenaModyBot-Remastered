from UserConfig import UserConfig
from Controler import Controller


def main():
    user = UserConfig()
    control_panel = Controller(user)
    '''
    Use methods below
    '''

    control_panel.find_enemies()
    # control_panel.gather_emeralds()
    # control_panel.gather_emeralds_and_fight()
    # control_panel.fight()
    # control_panel.test_logger()
    # control_panel.recheck_checked_enemies()
    # control_panel.recheck_enemies()

if __name__ == '__main__':
    main()
