'''
Created on 2015年12月10日

@author: Darren
'''

global count
count=0
def mergeSort(nums):
    if len(nums)<=1:
        return nums
    m=len(nums)//2
    return merge(mergeSort(nums[:m]),mergeSort(nums[m:]))

def merge(nums1,nums2):
    index1,index2=0,0
    res=[]
    global count
    while index1<len(nums1) and index2<len(nums2):
        if nums1[index1]>nums2[index2]:
            count+=len(nums1)-index1
            res.append(nums2[index2])
            index2+=1
        else:
            res.append(nums1[index1])
            index1+=1
    for i in range(index1,len(nums1)):
        res.append(nums1[i])
    for i in range(index2,len(nums2)):
        res.append(nums2[i])
    return res

nums=[2,1]
print(mergeSort(nums))
print(count)
    