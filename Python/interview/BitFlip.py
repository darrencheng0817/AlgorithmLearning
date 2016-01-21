'''
Created on 2016年1月20日

@author: Darren
'''
'''
1. 给一个0， 1数组，然后允许做之多一次的flip操作。flip操作指的是将一个区间内的0变成1,1变成0。问数组变化后最多可能有多少个1。
   举例：
   输入：
   8     // 数组长度
   1 0 0 1 0 0 1 0    // 变化前数组
   输出：
   6. 
   解释： 可以在[1,5]区间做flip 变成 1 1 1 0 1 1 1 0，也可以做[1, 7]区间做flip变成1 1 1 0 1 1 0 1，所以具体的方案不重要，重点试求最多可能的1的个数


'''
def  bitFlip( arr):
    if not arr or len(arr)<1:
        return 0
    count1,count0=0,0
    max0=0
    for num in arr:
        if num==1:
            count1+=1
            count0-=1
        else:
            count0+=1
        if count0<0:
            count0=0
        max0=max(max0,count0)
    return count1+max0
print(bitFlip([0,0]))