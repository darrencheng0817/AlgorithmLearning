'''
Created on 2015年12月1日

@author: Darren
'''
def check(pair1,pair2):
    i1,j1=pair1
    i2,j2=pair2
    if i1==i2 or j1==j2:
        return False
    if i1==j2 or i2==j1:
        return False
    return True

def fourSum(nums,target):
    if not nums or len(nums)<4:
        raise Exception("Invalid Input!")
    dic={}
    res=set()
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            pairSum=nums[i]+nums[j]
            pair=(i,j)
            if pairSum in dic:
                for candPair in dic[pairSum]:
                    if check(pair,candPair):
                        res.add(",".join([str(temp) for temp in sorted([i,j,candPair[0],candPair[1]])]))
            if target-pairSum not in dic:
                dic[target-pairSum]=[]
            dic[target-pairSum].append(pair)
    return res    
nums=[1,2,3,3,4]
print(fourSum(nums, 10))