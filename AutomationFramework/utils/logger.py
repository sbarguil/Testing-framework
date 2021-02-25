import os 
import logging.handlers
import sys
import datetime

def setup_log(test_case, HOSTS):
    """setup logging"""
    timestamp = datetime.datetime.now().strftime("%d_%b_%Y_%H_%M_%S")
    vendor = HOSTS[0]['vendor']
    if not os.path.exists('./logs/'+vendor):
        os.makedirs('./logs/'+vendor)
    log_filename = "./logs/{}/{}_{}.log".format(vendor, test_case, timestamp)

    logger1 = logging.getLogger('ncclient.manager')
    logger1.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(log_filename)
    logformatter = logging.Formatter('%(message)s')
    handler.setFormatter(logformatter)
    logger1.addHandler(handler)
    return logging.getLogger('ncclient.manager')
