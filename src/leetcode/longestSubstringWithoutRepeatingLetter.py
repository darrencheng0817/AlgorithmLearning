'''
Created on 2015Äê10ÔÂ24ÈÕ

@author: Darren
'''


def lengthOfLongestSubstring(s):
    myset=set()
    start , end , res= 0 , 0 , 0
    while end<len(s):
        if(s[end] in myset):
            res=max(res,end-start)
            while s[start]!=s[end]:
                myset.remove(s[start])
                start+=1
            start+=1
        else:
            myset.add(s[end])
        end+=1
    return max(res,end-start)

print(lengthOfLongestSubstring("aadshgklsjdghkj"))
