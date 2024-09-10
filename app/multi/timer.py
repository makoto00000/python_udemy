import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == '__main__':
    # 3秒後にthreadが開始される
    t = threading.Timer(3, worker1, args=(100, ), kwargs={'y': 200})
    t.start()

# 3秒後に以下が実行
# Thread-1: start
# Thread-1: 100
# Thread-1: 200
# Thread-1: end
