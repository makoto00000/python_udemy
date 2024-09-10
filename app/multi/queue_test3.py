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
    for i in range(100):
        queue.put(i)
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue, ))
        t.start()
        ts.append(t)
    logging.debug('tasks are not done')
    queue.join()  # task_done()を待つ
    logging.debug('tasks are done')
    for _ in range(len(ts)):
        queue.put(None)  # whileをbreakするため

    [t.join() for i in ts]

# thread3つで100個のタスクを並列処理する。

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
# Thread-1: 10
# Thread-1: 11
# Thread-1: 12
# Thread-1: 13
# Thread-1: 14
# Thread-1: 15
# Thread-1: 16
# Thread-2: start
# Thread-2: 18
# Thread-3: start
# Thread-3: 20
# Thread-3: 21
# Thread-1: 17
# Thread-1: 23
# Thread-1: 24
# Thread-1: 25
# Thread-1: 26
# MainThread: tasks are not done
# Thread-3: 22
# Thread-3: 28
# Thread-2: 19
# Thread-2: 30
# Thread-3: 29
# Thread-3: 32
# Thread-2: 31
# Thread-2: 34
# Thread-2: 35
# Thread-2: 36
# Thread-2: 37
# Thread-2: 38
# Thread-1: 27
# Thread-1: 40
# Thread-1: 41
# Thread-1: 42
# Thread-2: 39
# Thread-3: 33
# Thread-3: 45
# Thread-3: 46
# Thread-3: 47
# Thread-2: 44
# Thread-1: 43
# Thread-2: 49
# Thread-2: 51
# Thread-2: 52
# Thread-2: 53
# Thread-3: 48
# Thread-3: 55
# Thread-3: 56
# Thread-1: 50
# Thread-3: 57
# Thread-3: 59
# Thread-3: 60
# Thread-1: 58
# Thread-3: 61
# Thread-3: 63
# Thread-2: 54
# Thread-2: 65
# Thread-2: 66
# Thread-3: 64
# Thread-3: 68
# Thread-3: 69
# Thread-3: 70
# Thread-3: 71
# Thread-3: 72
# Thread-3: 73
# Thread-2: 67
# Thread-2: 75
# Thread-1: 62
# Thread-3: 74
# Thread-2: 76
# Thread-2: 79
# Thread-3: 78
# Thread-1: 77
# Thread-1: 82
# Thread-1: 83
# Thread-1: 84
# Thread-1: 85
# Thread-3: 81
# Thread-3: 87
# Thread-1: 86
# Thread-1: 89
# Thread-1: 90
# Thread-3: 88
# Thread-3: 92
# Thread-2: 80
# Thread-1: 91
# Thread-3: 93
# Thread-2: 94
# Thread-2: 97
# Thread-1: 95
# Thread-3: 96
# Thread-2: 98
# Thread-1: 99
# MainThread: tasks are done
# Thread-3: looooooooooong
# Thread-2: looooooooooong
# Thread-1: looooooooooong
# Thread-1: end
# Thread-3: end
# Thread-2: end
