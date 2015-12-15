'''
Created on 2015年12月1日

@author: Darren
'''
def findMinInRotatedArray(nums):
    if not nums:
        return 
    l,r=0,len(nums)-1
    res=nums[0]
    while l<r-1:
        m=(l+r)//2
        if nums[l]<nums[m]:
            res=min(res,nums[l])
            l=m+1
        elif nums[l]>nums[m]:
            res=min(res,nums[m])
            r=m-1
        else:
            l+=1
    res=min(res,nums[l],nums[r])
    return res

def findMinIndexInRotatedArray(nums):
    if not nums:
        return -1
    l,r=0,len(nums)-1
    res=0
    while l<r-1:
        m=(l+r)//2
        if nums[l]<nums[m]:
            if nums[l]<nums[res]:
                res=l
            l=m+1
        elif nums[l]>nums[m]:
            if nums[m]<nums[res]:
                res=m
            r=m-1
        else:
            l+=1
    if nums[l]<nums[res]:
        res=l
    if nums[m]<nums[res]:
        res=m
    return res
nums=[5,6,7,8,0,1,2,3,4]
print(findMinInRotatedArray(nums))
index=findMinIndexInRotatedArray(nums)
print(index)
res=list(nums)
res.reverse()
firstPart=res[:len(res)-index]
secondPart=res[len(res)-index:]
firstPart.reverse()
secondPart.reverse()
res=firstPart+secondPart
print(res)
