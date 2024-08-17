import logging
logging.basicConfig(level=logging.INFO)


# Trueのときだけログを出力する
class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())

logger.info('from main')
logger.info('password = 1234')
logger.info('xxxx = 1234')

# INFO:__main__:from main
# INFO:__main__:xxxx = 1234