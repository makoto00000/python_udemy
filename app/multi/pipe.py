import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def f(conn):
    conn.send(['test'])  # ['test']を送る
    time.sleep(2)
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    logging.info(child_conn.recv())  # sendされた値を受け取る
