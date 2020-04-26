import logging
import os
import traceback
import argparse

from feed.service import Client
from feed.settings import nanny_params

from src.main.actionchainimpl import CaptureCrawler
from feed.crawling import beginBrowserThread

parser = argparse.ArgumentParser()

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("kafka").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("selenium").setLevel(logging.WARNING)

parser.add_argument('--start-browser', action='store_true')


logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))



if __name__ == '__main__':
     cc = CaptureCrawler()
     cc.main()

