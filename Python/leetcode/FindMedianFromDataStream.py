'''
Created on 1.12.2016

@author: Darren
''''''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
Examples: 
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5 


Design a data structure that supports the following two operations:


void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.



For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2


Credits:Special thanks to @Louis1992 for adding this problem and creating all test cases." 
'''
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

nums=[1,2,3,4,5,6]
mf=MedianFinder()
for num in nums:
    mf.addNum(num)
    print(mf.findMedian())
    