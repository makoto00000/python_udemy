import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')
    return i * 2


if __name__ == '__main__':
    with multiprocessing.Pool(3) as p:
        m = p.map(worker1, [100, 200])  # 複数のプロセスを1行で実行できる（引数には配列を渡す）
        a = p.map_async(worker1, [100, 200])  # 終わるのを待たずに次の処理が走る
        r = p.imap(worker1, [100, 200])  # ループで表示させたいとき

        logging.debug('executed')

        logging.debug(m)  # [200, 400]
        logging.debug(a)  # multiprocessing.pool.MapResult object  → a.get()で取得
        logging.debug(r)  # multiprocessing.pool.IMapIterator object →forループで取得
        # logging.debug(r.get())
        # logging.debug([i for i in r])
        for i in r:
            logging.debug(i)
