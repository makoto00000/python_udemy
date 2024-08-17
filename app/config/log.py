import logging

# loggingレベルを変更する（デフォルトはwarningまで）
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

# ファイルに出力するとき
# logging.basicConfig(filename='config/test.log', level=logging.DEBUG)

formatter = '%(levelname)s:%(message)s'  # DEBUG:root:debug
# formatter = '%(asctime)s:%(message)s'  # 2024-08-16 11:33:14,265:debug
logging.basicConfig(level=logging.DEBUG, format=formatter)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

logging.info('info {} {}'.format('test', 'test2'))
logging.info('info %s %s' % ('test', 'test2'))
logging.info('info %s %s', 'test', 'test2')

# formatterの書き方
# https://docs.python.org/ja/3/library/logging.html

# DEBUG	おもに問題を診断するときにのみ関心があるような、詳細な情報。
# INFO	想定された通りのことが起こったことの確認。
# WARNING	想定外のことが起こった、または問題が近く起こりそうである (例えば、'disk space low') ことの表示。
# ERROR	より重大な問題により、ソフトウェアがある機能を実行できないこと。
# CRITICAL	プログラム自体が実行を続けられないことを表す、重大なエラー。

# フォーマット
# created	タイムスタンプ（秒単位）
# levelname	ログレベル名（INFO, WARNING, etc.）
# levelno	ログレベル番号（10, 20, etc.）
# message	ログメッセージ
# module	ログ発生モジュール名
# filename	ログ発生ファイル名
# pathname	ログ発生ファイルのフルパス
# funcName	ログ発生関数名
# lineno	ログ発生行番号
# process	プロセスID
# thread	スレッドID
# threadName	スレッド名
# msecs	タイムスタンプのミリ秒部分
# relativeCreated	ロガー生成からの経過時間（ミリ秒）
