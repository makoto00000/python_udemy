# 並列化

同時に並行して処理を実行したいときに使う。

## Thread

メモリ、コアは一つで、スレッドのみが分かれている。

- [スレッドの基礎](./thread.py)
- [スレッドをデーモン化](./daemon.py)
- [スレッドの一覧を取得](./thread_list.py)
- [スレッドの開始時間を操作する](./timer.py)
- [スレッドが走るタイミングを操作する](./lock.py)
- [同時にロックをかける数を操作する](./semaphore.py)
- [実行するスレッドをqueueで管理する](./queue_test.py)
- [実行する回数を指定する](./queue_test2.py)
- [3つのスレッドで100個のタスクを並列処理](./queue_test3.py)
- [指示があるまで待つ](./event.py)
- [実行する順番を操作する](./condition.py)
- [n回以上の許可を待って実行する](./barrier.py)

## MultiProcess

メモリ、プロセス、コア全てが分かれている。

- [マルチプロセスの基礎](./process.py)
- [同時に実行できるプロセス数を制御する（Semaphoreみたい）](./pool.py)
- [poolの前に必ず入れたい処理がある](./pool_block.py)
- [複数のプロセスを1行で書く](./pool_map.py)
- [mainとworker間で値をやりとり](./pipe.py)
- [各プロセス間で共通の値、配列を使う](./value_array.py)
- [速度を落としても良いのでpythonオブジェクトのように値をやり取りしたい](./manager.py)
- [クラサバ間で値をやりとりする](./basemanager)
- [単純な並列化だけ実装したい、Threadまたはmultiprocessに変更される可能性がある](./concurrent_futures.py)
