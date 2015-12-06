def searchRange( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res=[-1,-1]
    l,r=0,len(nums)-1
    while l<=r:
        m=l+(r-l)//2
        if nums[m]<target:
            l=m+1
        else:
            r=m-1
    res[0]=l
    l,r=0,len(nums)-1
    while l<=r:
        m=l+(r-l)//2
        if nums[m]<=target:
            l=m+1
        else:
            r=m-1
    res[1]=l-1
    return res if res[0]<=res[1] else [-1,-1]
    
print(searchRange([1], 1))