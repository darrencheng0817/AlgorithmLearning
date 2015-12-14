'''
Created on 2015年12月1日
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

https://leetcode.com/problems/search-in-rotated-sorted-array/
@author: Darren
'''
'''
public class Solution {
    public boolean search(int[] A, int target) {
        int first = 0, last=A.length-1;
        while (first <= last) {
            int mid =(first+last)/2;
            if (A[mid] == target)
                return true;
            if (A[first] < A[mid]) {
                if (A[first] <= target && target < A[mid])
                    last = mid-1;
                else
                    first = mid + 1;
            } else if(A[first]>A[mid]) {
                if (A[mid] < target && target <= A[last])
                    first = mid + 1;
                else
                    last = mid-1;
            }
            else
                first++;
        }
        return false;        
    }
}
'''
def search(nums,target):
    pass

nums=[5,6,7,8,9,1,2,3,4]
print(search(nums, 4))
