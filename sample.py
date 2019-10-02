import logging
from src.utils import OptionParser
from src.utils import config_loggers
from src.generator import generate_log

logger = logging.getLogger(__name__)


def run():
    generate_log()


if __name__ == "__main__":
    """Main Function"""
    optmgr = OptionParser('sample')
    opts = optmgr.parser.parse_args()
    level = logging.DEBUG if opts.debug else logging.INFO
    config_loggers(level)
    run()
