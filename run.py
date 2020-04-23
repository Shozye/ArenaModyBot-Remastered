from UserConfig import UserConfig
from Controler import Controller


def main():
    user = UserConfig()
    control_panel = Controller(user)

    '''
    Use methods below
    '''

    # control_panel.login_test()
    # control_panel.find_enemies()
    control_panel.gather_emeralds()
    # control_panel.gather_emeralds_and_fight()
    # control_panel.fight()
    # control_panel.test_logger()
if __name__ == '__main__':
    main()
