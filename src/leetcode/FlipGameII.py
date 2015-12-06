from timeit import Timer

_memo={}
def canWin( s):
    """
    :type s: str
    :rtype: bool
    """
    
    memo = _memo
    if s not in memo:
        memo[s]=False
        for i in range(len(s)-1):
            if s[i]=='+' and s[i+1]=='+':
                temp=s[:i]+'--'+s[i+2:]
                if not canWin(temp):
                    memo[s] = True
        
    return memo[s]

def canWin2(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s or len(s)<2:
        return False
    for i in range(len(s)-1):
        if s[i]=='+' and s[i+1]=='+':
            temp=s
            s=s[:i]+'--'+s[i+2:]
            if not canWin2(s):
                return True
            s=temp
    return False
ss='+++++++++++++++++++++++'
def mytest1():
    canWin(ss)
def mytest2():
    canWin2(ss)
print(canWin(ss))
print(canWin2(ss))
t1=Timer('mytest1()', 'from __main__ import mytest1')
t2=Timer('mytest2()', 'from __main__ import mytest2')

print(t1.timeit(100))
print(t2.timeit(100))