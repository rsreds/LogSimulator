import argparse
import json

PROGRAM_VERSION = 'v0.1'


class OptionParser():
    def __init__(self, program_name='PROG'):
        """User based option parser"""
        self.parser = argparse.ArgumentParser(program_name)
        self.parser.add_argument("--debug", "-d", action='store_true', dest='debug',
                                 default=False, help='show verbose output for debugging')
        self.parser.add_argument('--version', action='version',
                                 version=PROGRAM_VERSION)


def read_config(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    if data:
        return data
    else:
        print('Error in the configuration file')
        print('ABORT')
        exit()
