'''
Created on 2015年12月1日
https://leetcode.com/problems/word-break-ii/
只需要返回第一个符合条件的
@author: Darren
'''
def wordBreak(s,d):
    res=[]
    wordBreakUtil(s, d, res, [], 0)
    return res
def wordBreakUtil(s,d,res,item,index):
    if s[index:] in d:
        item.append(s[index:])
        res.append(" ".join(item))
        return
    for i in range(index+1,len(s)):
        if s[index:i] in d:
            wordBreakUtil(s, d, res, item+[s[index:i]], i)
s = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s, d))