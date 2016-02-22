'''
Created on 1.12.2016

@author: Darren
'''
'''
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
'''
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        min1,min2=0,0
        k1=0
        for i in range(1,len(costs)+1):
            cost=0
            new_k=0
            new_min1,new_min2=float('inf'),float('inf')
            for k in range(len(costs[0])):
                if k==k1:
                    cost=min2+costs[i-1][k]
                else:
                    cost=min1+costs[i-1][k]
                if cost<new_min2:
                    new_min2=cost
                if cost<new_min1:
                    new_min2=new_min1
                    new_min1=cost
                    new_k=k
            k1=new_k
            min1=new_min1
            min2=new_min2
        return min1

so=Solution()
costs=[]
print(so.minCostII(costs))