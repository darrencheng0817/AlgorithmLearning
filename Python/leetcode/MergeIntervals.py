'''
Created on 1.12.2016

@author: Darren
''''''
Given a collection of intervals, merge all overlapping intervals.


For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
" 
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        res=[]
        intervals=sorted(intervals,key=lambda x:x.start)
        res.append(intervals.pop(0))
        for interval in intervals:
            if interval.start<=res[-1].end:
                res[-1].end=max(res[-1].end,interval.end)
            else:
                res.append(interval)
        return res