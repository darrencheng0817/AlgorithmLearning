'''
Created on 2016年1月28日

@author: Darren
'''

import unittest


class Solution(object):
    def doubleNum(self,num):
        return num*2


class TestSolution(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.testClass=Solution()
    def test_none_0(self): #test function name should start with test
        num=213
        self.assertEqual(num*2, self.testClass.doubleNum(num),"Fail")


if __name__ == "__main__":
    unittest.main()
