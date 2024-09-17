import asyncio
# import time

loop = asyncio.get_event_loop()


# Python 3.5以前の書き方
# @asyncio.coroutine
# def worker():
#     print('start')
#     # time.sleep(2)  これだと並列化できない
#     yield from asyncio.sleep(2)
#     print('stop')


async def worker():
    print('start')
    # time.sleep(2)  これだと並列化できない
    await asyncio.sleep(2)
    print('stop')


if __name__ == '__main__':
    loop.run_until_complete(asyncio.wait([worker(), worker()]))
    loop.close()
