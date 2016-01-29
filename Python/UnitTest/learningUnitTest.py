'''
Created on 2016年1月28日

@author: Darren
'''

import unittest


class Solution(object):
    def doubleNum(self,num):
        return num*2


class TestSolution(unittest.TestCase):
    def test_none_0(self):
        num=213
        self.assertEqual(num*2, Solution.doubleNum(self,num),"?")


if __name__ == "__main__":
    unittest.main()
