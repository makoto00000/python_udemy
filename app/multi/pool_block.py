import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')
    return i


if __name__ == '__main__':
    with multiprocessing.Pool(3) as p:
        logging.debug(p.apply(worker1, (200, )))
        logging.debug('executed apply')
        p1 = p.apply_async(worker1, (100, ))
        p2 = p.apply_async(worker1, (100, ))
        logging.debug('executed')
        logging.debug(p1.get(timeout=5))  # raise TimeoutError
        logging.debug(p2.get())


# ForkPoolWorker-1: start
# ForkPoolWorker-1: end
# MainProcess: 200
# MainProcess: executed apply  p.apply()で実行されたものは終わるのを待つ
# MainProcess: executed
# ForkPoolWorker-3: start
# ForkPoolWorker-2: start
# ForkPoolWorker-3: end
# ForkPoolWorker-2: end
# MainProcess: 100
# MainProcess: 100
