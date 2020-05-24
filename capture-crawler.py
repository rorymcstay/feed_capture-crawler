import logging
import os
import traceback
import argparse

from feed.service import Client
from feed.settings import nanny_params

from src.main.actionchainimpl import CaptureCrawler


logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("kafka").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("selenium").setLevel(logging.WARNING)




logging.info("\n".join([f'{key}={os.environ[key]}' for key in os.environ]))




if __name__ == '__main__':
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s]%(thread)d: %(module)s - %(levelname)s - %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

     cc = CaptureCrawler()
     cc.main()

