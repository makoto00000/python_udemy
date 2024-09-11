import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')


def f(num, arr):
    logging.debug(num)
    num.value += 1.0
    logging.debug(arr)
    for i in range(len(arr)):  # 配列として扱えないのでこの書き方
        arr[i] *= 2


if __name__ == '__main__':
    num = multiprocessing.Value('f', 0.0)  # 各プロセス間で共通の値
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])

    p1 = multiprocessing.Process(target=f, args=(num, arr))
    p2 = multiprocessing.Process(target=f, args=(num, arr))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    logging.debug(num.value)
    logging.debug(arr[:])
