'''
Created on 2016年2月9日

@author: Darren
'''
'''
Dual Palindromes
Mario Cruz (Colombia) & Hugo Rickeboer (Argentina)
A number that reads the same from right to left as when read from left to right is called a palindrome. The number 12321 is a palindrome; the number 77778 is not. Of course, palindromes have neither leading nor trailing zeroes, so 0220 is not a palindrome.

The number 21 (base 10) is not palindrome in base 10, but the number 21 (base 10) is, in fact, a palindrome in base 2 (10101).

Write a program that reads two numbers (expressed in base 10):

N (1 <= N <= 15)
S (0 < S < 10000)
and then finds and prints (in base 10) the first N numbers strictly greater than S that are palindromic when written in two or more number bases (2 <= base <= 10).
Solutions to this problem do not require manipulating integers larger than the standard 32 bits.

PROGRAM NAME: dualpal

INPUT FORMAT

A single line with space separated integers N and S.

SAMPLE INPUT (file dualpal.in)

3 25
OUTPUT FORMAT

N lines, each with a base 10 number that is palindromic when expressed in at least two of the bases 2..10. The numbers should be listed in order from smallest to largest.
SAMPLE OUTPUT (file dualpal.out)

26
27
28
'''
def convert(num,base):
    res=""
    while num>0:
        temp=num%base
        if temp>9:
            res=chr(ord("A")-10+temp)+res
        else:
            res=str(temp)+res
        num//=base
    return res

def dualpal(N,S):
    res=[]
    while len(res)<N:
        S+=1
        count=0
        for base in range(2,11):
            cand=convert(S, base)
            if cand==cand[::-1]:
                count+=1
            if count>=2:
                res.append(S)
                break
    print(res)
    
dualpal(15, 9900)