import unittest
import calculation

release_name = 'lesson'


class CalTest(unittest.TestCase):
    # 各テストの前に実行
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    # 各テストの後に実行
    def tearDown(self):
        print('clean up')

    # テストをスキップする場合
    # @unittest.skip('skip!')
    @unittest.skipIf(release_name == 'lesson', 'skip!')
    def test_add_num_and_double(self):
        self.assertEqual(
            self.cal.add_num_and_double(1, 1), 4)

    # 例外処理のテスト
    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '2')


if __name__ == "__main__":
    unittest.main()
