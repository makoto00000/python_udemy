import os
import pytest


# 独自のfixtureを定義
@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('before test')
        yield c
        print('after test')


def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')

# pytest test/pytest_test.py --help
