import argparse
import json

PROGRAM_VERSION = 'v0.1'

# Deafult config keyvalue
DEFAULT_FILENAME = './log.txt'


class OptionParser():
    """Custom parsing class for command line arguments"""

    def __init__(self, program_name='PROG'):
        """User based option parser"""
        self.parser = argparse.ArgumentParser(program_name)
        self.parser.add_argument("--debug", "-d", action='store_true', dest='debug',
                                 default=False, help='show verbose output for debugging')
        self.parser.add_argument('--version', action='version',
                                 version=PROGRAM_VERSION)


def read_config(filename):
    """Read config file and output dict of parameters"""
    with open(filename, 'r') as f:
        data = json.load(f)
    if data is None:
        print('Empty configuration file')
        exit()

    if 'filename' not in data:
        data['filename'] = DEFAULT_FILENAME
    if 'lines' not in data:
        data['lines'] = 1000
    return data
