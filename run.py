from UserConfig import UserConfig
from Controler import Controler


def main():
    user = UserConfig()
    control_panel = Controler(user)

    '''
    Use methods below
    '''

    control_panel.login_test()


if __name__ == '__main__':
    main()
