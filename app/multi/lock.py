import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    time.sleep(5)
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')


# worker1をwithで書いたもの
def worker3(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
        logging.debug(d)

    logging.debug('end')


# withの2重構造にすると内側のlockは外側のlockが終わるのを待ち続けるのでプログラムが終わらない
def worker4(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] += 1

    logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    # lock = threading.Lock()
    lock = threading.RLock()  # RLockなら2重Lockでも処理できる
    t1 = threading.Thread(target=worker4, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()

# Thread-1: start
# Thread-2: start
# Thread-1: {'x': 1}  t1に5秒かかる処理があるがlockがreleaseされるまでt2は待つ。
# Thread-1: end
# Thread-2: {'x': 2}
# Thread-2: end
