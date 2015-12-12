'''
Created on 2015年12月11日
https://leetcode.com/problems/ugly-number/
https://leetcode.com/problems/ugly-number-ii/
https://leetcode.com/problems/super-ugly-number/
@author: Darren
'''
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''
def isUlgyNumber(num):
    if not num:
        return False
    if num==1:
        return True
    if num%2==0:
        return isUlgyNumber(num//2)
    if num%3==0:
        return isUlgyNumber(num//3)
    if num%5==0:
        return isUlgyNumber(num//5)
    return False

print(isUlgyNumber(14))

'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
'''

def ulgyNumber(N):
    if N<1:
        raise Exception("Invalid Input")
    if N==1:
        return 1
    res=[1]*N
    count=[0]*3
    primes=[2,3,5]
    for i in range(1,N):
        nextNum=min([prime*res[count[j]] for j,prime in enumerate(primes)])
        for j,prime in enumerate(primes):
            if nextNum==prime*res[count[j]]:
                count[j]+=1
        res[i]=nextNum
    return res

print(ulgyNumber(10))

'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
'''
def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    if n==1:
        return 1
    res=[1]*n
    count=[0]*len(primes)
    for __index in range(1,n):
        nextNum=min([prime*res[count[index]] for index,prime in enumerate(primes)])
        for index,prime in enumerate(primes):
            if nextNum==prime*res[count[index]]:
                count[index]+=1
        res[__index]=nextNum
    return res[-1] 
    
n=200000
primes=[2,3,5,13,19,29,31,41,43,53,59,73,83,89,97,103,107,109,127,137,139,149,163,173,179,193,197,199,211,223,227,229,239,241,251,257,263,269,271,281,317,331,337,347,353,359,367,373,379,389,397,409,419,421,433,449,457,461,463,479,487,509,521,523,541,547,563,569,577,593,599,601,613,619,631,641,659,673,683,701,709,719,733,739,743,757,761,769,773,809,811,829,857,859,881,919,947,953,967,971]
print(nthSuperUglyNumber(n, primes))