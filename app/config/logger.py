import logging
import logtest
logging.basicConfig(level=logging.INFO)
# logging.info('info')

# loggerで先に設定したものを使用するのが望ましい
# loggingで出力しない
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')

logger.info('from main')
logtest.do_something()

# INFO:root:info
# INFO:logtest:from logtest

# どこでエラーが発生したかわかりやすい
