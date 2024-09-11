import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')


def worker2(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')


if __name__ == '__main__':
    barrier = threading.Barrier(2)
    t1 = threading.Thread(target=worker1, args=(barrier, ))
    t2 = threading.Thread(target=worker2, args=(barrier, ))
    t1.start()
    t2.start()

# Barrier(2)としているので2回barrier.wait()が実行されないと、次に進まない
# Thread-2: num=1
# Thread-2: start
# Thread-1: num=0
# Thread-1: start
# Thread-1: end
# Thread-1: start
# Thread-2: end
# ...繰り返し
