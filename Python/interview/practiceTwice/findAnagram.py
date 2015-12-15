'''
Created on 2015年12月1日
给定字符串A，B， 判断A中是否存在子串是B的anagram
@author: Darren
'''
def findAnagram(a,b):
    diff={}
    for char in a:
        if char not in diff:
            diff[char]=0
        diff[char]+=1
    index=0
    while index<len(a)-1:
        char=b[index]
        if char not in diff:
            diff[char]=0
        diff[char]-=1
        if diff[char]==0:
            diff.pop(char)
        index+=1
    res=[]
    while index<len(b):
        char=b[index]
        if char not in diff:
            diff[char]=0
        diff[char]-=1
        if diff[char]==0:
            diff.pop(char)
        index+=1
        startIndex=index-len(a)
        if len(diff)==0:
            res.append(startIndex)
        char=b[startIndex]
        if char not in diff:
            diff[char]=0
        diff[char]+=1
        if diff[char]==0:
            diff.pop(char)
    return res
a="ajdhgkajhgkd"
b="hdkg"
print(findAnagram(b, a))