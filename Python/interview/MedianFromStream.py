'''
Created on 2015年12月1日
https://leetcode.com/problems/find-median-from-data-stream/
@author: Darren
'''
import heapq

class StreamMedian(object):
    def __init__(self):       
        self.minHeap=[]
        self.maxHeap=[]
    
    def insertNum(self,num):
        if len(self.maxHeap)>len(self.minHeap):
            tempNum=heapq.heappushpop(self.maxHeap, num)
            heapq.heappush(self.minHeap, -tempNum)
            return (self.maxHeap[0]-self.minHeap[0])/2
        else:
            heapq.heappush(self.maxHeap, num)
            return self.maxHeap[0]

streamMedian=StreamMedian()

while True:
    string=input()
    if string=="exit":
        break
    num=int(string)
    print(streamMedian.insertNum(num))