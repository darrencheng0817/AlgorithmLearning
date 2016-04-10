'''
Created on 2016年2月29日

@author: Darren
'''
class My_DS:
    def __init__(self):
        self.sum=0
        self.count=0
        self.data=[0]*1001
    
    def add(self,num):
        self.sum+=num
        self.count+=1
        self.data[num]+=1
        
    def get_mean(self):
        if self.count==0:
            return "Empty"
        return self.sum/self.count
    
    def get_median(self):
        if self.count==0:
            return "Empty"
        num1,num2=-1,-1
        count,index=0,0
        while index<len(self.data):
            count+=self.data[index]
            if count>=self.count//2 and num1==-1:
                num1=index
            if count>=self.count//2+1 and num2==-1:
                num2=index
            if num1!=-1 and num2!=-1:
                break
            index+=1
        if self.count&1==0:
            return (num1+num2)/2
        else:
            return num2
        
from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0        
        
nums=[5,15,1,3]
so=My_DS()
for index,num in enumerate(nums):
    so.add(num)
    print(index)
    print("mean",so.get_mean())
    print("median",so.get_median())        