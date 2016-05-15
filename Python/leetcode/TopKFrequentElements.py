'''
Created on 2016年5月1日

@author: Darren
'''
'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for num in nums:
            if num not in d:
                d[num]=0
            d[num]+=1
        return sorted(d.keys(),key=lambda x:d[x],reverse=True)[:k]