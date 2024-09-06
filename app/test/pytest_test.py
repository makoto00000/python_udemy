import os
import pytest

import calculation

is_release = True


def test_add_num_and_double():
    cal = calculation.Cal()
    assert cal.add_num_and_double(1, 1) == 4


class TestCal(object):
    # このクラスのテスト開始前に実行
    @classmethod
    def setup_class(cls):
        print('test start')
        cls.cal = calculation.Cal()
        cls.test_file_name = 'test.txt'

    # このクラスのテスト終了時に実行
    @classmethod
    def teardown_class(cls):
        print('test end')
        cls.cal = calculation.Cal()

    # 各テストの前に実行
    def setup_method(self, method):
        print('setup method={}'.format(method.__name__))
        # self.cal = calculation.Cal()

    # 各テストの後に実行
    def teardown_method(self, method):
        print('teardown method={}'.format(method.__name__))
        # del self.cal

    # @pytest.mark.skip(reason='skip!')
    # @pytest.mark.skipif(is_release is True, reason='skip!')
    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    # tmpdirで一時的なディレクトリを扱える
    def test_save(self, tmpdir):
        print(tmpdir)  # /tmp/pytest-of-root/pytest-0/test_tmpdir0
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    # withの中でValueエラーが発生するかどうか
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

# 「pytest test/pytest_test.py --os_name=mac -sv」を実行する。

# sオプション print文を表示
# vオプション 詳細表示（skip表示）
