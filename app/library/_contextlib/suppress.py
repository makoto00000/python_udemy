import contextlib
import os

# try exceptによる書き方
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass


# suppressを使った書き方
with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')
