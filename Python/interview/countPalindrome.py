'''
Created on 2016年1月15日

@author: Darren
'''
def  palindrome(string):
    if not str or len(string)==0:
        return 0
    s=set()
    dp=[[False] * len(string) for _ in range(len(string))]
    for i in range(len(string)):
        dp[i][i]=True
        if i>0 and string[i]==string[i-1]:
            dp[i-1][i]=True
    for length in range(3,len(string)+1):
        for i in range(len(string)-length+1):
            j=i+length-1
            if dp[i+1][j-1] and string[i]==string[j]:
                dp[i][j]=True
    count=0
    for i in range(len(string)):
        for j in range(i,len(string)):
            if dp[i][j]:
                count+=1
                s.add(string[i:j+1])
    print(count)
    return len(s)

def  count_palindromes( S):
    if not S:
        return 0
    res=0
    for index in range(len(S)):
        shift=0
        while index-shift>=0 and index+shift<len(S):
            if S[index-shift]==S[index+shift]:
                res+=1
            else:
                break
            shift+=1
        shift=0
        if index>0:
            while index-shift-1>=0 and index+shift<len(S):
                if S[index-shift-1]==S[index+shift]:
                    res+=1
                else:
                    break
                shift+=1
    return res
    

string="aaaaaaaaaaaaaaaaadddddddddddddddddd"
print(count_palindromes(string))
print(palindrome(string))

