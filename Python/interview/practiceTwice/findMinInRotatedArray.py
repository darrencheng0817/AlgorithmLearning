'''
Created on 2015年12月1日

@author: Darren
'''
def findMinInRotatedArray(nums):
    pass
def findMinIndexInRotatedArray(nums):
    pass
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
