from time import sleep
import requests

from feed.actionchains import KafkaActionPublisher, KafkaActionSubscription
from feed.crawling import BrowserService, BrowserActions, beginBrowserThread
from feed.settings import nanny_params

from feed.logger import getLogger

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start-browser', action='store_true', default=False)

logging= getLogger(__name__)



class CaptureCrawler(KafkaActionSubscription, KafkaActionPublisher, BrowserService):

    def __init__(self):
        KafkaActionSubscription.__init__(self, topic='sample-queue', implementation=BrowserActions)
        BrowserService.__init__(self)
        KafkaActionPublisher.__init__(self)

    def onClickActionCallback(self, actionReturn: BrowserActions.Return):
        if actionReturn is None:
            logging.warning(f'nothing returned for onClickActionCallback')
            return
        sleep(1)
        logging.info(f'posting sample source of length {len(self.driver.page_source)}')
        requests.post('http://{host}:{port}/samplepages/setExampleSource/{name}/{position}'.format(name=actionReturn.action.name, position=actionReturn.action.position+1, **nanny_params), data=self.driver.page_source.encode('utf-8'))

    def initialiseCallback(self, actionReturn: BrowserActions.Return, *args, **kwargs):
        requests.post('http://{host}:{port}/samplepages/setExampleSource/{name}/{position}'.format(name=actionReturn.name, position=0, **nanny_params), data=self.driver.page_source.encode('utf-8'))

if __name__ == '__main__':
    args = parser.parse_args()
    if args.startBrowser:
        bt = beginBrowserThread()

    runner = ActionChainImplementation()
    runner.main()
