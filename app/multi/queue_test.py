import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(queue):
    logging.debug('start')
    queue.put(100)
    logging.debug('time sleep')
    time.sleep(5)
    logging.debug('time sleep end')
    queue.put(200)
    logging.debug('end')


def worker2(queue):
    logging.debug('start')
    logging.debug('t2 {}'.format(queue.get()))
    logging.debug('t2 {}'.format(queue.get()))
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    t1 = threading.Thread(target=worker1, args=(queue, ))
    t2 = threading.Thread(target=worker2, args=(queue, ))
    t1.start()
    t2.start()


# Thread-1: start
# time sleep
# Thread-2: start
# t2 100  queueに100が入っているのですぐにgetできる
# time sleep end
# Thread-1: end
# t2 200 queueに200が入るまで待つ
# Thread-2: end
