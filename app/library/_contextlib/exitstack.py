import contextlib


def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        return True
    except Exception:
        return False


def cleanup1():
    print('clean up 1')


def cleanup2():
    print('clean up 2')


# is_ok_jobの実行結果によってcleanup関数を実行する
# try:
#     is_ok = is_ok_job()
#     print('more task')
# finally:
#     if not is_ok:
#         cleanup()


# ExitStackを用いた書き方
# stackの最後にcleanupを実行する
with contextlib.ExitStack() as stack:
    stack.callback(cleanup1)
    stack.callback(cleanup2)

    @stack.callback  # デコレーターで書くこともできる
    def cleanup3():
        print('clean up 3')

    is_ok = is_ok_job()
    print('more task')

    # cleanupをしなくても良い場合は、最後にstackをクリアする
    if is_ok:
        stack.pop_all()
