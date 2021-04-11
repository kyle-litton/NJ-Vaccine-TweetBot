import logging
from threading import Thread
from harvester import Harvester
import time

logging.getLogger('harvester').setLevel(logging.CRITICAL)

harvester = Harvester('127.0.0.1',1999)

tokens = harvester.intercept_recaptcha_v3(domain='riteaid.com', sitekey='6LcsQtQUAAAAAAvgAsY9ZxCFE9I-hkK2k36Igdme')

server_thread = Thread(target=harvester.serve, daemon=True)
server_thread.start()

# launch a browser instance where we can solve the captchas
harvester.launch_browser()

while True:
    time.sleep(2)