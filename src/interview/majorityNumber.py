'''
Created on 2015年12月1日
数组里一个数的出现次数超过数组长度的50%， 找到这个数
@author: Darren
'''

def findMajorityNum(nums):
    if not nums:
        raise Exception("Empty Input!")
    candidate=0
    count=0
    for index in range(len(nums)):
        if count==0:
            candidate=nums[index]
            count+=1
        else:
            if candidate==nums[index]:
                count+=1
            else:
                count-=1
    return candidate