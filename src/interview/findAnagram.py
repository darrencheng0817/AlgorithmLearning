'''
Created on 2015年12月1日
给定字符串A，B， 判断A中是否存在子串是B的anagram
@author: Darren
'''
def findAnagram(a,b):
    db={}
    for char in b:
        if char in db:
            db[char]+=1
        else:
            db[char]=1
    index=0
    da={}
    while index<len(b):
        char=a[index]
        if char in da:
            da[char]+=1
        else:
            da[char]=1
        index+=1
    while index<len(a):
        if da==db:
            return index-len(b)
        if a[index]!=a[index-len(b)]:
            if da[a[index-len(b)]]==1:
                da.pop(a[index-len(b)])
            else:
                da[a[index-len(b)]]-=1
            if a[index] in da:
                da[a[index]]+=1
            else:
                da[a[index]]=1
        index+=1
        
a="ajdhgkajhg"
b="hdkg"
print(findAnagram(a, b))