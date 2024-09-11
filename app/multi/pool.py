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
    with multiprocessing.Pool(2) as p:
        p1 = p.apply_async(worker1, (100, ))
        p2 = p.apply_async(worker1, (100, ))
        p3 = p.apply_async(worker1, (100, ))
        logging.debug('executed')
        logging.debug(p1.get(timeout=5))  # raise TimeoutError
        logging.debug(p2.get())
        logging.debug(p3.get())

# Pool(i) iは同時に走ることができるプロセスの数
# それを超えた数の処理をする場合は、待つことになる。
