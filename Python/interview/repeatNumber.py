'''
Created on 2015年12月1日
给你一个数组，range［1，n］inclusive，然后说如果有个n＋1的数组的话这里面有没
有重复？为什么？
然后followup：怎么找到那个重复的数字？有可能有多个重复
继续followup；如果说不让你交换数字，即不能排序怎么办？可以用空间.
继续followup：如果说没有空间怎么办？
@author: Darren
'''


def findDup(nums):
    if not nums:
        raise Exception("Invalid input!")
    slowP=nums[0]
    fastP=nums[0]
    while True:
        fastP=nums[nums[fastP]]
        slowP=nums[slowP]
        if fastP==slowP:
            break
    fastP=nums[0]
    while fastP!=slowP:
        fastP=nums[fastP]
        slowP=nums[slowP]
    return nums[slowP]

nums=[1,2,3,4,5,5,6,7,8]
print(findDup(nums))