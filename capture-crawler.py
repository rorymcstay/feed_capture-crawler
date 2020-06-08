import logging
from logging.config import dictConfig
import os
import traceback
import argparse

from feed.service import Client
from feed.settings import nanny_params, logger_settings_dict

from src.main.actionchainimpl import CaptureCrawler






if __name__ == '__main__':
    dictConfig(logger_settings_dict('root'))
    logging.getLogger('conn').setLevel('WARNING')
    logging.getLogger('urllib').setLevel('WARNING')
    logging.getLogger('parser').setLevel('WARNING')
    logging.getLogger('metrics').setLevel('WARNING')
    logging.getLogger('connectionpool').setLevel('WARNING')
    logging.getLogger('kafka').setLevel('WARNING')
    logging.getLogger('config').setLevel('WARNING')
    logging.info("####### Environment #######")
    logging.debug(logger_settings_dict('root'))
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("kafka").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.getLogger("selenium").setLevel(logging.WARNING)




    logging.info("\n".join([f'{key}={os.environ[key]}' for key in os.environ]))

    cc = CaptureCrawler()
    cc.main()

