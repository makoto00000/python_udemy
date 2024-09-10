import logging
import queue
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()

    logging.debug('looooooooooong')
    time.sleep(5)
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(10):
        queue.put(i)
    t1 = threading.Thread(target=worker1, args=(queue, ))
    t1.start()
    logging.debug('tasks are not done')
    queue.join()  # task_done()を待つ
    logging.debug('tasks are done')
    queue.put(None)  # whileをbreakするため
    t1.join()  # t1が終わるのを待つ

# Thread-1: start
# Thread-1: 0
# Thread-1: 1
# Thread-1: 2
# Thread-1: 3
# Thread-1: 4
# Thread-1: 5
# Thread-1: 6
# Thread-1: 7
# Thread-1: 8
# Thread-1: 9
# MainThread: tasks are not done
# MainThread: tasks are done
# Thread-1: looooooooooong
# Thread-1: end
