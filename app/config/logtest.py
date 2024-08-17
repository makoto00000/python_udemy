import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ファイルに書き込む場合（ロギングハンドラー）
# このモジュールのログだけファイルに書きこまれる
h = logging.FileHandler('config/logtest.log')
logger.addHandler(h)


def do_something():
    logger.info('from logtest')
    logger.debug('from logtest debug')
