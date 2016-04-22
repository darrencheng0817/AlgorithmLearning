'''
Created on 2015年12月1日

@author: Darren
'''

'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''



class pair(object):
    def __init__(self,indexA,indexB,sum):
        self.indexA=indexA
        self.indexB=indexB
        self.sum=sum

def check(pair1,pair2):
    if pair1.indexA==pair2.indexA or pair1.indexB==pair2.indexB:
        return False
    if pair1.indexA==pair2.indexB or pair1.indexB==pair2.indexA:
        return False
    return True   
def fourSum(nums,target):
    pairs={}
    res=set()
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            tempSum=nums[i]+nums[j]
            tempPair=pair(i,j,tempSum)
            if tempSum in pairs:
                for canPair in pairs[tempSum]:
                    if check(canPair,tempPair):
                        resString=" ".join(str(temp) for temp in sorted([canPair.indexA,canPair.indexB,tempPair.indexA,tempPair.indexB]))
                        res.add(resString)
            if target-tempSum in pairs:
                pairs[target-tempSum].append(tempPair)
            else:
                pairs[target-tempSum]=[tempPair]
    return res       
nums=[1,2,3,3,4]
print(fourSum(nums, 10))
a="adsagga"
print(sorted(a))