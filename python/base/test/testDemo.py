# test_calc.py
import unittest  # 导入模块
from calc import add # 是一种从模块中导入特定函数、类或变量的方式

class TestCalc(unittest.TestCase):

    def setUp(self):
        # 在每个测试前运行的代码
        self.a = 1
        self.b = 2

    #跳过某个测试。
    @unittest.skip("Skipping this test.")
    def test_example(self):
        self.assertEqual(1, 2)
    def test_add(self):
        # 测试加法函数
        self.assertEqual(add(1, 2), 3)  # 断言 1 + 2 == 3
        self.assertEqual(add(-1, 1), 0)  # 断言 -1 + 1 == 0
        self.assertEqual(add(0, 0), 0)   # 断言 0 + 0 == 0

    def test_add_with_negative(self):
        # 测试带负数的加法
        self.assertEqual(add(-1, -1), -2)  # 断言 -1 + (-1) == -2
        self.assertEqual(add(-1, 1), 0)    # 断言 -1 + 1 == 0

    def tearDown(self):
        # 在每个测试后运行的代码
        print("Test completed.")

if __name__ == '__main__':
    unittest.main()
