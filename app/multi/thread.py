import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    # print(threading.currentThread().getName(), 'start')
    logging.debug('start')
    time.sleep(5)
    # print(threading.currentThread().getName(), 'end')
    logging.debug('end')


def worker2(x, y=1):
    # print(threading.currentThread().getName(), 'start')
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    # print(threading.currentThread().getName(), 'end')
    logging.debug('end')


if __name__ == '__main__':
    t1 = threading.Thread(name='rename worker1', target=worker1)
    t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y': 200})
    t1.start()
    t2.start()
    print('started')


# Thread-1 start
# Thread-2 start  ← Thread-1が終わるのを待たずにThread2が走る
# started
# Thread-1 end
# Thread-2 end


# rename worker1: start
# Thread-1: start
# Thread-1: 100
# Thread-1: 200
# started
# rename worker1: end
# Thread-1: end
