import unittest
import test_inside
from BeautifulReport import BeautifulReport

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("开始单元测试：")

    def tearDown(self):
        print("测试结束")

    def test_self(self):
        print("测试orig.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_add.txt', 'ans.txt')

    def test_add(self):
        print("正在载入orig_0.8_add.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_add.txt', 'ans.txt')

    def test_del(self):
        print("正在载入orig_0.8_del.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_del.txt', 'ans.txt')
    def test_dis_1(self):
        print("正在载入orig_0.8_dis_1.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_1.txt', 'ans.txt')

    def test_dis_3(self):
        print("正在载入orig_0.8_dis_3.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_3.txt', 'ans.txt')

    def test_dis_7(self):
        print("正在载入orig_0.8_dis_7.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_7.txt', 'ans.txt')

    def test_dis_10(self):
        print("正在载入orig_0.8_dis_10.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_10.txt', 'ans.txt')

    def test_dis_15(self):
        print("正在载入orig_0.8_dis_15.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_15.txt', 'ans.txt')

    def test_mix(self):
        print("正在载入orig_0.8_mix.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_mix.txt', 'ans.txt')

    def test_rep(self):
        print("正在载入orig_0.8_rep.txt")
        test_inside.test('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_rep.txt', 'ans.txt')
'''
    def test_rep_NoChineseError(self):
        print("正在载入orig_NoChinese.txt")
        test_as_function.solve_tfidf('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_rep.txt', 'ans.txt')
    def test_rep_TextSameError(self):
        print("正在载入")
    def test_something(self):
        self.assertEqual(True, False)
'''


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_self'))
    suite.addTest(MyTestCase('test_add'))
    suite.addTest(MyTestCase('test_del'))
    suite.addTest(MyTestCase('test_dis_1'))
    suite.addTest(MyTestCase('test_dis_3'))
    suite.addTest(MyTestCase('test_dis_7'))
    suite.addTest(MyTestCase('test_dis_10'))
    suite.addTest(MyTestCase('test_dis_15'))
    suite.addTest(MyTestCase('test_mix'))
    suite.addTest(MyTestCase('test_rep'))
    runner = BeautifulReport(suite)
    runner.report\
    (
        description = "论文查重单元测试报告", #报告描述
        filename = 'sim_vsm.html', #生成的报告文件名
        log_path = '.'  #报告路径
    )

