'''
Created on 2015年12月1日
https://leetcode.com/problems/find-median-from-data-stream/
@author: Darren
'''
import heapq

class StreamMedian(object):
    pass

streamMedian=StreamMedian()

while True:
    string=input()
    if string=="exit":
        break
    num=int(string)
    print(streamMedian.insertNum(num))