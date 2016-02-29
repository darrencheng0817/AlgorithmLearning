'''
Created on 1.12.2016

@author: Darren
''''''

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].



You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.



Return the starting gas station s index if you can travel around the circuit once, otherwise return -1.



Note:
The solution is guaranteed to be unique.
" 
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost or len(gas)!=len(cost):
            return -1
        pointer,total=0,0
        local_sum=0
        for index in range(len(gas)):
            total+=gas[index]-cost[index]
            local_sum+=gas[index]-cost[index]
            if local_sum<0:
                local_sum=0
                pointer=index+1
        return pointer if total>=0 else -1
        