import logging
import argparse
import json

PROGRAM_VERSION = 'v0.1'

# Deafult config keyvalue
DEFAULT_FILENAME = './log.txt'

logger = logging.getLogger(__name__)
# Defined logger

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'brief': {
            'format': '[%(levelname)s] %(name)s: %(message)s'
        },
        'precise': {
            'format': '%(asctime)s.%(msecs)03d, [%(levelname)s], %(name)s, %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'level': 'WARN',
            'formatter': 'brief',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'level': 'INFO',
            'formatter': 'precise',
            'class': 'logging.FileHandler',
            'filename': 'logsimulator.log',
            'mode': 'w'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG'
        }
    }
}


class OptionParser():
    """Custom parsing class for command line arguments"""

    def __init__(self, program_name='PROG'):
        """User based option parser"""
        self.parser = argparse.ArgumentParser(program_name)
        self.parser.add_argument("--debug", "-d", action='store_true', dest='debug',
                                 default=False, help='show verbose output for debugging')
        self.parser.add_argument('--version', action='version',
                                 version=PROGRAM_VERSION)


def config_loggers(level):
    import logging.config
    if level == logging.DEBUG:
        LOGGING_CONFIG['handlers']['file']['level'] = 'DEBUG'
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.debug('Configured logger handlers')


def read_config(filename):
    """Read config file and output dict of parameters"""
    with open(filename, 'r') as f:
        data = json.load(f)
    if data is None:
        logger.critical(f'Configuration file {filename} is empty')
        exit()

    if 'filename' not in data:
        data['filename'] = DEFAULT_FILENAME
    if 'lines' not in data:
        data['lines'] = 1000
    return data
