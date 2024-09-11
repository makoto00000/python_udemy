from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager
)

# import logging
# import threading
# import time

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(threadName)s: %(message)s')


# def worker1(i):
#     logging.debug('start')
#     time.sleep(5)
#     logging.debug('end')


# def worker2(i):
#     logging.debug('start')
#     time.sleep(i)
#     logging.debug('end')


# if __name__ == '__main__':
#     i = 5
#     t1 = threading.Thread(target=worker1, args={i, })
#     t2 = threading.Thread(name='renamed worker2', target=worker2, args=(i, ))
#     t1.start()
#     t2.start()


import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    time.sleep(i)
    logging.debug('end')


if __name__ == '__main__':
    i = 2
    t1 = multiprocessing.Process(target=worker1, args={i, })
    t2 = multiprocessing.Process(
        name='renamed worker2', target=worker2, args=(i, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
