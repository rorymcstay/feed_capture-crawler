from time import sleep
import requests
import os

from feed.actionchains import KafkaActionPublisher, KafkaActionSubscription, ActionChain
from feed.crawling import BrowserService, BrowserActions
from feed.settings import nanny_params


from feed.logger import getLogger

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start-browser', action='store_true', default=False)

logging= getLogger(__name__)


class CaptureCrawler(KafkaActionSubscription, KafkaActionPublisher, BrowserService):

    def __init__(self):
        queue = f'sample-queue'
        logging.info(f'subscribing to {queue}')
        KafkaActionSubscription.__init__(self, queue, implementation=BrowserActions)
        BrowserService.__init__(self)
        KafkaActionPublisher.__init__(self)

    def onClickActionCallback(self, actionReturn: BrowserActions.Return, *args, **kwargs):
        if actionReturn is None:
            logging.warning(f'nothing returned for onClickActionCallback')
            return
        sleep(3)
        logging.info(f'posting sample source of length {len(self.driver.page_source)}')
        kwargs.get('chain').nannyClient.post(f'/samplepages/setExampleSource/{actionReturn.name}/{actionReturn.action.position}',
                                             payload=self.driver.page_source.encode('utf-8'))

    def onChainEndCallback(self, chain: ActionChain, ret, *args, **kwargs):
        logging.info(f'chain has returned')
        chain.repeating = False

    def initialiseCallback(self, actionReturn: BrowserActions.Return, *args, **kwargs):
        chain = kwargs.get("chain")
        logging.info(f'setting position=[{0}], name=[{actionReturn.name}]')
        chain.nannyClient.post(f'/samplepages/setExampleSource/{chain.name}/0', payload=self.driver.page_source.encode('utf-8'))

    def cleanUp(self):
        self._browser_clean_up()

