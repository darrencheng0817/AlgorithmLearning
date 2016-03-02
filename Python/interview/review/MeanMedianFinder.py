'''
Created on 2016年3月1日

@author: Darren
'''
import unittest
class MeanMedianFinder(object):
    def __init__(self):
        self.sum=0
        self.count=0
        self.nums=[0]*1000
    
    def insert(self,value):
        self.sum+=value
        self.count+=1
        self.nums[value]+=1
        
    def getMean(self):
        if self.count==0:
            raise Exception("No data inserted!")
        return self.sum/self.count

    def getMedian(self):
        if self.count==0:
            raise Exception("No data inserted!")
        index,num_count=0,0
        num1,num2=-1,-1
        while index<len(self.nums):
            num_count+=self.nums[index]
            if num_count>=self.count//2 and num1==-1:
                num1=index
            if num_count>=self.count//2+1 and num2==-1:
                num2=index
            if num1!=-1 and num2!=-1:
                break
            index+=1
        if self.count&1==0:
            return (num1+num2)/2
        else:
            return num2
        
meanMedianFinder=MeanMedianFinder()        
nums=[]
for num in nums:
    meanMedianFinder.insert(num)
    print("Mean:",meanMedianFinder.getMean())
    print("Median",meanMedianFinder.getMedian())
    
class FinderTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.meanMedianFinder=MeanMedianFinder()
        
    def test_median(self):
        testCase=[2,4,6]
        expectedResult=[2,3,4]
        actualResult=[]
        for num in testCase:
            self.meanMedianFinder.insert(num)
            actualResult.append(self.meanMedianFinder.getMedian())
        self.assertEqual(expectedResult,actualResult)
          
finderTest=FinderTest()   
unittest.main()

        