import logging
import logging.config
import os
import time


def config_logging():
    """
    This function should be used only once during initialization of the bot
    It configures logging.
    """
    if not os.path.isdir(os.path.join(os.getcwd(), 'logs')):
        os.mkdir('logs')
    if not os.path.isdir(os.path.join(os.getcwd(), 'logs', 'DEBUG')):
        os.mkdir(r'logs/DEBUG')
    if not os.path.isdir(os.path.join(os.getcwd(), 'logs', 'INFO')):
        os.mkdir(r'logs/INFO')

    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    date = time.strftime('_%y_%m_%d-%H_%M_%S_')
    form1 = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s')

    fh1 = logging.FileHandler('logs/DEBUG/debug' + date + '.log')
    fh1.setLevel(logging.DEBUG)
    fh1.setFormatter(form1)

    fh2 = logging.FileHandler('logs/INFO/info' + date + '.log')
    fh2.setLevel(logging.INFO)
    fh2.setFormatter(form1)

    ch1 = logging.StreamHandler()
    ch1.setLevel(logging.INFO)
    ch1.setFormatter(form1)

    logger.addHandler(fh1)
    logger.addHandler(fh2)

    sub_logger = logging.getLogger('w_ladies')
    sub_logger.setLevel(logging.INFO)

    form2 = logging.Formatter('%(asctime)s|%(message)s')
    fh3 = logging.FileHandler('logs/WorthyLadies.log')
    fh3.setLevel(logging.INFO)
    fh3.setFormatter(form2)

    sub_logger.addHandler(fh3)
