from simulator.utils import OptionParser
from simulator.generator import generate_log

DEBUG = False


def run():
    generate_log()
    if DEBUG:
        print('Run main function')


if __name__ == "__main__":
    """Main Function"""
    optmgr = OptionParser('sample')
    opts = optmgr.parser.parse_args()
    DEBUG = True if opts.debug else False
    run()
