import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == '__main__':
    # threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()
        # threads.append(t)
    print(threading.enumerate())
    for thread in threading.enumerate():
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()


# Thread-1: start
# Thread-2: start
# Thread-3: start
# Thread-4: start
# Thread-5: start

# [<_MainThread(MainThread, started 281473655619616)>, <Thread(Thread-1, started daemon 281473645080992)>, <Thread(Thread-2, started daemon 281473565389216)>, <Thread(Thread-3, started daemon 281473554903456)>, <Thread(Thread-4, started daemon 281473544417696)>, <Thread(Thread-5, started daemon 281473533931936)>]

# <_MainThread(MainThread, started 281473655619616)>
# Thread-4: end
# Thread-1: end
# Thread-3: end
# Thread-5: end
# Thread-2: end
