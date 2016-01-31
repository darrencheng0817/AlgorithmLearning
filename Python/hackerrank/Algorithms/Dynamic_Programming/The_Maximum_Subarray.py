'''
Created on 2016年1月30日

@author: Darren
'''
'''
Given an array A={a1,a2,…,aN} of N elements, find the maximum possible sum of a

1.Contiguous subarray
2.Non-contiguous (not necessarily contiguous) subarray.

Empty subarrays/subsequences should not be considered.

This Youtube video by Ben Wright might be useful to understand the Kadane algorithm for the maximum subarray in a 1-D sequence.


Input Format

First line of the input has an integer T. T cases follow. 
Each test case begins with an integer N. In the next line, N integers follow representing the elements of array A.

Constraints:

1≤T≤10
1≤N≤105
−104≤ai≤104
The subarray and subsequences you consider should have at least one element.

Output Format

Two, space separated, integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).

Sample Input

2 
4 
1 2 3 4
6
2 -1 2 3 4 -5
Sample Output

10 10
10 11
Explanation

In the first case: 
The max sum for both contiguous and non-contiguous elements is the sum of ALL the elements (as they are all positive).

In the second case: 
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum. 
For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.
'''
def getMaxSubarray(nums):
    res1,res2=0,0
    local=0
    maxNum=max(nums)
    if maxNum<0:
        return [maxNum,maxNum]
    for num in nums:
        local+=num
        if local<0:
            local=0
        res1=max(res1,local)
        if num>0:
            res2+=num
    return [res1,res2]

caseNum=int(input())
for caseIndex in range(caseNum):
    line1=input()
    line2=input().strip().split(" ")
    nums=[int(_) for _ in line2]
    print(" ".join([str(_) for _ in getMaxSubarray(nums)]))