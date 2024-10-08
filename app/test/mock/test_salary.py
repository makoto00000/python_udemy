import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    # デコレーターを使う場合
    # 上記のような関数内でmockを作るような書き方だと、mockを作成せずに呼び出してしまうかもしれない
    # そこであらかじめmockを使うことを明示する方が良い。
    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', return_value=1)
    # mock_bonusという引数でデコレーターを受け取る
    def test_calculation_salary_patch(self, mock_bonus):
        # mock_bonus.return_value = 1 と書いても良い

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    # withを使う場合
    def test_calculation_salary_patch_with(self):
        with mock.patch(
                'salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    # patcherを使う場合（関数ごとにmockを作る必要がなくなる）
    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary_patch_patcher(self):
        self.mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

    # side effect 複雑な処理で値を返したい場合
    def test_calculation_salary_patch_side_effect(self):
        # def f(year):
            # return year
        # self.mock_bonus.side_effect = f(1)
        # lambdaで1行で書ける
        # self.mock_bonus.side_effect = lambda year: 1
        # s = salary.Salary(year=2017)
        # salary_price = s.calculation_salary()
        # self.assertEqual(salary_price, 101)

        # APIでエラーになったときのテスト
        # self.mock_bonus.side_effect = ConnectionRefusedError
        # s = salary.Salary(year=2017)
        # salary_price = s.calculation_salary()
        # self.assertEqual(salary_price, 100)

        # 1回目に呼ばれたとき1を返す、2回目は2...
        self.mock_bonus.side_effect = [
          1,
          2,
          3,
          ValueError('Bankrupt!!!')
        ]
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 101)
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 102)
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 103)
        s = salary.Salary(year=200)
        with self.assertRaises(ValueError):
            s.calculation_salary()

    # spec（クラスごとmock化。メソッドが何を返すかをテスト関数内で定義する）
    @mock.patch('salary.ThirdPartyBonusRestApi', spec=True)
    @mock.patch('salary.Salary.get_from_boss')
    def test_calculation_salary_class(self, mock_boss, mock_rest):
        # mock_rest = MockRest()  # この場合は引数をMockRestとする
        # 上と同じ意味（下は分かりにくいが公式の書き方）
        # 右辺のmock_restは引数の方
        mock_rest = mock_rest.return_value
        mock_rest.bonus_price.return_value = 1
        mock_rest.get_api_name.return_value = 'Money'

        mock_boss.return_value = 10

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 111)
        mock_rest.bonus_price.assert_called()


if __name__ == '__main__':
    unittest.main()

# mockは自分で定義したメソッドに対しても書くことはできるが、外部APIに関するものや、未完成のものに対して書くのが一般的。全てmock化するようなコードだと、テストコードで間違えたmockを作ると、本来のコードは間違っていないのに、テストコードにバグが発生しているという状況になってしまう。
