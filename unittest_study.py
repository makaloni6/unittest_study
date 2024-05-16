# unittestモジュールのimport
import unittest

# TestCaseクラスの定義
class MyTestCase(unittest.TestCase):
    # テスト実行関数の定義
    # unittest.TestCaseを継承したクラスでtest_~~~のメソッドをテストしてくれる
    def test_test1(self):
        print("hoge")
    def test_test2(self):
        self.assertEqual((10 + 5), 15) # assertEqualはTestCaseクラスの関数なのでself.の形で呼び出す。
    def test_test3(self):
        self.assertNotEqual(1, 15)
    def test_test4(self):
        self.assertTrue(True)
    def test_test4(self):
        self.assertFalse(False)

    def test_test5(self):
        self.assertIn('kiwi', ['apple', 'banana'])

# テストの実行判定
if __name__ == "__main__":
    unittest.main()