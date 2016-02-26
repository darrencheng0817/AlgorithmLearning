'''
Created on 2016年2月24日

@author: Darren
'''
def sort(nums):
    index_p=0
    for index,num in enumerate(nums):
        if num>=0:
            nums[index_p],nums[index]=nums[index],nums[index_p]
            index_p+=1
    return nums

def sort2(nums):
    index_p=0
    index=0
    while index<len(nums):
        if nums[index]>=0:
            temp=nums[index]
            nums.pop(index)
            nums.insert(index_p,temp)  
            index_p+=1
        index+=1
    return nums
nums=[1,2,-3,4,3,2,0,-1,-3,-5,1,-4,5]
print(sort(nums))
nums=[-2,1,2,-3,4,3,2,0,-1,-3,-5,1,-4,5]
print(sort2(nums))
