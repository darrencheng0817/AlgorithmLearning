'''
Created on 2016年1月18日

@author: Darren
'''
'''
一堆string，找到其中最长的可以用其他string构成的那个string，例如 {hello, foo, bar, disney, funny, world, foobar, disneyworld} 返回disneyworld.
'''
def check(string,stringSet):
    stringSet.remove(string)
    dp=[False]*(len(string)+1)
    dp[0]=True
    for i in range(len(string)):
        for j in range(i):
            if dp[j] and string[j:i+1] in stringSet:
                dp[i+1]=True
                break
    return dp[-1]

def getLongestString(strings):
    strings=sorted(strings, key=lambda x:-len(x))
    stringSet=set(strings)
    for string in strings:
        if check(string,stringSet):
            return string
    return None
    

strings=['hello','foo','bar', 'disney', 'funny', 'world', 'foobar', 'disneyworld']
print(getLongestString(strings))